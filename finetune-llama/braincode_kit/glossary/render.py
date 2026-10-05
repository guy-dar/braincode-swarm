"""Render glossary.jsonl into glossary.md: one table row per record, grouped
by kind (values by category). It is both the human editing view (edit a
cell, then `python -m glossary.import_md`) and what models read, so it holds
the authored fields only — ids, versions, rule links and provenance stay in
glossary.jsonl / glossary-provenance.jsonl.

    python -m glossary.render            # renders reference/glossary.md
"""
import json
import sys
from pathlib import Path

from . import groups as groups_mod
from . import records as rec_mod

REF_DIR = rec_mod.REF_DIR
GLOSSARY_MD = REF_DIR / "glossary.md"
LANGUAGE_VERSION = "19.0.0-draft.2-lexical-groups"

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
    # Value groups (spec §3.1): the contract is spread over these columns and
    # folded back into the record's `group` field by import_md. Leaf values
    # are never rows: any admissible key is valid without an entry.
    ("Value groups", ("lexical_group",), ("symbol", "kind", "definition", "admission", "standard", "key_form",
                                          "examples", "key_aliases", "recognition", "members", "status")),
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


def group_cells(record: dict) -> dict:
    """The contract of a value group as table cells (defaults left blank)."""
    raw = record.get("group") or {}
    members = raw.get("members") or {}
    return {
        "admission": raw.get("admission", ""),
        "standard": raw.get("standard", ""),
        "key_form": raw.get("key_form", ""),
        "examples": ", ".join(raw.get("examples") or []),
        "key_aliases": ", ".join(f"{a}={t}" for a, t in (raw.get("key_aliases") or {}).items()),
        "recognition": "\n".join(raw.get("recognition") or []),
        "members": json.dumps(members, ensure_ascii=False, separators=(",", ":")) if members else "",
    }


def _value(record: dict, column: str):
    if record.get("kind") == "lexical_group" and column in groups_mod.GROUP_FIELDS:
        return group_cells(record).get(column, "")
    return record.get(column, "")


def _table(records: list, columns: tuple) -> list:
    lines = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
    for r in records:
        lines.append("| " + " | ".join(cell(_value(r, c)) for c in columns) + " |")
    return lines


def render_md(records: list, glossary_version: str = "") -> str:
    live = [r for r in records if r["status"] != "Deprecated"]
    lines = [
        "# BrainCode glossary",
        "",
        f"Language {LANGUAGE_VERSION} · glossary {glossary_version or 'unversioned'} · {len(live)} live records"
        + (f" ({len(records) - len(live)} deprecated, listed last)" if len(records) != len(live) else ""),
        "",
        # No shell commands in this header: the file is attached to model requests, and the model proxy's
        # firewall blocks request bodies containing "run `<command>`" as suspected command injection.
        # How to edit and re-import is documented in swarm/README.md.
        "Rendered from glossary.jsonl (the source of truth); see swarm/README.md for how to edit it. In cells, "
        "`<br>` is a line break and `\\|` a literal pipe. To deprecate, set status to `Deprecated` and give a "
        "reason in `not`. Signatures: `?` optional, `A / B` alternatives, `void` no result, `ATOM[g]` a value of "
        "group g written `g::key`. `not` is the nearest wrong reading of the symbol. Leaf values of a value group "
        "(object labels, colors, ISO country and currency codes) are not listed: any admissible key is valid.",
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


def compact_line(record: dict, slots: list = None) -> str:
    """One line per record — how retrieval context presents a record. A
    value group shows its contract (admission, key form, examples, aliases)
    and, when given, the signature slots that accept it."""
    if record.get("kind") == "lexical_group":
        g = groups_mod.contract(record)
        parts = [f"{record['symbol']}::<key>", "lexical_group", groups_mod.describe(record),
                 _one_line(record["definition"])]
        if g["examples"]:
            parts.append("e.g. " + ", ".join(g["examples"]))
        if g["key_aliases"]:
            parts.append("key aliases: " + ", ".join(f"{a}={t}" for a, t in g["key_aliases"].items()))
        if record.get("not"):
            parts.append("not: " + _one_line(record["not"]))
        if slots:
            parts.append("slots: " + ", ".join(f"{s}.{p}" for s, p in slots[:8]) + (" …" if len(slots) > 8 else ""))
        return " | ".join(parts)
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
