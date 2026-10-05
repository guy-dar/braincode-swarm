"""Atomic value groups (spec §3.1): the `lexical_group` record kind.

A group record's `group` field holds its contract; omitted fields take the
§3.1 defaults. Leaf values are never glossary entries:

  open_label  any key of the right form is admissible (a source-supplied
              label: object_label::thimble); the record lists only 1-3
              illustrative examples, never a member list
  standard    keys are the codes of a bundled external standard
              (reference/standards/<name>.json, e.g. ISO 4217 for currency);
              valid iff the code is in that list; no members in the glossary
  registered  keys are the record's own pinned member map (kept for
              compatibility with the §3.1 contract; no group uses it now)

Where a group may appear is decided only by consumer signatures
(`target: STRING / ATOM[object_label]`); `consumers()` derives that map.
"""
import json
import re
from functools import lru_cache
from pathlib import Path

REF_DIR = Path(__file__).resolve().parent.parent / "reference"
STANDARDS_DIR = REF_DIR / "standards"

ADMISSIONS = ("open_label", "standard", "registered")
KEY_FORMS = {
    "lower_word": re.compile(r"^[a-z]+$"),
    "lower_identifier": re.compile(r"^[a-z][a-z0-9_]*$"),
    "upper_code": re.compile(r"^[A-Z][A-Z0-9]*$"),
}
DEFAULTS = {"admission": "open_label", "key_form": "lower_word", "key_aliases": {}, "members": {},
            "recognition": [], "examples": [], "standard": ""}
GROUP_FIELDS = set(DEFAULTS)

ATOM_RE = re.compile(r"\b([a-z][a-z0-9_]*)::([A-Za-z0-9_]*)")
ATOM_TYPE_RE = re.compile(r"ATOM\[\s*([A-Za-z_][A-Za-z0-9_]*)\s*\]")
# `name?: STRING / ATOM[g] / ...` inside a signature's parameter list
PARAM_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\??\s*:\s*([^,()]*(?:\([^)]*\)[^,()]*)*)")


def contract(record: dict) -> dict:
    """The record's group contract with every default filled in."""
    g = dict(DEFAULTS)
    g.update((record.get("group") or {}) if isinstance(record.get("group"), dict) else {})
    return g


def is_group(record: dict) -> bool:
    return record.get("kind") == "lexical_group"


@lru_cache(maxsize=None)
def _standard_codes(name: str, standards_dir: str) -> dict:
    path = Path(standards_dir) / f"{name}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return dict(data.get("codes") or {})


def standard_title(name: str, standards_dir: Path = None) -> str:
    """The standard's display name ("ISO 4217"), or its file name."""
    try:
        path = Path(standards_dir or STANDARDS_DIR) / f"{name}.json"
        return json.loads(path.read_text(encoding="utf-8")).get("standard") or name
    except (OSError, ValueError):
        return name


def standard_codes(name: str, standards_dir: Path = None) -> dict:
    """{code: English name} of a bundled standard; {} when it doesn't exist."""
    try:
        return _standard_codes(name, str(standards_dir or STANDARDS_DIR))
    except (OSError, ValueError):
        return {}


def contract_errors(record: dict, standards_dir: Path = None) -> list:
    """Problems with one group record's contract (spec §3.1)."""
    rid = record.get("id", "<no id>")
    raw = record.get("group")
    if not isinstance(raw, dict):
        return [f"{rid}: lexical_group requires a `group` object"]
    errors = [f"{rid}: unknown group field {k!r}" for k in raw if k not in GROUP_FIELDS]
    g = contract(record)
    admission, key_form = g["admission"], g["key_form"]
    if admission not in ADMISSIONS:
        return errors + [f"{rid}: admission must be one of {', '.join(ADMISSIONS)}"]
    if key_form not in KEY_FORMS:
        return errors + [f"{rid}: key_form must be one of {', '.join(KEY_FORMS)}"]
    key_re = KEY_FORMS[key_form]
    members = g["members"] if isinstance(g["members"], dict) else {}
    if admission == "open_label":
        if key_form not in ("lower_word", "lower_identifier"):
            errors.append(f"{rid}: an open_label group uses key_form lower_word (or lower_identifier for names)")
        if members:
            errors.append(f"{rid}: an open_label group lists no members (examples only)")
    elif admission == "standard":
        if members:
            errors.append(f"{rid}: a standard group lists no members (the standard is the list)")
        if not g["standard"]:
            errors.append(f"{rid}: a standard group names its `standard` (reference/standards/<name>.json)")
        elif not standard_codes(g["standard"], standards_dir):
            errors.append(f"{rid}: standard {g['standard']!r} has no bundled code list")
    elif admission == "registered" and not members:
        errors.append(f"{rid}: a registered group needs members")
    examples = g["examples"] if isinstance(g["examples"], list) else []
    if not 1 <= len(examples) <= 3:
        errors.append(f"{rid}: give 1-3 illustrative examples")
    for ex in examples:
        m = ATOM_RE.fullmatch(str(ex))
        if not m or m.group(1) != record.get("symbol"):
            errors.append(f"{rid}: example {ex!r} is not {record.get('symbol')}::<key>")
        elif not key_re.match(m.group(2)):
            errors.append(f"{rid}: example key {m.group(2)!r} does not match {key_form}")
    aliases = g["key_aliases"] if isinstance(g["key_aliases"], dict) else {}
    for alias, target in aliases.items():
        if not key_re.match(str(alias)) or not key_re.match(str(target)):
            errors.append(f"{rid}: alias {alias!r} -> {target!r} does not match {key_form}")
        if target in aliases:
            errors.append(f"{rid}: alias {alias!r} points at another alias {target!r} (no chains)")
        if alias in members:
            errors.append(f"{rid}: alias {alias!r} collides with a member key")
        if admission == "registered" and target not in members:
            errors.append(f"{rid}: alias target {target!r} is not a member")
        if admission == "standard" and g["standard"] and target not in standard_codes(g["standard"], standards_dir):
            errors.append(f"{rid}: alias target {target!r} is not a {g['standard']} code")
    seen = {}
    for key, member in members.items():
        if not key_re.match(str(key)):
            errors.append(f"{rid}: member key {key!r} does not match {key_form}")
        sense = (member or {}).get("sense_id") if isinstance(member, dict) else None
        if not sense or not (member or {}).get("definition"):
            errors.append(f"{rid}: member {key!r} needs sense_id and definition")
        elif sense in seen:
            errors.append(f"{rid}: members {seen[sense]!r} and {key!r} share sense_id {sense}")
        else:
            seen[sense] = key
    return errors


