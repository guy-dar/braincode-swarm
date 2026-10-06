"""Gemini client. Used by the Searcher role by default, and by the Shaper on its Gemini rotation
turn (see config.yaml -> roles.shaper.rotation).

Also the only client that implements `use_search_grounding` for real: Gemini's API supports
native Google Search grounding (the model issues live web searches during generation and cites
what it finds). The Searcher role uses this for its "internet" mode
(config.yaml -> roles.searcher.folder_probability) — see roles/searcher.py.
"""
from __future__ import annotations

from .base import LLMClient, LLMResponse, get_api_key


class GeminiClient(LLMClient):
    provider = "gemini"

    def __init__(self, model: str):
        super().__init__(model)
        self._client = None

    def _ensure_client(self):
        if self._client is None:
            from google import genai

            api_key = get_api_key("GEMINI_API_KEY")
            if not api_key:
                raise RuntimeError(
                    "GEMINI_API_KEY is not set. Set it in .env or your environment, or "
                    "set run.dry_run: true in config.yaml to test the loop without API calls."
                )
            self._client = genai.Client(api_key=api_key)
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
        from google.genai import types

        config_kwargs = dict(
            system_instruction=system,
            max_output_tokens=max_tokens,
            temperature=temperature,
            # We never pass Python-callable tools (only `google_search`, which isn't a
            # function-calling tool), so automatic function calling has nothing to do here —
            # disabling it silences the SDK's "Direct use of AFC in Models.generate_content is
            # not recommended" warning without changing any actual behavior.
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        )
        if use_search_grounding:
            config_kwargs["tools"] = [types.Tool(google_search=types.GoogleSearch())]

        resp = client.models.generate_content(
            model=self.model,
            contents=user,
            config=types.GenerateContentConfig(**config_kwargs),
        )
        text = resp.text or ""
        usage = getattr(resp, "usage_metadata", None)
        input_tokens = getattr(usage, "prompt_token_count", 0) if usage else 0
        output_tokens = getattr(usage, "candidates_token_count", 0) if usage else 0
        return LLMResponse(
            text=text,
            input_tokens=input_tokens or 0,
            output_tokens=output_tokens or 0,
            provider=self.provider,
            model=self.model,
            used_search_grounding=use_search_grounding,
        )
