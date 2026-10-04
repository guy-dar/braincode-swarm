#!/usr/bin/env python3
"""Inspector: count one batch's suggestions, what the migrator accepted, and
decide whether to stop early.

For batch N it reads every `N-<tnum>.md` in translator_suggestions/ and counts
suggestion headings by type (add / refine), in total and per dataset. It then
reads reference/glossary-provenance.jsonl, where every applied migration op
lists the translator suggestions it came from (`<tid>#S<k>`), and counts the
suggestions the migrator accepted — carried into an applied add / update /
merge / split / deprecate — by their original type and dataset. A suggestion
folded into several ops counts once. Run figures (rounds, model calls, wall
time, cost, migration status) come from runs/loop_state.json.

It upserts one row into translator_suggestions/suggestion_counts.csv, redraws
graphs/ (plot_inspector.py), prints the counts and the decision, and exits 3
to stop the loop (0 to continue).

Stop rule: accepted add <= 2 AND accepted refine <= 5 — the migrator has
stopped finding much worth changing — but only when at least --min-finished
(default 0.8) of the batch's translators produced valid output and the
batch's migration was installed (or skipped for lack of suggestions). A batch
that mostly crashed, or whose migration failed validation, has few accepted
suggestions for the wrong reason and must not end the run.

    python inspector.py --batch 7
    python inspector.py --batches 1-7      # recompute rows (e.g. after adding columns)
"""
import argparse
import csv
import json
import subprocess
import sys

import loop_files as lf

STOP_EXIT_CODE = 3
DEFAULT_MAX_ADD = 2
DEFAULT_MAX_REFINE = 5
DEFAULT_MIN_FINISHED = 0.8
APPLIED_OPS = ("add", "update", "merge", "split", "deprecate")
# batch 1 ran before the op names settled
OP_ALIASES = {"created": "add", "changed": "update"}


def columns() -> list:
    ds = lf.DATASETS
    cols = ["batch", "translators_planned", "translators_finished", "successful_translations",
            "failed_translations", "unfinished_translations", "success_pct",
            "add_total", "refine_total"]
    cols += [f"add_{d}" for d in ds] + [f"refine_{d}" for d in ds]
    cols += ["add_lexical_group", "label_preserved_needs", "leaf_value_adds", "leaf_value_symbols"]
    cols += ["accepted_add_total", "accepted_refine_total", "accepted_pct"]
    cols += [f"accepted_add_{d}" for d in ds] + [f"accepted_refine_{d}" for d in ds]
    cols += [f"ops_{op}" for op in APPLIED_OPS]
    cols += ["migration_status", "glossary_version", "glossary_live_records_after",
             "translator_rounds", "translator_model_calls", "migration_model_calls",
             "wall_minutes", "cost_usd", "cost_translators_usd", "cost_migration_usd"]
    return cols + ["decision", "reason", "inspected_at"]


# ---------------------------------------------------------------------- sources

