# datasets/

Pointers to external datasets of human↔LLM trajectories and sessions, plus the small real samples
the Critic actually simulates on. Two classes, matching `config.yaml -> evaluation.simulation`:

1. **Closed class** — structured, single-outcome tasks with a defined action sequence or fix
   (web-agent trajectories, household-robot instructions, GitHub issue → patch pairs, plus the
   hand-curated dev/heldout task pool). This is what BrainCode was originally built to formalize.
2. **Open class** — free-form human↔LLM conversations, including per-turn or end-of-conversation
   human feedback. Added later for the same reason SWE-bench was added to the closed class: more
   linguistic/structural diversity (branching, correction, negotiation, revision) than closed-class
   trajectories exhibit on their own.

None of the full datasets ship in the repo — these are pointers/download instructions, not
vendored copies. Every fetchable dataset below (everything except `seed_tasks`) is sampled into
`samples/` (see [Local samples](#local-samples-what-the-critic-simulates-on)) and, together with
`braincode_loop/seed_tasks.json`, is what the Critic draws from every attempt to simulate the
proposed syntax on real tasks and conversations.

## Closed class

| Dataset | Size | Link | Notes |
|---|---|---|---|
| **seed_tasks** | 9 hand-curated items (dev + heldout domains) | `braincode_loop/seed_tasks.json` | Not fetched by any script — hand-written and maintained directly. Also the source of the Shaper's candidate tasks each sprint (dev domains only); the Critic's simulation pool draws from both splits. |
| **Mind2Web** | 2,000+ tasks, 137 websites, 31 domains, crowdsourced action sequences (public `train` split: 1,009) | https://github.com/OSU-NLP-Group/Mind2Web (mirror: `osunlp/Mind2Web` on Hugging Face; fields `confirmed_task`, `action_reprs`, `domain`, `subdomain`, `website`) | Real-world (not simulated) web-agent action trajectories. **Sampled into `samples/mind2web.jsonl`.** CC BY 4.0. Public train split spans only 3 domains (Travel/Shopping/Entertainment) — Mind2Web's other ~28 domains live in restricted-access test splits, a real dataset limit, not something better sampling can fix. |
| **ALFRED** | 8k+ expert household-robot demonstrations × 3 language annotations each (goal `task_desc` + step-by-step `high_descs`), 7 task types | https://github.com/askforalfred/alfred — trajectory-only lite JSON: https://ai2-vision-alfred.s3-us-west-2.amazonaws.com/json_2.1.0.7z (~35 MB) | Embodied, grounded instructions with explicit sub-goal decomposition. **Sampled into `samples/alfred.jsonl`.** |
| **SWE-bench_Verified** | 500 human-validated GitHub issue → patch pairs across 12 popular Python repos (Django, sympy, scikit-learn, ...) — this is its full size, no more rows exist | https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified (fields `problem_statement`, `patch`, `test_patch`, `hints_text`, `difficulty`) | Chosen specifically for structural/linguistic diversity over Mind2Web/ALFRED's mostly-linear action sequences: `problem_statement` hits conditional language 69% of the time and negation 67% (vs. Mind2Web's 2.3%/1.7%) — bug reports are inherently "expected X, got Y" narratives. **Sampled into `samples/swebench.jsonl`**, capped at 500 (its real maximum) even when other datasets sample 1000 — kept on **Verified** rather than the larger, non-human-validated full `princeton-nlp/SWE-bench` (2,294 test rows) specifically to keep the human-validation guarantee. MIT-licensed. |

## Open class

| Dataset | Size | Link | Notes |
|---|---|---|---|
| **PRISM** | 8,011 full conversations (`conversations` config; a flat `utterances` config also exists, 68,371 rows — see below) | https://huggingface.co/datasets/HannahRoseKirk/prism-alignment (not gated) | Real human↔LLM alignment conversations with per-turn model/score metadata and free-text `open_feedback`. **One row is already a full conversation including feedback**, not a single message. `conversation_history` is a nested `list<struct>` column — see [Local samples](#local-samples-what-the-critic-simulates-on) for the timing caveat and the flat-config fallback. **Sampled into `samples/prism.jsonl`.** |
| **PATHs (annotated WildChat)** | 32,697 full conversations (`wildchat1m_en3u-task_utterance_wintent_anns` config — the richest of its 3 configs) | https://huggingface.co/datasets/microsoft/prototypical-hai-collaborations (not gated, ODC-BY) | GPT-4o-annotated real WildChat conversations (`microsoft/prototypical-hai-collaborations`, from *Prototypical Human-AI Collaboration Behaviors from LLM-Assisted Writing in the Wild*, https://arxiv.org/abs/2505.16023) — task/utterance-type/writing-intent labels. **Annotations are LLM-generated, human-validated only on a subset — not human ground truth**, unlike this table's other feedback sources. One row is already a full conversation. **Sampled into `samples/paths.jsonl`.** |
| **ThoughtTrace** | 2,155 full conversations — this is its full size, no more rows exist | https://huggingface.co/datasets/SCAI-JHU/ThoughtTrace (not gated, CC-BY-4.0; paper https://arxiv.org/abs/2605.20087) | Human↔LLM reasoning-trace conversations with per-message human `reasons`/`reactions` feedback. One row is already a full conversation; `messages` is a `list<string>` of JSON-*encoded* message objects (decoded in Python, not a typed struct). **Sampled into `samples/thoughttrace.jsonl`**, naturally capped at 2,155 items even at a 1000-per-dataset target — not an error, just this dataset's real ceiling. |

## Other candidates considered (not currently fetched)

Datasets from earlier research that remain plausible future additions but aren't wired into
`scripts/fetch_dataset_samples.py` today:

| Dataset | Size | Link | Notes |
|---|---|---|---|
| **LMSYS-Chat-1M** | 1M conversations, 25 models, 210K IPs, 154 languages | https://huggingface.co/datasets/lmsys/lmsys-chat-1m | Real Chatbot Arena / Vicuna-demo traffic. The same/similar prompts were sent to many different models, so it doubles as a natural cross-model comparison corpus. |
| **WildChat-1M** | ~1M conversations (GPT-3.5/GPT-4) | https://huggingface.co/datasets/allenai/WildChat-1M | **Tested and rejected** as a closed-class candidate: 536s to fetch just 159 rows — its `conversation` field is a nested `STRUCT[]` that Parquet can't column-prune as cheaply as a flat column — and the content itself was mostly non-task chat rather than agent-style requests. (PATHs, above, is an annotated derivative of this same underlying data and is fetched instead.) |
| **Chatbot Arena Conversations** | Large-scale human-preference conversation pairs | https://huggingface.co/datasets/lmsys/chatbot_arena_conversations | Paired human-preference judgments over conversations. |
| **OpenAssistant Conversations (OASST2)** | ~135K messages in conversation trees | https://huggingface.co/datasets/OpenAssistant/oasst2 | **Tested and rejected**: 195s for 45 rows, and lower phenomena rates than hoped for despite its tree structure. |
| **AgentInstruct** | 1,866 trajectories across 6 task families (ALFWorld, WebShop, Mind2Web, Knowledge Graph, Operating System, Database) | https://huggingface.co/datasets/zai-org/AgentInstruct | Multi-domain agent trajectories already split by task family. |
| **ToolBench** | 16,464 real RapidAPI APIs, ~49,831 train / 9,965 test tool-call trajectories (DFSDT search) | https://github.com/OpenBMB/ToolBench (dataset: `OpenBMB/ToolBench`) | **Gated on Hugging Face (needs manual access approval)** — not fetchable by `scripts/fetch_dataset_samples.py` as-is. |

Check its Parquet schema is flat (`DESCRIBE read_parquet(...)`) before assuming a new source will
be cheap to sample from — see the WildChat-1M rejection above.

## Local samples (what the Critic simulates on)

`samples/` holds small JSONL samples with a shared shape — `id`, `nl` (the natural-language task or
opening prompt), `steps` (trajectory steps or subsequent conversation turns/feedback, if any),
`source`, plus `domain`/`task_type`:

| File | Contents | Committed? |
|---|---|---|
| `samples/{mind2web,alfred,swebench,prism,paths,thoughttrace}.seed.jsonl` | 10 illustrative items each, hand-written in the dataset's style and labeled `illustrative — …` | yes — the offline fallback so `--dry-run` and keyless runs work |
| `samples/mind2web.jsonl` | real reservoir sample (default 1000, capped by the 1,009-row public train split) drawn via `duckdb` querying Hugging Face's auto-generated Parquet conversion, projecting only the lightweight text columns (the `actions` column, embedded page HTML, is never fetched) | no — generated by `python scripts/fetch_dataset_samples.py --n 1000` (needs network + `duckdb` + `py7zr`, see `requirements.txt`) |
| `samples/alfred.jsonl` | real random sample (default 1000) from the ALFRED lite JSON archive | no — same command as above |
| `samples/swebench.jsonl` | real reservoir sample, **capped at 500** (SWE-bench_Verified's actual maximum, regardless of `--n`) — `steps` is a lightweight file-list extracted from the `patch` diff header, not the diff body itself | no — same command as above |
| `samples/prism.jsonl` | real reservoir sample (default 1000, capped by the 8,011-row `conversations` config) — `steps` includes per-turn model/score plus a trailing `open_feedback` line when present | no — same command as above. `fetch_prism()` times itself (nested-struct column, see the Open class table above); `fetch_prism_flat()` is a documented, not-yet-adopted-by-default fallback via the flat `utterances` config if the primary path proves too slow at scale |
| `samples/paths.jsonl` | real reservoir sample (default 1000, capped by the 32,697-row config) — `steps` includes the `coarse_tasks`/`writing_intents` annotations appended as a trailing note | no — same command as above |
| `samples/thoughttrace.jsonl` | real reservoir sample, **capped at 2,155** (its actual maximum, regardless of `--n`) — `steps` includes inline `reasons`/`reactions` feedback | no — same command as above |

`braincode_loop/simulation.py` prefers the real `<name>.jsonl` when present and falls back to the
`.seed.jsonl` otherwise. Every attempt, the Critic draws `evaluation.simulation.items_per_dataset_closed`
items from each closed-class source and `items_per_dataset_open` from each open-class source (a
seeded RNG, `run.random_seed`, so a given config + seed reproduces the same items), weighting the
open class higher per-source since it's the newer, less-tested addition. The Critic must render
**every** sampled item in BrainCode, and those renderings are written to `docs/changelog.md` and
`runs/kpi_history.jsonl`.

Use `python scripts/show_dataset_samples.py --n 3` to print a few items from every dataset in both
classes (falling back to `.seed.jsonl` for anything not yet fetched) — the quickest way to
eyeball whether real data looks right before spending a real Critic run on it.

## Using these for the small-group loop

- **Sampling, not bulk-loading.** This loop runs on a bounded per-invocation budget and a handful
  of sprints — never point a role at a full dataset download. The fetch script streams every
  dataset and extracts only the sampled items.
- **Attribution.** All datasets above are third-party research releases — check each dataset's
  license/card on its Hugging Face page before redistributing any sampled subset outside this
  project. PATHs' annotations in particular are LLM-generated, not human ground truth — don't
  present them as such downstream.
- **Growing this list.** The Searcher role should keep adding to this file as it encounters new
  sources — append rows, don't replace this file wholesale. To make a new dataset available to the
  Critic's simulations: add a `fetch_<name>` to `scripts/fetch_dataset_samples.py` producing
  `samples/<name>.jsonl` in the shape above, add a `<name>.seed.jsonl` fallback, and list it under
  `evaluation.simulation.closed_sources` or `open_sources` in `config.yaml`.
