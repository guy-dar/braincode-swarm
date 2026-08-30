---
name: orchestrator
description: Run or configure the swarm pipeline (spawn_batch.py) in this repo — tasks, harnesses, models, batching. Use when asked to run discovery, translate trajectories into BrainCode, kick off a batch, or add a new task/harness/model.
---

# Orchestrator

This repo's pipeline for running one task against many trajectories, isolated per
record. Entry point: `swarm/spawn_batch.py`. For the architecture behind any of
this — why the task/harness split exists, the security posture, known failure
modes — read `swarm/README.md` before re-deriving it from the code.

## Concepts

- **Task** (`SWARM_TASK`) — what each subagent is asked to do. Currently one:
  `discovery` (`swarm/tasks/discovery.md`) — translates one trajectory into
  BrainCode (see `swarm/DESIGN_DOC.md` for the language). A task file's content
  *is* the prompt sent to the subagent, verbatim; nothing else to configure.
- **Harness** (`SWARM_HARNESS`) — which CLI agent actually runs the model, each in
  its own Docker image. Currently two: `opencode` (default) and `pi`, folders under
  `swarm/harnesses/` (`Dockerfile` + `entrypoint.sh` + config). Adding a harness
  means adding a folder there; `spawn_batch.py` never branches on which one runs.
- **Model** (`SWARM_MODEL`) — passed straight through to the harness's entrypoint
  as an env var. Currently one is actually wired up: `vertex-proxy/gemini-flash`
  (Gemini 3.7 Flash, via the vertex-proxy backend — see
  `vertex-proxy/OPENCODE_SETUP.md`). More get added by extending a harness's own
  config (`swarm/harnesses/opencode/config.jsonc`'s `models` block,
  `swarm/harnesses/pi/models.template.json`'s `models` array) — check those files
  for what's actually live before assuming a model string will resolve.

## Running a batch

1. Get data into JSONL: one JSON object per line, each with `content` (the raw
   trajectory, `<|user|>`/`<|assistant|>` turns — see `swarm/DESIGN_DOC.md`'s
   Glossary for the Turn definition). An `id` field is optional and unused by the
   pipeline — output folder names are derived from each record's content, not
   from `id`. See `.claude/skills/miner` for what counts as a good trajectory and
   where to stage one before it's batched.
2. Split into `swarm/batches/batch-NN.jsonl` files (~20 records each is a
   reasonable default — `SWARM_BATCH_SIZE`, informational, not enforced by the
   script).
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
   only reprocesses records whose content hash isn't already recorded. A folder
   with no `metadata.json` (only `stdout.log`/`stderr.log`) failed — check its
   logs.

Data doesn't have to be one static source, and this isn't a one-time run: mixed
sources and data that grows over time are the normal case, not an edge case — call
`spawn_batch.py` again whenever there's a new batch, from wherever it came from.

## Parameters

| Var | Default | Meaning |
|---|---|---|
| `SWARM_HARNESS` | `opencode` | picks `swarm/harnesses/$SWARM_HARNESS/` |
| `SWARM_TASK` | `discovery` | picks `swarm/tasks/$SWARM_TASK.md` |
| `SWARM_MODEL` | `vertex-proxy/gemini-flash` | passed to the harness's entrypoint |
| `SWARM_CONCURRENCY` | `4` | concurrent `docker run`s within one `spawn_batch.py` call |
| `SWARM_BATCH_SIZE` | `20` | informational — how you split data, not enforced |
| `SWARM_EXPERIMENT` | *(unset)* | recorded in each record's `metadata.json`; tags which run it came from |
| `PROXY_API_KEY` | *(required)* | — |
| `PROXY_BASE_URL` | vertex-proxy's URL | the model backend every harness talks to |
