"""Shared machinery for every role: loads its system prompt, resolves its LLM client, and wraps
every call with the budget check + cost accounting so no role can bypass the spend/iteration
caps.
"""
from __future__ import annotations

import logging
import os

from ..budget import BudgetTracker
from ..llm import generate_resilient
from ..llm.pricing import estimate_cost_usd
from ..utils import parse_json_response

logger = logging.getLogger("braincode_loop")

_PROMPTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts")


class LLMCallFailed(Exception):
    """The underlying LLM call itself failed — before any response came back — as opposed to a
    response that came back but didn't parse as JSON (parse_json_response's ValueError, raised
    separately). Deliberately NOT a ValueError: a real production incident had an Anthropic SDK
    pre-flight rejection ("Streaming is required for operations that may take longer than 10
    minutes" — a client-side check on large max_tokens, raised before any network request) get
    caught by a bare `except ValueError` at the orchestrator level and logged as "Shaper never
    produced parseable JSON" for all 100 bootstrap attempts, each failing instantly since the
    request was never sent — actively misleading, since the real problem had nothing to do with
    JSON. Keeping this a distinct type lets callers tell the two failure classes apart."""


def _load_prompt(filename: str) -> str:
    with open(os.path.join(_PROMPTS_DIR, filename), "r", encoding="utf-8") as f:
        return f.read()


