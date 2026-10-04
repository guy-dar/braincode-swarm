#!/usr/bin/env python3
"""The translator -> migrator -> inspector loop.

    python loop.py plan   [--per-dataset 500] [--batch-size 30] [--seed 42]
    python loop.py run    [--max-batches N] [--no-dense] [--continue-after-stop]
    python loop.py status

`plan` draws --per-dataset train items from each of the six datasets in
data/ (all of a dataset's train items if it has fewer), shuffles them
together and cuts them into batches; each row gets its translator id
`<batch_id>-<tnum_inside_batch>`. The plan is frozen in runs/plan.jsonl.

`run` processes batches in order, resuming where it left off:
  1. translators   — translate_batch.run_batch: batch-size containers at once
  2. migrator      — migrate.run_migration: suggestions -> glossary (+ RAG reindex)
  3. inspector     — inspector.inspect: counts -> CSV -> stop or continue
The glossary RAG server runs in-process for the whole run (translators
reach it at host.docker.internal:$RAG_PORT); a migration reloads it.

Configuration (environment or swarm/.env):
  PROXY_API_KEY (required), PROXY_BASE_URL
  SWARM_MODEL      translator model     (default vertex-proxy/gemini-3.5-flash)
  MIGRATOR_MODEL   migrator model       (default vertex-proxy/gemini-flash-high)
  NEEDS_MODEL      need-extraction model (default: SWARM_MODEL)
  SWARM_HARNESS / MIGRATOR_HARNESS      (default pi)
  SWARM_TIMEOUT / MIGRATOR_TIMEOUT      seconds (default 1200 / 3600)
  RAG_PORT / RAG_HOST                    (default 8765 / 0.0.0.0)
  PER_DATASET / BATCH_SIZE / LOOP_SEED   plan defaults (500 / 30 / 42)
  LOOP_CONCURRENCY translators running at once within a batch (default 10)
  PREFETCH_WORKERS parallel need extractions when prefetching the next batch (default 4)
  THROTTLE=0 to disable the model-call gateway (throttle.py); THROTTLE_PORT (8766),
  THROTTLE_CONCURRENCY max model calls in flight (6), THROTTLE_MIN (2), THROTTLE_RAISE_AFTER (20)

Translators get the spec (reference/language-spec.compact.md, built by
spec_compact.py), their retrieval context and the output formats attached to
their first message (harness /attach), and need extraction for batch N+1 runs
while batch N migrates (cached in runs/needs_cache/).
"""
import argparse
import contextlib
import json
import os
import random
import subprocess
import sys
import threading
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import loop_files as lf
import utils

# The main stratification feature of each dataset, as documented in
# data/README.md (written by fetch_datasets.py, which defines it).
STRATIFY_KEYS = {
    "mind2web": "domain",
    "alfred": "task_type",
    "swebench": "repo_stratum",
    "prism": "conversation_type",
    "paths": "primary_task",
    "thoughttrace": "model_provider",
}


@dataclass
class LoopConfig:
    model: str
    migrator_model: str
    harness_name: str
    migrator_harness: str
    timeout_s: int
    migrator_timeout_s: int
    rag_port: int
    rag_host: str
    per_dataset: int
    batch_size: int
    concurrency: int
    prefetch_workers: int
    seed: int
    api_key: str
    base_url: str


