# BrainCode Syntax Backlog

Agile product backlog for the syntax-creation loop. Each sprint pulls a candidate task, drives a
**set of changes** (one or more `add`/`revise` operations) through Shape → Critique → Document,
and records one row per change here. A sprint whose proposal comes back `needs-rework` is
retried within the same sprint (`config.yaml -> run.sprint.max_attempts`), so several rows can
carry the same sprint number with different attempt labels.

**Sprint 0** is a setup sprint, not a normal backlog item: it establishes the entire initial
syntax basis at once (several constructs, inspired by Python/HTML/English — see
`config/config.yaml -> run.bootstrap`). Its rows are tagged `Sprint 0`; it does not count against
`budget.max_iterations`.

## Status definitions

| Status | Meaning |
|---|---|
| `accepted` | Critic accepted the attempt and doc hygiene passed; merged into `language-spec.md` + `glossary.md`. |
| `needs-rework` | Critic sent the attempt back (or doc hygiene failed); its `required_changes` were fed into the next attempt of the same sprint. |
| `rejected` | Critic judged the changes fundamentally the wrong shape — sprint ends, kept here with the reason so it isn't re-proposed blindly. |

## Dev vs. held-out domains

The Shaper's candidate tasks come from `braincode_loop/seed_tasks.json`'s dev domains. The
Critic's simulation items are sampled from `seed_tasks` (both splits) plus `datasets/samples/`
(Mind2Web, ALFRED) — see `config.yaml -> evaluation.simulation`.

- **Dev domains:** email_assistant, web_navigation, code_task, embodied_task
- **Held-out domains (not used as candidate tasks; only appear in simulation):** trip_planning, customer_support

## Backlog

*(Empty at seed. The Documenter appends rows here every attempt — see
`braincode_loop/roles/documenter.py`.)*

