#!/usr/bin/env python3
"""Inspector: count one batch's suggestions and decide whether to stop early.

Works in translator_suggestions/. For batch N it reads every
`N-<tnum>.md` there, counts suggestion headings by type (add / refine) in
total and per dataset, upserts one row into
translator_suggestions/suggestion_counts.csv, prints the counts and the
decision, and exits 3 to stop the loop (0 to continue).

Stop rule: add <= 2 AND refine <= 5 — the glossary has stopped needing much —
but only when at least --min-finished (default 0.8) of the batch's
translators produced valid output. A batch that mostly crashed (proxy outage,
timeouts) has few suggestions for the wrong reason and must not end the run.

    python inspector.py --batch 7
"""
import argparse
import csv
import sys

import loop_files as lf

STOP_EXIT_CODE = 3
DEFAULT_MAX_ADD = 2
DEFAULT_MAX_REFINE = 5
DEFAULT_MIN_FINISHED = 0.8


def columns() -> list:
    cols = ["batch", "translators_planned", "translators_finished", "successful_translations",
            "failed_translations", "add_total", "refine_total"]
    cols += [f"add_{ds}" for ds in lf.DATASETS] + [f"refine_{ds}" for ds in lf.DATASETS]
    return cols + ["decision", "reason", "inspected_at"]


def count_batch(batch_id: int, plan_rows: list = None) -> dict:
    plan_rows = plan_rows if plan_rows is not None else lf.plan_batches(lf.load_plan()).get(batch_id, [])
    row = {c: 0 for c in columns()}
    row["batch"] = batch_id
    row["translators_planned"] = len(plan_rows)
    for item in plan_rows:
        tid, ds = item["translator_id"], item["dataset"]
        if lf.success_path(ds, tid).exists():
            row["successful_translations"] += 1
        elif lf.failed_path(ds, tid).exists():
            row["failed_translations"] += 1
    row["translators_finished"] = row["successful_translations"] + row["failed_translations"]

    for path in lf.batch_suggestion_files(batch_id):
        text = path.read_text(encoding="utf-8", errors="replace")
        dataset = lf.header_field(text, "Dataset")
        for s in lf.parse_suggestions(text):
            row[f"{s['type']}_total"] += 1
            if f"{s['type']}_{dataset}" in row:
                row[f"{s['type']}_{dataset}"] += 1
    return row


def decide(row: dict, max_add: int = DEFAULT_MAX_ADD, max_refine: int = DEFAULT_MAX_REFINE,
           min_finished: float = DEFAULT_MIN_FINISHED) -> tuple:
    planned = row["translators_planned"]
    finished_share = row["translators_finished"] / planned if planned else 0.0
    quiet = row["add_total"] <= max_add and row["refine_total"] <= max_refine
    if not quiet:
        return "continue", (f"{row['add_total']} add (limit {max_add}) / {row['refine_total']} refine "
                            f"(limit {max_refine}) — the glossary still needs changes")
    if finished_share < min_finished:
        return "continue", (f"suggestions are under the limits, but only {row['translators_finished']}/{planned} "
                            f"translators finished ({finished_share:.0%} < {min_finished:.0%}); not trusting the low count")
    return "stop", (f"{row['add_total']} add <= {max_add} and {row['refine_total']} refine <= {max_refine}, "
                    f"with {row['translators_finished']}/{planned} translators finished — early stopping")


def upsert_csv(row: dict) -> None:
    lf.SUGGESTIONS_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    if lf.COUNTS_CSV.exists():
        with lf.COUNTS_CSV.open(newline="", encoding="utf-8") as fh:
            rows = [r for r in csv.DictReader(fh) if str(r.get("batch")) != str(row["batch"])]
    rows.append({k: row.get(k, "") for k in columns()})
    rows.sort(key=lambda r: int(r["batch"]))
    with lf.COUNTS_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns(), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def inspect(batch_id: int, plan_rows: list = None, max_add: int = DEFAULT_MAX_ADD,
            max_refine: int = DEFAULT_MAX_REFINE, min_finished: float = DEFAULT_MIN_FINISHED, log=print) -> dict:
    row = count_batch(batch_id, plan_rows)
    row["decision"], row["reason"] = decide(row, max_add, max_refine, min_finished)
    row["inspected_at"] = lf.now_iso()
    upsert_csv(row)
    per_ds = ", ".join(f"{ds} {row[f'add_{ds}']}/{row[f'refine_{ds}']}" for ds in lf.DATASETS)
    log(f"inspector: batch {batch_id}: translators {row['translators_finished']}/{row['translators_planned']} finished "
        f"({row['successful_translations']} successful, {row['failed_translations']} failed)")
    log(f"inspector: batch {batch_id}: suggestions add {row['add_total']}, refine {row['refine_total']} "
        f"(add/refine per dataset: {per_ds})")
    log(f"inspector: batch {batch_id}: decision {row['decision'].upper()} — {row['reason']}")
    return row


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("--max-add", type=int, default=DEFAULT_MAX_ADD)
    p.add_argument("--max-refine", type=int, default=DEFAULT_MAX_REFINE)
    p.add_argument("--min-finished", type=float, default=DEFAULT_MIN_FINISHED)
    args = p.parse_args(argv)
    row = inspect(args.batch, max_add=args.max_add, max_refine=args.max_refine, min_finished=args.min_finished)
    sys.exit(STOP_EXIT_CODE if row["decision"] == "stop" else 0)


if __name__ == "__main__":
    main()
