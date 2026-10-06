"""Searcher: grounds each sprint's candidate task (or, at Sprint 0, the whole language basis; or,
in a steering sprint, one of the user's fundamental notes) against prior work.

Per sprint, randomly chooses between two modes (config.yaml -> roles.searcher.folder_probability,
default 70% folder / 30% internet):

- **folder** — reason only over the existing `sources/previous_work.md` content passed in.
- **internet** — call Gemini with live Google Search grounding enabled
  (llm/gemini_client.py::GeminiClient) so the model can pull in fresh material beyond what's
  already catalogued. Anything durable it finds gets logged back into
  `sources/previous_work.md` (via LanguageState.append_discovered_source) so future folder-mode
  sprints benefit from it too — the two modes feed each other over time.

The split is chosen via a seeded RNG (run.random_seed) so a given config + seed reproduces the
same sequence of modes across a run.
"""
from __future__ import annotations

import random

from ..state import LanguageState
from .base_role import BaseRole


class Searcher(BaseRole):
    role_name = "searcher"
    prompt_file = "searcher_system.md"
    bootstrap_prompt_file = "searcher_bootstrap_system.md"

    def __init__(self, role_cfg, pricing_table, budget, dry_run, random_seed: int = 42, llm_cfg=None, transcript=None):
        super().__init__(role_cfg, pricing_table, budget, dry_run, llm_cfg=llm_cfg, transcript=transcript)
        self.folder_probability = role_cfg.get("folder_probability", 0.7)
        # Separate RNG stream from LanguageState's task-sampling RNG so mode choice doesn't
        # perturb which tasks get sampled, while staying reproducible for a given seed.
        self._rng = random.Random(random_seed + 1)

    def _choose_mode(self) -> str:
        return "folder" if self._rng.random() < self.folder_probability else "internet"

    def _maybe_log_discovery(self, result: dict, state: LanguageState) -> None:
        suggestion = result.get("new_source_suggestion")
        if suggestion and isinstance(suggestion, dict) and suggestion.get("link"):
            state.append_discovered_source(suggestion)

    def ground_candidate(self, *, sprint: int, task, sources_text: str, state: LanguageState) -> dict:
        mode = self._choose_mode()
        prompt = (
            f"Search mode for this sprint: **{mode}**.\n"
            + (
                "Ground your answer only in the sources text below — do not use live search.\n\n"
                if mode == "folder"
                else "Live web search is available this sprint — use it to find precedent beyond "
                "what's already catalogued below, and fill `new_source_suggestion` if you find "
                "something durable enough to add to the project's source list.\n\n"
            )
            + f"Candidate task ({task.domain}, split={task.split}):\n\"{task.nl}\"\n\n"
            f"Known prior work, including everything discovered by earlier sprints this run "
            f"(sources/previous_work.md, up to date as of this sprint):\n{sources_text}\n\n"
            "Do not put anything already listed above into `new_source_suggestion` — cite it in "
            "`relevant_precedents` instead.\n"
        )
        result = self.call(
            sprint=sprint, user_prompt=prompt, use_search_grounding=(mode == "internet"), attempt=1,
        )
        result["_search_mode"] = mode
        self._maybe_log_discovery(result, state)
        return result

    def ground_note(self, *, sprint: int, note, notes_text: str, spec_text: str, sources_text: str, state: LanguageState) -> dict:
        """Steering sprint: ground one fundamental note (steering/notes.md) — precedent for how
        other languages/formalisms realize what the note asks for, and which existing BrainCode
        constructs it touches. Same output shape as ground_candidate."""
        mode = self._choose_mode()
        prompt = (
            f"Search mode for this sprint: **{mode}**.\n"
            + (
                "Ground your answer only in the sources text below — do not use live search.\n\n"
                if mode == "folder"
                else "Live web search is available this sprint — use it to find precedent beyond "
                "what's already catalogued below, and fill `new_source_suggestion` if you find "
                "something durable enough to add to the project's source list.\n\n"
            )
            + f"STEERING SPRINT — instead of a candidate task, this sprint realizes the project "
            f"lead's fundamental note {note.id} [{note.kind}]: {note.title}\n"
            + (f"{note.body}\n" if note.body else "")
            + "Find precedent for how other languages/formalisms realize what this note asks for, "
            "name the existing BrainCode constructs it touches (from the spec below), and in "
            "`comparable_expression` show one task rendered the way the precedent would do it.\n\n"
            f"{notes_text}\n"
            f"Current language-spec.md:\n{spec_text}\n\n"
            f"Known prior work, including everything discovered by earlier sprints this run "
            f"(sources/previous_work.md, up to date as of this sprint):\n{sources_text}\n\n"
            "Do not put anything already listed above into `new_source_suggestion` — cite it in "
            "`relevant_precedents` instead.\n"
        )
        result = self.call(
            sprint=sprint, user_prompt=prompt, role_marker="searcher_steering",
            use_search_grounding=(mode == "internet"), attempt=1,
        )
        result["_search_mode"] = mode
        self._maybe_log_discovery(result, state)
        return result

    def ground_basis(self, *, sprint: int, sources_text: str, inspiration_languages: list[str], state: LanguageState) -> dict:
        """Sprint 0 only: gather documentation/precedent on the languages BrainCode's initial
        basis should draw structural inspiration from, plus formal-language foundations."""
        mode = self._choose_mode()
        langs = ", ".join(inspiration_languages)
        prompt = (
            f"Search mode for this sprint: **{mode}**.\n"
            + (
                "Ground your answer only in the sources text below — do not use live search.\n\n"
                if mode == "folder"
                else "Live web search is available this sprint — use it to pull in language-reference "
                "material beyond what's already catalogued below.\n\n"
            )
            + "This is Sprint 0 (bootstrap): BrainCode has no constructs yet. Before the Shaper "
            f"proposes an initial syntax basis, summarize what's structurally worth borrowing from "
            f"each of these languages: {langs}. Also summarize relevant formal-language-theory "
            f"foundations (e.g. grammar classes, composability, avoiding ambiguity).\n\n"
            f"Known prior work, including everything discovered by earlier sprints this run "
            f"(sources/previous_work.md, up to date as of this sprint):\n{sources_text}\n\n"
            "Do not put anything already listed above into `new_source_suggestion` — cite it in "
            "`relevant_precedents` instead.\n\n"
            'Return JSON: {"search_mode": "folder"|"internet", "python_notes": "...", '
            '"html_notes": "...", "english_notes": "...", "formal_language_notes": "...", '
            '"relevant_precedents": ["..."], "new_source_suggestion": {"name": "...", "link": "...", "relevance": "..."} | null}'
        )
        result = self.call(
            sprint=sprint, user_prompt=prompt, role_marker="searcher_bootstrap",
            use_search_grounding=(mode == "internet"), bootstrap=True, attempt=1,
        )
        result["_search_mode"] = mode
        self._maybe_log_discovery(result, state)
        return result
