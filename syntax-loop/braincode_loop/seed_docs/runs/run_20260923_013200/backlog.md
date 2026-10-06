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
