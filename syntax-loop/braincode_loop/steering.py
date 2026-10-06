"""Steering: the user's fundamental notes (steering/notes.md) and their per-note status.

The notes file is user-owned — the loop only reads it. Each note is a level-2 heading:

    ## N1 [hard] No construct may take another construct inline as an argument.
    Optional body lines explaining the note, up to the next `## ` heading.

`hard` notes are constraints the agents may not override; `direction` notes are goals the Shaper
may contest with evidence (the Critic rules on it). While any note is open, sprints are
*steering sprints* focused on the next open note instead of a random seed task — see
orchestrator.py::Orchestrator.run_sprint.

Per-note status lives in docs/notes-status.json (loop-owned, reset by `--reset`/`--from`):
    {"N1": {"status": "open|resolved|declined|stalled", "sprints": [11, 12],
            "text_hash": "...", "last_assessment": {...}}}
Editing a note's text changes its hash, which reopens it.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass

NOTE_KINDS = ("hard", "direction")
STATUS_FILE = "notes-status.json"
_HEADING_RE = re.compile(r"^##\s+(N\d+)\s*\[(hard|direction)\]\s*(.*)$", re.IGNORECASE)


@dataclass
class Note:
    id: str
    kind: str  # "hard" | "direction"
    title: str
    body: str = ""

    @property
    def text_hash(self) -> str:
        return hashlib.sha1(f"{self.kind}\n{self.title}\n{self.body}".encode("utf-8")).hexdigest()[:12]

    def describe(self) -> str:
        return f"{self.id} [{self.kind}] {self.title}" + (f"\n    {self.body}" if self.body else "")


def parse_notes(text: str) -> list[Note]:
    # HTML comments hold the template's examples — never parse notes from inside them.
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    notes: list[Note] = []
    current: Note | None = None
    body: list[str] = []
    for line in text.splitlines():
        m = _HEADING_RE.match(line.strip())
        if m or line.startswith("## ") or line.startswith("# "):
            if current:
                current.body = " ".join(" ".join(body).split())
                notes.append(current)
            current, body = None, []
            if m:
                current = Note(id=m.group(1).upper(), kind=m.group(2).lower(), title=m.group(3).strip())
            continue
        if current:
            body.append(line.strip())
    if current:
        current.body = " ".join(" ".join(body).split())
        notes.append(current)
    return notes


def load_notes(path: str | None) -> list[Note]:
    if not path or not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return parse_notes(f.read())


class NoteStatus:
    """docs/notes-status.json — which notes are open/resolved/declined/stalled."""

    def __init__(self, docs_dir: str):
        self.path = os.path.join(docs_dir, STATUS_FILE)
        self.data: dict[str, dict] = {}
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)

    def sync(self, notes: list[Note]) -> None:
        """Add new notes as open; reopen any note whose text changed since it was last judged."""
        for note in notes:
            entry = self.data.get(note.id)
            if entry is None or entry.get("text_hash") != note.text_hash:
                self.data[note.id] = {"status": "open", "sprints": [], "text_hash": note.text_hash, "last_assessment": None}
        self.save()

    def status_of(self, note_id: str) -> str:
        return (self.data.get(note_id) or {}).get("status", "open")

    def record(self, note: Note, *, sprint: int, status: str, assessment: dict | None,
               last_attempt: dict | None = None) -> None:
        """`last_attempt` ({changes, critique}) is kept only while the note stays open, so the
        next sprint on this note continues the discussion instead of restarting it."""
        entry = self.data.setdefault(note.id, {"status": "open", "sprints": [], "text_hash": note.text_hash})
        if sprint not in entry["sprints"]:
            entry["sprints"].append(sprint)
        entry["status"] = status
        entry["last_assessment"] = assessment
        entry["last_attempt"] = {**last_attempt, "origin": f"carried over from sprint {sprint}"} if (last_attempt and status == "open") else None
        self.save()

    def last_attempt(self, note_id: str) -> dict | None:
        return (self.data.get(note_id) or {}).get("last_attempt")

    def save(self) -> None:
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)


def next_note(notes: list[Note], status: NoteStatus) -> Note | None:
    """First open note — hard notes before direction notes, file order within each kind."""
    open_notes = [n for n in notes if status.status_of(n.id) == "open"]
    open_notes.sort(key=lambda n: NOTE_KINDS.index(n.kind))
    return open_notes[0] if open_notes else None


def resolve_status(*, note: Note, decision: str, assessment: dict | None, sprints_spent: int, max_sprints: int) -> str:
    """Status of the focus note after a steering sprint ends."""
    verdict = str((assessment or {}).get("status", "")).lower()
    # A hard note is fully realized when `upheld`, a direction note when `satisfied`.
    if decision == "accepted" and verdict in ("satisfied", "upheld"):
        return "resolved"
    if decision == "accepted" and verdict == "contested" and note.kind == "direction":
        return "declined"
    if sprints_spent >= max_sprints:
        return "stalled"
    return "open"


def notes_block(notes: list[Note], status: NoteStatus | None = None, focus: Note | None = None) -> str:
    """Prompt text given to every role whenever notes exist. Empty string when there are none."""
    if not notes:
        return ""
    lines = [
        "FUNDAMENTAL NOTES from the project lead (steering/notes.md). `hard` notes are constraints "
        "the language must converge to: no change may make one worse, and they cannot be contested. "
        "The current language may not satisfy them yet — they are realized one per sprint, in "
        "accepted increments. `direction` notes are goals — they may be contested only with "
        "concrete evidence, and the Critic rules on it. These notes take precedence over any default "
        "guidance in your instructions that they contradict."
    ]
    for n in notes:
        tag = " <- FOCUS OF THIS SPRINT" if focus and n.id == focus.id else ""
        st = f" (status: {status.status_of(n.id)})" if status else ""
        lines.append(f"- {n.describe()}{st}{tag}")
    return "\n".join(lines) + "\n"