def load_provenance() -> list:
    if not lf.PROVENANCE_PATH.exists():
        return []
    return [json.loads(line) for line in lf.PROVENANCE_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_state_entry(batch_id: int) -> dict:
    if not lf.STATE_PATH.exists():
        return {}
    return (json.loads(lf.STATE_PATH.read_text(encoding="utf-8")).get("batches") or {}).get(str(batch_id), {})


def glossary_sizes(events: list) -> tuple:
    """(initial live records, {batch: live records after its migration}),
    reconstructed from the provenance log. Human edits made between batches
    count toward the next batch's figure."""
    initial, after = glossary_live_sets(events)
    return len(initial), {b: len(ids) for b, ids in after.items()}


def glossary_live_sets(events: list) -> tuple:
    """(initial live record ids, {batch: live ids after its migration}); see
    glossary_sizes."""

    def is_initial(e):
        return (e.get("batch") is None and e.get("op") == "created"
                and str(e.get("migration", "")).startswith("glossary.md"))

    # The initial import's events are interleaved with later "changed" events
    # in the log, so take all of them first.
    live = {i for e in events if is_initial(e) for i in e.get("ids") or []}
    initial = set(live)
    after, current_batch = {}, None
    for e in events:
        if is_initial(e):
            continue
        op, ids, batch = e.get("op"), e.get("ids") or [], e.get("batch")
        if batch is None:
            # a human edit between batches closes the batch before it
            if current_batch is not None and current_batch not in after:
                after[current_batch] = set(live)
        elif batch != current_batch:
            if current_batch is not None and current_batch not in after:
                after[current_batch] = set(live)
            current_batch = batch
        if op in ("created", "add"):
            live.update(ids)
        elif op == "split" and ids:
            live.discard(ids[0])
            live.update(ids[1:])
        elif op == "merge" and len(ids) > 1:
            live.difference_update(ids[1:])
        elif op in ("deprecate", "retire") and ids:
            live.discard(ids[0])
    if current_batch is not None and current_batch not in after:
        after[current_batch] = set(live)
    return initial, after


# ---------------------------------------------------------------------- counting

_KINDS = {}


def _record_kind(rid: str) -> tuple:
    """(kind, category, symbol) of a record id, from the current glossary or
    any history snapshot (retired records exist only there)."""
    if not _KINDS:
        for path in sorted(lf.HISTORY_DIR.glob("*/glossary.jsonl")) + [lf.REFERENCE_DIR / "glossary.jsonl"]:
            for line in path.read_text(encoding="utf-8").splitlines():
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                _KINDS[r.get("id")] = (r.get("kind"), r.get("category", ""), r.get("symbol"))
    return _KINDS.get(rid, (None, "", rid))


def count_batch(batch_id: int, plan_rows: list = None, events: list = None, entry: dict = None) -> dict:
    plan_rows = plan_rows if plan_rows is not None else lf.plan_batches(lf.load_plan()).get(batch_id, [])
    events = load_provenance() if events is None else events
    entry = load_state_entry(batch_id) if entry is None else entry
    row = {c: 0 for c in columns()}
    row["leaf_value_symbols"] = ""
    row["batch"] = batch_id
    row["translators_planned"] = len(plan_rows)
    for item in plan_rows:
        tid, ds = item["translator_id"], item["dataset"]
        path = None
        if lf.success_path(ds, tid).exists():
            row["successful_translations"] += 1
            path = lf.success_path(ds, tid)
        elif lf.failed_path(ds, tid).exists():
            row["failed_translations"] += 1
            path = lf.failed_path(ds, tid)
        if path is not None:
            # the host's check, appended to every routed translation: needs
            # covered only by an open-group label (spec §3.1)
            text = path.read_text(encoding="utf-8", errors="replace")
            row["label_preserved_needs"] += sum(1 for line in text.splitlines() if line.startswith("- [LABEL]"))
    row["translators_finished"] = row["successful_translations"] + row["failed_translations"]
    row["unfinished_translations"] = row["translators_planned"] - row["translators_finished"]
    row["success_pct"] = round(100 * row["successful_translations"] / row["translators_planned"], 1) \
        if row["translators_planned"] else 0.0

    # suggestions written: {"<tid>#S<k>": (type, dataset)}
    suggested = {}
    for path in lf.batch_suggestion_files(batch_id):
        text = path.read_text(encoding="utf-8", errors="replace")
        dataset = lf.header_field(text, "Dataset")
        for s in lf.parse_suggestions(text):
            suggested[f"{path.stem}#S{s['n']}"] = (s["type"], dataset)
            if s["dimension"] == "lexical-group":
                row["add_lexical_group"] += 1
            row[f"{s['type']}_total"] += 1
            if f"{s['type']}_{dataset}" in row:
                row[f"{s['type']}_{dataset}"] += 1

    # suggestions accepted: carried into an applied op of this batch's migration
    accepted = set()
    for e in events:
        if e.get("batch") != batch_id:
            continue
        op = OP_ALIASES.get(e.get("op"), e.get("op"))
        if op not in APPLIED_OPS:
            continue
        row[f"ops_{op}"] += 1
        accepted.update(r for r in e.get("suggestions") or [] if r in suggested)
        if op == "add":
            # leaf values added as records (kind value): the glossary should
            # grow groups, not enumerations of open domains (spec §3.1)
            for rid in e.get("ids") or []:
                kind, cat, sym = _record_kind(rid)
                if kind == "value":
                    row["leaf_value_adds"] += 1
                    row["leaf_value_symbols"] = ", ".join(filter(None, [row["leaf_value_symbols"] or "",
                                                                        f"{sym} ({cat})"]))
    for ref in accepted:
        kind, dataset = suggested[ref]
        row[f"accepted_{kind}_total"] += 1
        if f"accepted_{kind}_{dataset}" in row:
            row[f"accepted_{kind}_{dataset}"] += 1
    total = row["add_total"] + row["refine_total"]
    row["accepted_pct"] = round(100 * len(accepted) / total, 1) if total else 0.0

    _, after = glossary_sizes(events)
    row["glossary_live_records_after"] = after.get(batch_id, "")
    row["migration_status"] = entry.get("migration", "")
    row["glossary_version"] = entry.get("glossary_version", "")
    row["translator_rounds"] = entry.get("translator_rounds", "")
    row["translator_model_calls"] = (entry.get("translator_usage") or {}).get("calls", "")
    row["migration_model_calls"] = (entry.get("migration_usage") or {}).get("calls", "")
    cost = entry.get("cost_usd") or {}
    row["wall_minutes"] = entry.get("wall_minutes", "")
    row["cost_usd"] = cost.get("total", "")
    row["cost_translators_usd"] = cost.get("translators", "")
    row["cost_migration_usd"] = cost.get("migration", "")
    return row


def decide(row: dict, max_add: int = DEFAULT_MAX_ADD, max_refine: int = DEFAULT_MAX_REFINE,
           min_finished: float = DEFAULT_MIN_FINISHED) -> tuple:
    planned = row["translators_planned"]
    finished_share = row["translators_finished"] / planned if planned else 0.0
    add, refine = row["accepted_add_total"], row["accepted_refine_total"]
    quiet = add <= max_add and refine <= max_refine
    if not quiet:
        return "continue", (f"{add} accepted add (limit {max_add}) / {refine} accepted refine (limit {max_refine}) "
                            f"— the glossary still needs changes")
    if finished_share < min_finished:
        return "continue", (f"accepted suggestions are under the limits, but only {row['translators_finished']}/"
                            f"{planned} translators finished ({finished_share:.0%} < {min_finished:.0%}); "
                            f"not trusting the low count")
    status = str(row.get("migration_status") or "")
    if status not in ("installed", "skipped"):
        return "continue", (f"accepted suggestions are under the limits, but the migration was not installed "
                            f"({status or 'no status'}); not trusting the low count")
    return "stop", (f"{add} accepted add <= {max_add} and {refine} accepted refine <= {max_refine} "
                    f"({row['add_total']} add / {row['refine_total']} refine suggested), with "
                    f"{row['translators_finished']}/{planned} translators finished — early stopping")


def upsert_csv(row: dict) -> None:
    lf.SUGGESTIONS_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    if lf.COUNTS_CSV.exists():
        with lf.COUNTS_CSV.open(newline="", encoding="utf-8") as fh:
            rows = [r for r in csv.DictReader(fh) if str(r.get("batch")) != str(row["batch"])]
    rows.append({k: row.get(k, "") for k in columns()})
    rows.sort(key=lambda r: int(r["batch"]))
    with lf.COUNTS_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns(), extrasaction="ignore", restval="")
        writer.writeheader()
        writer.writerows(rows)


