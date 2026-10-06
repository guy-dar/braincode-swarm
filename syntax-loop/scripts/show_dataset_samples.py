#!/usr/bin/env python3
"""Print N sample items from every dataset (closed + open class) for manual QA/eyeballing.

    python scripts/show_dataset_samples.py --n 3

Reads datasets/samples/<name>.jsonl, falling back to <name>.seed.jsonl — same resolution order as
braincode_loop/simulation.py::resolve_dataset_path, duplicated here (not imported) because
datasets/ is an importable namespace package that can shadow the `datasets` HF library when this
script runs with cwd=syntax-loop; see fetch_dataset_samples.py's module docstring.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys

# Windows consoles often default to a legacy codepage (e.g. cp1252) that can't encode characters
# real dataset text sometimes contains (em dashes, zero-width spaces, etc.) — force UTF-8 output
# with lossy fallback instead of crashing partway through printing.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLES_DIR = os.path.join(BASE_DIR, "datasets", "samples")
CLOSED = ["seed_tasks", "mind2web", "alfred", "swebench"]
OPEN = ["prism", "paths", "thoughttrace"]


def _resolve(name: str) -> str | None:
    for candidate in (f"{name}.jsonl", f"{name}.seed.jsonl"):
        path = os.path.join(SAMPLES_DIR, candidate)
        if os.path.exists(path):
            return path
    return None


def _load(name: str, n: int, seed: int) -> list[dict]:
    if name == "seed_tasks":
        path = os.path.join(BASE_DIR, "braincode_loop", "seed_tasks.json")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        rows = [
            {"id": item["id"], "nl": item["nl"], "domain": domain, "source": "seed_tasks", "steps": []}
            for key in ("dev_domains", "heldout_domains")
            for domain, items in data.get(key, {}).items()
            for item in items
        ]
    else:
        path = _resolve(name)
        if not path:
            print(f"## {name}: NOT FOUND (no .jsonl or .seed.jsonl in {SAMPLES_DIR})\n")
            return []
        with open(path, "r", encoding="utf-8") as f:
            rows = [json.loads(line) for line in f if line.strip()]
    random.Random(seed).shuffle(rows)
    return rows[:n]


def _print_item(name: str, item: dict) -> None:
    print(f"### {name} — {item.get('id')}")
    print(f"source: {item.get('source', '')}")
    print(f"nl: {item.get('nl', '')}")
    for step in (item.get("steps") or [])[:12]:
        print(f"  - {step}")
    print()


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--n", type=int, default=3, help="items to show per dataset (default 3)")
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    print("## Closed class\n")
    for name in CLOSED:
        for item in _load(name, args.n, args.seed):
            _print_item(name, item)

    print("## Open class\n")
    for name in OPEN:
        for item in _load(name, args.n, args.seed):
            _print_item(name, item)


if __name__ == "__main__":
    main()
