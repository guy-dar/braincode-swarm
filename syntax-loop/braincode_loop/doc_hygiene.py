"""Doc hygiene: the one scripted, non-negotiable structural check. Every change in a proposal must
carry a complete glossary entry (gloss + worked example) or the Documenter has nothing to write
into docs/glossary.md — an undocumented construct is a documentation failure by definition, so a
failing proposal always goes back for rework regardless of what the Critic concludes.

Two kinds of change: `kind: "construct"` (default — a grammar construct, written to the spec and
the glossary) and `kind: "vocabulary"` (a category of the descriptive lexicon — actions, objects,
attribute values, literal forms — written only to the glossary's Vocabulary section).

This is not a KPI test and not statistical; it is schema completeness.
"""
from __future__ import annotations

from dataclasses import dataclass, field

REQUIRED_FIELDS = ("construct_name", "grammar", "semantics", "glossary_gloss", "worked_example")
VOCAB_REQUIRED_FIELDS = ("construct_name", "glossary_gloss", "worked_example")
REMOVE_REQUIRED_FIELDS = ("construct_name", "rationale")  # a removal has nothing left to document


@dataclass
class HygieneResult:
    ok: bool
    failures: list[dict] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {"ok": self.ok, "failures": self.failures}

    def describe(self) -> str:
        if self.ok:
            return "All changes carry a complete glossary entry (gloss + worked example), and every revise/remove targets an existing entry."
        parts = [f"`{f['construct_name']}` missing {', '.join(f['missing_fields'])}" for f in self.failures]
        return "Doc hygiene FAILED — " + "; ".join(parts)


def is_vocabulary(change: dict) -> bool:
    return str(change.get("kind", "construct")).lower() == "vocabulary"


def check_change(change: dict, existing_names: set[str] | None = None, existing_vocab: set[str] | None = None) -> list[str]:
    op = change.get("op", "add")
    vocab = is_vocabulary(change)
    existing = existing_vocab if vocab else existing_names
    where = "the glossary's Vocabulary section" if vocab else "language-spec.md"
    if op == "remove":
        missing = [k for k in REMOVE_REQUIRED_FIELDS if not change.get(k)]
        if existing is not None and change.get("construct_name") not in existing:
            missing.append(f"an existing entry to remove (not in {where})")
        return missing
    missing = [k for k in (VOCAB_REQUIRED_FIELDS if vocab else REQUIRED_FIELDS) if not change.get(k)]
    if vocab and not change.get("members") and not change.get("membership_rule"):
        missing.append("members or membership_rule")
    if op == "revise" and existing is not None and change.get("construct_name") not in existing:
        missing.append(f"an existing entry to revise (not in {where} — use op: add)")
    example = change.get("worked_example") or {}
    if not isinstance(example, dict) or not example.get("nl") or not example.get("braincode"):
        missing.append("worked_example.nl/braincode")
    return missing


def check(proposal: dict, existing_names: set[str] | None = None, existing_vocab: set[str] | None = None) -> HygieneResult:
    """`existing_names` (the spec's construct names) and `existing_vocab` (the glossary's
    vocabulary categories) enable the revise/remove-target check; omit them to check schema
    completeness only."""
    changes = proposal.get("changes") or []
    failures = []
    if not changes:
        failures.append({"construct_name": "(none)", "missing_fields": ["changes (proposal has no changes)"]})
    for change in changes:
        missing = check_change(change, existing_names, existing_vocab)
        if missing:
            failures.append({"construct_name": change.get("construct_name") or "?", "missing_fields": missing})
    return HygieneResult(ok=not failures, failures=failures)
