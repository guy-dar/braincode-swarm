"""Fold a family of leaf-value records into a value group (spec §3.1), as one
validated glossary revision.

A consolidation spec (reference/consolidations/<group>.json) names:
  group      the new lexical_group record (authored fields: symbol, definition,
             not, group {admission, key_form, examples, key_aliases, ...})
  slots      {record symbol: [param, ...]}: signatures that must accept
             ATOM[<group>] (` / ATOM[g]` is appended to each param's type)
  retire     {old symbol: new key}: leaf records deleted, written
             `<group>::<key>` from now on (null key = the old symbol)
  rewrite    {old symbol: new key}: extra text replacements inside other
             records (expansions, example code, contrasts), default = retire
  retire_rules  category rules that become empty

Leaf records are deleted (`retire`), never kept as entries; the previous
glossary is snapshotted to reference/history/<name>/, the retired symbols are
added to reference/retired-symbols.json (host-only: the check rejects them),
and provenance records every change.

    python -m glossary.consolidate reference/consolidations/platform_label.json --check
    python -m glossary.consolidate reference/consolidations/platform_label.json
"""
import json
import re
import shutil
import sys
from pathlib import Path

from . import groups as groups_mod
from . import manifest
from . import records as rec_mod
from . import render

REF = rec_mod.REF_DIR
RETIRED_MAP = REF / "retired-symbols.json"
PARAM_TYPE_RE = r"(\b{param}\??\s*:\s*)([^,()]*?)(\s*(?:,|\)|$))"


def add_atom_to_param(signature: str, param: str, group: str) -> str:
    """Append ` / ATOM[group]` to one parameter's type (idempotent)."""
    pattern = re.compile(PARAM_TYPE_RE.format(param=re.escape(param)))
    m = pattern.search(signature)
    if not m:
        raise SystemExit(f"consolidate: no parameter {param!r} in signature {signature!r}")
    if f"ATOM[{group}]" in m.group(2):
        return signature
    return signature[:m.start(2)] + m.group(2).rstrip() + f" / ATOM[{group}]" + signature[m.end(2):]


def rewrite_text(text: str, mapping: dict, group: str) -> str:
    """`django` -> `platform_label::django` for bare identifiers (not inside
    quotes, not already an atom, not an argument name)."""
    if not text:
        return text
    pieces = re.split(r'("(?:[^"\\]|\\.)*")', text)
    out = []
    for i, piece in enumerate(pieces):
        if i % 2:          # quoted literal: untouched
            out.append(piece)
            continue
        out.append(re.sub(r"(?<![\w:])([A-Za-z_][A-Za-z0-9_]*)(?![\w:])(?!\s*=(?!=))",
                          lambda m: f"{group}::{mapping[m.group(1)]}" if m.group(1) in mapping else m.group(1),
                          piece))
    return "".join(out)


