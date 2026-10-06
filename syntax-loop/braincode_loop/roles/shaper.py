"""The Shaper has no fixed model in the source meeting notes ("Shaper - composes the language" -
no provider listed, unlike the other roles). This loop treats that as intentional: it rotates the
Shaper across all three providers, one per sprint, so the language is composed by a "small group
of diverse agents" rather than one model's idiosyncratic style — directly serving the Determinism
pre-KPI (a construct that looks reasonable to all three providers is more likely to be
model-style-independent) and the meeting notes' framing of the loop as diverse-role debate.

A proposal is a *set* of changes (`changes: [{op: add|revise|remove, ...}]`), not a single
construct — one sprint may add a construct and revise two others if that is what the task calls for.

In a *steering sprint* (propose_steering) the agenda is one of the user's fundamental notes
(steering/notes.md) instead of a seed task. On a rework the Shaper may answer a required change
with a `rebuttal` (an argument) instead of complying; the Critic rules on each one.
"""
from __future__ import annotations

import json

from .base_role import BaseRole

CHANGE_SCHEMA = (
    '{"op": "add" | "revise" | "remove", "construct_name": "...", "grammar": "...", "semantics": "...", '
    '"worked_example": {"nl": "...", "braincode": "..."}, "glossary_gloss": "...", '
    '"change_type": "MAJOR" | "MINOR" | "PATCH", "rationale": "...", "cites_source": "..." | null, '
    '"addresses_note": "N<k>" | null}'
)
# A vocabulary change (`kind: "vocabulary"`) goes in the same `changes` list — see VOCAB_SCHEMA.
CHANGE_SCHEMA += (
    ' — or, for a category of the descriptive lexicon (actions, objects, roles, attribute values, '
    'literal forms): {"op": "add" | "revise" | "remove", "kind": "vocabulary", "construct_name": '
    '"<category name, e.g. tone-value>", "glossary_gloss": "...", "closed": true | false, '
    '"members": [{"symbol": "...", "gloss": "...", "nl_synonyms": ["..."]}], '
    '"membership_rule": "..." | null, "worked_example": {"nl": "...", "braincode": "..."}, '
    '"change_type": "MAJOR" | "MINOR" | "PATCH", "rationale": "...", "addresses_note": "N<k>" | null}'
)
REBUTTAL_SCHEMA ='{"target": "...", "change": "<the required change you contest>", "argument": "..."}'


def _rework_block(previous_attempt: dict | None) -> str:
    if not previous_attempt:
        return ""
    critique = {k: v for k, v in previous_attempt.get("critique", {}).items() if not k.startswith("_")}
    origin = previous_attempt.get("origin")
    applied = previous_attempt.get("applied") or []
    if applied and not previous_attempt.get("changes"):
        status_line = (
            f"ACCEPTED WITH KNOWN ISSUES: all of these changes WERE applied and are now in the "
            f"spec/glossary shown below: {', '.join(applied)}. Nothing from it is pending. Continue "
            "from the current spec: address the Critic's required changes (the known issues) below "
            "and make further progress on the note, using `revise` for entries that now exist.\n"
        )
    elif applied:
        status_line = (
            f"PARTIALLY ACCEPTED: these changes WERE applied and are now in the spec/glossary shown "
            f"below: {', '.join(applied)}. The remaining changes listed below were NOT applied. "
            "Resubmit the remaining changes you still want (improved per the critique), plus "
            "anything new the fixes need; use `revise` for the applied entries if they need further "
            "work.\n"
        )
    else:
        status_line = (
            "IMPORTANT: the previous attempt was NOT applied — none of its changes are in the current "
            "spec or glossary shown below. Resubmit the COMPLETE set of changes you want applied: "
            "carry forward every previous change you still want (unchanged or improved) alongside the "
            "fixes, not just the delta. "
        )
    return (
        "\n\nYOUR PREVIOUS ATTEMPT WAS SENT BACK — this is a revision, not a fresh start"
        + (f" ({origin})" if origin else "") + ".\n"
        + status_line
        + "Use `op: \"add\"` for anything not yet in the current spec/glossary, "
        "`revise`/`remove` only for entries that exist there now.\n"
        f"Previous changes{' not applied' if applied else ''}: {json.dumps(previous_attempt.get('changes', []), ensure_ascii=False)}\n"
        f"Critic's decision: {critique.get('decision')}\n"
        f"Critic's reasoning: {critique.get('reasoning')}\n"
        f"Required changes (address every one explicitly): {json.dumps(critique.get('required_changes', []), ensure_ascii=False)}\n"
        f"Logic issues: {json.dumps(critique.get('logic_issues', []), ensure_ascii=False)}\n"
        f"Pre-KPI assessment: {json.dumps(critique.get('kpi_assessment', {}), ensure_ascii=False)}\n"
        f"Simulated examples that exposed gaps: {json.dumps(critique.get('simulations', []), ensure_ascii=False)}\n"
        f"Rebuttal rulings on your previous rebuttals (if any): {json.dumps(critique.get('rebuttal_rulings', []), ensure_ascii=False)}\n"
        "Address every required change — either comply, or put it in `rebuttals` with a concrete "
        "argument (evidence from the simulated items, a conflict with another construct or with a "
        "fundamental note) for why it should not be made. The Critic rules on each rebuttal; an "
        "overruled rebuttal must be complied with next time. Never rebut a change that enforces a "
        "`hard` fundamental note. Revising an existing spec construct is `op: \"revise\"` with the "
        "same construct_name.\n"
    )