def refresh_graphs(log=print) -> bool:
    """Redraw graphs/ from the CSV (plot_inspector.py, in its own process so
    matplotlib stays out of the loop). A failed redraw is reported, never
    raised: it must not stop the loop."""
    try:
        result = subprocess.run([sys.executable, str(lf.SELF_DIR / "plot_inspector.py")], capture_output=True,
                                text=True, encoding="utf-8", errors="replace", timeout=300)
    except Exception as e:
        log(f"inspector: graphs/ not updated ({type(e).__name__}: {e})")
        return False
    if result.returncode != 0:
        log(f"inspector: graphs/ not updated: {(result.stderr or result.stdout).strip()[-300:]}")
        return False
    log("inspector: graphs/ updated")
    return True


def inspect(batch_id: int, plan_rows: list = None, max_add: int = DEFAULT_MAX_ADD,
            max_refine: int = DEFAULT_MAX_REFINE, min_finished: float = DEFAULT_MIN_FINISHED, log=print,
            entry: dict = None, graphs: bool = True) -> dict:
    """Count, decide, record the CSV row and (graphs=True) redraw graphs/."""
    row = count_batch(batch_id, plan_rows, entry=entry)
    row["decision"], row["reason"] = decide(row, max_add, max_refine, min_finished)
    row["inspected_at"] = lf.now_iso()
    upsert_csv(row)
    per_ds = ", ".join(f"{ds} {row[f'add_{ds}']}/{row[f'refine_{ds}']}" for ds in lf.DATASETS)
    per_ds_acc = ", ".join(f"{ds} {row[f'accepted_add_{ds}']}/{row[f'accepted_refine_{ds}']}" for ds in lf.DATASETS)
    log(f"inspector: batch {batch_id}: translators {row['translators_finished']}/{row['translators_planned']} finished "
        f"({row['successful_translations']} successful, {row['failed_translations']} failed)")
    log(f"inspector: batch {batch_id}: suggestions add {row['add_total']} (of them {row['add_lexical_group']} new "
        f"value groups), refine {row['refine_total']} (add/refine per dataset: {per_ds}); "
        f"{row['label_preserved_needs']} needs covered by a group label only")
    log(f"inspector: batch {batch_id}: accepted add {row['accepted_add_total']}, refine {row['accepted_refine_total']} "
        f"({row['accepted_pct']}% of suggestions; per dataset: {per_ds_acc}); ops "
        + ", ".join(f"{op} {row[f'ops_{op}']}" for op in APPLIED_OPS))
    if row["leaf_value_adds"]:
        log(f"inspector: batch {batch_id}: LEAF VALUES ADDED AS RECORDS ({row['leaf_value_adds']}): "
            f"{row['leaf_value_symbols']} — check whether a value group should hold them instead")
    log(f"inspector: batch {batch_id}: decision {row['decision'].upper()} — {row['reason']}")
    if graphs:
        refresh_graphs(log)
    return row


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--batch", type=int)
    g.add_argument("--batches", help="a range lo-hi: recompute each batch's row")
    p.add_argument("--max-add", type=int, default=DEFAULT_MAX_ADD)
    p.add_argument("--max-refine", type=int, default=DEFAULT_MAX_REFINE)
    p.add_argument("--min-finished", type=float, default=DEFAULT_MIN_FINISHED)
    args = p.parse_args(argv)
    if args.batches:
        lo, hi = (int(x) for x in args.batches.split("-"))
        ids = range(lo, hi + 1)
    else:
        ids = [args.batch]
    row = None
    for b in ids:
        # one redraw at the end, not one per recomputed batch
        row = inspect(b, max_add=args.max_add, max_refine=args.max_refine, min_finished=args.min_finished,
                      graphs=b == ids[-1])
    sys.exit(STOP_EXIT_CODE if row and row["decision"] == "stop" else 0)


if __name__ == "__main__":
    main()