def build(spec: dict, records: list) -> tuple:
    """(new records, report events, retired map entries)."""
    out = [dict(r) for r in records]
    by_symbol = {r["symbol"]: r for r in out}
    gdef = dict(spec["group"])
    gsym = gdef["symbol"]
    if gsym in by_symbol:
        raise SystemExit(f"consolidate: {gsym} already exists")
    retire = {old: (key or old) for old, key in spec["retire"].items()}
    missing = [s for s in retire if s not in by_symbol]
    if missing:
        raise SystemExit(f"consolidate: not in the glossary: {', '.join(missing)}")
    mapping = {**retire, **(spec.get("rewrite") or {})}
    report = []

    def ev(op, rid, outcome):
        report.append({"op": op, "target": rid, "targets": [rid], "suggestions": [], "translator_ids": [],
                       "outcome": outcome})

    # 1. the group record
    rule_ids = {r["id"] for r in out if r["kind"] in ("rule", "category_rule")}
    group_rec = rec_mod._new_record({**gdef, "kind": "lexical_group", "status": gdef.get("status", "Accepted")},
                                    rule_ids, 0)
    out.append(group_rec)
    ev("add", group_rec["id"], f"value group {gsym} (consolidates {len(retire)} leaf records)")
    # 2. consuming signatures
    for sym, params in spec["slots"].items():
        rec = by_symbol.get(sym)
        if rec is None:
            raise SystemExit(f"consolidate: slot owner {sym} not in the glossary")
        sig = rec["signature"]
        for param in params:
            sig = add_atom_to_param(sig, param, gsym)
        if sig != rec["signature"]:
            rec["signature"] = sig
            rec["version"] = int(rec.get("version", 1)) + 1
            ev("update", rec["id"], f"accepts ATOM[{gsym}] in {', '.join(params)}")
    # 3. text references in other records
    retired_ids = {by_symbol[s]["id"] for s in retire}
    for rec in out:
        if rec["id"] in retired_ids:
            continue
        changed = False
        for field in ("expansion", "code", "not", "definition"):
            value = rec.get(field)
            if isinstance(value, str) and value:
                new = rewrite_text(value, mapping, gsym)
                if new != value:
                    rec[field] = new
                    changed = True
        refs = [d for d in rec.get("dependencies") or [] if d in retired_ids]
        if refs:
            rec["dependencies"] = [d for d in rec["dependencies"] if d not in retired_ids]
            changed = True
        for field in ("related", "mentions"):
            if any(x in retired_ids for x in rec.get(field) or []):
                rec[field] = [x for x in rec[field] if x not in retired_ids]
                changed = True
        if changed and rec is not group_rec:
            rec["version"] = int(rec.get("version", 1)) + 1
            ev("update", rec["id"], f"references to retired leaf values now written {gsym}::<key>")
    # 4. retire the leaf records and emptied category rules
    retired_entries = {}
    for old, key in retire.items():
        rec = by_symbol[old]
        out.remove(rec)
        retired_entries[old] = {"old_id": rec["id"], "replacement": f"{gsym}::{key}"}
        ev("retire", rec["id"], f"retired: leaf value now written {gsym}::{key}")
    for rid in spec.get("retire_rules") or []:
        rule = next((r for r in out if r["id"] == rid), None)
        if rule is not None:
            out.remove(rule)
            ev("retire", rid, "retired: category rule emptied by the consolidation")
    for rec in out:
        rec["shared_rules"] = [r for r in rec.get("shared_rules") or [] if r not in set(spec.get("retire_rules") or [])]
    # 5. dependencies derived again (signatures now name the group)
    known = {r["symbol"]: r for r in out if r["status"] != "Deprecated"}
    for rec in out:
        if rec["status"] != "Deprecated":
            rec["dependencies"] = rec_mod.derive_dependencies(rec, known)
    return out, report, retired_entries


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        sys.exit(__doc__)
    spec_path = Path(argv[0])
    check_only = "--check" in argv
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    current = rec_mod.load()
    new, report, retired_entries = build(spec, current)
    errors = rec_mod.validate(new, previous=current, retired=rec_mod.retired_ids(report))
    gsym = spec["group"]["symbol"]
    print(f"consolidate {gsym}: {len(current)} -> {len(new)} records; {len(retired_entries)} leaf records retired; "
          f"{sum(e['op'] == 'update' for e in report)} records updated; {len(errors)} validation error(s)")
    for e in errors[:30]:
        print("  error:", e)
    print("  slots:", ", ".join(f"{s}.{p}" for s, p in groups_mod.consumers(new).get(gsym, [])))
    if errors:
        sys.exit(1)
    if check_only:
        return
    history = REF / "history" / f"consolidate-{gsym}"
    if history.exists():
        sys.exit(f"{history} exists: already consolidated")
    history.mkdir(parents=True)
    for name in ("glossary.jsonl", "glossary.md", "glossary-provenance.jsonl", "reference-manifest.json",
                 "retired-symbols.json"):
        if (REF / name).exists():
            shutil.copy2(REF / name, history / name)
    data = json.loads(RETIRED_MAP.read_text(encoding="utf-8")) if RETIRED_MAP.exists() else {"retired": {}}
    data["retired"].update(retired_entries)
    RETIRED_MAP.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    rec_mod.save(new)
    note = f"consolidate {gsym} ({spec_path.name})"
    rec_mod.append_provenance(rec_mod.provenance_events(report, None, note))
    version = manifest.bump_version(note=note)
    render.render_all(new, version)
    manifest.refresh()
    print(f"installed as glossary {version}; snapshot in {history.relative_to(REF.parent)}; "
          f"the RAG index rebuilds when the loop starts")


if __name__ == "__main__":
    main()
