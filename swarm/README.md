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
`failures/` (any namespace), or an earlier batch; `spawn_batch.py` dispatches a
batch file. Run
them separately for a different filter, or to re-run an existing batch, which
retries just its failures:

```bash
python3 spawn_batch.py batches/batch-07.jsonl output/
```

Results land in `output/<namespace>/<hash6>-<slug>/`, one folder per
successful record, where `<namespace>` is `SWARM_EXPERIMENT` (or `default` if
unset) — every run gets its own namespace, so re-running the exact same batch
under a new tag re-translates every record instead of being skipped as
already-done. Anything that failed leaves its logs in
`failures/<namespace>/` instead, and re-running the same batch retries just
those.

## The loop: translator → migrator → inspector

`loop.py` turns batch translation into a loop that grows the glossary:

1. **Translators.** A batch of 30 containers runs in parallel, one item each (`translate_batch.py`, `tasks/translator.md`). Each translator reads `reference/language-spec.md` and the glossary retrieval for its item, then translates. If the glossary can't express the item, it fails with suggestions for glossary additions or refinements.
2. **Migrator** (`migrate.py`). Up to 5 pre-migrators on the translators' model merge the suggestion files in groups of up to 6. A stronger model (`MIGRATOR_MODEL`, default `gemini-flash-high`) consolidates the merged files into one suggestion file. Up to 5 drafters on the translators' model turn slices of it into draft glossary operations, using the host's RAG pre-search of existing entries. The strong model then reviews the drafts (approve / replace / drop / add). The host validates the assembled operations and installs them into the glossary and the RAG index. Every migration agent writes a live progress log with token usage under `migrations/batch-NNN/`.
3. **Inspector.** `inspector.py` counts the batch's add and refine suggestions in `translator_suggestions/suggestion_counts.csv`, and stops the loop early once a batch has at most 2 adds and at most 5 refines (provided at least 80% of its translators finished).

```bash
pip install -r requirements.txt
python loop.py plan                 # 500 train items per dataset (all if fewer) -> runs/plan.jsonl, batches of 30
python loop.py run                  # resumable; --max-batches N to stop after N batches
python loop.py status
```

- **Translator IDs** are `<batch_id>-<tnum_inside_batch>` (e.g. `7-23`).
- **Outputs:**
  - `translations/{successful,failed}/<dataset>/<tid>.md`
  - `translator_suggestions/<tid>.md`
  - `migrations/batch-NNN.md`
  - `reference/history/batch-NNN/` (the glossary before each migration)
- **Formats** are fixed in `doc_formats/`.

**Glossary.** `reference/glossary.jsonl` is the source of truth (`glossary/`), with compact records: only `symbol`, `kind`, `category`, `signature`, `definition`, `not`, `aliases` and `expansion` are authored; the host maintains ids, versions, rule links and dependencies. `glossary.md` (one table row per record) is rendered from it. It's both the view models read and the one people edit (then run `python -m glossary.import_md`). Who changed what is logged in `glossary-provenance.jsonl`.

**RAG.** `rag/` indexes glossary records only. Retrieval decomposes an item into source-linked needs, searches each need by exact name, keyword (BM25) and meaning (fastembed), reranks, and expands to dependencies and shared rules. Any model can use it: `python -m rag.cli …` on the host, `rag/server.py` over HTTP, `kit/rag.mjs` inside containers, and `kit/tool_schema.json` for function calling. See `kit/README.md`.

## Layout

- `loop.py` — the translator → migrator → inspector loop (above); `translate_batch.py`, `migrate.py`, `inspector.py` are its steps, each runnable alone; `loop_files.py` holds the shared file-naming contract.
- `glossary/` — glossary records: schema, validation, migration ops, rendering, import.
- `rag/` — glossary retrieval (index, needs, retrieve, server, client, cli); `kit/` — the same for models in containers.
- `doc_formats/` — the fixed formats of translations, suggestions and migration output.
- `run_batch.sh`, `spawn_batch.py`, `sample_batch.py` — the original one-shot path (sample + dispatch one batch, no glossary loop).
- `tasks/`, `harnesses/` — pluggable task/harness definitions.
- `reference/` — the language spec (`language-spec.md`), the glossary (`glossary.jsonl` + rendered views), `purpose.md`, `examples.jsonl`, and `history/`; mounted read-only into containers at `/reference`.
- `.env` / `.env.example` — config, auto-loaded.

See `ADVANCED.md` for config variables, output format, adding a task/harness,
security posture, running the tests, and running without Claude Code.
