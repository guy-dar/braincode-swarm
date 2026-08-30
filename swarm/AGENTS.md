# Swarm Orchestrator

Given a prompt describing where trajectory data lives, locate it, batch it, and
spawn one subagent per record — never do the task yourself. Data doesn't have to be
one static source: it may be mixed from several places, or extended later with a
newly-mined batch — that's fine, run this as many times as you have batches, from
however many sources, whenever new data shows up. Which task each subagent runs, and
which harness runs it, are not your concern; those are decided by `SWARM_TASK` and
`SWARM_HARNESS` (read from `.env`/the environment by `spawn_batch.py`, defaulting to
`discovery` and `opencode`) and the corresponding files under `tasks/` and
`harnesses/`. See `.claude/skills/miner` for what makes a good source and
`.claude/skills/orchestrator` for the fuller parameter reference.

1. Locate and read the data with your tools (bash/file/web). Confirm you can
   enumerate individual records before proceeding.
2. Normalize records to one JSON object per line, each with a `content` field
   (`<|user|>`/`<|assistant|>` turns), into `batches/source.jsonl`. An `id` field
   is optional — output folder names are derived from each record's content, not
   from `id`, so mixing sources with unrelated or absent ids is fine.
3. Split into `batches/batch-NN.jsonl` files of `SWARM_BATCH_SIZE` records each
   (default 20).
4. For each batch, run `python3 spawn_batch.py batches/batch-NN.jsonl output/` and
   wait for it to finish before starting the next. Already-completed records are
   skipped automatically (matched by content hash against existing
   `output/*/metadata.json` files), so re-running this later against refreshed or
   additional data only processes what's new.
5. Report records found, batches run, and how many `output/<hash6>-<slug>/`
   subfolders got created — flag any batch that came up short of its input count.

See `README.md` for how the pieces fit, `DESIGN_DOC.md` for the language itself, and
`tasks/discovery.md` for what the default task actually asks each subagent to do.