def load_loop_config() -> LoopConfig:
    utils.load_dotenv(lf.SELF_DIR / ".env")
    api_key = os.environ.get("PROXY_API_KEY", "")
    if not api_key:
        sys.exit("loop: PROXY_API_KEY not set (checked environment and swarm/.env)")
    cfg = LoopConfig(
        model=os.environ.get("SWARM_MODEL", "vertex-proxy/gemini-3.5-flash"),
        migrator_model=os.environ.get("MIGRATOR_MODEL", "vertex-proxy/gemini-flash-high"),
        harness_name=os.environ.get("SWARM_HARNESS", "pi"),
        migrator_harness=os.environ.get("MIGRATOR_HARNESS", os.environ.get("SWARM_HARNESS", "pi")),
        timeout_s=int(os.environ.get("SWARM_TIMEOUT", "1200")),
        migrator_timeout_s=int(os.environ.get("MIGRATOR_TIMEOUT", "3600")),
        rag_port=int(os.environ.get("RAG_PORT", "8765")),
        rag_host=os.environ.get("RAG_HOST", "0.0.0.0"),
        per_dataset=int(os.environ.get("PER_DATASET", "500")),
        batch_size=int(os.environ.get("BATCH_SIZE", "30")),
        # Translators in flight at once. A batch is still BATCH_SIZE items;
        # this only bounds how many hit the model proxy simultaneously — 30 at
        # once draws Cloudflare 429s from the proxy (see harnesses/pi/settings.json).
        concurrency=int(os.environ.get("LOOP_CONCURRENCY", "10")),
        prefetch_workers=int(os.environ.get("PREFETCH_WORKERS", "4")),
        seed=int(os.environ.get("LOOP_SEED", "42")),
        api_key=api_key,
        base_url=os.environ.setdefault("PROXY_BASE_URL", "https://vertex-proxy-v26q.onrender.com/v1"),
    )
    for harness in {cfg.harness_name, cfg.migrator_harness}:
        if not (lf.SELF_DIR / "harnesses" / harness / "Dockerfile").exists():
            sys.exit(f"loop: no such harness: harnesses/{harness}")
    return cfg


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


# ---------------------------------------------------------------------- plan

def _stratum(line: str, key) -> str:
    if not key:
        return ""
    try:
        return str(json.loads(line).get(key))
    except (ValueError, AttributeError):
        return "None"


def stratified_sample(lines: list, n: int, key, rng: random.Random) -> list:
    """n lines whose `key` distribution matches the whole file's: each stratum
    gets its proportional share, rounded by largest remainder, so the sample
    keeps the split's composition (data/README.md documents the keys)."""
    if not key:
        return rng.sample(lines, n)
    groups = {}
    for line in lines:
        groups.setdefault(_stratum(line, key), []).append(line)
    total = len(lines)
    quotas = {s: n * len(g) / total for s, g in groups.items()}
    alloc = {s: int(q) for s, q in quotas.items()}
    for s in sorted(quotas, key=lambda s: (quotas[s] - alloc[s], s), reverse=True)[: n - sum(alloc.values())]:
        alloc[s] += 1
    chosen = []
    for s in sorted(groups):
        chosen += rng.sample(groups[s], min(alloc[s], len(groups[s])))
    return chosen


def interleave_strata(lines: list, key, rng: random.Random) -> list:
    """Order a dataset's items so consecutive items cycle through strata
    (largest first). Dealt round-robin into batches, this gives each batch a
    spread of the dataset's strata instead of clusters of one."""
    groups = {}
    for line in lines:
        groups.setdefault(_stratum(line, key), []).append(line)
    for g in groups.values():
        rng.shuffle(g)
    order = sorted(groups, key=lambda s: (-len(groups[s]), s))
    # Spread each stratum evenly over the sequence: item i of a stratum with
    # m items gets position (i + offset) / m, then sort by position.
    placed = []
    for rank, s in enumerate(order):
        m = len(groups[s])
        offset = rng.random()
        placed += [((i + offset) / m, rank, line) for i, line in enumerate(groups[s])]
    placed.sort(key=lambda t: (t[0], t[1]))
    return [line for _, _, line in placed]


