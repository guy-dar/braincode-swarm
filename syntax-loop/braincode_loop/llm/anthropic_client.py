"""Claude client. Used by the Documenter and Examiner roles by default, and by the Shaper on its
Anthropic rotation turn (see config.yaml -> roles.shaper.rotation)."""
from __future__ import annotations

from .base import LLMClient, LLMResponse, get_api_key


class AnthropicClient(LLMClient):
    provider = "anthropic"

    def __init__(self, model: str):
        super().__init__(model)
        self._client = None  # lazy: don't require the SDK/key unless actually called

    def _ensure_client(self):
        if self._client is None:
            import anthropic

            api_key = get_api_key("ANTHROPIC_API_KEY", "CLAUDE_API_KEY")
            if not api_key:
                raise RuntimeError(
                    "No Anthropic API key found. Set ANTHROPIC_API_KEY or CLAUDE_API_KEY in "
                    ".env or your environment, or set run.dry_run: true in config.yaml to test "
                    "the loop without API calls."
                )
            self._client = anthropic.Anthropic(api_key=api_key)
        return self._client

    def generate(
        self,
        *,
        system: str,
        user: str,
        max_tokens: int = 1500,
        temperature: float = 0.4,
        use_search_grounding: bool = False,
        effort: str | None = None,
    ) -> LLMResponse:
        client = self._ensure_client()
        # `temperature` is accepted for interface parity with the other providers (see
        # llm/base.py) but silently ignored here: as of the anthropic 1.x SDK/API (verified
        # 2026-08-27), the Messages API dropped temperature/top_p/top_k entirely in favor of
        # `output_config.effort` (a reasoning-depth control, not sampling randomness — not an
        # equivalent knob, so it isn't substituted in automatically). Passing `temperature`
        # raises `TypeError: Messages.create() got an unexpected keyword argument 'temperature'`.
        #
        # Uses the streaming helper, not messages.create(), because the SDK refuses a
        # non-streaming call outright once max_tokens is high enough that it estimates
        # generation could exceed 10 minutes for this model (raises client-side, before any
        # network request — "Streaming is required for operations that may take longer than 10
        # minutes"). This bit us in production once roles.shaper.max_tokens/roles.critic.max_tokens
        # were bumped for larger proposals — every single attempt failed instantly, all 100
        # bootstrap retries within the same second, since the request never even got sent.
        # `.stream(...)` + `get_final_message()` gives the identical synchronous "wait for the
        # whole response" shape the rest of this method already expects, just over SSE
        # internally, so nothing downstream needs to change.
        #
        # `effort` -> output_config.effort (low|medium|high|xhigh|max). Sonnet 5 runs adaptive
        # thinking by default at effort `high`, and thinking counts against max_tokens: on
        # 2026-09-30 a Shaper call spent ~48k tokens thinking and emitted 1.7k chars before being
        # cut off. Lower effort leaves the visible answer its budget (config.yaml -> llm.anthropic).
        extra = {"output_config": {"effort": effort}} if effort else {}
        with client.messages.stream(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
            **extra,
        ) as stream:
            resp = stream.get_final_message()
        text = "".join(block.text for block in resp.content if getattr(block, "type", None) == "text")
        return LLMResponse(
            text=text,
            input_tokens=resp.usage.input_tokens,
            output_tokens=resp.usage.output_tokens,
            provider=self.provider,
            model=self.model,
        )
