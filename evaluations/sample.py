#!/usr/bin/env python3
"""Freeze the evaluation sample: unseen test-split items, stratified like the
swarm's plan (swarm/loop.py: STRATIFY_KEYS, stratified_sample,
interleave_strata), items of at most --max-chars characters.

  per dataset: --per-dataset items (Gemini models translate all of them);
  the first --shared of each dataset (stratum-interleaved order) are flagged
  `all_models` and are translated by every model.

    python sample.py                 # -> sample.jsonl (refuses to overwrite)
    python sample.py --force
"""
import argparse
import json
import random
import sys
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent
SWARM = EVAL_DIR.parent / "swarm"
sys.path.insert(0, str(SWARM))

import loop  # noqa: E402
import loop_files as lf  # noqa: E402

SAMPLE_PATH = EVAL_DIR / "sample.jsonl"


def build(per_dataset: int, shared: int, max_chars: int, seed: int) -> list:
    rng = random.Random(seed)
    rows = []
    for ds in lf.DATASETS:
        path = lf.DATA_DIR / ds / "test.jsonl"
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        lines = [line for line in lines if len(lf.item_content({"record_line": line})) <= max_chars]
        if len(lines) < per_dataset:
            sys.exit(f"sample: {ds} has only {len(lines)} test items <= {max_chars} chars")
        key = loop.STRATIFY_KEYS.get(ds)
        chosen = loop.stratified_sample(lines, per_dataset, key, rng)
        ordered = loop.interleave_strata(chosen, key, rng)
        for n, line in enumerate(ordered, 1):
            rows.append({
                "item_key": f"{ds}-{n}",
                "dataset": ds,
                "all_models": n <= shared,
                "item_id": lf.item_id({"record_line": line}),
                "stratum": loop._stratum(line, key),
                "chars": len(lf.item_content({"record_line": line})),
                "record_line": line,
            })
    return rows


def load(path: Path = SAMPLE_PATH) -> list:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--per-dataset", type=int, default=8)
    p.add_argument("--shared", type=int, default=3)
    p.add_argument("--max-chars", type=int, default=6000)
    p.add_argument("--seed", type=int, default=2026)
    p.add_argument("--force", action="store_true")
    args = p.parse_args(argv)
    if SAMPLE_PATH.exists() and not args.force:
        sys.exit(f"{SAMPLE_PATH.name} exists (frozen); pass --force to replace it")
    rows = build(args.per_dataset, args.shared, args.max_chars, args.seed)
    SAMPLE_PATH.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    shared = sum(r["all_models"] for r in rows)
    print(f"sample: {len(rows)} items ({shared} shared by all models) -> {SAMPLE_PATH.name}")
    for ds in lf.DATASETS:
        sub = [r for r in rows if r["dataset"] == ds]
        print(f"  {ds:13} {len(sub)} items, strata {sorted({r['stratum'] for r in sub})[:6]}, "
              f"max {max(r['chars'] for r in sub):,} chars")


if __name__ == "__main__":
    main()
