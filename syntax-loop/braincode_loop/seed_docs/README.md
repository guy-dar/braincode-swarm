# braincode_loop/seed_docs/

Two unrelated things share this directory — read the distinction carefully before touching either.

## The pristine templates (`language-spec.md`, `glossary.md`, `backlog.md`, `changelog.md`)

These are hand-maintained source files, committed to the repo like any other code. `python run.py
--reset` (`braincode_loop/reset.py::reset_workspace`) copies them over `../../docs/` so a fresh
run starts from Sprint 0 against an empty spec. `language-spec.md` in particular must keep the
exact `**Version:** 0.1.0`, `**Status:** not yet bootstrapped …`, and `*(To be filled in …)*`
strings that `state.py` regexes depend on — don't edit those markers casually.

## `runs/` — generated per-run doc snapshots (not source, not committed)

`runs/run_<run_id>/` holds a copy of whatever `../../docs/{language-spec,glossary,backlog,
changelog}.md` looked like at the end of that run — written by
`braincode_loop/reset.py::snapshot_docs`, called from `orchestrator.py::Orchestrator.run()`'s
`finally` block (so it fires whether the run succeeded, failed, or was cut short by budget).
`run_id` matches the same identifier used for that run's `../../runs/logs/run_<run_id>/` folder,
so a run's logs and its produced documentation are correlated by name.

This exists because `docs/` is a single *live*, continuously-mutated working copy — every new
run's Documenter writes into it, and `--reset` wipes it back to the templates above. Without this
snapshot, an earlier run's actual output (what got bootstrapped, what the backlog/changelog said)
would be unrecoverable the moment a later run changed or reset it. `runs/` here is gitignored (see
the repo root `.gitignore`) — it's generated output living inside the source tree for convenience,
not part of the codebase.

Skipped entirely when a run uses `--no-log-file` (no `run_id` to key the snapshot by, consistent
with that flag turning off all per-run artifact writing).
