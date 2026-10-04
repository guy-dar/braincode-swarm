"""Render glossary.jsonl into glossary.md: one table row per record, grouped
by kind (values by category). It is both the human editing view (edit a
cell, then `python -m glossary.import_md`) and what models read, so it holds
the authored fields only — ids, versions, rule links and provenance stay in
glossary.jsonl / glossary-provenance.jsonl.

    python -m glossary.render            # renders reference/glossary.md
"""
import sys
from pathlib import Path

from . import records as rec_mod

REF_DIR = rec_mod.REF_DIR
GLOSSARY_MD = REF_DIR / "glossary.md"
LANGUAGE_VERSION = "19.0.0-draft.1"

# (section title, kinds, columns). Columns are record field names; the
# importer reads them back by header, so a table's columns define its fields.
ITEM_COLUMNS = ("symbol", "kind", "signature", "definition", "not", "aliases", "expansion", "status")
SECTIONS = (
    ("Shared rules", ("rule",), ("symbol", "kind", "definition")),
    ("Operations", ("operation",), ITEM_COLUMNS),
    ("Speech acts", ("speech_act",), ITEM_COLUMNS),
    ("Constructors", ("constructor",), ITEM_COLUMNS),
    ("Claim relations and links", ("claim_relation", "link"), ITEM_COLUMNS),
    ("Composite definitions", ("composite",), ITEM_COLUMNS),
    ("Values by category", ("category_rule", "value"), ("symbol", "kind", "category", "definition", "not", "aliases", "status")),
    ("Attributes", ("attribute",), ("symbol", "kind", "category", "definition", "aliases", "status")),
    ("Structural tokens", ("structural",), ("symbol", "kind", "category", "definition", "status")),
    ("Worked examples", ("example",), ("symbol", "kind", "definition", "code")),
)
DEFAULT_STATUSES = {"Retained", "Adapted", "Accepted", "Structural", "Composite"}


def cell(value) -> str:
    if isinstance(value, list):
        value = ", ".join(str(v) for v in value)
    text = str(value or "")
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\r\n", "\n").replace("\n", "<br>")


def _table(records: list, columns: tuple) -> list:
    lines = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
    for r in records:
        lines.append("| " + " | ".join(cell(r.get(c, "")) for c in columns) + " |")
    return lines


def render_md(records: list, glossary_version: str = "") -> str:
    live = [r for r in records if r["status"] != "Deprecated"]
    lines = [
        "# BrainCode glossary",
        "",
        f"Language {LANGUAGE_VERSION} · glossary {glossary_version or 'unversioned'} · {len(live)} live records"
        + (f" ({len(records) - len(live)} deprecated, listed last)" if len(records) != len(live) else ""),
        "",
        "Rendered from `glossary.jsonl` by `python -m glossary.render`. To edit: change a table cell (`<br>` = line "
        "break, `\\|` = a literal pipe) and run `python -m glossary.import_md`. To deprecate, set status to "
        "`Deprecated` and give a reason in `not`; never delete a row. Signatures: `?` optional, `A / B` "
        "alternatives, `void` no result. `not` is the nearest wrong reading of the symbol.",
        "",
    ]
    for title, kinds, columns in SECTIONS:
        group = [r for r in live if r["kind"] in kinds]
        if not group:
            continue
        lines += [f"## {title}", ""]
        if "category" in columns and kinds[0] == "category_rule":
            for category in sorted({r["category"] for r in group}):
                members = sorted((r for r in group if r["category"] == category),
                                 key=lambda r: (r["kind"] != "category_rule", r["symbol"]))
                lines += [f"### {category}", ""] + _table(members, columns) + [""]
            continue
        group.sort(key=lambda r: (not r.get("core"), r.get("category", ""), r["symbol"]))
        lines += _table(group, columns) + [""]
    dead = [r for r in records if r["status"] == "Deprecated"]
    if dead:
        lines += ["## Deprecated", ""] + _table(dead, ("symbol", "kind", "category", "definition", "deprecated",
                                                       "superseded_by", "status")) + [""]
    return "\n".join(lines)


def _one_line(text: str) -> str:
    return " ".join(str(text or "").split())


def compact_line(record: dict) -> str:
    """One line per record — how retrieval context presents a record."""
    parts = [record["symbol"], record["kind"]]
    if record.get("category"):
        parts.append(record["category"])
    if record.get("signature"):
        parts.append(_one_line(record["signature"]))
    parts.append(_one_line(record["definition"]))
    if record.get("expansion"):
        parts.append("= " + _one_line(record["expansion"]))
    if record.get("not"):
        parts.append("not: " + _one_line(record["not"]))
    if record.get("aliases"):
        parts.append("aliases: " + ", ".join(record["aliases"]))
    if record["status"] not in DEFAULT_STATUSES:
        parts.append("STATUS " + record["status"])
    if record.get("superseded_by"):
        parts.append("use instead: " + ", ".join(record["superseded_by"]))
    return " | ".join(parts)


def render_all(records: list, glossary_version: str = "", ref_dir: Path = REF_DIR) -> None:
    (ref_dir / "glossary.md").write_text(render_md(records, glossary_version), encoding="utf-8", newline="\n")
    stale = ref_dir / "glossary-compact.txt"   # superseded by the compact glossary.md
    if stale.exists():
        stale.unlink()


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    path = Path(argv[0]) if argv else rec_mod.GLOSSARY_JSONL
    records = rec_mod.load(path)
    from . import manifest
    render_all(records, manifest.current_version(), path.parent)
    print(f"rendered {len(records)} records -> glossary.md")


if __name__ == "__main__":
    main()
