"""Load, validate, and change glossary records.

Every change to the glossary goes through apply_ops — the migrator never
edits glossary.jsonl directly, it emits operations (doc_formats/migration_ops.md)
and this module applies them, bumps versions, records provenance events and
validates the result before anything is installed.

    python -m glossary.records validate [path]
"""
import copy
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import schema

REF_DIR = Path(__file__).resolve().parent.parent / "reference"
GLOSSARY_JSONL = REF_DIR / "glossary.jsonl"
PROVENANCE_JSONL = REF_DIR / "glossary-provenance.jsonl"

TOKEN_RE = re.compile(r"\$?[A-Za-z_][A-Za-z0-9_]*")
QUOTED_RE = re.compile(r'"(?:[^"\\]|\\.)*"')
# Kinds a dependency may point at. Attributes and grammar tokens are named
# everywhere and carry no meaning a reader needs pulled in alongside.
DEPENDABLE_KINDS = {"value", "operation", "speech_act", "constructor", "composite",
                    "claim_relation", "link"}


# ---------------------------------------------------------------------------- io

def load(path: Path = GLOSSARY_JSONL) -> list:
    records = []
    with Path(path).open(encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(schema.normalize(json.loads(line)))
            except ValueError as e:
                raise ValueError(f"{path}:{n}: invalid JSON: {e}") from None
    return records


def dumps(records: list) -> str:
    return "".join(json.dumps(schema.compact(r), ensure_ascii=False) + "\n" for r in records)


def save(records: list, path: Path = GLOSSARY_JSONL) -> None:
    Path(path).write_text(dumps(records), encoding="utf-8", newline="\n")


def sha256_of(records: list) -> str:
    return hashlib.sha256(dumps(records).encode("utf-8")).hexdigest()


def by_id(records: list) -> dict:
    return {r["id"]: r for r in records}


def symbol_index(records: list) -> dict:
    return {r["symbol"]: r for r in records}


def resolve(records: list, key: str):
    """A record by id, symbol, or alias-free case-insensitive symbol."""
    ids = by_id(records)
    if key in ids:
        return ids[key]
    syms = symbol_index(records)
    if key in syms:
        return syms[key]
    lowered = {s.lower(): r for s, r in syms.items()}
    return lowered.get(key.lower())


# ---------------------------------------------------------------------------- derivation

def referenced_symbols(text: str, known: dict) -> list:
    """Glossary symbols named in a signature/expansion/code text, excluding
    quoted literals, `$parameter` copies and argument names (`name=`)."""
    if not text:
        return []
    stripped = QUOTED_RE.sub(" ", text)
    found = []
    for m in TOKEN_RE.finditer(stripped):
        token = m.group(0)
        if token.startswith("$"):
            continue
        rest = stripped[m.end():].lstrip()
        if rest.startswith("=") and not rest.startswith("=="):
            continue  # argument name
        rec = known.get(token)
        if rec is not None and rec["kind"] in DEPENDABLE_KINDS and token not in found:
            found.append(token)
    return found


def derive_dependencies(record: dict, known: dict) -> list:
    """Ids this record's expansion/signature/example code depends on, merged
    with any dependencies it already declares. A record never depends on itself."""
    texts = [record.get("expansion") or "", record.get("signature") or ""]
    if record.get("kind") == "example":
        texts.append(record.get("code") or "")
    deps = list(record.get("dependencies") or [])
    for text in texts:
        for sym in referenced_symbols(text, known):
            rid = known[sym]["id"]
            if rid != record["id"] and rid not in deps:
                deps.append(rid)
    return deps


# ---------------------------------------------------------------------------- validation

def _cycles(records: list) -> list:
    ids = by_id(records)
    graph = {r["id"]: [d for d in r.get("dependencies", []) if d in ids]
             for r in records if r["kind"] not in schema.RULE_KINDS and r["kind"] != "example"}
    WHITE, GREY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}
    cycles = []

    def visit(node, path):
        color[node] = GREY
        for dep in graph.get(node, []):
            if dep not in graph:
                continue
            if color[dep] == GREY:
                cycles.append(path[path.index(dep):] + [dep] if dep in path else [node, dep])
            elif color[dep] == WHITE:
                visit(dep, path + [dep])
        color[node] = BLACK

    sys.setrecursionlimit(max(10000, sys.getrecursionlimit()))
    for node in graph:
        if color[node] == WHITE:
            visit(node, [node])
    return cycles


