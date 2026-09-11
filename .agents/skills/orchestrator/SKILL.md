---
name: orchestrator
description: Run or configure the swarm pipeline (spawn_batch.py) in this repo — tasks, harnesses, models, batching. Use when asked to run discovery, translate trajectories into BrainCode, kick off a batch, or add a new task/harness/model.
---

# Orchestrator

This repo's pipeline for running one task against many trajectories, isolated per
record. Entry point: `swarm/spawn_batch.py`. For the architecture behind any of
this — why the task/harness split exists, the security posture, known failure
modes — read `swarm/ADVANCED.md` before re-deriving it from the code.

## Concepts

- **Task** (`SWARM_TASK`) — what each subagent is asked to do. Currently one:
  `discovery` (`swarm/tasks/discovery.md`) — translates one trajectory into
  BrainCode (see `swarm/reference/DESIGN_DOC.md` for the language). A task file's content
  *is* the prompt sent to the subagent, verbatim; nothing else to configure.
- **Harness** (`SWARM_HARNESS`) — which CLI agent actually runs the model, each in
  its own Docker image. Currently two: `pi` (default) and `opencode`, folders under
  `swarm/harnesses/` (`Dockerfile` + `entrypoint.sh` + config). Adding a harness
  means adding a folder there; `spawn_batch.py` never branches on which one runs.
- **Model** (`SWARM_MODEL`) — passed straight through to the harness's entrypoint
  as an env var. Three are wired up, all via the vertex-proxy backend (see
  `vertex-proxy/OPENCODE_SETUP.md`): `vertex-proxy/gemini-3.5-flash` (the
  default), `vertex-proxy/gemini-flash` (Gemini 3.7 Flash, medium reasoning
  effort), and `vertex-proxy/gemini-flash-high` (same model, high effort). Reaching a
  model takes two things — the proxy has to serve the alias *and* the harness has
  to declare it (`swarm/harnesses/opencode/config.jsonc`'s `models` block,
  `swarm/harnesses/pi/models.template.json`'s `models` array); a string the
  harness doesn't declare won't resolve no matter what the proxy serves, so check
  both before assuming.

  Worth knowing when choosing: 3.7 Flash does no implicit prompt caching, while
  3.5 Flash caches a growing conversation's prefix automatically. Over a long run
  that's a real cost difference, not a detail.

## Running a batch

1. Get data into JSONL under `swarm/data/`: one JSON object per line, each with
   `content` (the raw trajectory, `<|user|>`/`<|assistant|>` turns). `id` is
   optional — output folders are named from a content hash rather than from it —
   but include it when the source has one, since it catches a record re-offered
   with a re-serialized line, which a hash cannot. See `.claude/skills/miner` for
   what counts as a good trajectory.
2. Run it: `swarm/run_batch.sh <experiment> [count]` does steps 2 and 4 in one line and
   is the normal way to start a run. To sample without dispatching, `python3
   swarm/sample_batch.py -n 30` writes the next free
   `swarm/batches/batch-NN.jsonl`. **Don't hand-roll the sampling.** It excludes
   every record already in `output/`, `failures/`, and any prior batch file, by
   `id` as well as by content hash — get that wrong and a run silently re-does
   work, which is invisible in the results and expensive. Useful flags:
   `--max-chars` (cap trajectory length), `--latin-only` (keep a corpus readable
   for review), `--min-chars`, `--data` (files, dirs, or globs), `--seed`. It
   prints why records were rejected, which is how you tell an exhausted pool from
   a too-strict filter.
3. `pip install -r swarm/requirements.txt` (just `litellm`, used to name output
   folders). Ensure `swarm/.env` exists (`cp swarm/.env.example swarm/.env`, fill
   in `PROXY_API_KEY`) — or export `PROXY_API_KEY`/`PROXY_BASE_URL`/`SWARM_*`
   directly; real env vars always win over `.env`.
4. For each batch file: `python3 swarm/spawn_batch.py swarm/batches/batch-NN.jsonl
   swarm/output/`. Don't dispatch the same batch file from two invocations at
   once — `spawn_batch.py` doesn't coordinate across simultaneous runs of itself,
   only within one run's own concurrency.
5. Results land in `swarm/output/<hash6>-<slug>/` — one folder per record, named
   from a content-hash prefix plus an LLM-generated slug describing that
   trajectory specifically. `metadata.json` on success (with the full hash,
   a timestamp, and `SWARM_TASK`/`SWARM_HARNESS`/`SWARM_MODEL`), which doubles as
   the marker a later run checks: re-running against refreshed or additional data
   only reprocesses records whose content hash isn't already recorded.
6. `swarm/output/` holds successes only. A failed record's logs go to
   `swarm/failures/<hash6>[-n]/` instead — one directory per *attempt*, with
   `failure.json` carrying the container's exit code, whether it wrote
   anything, how long it ran, and the harness's last error line (`null` when it
   reported none, which is the signature of a run that stalled rather than
   failed). These survive later runs, so re-running a batch to retry its
   failures doesn't cost you the evidence from the previous attempt. Read the
   `-n` suffix as nothing more than "the name was taken" — it happens both when
   one record fails repeatedly and when two records share a hash prefix, so
   group by `failure.json`'s full `hash`, not by name (see
   `swarm/ADVANCED.md`).

Data doesn't have to be one static source, and this isn't a one-time run: mixed
sources and data that grows over time are the normal case, not an edge case — call
`spawn_batch.py` again whenever there's a new batch, from wherever it came from.

## Parameters

| Var | Default | Meaning |
|---|---|---|
| `SWARM_HARNESS` | `pi` | picks `swarm/harnesses/$SWARM_HARNESS/` |
| `SWARM_TASK` | `discovery` | picks `swarm/tasks/$SWARM_TASK.md` |
| `SWARM_MODEL` | `vertex-proxy/gemini-3.5-flash` | passed to the harness's entrypoint |
| `SWARM_CONCURRENCY` | `16` | concurrent `docker run`s within one `spawn_batch.py` call |
| `SWARM_TIMEOUT` | `1200` | seconds before a record's container is killed and recorded as failed |
| `SWARM_EXPERIMENT` | *(unset)* | recorded in each record's `metadata.json`; tags which run it came from |
| `PROXY_API_KEY` | *(required)* | — |
| `PROXY_BASE_URL` | vertex-proxy's URL | the model backend every harness talks to |