| # | Item | Status | Sprint | Notes |
|---|---|---|---|---|
| 0 | `Lexical Primitives` | needs-rework | 0 | (attempt 1) add — The proposed basis has useful structural intent: explicit blocks, sequencing, bi |
| 0 | `Action` | needs-rework | 0 | (attempt 1) add — The proposed basis has useful structural intent: explicit blocks, sequencing, bi |
| 0 | `Sequence & Binding` | needs-rework | 0 | (attempt 1) add — The proposed basis has useful structural intent: explicit blocks, sequencing, bi |
| 0 | `Task` | needs-rework | 0 | (attempt 1) add — The proposed basis has useful structural intent: explicit blocks, sequencing, bi |
| 0 | `Condition` | needs-rework | 0 | (attempt 1) add — The proposed basis has useful structural intent: explicit blocks, sequencing, bi |
| 0 | `Iteration` | needs-rework | 0 | (attempt 1) add — The proposed basis has useful structural intent: explicit blocks, sequencing, bi |
| 0 | `Lexical Primitives` | needs-rework | 0 | (attempt 2) revise — This is a promising structural core: explicit sequential execution, scoped bindi |
| 0 | `Action` | needs-rework | 0 | (attempt 2) revise — This is a promising structural core: explicit sequential execution, scoped bindi |
| 0 | `Sequence & Binding` | needs-rework | 0 | (attempt 2) revise — This is a promising structural core: explicit sequential execution, scoped bindi |
| 0 | `Task` | needs-rework | 0 | (attempt 2) revise — This is a promising structural core: explicit sequential execution, scoped bindi |
| 0 | `Condition` | needs-rework | 0 | (attempt 2) revise — This is a promising structural core: explicit sequential execution, scoped bindi |
| 0 | `Iteration` | needs-rework | 0 | (attempt 2) revise — This is a promising structural core: explicit sequential execution, scoped bindi |
| 0 | `Action` | needs-rework | 0 | (attempt 1) add — This is a promising core: ordered Tasks, bindings, fixed-precedence conditions,  |
| 0 | `Task` | needs-rework | 0 | (attempt 1) add — This is a promising core: ordered Tasks, bindings, fixed-precedence conditions,  |
| 0 | `Condition` | needs-rework | 0 | (attempt 1) add — This is a promising core: ordered Tasks, bindings, fixed-precedence conditions,  |
| 0 | `Binding` | needs-rework | 0 | (attempt 1) add — This is a promising core: ordered Tasks, bindings, fixed-precedence conditions,  |
| 0 | `ForEach` | needs-rework | 0 | (attempt 1) add — This is a promising core: ordered Tasks, bindings, fixed-precedence conditions,  |
| 0 | `Document` | needs-rework | 0 | (attempt 2) add — This is a promising direction: explicit indentation, entry-point rules, ordered  |
| 0 | `Action` | needs-rework | 0 | (attempt 2) revise — This is a promising direction: explicit indentation, entry-point rules, ordered  |
| 0 | `Task` | needs-rework | 0 | (attempt 2) revise — This is a promising direction: explicit indentation, entry-point rules, ordered  |
| 0 | `Condition` | needs-rework | 0 | (attempt 2) revise — This is a promising direction: explicit indentation, entry-point rules, ordered  |
| 0 | `Binding` | needs-rework | 0 | (attempt 2) revise — This is a promising direction: explicit indentation, entry-point rules, ordered  |
| 0 | `TASK` | needs-rework | 0 | (attempt 1/3) add — This is a promising structural core, and its explicit sequencing, branch precede |
| 0 | `ACTION` | needs-rework | 0 | (attempt 1/3) add — This is a promising structural core, and its explicit sequencing, branch precede |
| 0 | `CHECK` | needs-rework | 0 | (attempt 1/3) add — This is a promising structural core, and its explicit sequencing, branch precede |
| 0 | `CONDITIONAL` | needs-rework | 0 | (attempt 1/3) add — This is a promising structural core, and its explicit sequencing, branch precede |
| 0 | `ITERATION` | needs-rework | 0 | (attempt 1/3) add — This is a promising structural core, and its explicit sequencing, branch precede |
| 0 | `MESSAGE` | needs-rework | 0 | (attempt 1/3) add — This is a promising structural core, and its explicit sequencing, branch precede |
| 0 | `TASK` | needs-rework | 0 | (attempt 2/3) revise — This is a promising structural basis: sequencing, strict boolean control flow, s |
| 0 | `ACTION` | needs-rework | 0 | (attempt 2/3) revise — This is a promising structural basis: sequencing, strict boolean control flow, s |
| 0 | `CHECK` | needs-rework | 0 | (attempt 2/3) revise — This is a promising structural basis: sequencing, strict boolean control flow, s |
| 0 | `CONDITIONAL` | needs-rework | 0 | (attempt 2/3) revise — This is a promising structural basis: sequencing, strict boolean control flow, s |
| 0 | `ITERATION` | needs-rework | 0 | (attempt 2/3) revise — This is a promising structural basis: sequencing, strict boolean control flow, s |
| 0 | `MESSAGE` | needs-rework | 0 | (attempt 2/3) revise — This is a promising structural basis: sequencing, strict boolean control flow, s |
| 0 | `TASK` | needs-rework | 0 | (attempt 3/3) revise — This bootstrap has promising foundations in its lexical rules, sequential execut |
| 0 | `ACTION` | needs-rework | 0 | (attempt 3/3) revise — This bootstrap has promising foundations in its lexical rules, sequential execut |
| 0 | `Task` | needs-rework | 0 | (attempt 1/3) add — This is a promising basis: the simulations show real gains for ordered closed ta |
| 0 | `Action` | needs-rework | 0 | (attempt 1/3) add — This is a promising basis: the simulations show real gains for ordered closed ta |
| 0 | `Check` | needs-rework | 0 | (attempt 1/3) add — This is a promising basis: the simulations show real gains for ordered closed ta |
| 0 | `Flow-If` | needs-rework | 0 | (attempt 1/3) add — This is a promising basis: the simulations show real gains for ordered closed ta |
| 0 | `Iterate` | needs-rework | 0 | (attempt 1/3) add — This is a promising basis: the simulations show real gains for ordered closed ta |
| 0 | `Bind` | needs-rework | 0 | (attempt 1/3) add — This is a promising basis: the simulations show real gains for ordered closed ta |
| 0 | `Task` | needs-rework | 0 | (attempt 2/3) revise — This is a promising bootstrap because it supplies a real compositional core, exp |
| 0 | `Action` | needs-rework | 0 | (attempt 2/3) revise — This is a promising bootstrap because it supplies a real compositional core, exp |
| 0 | `Check` | needs-rework | 0 | (attempt 2/3) revise — This is a promising bootstrap because it supplies a real compositional core, exp |
| 0 | `Flow-If` | needs-rework | 0 | (attempt 2/3) revise — This is a promising bootstrap because it supplies a real compositional core, exp |
| 0 | `Iterate` | needs-rework | 0 | (attempt 2/3) revise — This is a promising bootstrap because it supplies a real compositional core, exp |
| 0 | `Bind` | needs-rework | 0 | (attempt 2/3) revise — This is a promising bootstrap because it supplies a real compositional core, exp |
| 0 | `Conversation` | needs-rework | 0 | (attempt 2/3) add — This is a promising bootstrap because it supplies a real compositional core, exp |
| 0 | `Types & Lexicon` | accepted | 0 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 0 | `Task` | accepted | 0 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 0 | `Action` | accepted | 0 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 0 | `Utterance` | accepted | 0 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 0 | `Check` | accepted | 0 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 0 | `Flow-If` | accepted | 0 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 0 | `Iterate` | accepted | 0 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 0 | `Bind` | accepted | 0 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 0 | `Conversation` | accepted | 0 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 1 | `bind` | needs-rework | 1 | (attempt 1/3) revise — The underlying documentation idea is useful: existing LET plus ordered actions i |
| 1 | `bind` | needs-rework | 1 | (attempt 2/3) revise — This is a valuable corrective patch: it makes binding scope and UTTER content bi |
| 1 | `types-lexicon` | accepted | 1 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 1 | `action` | accepted | 1 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 1 | `bind` | accepted | 1 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 2 | `Action` | needs-rework | 2 | (attempt 1/3) revise — Canonical `draft` is a useful, positive addition for text-generation requests an |
| 2 | `Action` | needs-rework | 2 | (attempt 2/3) revise — The pure-generation distinction is a strong and useful direction, and the struct |
| 2 | `action` | needs-rework | 2 | (attempt 2/3) revise — The pure-generation distinction is a strong and useful direction, and the struct |
| 2 | `Generate` | needs-rework | 2 | (attempt 2/3) add — The pure-generation distinction is a strong and useful direction, and the struct |
| 2 | `Task` | needs-rework | 2 | (attempt 2/3) revise — The pure-generation distinction is a strong and useful direction, and the struct |
| 2 | `bind` | needs-rework | 2 | (attempt 2/3) revise — The pure-generation distinction is a strong and useful direction, and the struct |
| 2 | `Types & Lexicon` | accepted | 2 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 2 | `types-lexicon` | accepted | 2 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 2 | `Action` | accepted | 2 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 2 | `action` | accepted | 2 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 2 | `Bind` | accepted | 2 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 2 | `bind` | accepted | 2 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 2 | `Task` | accepted | 2 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 2 | `Generate` | accepted | 2 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 3 | `Action` | needs-rework | 3 | (attempt 1/3) revise — Closing exact tone literals is a useful local improvement for explicit values su |
| 3 | `Action` | needs-rework | 3 | (attempt 2/3) revise — The proposal has a sound core idea and materially improves deterministic transla |
| 3 | `Utterance` | needs-rework | 3 | (attempt 2/3) revise — The proposal has a sound core idea and materially improves deterministic transla |
| 3 | `Generate` | needs-rework | 3 | (attempt 2/3) revise — The proposal has a sound core idea and materially improves deterministic transla |
| 3 | `Action` | accepted | 3 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 3 | `Utterance` | accepted | 3 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 3 | `Generate` | accepted | 3 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 4 | `household-verb-normalization` | needs-rework | 4 | (attempt 1/3) add — The underlying normalization goal is sound and its simplest intended result is a |
| 4 | `Action` | needs-rework | 4 | (attempt 2/3) revise — The core idea is sound: normalize ordinary household bare put into the existing  |
| 4 | `Action` | accepted | 4 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 5 | `Action` | needs-rework | 5 | (attempt 1/3) revise — The core idea of adding structured travel and web-search fields is promising, bu |
| 5 | `Action` | needs-rework | 5 | (attempt 2/3) revise — The web collection data-flow idea is useful and the ISO-date flight example is c |
| 5 | `Task` | accepted | 5 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 5 | `Action` | accepted | 5 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 6 | `Action` | needs-rework | 6 | (attempt 1/3) revise — The core addition is the right shape: a typed Action result consumed by Flow-If  |
| 6 | `Action` | needs-rework | 6 | (attempt 2/3) revise — The core idea is sound: a future reply deadline should suspend control, and tran |
| 6 | `Flow-If` | needs-rework | 6 | (attempt 2/3) revise — The core idea is sound: a future reply deadline should suspend control, and tran |
| 6 | `Task` | needs-rework | 6 | (attempt 2/3) revise — The core idea is sound: a future reply deadline should suspend control, and tran |
| 6 | `Task` | accepted | 6 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 6 | `Action` | accepted | 6 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 6 | `Flow-If` | accepted | 6 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 7 | `Generate` | needs-rework | 7 | (attempt 2/3) revise — The quantity and typed-query ideas are sound and improve validation and conditio |
| 7 | `Action` | needs-rework | 7 | (attempt 2/3) revise — The quantity and typed-query ideas are sound and improve validation and conditio |
| 7 | `Generate` | accepted | 7 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 7 | `Action` | accepted | 7 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 8 | `Flow-If` | needs-rework | 8 | (attempt 1/3) revise — This attempt is not logically broken, but it makes no actual change: the propose |
| 8 | `Action` | needs-rework | 8 | (attempt 2/3) revise — The typed support query is a sound and useful extension: it materially improves  |
| 8 | `Action` | accepted | 8 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 9 | `Action` | needs-rework | 9 | (attempt 1/3) revise — The core idea is valuable and directly improves the selected rinse-then-place ca |
| 9 | `Action` | needs-rework | 9 | (attempt 2/3) revise — Explicit Action signatures and result categories are a real improvement for type |
| 9 | `Action` | accepted | 9 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 10 | `generate` | needs-rework | 10 | (attempt 1/3) revise — The central design choice is sound: drafting an email should be a pure GENERATE  |