class BaseRole:
    role_name: str = "base"
    prompt_file: str = ""                   # steady-state (regular sprint) system prompt
    bootstrap_prompt_file: str = ""         # Sprint 0 system prompt; falls back to prompt_file if unset
    bootstrap_rework_prompt_file: str = ""  # Sprint 0 REVISION system prompt; falls back to bootstrap_prompt_file if unset

    def __init__(
        self, role_cfg: dict, pricing_table: dict, budget: BudgetTracker, dry_run: bool,
        llm_cfg: dict | None = None, transcript=None,
    ):
        self.cfg = role_cfg
        self.pricing_table = pricing_table
        self.budget = budget
        self.dry_run = dry_run
        self.llm_cfg = llm_cfg or {}  # config.yaml -> llm: retry/fallback settings, see llm/generate_resilient
        self.transcript = transcript  # transcript.py::TranscriptLogger, or None (--no-log-file)
        self.system_prompt = _load_prompt(self.prompt_file) if self.prompt_file else ""
        self.bootstrap_system_prompt = (
            _load_prompt(self.bootstrap_prompt_file) if self.bootstrap_prompt_file else self.system_prompt
        )
        self.bootstrap_rework_system_prompt = (
            _load_prompt(self.bootstrap_rework_prompt_file) if self.bootstrap_rework_prompt_file else self.bootstrap_system_prompt
        )

    def call(
        self,
        *,
        sprint: int,
        user_prompt: str,
        provider: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
        temperature: float | None = None,
        role_marker: str | None = None,
        use_search_grounding: bool = False,
        bootstrap: bool = False,
        bootstrap_rework: bool = False,
        attempt: int = 1,
    ) -> dict:
        """Make one LLM call for this role, tagged with `sprint`, and return parsed JSON.

        Checks the budget *before* spending anything (BudgetExceeded propagates to the
        orchestrator, which stops the run cleanly). Records actual cost *after* the call using
        real usage numbers from the provider response.

        `use_search_grounding` requests live web search during this call — only meaningful for
        providers that support it (currently Gemini; see llm/gemini_client.py). Other providers
        silently ignore it. Used by the Searcher role's "internet" mode
        (config.yaml -> roles.searcher.folder_probability).

        Three system prompts, picked in this order: `bootstrap_rework_system_prompt` if
        `bootstrap_rework` (Sprint 0, revising a previously sent-back basis), else
        `bootstrap_system_prompt` if `bootstrap` (Sprint 0, first attempt), else `system_prompt`
        (every steady-state sprint). `bootstrap_rework=True` implies bootstrap semantics — a
        rework call is still a bootstrap-sprint call, so callers don't need to pass both unless
        they want to be explicit. Each role's *_basis()/initialize_*() method should pass
        bootstrap=True; the regular per-sprint methods leave both False.

        A response that comes back with a 200 but isn't valid JSON (e.g. malformed on a large,
        deeply-nested Sprint 0 basis) is retried as a fresh call, up to `llm.retry.max_attempts`
        (same knob `generate_resilient` uses for transient API failures) — this is a different
        failure mode (the call succeeded; the *content* didn't parse) but the same resilience
        philosophy: one bad sample shouldn't kill the whole run. Every attempt's real cost is
        recorded regardless of whether it parsed, since money was genuinely spent either way.

        `attempt` is only for `self.transcript`'s labeling (see transcript.py) — it doesn't affect
        which prompt/model gets used. Searcher's single per-sprint grounding call (not itself
        inside the attempt loop) passes the default `attempt=1`.
        """
        provider = provider or self.cfg["provider"]
        model = model or self.cfg.get("model") or self.cfg.get("models", {}).get(provider)
        max_tokens = max_tokens or self.cfg.get("max_tokens", 1500)
        temperature = temperature if temperature is not None else self.cfg.get("temperature", 0.4)
        marker = role_marker or self.role_name
        if bootstrap_rework:
            system_prompt = self.bootstrap_rework_system_prompt
        elif bootstrap:
            system_prompt = self.bootstrap_system_prompt
        else:
            system_prompt = self.system_prompt

        tagged_prompt = f"# ROLE: {marker}\n\n{user_prompt}"

        max_json_attempts = max(1, self.llm_cfg.get("retry", {}).get("max_attempts", 3))
        last_parse_error: ValueError | None = None
        for json_attempt in range(1, max_json_attempts + 1):
            self.budget.ensure_available()

            try:
                response, model_used = generate_resilient(
                    provider=provider,
                    model=model,
                    system=system_prompt,
                    user=tagged_prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    use_search_grounding=use_search_grounding,
                    dry_run=self.dry_run,
                    llm_cfg=self.llm_cfg,
                    log_prefix=f"[{marker}] ",
                )
            except Exception as exc:
                # Not retried here: a deterministic client/SDK-level rejection (e.g. "streaming
                # required") would fail identically every time within this same call, unlike a
                # JSON-parse failure where a fresh sample might succeed — generate_resilient()
                # has already exhausted its own transient-failure retries/fallbacks by this point.
                raise LLMCallFailed(f"[{marker}] LLM call failed before returning a response: {exc}") from exc

            cost = estimate_cost_usd(self.pricing_table, model_used, response.input_tokens, response.output_tokens)
            self.budget.record_call(
                sprint=sprint,
                role=self.role_name,
                provider=provider,
                model=model_used,
                input_tokens=response.input_tokens,
                output_tokens=response.output_tokens,
                cost_usd=cost,
            )
            last_response_text = response.text

            try:
                result = parse_json_response(response.text)
            except ValueError as exc:
                last_parse_error = exc
                if json_attempt < max_json_attempts:
                    logger.warning(
                        "[%s] response wasn't valid JSON (attempt %d/%d) — retrying: %s",
                        marker, json_attempt, max_json_attempts, exc,
                    )
                continue

            if self.transcript:
                self.transcript.log_call(
                    sprint=sprint, attempt=attempt, bootstrap=bootstrap, role=marker, provider=provider,
                    model=model_used, system_prompt=system_prompt, user_prompt=tagged_prompt,
                    response_text=response.text, cost_usd=cost,
                )
            return result

        if self.transcript:
            self.transcript.log_call(
                sprint=sprint, attempt=attempt, bootstrap=bootstrap, role=marker, provider=provider,
                model=model_used, system_prompt=system_prompt, user_prompt=tagged_prompt,
                response_text=last_response_text, cost_usd=cost, parse_error=str(last_parse_error),
            )
        assert last_parse_error is not None
        raise last_parse_error
