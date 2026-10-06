"""Documenter: writes the changelog summary (one LLM call) and owns all filesystem writes to
docs/ (spec, glossary, backlog, changelog) via LanguageState — the orchestrator calls it once per
attempt after the Critic has ruled.
"""
from __future__ import annotations

import json
import re

from ..doc_hygiene import HygieneResult, is_vocabulary
from ..state import LanguageState
from ..utils import format_attempt_label
from .base_role import BaseRole

_STATUS = {"accepted": "accepted", "needs-rework": "needs-rework", "rejected": "rejected",
           "partially-accepted": "partially-accepted"}


def _safe_summary(call_fn, **kwargs) -> str:
    """The Documenter's own prose summary is a nice-to-have next to the state writes it's about
    to make (applying an accepted change, appending the changelog/backlog rows) — if its JSON
    response fails to parse after retries, the accepted change must still be recorded rather
    than the whole run crashing on an unrelated prose-generation failure."""
    try:
        return call_fn(**kwargs).get("summary", "(no summary produced)")
    except ValueError as exc:
        return f"(documenter summary unavailable — response failed to parse: {exc})"


def _kpi_lines(critique: dict) -> str:
    assessment = critique.get("kpi_assessment") or {}
    lines = []
    for kpi in ("coverage", "expressivity", "determinism", "interpretability", "improvement"):
        entry = assessment.get(kpi) or {}
        lines.append(f"  - {kpi}: {entry.get('impact', '?')} — {entry.get('reasoning', '')}")
    return "\n".join(lines)


def _simulation_lines(critique: dict) -> str:
    sims = critique.get("simulations") or []
    if not sims:
        return "  - (none recorded)"
    lines = []
    for s in sims:
        lines.append(
            f"  - `{s.get('item_id', '?')}` ({s.get('source', '?')}) [{s.get('coverage', '?')}] "
            f"NL: \"{s.get('nl', '')}\" → `{s.get('braincode', '')}` — {s.get('notes', '')}"
        )
    return "\n".join(lines)


def _required_changes_lines(critique: dict) -> str:
    reqs = critique.get("required_changes") or []
    if not reqs:
        return "  - (none)"
    return "\n".join(f"  - `{r.get('target', '?')}`: {r.get('change', '')}" for r in reqs)


def _changes_line(proposal: dict) -> str:
    changes = proposal.get("changes") or []
    return ", ".join(
        f"`{c.get('construct_name', '?')}` ({c.get('op', 'add')}{' vocabulary' if is_vocabulary(c) else ''}, {c.get('change_type', '?')})"
        for c in changes
    ) or "(none)"


