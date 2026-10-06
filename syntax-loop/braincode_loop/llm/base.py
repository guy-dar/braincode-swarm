"""Provider-agnostic LLM client interface."""
from __future__ import annotations

import os
from dataclasses import dataclass


def get_api_key(*names: str) -> str | None:
    """Return the first set, non-empty environment variable among `names`. Lets each provider
    accept the conventional key name plus whatever alternate name(s) a user already has set
    (e.g. a personal env var from before this project existed)."""
    for name in names:
        val = os.environ.get(name)
        if val:
            return val
    return None


@dataclass
class LLMResponse:
    text: str
    input_tokens: int
    output_tokens: int
    provider: str
    model: str
    used_search_grounding: bool = False


class LLMClient:
    """Every concrete client (anthropic/openai/gemini/dry-run) implements this."""

    provider: str = "base"

    def __init__(self, model: str):
        self.model = model

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
        """`use_search_grounding` requests live web search during generation (the Searcher
        role's "internet" mode — see roles/searcher.py). Only GeminiClient currently implements
        it (native Google Search grounding); other clients accept and silently ignore the flag
        so callers don't need to special-case providers.
        """
        raise NotImplementedError
