# runs/

Output directory, populated at runtime — empty at seed. Not hand-edited.

- `kpi_history.jsonl` — one JSON line per **attempt** (a sprint may have several):
  `{sprint, attempt, changes: [{op, construct_name, change_type}], decision, hygiene,
  kpi_assessment: {coverage|expressivity|determinism|interpretability|improvement: {impact,
  reasoning}}, simulations: [{item_id, source, nl, braincode, coverage, notes}], cross_check,
  required_changes, logic_issues, critic_reasoning}` — written by
  `braincode_loop/decision.py::append_history`. This is the raw data behind the entries in
  `../docs/changelog.md`, and the feed for later trend analysis once the loop runs at swarm scale.
- `budget_log.json` — every LLM call made during the run (role, provider, model, tokens, cost)
  plus a final summary, written at the end of `orchestrator.py::Orchestrator.run()`. Roles seen
  here: `searcher`, `shaper`, `critic`, `documenter`, and `cross_check_translator` (the
  independent translations fed to the Critic as Determinism evidence). Overwritten every
  invocation — it's one run's own detail, not a running total.
- `total_spend.json` — cumulative real spend across every real invocation ever:
  `{"total_usd": <float>, "by_provider": {"anthropic": <float>, "openai": <float>, "gemini": <float>},
  "runs": [{"timestamp", "spent_usd", "by_provider"}, ...]}`. `runs` is **append-only,
  oldest-to-newest** — new entries are pushed to the end. Unlike `budget_log.json` this is never
  overwritten, only added to (`budget.py::add_to_total_spent`), and only for real runs — a
  `--dry-run` never touches it, since its costs are fabricated from text length, not real money.
  `Orchestrator.run()` logs a multi-line "Budget burndown" block both before starting (the total +
  per-provider breakdown + the last 10 runs, so it never grows unbounded even though the file
  keeps full history) and after finishing (the updated figures). `--reset` intentionally does
  **not** remove this file — it tracks real money spent on the project, not per-attempt content,
  so restarting Sprint 0 shouldn't erase it.
- `logs/run_<timestamp>/` — one **folder** per invocation (never overwritten), containing:
  - `orchestration.log` — the console/orchestration log for whatever `run.py` printed that run:
    simulation-pool stats, per-attempt decision/hygiene/cost summaries, and
    JSON-parse-retry/malformed-attempt warnings/errors, all at INFO or above. `--verbose` only
    raises the detail level of the loop's own log lines — it does not enable the underlying
    HTTP/SDK libraries' debug output (`run.py::_configure_logging` pins `httpx`, `httpcore`,
    `anthropic`, `openai`, and `google_genai` to WARNING regardless), so the file stays scannable
    even in verbose mode.
  - `transcript.log` — every role's **full** system+user prompt and full raw response, one clearly
    delimited block per LLM call (searcher, shaper, critic, documenter, cross_check_translator),
    plus an end-of-attempt "ITERATION SUMMARY" block (decision, hygiene, full untruncated critic
    reasoning, required changes, pre-KPI assessment, cost). Answers "what did the agents actually
    say to each other" — previously not persisted anywhere. Written by
    `braincode_loop/transcript.py::TranscriptLogger`, wired through every role's `BaseRole.call()`
    and `simulation.py::cross_translate`. Not truncated or compressed by design (that would defeat
    the purpose) — can grow large on a long run since the full spec/glossary/critique JSON is
    re-sent every attempt; an accepted tradeoff, same as any other log.

  Both files are written by `run.py::_configure_logging`/`Orchestrator.__init__(log_dir=...)`; skip
  the whole folder with `--no-log-file`. `*.log` is gitignored at the repo root, so these never get
  committed.

Note: the *documentation* a run actually produces (`../docs/language-spec.md`, `glossary.md`,
`backlog.md`, `changelog.md`) isn't archived under `runs/` — it's snapshotted into
`../braincode_loop/seed_docs/runs/<run_id>/` at the end of every run (same `run_id` as this
folder's own `run_<run_id>`), by `braincode_loop/reset.py::snapshot_docs`. That way a run's
produced docs survive a later `--reset` or a later run overwriting `../docs/` further — see
`braincode_loop/seed_docs/README.md` for details.

`python run.py --reset` removes `kpi_history.jsonl`/`budget_log.json` (and restores `../docs/` to
seed) so a fresh run starts from Sprint 0 — it does not touch `logs/`, since those are a plain
history of past invocations, not per-run state; each run's own folder means re-running never
requires resetting or losing previous logs. `python run.py --dry-run --max-iterations 2`
regenerates the runtime files offline at $0.
