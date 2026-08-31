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

Batch your data yourself — one JSON object per line, each with a `content`
field (`<|user|>`/`<|assistant|>` turns; `id` is optional and unused) — then run
each batch file:

```bash
python3 spawn_batch.py batches/batch-01.jsonl output/
```

Results land in `output/<hash6>-<slug>/`, one folder per successful record.
Anything that failed leaves its logs in `failures/` instead, and re-running the
same batch retries just those.

## Layout

- `spawn_batch.py` — the dispatcher.
- `tasks/`, `harnesses/` — pluggable task/harness definitions.
- `DESIGN_DOC.md` — the BrainCode language reference, mounted into every subagent.
- `.env` / `.env.example` — config, auto-loaded.

See `ADVANCED.md` for config variables, output format, adding a task/harness,
security posture, running the tests, and running without Claude Code.