class Documenter(BaseRole):
    role_name = "documenter"
    prompt_file = "documenter_system.md"
    bootstrap_prompt_file = "documenter_bootstrap_system.md"

    def _apply_accepted(self, *, proposal: dict, sprint: int, state: LanguageState) -> str:
        changes = proposal.get("changes") or []
        for change in changes:
            vocab = is_vocabulary(change)
            if change.get("op") == "remove":
                if vocab:
                    state.remove_vocabulary_entry(change["construct_name"])
                else:
                    state.remove_construct(change["construct_name"])
                continue
            entry = {**change, "sprint": sprint}
            if vocab:
                state.upsert_vocabulary_entry(entry)
            else:
                state.upsert_construct_in_spec(entry)
                state.upsert_glossary_entry(entry)
        if proposal.get("foundations_overview"):
            state.replace_foundations(proposal["foundations_overview"])
        # Removing a construct breaks every expression that used it — always a MAJOR bump.
        return state.bump_version_for(
            ["MAJOR" if c.get("op") == "remove" else c.get("change_type", "MINOR") for c in changes]
        )

    def _write_backlog(self, *, sprint: int, proposal: dict, decision: str, critique: dict, attempt: int, max_attempts: int, state: LanguageState, applied_names: list[str] | None = None) -> None:
        label = format_attempt_label(attempt, max_attempts)
        attempt_note = f"{label} " if label else ""
        reason = re.sub(r"\s+", " ", critique.get("reasoning", ""))[:80]
        for change in proposal.get("changes") or []:
            status = _STATUS.get(decision, decision)
            if applied_names is not None:  # partial acceptance: per-change status
                status = "accepted" if change.get("construct_name") in applied_names else "needs-rework"
            state.append_backlog_row(
                f"| {sprint} | `{change.get('construct_name', '?')}` | {status} | "
                f"{sprint} | {attempt_note}{change.get('op', 'add')} — {reason} |\n"
            )

    def _trail_blocks(self, *, critique: dict, hygiene: HygieneResult, decision: str, summary: str, cost: float) -> str:
        xc = critique.get("cross_check") or {}
        blocks = (
            f"- **Critic decision:** {critique.get('decision', '?')} — {critique.get('reasoning', '')}\n"
            f"- **Doc hygiene:** {'pass' if hygiene.ok else 'FAIL'} — {hygiene.describe()}\n"
            f"- **Pre-KPI assessment:**\n{_kpi_lines(critique)}\n"
            f"- **Simulated examples:**\n{_simulation_lines(critique)}\n"
            f"- **Cross-check:** used={xc.get('used', False)}, agreement={xc.get('agreement', 'n/a')} — {xc.get('notes', '')}\n"
        )
        if decision != "accepted" or critique.get("required_changes"):
            blocks += f"- **Required changes:**\n{_required_changes_lines(critique)}\n"
        if critique.get("logic_issues"):
            blocks += "- **Logic issues:** " + "; ".join(str(i) for i in critique["logic_issues"]) + "\n"
        if critique.get("notes_assessment"):
            blocks += "- **Fundamental notes:**\n" + "\n".join(
                f"  - {nid}: {(e or {}).get('status', '?')} — {(e or {}).get('reasoning', '')}"
                for nid, e in critique["notes_assessment"].items()
            ) + "\n"
        if critique.get("position_comparison"):
            blocks += (
                f"- **Competing positions:** chose position {critique.get('chosen_position', '?')} — "
                f"{critique['position_comparison']}\n"
            )
        if critique.get("rebuttal_rulings"):
            blocks += "- **Rebuttal rulings:**\n" + "\n".join(
                f"  - `{r.get('target', '?')}`: {r.get('ruling', '?')} — {r.get('reasoning', '')}"
                for r in critique["rebuttal_rulings"]
            ) + "\n"
        blocks += (
            f"- **Decision:** {decision}\n"
            f"- **Documenter summary:** {summary}\n"
            f"- **Cost this sprint:** ${cost:.4f}\n"
        )
        return blocks

    def record_sprint(
        self, *, sprint: int, task, searcher_notes: dict, proposal: dict, critique: dict, hygiene: HygieneResult,
        decision: str, state: LanguageState, cost_this_sprint: float, attempt: int = 1, max_attempts: int = 1,
        focus_note=None, applied_names: list[str] | None = None,
    ) -> str:
        """`focus_note` set (and `task` None) for a steering sprint. `applied_names` (with decision
        "partially-accepted") applies only those changes; the rest are recorded as sent back."""
        if focus_note is not None:
            agenda_label, agenda = "Steering note", f"{focus_note.id} [{focus_note.kind}] {focus_note.title}"
        else:
            agenda_label, agenda = "Candidate task", task.nl
        prompt = (
            f"Sprint {sprint}, attempt {attempt}/{max_attempts}.\n"
            f"{agenda_label}: \"{agenda}\"\n"
            f"Searcher notes: {searcher_notes}\n"
            f"Shaper proposal: {json.dumps(proposal, ensure_ascii=False)}\n"
            f"Critic assessment: {json.dumps(critique, ensure_ascii=False)}\n"
            f"Doc hygiene: {hygiene.describe()}\n"
            f"Decision: {decision}\n"
        )
        summary = _safe_summary(self.call, sprint=sprint, user_prompt=prompt, attempt=attempt)

        version_before = state.version
        if decision == "accepted":
            version_after = self._apply_accepted(proposal=proposal, sprint=sprint, state=state)
        elif decision == "partially-accepted" and applied_names:
            subset = {**proposal, "changes": [c for c in proposal.get("changes") or [] if c.get("construct_name") in applied_names]}
            subset.pop("foundations_overview", None)  # a partial step doesn't rewrite the philosophy
            version_after = self._apply_accepted(proposal=subset, sprint=sprint, state=state)
        else:
            version_after = version_before
        self._write_backlog(
            sprint=sprint, proposal=proposal, decision=decision, critique=critique, attempt=attempt,
            max_attempts=max_attempts, state=state,
            applied_names=applied_names if decision == "partially-accepted" else None,
        )

        attempt_label = format_attempt_label(attempt, max_attempts)
        header = f"## Sprint {sprint}" + (f" {attempt_label}" if attempt_label else "") + f" — {state.today()}"
        change_types = sorted({str(c.get("change_type", "MINOR")) for c in proposal.get("changes") or []})
        entry = (
            f"\n{header}\n\n"
            f"- **Language version:** {version_before} → {version_after} ({'/'.join(change_types) or 'n/a'})\n"
            f"- **{agenda_label}:** {agenda}\n"
            f"- **Shaper proposal (model: {proposal.get('_provider_used', '?')}/{proposal.get('_model_used', '?')}):** {proposal.get('summary', '')}\n"
            + (
                f"- **Shaper's position on the note:** {proposal.get('note_position', '?')} — {proposal.get('note_argument', '')}\n"
                if focus_note is not None else ""
            )
            + f"- **Changes:** {_changes_line(proposal)}\n"
            + (
                f"- **Partial acceptance:** applied {len(applied_names)} of {len(proposal.get('changes') or [])} "
                f"changes ({', '.join(f'`{n}`' for n in applied_names)}); the rest were sent back for rework.\n"
                if decision == "partially-accepted" and applied_names else ""
            )
            + (
                "- **Shaper rebuttals:**\n" + "\n".join(
                    f"  - `{r.get('target', '?')}`: {r.get('argument', '')}" for r in proposal["rebuttals"]
                ) + "\n"
                if proposal.get("rebuttals") else ""
            )
            + self._trail_blocks(critique=critique, hygiene=hygiene, decision=decision, summary=summary, cost=cost_this_sprint)
        )
        state.append_changelog_entry(entry)
        return summary

    def initialize_documentation(
        self, *, sprint: int, basis: dict, searcher_notes: dict, critique: dict, hygiene: HygieneResult,
        decision: str, state: LanguageState, cost_this_sprint: float, attempt: int = 1, max_attempts: int = 1,
    ) -> str:
        """Sprint 0 only: write the Foundations section and every construct in the accepted basis
        in one atomic bootstrap changelog entry."""
        changes = basis.get("changes") or []
        prompt = (
            f"Sprint 0 (bootstrap), attempt {attempt}/{max_attempts}. Searcher notes: {searcher_notes}\n"
            f"Foundations overview: {basis.get('foundations_overview')}\n"
            f"Proposed basis ({len(changes)} constructs): {json.dumps(changes, ensure_ascii=False)}\n"
            f"Critic assessment: {json.dumps(critique, ensure_ascii=False)}\n"
            f"Doc hygiene: {hygiene.describe()}\n"
            f"Decision: {decision}\n"
        )
        summary = _safe_summary(
            self.call, sprint=sprint, user_prompt=prompt, role_marker="documenter_bootstrap", bootstrap=True,
            attempt=attempt,
        )

        version_before = state.version
        if decision == "accepted":
            state.set_foundations(f"{basis.get('foundations_overview', '')}\n\n{basis.get('inspiration_summary', '')}\n")
            for change in changes:
                construct = {**change, "sprint": sprint}
                state.upsert_construct_in_spec(construct)
                state.upsert_glossary_entry(construct)
            version_after = state.bump_version("MAJOR")
            self._update_spec_status(state, "bootstrapped — base syntax established; sprints from here build incrementally.")
        else:
            version_after = version_before

        self._write_backlog(sprint=0, proposal=basis, decision=decision, critique=critique, attempt=attempt, max_attempts=max_attempts, state=state)

        attempt_label = format_attempt_label(attempt, max_attempts).strip("()")
        header = "## Sprint 0 (bootstrap" + (f", {attempt_label})" if attempt_label else ")") + f" — {state.today()}"
        entry = (
            f"\n{header}\n\n"
            f"- **Language version:** {version_before} → {version_after} (MAJOR — establishes the base syntax)\n"
            f"- **Inspiration languages:** {basis.get('inspiration_summary', '')}\n"
            f"- **Shaper proposal (model: {basis.get('_provider_used', '?')}/{basis.get('_model_used', '?')}):** {basis.get('summary', '')}\n"
            f"- **Changes:** {_changes_line(basis)}\n"
            + self._trail_blocks(critique=critique, hygiene=hygiene, decision=decision, summary=summary, cost=cost_this_sprint)
        )
        state.append_changelog_entry(entry)
        return summary

    @staticmethod
    def record_note_outcome(*, sprint: int, note, status: str, assessment: dict | None, state: LanguageState) -> None:
        """One backlog row per steering sprint: where the focus note stands after it (no LLM call)."""
        reason = re.sub(r"\s+", " ", str((assessment or {}).get("reasoning", "")))[:80]
        state.append_backlog_row(
            f"| {sprint} | note {note.id} [{note.kind}] | {status} | {sprint} | "
            f"{(assessment or {}).get('status', 'n/a')} — {reason} |\n"
        )

    @staticmethod
    def _update_spec_status(state: LanguageState, status_note: str) -> None:
        with open(state.spec_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = re.sub(r"\*\*Status:\*\*.*?(?=\n\n|\n##)", f"**Status:** {status_note}", content, count=1, flags=re.DOTALL)
        with open(state.spec_path, "w", encoding="utf-8") as f:
            f.write(content)
