# swarm

Runs one task (currently: translating trajectories into BrainCode) against many
records, one isolated `docker run` per record.

## Recommended: via Claude Code

Use the `orchestrator` skill — tell Claude Code where your data lives and let it
locate, batch, and run it:

> "The dataset is at /path/to/data.jsonl. Go."

Looking for data to feed it first? See the `miner` skill.

## Manual setup & run

```bash
cd swarm
pip install -r requirements.txt
cp .env.example .env
# fill in PROXY_API_KEY — see ../vertex-proxy/OPENCODE_SETUP.md
```

Put your data in `data/` as JSONL — one JSON object per line, each with a
`content` field (`<|user|>`/`<|assistant|>` turns; `id` optional). Then:

```bash
./run_batch.sh my-experiment          # or: ./run_batch.sh my-experiment 50
```

That's the two steps below in one line. `sample_batch.py` writes the next free
`batches/batch-NN.jsonl`, sampling only records that aren't already in `output/`,
`failures/`, or an earlier batch; `spawn_batch.py` dispatches a batch file. Run
them separately for a different filter, or to re-run an existing batch, which
retries just its failures:

```bash
python3 spawn_batch.py batches/batch-07.jsonl output/
```

Results land in `output/<hash6>-<slug>/`, one folder per successful record.
Anything that failed leaves its logs in `failures/` instead, and re-running the
same batch retries just those.

## Layout

- `run_batch.sh` — sample + dispatch in one line; the normal entry point.
- `spawn_batch.py` — the dispatcher.
- `sample_batch.py` — draws a batch file from `data/`, excluding anything already processed.
- `tasks/`, `harnesses/` — pluggable task/harness definitions.
- `reference/` — the BrainCode language spec (`DESIGN_DOC.md`), mounted read-only into every subagent at `/reference`.
- `.env` / `.env.example` — config, auto-loaded.

See `ADVANCED.md` for config variables, output format, adding a task/harness,
security posture, running the tests, and running without Claude Code.
