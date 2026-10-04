"""One-time install of the lexical-groups language release
(reference/proposed-lexical-groups/, built on glossary g14).

Differences from the proposal, decided when adopting it:
  - country and currency are `standard` groups keyed by ISO 3166-1 alpha-2 /
    ISO 4217 codes (reference/standards/*.json), not registered member lists:
    leaf values are never glossary entries;
  - the retired leaf values are deleted (`retire` op), not deprecated; they
    stay in reference/history/release-lexical-groups/ and in
    reference/retired-symbols.json (host-only: used to *reject* bare retired
    symbols, never to admit anything).

    python -m glossary.adopt_release            # install
    python -m glossary.adopt_release --check    # build and validate only
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
SWARM = REF.parent
PROPOSAL = REF / "proposed-lexical-groups"
HISTORY = REF / "history" / "release-lexical-groups"
RETIRED_MAP = REF / "retired-symbols.json"
RELEASE = f"release {render.LANGUAGE_VERSION}"

COUNTRY_CODES = {"japan": "JP", "argentina": "AR", "mexico": "MX", "germany": "DE", "poland": "PL",
                 "china": "CN", "united_states": "US"}

STANDARD_GROUPS = {
    "v19/lexical-group/country": {
        "definition": "A country identified by its ISO 3166-1 alpha-2 code (country::JP is Japan). The code names the "
                      "country only; no language, currency or region membership is implied.",
        "group": {"admission": "standard", "standard": "iso3166-1-alpha2", "key_form": "upper_code",
                  "examples": ["country::JP", "country::DE"]},
        "not": "A language (use a locale value) or a currency (use currency::<ISO 4217 code>).",
    },
    "v19/lexical-group/currency": {
        "definition": "A currency identified by its ISO 4217 code (currency::ZAR is the South African rand); no "
                      "exchange rate or implicit conversion.",
        "group": {"admission": "standard", "standard": "iso4217", "key_form": "upper_code",
                  "examples": ["currency::USD", "currency::EUR"]},
        "not": "A country (use country::<ISO 3166-1 alpha-2 code>) or an amount (use measure with a currency unit).",
    },
}

# ---------------------------------------------------------------------- spec

SPEC_EDITS = [
    ("**Status:** proposed revision; not adopted or implemented",
     "**Status:** adopted by the swarm loop (glossary release g15); no parser implementation yet"),
    (" Adoption and historical migration notes are in design-notes.md.",
     " Adoption and historical migration notes are in proposed-lexical-groups/design-notes.md."),
    ("a compatible glossary with exact signatures, definitions, lexical-group contracts and pinned member registries,",
     "a compatible glossary with exact signatures, definitions and lexical-group contracts, the bundled standard "
     "code lists,"),
    ("| admission | `open_label`; alternatively `registered` |",
     "| admission | `open_label`; alternatively `standard` or `registered` |\n"
     "| standard | for `standard` groups: the name of a bundled code list, `standards/<name>.json` "
     "(`iso3166-1-alpha2`, `iso4217`) |"),
    ("registered groups may instead use `lower_identifier`",
     "standard and registered groups may instead use `lower_identifier`"),
    ("Examples are not a whitelist. Open groups require lower_word and no members; registered groups require "
     "nonempty members.",
     "Examples are not a whitelist. Open groups require lower_word and no members; standard groups name their "
     "standard, use its key form and list no members; registered groups require nonempty members."),
    ("A registered value denotes its pinned member definition; unknown members fail.",
     "A standard value denotes the standard's entry for that code (`currency::ZAR` is the South African rand, "
     "`country::JP` is Japan); a code outside the bundled list fails (`currency::ZZZ`). A registered value denotes "
     "its pinned member definition; unknown members fail."),
    ("Registry contents must accompany the release;",
     "Registry contents and standard code lists must accompany the release;"),
]


def build_spec() -> str:
    text = (PROPOSAL / "language-spec.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    for old, new in SPEC_EDITS:
        if text.count(old) != 1:
            raise SystemExit(f"adopt_release: spec edit anchor found {text.count(old)}x: {old[:80]!r}")
        text = text.replace(old, new)
    return text


# ---------------------------------------------------------------------- glossary

COUNTRY_RE = re.compile(r"\bcountry::([a-z_]+)\b")


def build_glossary() -> tuple:
    """(records, retired ids, retired map) for the new release."""
    records = rec_mod.load(PROPOSAL / "glossary.jsonl")
    by_id = rec_mod.by_id(records)
    for gid, patch in STANDARD_GROUPS.items():
        rec = by_id[gid]
        rec.update(patch)
        rec["version"] = int(rec.get("version", 1)) + 1
    for rec in records:
        if rec["id"] in STANDARD_GROUPS:
            continue
        for field in ("definition", "not", "signature", "expansion", "code"):
            value = rec.get(field)
            if isinstance(value, str) and "country::" in value:
                rec[field] = COUNTRY_RE.sub(lambda m: f"country::{COUNTRY_CODES.get(m.group(1), m.group(1))}", value)
        if rec["id"] == "v19/rule/lexical-groups":
            rec["definition"] = ("Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups "
                                 "admit any key of their form (examples are not whitelists); standard groups admit "
                                 "the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for "
                                 "currency). Leaf values are never glossary entries. Consumer signatures alone decide "
                                 "where a group may appear. Retired bare symbols are invalid.")
    # every dependency is derived again: signatures now name ATOM[g] groups
    known = {r["symbol"]: r for r in records if r["status"] != "Deprecated"}
    for rec in records:
        if rec["status"] != "Deprecated":
            rec["dependencies"] = rec_mod.derive_dependencies(rec, known)
    mm = json.loads((PROPOSAL / "migration-map.json").read_text(encoding="utf-8"))
    retired_map = {}
    for e in mm["entries"]:
        repl = e["replacement"]
        m = COUNTRY_RE.fullmatch(repl or "")
        if m:
            repl = f"country::{COUNTRY_CODES[m.group(1)]}"
        retired_map[e["old_symbol"]] = {"old_id": e["old_id"], "replacement": repl}
    current = rec_mod.load()
    new_ids = {r["id"] for r in records}
    retired = {r["id"] for r in current if r["id"] not in new_ids}
    return records, retired, retired_map, current


def provenance(current: list, new: list, retired_map: dict) -> list:
    old = rec_mod.by_id(current)
    now = rec_mod.by_id(new)
    by_old_id = {v["old_id"]: (k, v["replacement"]) for k, v in retired_map.items()}
    events = []

    def ev(op, rid, outcome):
        events.append({"at": None, "batch": None, "migration": RELEASE, "op": op, "ids": [rid], "suggestions": [],
                       "translator_ids": [], "outcome": outcome})
    for rid in old:
        if rid not in now:
            sym, repl = by_old_id.get(rid, (old[rid]["symbol"], ""))
            ev("retire", rid, f"retired: leaf value now written as a value-group atom" + (f" ({repl})" if repl else ""))
    for rid, rec in now.items():
        if rid not in old:
            ev("add", rid, "added by the lexical-groups release")
        elif {k: v for k, v in rec.items() if k != "version"} != {k: v for k, v in old[rid].items() if k != "version"}:
            ev("update", rid, "updated by the lexical-groups release (group-aware signature/definition/dependencies)")
    return events


def migrated_examples() -> str:
    lines = []
    for line in (REF / "examples.jsonl").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        e = json.loads(line)
        if e.get("id") == "section-013-example-1":
            e["braincode"] = ("MODE REQUEST\nENTRYPOINT ObjectLabelPillow\nTASK ObjectLabelPillow {\n"
                              "  ACTION pick_up(target=object_label::pillow, quantity=2, source=object_label::sofa) "
                              "-> object_label_pillow_refs : LIST[REF[STRING]]\n"
                              "  FOR EACH item IN object_label_pillow_refs {\n"
                              "    ACTION place(target=item, destination=object_label::armchair, relation=on)\n"
                              "  }\n}\n")
            e["status"] = "migrated to value groups (lexical-groups release); source qualifications apply"
        lines.append(json.dumps(e, ensure_ascii=False))
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------- main

def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    check_only = "--check" in argv
    import spec_compact  # swarm/spec_compact.py (cwd or sys.path)
    spec = build_spec()
    compact_spec = spec_compact.build(spec)
    records, retired, retired_map, current = build_glossary()
    errors = rec_mod.validate(records, previous=current, retired=retired)
    unmapped = sorted(r for r in retired if r not in {v["old_id"] for v in retired_map.values()}
                      and not r.startswith("v19/rule/"))
    print(f"release: {len(records)} records ({len(retired)} retired, "
          f"{sum(groups_mod.is_group(r) for r in records)} value groups); spec {len(spec):,} chars, "
          f"compact {len(compact_spec):,} chars; {len(errors)} validation error(s)")
    for e in errors[:40]:
        print("  error:", e)
    if unmapped:
        print("  note: retired without a replacement mapping:", ", ".join(unmapped))
    if errors:
        sys.exit(1)
    if check_only:
        return
    if HISTORY.exists():
        sys.exit(f"{HISTORY} exists: the release is already installed")
    HISTORY.mkdir(parents=True)
    for name in ("language-spec.md", "language-spec.compact.md", "glossary.jsonl", "glossary.md",
                 "glossary-provenance.jsonl", "examples.jsonl", "reference-manifest.json"):
        if (REF / name).exists():
            shutil.copy2(REF / name, HISTORY / name)
    (REF / "language-spec.md").write_text(spec, encoding="utf-8", newline="\n")
    (REF / "language-spec.compact.md").write_text(compact_spec, encoding="utf-8", newline="\n")
    (REF / "examples.jsonl").write_text(migrated_examples(), encoding="utf-8", newline="\n")
    RETIRED_MAP.write_text(json.dumps({
        "purpose": "Bare symbols retired by the lexical-groups release, with their value-group form. Host-only: the "
                   "coverage check rejects a retired bare symbol; nothing here admits a value.",
        "retired": retired_map}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    rec_mod.save(records)
    rec_mod.append_provenance(provenance(current, records, retired_map))
    version = manifest.bump_version(note=RELEASE)
    render.render_all(records, version)
    manifest.refresh()
    print(f"installed {RELEASE} as glossary {version}; snapshot in {HISTORY.relative_to(SWARM)}; "
          f"rebuild the RAG index (the loop does it on start)")


if __name__ == "__main__":
    main()