def build_plan(per_dataset: int, batch_size: int, seed: int, data_dir: Path = lf.DATA_DIR,
               datasets=lf.DATASETS) -> tuple:
    """(rows, summary). Each dataset contributes min(per_dataset, its train
    size) items — the fallback: a dataset with fewer train items gives all of
    them.

    Stratified twice:
    - the sample: each dataset's items are drawn in proportion to its main
      feature (STRATIFY_KEYS, as in data/README.md), so 500 PRISM items keep
      PRISM's conversation_type mix;
    - the batches: every batch takes an equal, consecutive chunk of each
      dataset's stratum-interleaved sequence (500 per dataset over 100
      batches of 30 -> exactly 5 of each dataset per batch, spread over that
      dataset's strata). A dataset with fewer items is spread as evenly as it
      can be. Order within a batch is shuffled."""
    rng = random.Random(seed)
    per_ds, summary = {}, []
    for ds in datasets:
        path = data_dir / ds / "train.jsonl"
        if not path.exists():
            summary.append({"dataset": ds, "available": 0, "taken": 0, "note": "missing train.jsonl"})
            continue
        with path.open(encoding="utf-8") as fh:
            lines = [line.rstrip("\n") for line in fh if line.strip()]
        key = STRATIFY_KEYS.get(ds)
        if len(lines) > per_dataset:
            chosen = stratified_sample(lines, per_dataset, key, rng)
            note = ""
        else:
            chosen = list(lines)
            note = f"fallback: only {len(lines)} train items, all taken"
        chosen = interleave_strata(chosen, key, rng)
        per_ds[ds] = chosen
        summary.append({"dataset": ds, "available": len(lines), "taken": len(chosen), "note": note,
                        "stratified_on": key,
                        "strata_train": dict(Counter(_stratum(l, key) for l in lines).most_common()),
                        "strata_taken": dict(Counter(_stratum(l, key) for l in chosen).most_common())})
    total = sum(len(v) for v in per_ds.values())
    n_batches = max(1, -(-total // batch_size))
    batches = [[] for _ in range(n_batches)]
    # Each batch takes a consecutive chunk of each dataset's sequence (item j
    # of m goes to batch j * n_batches // m): equal shares per batch, and —
    # because interleave_strata cycles strata along the sequence — a spread
    # of strata within each chunk. A short dataset's chunks are evenly
    # spaced over all batches rather than packed into the first ones.
    for ds, lines in per_ds.items():
        m = len(lines)
        for j, line in enumerate(lines):
            batches[j * n_batches // m].append((ds, line))
    rows = []
    for b, items in enumerate(batches, 1):
        rng.shuffle(items)
        for t, (ds, line) in enumerate(items, 1):
            rows.append({"translator_id": lf.translator_id(b, t), "batch_id": b, "tnum": t,
                         "dataset": ds, "record_line": line})
    return rows, summary


def write_plan(rows: list, meta: dict, path: Path = lf.PLAN_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    (path.parent / "plan_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")


def cmd_plan(args, cfg: LoopConfig = None):
    per_dataset = args.per_dataset or (cfg.per_dataset if cfg else int(os.environ.get("PER_DATASET", "500")))
    batch_size = args.batch_size or (cfg.batch_size if cfg else int(os.environ.get("BATCH_SIZE", "30")))
    seed = args.seed if args.seed is not None else (cfg.seed if cfg else int(os.environ.get("LOOP_SEED", "42")))
    if lf.PLAN_PATH.exists() and not args.force:
        sys.exit(f"loop: {lf.PLAN_PATH.relative_to(lf.SELF_DIR)} exists — the plan is frozen once written. "
                 f"Use --force to replace it (only before any batch has run).")
    rows, summary = build_plan(per_dataset, batch_size, seed)
    batches = lf.plan_batches(rows)
    write_plan(rows, {"per_dataset": per_dataset, "batch_size": batch_size, "seed": seed,
                      "datasets": summary, "translators": len(rows), "batches": len(batches),
                      "created_at": lf.now_iso()})
    for s in summary:
        log(f"plan: {s['dataset']:<13} {s['taken']:>5} of {s['available']:>6} train items"
            + (f"  ({s['note']})" if s["note"] else ""))
    log(f"plan: {len(rows)} translators in {len(batches)} batches of {batch_size} -> "
        f"{lf.PLAN_PATH.relative_to(lf.SELF_DIR)}")
    return rows


# ---------------------------------------------------------------------- services

def build_image(harness: str) -> str:
    image = f"braincode-swarm-{harness}"
    log(f"loop: building harness image {image} ...")
    subprocess.run(["docker", "build", "-q", "-t", image, str(lf.SELF_DIR / "harnesses" / harness)], check=True,
                   stdout=subprocess.DEVNULL)
    return image


CONTAINER_PREFIXES = ("swarm-tr-", "swarm-mig-")
TRANSLATOR_ROUNDS = 3
ROUND_PAUSE_S = 120


def kill_loop_containers() -> int:
    """Kill every translator/migrator container still running. Stopping the
    loop kills the `docker run` clients but not the containers behind them,
    which otherwise keep running (and spending tokens) unattended."""
    try:
        names = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True,
                               timeout=60).stdout.split()
    except Exception:
        return 0
    mine = [n for n in names if n.startswith(CONTAINER_PREFIXES)]
    if mine:
        subprocess.run(["docker", "kill", *mine], capture_output=True, text=True, timeout=120)
    return len(mine)


THROTTLE = {"server": None}


def start_throttle(cfg: "LoopConfig"):
    """Route every model call of the run through throttle.py (unless
    THROTTLE=0): containers get it as PROXY_BASE_URL, need extraction as
    NEEDS_BASE_URL; the real proxy becomes its upstream."""
    if os.environ.get("THROTTLE", "1") == "0":
        return None
    import throttle
    port = int(os.environ.get("THROTTLE_PORT", "8766"))
    gate = throttle.gate_from_env()
    server = throttle.ThrottleServer(cfg.base_url, cfg.rag_host, port, gate).start()
    os.environ["PROXY_BASE_URL"] = f"http://host.docker.internal:{port}/v1"
    os.environ["NEEDS_BASE_URL"] = f"http://127.0.0.1:{port}/v1"
    THROTTLE["server"] = server
    log(f"loop: throttle on :{port} -> {cfg.base_url} (up to {gate.max_inflight} model calls in flight, "
        f"adaptive down to {gate.min_inflight})")
    return server


def throttle_stats() -> dict:
    server = THROTTLE.get("server")
    return server.gate.snapshot() if server is not None else {}


@contextlib.contextmanager
def rag_service(cfg: LoopConfig, dense: bool = True):
    """The glossary RAG for the duration of a run: an in-process Retriever
    (rebuilt from glossary.jsonl if the index is stale) served over HTTP so
    containers can reach it."""
    from glossary import records as rec_mod
    from rag.retrieve import Retriever
    from rag.server import RagServer
    if not rec_mod.GLOSSARY_JSONL.exists():
        sys.exit("loop: reference/glossary.jsonl is missing — import it first: "
                 "python -m glossary.import_legacy <legacy glossary.md> reference/glossary.jsonl")
    errors = rec_mod.validate(rec_mod.load())
    if errors:
        sys.exit("loop: reference/glossary.jsonl is invalid:\n  " + "\n  ".join(errors[:20]))
    # A previous run killed from outside never reached its own cleanup; its
    # containers may still be running and must not overlap this run's.
    stale = kill_loop_containers()
    if stale:
        log(f"loop: killed {stale} leftover container(s) from a previous run")
    log("loop: loading glossary RAG index ...")
    retriever = Retriever(dense=dense)
    server = RagServer(retriever, cfg.rag_host, cfg.rag_port).start()
    log(f"loop: RAG server on {cfg.rag_host}:{cfg.rag_port} ({len(retriever.index.records)} records, dense={dense})")
    gateway = start_throttle(cfg)
    try:
        yield retriever
    finally:
        if gateway is not None:
            log(f"loop: throttle totals: {gateway.gate.snapshot()}")
            gateway.stop()
        # Set before killing containers: their `docker run` clients then exit
        # non-zero, and without the flag a worker would read that as a failed
        # attempt and start a retry container during shutdown.
        import translate_batch
        translate_batch.STOPPING.set()
        server.stop()
        killed = kill_loop_containers()
        if killed:
            log(f"loop: killed {killed} container(s) still running at exit")


# ---------------------------------------------------------------------- state

def load_state() -> dict:
    if lf.STATE_PATH.exists():
        return json.loads(lf.STATE_PATH.read_text(encoding="utf-8"))
    return {"batches": {}, "stopped": None}


def save_state(state: dict) -> None:
    lf.STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = lf.STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2), encoding="utf-8")
    tmp.replace(lf.STATE_PATH)


# ---------------------------------------------------------------------- run

def cmd_run(args, cfg: LoopConfig):
    import inspector
    import migrate
    import translate_batch
    from glossary import manifest

    if not lf.PLAN_PATH.exists():
        cmd_plan(args, cfg)
    batches = lf.plan_batches(lf.load_plan())
    state = load_state()
    if state.get("stopped") and not args.continue_after_stop:
        log(f"loop: stopped early after batch {state['stopped']['batch']} ({state['stopped']['reason']}). "
            f"Pass --continue-after-stop to keep going.")
        return
    state["stopped"] = None

    processed = 0
    prefetch = None
    with rag_service(cfg, dense=not args.no_dense) as retriever:
        translator_image = build_image(cfg.harness_name)
        migrator_image = translator_image if cfg.migrator_harness == cfg.harness_name else build_image(cfg.migrator_harness)
        for batch_id, rows in batches.items():
            entry = state["batches"].setdefault(str(batch_id), {})
            if entry.get("inspection"):
                continue
            if args.max_batches and processed >= args.max_batches:
                log(f"loop: --max-batches {args.max_batches} reached; next run resumes at batch {batch_id}")
                break
            processed += 1
            if prefetch is not None:
                prefetch.join()  # the previous batch's prefetch of this batch's needs
                prefetch = None
            log(f"\n=== batch {batch_id}/{len(batches)} ({len(rows)} translators) — glossary "
                f"{manifest.current_version()} ===")

            # Translators that errored (proxy outages, unusable output) are run
            # again — a translator only counts once its output is routed —
            # for up to TRANSLATOR_ROUNDS rounds, across resumes too. After
            # that the batch moves on and the inspector's completion guard
            # sees the gap.
            while entry.get("translators") != "done":
                entry["translator_rounds"] = entry.get("translator_rounds", 0) + 1
                summary = translate_batch.run_batch(batch_id, rows, cfg, retriever, translator_image,
                                                    manifest.current_version(), log=log)
                counts = summary["counts"]
                unfinished = [r["tid"] for r in summary["results"] if r["outcome"] in ("error", "interrupted")]
                entry["translator_counts"] = counts
                used = entry.setdefault("translator_usage", {})
                for key, value in (summary.get("usage") or {}).items():
                    used[key] = used.get(key, 0) + value
                if not unfinished or entry["translator_rounds"] >= TRANSLATOR_ROUNDS:
                    entry["translators"] = "done"
                save_state(state)
                entry["throttle_after_translators"] = throttle_stats()
                log(f"loop: throttle so far: {entry['throttle_after_translators']}")
                log(f"loop: batch {batch_id} translators round {entry['translator_rounds']}: {counts}"
                    + (f"; unfinished: {', '.join(unfinished)}" if unfinished else ""))
                if unfinished and entry.get("translators") != "done":
                    log(f"loop: re-running {len(unfinished)} unfinished translator(s) after a pause")
                    time.sleep(ROUND_PAUSE_S)

            # Need extraction doesn't depend on the glossary, so the next
            # batch's needs are extracted now, alongside this batch's
            # migration (when the proxy is mostly idle), instead of on each
            # translator's critical path. Only for a batch this run will reach.
            ids = list(batches)
            pos = ids.index(batch_id)
            nxt = ids[pos + 1] if pos + 1 < len(ids) else None
            if nxt is not None and (not args.max_batches or processed < args.max_batches) and prefetch is None:
                prefetch = threading.Thread(target=_prefetch, args=(nxt, batches[nxt], cfg), daemon=True,
                                            name=f"prefetch-{nxt}")
                prefetch.start()

            if not entry.get("migration"):
                result = migrate.run_migration(batch_id, cfg, retriever, migrator_image, log=log,
                                               premigrator_image=translator_image)
                entry["migration"] = result["status"]
                entry["glossary_version"] = result["version"]
                entry["migration_usage"] = result.get("usage", {})
                entry["throttle_after_migration"] = throttle_stats()
                save_state(state)

            row = inspector.inspect(batch_id, rows, min_finished=args.min_finished, log=log)
            entry["inspection"] = {"decision": row["decision"], "reason": row["reason"],
                                   "add": row["add_total"], "refine": row["refine_total"]}
            save_state(state)
            if row["decision"] == "stop":
                state["stopped"] = {"batch": batch_id, "reason": row["reason"]}
                save_state(state)
                log(f"loop: early stop after batch {batch_id}")
                break
    cmd_status(args)


def _prefetch(batch_id: int, rows: list, cfg: LoopConfig):
    import translate_batch
    started = time.monotonic()
    try:
        counts = translate_batch.prefetch_needs(rows, workers=cfg.prefetch_workers, log=log)
        log(f"loop: prefetched needs for batch {batch_id} in {time.monotonic() - started:.0f}s: {counts}")
    except Exception as e:  # a failed prefetch only means translators extract live
        log(f"loop: needs prefetch for batch {batch_id} failed ({type(e).__name__}: {e}); translators will extract live")


def cmd_status(args):
    plan = lf.load_plan()
    batches = lf.plan_batches(plan)
    state = load_state()
    done = [b for b, e in state["batches"].items() if e.get("inspection")]
    print(f"plan: {len(plan)} translators in {len(batches)} batches; {len(done)} batches complete")
    for b, e in sorted(state["batches"].items(), key=lambda kv: int(kv[0])):
        insp = e.get("inspection") or {}
        print(f"  batch {b:>3}: translators {e.get('translator_counts', {})}, migration {e.get('migration', '-')}, "
              f"glossary {e.get('glossary_version', '-')}, add {insp.get('add', '-')}, refine {insp.get('refine', '-')}, "
              f"{insp.get('decision', 'in progress')}")
        for label in ("translator_usage", "migration_usage"):
            u = e.get(label)
            if u:
                print(f"             {label.split('_')[0]} tokens: {u.get('calls', 0)} calls, input {u.get('input', 0):,} "
                      f"+ cached {u.get('cacheRead', 0):,}, output {u.get('output', 0):,} "
                      f"(+ {u.get('reasoning', 0):,} reasoning)")
    if state.get("stopped"):
        print(f"stopped early after batch {state['stopped']['batch']}: {state['stopped']['reason']}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", choices=["plan", "run", "status"])
    p.add_argument("--per-dataset", type=int)
    p.add_argument("--batch-size", type=int)
    p.add_argument("--seed", type=int)
    p.add_argument("--force", action="store_true", help="plan: replace an existing plan")
    p.add_argument("--max-batches", type=int, default=0, help="run: process at most this many batches now")
    p.add_argument("--min-finished", type=float, default=0.8, help="inspector's completion guard")
    p.add_argument("--no-dense", action="store_true", help="RAG without the embedding model")
    p.add_argument("--continue-after-stop", action="store_true")
    args = p.parse_args(argv)
    if args.command == "status":
        return cmd_status(args)
    if args.command == "plan":
        utils.load_dotenv(lf.SELF_DIR / ".env")
        return cmd_plan(args)
    cmd_run(args, load_loop_config())


if __name__ == "__main__":
    main()
