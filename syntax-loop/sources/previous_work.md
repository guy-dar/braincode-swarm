# Previous Work / Inspiration

Carried over from the `instructions/` meeting notes (Aug 16 & 17, 2026) and the project
proposal. This is the seed list the **Searcher** role should expand on — every entry here is a
starting point for retrieval, not a closed set. When the Searcher finds a new precedent worth
keeping, add a row here and note *why* it's relevant to BrainCode specifically (not just "this
is a cool paper").

## Iteration-0 baseline inspiration (Sprint 0 bootstrap)

BrainCode's initial syntax basis (Sprint 0 — see `../README.md` and `config/config.yaml ->
run.bootstrap`) draws structural inspiration from a handful of existing languages, not agentic
precedent papers. Configurable via `run.bootstrap.inspiration_languages`; defaults to:

| Language | Reference | What to borrow |
|---|---|---|
| Python | https://docs.python.org/3/reference/ | Concise, composable statements; small orthogonal core; avoids deep nesting. |
| HTML | https://html.spec.whatwg.org/ | Separating *content* from *context/attributes* (style, register) — the meeting notes' example of "email my mom vs. my professor" differing in attributes, not phrasing. |
| English | https://owl.purdue.edu/owl/general_writing/grammar/index.html | The natural language BrainCode must stay expressive relative to; closed-class function words (conditionals, negation, connectives) as a model for keeping the core grammar small. |
| Formal language theory (general) | https://en.wikipedia.org/wiki/Formal_language and https://en.wikipedia.org/wiki/Chomsky_hierarchy | Starting points only — Searcher should deepen these via folder/internet lookup at bootstrap time; aim for a context-free-ish, parseable core over an ambiguous context-sensitive one. |

## Language / agent structure precedents

| Name | Link | Relevance to BrainCode |
|---|---|---|
| ReAct | https://arxiv.org/abs/2210.03629 | Baseline agentic reasoning/acting loop structure — informs how BrainCode expressions should interleave reasoning steps and actions rather than being pure declarative syntax. |
| Parsel | https://arxiv.org/abs/2212.10561 | Closest prior art in spirit: a language for composing hierarchical decompositions that LLMs can implement. Direct comparison point for BrainCode's task-decomposition operators — read this first when the Shaper designs decomposition constructs. |
| Automatic Textbook Formalization | https://arxiv.org/abs/2604.03071 | **Named explicitly as inspiration in the project brief.** Formalizes informal textbook content into structured/verifiable representations — methodologically close to what BrainCode does (informal NL agent trajectories → structured, checkable syntax). Worth mining for: (a) how they validate that formalization preserves meaning (→ Expressivity KPI), (b) how they handle content that resists formalization (→ Coverage KPI failure modes). |
| Agent swarms and the new model economics | https://cursor.com/blog/agent-swarm-model-economics | Motivates the two-stage architecture: this repo (small diverse-role debate for syntax) feeds a *later* Gemini-swarm stage for vocabulary enrichment. Also informs budget/cost thinking for this loop's own budget cap. |
| Why Agentic Systems Need Ontologies | https://www.youtube.com/watch?v=Sir59K8ZDPU | Talk on why agent systems benefit from shared, structured ontologies rather than free-text — background argument for why BrainCode should exist at all; useful framing for the Documenter's spec introduction. |
| Shared Gemini conversation (more articles/ideas) | https://share.gemini.google/sdRC4AhpshiJ | Team's running scratchpad of candidate sources from the Aug 16 meeting. Not yet triaged into this table — Searcher should periodically re-check it for new links and promote anything durable into this file. |

## Benchmark suites referenced for Coverage / held-out testing

Pulled from `instructions/kpi-examination-plan.md` — use these as the source pool for dev vs.
held-out domain splits (see `docs/backlog.md` for which domains are currently "dev" vs. frozen
as "held-out" for the running language version).

- BIG-bench
- HELM
- AgentBench
- GAIA
- SWE-bench

## Vocabulary inspirations (from Aug 16 meeting notes)

These are candidate *sources of primitive vocabulary/operators*, not precedent papers. They
belong to the later Gemini-swarm vocabulary-enrichment stage, but the Shaper in this small-group
loop should keep them in mind when naming/grounding new syntax constructs so the two stages stay
compatible:

- **Emojis** — dense, universally recognized symbol set; candidate for compact operator glyphs.
- **English / other natural languages** — cross-lingual comparison to check constructs aren't
  overfit to English syntax or idiom.
- **Benchmarks of complex reasoning tasks** — source of the semantic content operators need to
  express (multi-step, conditional, causal reasoning).
- **Trajectories / human-AI sessions** — see `../datasets/README.md`. The single most important
  vocabulary source per the meeting notes; this is what the small-group loop should sample
  example tasks from.

## How to use this file

- The Searcher role reads this file at the start of every sprint. Each sprint, it randomly picks
  one of two modes (config.yaml -> roles.searcher.folder_probability, default 70/30):
  - **folder** (70%) — reason only over what's already in this file.
  - **internet** (30%) — search live (Gemini's Google Search grounding — see
    `braincode_loop/llm/gemini_client.py`) for precedent beyond what's catalogued here.
- The Shaper role should cite a row from this table (by name) in its proposal notes whenever a
  new construct is directly inspired by one of these precedents — this gets recorded in
  `docs/changelog.md` so the spec's provenance stays auditable.
- Do not delete rows. If a source turns out to be a dead end, add a one-line note explaining why
  instead of removing it — negative results are still useful to the next person.

## Sources found during sprints (auto-logged)

Populated automatically (`braincode_loop/state.py::LanguageState.append_discovered_source`) when
an internet-mode Searcher call finds something it judges durable enough to keep. Not hand-curated
— review periodically and promote anything that holds up into the curated tables above.

*(Empty at seed.)*