def _reject_truncated(result: dict, max_changes: int) -> None:
    """A proposal cut off at the output limit has silently lost its trailing changes (typically
    the construct revisions that use the new vocabulary) — never pass it on as if complete. The
    ValueError goes through the orchestrator's malformed-attempt path, so the next attempt is
    told why."""
    if result.get("_truncated"):
        raise ValueError(
            f"the proposal was cut off at the output limit, so its trailing changes were lost — "
            f"resubmit a smaller, complete set (at most {max_changes} changes, concise fields)"
        )


def _proposal_json_spec(extra: str = "") -> str:
    return (
        f'Return JSON: {{"summary": "1-2 sentences on what this set of changes achieves", {extra}'
        f'"changes": [{CHANGE_SCHEMA}, ...], "rebuttals": [{REBUTTAL_SCHEMA}, ...]}}'
    )


class Shaper(BaseRole):
    role_name = "shaper"
    prompt_file = "shaper_system.md"
    bootstrap_prompt_file = "shaper_bootstrap_system.md"
    bootstrap_rework_prompt_file = "shaper_bootstrap_rework_system.md"

    def __init__(self, role_cfg, pricing_table, budget, dry_run, llm_cfg=None, transcript=None):
        super().__init__(role_cfg, pricing_table, budget, dry_run, llm_cfg=llm_cfg, transcript=transcript)
        self.rotation = role_cfg.get("rotation", ["anthropic", "openai", "gemini"])
        self.models = role_cfg.get("models", {})

    def provider_for_sprint(self, sprint: int) -> str:
        return self.rotation[sprint % len(self.rotation)]

    def propose(
        self, *, sprint: int, task, searcher_notes: dict, spec_text: str, glossary_text: str,
        previous_attempt: dict | None = None, attempt: int = 1, notes_text: str = "",
    ) -> dict:
        provider = self.provider_for_sprint(sprint)
        model = self.models.get(provider)
        prompt = (
            f"Candidate task ({task.domain}, split={task.split}):\n\"{task.nl}\"\n\n"
            + (f"{notes_text}\n" if notes_text else "")
            + f"Searcher's notes for this sprint:\n{searcher_notes}\n\n"
            f"Current language-spec.md:\n{spec_text}\n\n"
            f"Current glossary.md:\n{glossary_text}\n"
            f"{_rework_block(previous_attempt)}\n"
            + _proposal_json_spec()
        )
        result = self.call(sprint=sprint, user_prompt=prompt, provider=provider, model=model, attempt=attempt)
        result["_provider_used"] = provider
        result["_model_used"] = model
        return result

    def propose_steering(
        self, *, sprint: int, note, notes_text: str, searcher_notes: dict, spec_text: str,
        glossary_text: str, previous_attempt: dict | None = None, attempt: int = 1,
        provider: str | None = None, max_changes: int = 12,
    ) -> dict:
        """Steering sprint: revise the existing language so it realizes one fundamental note.
        `provider` overrides the rotation (multi-position attempts and their reworks)."""
        provider = provider or self.provider_for_sprint(sprint)
        model = self.models.get(provider)
        contest = (
            "This is a `hard` note: realize it — it cannot be contested."
            if note.kind == "hard"
            else "This is a `direction` note: realize it, or — only if the evidence (simulated "
            "items, conflicts with other notes or constructs) shows it would harm the pre-KPIs — "
            "argue against it in `note_argument` with `note_position: \"contest\"` and propose the "
            "best alternative."
        )
        prompt = (
            f"STEERING SPRINT — focus note {note.id} [{note.kind}]: {note.title}\n"
            + (f"{note.body}\n" if note.body else "")
            + f"{contest}\n\n"
            "You are working on an existing, mature language — not starting over. Change what the "
            "note requires: `revise` constructs it touches, `remove` constructs it makes obsolete "
            "(merging two constructs = revise one + remove the other), `add` only if nothing "
            "existing can carry it. Tag each change with `addresses_note`. If the note changes the "
            "grammar philosophy, include a rewritten `foundations_overview`, else null.\n"
            f"SCOPE: at most {max_changes} changes this sprint. Take one coherent, fully specified "
            "step — the constructs and the vocabulary they use, consistent with each other — rather "
            "than an overreaching redesign; the note stays open for the next sprint if it isn't "
            "fully realized. Keep each field concise: an answer that runs out of output space is "
            "rejected unread.\n\n"
            f"{notes_text}\n"
            f"Searcher's notes for this sprint:\n{searcher_notes}\n\n"
            f"Current language-spec.md:\n{spec_text}\n\n"
            f"Current glossary.md:\n{glossary_text}\n"
            f"{_rework_block(previous_attempt)}\n"
            + _proposal_json_spec(
                '"note_position": "comply" | "contest", "note_argument": "how the changes realize '
                'the note, or the evidence for contesting it", "foundations_overview": "..." | null, '
            )
        )
        result = self.call(
            sprint=sprint, user_prompt=prompt, provider=provider, model=model,
            role_marker="shaper_steering", attempt=attempt,
        )
        _reject_truncated(result, max_changes)
        result["_provider_used"] = provider
        result["_model_used"] = model
        return result

    def propose_basis(
        self, *, sprint: int, searcher_notes: dict, inspiration_languages: list[str],
        previous_attempt: dict | None = None, attempt: int = 1, notes_text: str = "",
    ) -> dict:
        """Sprint 0 only: propose the entire initial syntax basis (all `op: add`), grounded in the
        Searcher's notes on the inspiration languages plus formal-language foundations."""
        provider = self.provider_for_sprint(sprint)
        model = self.models.get(provider)
        langs = ", ".join(inspiration_languages)
        prompt = (
            f"This is Sprint 0 (bootstrap): the language has no constructs yet. Propose an "
            f"initial syntax **basis** — a small set of foundational, composable constructs "
            f"(aim for 3-6, every change `op: \"add\"`, change_type MAJOR) that together can express "
            f"simple agent-requests, drawing structural inspiration from: {langs}. Prefer a small "
            f"orthogonal core over redundant coverage — every later sprint composes from these."
            f"{_rework_block(previous_attempt)}\n\n"
            + (f"{notes_text}\n" if notes_text else "")
            + f"Searcher's notes for this sprint:\n{searcher_notes}\n\n"
            'Return JSON: {"foundations_overview": "2-4 sentences for the spec\'s Foundations '
            'section: the grammar philosophy and how it draws on the inspiration languages", '
            '"inspiration_summary": "1-2 sentences citing which language inspired which choice", '
            '"summary": "1 sentence", '
            f'"changes": [{CHANGE_SCHEMA}, ...]}}'
        )
        result = self.call(
            sprint=sprint, user_prompt=prompt, provider=provider, model=model,
            role_marker="shaper_bootstrap", bootstrap=True, bootstrap_rework=bool(previous_attempt),
            attempt=attempt,
        )
        result["_provider_used"] = provider
        result["_model_used"] = model
        return result
