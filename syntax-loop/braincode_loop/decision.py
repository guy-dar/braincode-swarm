"""Turns the doc-hygiene check plus the Critic's judgment into this attempt's decision, and writes
the per-attempt history record to runs/kpi_history.jsonl.

There is no scoring gate here: the Critic's critical assessment of the pre-KPIs *is* the decision.
Doc hygiene is the only scripted override, and it is structural, not statistical. The one other
guard is consistency with the Critic's *own* verdict: an `accept` that the same critique reports as
making a `hard` fundamental note (steering/notes.md) *worse* than the current spec (`trend:
regressed`) is downgraded to needs-rework. Hard notes the current spec already violates don't
block — gating is no-regression, so the language can improve one note per sprint.
"""
from __future__ import annotations

import json
import os

from .doc_hygiene import HygieneResult

_CRITIC_TO_DECISION = {
    "accept": "accepted",
    "accepted": "accepted",
    "needs-rework": "needs-rework",
    "reject": "rejected",
    "rejected": "rejected",
}


def _hard_notes_where(critique: dict, hard_note_ids: set[str], field: str, value: str) -> list[str]:
    assessment = critique.get("notes_assessment") or {}
    return sorted(
        nid for nid, entry in assessment.items()
        if nid in hard_note_ids and str((entry or {}).get(field, "")).lower() == value
    )


def violated_hard_notes(critique: dict, hard_note_ids: set[str]) -> list[str]:
    """Hard notes the language still violates after the changes — informational, not a gate."""
    return _hard_notes_where(critique, hard_note_ids, "status", "violated")


def regressed_hard_notes(critique: dict, hard_note_ids: set[str]) -> list[str]:
    """Hard notes the changes make worse than the current spec — these block acceptance."""
    return _hard_notes_where(critique, hard_note_ids, "trend", "regressed")


def decide(hygiene: HygieneResult, critique: dict, hard_note_ids: set[str] | None = None) -> str:
    if not hygiene.ok:
        return "needs-rework"
    raw = str(critique.get("decision", "")).strip().lower()
    decision = _CRITIC_TO_DECISION.get(raw, "needs-rework")
    if decision == "accepted" and hard_note_ids and regressed_hard_notes(critique, hard_note_ids):
        return "needs-rework"
    return decision


def build_history_record(
    *, sprint: int, attempt: int, proposal: dict, hygiene: HygieneResult, critique: dict,
    decision: str, cross_check_note: str, focus_note: str | None = None,
) -> dict:
    changes = [
        {"op": c.get("op", "add"), "construct_name": c.get("construct_name"), "change_type": c.get("change_type")}
        for c in proposal.get("changes") or []
    ]
    cross_check = dict(critique.get("cross_check") or {})
    cross_check.setdefault("script_note", cross_check_note)
    return {
        "sprint": sprint,
        "attempt": attempt,
        "changes": changes,
        "decision": decision,
        "hygiene": hygiene.as_dict(),
        "kpi_assessment": critique.get("kpi_assessment", {}),
        "simulations": critique.get("simulations", []),
        "cross_check": cross_check,
        "required_changes": critique.get("required_changes", []),
        "logic_issues": critique.get("logic_issues", []),
        "critic_reasoning": critique.get("reasoning", ""),
        "focus_note": focus_note,
        "notes_assessment": critique.get("notes_assessment", {}),
        "rebuttals": proposal.get("rebuttals", []),
        "rebuttal_rulings": critique.get("rebuttal_rulings", []),
    }


def append_history(runs_dir: str, record: dict) -> None:
    os.makedirs(runs_dir, exist_ok=True)
    with open(os.path.join(runs_dir, "kpi_history.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
