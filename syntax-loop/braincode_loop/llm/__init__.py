"""Provider factory. All role code should build clients through get_client() rather than
importing a specific provider client directly, so `run.dry_run` in config.yaml can swap every
role over to DryRunClient with a single flag.

Also provides generate_resilient(), the single choke point every LLM call in the loop should go
through (roles/base_role.py and the kpi/*.py modules that call providers directly) so a transient
outage or a retired model doesn't kill the whole run — see its docstring.
"""
from __future__ import annotations

import logging
import re
import time

from .base import LLMClient, LLMResponse
from .dry_run_client import DryRunClient

logger = logging.getLogger("braincode_loop")

_PROVIDERS = {}

# Transient — worth retrying the *same* model with backoff before giving up on it.
_RETRYABLE_STATUS = {408, 409, 429, 500, 502, 503, 504}
# Not transient — the model itself is gone/renamed (e.g. a retired/deprecated model ID). Retrying
# the same model is pointless; skip straight to the next fallback candidate.
_UNAVAILABLE_STATUS = {404}


def _lazy_providers():
    if not _PROVIDERS:
        from .anthropic_client import AnthropicClient
        from .gemini_client import GeminiClient
        from .openai_client import OpenAIClient

        _PROVIDERS.update(
            {
                "anthropic": AnthropicClient,
                "openai": OpenAIClient,
                "gemini": GeminiClient,
            }
        )
    return _PROVIDERS


def get_client(provider: str, model: str, dry_run: bool = False) -> LLMClient:
    if dry_run:
        return DryRunClient(model=f"dry-run:{provider}:{model}")
    providers = _lazy_providers()
    if provider not in providers:
        raise ValueError(f"Unknown provider {provider!r}. Known: {sorted(providers)} (or dry_run=True)")
    return providers[provider](model=model)


def _status_code(exc: BaseException) -> int | None:
    """Best-effort status code extraction across anthropic/openai (`.status_code`) and
    google-genai (`.code`) SDK exceptions, with a regex fallback over the message for anything
    else (SDKs change their exception shape between versions more often than the HTTP status
    embedded in the error text does)."""
    for attr in ("status_code", "code"):
        val = getattr(exc, attr, None)
        if isinstance(val, int):
            return val
    match = re.search(r"\b([45]\d{2})\b", str(exc))
    return int(match.group(1)) if match else None


def generate_resilient(
    *,
    provider: str,
    model: str,
    system: str,
    user: str,
    max_tokens: int,
    temperature: float,
    use_search_grounding: bool = False,
    dry_run: bool,
    llm_cfg: dict | None = None,
    log_prefix: str = "",
    effort: str | None = None,
) -> tuple[LLMResponse, str]:
    """Call `provider`/`model`, retrying transient failures (429/5xx — e.g. "high demand, try
    again later") with backoff, and falling back to alternate same-provider models
    (config.yaml -> llm.fallback_models) if the primary model is retired/unavailable (404) or
    keeps failing after retries are exhausted. Returns (response, model_actually_used) so callers
    record cost against whichever model actually answered, not necessarily the one requested.

    Fallback is same-provider only, deliberately: role->provider assignments (e.g. Reviewer must
    stay OpenAI, Searcher must stay Gemini) are load-bearing per the project's meeting notes, so
    this never silently switches a role to a different provider.

    A non-transient error (bad request, auth failure, etc.) is raised immediately without
    consuming the fallback chain — switching models can't fix those, so failing fast is more
    useful than churning through every candidate first.
    """
    llm_cfg = llm_cfg or {}
    # Provider-level default (config.yaml -> llm.<provider>.effort); a caller's `effort` wins.
    effort = effort or (llm_cfg.get(provider) or {}).get("effort")
    retry_cfg = llm_cfg.get("retry", {})
    max_attempts = max(1, retry_cfg.get("max_attempts", 3))
    base_backoff = retry_cfg.get("backoff_seconds", 5)

    chain = [model]
    for alt in llm_cfg.get("fallback_models", {}).get(provider, []):
        if alt not in chain:
            chain.append(alt)

    last_exc: Exception | None = None
    for candidate_model in chain:
        for attempt in range(max_attempts):
            try:
                client = get_client(provider, candidate_model, dry_run=dry_run)
                response = client.generate(
                    system=system, user=user, max_tokens=max_tokens, temperature=temperature,
                    use_search_grounding=use_search_grounding, effort=effort,
                )
                if candidate_model != model:
                    logger.warning(
                        "%s%s/%s unavailable — succeeded with fallback model %s.",
                        log_prefix, provider, model, candidate_model,
                    )
                return response, candidate_model
            except Exception as exc:  # noqa: BLE001 - each provider SDK raises its own hierarchy
                last_exc = exc
                status = _status_code(exc)
                if status in _UNAVAILABLE_STATUS:
                    logger.warning(
                        "%s%s/%s: %s (status=%s) — model unavailable, trying next fallback "
                        "candidate instead of retrying.", log_prefix, provider, candidate_model, exc, status,
                    )
                    break  # no point retrying a model that doesn't exist; try the next candidate
                if status in _RETRYABLE_STATUS and attempt < max_attempts - 1:
                    delay = base_backoff * (2 ** attempt)
                    logger.warning(
                        "%s%s/%s: %s (status=%s) — transient, retrying in %ss (attempt %d/%d).",
                        log_prefix, provider, candidate_model, exc, status, delay, attempt + 1, max_attempts,
                    )
                    time.sleep(delay)
                    continue
                if status in _RETRYABLE_STATUS:
                    logger.warning(
                        "%s%s/%s: %s (status=%s) — retries exhausted, trying next fallback candidate.",
                        log_prefix, provider, candidate_model, exc, status,
                    )
                    break  # retries exhausted for this model; try the next candidate
                raise  # not transient / not a model-availability issue — fail fast

    assert last_exc is not None
    raise last_exc


__all__ = ["LLMClient", "LLMResponse", "get_client", "generate_resilient", "DryRunClient"]
