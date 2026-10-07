"""One-time conversion of the legacy (migrated v19 draft) glossary.md into
glossary.jsonl records.

The legacy file spreads one symbol's meaning across several sections — its
gloss and aliases in the Section 10 inventory, its signature in Section 3
(operations) or Section 5 (composites), its contract in the Section 6
category table. This importer joins those into one record per symbol and
turns the prose sections into `rule` records the members link to.

    python -m glossary.import_legacy reference/glossary.md reference/glossary.jsonl
"""
import re
import sys
from pathlib import Path

from . import records as rec_mod
from . import schema

SOURCE = "glossary.md v19.0.0-draft.1 (legacy migrated layout)"
SYN_RE = re.compile(r"\s*\(natural-language synonyms:\s*(.*?)\)\s*$")


def _strip_ticks(text: str) -> str:
    text = text.strip()
    if len(text) >= 2 and text.startswith("`") and text.endswith("`"):
        return text[1:-1]
    return text


def _cells(line: str) -> list:
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [c.strip() for c in inner.split("|")]


def parse_sections(text: str) -> dict:
    """{(h2, h3): {"tables": [[header, rows]], "prose": [paragraph, ...], "code": [...]}}."""
    sections = {}
    h2 = h3 = ""
    lines = text.splitlines()
    i = 0
    para = []

    def bucket():
        return sections.setdefault((h2, h3), {"tables": [], "prose": [], "code": []})

    def flush():
        if para:
            bucket()["prose"].append(" ".join(l.strip() for l in para).strip())
            para.clear()

    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            flush()
            h2, h3 = line[3:].strip(), ""
        elif line.startswith("### "):
            flush()
            h3 = line[4:].strip()
        elif line.startswith("# "):
            flush()
        elif line.startswith("```"):
            flush()
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            bucket()["code"].append("\n".join(code))
        elif line.strip().startswith("|") and i + 1 < len(lines) and set(lines[i + 1].strip()) <= set("|-: "):
            flush()
            header = _cells(line)
            rows = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(_cells(lines[i]))
                i += 1
            bucket()["tables"].append([header, rows])
            continue
        elif not line.strip():
            flush()
        elif line.lstrip().startswith("- ") and para:
            flush()
            para.append(line)
        else:
            para.append(line)
        i += 1
    flush()
    return sections


def _find(sections, h2_prefix, h3=None):
    for (a, b), body in sections.items():
        if a.startswith(h2_prefix) and (h3 is None or b == h3):
            return body
    return {"tables": [], "prose": [], "code": []}