def member_changes(old: dict, new: dict) -> list:
    """Registered members (or standards) a revision may not silently change."""
    rid = new.get("id")
    o, n = contract(old), contract(new)
    errors = []
    if o["admission"] == "standard" and n["admission"] == "standard" and o["standard"] != n["standard"]:
        errors.append(f"{rid}: changing the standard ({o['standard']} -> {n['standard']}) needs a migration")
    for key, member in (o["members"] or {}).items():
        if key not in (n["members"] or {}):
            errors.append(f"{rid}: member {key!r} was dropped; keep the complete member map")
        elif (n["members"][key] or {}).get("sense_id") != (member or {}).get("sense_id"):
            errors.append(f"{rid}: member {key!r} changed its sense_id")
    return errors


def groups_by_symbol(records: list) -> dict:
    return {r["symbol"]: r for r in records if is_group(r) and r.get("status") != "Deprecated"}


def normalize_key(group_record: dict, key: str):
    """The canonical key (explicit aliases only), or None if not admissible."""
    g = contract(group_record)
    key_re = KEY_FORMS.get(g["key_form"], KEY_FORMS["lower_word"])
    key = g["key_aliases"].get(key, key) if isinstance(g["key_aliases"], dict) else key
    if not key_re.match(key or ""):
        return None
    if g["admission"] == "standard" and key not in standard_codes(g["standard"]):
        return None
    if g["admission"] == "registered" and key not in (g["members"] or {}):
        return None
    return key


def check_atom(groups: dict, group: str, key: str) -> tuple:
    """(status, message): status is ok | alias | unknown_group | bad_key |
    not_in_standard | unregistered. Only `ok` and `alias` are admissible;
    `alias` asks for the canonical spelling."""
    rec = groups.get(group)
    if rec is None:
        return "unknown_group", f"{group}::{key}: no value group `{group}` in this glossary"
    g = contract(rec)
    key_re = KEY_FORMS.get(g["key_form"], KEY_FORMS["lower_word"])
    aliases = g["key_aliases"] if isinstance(g["key_aliases"], dict) else {}
    canonical = aliases.get(key, key)
    if not key_re.match(canonical or ""):
        hint = " (ISO codes are upper case)" if g["key_form"] == "upper_code" else ""
        return "bad_key", f"{group}::{key}: key must match {g['key_form']}{hint}"
    if g["admission"] == "standard":
        codes = standard_codes(g["standard"])
        if canonical not in codes:
            return "not_in_standard", f"{group}::{key}: `{key}` is not an {standard_title(g['standard'])} code"
    if g["admission"] == "registered" and canonical not in (g["members"] or {}):
        return "unregistered", f"{group}::{key}: `{key}` is not a registered member of {group}"
    if canonical != key:
        return "alias", f"{group}::{key}: write the canonical {group}::{canonical}"
    return "ok", ""


def signature_slots(signature: str) -> list:
    """[(param, [group, ...])] for every parameter that admits ATOM[g]."""
    if not signature or "ATOM[" not in signature:
        return []
    start, end = signature.find("("), signature.rfind(")")
    params = signature[start + 1:end] if start >= 0 and end > start else signature
    out = []
    for name, typ in PARAM_RE.findall(params):
        found = ATOM_TYPE_RE.findall(typ)
        if found:
            out.append((name, found))
    return out


def consumers(records: list) -> dict:
    """{group symbol: [(record symbol, param)]} from every live signature."""
    out = {}
    for r in records:
        if r.get("status") == "Deprecated":
            continue
        for param, groups in signature_slots(r.get("signature") or ""):
            for g in groups:
                out.setdefault(g, []).append((r["symbol"], param))
    return out


def describe(record: dict, max_examples: int = 3) -> str:
    """`open label, lower_word` / `ISO 4217 code, upper_code`."""
    g = contract(record)
    if g["admission"] == "standard":
        codes = standard_codes(g["standard"])
        return f"{standard_title(g['standard'])} codes ({len(codes)}), {g['key_form']}"
    if g["admission"] == "registered":
        return f"registered ({len(g['members'] or {})} members), {g['key_form']}"
    return f"open label, {g['key_form']}"


def catalog_line(record: dict, slots: list = None, max_slots: int = 8) -> str:
    """One compact line for the always-present group catalog."""
    g = contract(record)
    examples = ", ".join((g["examples"] or [])[:3])
    line = f"`{record['symbol']}::<key>` — {describe(record)} — {' '.join(str(record.get('definition', '')).split())}"
    if examples:
        line += f" e.g. {examples}"
    if slots:
        shown = ", ".join(f"{s}.{p}" for s, p in slots[:max_slots])
        line += f" | slots: {shown}" + (" …" if len(slots) > max_slots else "")
    return line


def catalog_lines(records: list) -> list:
    groups = groups_by_symbol(records)
    used_by = consumers(records)
    return [catalog_line(groups[s], used_by.get(s, [])) for s in sorted(groups)]
