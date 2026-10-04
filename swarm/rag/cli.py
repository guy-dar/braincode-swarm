"""Command line for the glossary RAG (host side). Run from swarm/.

    python -m rag.cli build                        # (re)build the index from reference/glossary.jsonl
    python -m rag.cli serve [--port 8765]          # HTTP server (see rag/server.py)
    python -m rag.cli retrieve --file item.txt     # steps 1-4 on an item, printed as the translator sees it
    python -m rag.cli retrieve --record data/alfred/train.jsonl:3   # the 3rd record of a JSONL file
    python -m rag.cli search "cheapest first" [--kind constraint]
    python -m rag.cli widen "walk at most 20 minutes between stops"
    python -m rag.cli entry pick_up
    python -m rag.cli check --translation t.md --needs needs.json

Add --no-dense to skip the embedding model, --no-llm to use heuristic needs.
"""
import argparse
import json
import os
import sys
from pathlib import Path

SWARM_DIR = Path(__file__).resolve().parent.parent
if str(SWARM_DIR) not in sys.path:
    sys.path.insert(0, str(SWARM_DIR))

from rag import index as index_mod  # noqa: E402
from rag.retrieve import Retriever, render_candidates, render_check, render_context  # noqa: E402


def _item_text(args) -> str:
    if args.text:
        return args.text
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    if args.record:
        path, _, n = args.record.rpartition(":")
        with open(path, encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                if i == int(n):
                    return json.loads(line)["content"]
        sys.exit(f"no record {n} in {path}")
    return sys.stdin.read()


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", choices=["build", "serve", "retrieve", "search", "widen", "entry", "check"])
    p.add_argument("query", nargs="?", default="")
    p.add_argument("--file")
    p.add_argument("--record")
    p.add_argument("--text")
    p.add_argument("--kind", default="")
    p.add_argument("--context", default="")
    p.add_argument("--translation")
    p.add_argument("--needs")
    p.add_argument("--json", action="store_true")
    p.add_argument("--no-dense", action="store_true")
    p.add_argument("--no-llm", action="store_true")
    p.add_argument("--host", default=os.environ.get("RAG_HOST", "0.0.0.0"))
    p.add_argument("--port", type=int, default=int(os.environ.get("RAG_PORT", "8765")))
    args = p.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    dense = not args.no_dense
    if args.command == "build":
        idx = index_mod.build(dense=dense)
        print(f"indexed {len(idx.records)} of {len(idx.all_records)} records (dense={dense}) -> {index_mod.INDEX_DIR}")
        return

    retriever = Retriever(dense=dense, use_llm=not args.no_llm)
    if args.command == "serve":
        from rag.server import RagServer
        print(f"RAG server on http://{args.host}:{args.port} ({len(retriever.index.records)} records)", file=sys.stderr)
        RagServer(retriever, args.host, args.port).serve_forever()
    elif args.command == "retrieve":
        result = retriever.retrieve(_item_text(args))
        if args.json:
            print(json.dumps(result, indent=1, ensure_ascii=False))
        else:
            from glossary import manifest
            print(render_context(result, retriever, manifest.current_version()))
    elif args.command in ("search", "widen"):
        text = args.query or args.text or ""
        result = ({"text": text, "candidates": retriever.search_need(text, args.context, args.kind)}
                  if args.command == "search" else retriever.widen(text, args.context, args.kind))
        print(json.dumps(result, indent=1, ensure_ascii=False) if args.json else render_candidates(result))
    elif args.command == "entry":
        found = retriever.entry(args.query)
        if not found:
            sys.exit(f"no glossary record {args.query!r}")
        print(json.dumps(found, indent=1, ensure_ascii=False))
    elif args.command == "check":
        needs = json.loads(Path(args.needs).read_text(encoding="utf-8"))
        needs = needs.get("needs", needs) if isinstance(needs, dict) else needs
        report = retriever.check(Path(args.translation).read_text(encoding="utf-8"), needs)
        print(json.dumps(report, indent=1, ensure_ascii=False) if args.json else render_check(report))


if __name__ == "__main__":
    main()
