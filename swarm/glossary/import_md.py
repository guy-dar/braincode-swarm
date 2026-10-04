"""Read a hand-edited glossary.md back into glossary.jsonl.

glossary.md is a set of tables whose headers are record field names, so each
row maps back to a record by `symbol`. Only the columns shown are taken from
the file; host-maintained fields (id, version, rule links, dependencies…) are
kept from the current glossary.jsonl. A new row becomes a new record (id and
shared rules assigned by the host). Changed records get their version bumped
and a provenance event; the result is validated (nothing removed) before
anything is written.

    python -m glossary.import_md               # reference/glossary.md -> reference/glossary.jsonl
    python -m glossary.import_md --check       # validate only, write nothing
"""
import copy
import re
import sys

from . import records as rec_mod
from . import schema

LIST_COLUMNS = {"aliases", "superseded_by"}


def _uncell(text: str) -> str:
    out, i = [], 0
    text = text.strip()
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text) and text[i + 1] in "|\\":
            out.append(text[i + 1])
            i += 2
            continue
        out.append(text[i])
        i += 1
    return "".join(out).replace("<br>", "\n")


def _split_row(line: str) -> list:
    cells, cur, i = [], [], 0
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|") and not body.endswith("\\|"):
        body = body[:-1]
    while i < len(body):
        if body[i] == "\\" and i + 1 < len(body):
            cur.append(body[i:i + 2])
            i += 2
            continue
        if body[i] == "|":
            cells.append("".join(cur))
            cur = []
        else:
            cur.append(body[i])
        i += 1
    cells.append("".join(cur))
    return [_uncell(c) for c in cells]


def parse_md(text: str) -> list:
    """[{column: value}] for every table row (header = field names)."""
    rows, header = [], None
    lines = text.replace("\r\n", "\n").split("\n")
    for i, line in enumerate(lines):
        if not line.startswith("|"):
            header = None
            continue
        if header is None:
            if i + 1 < len(lines) and re.match(r"^\|(\s*-+\s*\|)+\s*$", lines[i + 1]):
                header = [h.strip() for h in _split_row(line)]
            continue
        if re.match(r"^\|(\s*-+\s*\|)+\s*$", line):
            continue
        values = _split_row(line)
        row = {}
        for name, value in zip(header, values):
            row[name] = ([v.strip() for v in value.split(",") if v.strip()] if name in LIST_COLUMNS else value)
        if row.get("symbol"):
            rows.append(row)
    return rows


def merge_edits(current: list, rows: list) -> tuple:
    """Apply table rows onto the current records. Returns (records, changed_ids)."""
    out = copy.deepcopy(current)
    by_symbol = {r["symbol"]: r for r in out}
    rule_ids = {r["id"] for r in out if r["kind"] in schema.RULE_KINDS}
    changed = []
    for row in rows:
        rec = by_symbol.get(row["symbol"])
        if rec is None:
            new = schema.normalize({k: v for k, v in row.items() if k in schema.FIELDS})
            new["id"] = schema.derive_id(new)
            new["shared_rules"] = schema.default_rules(new, rule_ids)
            out.append(new)
            by_symbol[new["symbol"]] = new
            changed.append(new["id"])
            continue
        before = {k: rec.get(k) for k in row}
        for field, value in row.items():
            if field in schema.FIELDS and field not in ("id", "version"):
                rec[field] = value
        if any(before[k] != rec.get(k) for k in row):
            rec["version"] = int(rec.get("version", 1)) + 1
            changed.append(rec["id"])
    return out, changed


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    check_only = "--check" in argv
    md_path = rec_mod.REF_DIR / "glossary.md"
    current = rec_mod.load()
    records, changed = merge_edits(current, parse_md(md_path.read_text(encoding="utf-8")))
    errors = rec_mod.validate(records, previous=current)
    for e in errors:
        print("error:", e)
    print(f"{len(records)} records, {len(changed)} changed: {', '.join(changed[:20])}")
    if errors:
        sys.exit(1)
    if check_only or not changed:
        return
    rec_mod.save(records)
    rec_mod.append_provenance([{"at": None, "batch": None, "migration": "manual edit of glossary.md",
                                "op": "edit", "ids": changed, "suggestions": [], "translator_ids": [],
                                "outcome": "manual edit"}])
    from . import manifest, render
    version = manifest.bump_version(note="manual edit of glossary.md")
    render.render_all(records, version)
    manifest.refresh()
    print("wrote glossary.jsonl and re-rendered glossary.md; rebuild the RAG index with `python -m rag.cli build`")


if __name__ == "__main__":
    main()
