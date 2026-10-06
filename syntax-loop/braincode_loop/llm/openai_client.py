"""OpenAI client. Used by the Reviewer role by default, and by the Shaper on its OpenAI rotation
turn (see config.yaml -> roles.shaper.rotation)."""
from __future__ import annotations

from .base import LLMClient, LLMResponse, get_api_key


class OpenAIClient(LLMClient):
    provider = "openai"

    def __init__(self, model: str):
        super().__init__(model)
        self._client = None

    def _ensure_client(self):
        if self._client is None:
            import openai

            api_key = get_api_key("OPENAI_API_KEY", "OPENAI_API_KEY_PERSONAL")
            if not api_key:
                raise RuntimeError(
                    "No OpenAI API key found. Set OPENAI_API_KEY or OPENAI_API_KEY_PERSONAL in "
                    ".env or your environment, or set run.dry_run: true in config.yaml to test "
                    "the loop without API calls."
                )
            self._client = openai.OpenAI(api_key=api_key)
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
        # `max_tokens` was retired in favor of `max_completion_tokens` — current-generation
        # models (verified against gpt-5.6-terra, 2026-08-27) reject the old name with
        # `openai.BadRequestError: Unsupported parameter: 'max_tokens'...`.
        #
        # `temperature` is accepted for interface parity with the other providers (see
        # llm/base.py) but silently ignored here: gpt-5.6-terra (a reasoning-tuned model) only
        # supports the default temperature (1) and rejects any explicit value with
        # `openai.BadRequestError: Unsupported value: 'temperature' does not support <x> with
        # this model. Only the default (1) value is supported.`
        resp = client.chat.completions.create(
            model=self.model,
            max_completion_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        text = resp.choices[0].message.content or ""
        usage = resp.usage
        return LLMResponse(
            text=text,
            input_tokens=usage.prompt_tokens if usage else 0,
            output_tokens=usage.completion_tokens if usage else 0,
            provider=self.provider,
            model=self.model,
        )