def _split_sig(text: str):
    """`name(args) -> R` or `name(args)` -> (name, '(args) -> R')."""
    text = _strip_ticks(text)
    m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*(\(.*)$", text)
    if not m:
        return text, ""
    return m.group(1), m.group(2).strip()


def _rule(rid, symbol, definition, core=False, category="", mentions_text=""):
    return {"id": rid, "symbol": symbol, "kind": "rule", "status": "Retained",
            "category": category, "definition": definition.strip(), "core": core,
            "provenance": {"source": SOURCE}, "_mentions_text": mentions_text or definition}


def convert(text: str) -> list:
    sections = parse_sections(text)
    out = {}          # id -> record
    by_symbol = {}    # symbol -> id

    def put(record):
        out[record["id"]] = record
        if record["kind"] not in ("rule", "category_rule", "example"):
            by_symbol[record["symbol"]] = record["id"]
        return record

    # ---- shared rules ---------------------------------------------------------
    def prose(h2, h3=None):
        return "\n\n".join(_find(sections, h2, h3)["prose"])

    def table_text(h2, h3=None):
        chunks = []
        for header, rows in _find(sections, h2, h3)["tables"]:
            chunks.append("| " + " | ".join(header) + " |\n|" + "---|" * len(header))
            chunks.extend("| " + " | ".join(r) + " |" for r in rows)
        return "\n".join(chunks)

    rules = [
        _rule("v19/rule/reading-guide", "rule_reading_guide",
              prose("1. How to read") + "\n\n" + table_text("1. How to read"), core=True),
        _rule("v19/rule/structural-constructs", "rule_structural_constructs",
              table_text("2. Structural") + "\n\n" + prose("2. Structural"), core=True),
        _rule("v19/rule/operations-general", "rule_operations_general",
              prose("3. Operation contracts", "") + "\n\n" + prose("3. Operation contracts", "External operations").split("`search_web` optional")[0]
              + "\n\n" + [p for p in _find(sections, "3. Operation contracts", "External operations")["prose"] if p.startswith("These explicit")][0]),
        _rule("v19/rule/search-web-attributes", "rule_search_web_attributes",
              "\n\n".join(p for p in _find(sections, "3. Operation contracts", "External operations")["prose"]
                          if p.startswith("`search_web`") or p.startswith("Search ranking"))),
        _rule("v19/rule/speech-acts-general", "rule_speech_acts_general",
              prose("3. Operation contracts", "Speech acts"), core=True),
        _rule("v19/rule/recording-signatures", "rule_recording_signatures",
              prose("3. Operation contracts", "Recording signatures"), core=True),
        _rule("v19/rule/support-primitives-general", "rule_support_primitives_general",
              prose("4. Semantic primitives", "")),
        _rule("v19/rule/trace-relations-general", "rule_trace_relations_general",
              prose("4. Semantic primitives", "Minimal trace relations and links"), core=True),
        _rule("v19/rule/composites-general", "rule_composites_general", prose("5. Composite")),
        _rule("v19/rule/attributes-and-generate", "rule_attributes_and_generate",
              prose("6. Category rules", "Attributes and Generate extensions")),
        _rule("v19/rule/supplemental-general", "rule_supplemental_general", prose("8. Minimal supplemental")),
        _rule("v19/rule/review-points", "rule_review_points", prose("9. Review points")),
        _rule("v19/rule/examples-general", "rule_examples_general", prose("7. Corrected examples", "")),
    ]
    for r in rules:
        put(r)

    for header, rows in _find(sections, "6. Category rules", "")["tables"]:
        for category, contract in rows:
            put({"id": f"v19/rule/category/{category}", "symbol": f"rule_category_{category.replace('-', '_')}",
                 "kind": "category_rule", "status": "Retained", "category": category,
                 "definition": contract, "provenance": {"source": SOURCE}, "_mentions_text": contract})

    # ---- inventory: one record per listed member -------------------------------
    inventory_status = {}
    for (h2, h3), body in sections.items():
        if not h3.startswith("Inventory: "):
            continue
        category = h3[len("Inventory: "):].strip()
        for header, rows in body["tables"]:
            for row in rows:
                symbol, gloss, status = _strip_ticks(row[0]), row[1], row[2]
                aliases = []
                m = SYN_RE.search(gloss)
                if m:
                    aliases = [a.strip() for a in m.group(1).split(",") if a.strip()]
                    gloss = gloss[:m.start()].strip()
                if category == "structural-word":
                    kind = "structural"
                elif category == "attribute-name":
                    kind = "attribute"
                elif status == "Composite":
                    kind = "composite"
                elif category == "operation-vocabulary":
                    kind = "operation"
                else:
                    kind = "value"
                rid = f"v19/composite/{symbol}" if kind == "composite" else f"v19/{category}/{symbol}"
                inventory_status[symbol] = status
                put({"id": rid, "symbol": symbol, "kind": kind, "status": status, "category": category,
                     "definition": gloss, "aliases": aliases,
                     "provenance": {"source": SOURCE, "source_definition": gloss, "source_category": category}})

    def member(symbol):
        rid = by_symbol.get(symbol)
        return out[rid] if rid else None

    # ---- operations (Section 3) -------------------------------------------------
    for header, rows in _find(sections, "3. Operation contracts", "External operations")["tables"]:
        for symbol, sig, meaning in rows:
            symbol = _strip_ticks(symbol)
            r = member(symbol)
            r["signature"] = _strip_ticks(sig)
            r["definition"] = meaning
            r["shared_rules"] = ["v19/rule/operations-general", "v19/rule/recording-signatures"]
            if symbol in ("search_web", "sort"):
                r["shared_rules"].append("v19/rule/search-web-attributes")

    for header, rows in _find(sections, "3. Operation contracts", "Speech acts")["tables"]:
        for symbol, arg, meaning in rows:
            r = member(_strip_ticks(symbol))
            r["kind"] = "speech_act"
            r["signature"] = "UTTER " + r["symbol"] + "(" + arg.replace("`", "") + ")"
            r["definition"] = meaning
            r["shared_rules"] = ["v19/rule/speech-acts-general"]

    # ---- primitives and relations (Section 4) --------------------------------
    for header, rows in _find(sections, "4. Semantic primitives", "")["tables"]:
        for sig, definition, contrast in rows:
            symbol, args = _split_sig(sig)
            put({"id": f"v19/support/{symbol}", "symbol": symbol, "kind": "constructor", "status": "Retained",
                 "signature": f"TERM {symbol}{args} -> TERM", "definition": definition,
                 "examples": {"positive": [], "contrast": [contrast]},
                 "shared_rules": ["v19/rule/support-primitives-general"],
                 "provenance": {"source": SOURCE}})

    for header, rows in _find(sections, "4. Semantic primitives", "Minimal trace relations and links")["tables"]:
        for symbol, sig, meaning in rows:
            kind_word, _, args = sig.partition(" ")
            kind = "claim_relation" if kind_word == "CLAIM" else "link"
            put({"id": f"v19/support/{symbol}", "symbol": symbol, "kind": kind, "status": "Retained",
                 "signature": f"{kind_word} {symbol}{_strip_ticks(args)}", "definition": meaning,
                 "shared_rules": ["v19/rule/trace-relations-general"], "core": True,
                 "provenance": {"source": SOURCE}})

    # ---- composites (Section 5) ------------------------------------------------
    for header, rows in _find(sections, "5. Composite")["tables"]:
        for sig, expansion in rows:
            symbol, args = _split_sig(sig)
            r = member(symbol)
            r["kind"] = "composite"
            r["signature"] = f"TERM {symbol}{args} -> TERM"
            r["expansion"] = _strip_ticks(expansion)
            r["shared_rules"] = ["v19/rule/composites-general"]

    # ---- supplemental (Section 8) ----------------------------------------------
    for header, rows in _find(sections, "8. Minimal supplemental")["tables"]:
        for symbol, kind_sig, definition in rows:
            if kind_sig.startswith("Action"):
                kind, category, sig = "operation", "operation-vocabulary", _strip_ticks(kind_sig[len("Action"):].strip())
                rules = ["v19/rule/operations-general", "v19/rule/recording-signatures", "v19/rule/supplemental-general"]
            else:
                category = kind_sig.split()[0]
                kind, sig = "value", ""
                rules = ["v19/rule/supplemental-general"]
            put({"id": f"v19/support/{symbol}", "symbol": symbol, "kind": kind, "status": "Retained",
                 "category": category, "signature": sig, "definition": definition, "shared_rules": rules,
                 "provenance": {"source": SOURCE}})

    # ---- category rules attach to every member --------------------------------
    category_rules = {r["category"]: r["id"] for r in out.values() if r["kind"] == "category_rule"}
    for r in out.values():
        if r["kind"] in ("rule", "category_rule", "example"):
            continue
        r.setdefault("shared_rules", [])
        rule = category_rules.get(r.get("category"))
        if rule and rule not in r["shared_rules"]:
            r["shared_rules"].append(rule)
        if r.get("category") in ("attribute-name", "artifact-value") or r["kind"] == "attribute":
            if "v19/rule/attributes-and-generate" not in r["shared_rules"]:
                r["shared_rules"].append("v19/rule/attributes-and-generate")
        if r["kind"] == "composite" and "v19/rule/composites-general" not in r["shared_rules"]:
            r["shared_rules"].append("v19/rule/composites-general")

    # ---- worked examples (Section 7) --------------------------------------------
    for (h2, h3), body in sections.items():
        if not h2.startswith("7. Corrected examples") or not h3:
            continue
        letter, _, title = h3.partition(". ")
        slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
        put({"id": f"v19/example/{letter.lower()}", "symbol": f"example_{letter.lower()}_{slug}",
             "kind": "example", "status": "Retained", "definition": title + "\n\n" + "\n\n".join(body["prose"]),
             "examples": {"positive": body["code"], "contrast": []},
             "shared_rules": ["v19/rule/examples-general"], "provenance": {"source": SOURCE}})

    # ---- derived links ---------------------------------------------------------
    records = [schema.normalize({k: v for k, v in r.items() if not k.startswith("_")}) for r in out.values()]
    known = {r["symbol"]: r for r in records}
    mentions_src = {r["id"]: r.get("_mentions_text", "") for r in out.values()}
    for r in records:
        if r["kind"] in schema.RULE_KINDS:
            text = mentions_src[r["id"]]
            names = re.findall(r"`([A-Za-z_][A-Za-z0-9_]*)`|\b([a-z]+_[a-z0-9_]+)\b", text)
            ment = []
            for a, b in names:
                sym = a or b
                if sym in known and known[sym]["kind"] not in schema.RULE_KINDS and known[sym]["id"] not in ment:
                    ment.append(known[sym]["id"])
            r["mentions"] = ment
        else:
            r["dependencies"] = rec_mod.derive_dependencies(r, known)
    return records


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) != 2:
        sys.exit("usage: python -m glossary.import_legacy <legacy glossary.md> <out glossary.jsonl>")
    src, dst = Path(argv[0]), Path(argv[1])
    records = convert(src.read_text(encoding="utf-8"))
    errors = rec_mod.validate(records)
    for e in errors:
        print("error:", e)
    rec_mod.save(records, dst)
    kinds = {}
    for r in records:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    print(f"wrote {len(records)} records to {dst}: {kinds}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
