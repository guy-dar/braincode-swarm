# docs/

The living BrainCode syntax documentation — treated like a programming-language reference doc
("think of language documentation like coding language documentation nowadays," per the Aug 17
meeting notes), kept in a form both humans and LLM agents can work with efficiently.

| File | Owner role | Updated |
|---|---|---|
| [`language-spec.md`](language-spec.md) | Documenter | Sprint 0 (Foundations + initial basis), then every accepted attempt — sections are added (`op: add`) or rewritten in place (`op: revise`) |
| [`glossary.md`](glossary.md) | Documenter (drafted by Shaper) | Same cadence as the spec — no construct ships without a glossary entry |
| [`backlog.md`](backlog.md) | Documenter | Every attempt including Sprint 0: one row per change |
| [`changelog.md`](changelog.md) | Documenter | Every attempt including Sprint 0 (append-only) |

## Why these four files

- **`language-spec.md`** is the single source of truth for what BrainCode *is* right now. It
  carries the semantic version and is what the Critic (and the cross-provider translators) are
  handed when simulating the language on sampled tasks.
- **`glossary.md`** exists because Interpretability is a first-class pre-KPI and because the
  scripted doc-hygiene check (`braincode_loop/doc_hygiene.py`) refuses any change without a gloss
  and worked example — before the Critic even reads it. A construct with no glossary entry is a
  failed attempt, not a documentation TODO.
- **`backlog.md`** is what makes the workflow Agile rather than a single long debate: every change
  in every attempt gets a row with a status (`accepted` / `needs-rework` / `rejected`), so work
  happens in small, inspectable increments.
- **`changelog.md`** gives every attempt a paper trail: which sprint and attempt, which model
  proposed which set of changes, the Critic's decision and per-pre-KPI benefit/harm judgment, the
  **simulated examples** (sampled dataset items rendered in BrainCode, with Full/Partial/Fail
  coverage), whether cross-provider translations were used, the required changes, and the cost.
  This is the record that answers "what did this specific syntax change actually contribute?"

## Sprint 0 (bootstrap)

Before any of the above gets filled in incrementally, one setup sprint establishes a starting
point: the Searcher gathers structural notes on a handful of reference languages (default:
Python, HTML, English — `config.yaml -> run.bootstrap.inspiration_languages`) plus
formal-language-theory foundations, the Shaper proposes an entire initial basis (several
constructs at once), the Critic simulates it holistically on sampled items, and the Documenter
fills in `language-spec.md`'s **Foundations** section and every construct in one pass, bumping
the version straight to `1.0.0`. It runs automatically the first time the loop sees an empty
`language-spec.md`, retries up to `run.bootstrap.max_attempts` times with the Critic's required
changes fed back to the Shaper, and is skipped on every run after that (see
`braincode_loop/state.py::LanguageState.is_bootstrapped`). See the top-level `../README.md`.

## Versioning

`language-spec.md` carries a semantic version (`MAJOR.MINOR.PATCH`). Each change in a proposal
declares its own type; an accepted attempt bumps the version **once**, by the strongest type in
the set (`LanguageState.bump_version_for`):

- **MAJOR** — Sprint 0 establishing the base syntax, or a later change that breaks/redefines an
  existing construct's meaning.
- **MINOR** — a new construct/operator added, existing ones untouched.
- **PATCH** — documentation/glossary clarification, no semantic change.

## On statistics

No decision recorded here is gated on a statistical test, a sample size, or a threshold. The
Critic's critical judgment of the five pre-KPIs — informed by simulating the proposal on
randomly sampled dataset items — *is* the decision; doc hygiene is the only override. The full
statistical protocols in `../../instructions/kpi-examination-plan.md` are for a later,
larger-scale stage.

## Resetting

`python ../run.py --reset` restores all four files from `braincode_loop/seed_docs/` and clears
`../runs/`. Hand-edit the seed copies, not these, if the templates need to change.