def validate(records: list, previous: list = None) -> list:
    """Every problem with this glossary, as human-readable strings. Empty
    means valid. With `previous`, also enforces that nothing was removed:
    the glossary only ever deprecates."""
    errors = []
    for r in records:
        errors.extend(schema.record_errors(r))

    seen_ids, seen_symbols = {}, {}
    for r in records:
        if r["id"] in seen_ids:
            errors.append(f"duplicate id {r['id']}")
        seen_ids[r["id"]] = r
        if r["symbol"] in seen_symbols:
            errors.append(f"duplicate symbol {r['symbol']!r} ({seen_symbols[r['symbol']]['id']} and {r['id']})")
        seen_symbols[r["symbol"]] = r

    for r in records:
        for dep in r.get("dependencies", []):
            if dep not in seen_ids:
                errors.append(f"{r['id']}: dependency {dep} does not resolve")
        for rule in r.get("shared_rules", []):
            target = seen_ids.get(rule)
            if target is None:
                errors.append(f"{r['id']}: shared rule {rule} does not resolve")
            elif target["kind"] not in schema.RULE_KINDS:
                errors.append(f"{r['id']}: shared rule {rule} is a {target['kind']}, not a rule")
        for rel in r.get("related", []):
            if rel not in seen_ids:
                errors.append(f"{r['id']}: related {rel} does not resolve")
        for sup in r.get("superseded_by", []):
            if sup not in seen_ids:
                errors.append(f"{r['id']}: superseded_by {sup} does not resolve")
        if r["status"] != "Deprecated":
            for dep in r.get("dependencies", []):
                if seen_ids.get(dep, {}).get("status") == "Deprecated":
                    errors.append(f"{r['id']}: depends on deprecated {dep}; point it at the replacement")

    for cycle in _cycles(records):
        errors.append("dependency cycle: " + " -> ".join(cycle))

    if previous is not None:
        current = set(seen_ids)
        for old in previous:
            if old["id"] not in current:
                errors.append(f"{old['id']} was removed; deprecate it instead (status Deprecated + superseded_by)")
    return errors


# ---------------------------------------------------------------------------- operations

OP_KINDS = ("add", "update", "merge", "split", "deprecate", "reject")
# Host-maintained: an op can't set these directly.
IMMUTABLE_FIELDS = {"id", "version"}
LIST_MERGE_FIELDS = {"aliases", "related"}


class OpError(ValueError):
    pass


def _suggestions_of(op: dict) -> list:
    raw = op.get("suggestions", op.get("suggestion", []))
    return [raw] if isinstance(raw, str) else list(raw or [])


def translators_of(suggestions: list) -> list:
    out = []
    for s in suggestions:
        tid = s.split("#", 1)[0]
        if tid and tid not in out:
            out.append(tid)
    return out


def _bump(record: dict):
    record["version"] = int(record.get("version", 1)) + 1


def _rewrite_references(records: list, old_id: str, new_ids: list):
    """Point every dependency on old_id at its replacement(s)."""
    for r in records:
        if r["status"] == "Deprecated":
            continue
        deps = r.get("dependencies", [])
        if old_id in deps:
            new = []
            for d in deps:
                for nd in ([*new_ids] if d == old_id else [d]):
                    if nd not in new and nd != r["id"]:
                        new.append(nd)
            r["dependencies"] = new


def _new_record(raw: dict, rule_ids: set, op_index: int) -> dict:
    """An authored record completed by the host: id derived when absent,
    shared rules assigned from kind/category (plus any valid ones given),
    version 1."""
    if not isinstance(raw, dict) or not raw.get("symbol") or not raw.get("kind"):
        raise OpError(f"op {op_index}: a new record needs at least `symbol` and `kind`")
    rec = schema.normalize(raw)
    rec["id"] = raw.get("id") or schema.derive_id(rec)
    given = [r for r in rec.get("shared_rules") or [] if r in rule_ids]
    rec["shared_rules"] = given + [r for r in schema.default_rules(rec, rule_ids) if r not in given]
    rec["version"] = 1
    return rec


