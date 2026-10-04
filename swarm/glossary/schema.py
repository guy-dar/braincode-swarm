"""The glossary record schema: one JSON object per line in reference/glossary.jsonl.

glossary.jsonl is the single source of truth. glossary.md (one table row per
record: the human editing view and what models read) is rendered from it by
render.py, and the RAG index (../rag/) is derived from it too. Who changed
what, and why, is kept out of the records, in glossary-provenance.jsonl.

A record is deliberately small. Only the fields a translator needs to *use*
a symbol are authored (by the migrator, or a person editing glossary.md):

  symbol, kind, category (values), signature, definition, not, aliases,
  expansion (composites), group (lexical groups, see groups.py), status

Leaf values of a value group are never records: `object_label::thimble` needs
no entry, and a group record carries at most 1-3 illustrative examples.

Everything else is maintained by the host: `id` (derived from kind/category/
symbol), `version`, `shared_rules` (assigned from kind/category),
`dependencies` (derived from signature/expansion), `related` (retrieval hints),
`mentions` (rules only), `superseded_by` / `deprecated` (deprecation), `core`,
and `code` (worked examples only).
"""
import re

ID_PREFIX = "v19/"

KINDS = (
    "value",            # STRING-typed vocabulary member of a category
    "operation",        # external Action, REQUEST signature (+ RECORD signature rule)
    "speech_act",       # UTTER act
    "constructor",      # primitive TERM constructor
    "composite",        # TERM constructor defined by an acyclic expansion
    "claim_relation",   # CLAIM predicate
    "link",             # LINK relation between claims
    "attribute",        # argument name, not a value
    "structural",       # grammar token
    "category_rule",    # contract shared by every member of one category
    "rule",             # any other shared rule (general reading rules, family rules)
    "example",          # a complete worked example document
    "lexical_group",    # an atomic value group (spec §3.1): `group::key` values, contract in `group`
)

STATUSES = (
    "Retained", "Adapted", "Composite", "Needs clarification", "Structural",
    "Accepted",         # added or confirmed by a swarm migration
    "Proposed",         # recorded but not yet usable in a frozen release
    "Deprecated",       # superseded; kept so old references still resolve
)

# The fields a migrator (or a person) writes. Everything else is host-maintained.
AUTHORED_FIELDS = ("symbol", "kind", "category", "signature", "definition", "not", "aliases", "expansion", "group",
                   "status")

# Every field, in serialization order.
FIELDS = (
    "id", "version", "symbol", "kind", "status", "category", "signature", "definition", "not", "aliases",
    "expansion", "group", "code", "dependencies", "shared_rules", "related", "mentions", "core", "superseded_by",
    "deprecated",
)

DEFAULTS = {
    "version": 1,
    "status": "Accepted",
    "category": "",
    "signature": "",
    "definition": "",
    "not": "",
    "aliases": [],
    "expansion": "",
    "group": {},
    "code": "",
    "dependencies": [],
    "shared_rules": [],
    "related": [],
    "mentions": [],
    "core": False,
    "superseded_by": [],
    "deprecated": "",
}
# Always written even when default, so every line is self-describing.
ALWAYS = {"id", "version", "symbol", "kind", "status", "definition"}

# Kinds whose meaning is a typed call shape: a signature is mandatory.
SIGNATURE_KINDS = {"operation", "speech_act", "constructor", "composite", "claim_relation", "link"}
RULE_KINDS = {"rule", "category_rule"}
# Kinds whose `symbol` must be a BrainCode identifier. Structural tokens
# (`{`, `->`) and rules/examples (slugs) are exempt.
IDENT_KINDS = {"value", "operation", "speech_act", "constructor", "composite",
               "claim_relation", "link", "attribute", "lexical_group"}

# Rules every record of a kind is governed by. Values add their category's rule.
KIND_RULES = {
    "operation": ["v19/rule/operations-general", "v19/rule/recording-signatures"],
    "speech_act": ["v19/rule/speech-acts-general"],
    "constructor": ["v19/rule/support-primitives-general"],
    "composite": ["v19/rule/composites-general"],
    "claim_relation": ["v19/rule/trace-relations-general"],
    "link": ["v19/rule/trace-relations-general"],
    "attribute": ["v19/rule/attributes-and-generate"],
    "example": ["v19/rule/examples-general"],
    "lexical_group": ["v19/rule/lexical-groups"],
}

IDENT_RE = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")
ID_RE = re.compile(r"^v19/\S+$")


def _join(*parts) -> str:
    return " ".join(p.strip() for p in parts if p and str(p).strip())


