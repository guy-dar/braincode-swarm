#!/usr/bin/env python3
"""Build reference/language-spec.compact.md: the spec as translators receive it.

Only change-log / revision-history material is removed (where this version
came from, what v18 did differently, the adoption roadmap), plus wording that
existed only to point at that history. Every language rule is kept: each edit
below either deletes a purely historical sentence or rewrites one so the rule
it carried survives without the history. The canonical
reference/language-spec.md is never modified; the migrator still reads it.

Each edit must match exactly once, so a change to the spec that touches an
edited sentence stops the build instead of silently skipping the edit.

    python spec_compact.py          # rebuild after editing language-spec.md
"""
import re
import sys
from pathlib import Path

REF = Path(__file__).resolve().parent / "reference"
SOURCE = REF / "language-spec.md"
TARGET = REF / "language-spec.compact.md"

# (old, new) — exact substrings of language-spec.md.
EDITS = [
    # Intro: how this revision relates to v18 and the old design document.
    ("This is a separate revision of the v18 specification. It preserves Task, Action, Generate, Utterance, Check, "
     "Flow-If, Iterate, Bind, Conversation, and canonical translation, while adding a semantic layer for meaning, "
     "reasoning, provenance, and observed behavior. It does not adopt the old design document's syntax or nine-sort "
     "system.\n\n", ""),
    (" Adoption and historical migration notes are in proposed-lexical-groups/design-notes.md.", ""),
    # Rules that cited v18 / "this draft" as their justification: rule kept, history dropped.
    ("have static type STRING, preserving v18 behavior.", "have static type STRING."),
    ("Early returns are outside this draft.", "Early returns are not supported."),
    ("Mutual recursion is outside this draft.", "Mutual recursion is not supported."),
    ("The following compatibility profile retains v18's intent; the migrated glossary must supply complete signatures:",
     "Operation profile (the glossary supplies complete signatures):"),
    ("Existing fields such as `duration`, `stop_min_per_day`, and `max_walk_duration` may be migrated only with "
     "explicit definitions.",
     "Fields such as `duration`, `stop_min_per_day`, and `max_walk_duration` require explicit glossary definitions."),
    ("no result binding in this draft;", "no result binding;"),
    (" This replaces v18's inconsistent assumption that every utterance has a content STRING to return.", ""),
    ("cannot be compared by Check in this draft;", "cannot be compared by Check;"),
    ("Truthiness preserves v18's rules:", "Truthiness:"),
    ("This preserves v18's ban on inline nested calls while allowing arbitrarily useful composition through explicit "
     "bindings.", "Inline nested calls remain banned; compose through explicit bindings."),
    ("This is a narrow addition to v18: it permits", "This permits"),
    (" This preserves the design document's anti-evasion principle without deleting exact-wording requirements.", ""),
    ("Remove v18's automatic `custom_general_<predicate>` escape hatch.",
     "There is no automatic `custom_general_<predicate>` escape hatch."),
    ("They are illustrative proposed glossary entries, not claims that the existing glossary already contains them. "
     "No empirical language-quality validation is implied.",
     "They are illustrative entries and may not exist in the current glossary; use the glossary's definitions."),
]
# Header lines that record where this revision came from (date, status, base
# file, old design doc).
HEADER_HISTORY_RE = re.compile(r"^\*\*(Date|Status|Base|Semantic reference):\*\*.*\n", re.M)
# A change-log section (v18 -> this draft table and adoption roadmap), cut if
# present; the lexical-groups release already moved it to design notes.
CUT_FROM = "## 17. Changes from v18 and adoption requirements"


def build(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = HEADER_HISTORY_RE.sub("", text)
    for old, new in EDITS:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"spec_compact: expected exactly one match, found {count}: {old[:80]!r}")
        text = text.replace(old, new)
    cut = text.find(CUT_FROM)
    if cut != -1:
        text = text[:cut].rstrip() + "\n"
    leftovers = [w for w in ("v18", "this draft", "DESIGN_DOC", "Section 17") if w in text]
    if leftovers:
        print(f"spec_compact: note — still mentions {leftovers} (review)", file=sys.stderr)
    return text


def main():
    src = SOURCE.read_text(encoding="utf-8")
    out = build(src)
    TARGET.write_text(out, encoding="utf-8", newline="\n")
    print(f"{SOURCE.name}: {len(src):,} chars -> {TARGET.name}: {len(out):,} chars "
          f"({100 * (1 - len(out) / len(src)):.0f}% smaller)")


if __name__ == "__main__":
    main()
