# BrainCode syntax-loop

The small-group agentic loop that creates and evolves BrainCode's syntax — the "small group of
diverse agents for syntax and basic vocabulary" stage described in the team's Aug 16-17, 2026
meeting notes (`../instructions/`), as distinct from the later Gemini-swarm vocabulary-enrichment
stage that this loop's output feeds into but does not itself implement.

Run it with `python run.py --dry-run` first (see [Running it](#running-it)) — that exercises the
entire pipeline with $0 cost and no API keys.

## What this loop does

BrainCode aims to turn human-agent communication into a formal syntax: expressive, broad-coverage,
deterministic, and interpretable (see `../instructions/Project Proposal.pdf`). This loop runs the
**small-group debate** half of that project — four roles, each backed by a specific model
provider, first establishing an initial syntax basis in a one-off Sprint 0 (bootstrap), then
evolving the language as a sequence of Agile sprints, each carrying a **set of changes**.

There is no scripted KPI battery and no statistical gate in this loop. Every attempt, a single
**Critic** role reads the proposal, **simulates** it on randomly sampled real tasks (Mind2Web web
trajectories, ALFRED household instructions, SWE-bench GitHub issue/patch reports, seed tasks),
and judges whether the changes
**benefit or harm each of the five pre-KPIs** — Coverage, Expressivity, Determinism,
Interpretability, Improvement — and what would have to change to maximize benefit. Its simulated
examples are written into the changelog so every decision is inspectable. The full statistical
protocols in `../instructions/kpi-examination-plan.md` remain the reference for a later,
larger-scale stage.

## Roles and models

From `../instructions/NLP Project Discussion.docx` (Aug 16 meeting notes), with one deliberate
change: the notes' **Reviewer** (OpenAI, adversarial logic/expressivity check) and **Examiner**
(Claude/script, KPI scoring) are merged into one **Critic** — the two jobs were producing verdicts
nobody reconciled, and the KPI scripts at n=1 per sprint never told anyone anything the reviewer
didn't already see.

| Role | Model | Job | Code |
|---|---|---|---|
| Documenter & document design | Claude | Records the debate, maintains the living language-spec doc — including initializing it at Sprint 0 | `braincode_loop/roles/documenter.py` |
| Searcher | Gemini | Retrieves external concepts, precedents, benchmarks, examples — at Sprint 0, documentation on the bootstrap's inspiration languages | `braincode_loop/roles/searcher.py` |
| Shaper | *(unassigned in the notes — see below)* | Composes/revises language constructs, grounded in formal-language foundations + pre-KPIs — proposes the entire initial basis at Sprint 0, a set of `add`/`revise` changes every sprint after | `braincode_loop/roles/shaper.py` |
| Critic | OpenAI | Adversarial logic check **and** pre-KPI judgment in one: simulates the proposal on sampled dataset items, decides accept / needs-rework / reject, lists required changes | `braincode_loop/roles/critic.py`, `braincode_loop/prompts/critic_system.md` |

The Shaper is the one role the meeting notes leave without a fixed provider. This implementation
treats that as intentional: the Shaper **rotates across all three providers, one per sprint**
(`config.yaml -> roles.shaper.rotation`), so the language is composed by a genuinely diverse small
group rather than one model's idiosyncratic style — which also directly feeds the Determinism
pre-KPI. The Critic is pinned to OpenAI so a proposal is always judged by a provider other than
Claude (Documenter) and, two sprints out of three, other than the one that wrote it.

**The Searcher's sources, every sprint (including Sprint 0), come from one of two places**,
chosen randomly (`config.yaml -> roles.searcher.folder_probability`, default **70% folder / 30%
internet**): **folder** — ground only in `sources/previous_work.md`; **internet** — search live
via Gemini's native Google Search grounding (`braincode_loop/llm/gemini_client.py`). Anything
durable it finds is logged back into `sources/previous_work.md`'s auto-logged section.

## File I/O per role

Most `docs/*.md` reads happen at the orchestrator layer (it reads a file into a string and passes
that string into the role method). The only role that writes to the filesystem is the Documenter
(via `braincode_loop/state.py::LanguageState`), plus the Searcher for one specific case.

| Role | Prompt file(s) | Project files read | Project files written |
|---|---|---|---|
| Searcher | `searcher_system.md`, `searcher_bootstrap_system.md` | `sources/previous_work.md` (re-read fresh every sprint) | `sources/previous_work.md` — appends a discovered source in **internet** mode only |
| Shaper | `shaper_system.md`, `shaper_bootstrap_system.md` | `docs/language-spec.md`, `docs/glossary.md` (steady state; nothing at Sprint 0) | *(none — returns a proposal dict)* |
| Critic | `critic_system.md` (one file; a Sprint 0 section adds the holistic checks) | `docs/language-spec.md`, `docs/glossary.md`; sampled items from `braincode_loop/seed_tasks.json` and `datasets/samples/*.jsonl` (via `braincode_loop/simulation.py`) | *(none — returns an assessment dict; `braincode_loop/decision.py` writes `runs/kpi_history.jsonl`)* |
| Documenter | `documenter_system.md`, `documenter_bootstrap_system.md` | `docs/language-spec.md` (re-opened for regex edits: version, Foundations, Status) | `docs/language-spec.md`, `docs/glossary.md` (sections added or rewritten in place), `docs/backlog.md` (one row per change), `docs/changelog.md` (one entry per attempt) |

**Not a role, but does the rest of the I/O**: the `Orchestrator` reads `config/config.yaml`,
`.env`, the seed tasks and dataset samples (once, at start), runs the scripted doc-hygiene check
(`braincode_loop/doc_hygiene.py`), optionally requests cross-provider translations of the sampled
items (`simulation.cross_translate`, logged as role `cross_check_translator`), and writes
`runs/budget_log.json` at the end of the run.

## The Agile loop

### Sprint 0 (bootstrap)

One setup sprint runs automatically the first time the loop sees an empty
`docs/language-spec.md` (`LanguageState.is_bootstrapped`), and is skipped afterwards:

1. **Searcher** gathers structural notes on the inspiration languages (default: Python, HTML,
   English — `config.yaml -> run.bootstrap.inspiration_languages`) plus formal-language-theory
   foundations. Runs once per Sprint 0, not once per attempt.
2. **Shaper** proposes an entire initial **basis** — several constructs at once, every change
   `op: add`, `change_type: MAJOR` (`Shaper.propose_basis`).
3. **Doc hygiene** (script) checks every construct has a gloss and worked example.
4. **Simulation items** are sampled; cross-provider translations are requested if
   `evaluation.cross_check` says they'd mean something this attempt (see below).
5. **Critic** judges the basis holistically — cross-construct consistency, redundancy, the
   first-draft gap checklist (evaluation order, precedence, scoping, data flow, iteration…) —
   simulates every sampled item, assesses the five pre-KPIs, and decides.
6. **Documenter** writes the attempt to `docs/changelog.md` and `docs/backlog.md`; if accepted,
   fills `language-spec.md`'s Foundations, writes every construct, and bumps to **1.0.0**.

If the Critic sends the basis back, the loop retries within Sprint 0 (up to
`run.bootstrap.max_attempts`, default 3), feeding the Critic's `required_changes`, logic issues,
and failed simulations into the Shaper's next attempt. If no attempt is accepted the loop halts
before any steady-state sprint — inspect the changelog, adjust prompts/config, `--reset`, rerun.
Sprint 0 spends $ like any sprint but does **not** count against `budget.max_iterations`.

### Steady state (sprints 1..N)

1. **Searcher** samples one candidate task from the dev-domain pool and grounds it against
   `sources/previous_work.md`.
2. **Shaper** (this sprint's rotated provider) proposes a **set of changes** — one or more, each
   `op: add` (new construct), `op: revise` (rewrite an existing construct's definition under the
   same name), or `op: remove` (delete an existing construct). Several related changes in one
   sprint are expected, not exceptional.
3. **Doc hygiene** (script) — the only hard, non-LLM requirement.
4. **Simulation items** (`evaluation.simulation.items_per_sprint`, default 4) are sampled
   round-robin from `seed_tasks`, `mind2web`, `alfred` with a seeded RNG. If
   `evaluation.cross_check.mode` is `auto`, independent translations of those items by the two
   non-Critic providers are requested as Determinism evidence — *unless* they'd be meaningless this
   attempt (spec empty and fewer than two constructs proposed; every change is PATCH-only; budget
   too low), in which case the Critic is told to simulate Determinism itself.
5. **Critic** breaks the changes (ambiguity, underspecification, overlap with the spec, example vs.
   semantics, gloss over-claiming), renders every sampled item in BrainCode, judges each pre-KPI
   `benefit / harm / neutral / mixed`, lists `required_changes`, and decides.
6. **Decision** = the Critic's decision, unless doc hygiene failed (`braincode_loop/decision.py`).
7. **Documenter** records the attempt; if accepted, applies every change to the spec and glossary
   (adding or rewriting sections in place) and bumps the version once, by the strongest
   `change_type` in the set.

A `needs-rework` attempt is retried within the same sprint (`run.sprint.max_attempts`, default 2)
with the Critic's critique fed to the Shaper; `rejected` ends the sprint. Attempts don't count
as iterations, but each costs about as much as a full sprint. The loop stops when
`budget.max_budget_usd` (default **$20**) or `budget.max_iterations` (default **25** sprints) is
hit — both are checked before every LLM call.

### Starting from products + steering notes

Instead of bootstrapping from scratch, a run can start from an existing product and be steered by
the project lead's **fundamental notes**:

```bash
python run.py --from          # reset, import the latest product from run.baseline_dir, exit
# write your notes in steering/notes.md, then:
python run.py --max-budget 5 --max-iterations 3
```

- **`--from [DIR]`** (`reset.py::import_baseline`) resets the workspace and imports a product.
  - **Where it imports from:** DIR defaults to `config.yaml -> run.baseline_dir`, which is
    `../syntax-loop-favourite-products`. DIR may hold `language-spec.md` + `glossary.md` directly,
    or versioned subfolders (`v1/`, `v2/`, …); with subfolders, the highest complete version is
    used. Pass a specific folder (e.g. `--from ../syntax-loop-favourite-products/v1`) to pin one.
  - **The product folder is read-only.** The files are copied into `docs/`, and the loop never
    writes to the product folder.
  - **After importing**, it starts a fresh changelog with a single *Baseline* entry. Because the
    spec already has constructs, Sprint 0 is skipped. Sprint numbering continues after the highest
    sprint stamped in the imported spec (`LanguageState.last_sprint_number`).
- **Nothing is deleted.** `--reset` and `--from` first *move* everything they displace into
  `runs/archive/reset_<timestamp>/`:
  - the previous `docs/` files and `docs/notes-status.json`;
  - `runs/kpi_history.jsonl` and `runs/budget_log.json`;
  - the auto-logged source rows.

  `runs/logs/` is never touched. Every run also keeps its own `budget_log.json` in its
  `runs/logs/run_<timestamp>/` folder, so the next run's `runs/budget_log.json` (latest run only)
  doesn't erase it.
- **Glossary vocabulary**: besides constructs, a change may be `kind: "vocabulary"`: one category of
  the descriptive lexicon. Examples are actions, objects, an attribute's allowed values
  (`tone-value`), or a literal form (person names, dates).
  - It is written only to a *Vocabulary* section at the end of `glossary.md`, never to the spec.
  - Each entry has a gloss, whether its member list is exhaustive (`closed`), members with glosses
    and natural-language synonyms, a membership rule for open categories, and a worked example.
- **Precedence**: notes override the prompts' built-in defaults. For example, the default that an
  open conversational item's content may stay as prose no longer applies once a note forbids
  natural language inside expressions.
- **`steering/notes.md`** is yours; the loop only reads it. Each note is a heading like
  `## N1 [hard] …` or `## N2 [direction] …`, optionally with explanation lines underneath.
  - `hard` notes are constraints. An accept that the Critic itself reports as violating one is
    downgraded to needs-rework, and force-accept never overrides it.
  - `direction` notes are goals. The Shaper may contest one with evidence, and the Critic rules on
    the contest.
  - Every role sees all the notes in every sprint.
  - Per-note status (`open / resolved / declined / stalled`) lives in `docs/notes-status.json`.
    Editing a note's text reopens it.
- **Steering sprints**: while any note is open, each sprint focuses on the next open note (hard
  notes first) instead of a seed task.
  - The Searcher grounds the note.
  - The Shaper revises the existing language to realize it. `op: remove` deletes a construct;
    merging two constructs is a revise plus a remove.
  - The Critic simulates the sampled items for regressions and fills in `notes_assessment`.
  - A note is `resolved` when an accepted attempt satisfies it, and `declined` when an accepted
    contest of a direction note stands. After `run.steering.max_sprints_per_note` sprints without
    either, it is `stalled`.
  - Once every note is settled the loop goes back to seed-task sprints
    (`run.steering.fallback_to_tasks`).
- **Rebuttals**: on any rework, the Shaper may answer a required change with a `rebuttal` instead
  of making it. The Critic rules `upheld` (the change is dropped) or `overruled`, and the rulings
  go into the changelog.
- **Competing positions**: with `run.steering.positions: 3`, attempt 1 of a steering sprint gets
  one proposal from each provider. The Critic picks one (`chosen_position`) and later reworks
  continue with that provider. This costs two extra Shaper calls per steering sprint, and the
  cross-check is skipped for that attempt.

## Pre-KPI assessment: critical judgment, not statistics

`../instructions/kpi-examination-plan.md` specifies powered statistical protocols (n=100-200,
McNemar / Fleiss' kappa / mixed-effects models) for each KPI. Running those after every attempt
would be statistically meaningless at this scale and prohibitively expensive, and the previous
scripted n=1 "lightweight KPI" checks turned out to add nothing the reviewer couldn't see.

So this loop asks one LLM to do what a careful language designer would: **look at the actual
changes, try them on real tasks, and reason about each goal.** For every attempt the Critic must
produce, and the Documenter must record:

| Pre-KPI | What the Critic judges |
|---|---|
| Coverage | Do the sampled items (web, household, chat — including domains the language wasn't built on) express in full, or does something fall back to prose? |
| Expressivity | Does the BrainCode rendering preserve recipient, register, conditions, ordering, quantities, branches? |
| Determinism | Would independent translators converge? (Compared directly when cross-provider translations are available; reasoned about otherwise.) |
| Interpretability | Can a reader with only the glossary recover intent; do the changes keep the grammar small and unambiguous? |
| Improvement | Would a weaker model act better from this expression than from the raw request? |

Each judgment is `benefit / harm / neutral / mixed` with reasoning; the **simulated examples**
(item, source, NL, BrainCode rendering, Full/Partial/Fail) are written verbatim to
`docs/changelog.md` and `runs/kpi_history.jsonl`. The only scripted check is doc hygiene.
There is no `significance_alpha`, no threshold, and no p-value anywhere in the loop.

## Repository layout

```
syntax-loop/
├── README.md                    <- this file
├── run.py                       <- CLI entrypoint (--dry-run, --reset, --max-budget, --max-iterations)
├── requirements.txt
├── env.example.txt              <- copy to .env and fill in API keys (not needed for --dry-run)
│
├── config/
│   └── config.yaml               <- role->model assignments, Sprint 0 + rework attempt caps, budget caps,
│                                     evaluation.simulation / evaluation.cross_check, pricing table
│
├── braincode_loop/                <- all Python source
│   ├── orchestrator.py            <- the sprint loop (run, run_bootstrap_sprint, run_sprint, _run_attempt)
│   ├── state.py                   <- LanguageState: docs/*.md reads/writes (upsert sections), task pool, version
│   ├── simulation.py              <- sample items for the Critic; cross-provider translations; auto skip rule
│   ├── doc_hygiene.py             <- the one scripted hard requirement (gloss + worked example per change)
│   ├── decision.py                <- hygiene + Critic decision -> accepted/needs-rework/rejected; kpi_history writer
│   ├── reset.py                   <- restore docs/ from seed_docs/, clear runs/
│   ├── budget.py                  <- BudgetTracker: the $/iteration guardrails
│   ├── utils.py                   <- JSON extraction, canonicalization
│   ├── seed_tasks.json            <- hand-picked dev/held-out candidate tasks (also simulation items)
│   ├── seed_docs/                 <- pristine docs/*.md templates used by --reset
│   │
│   ├── llm/                       <- provider-agnostic LLM client layer
│   │   ├── base.py, anthropic_client.py, openai_client.py, gemini_client.py
│   │   ├── dry_run_client.py      <- canned offline responses for --dry-run (all roles + translator)
│   │   └── pricing.py
│   │
│   ├── roles/                     <- the four roles, each a thin wrapper over an LLM call
│   │   ├── base_role.py           <- shared call() helper: budget check -> LLM call -> cost record -> JSON parse
│   │   ├── searcher.py            <- ground_candidate + ground_basis (Sprint 0)
│   │   ├── shaper.py              <- propose (set of changes) + propose_basis (Sprint 0); rework block
│   │   ├── critic.py              <- assess (steady state and Sprint 0)
│   │   └── documenter.py          <- record_sprint + initialize_documentation (Sprint 0)
│   │
│   └── prompts/                   <- one system-prompt .md per role
│
├── scripts/
│   └── fetch_dataset_samples.py   <- pulls real Mind2Web + ALFRED + SWE-bench_Verified samples into datasets/samples/*.jsonl
│
├── datasets/                      <- pointers to external trajectory datasets + local samples
│   ├── README.md                  <- 9 datasets incl. Mind2Web, ALFRED, SWE-bench_Verified; sample format
│   └── samples/                   <- *.seed.jsonl (committed, illustrative) / *.jsonl (fetched, real)
│
├── docs/                          <- syntax documentation (the "developed file system" for BrainCode itself)
│   ├── README.md
│   ├── language-spec.md           <- living spec, semver-versioned, one section per construct
│   ├── glossary.md                <- one gloss + worked example per construct
│   ├── backlog.md                 <- Agile backlog: one row per change per attempt
│   └── changelog.md               <- append-only attempt-by-attempt audit trail incl. simulated examples
│
├── sources/                       <- inspiration / prior-work folder (Searcher's folder mode)
│   ├── README.md
│   └── previous_work.md
│
├── runs/                          <- runtime output (empty at seed)
│   ├── README.md
│   ├── kpi_history.jsonl          <- generated: one JSON line per attempt (Critic assessment + simulations)
│   ├── budget_log.json            <- generated: full LLM call log + cost summary
│   └── logs/run_<timestamp>.log   <- generated: one console-log file per invocation (gitignored via *.log)
│
└── tests/                         <- pytest; includes an offline end-to-end dry-run smoke test
```

## Running it

```bash
cd syntax-loop
python -m pip install -r requirements.txt   # LLM SDKs only needed for real runs; datasets/py7zr only for the fetch script

# Smoke-test the whole pipeline offline, $0 cost, no API keys required:
python run.py --dry-run --max-iterations 2

# Start clean (restores docs/ from braincode_loop/seed_docs/, clears runs/):
python run.py --reset

# Optional: replace the illustrative dataset samples with real Mind2Web / ALFRED / SWE-bench items:
python scripts/fetch_dataset_samples.py --n 100

# Real run, using API keys from .env (copy env.example.txt -> .env first):
python run.py

# Override the guardrails for a given run without editing config.yaml:
python run.py --max-budget 5 --max-iterations 10

# Every invocation also writes its console log to runs/logs/run_<timestamp>.log (gitignored);
# skip that if you don't want it:
python run.py --no-log-file

# Tests:
python -m pytest tests -q
```

`config.yaml` is the single place to change role->model assignments, the Shaper's rotation, how
many simulation items the Critic sees, the cross-check policy, attempt caps, budget caps, and the
pricing table.

## What's deliberately out of scope here

- **The Gemini-swarm vocabulary-enrichment stage** — this repo only implements the small
  diverse-role debate; `runs/kpi_history.jsonl` and `docs/` are the handoff artifacts.
- **The full KPI statistical protocols** — `../instructions/kpi-examination-plan.md` remains the
  reference for the powered version, run at milestones once there's a stable language to test.
- **Bulk dataset ingestion** — `scripts/fetch_dataset_samples.py` pulls small random samples;
  nothing downloads a full dataset.