def normalize(record: dict) -> dict:
    """Fill defaults and order keys, without mutating the input. Records in
    the old, verbose layout are converted: restrictions fold into the
    definition, contrasts become `not`, an example's code moves to `code`,
    other usage examples and provenance are dropped (provenance lives in
    glossary-provenance.jsonl)."""
    record = dict(record)
    restrictions = record.pop("restrictions", None) or []
    examples = record.pop("examples", None) or {}
    record.pop("provenance", None)
    if restrictions:
        record["definition"] = _join(record.get("definition", ""),
                                     *(r if r.rstrip().endswith(".") else r.rstrip() + "." for r in restrictions))
    contrast = examples.get("contrast") or []
    if contrast and not record.get("not"):
        record["not"] = "; ".join(str(c).strip().rstrip(".") for c in contrast if str(c).strip())
    if record.get("kind") == "example" and not record.get("code") and examples.get("positive"):
        record["code"] = "\n\n".join(examples["positive"])
    if isinstance(record.get("not"), list):
        record["not"] = "; ".join(str(x) for x in record["not"])
    out = {}
    for field in FIELDS:
        if field in record:
            out[field] = record[field]
        elif field in DEFAULTS:
            default = DEFAULTS[field]
            out[field] = list(default) if isinstance(default, list) else default
    # Anything unknown is kept, after the known fields — a migrator adding a
    # field shouldn't have it silently dropped on the next render.
    for key, value in record.items():
        if key not in out:
            out[key] = value
    return out


def compact(record: dict) -> dict:
    """The record as stored: defaults omitted."""
    rec = normalize(record)
    return {k: v for k, v in rec.items() if k in ALWAYS or v != DEFAULTS.get(k, object())}


def derive_id(record: dict) -> str:
    """The stable id a record gets when its author doesn't give one."""
    sym, kind = record.get("symbol", ""), record.get("kind", "")
    if kind == "value" or (kind in ("attribute", "structural") and record.get("category")):
        return f"{ID_PREFIX}{record.get('category') or kind}/{sym}"
    if kind == "composite":
        return f"{ID_PREFIX}composite/{sym}"
    if kind in ("operation", "speech_act"):
        return f"{ID_PREFIX}operation-vocabulary/{sym}"
    if kind in ("rule", "category_rule"):
        return f"{ID_PREFIX}rule/{sym}"
    if kind == "example":
        return f"{ID_PREFIX}example/{sym}"
    if kind == "lexical_group":
        return f"{ID_PREFIX}lexical-group/{sym}"
    return f"{ID_PREFIX}support/{sym}"


def default_rules(record: dict, known_rule_ids) -> list:
    """The shared rules a record of this kind/category is governed by (only
    rules that exist)."""
    rules = []
    if record.get("category"):
        rules.append(f"{ID_PREFIX}rule/category/{record['category']}")
    rules += KIND_RULES.get(record.get("kind"), [])
    return [r for r in rules if r in known_rule_ids]


def record_errors(record: dict) -> list:
    """Per-record checks that need no other record. Cross-record checks
    (uniqueness, resolution, cycles) live in records.validate."""
    errors = []
    rid = record.get("id", "<no id>")
    if not isinstance(record.get("id"), str) or not ID_RE.match(record["id"]):
        errors.append(f"{rid}: id must look like 'v19/<category>/<symbol>'")
    if record.get("kind") not in KINDS:
        errors.append(f"{rid}: unknown kind {record.get('kind')!r}")
    if record.get("status") not in STATUSES:
        errors.append(f"{rid}: unknown status {record.get('status')!r}")
    symbol = record.get("symbol")
    if not isinstance(symbol, str) or not symbol:
        errors.append(f"{rid}: missing symbol")
    elif record.get("kind") in IDENT_KINDS and not IDENT_RE.match(symbol):
        errors.append(f"{rid}: symbol {symbol!r} is not a BrainCode identifier")
    if not str(record.get("definition") or "").strip():
        errors.append(f"{rid}: missing definition")
    if record.get("kind") in SIGNATURE_KINDS and not str(record.get("signature") or "").strip():
        errors.append(f"{rid}: kind {record.get('kind')} requires a signature")
    if record.get("kind") == "composite" and not str(record.get("expansion") or "").strip():
        errors.append(f"{rid}: composite requires an expansion")
    if record.get("kind") == "value" and not record.get("category"):
        errors.append(f"{rid}: value requires a category")
    if record.get("kind") == "lexical_group":
        from . import groups
        errors.extend(groups.contract_errors(record))
    elif record.get("group"):
        errors.append(f"{rid}: only a lexical_group has a `group` field")
    if record.get("status") == "Deprecated" and not (record.get("superseded_by") or record.get("deprecated")):
        errors.append(f"{rid}: Deprecated needs superseded_by or a `deprecated` reason")
    if not isinstance(record.get("version"), int) or record["version"] < 1:
        errors.append(f"{rid}: version must be a positive integer")
    for list_field in ("aliases", "dependencies", "shared_rules", "related", "mentions", "superseded_by"):
        if not isinstance(record.get(list_field, []), list):
            errors.append(f"{rid}: {list_field} must be a list")
    for text_field in ("definition", "not", "signature", "expansion"):
        if not isinstance(record.get(text_field, ""), str):
            errors.append(f"{rid}: {text_field} must be a string")
    return errors