def apply_ops(records: list, ops: list, batch=None, migration_ref: str = "") -> tuple:
    """Apply migration operations to a deep copy of `records`.

    Returns (new_records, report) where report is a list of
    {op, target, targets, suggestions, translator_ids, outcome} dicts — also
    the provenance events written to glossary-provenance.jsonl on install.
    Raises OpError for an op that cannot be applied at all (unknown id,
    malformed op); validation of the *result* is the caller's job (validate()).
    """
    out = copy.deepcopy(records)
    ids = by_id(out)
    rule_ids = {r["id"] for r in out if r["kind"] in schema.RULE_KINDS}
    report = []

    def get(rid, op_index):
        rec = ids.get(rid) or symbol_index(out).get(rid)
        if rec is None:
            raise OpError(f"op {op_index}: no record {rid!r}")
        return rec

    def event(kind, target, sugg, outcome, targets=None):
        report.append({"op": kind, "target": target, "targets": targets or ([target] if target else []),
                       "suggestions": sugg, "translator_ids": translators_of(sugg), "outcome": outcome})

    for i, op in enumerate(ops, 1):
        kind = op.get("op")
        sugg = _suggestions_of(op)
        if kind not in OP_KINDS:
            raise OpError(f"op {i}: unknown op {kind!r} (expected one of {', '.join(OP_KINDS)})")

        if kind == "reject":
            if not op.get("reason"):
                raise OpError(f"op {i}: reject needs a reason")
            event(kind, None, sugg, op["reason"])
            continue

        if kind == "add":
            rec = _new_record(op.get("record"), rule_ids, i)
            if rec["id"] in ids:
                raise OpError(f"op {i}: add of existing id {rec['id']} (use update)")
            out.append(rec)
            ids[rec["id"]] = rec
            if rec["kind"] in schema.RULE_KINDS:
                rule_ids.add(rec["id"])
            event(kind, rec["id"], sugg, "added")

        elif kind == "update":
            rec = get(op.get("id"), i)
            changes = op.get("set") or {}
            appends = op.get("append") or {}
            if not changes and not appends:
                raise OpError(f"op {i}: update needs `set` or `append`")
            bad = IMMUTABLE_FIELDS & set(changes)
            if bad:
                raise OpError(f"op {i}: cannot set {sorted(bad)}")
            for field, value in changes.items():
                rec[field] = value
            for field, value in appends.items():
                if field not in LIST_MERGE_FIELDS:
                    raise OpError(f"op {i}: append only supports {sorted(LIST_MERGE_FIELDS)}")
                rec[field] = list(rec.get(field) or []) + [v for v in value if v not in (rec.get(field) or [])]
            _bump(rec)
            event(kind, rec["id"], sugg, (op.get("reason") or "updated") + " ["
                  + ", ".join(sorted(set(changes) | set(appends))) + "]")

        elif kind == "merge":
            into = get(op.get("into"), i)
            sources = [get(s, i) for s in (op.get("from") or [])]
            if not sources:
                raise OpError(f"op {i}: merge needs `from`")
            for src in sources:
                if src["id"] == into["id"]:
                    raise OpError(f"op {i}: cannot merge {src['id']} into itself")
                for alias in [src["symbol"].replace("_", " "), *src.get("aliases", [])]:
                    if alias not in into["aliases"]:
                        into["aliases"].append(alias)
                src["status"] = "Deprecated"
                src["superseded_by"] = [into["id"]]
                src["deprecated"] = op.get("notes") or f"merged into {into['id']}"
                _bump(src)
                _rewrite_references(out, src["id"], [into["id"]])
            for field, value in (op.get("set") or {}).items():
                if field in IMMUTABLE_FIELDS:
                    raise OpError(f"op {i}: cannot set {field}")
                into[field] = value
            _bump(into)
            event(kind, into["id"], sugg, "merged " + ", ".join(s["id"] for s in sources),
                  targets=[into["id"]] + [s["id"] for s in sources])

        elif kind == "split":
            src = get(op.get("id"), i)
            new_records = [_new_record(r, rule_ids, i) for r in (op.get("into") or [])]
            if len(new_records) < 2:
                raise OpError(f"op {i}: split needs at least two records in `into`")
            new_ids = []
            for rec in new_records:
                if rec["id"] in ids:
                    raise OpError(f"op {i}: split target {rec['id']} already exists")
                out.append(rec)
                ids[rec["id"]] = rec
                new_ids.append(rec["id"])
            src["status"] = "Deprecated"
            src["superseded_by"] = new_ids
            src["deprecated"] = op.get("notes") or "split"
            _bump(src)
            # A split can't know which half each dependent meant; references
            # are kept on the old id only if the op says how to re-point them.
            for dependent, target in (op.get("repoint") or {}).items():
                dep_rec = get(dependent, i)
                dep_rec["dependencies"] = [target if d == src["id"] else d for d in dep_rec["dependencies"]]
            event(kind, src["id"], sugg, "split into " + ", ".join(new_ids), targets=[src["id"], *new_ids])

        elif kind == "deprecate":
            rec = get(op.get("id"), i)
            if not op.get("reason"):
                raise OpError(f"op {i}: deprecate needs a reason")
            rec["status"] = "Deprecated"
            rec["superseded_by"] = list(op.get("superseded_by") or [])
            rec["deprecated"] = op["reason"]
            _bump(rec)
            if rec["superseded_by"]:
                _rewrite_references(out, rec["id"], rec["superseded_by"])
            event(kind, rec["id"], sugg, "deprecated: " + op["reason"])

    # Re-derive dependencies for anything touched, so a new composite's
    # expansion is linked without the migrator having to list every id.
    known = {r["symbol"]: r for r in out if r["status"] != "Deprecated"}
    touched = {t for e in report for t in e["targets"]}
    for r in out:
        if r["id"] in touched and r["status"] != "Deprecated":
            r["dependencies"] = derive_dependencies(r, known)
    return out, report


def provenance_events(report: list, batch, migration_ref: str) -> list:
    """glossary-provenance.jsonl lines for an applied migration."""
    at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return [{"at": at, "batch": batch, "migration": migration_ref, "op": e["op"], "ids": e["targets"],
             "suggestions": e["suggestions"], "translator_ids": e["translator_ids"], "outcome": e["outcome"]}
            for e in report]


def append_provenance(events: list, path: Path = None) -> None:
    path = Path(path) if path else PROVENANCE_JSONL
    with path.open("a", encoding="utf-8", newline="\n") as fh:
        for e in events:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] != "validate":
        sys.exit("usage: python -m glossary.records validate [glossary.jsonl]")
    path = Path(argv[1]) if len(argv) > 1 else GLOSSARY_JSONL
    records = load(path)
    errors = validate(records)
    for e in errors:
        print(e)
    print(f"{len(records)} records, {len(errors)} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
