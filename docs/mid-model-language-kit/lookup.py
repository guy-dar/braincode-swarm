"""Read-only local retrieval. No external dependencies, network or model calls.

CLI: python lookup.py lookup "pick_up"
JSON-lines host bridge: python lookup.py serve
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent


def terms(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


class Kit:
    def __init__(self, root=ROOT):
        self.root = Path(root)
        self.data = json.loads((self.root / "glossary.json").read_text(encoding="utf-8"))
        self.parts = {s["id"]: s for s in self.data["sections"]}
        reconstructed = "".join(s["raw_markdown"] for s in self.data["sections"]).encode("utf-8")
        if hashlib.sha256(reconstructed).hexdigest() != self.data["source_sha256"]:
            raise ValueError("Glossary integrity check failed; rebuild from the frozen source.")
        self.entries = {e["symbol"]: e for e in self.data["entries"]}
        self.parents = {}
        stack = []
        for s in self.data["sections"]:
            while stack and stack[-1]["level"] >= s["level"]:
                stack.pop()
            self.parents[s["id"]] = [p["id"] for p in stack]
            stack.append(s)

    def lookup_symbols(self, query, limit=3, section_filter=None, max_chars=18000):
        if not isinstance(query, str) or not query.strip() or len(query) > 500:
            raise ValueError("query must be a nonempty string of at most 500 characters")
        if type(limit) is not int or not 1 <= limit <= 8:
            raise ValueError("limit must be an integer from 1 to 8")
        if type(max_chars) is not int or not 2000 <= max_chars <= 40000:
            raise ValueError("max_chars must be an integer from 2000 to 40000")
        if section_filter is not None and not isinstance(section_filter, str):
            raise ValueError("section_filter must be text or null")
        q = query.strip().lower()
        qt = terms(q)
        scored = []
        for e in self.entries.values():
            if section_filter and not any(section_filter.lower() in o["section_title"].lower() for o in e["occurrences"]):
                continue
            aliases = [a.lower() for a in e["source_alias_hints"]]
            name = e["symbol"].lower()
            exact = q == name
            alias = q in aliases
            body = " ".join(" ".join(o["cells"]) for o in e["occurrences"])
            overlap = qt & terms(name + " " + " ".join(aliases) + " " + body)
            if not exact and not alias and not overlap:
                continue
            # Deterministic lexical ranking; score is not confidence or endorsement.
            score = 10000 if exact else 5000 if alias else 100 * len(qt & terms(name)) + 30 * len(qt & terms(" ".join(aliases))) + 5 * len(overlap)
            scored.append((score, e["symbol"], e))
        scored.sort(key=lambda x: (-x[0], x[1]))
        # Exact identity should not drag in weakly related rows merely to fill limit.
        if scored and scored[0][0] == 10000:
            scored = scored[:1]
        chosen = [x[2] for x in scored[:limit]]
        related = {}
        pending = list(chosen)
        visited = {e["symbol"] for e in chosen}
        while pending:
            e = pending.pop()
            for o in e["occurrences"]:
                candidates = []
                if o["section_title"].startswith("Inventory: "):
                    candidates.append(o["section_title"][len("Inventory: "):])
                if "Structured expansion" in o["headers"]:
                    expr = o["cells"][o["headers"].index("Structured expansion")]
                    expr = re.sub(r'"(?:[^"\\]|\\.)*"', "", expr)
                    candidates += re.findall(r"\b[a-z][a-z0-9_]*\b", expr)
                for name in candidates:
                    if name in self.entries and name not in visited:
                        visited.add(name)
                        related[name] = self.entries[name]
                        pending.append(self.entries[name])
        selected_parts = set()
        for e in chosen + list(related.values()):
            for o in e["occurrences"]:
                selected_parts.add(o["section_id"])
                selected_parts.update(self.parents[o["section_id"]])
        context = []
        for sid in sorted(selected_parts):
            s = self.parts[sid]
            # Preserve original prose exactly; table rows are already in entries.
            excerpt = "".join(line for line in s["raw_markdown"].splitlines(keepends=True) if not line.startswith("|"))
            context.append({"section_id": sid, "title": s["title"], "prose_excerpt": excerpt})
        result = {"query": query, "source_sha256": self.data["source_sha256"],
                  "matches": chosen, "referenced_entries": list(related.values()),
                  "context": context, "more_matches": max(0, len(scored) - len(chosen)),
                  "retrieval_complete": True,
                  "notice": "Original statuses and caveats are included without filtering. A match is not approval. Referenced entries are lexical links, not a formal dependency proof."}
        if len(json.dumps(result, ensure_ascii=False)) > max_chars:
            return {"query": query, "retrieval_complete": False,
                    "reason": "Full entry/context bundle exceeds response budget. Nothing was silently truncated.",
                    "matches": [{"symbol": e["symbol"], "section_ids": list(dict.fromkeys(o["section_id"] for o in e["occurrences"]))} for e in chosen],
                    "next_action": "Use read_document for the listed glossary sections, or retry with fewer matches/larger max_chars."}
        return result

    def read_document(self, document, section=None, start_line=1, max_lines=80):
        if document not in ("spec", "glossary"):
            raise ValueError("document must be spec or glossary")
        if type(start_line) is not int or start_line < 1 or type(max_lines) is not int or not 1 <= max_lines <= 150:
            raise ValueError("start_line >= 1 and 1 <= max_lines <= 150 are required")
        if section is not None and not isinstance(section, str):
            raise ValueError("section must be text or null")
        if document == "glossary":
            parts = self.data["sections"]
        else:
            from build_kit import sections
            parts = sections((self.root / "language-spec.md").read_bytes().decode("utf-8"))
        if section == "index":
            return {"document": document, "sections": [{k: s[k] for k in ("id", "title", "start_line")} for s in parts]}
        if section:
            found = [s for s in parts if s["id"] == section or s["title"] == section]
            if not found:
                found = [s for s in parts if section.lower() in s["title"].lower()]
            if len(found) != 1:
                return {"document": document, "error": "Section missing or ambiguous; use an exact ID from the index.",
                        "candidates": [{"id": s["id"], "title": s["title"]} for s in found]}
            text = found[0]["raw_markdown"]
            base_line = found[0]["start_line"]
            section = found[0]["id"]
        else:
            text = "".join(s["raw_markdown"] for s in parts)
            base_line = 1
        lines = text.splitlines(keepends=True)
        selected = []
        for line in lines[start_line-1:start_line-1+max_lines]:
            if selected and sum(map(len, selected)) + len(line) > 20000:
                break
            selected.append(line)
        end = start_line - 1 + len(selected)
        return {"document": document, "section": section, "line_numbering": "relative to selected section/document",
                "start_line": start_line, "source_start_line": base_line+start_line-1,
                "text": "".join(selected), "has_more": end < len(lines),
                "next_start_line": end+1 if end < len(lines) else None}

    def get_examples(self, query="", limit=2):
        if not isinstance(query, str) or len(query) > 500 or type(limit) is not int or not 1 <= limit <= 5:
            raise ValueError("query must be <= 500 characters; limit must be 1..5")
        examples = [json.loads(line) for line in (self.root / "examples.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
        if query:
            examples = [(len(terms(query) & terms(e["context_markdown"] + e["braincode"])), e) for e in examples]
            examples = [e for score, e in sorted(examples, key=lambda x: (-x[0],x[1]["id"])) if score]
        return {"examples": examples[:limit], "notice": "Copied examples retain all source qualifications; they are not parser-certified."}

    def dispatch(self, request):
        if not isinstance(request, dict) or set(request) - {"name", "arguments"}:
            raise ValueError("Expected {name, arguments}")
        functions = {"lookup_symbols": self.lookup_symbols, "read_document": self.read_document, "get_examples": self.get_examples}
        if request.get("name") not in functions:
            raise ValueError("Unknown tool name")
        arguments = request.get("arguments", {})
        if not isinstance(arguments, dict):
            raise ValueError("arguments must be an object")
        return functions[request["name"]](**arguments)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("lookup")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=3)
    p.add_argument("--format", choices=("json", "text"), default="text")
    p = sub.add_parser("read")
    p.add_argument("document", choices=("spec", "glossary"))
    p.add_argument("--section")
    p.add_argument("--start-line", type=int, default=1)
    p.add_argument("--max-lines", type=int, default=80)
    sub.add_parser("serve")
    sub.add_parser("examples").add_argument("query", nargs="?", default="")
    args = parser.parse_args()
    kit = Kit()
    if args.command == "serve":
        for line in sys.stdin:
            if not line.strip():
                continue
            try:
                if len(line) > 100000:
                    raise ValueError("Request too large")
                answer = {"ok": True, "result": kit.dispatch(json.loads(line))}
            except (ValueError, TypeError, KeyError) as exc:
                answer = {"ok": False, "error": str(exc)}
            print(json.dumps(answer, ensure_ascii=False), flush=True)
        return
    try:
        if args.command == "lookup":
            result = kit.lookup_symbols(args.query, limit=args.limit)
            if args.format == "text" and result["retrieval_complete"]:
                print("SOURCE ROWS (unchanged; read their restrictions and migration status)")
                for entry in result["matches"] + result["referenced_entries"]:
                    print("\n" + entry["symbol"])
                    for o in entry["occurrences"]:
                        print(f"[{o['section_id']}, line {o['source_line']}] " + " | ".join(o["headers"]))
                        print(o["raw_row"])
                for c in result["context"]:
                    print("\n" + c["prose_excerpt"])
                return
        elif args.command == "read":
            result = kit.read_document(args.document, args.section, args.start_line, args.max_lines)
        else:
            result = kit.get_examples(args.query)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, TypeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
