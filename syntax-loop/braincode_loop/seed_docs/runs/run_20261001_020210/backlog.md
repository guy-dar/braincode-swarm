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
| 10 | `Types & Lexicon` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `structural-symbol` | needs-rework | 10 | (attempt 1/3) add — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `literal-form` | needs-rework | 10 | (attempt 1/3) add — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `operation-symbol` | needs-rework | 10 | (attempt 1/3) add — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `entity-symbol` | needs-rework | 10 | (attempt 1/3) add — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `role-symbol` | needs-rework | 10 | (attempt 1/3) add — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `intent-symbol` | needs-rework | 10 | (attempt 1/3) add — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `attribute-symbol` | needs-rework | 10 | (attempt 1/3) add — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `attribute-value-symbol` | needs-rework | 10 | (attempt 1/3) add — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Action` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Utterance` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Generate` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Task` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Bind` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Conversation` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Flow-If` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Iterate` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Check` | needs-rework | 10 | (attempt 1/3) revise — The central idea—replace free text with typed literals, glossary categories, and |
| 10 | `Types & Lexicon` | needs-rework | 10 | (attempt 2/3) revise — This is a promising attempt to replace free strings with typed symbolic categori |
| 10 | `structural-symbol` | needs-rework | 10 | (attempt 2/3) revise — This is a promising attempt to replace free strings with typed symbolic categori |
| 10 | `operation-symbol` | needs-rework | 10 | (attempt 2/3) revise — This is a promising attempt to replace free strings with typed symbolic categori |
| 10 | `intent-symbol` | needs-rework | 10 | (attempt 2/3) revise — This is a promising attempt to replace free strings with typed symbolic categori |
| 10 | `code-form` | needs-rework | 10 | (attempt 2/3) add — This is a promising attempt to replace free strings with typed symbolic categori |
| 10 | `Task` | needs-rework | 10 | (attempt 2/3) revise — This is a promising attempt to replace free strings with typed symbolic categori |
| 10 | `Conversation` | needs-rework | 10 | (attempt 2/3) revise — This is a promising attempt to replace free strings with typed symbolic categori |
| 10 | `Utterance` | needs-rework | 10 | (attempt 2/3) revise — This is a promising attempt to replace free strings with typed symbolic categori |
| 10 | `Action` | needs-rework | 10 | (attempt 2/3) revise — This is a promising attempt to replace free strings with typed symbolic categori |
| 10 | `Generate` | needs-rework | 10 | (attempt 2/3) revise — This is a promising attempt to replace free strings with typed symbolic categori |
| 11 | `Types & Lexicon` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `structural-symbol` | needs-rework | 11 | (attempt 1/3) add — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `literal-form` | needs-rework | 11 | (attempt 1/3) add — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `code-form` | needs-rework | 11 | (attempt 1/3) add — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `entity-symbol` | needs-rework | 11 | (attempt 1/3) add — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `role-symbol` | needs-rework | 11 | (attempt 1/3) add — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `value-symbol` | needs-rework | 11 | (attempt 1/3) add — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `attribute-symbol` | needs-rework | 11 | (attempt 1/3) add — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `operation-symbol` | needs-rework | 11 | (attempt 1/3) add — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `intent-symbol` | needs-rework | 11 | (attempt 1/3) add — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `Action` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `Utterance` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `Generate` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `Task` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `Bind` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `Conversation` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `Flow-If` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `Iterate` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 11 | `Check` | needs-rework | 11 | (attempt 1/3) revise — The attempt addresses several prior structural requests and passes doc hygiene,  |
| 13 | `Types & Lexicon` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `structural-symbol` | needs-rework | 13 | (attempt 1/3) add — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `ontology-symbol` | needs-rework | 13 | (attempt 1/3) add — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Action` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Utterance` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Generate` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Task` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Bind` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Iterate` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Check` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Conversation` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Flow-If` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Generate` | needs-rework | 13 | (attempt 1/3) revise — This is a sound and substantial move toward the closed symbolic vocabulary requi |
| 13 | `Types & Lexicon` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `structural-symbol` | needs-rework | 13 | (attempt 2/3) add — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `ontology-symbol` | needs-rework | 13 | (attempt 2/3) add — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Action` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Utterance` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Generate` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Task` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Bind` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Iterate` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Check` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Flow-If` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Conversation` | needs-rework | 13 | (attempt 2/3) revise — This attempt makes substantial, sound progress on the focus note by closing free |
| 13 | `Types & Lexicon` | needs-rework | 13 | (attempt 3/3) revise — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `structural-symbol` | needs-rework | 13 | (attempt 3/3) add — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `entity-symbol` | needs-rework | 13 | (attempt 3/3) add — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `role-symbol` | needs-rework | 13 | (attempt 3/3) add — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `semantic-symbol` | needs-rework | 13 | (attempt 3/3) add — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `Action` | needs-rework | 13 | (attempt 3/3) revise — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `Utterance` | needs-rework | 13 | (attempt 3/3) revise — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `Generate` | needs-rework | 13 | (attempt 3/3) revise — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `Task` | needs-rework | 13 | (attempt 3/3) revise — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `Bind` | needs-rework | 13 | (attempt 3/3) revise — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `Iterate` | needs-rework | 13 | (attempt 3/3) revise — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `Check` | needs-rework | 13 | (attempt 3/3) revise — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | `Conversation` | needs-rework | 13 | (attempt 3/3) revise — The revision makes genuine progress toward closed vocabulary by removing free st |
| 13 | note N1 [hard] | stalled | 13 | violated — Removing STRING, unrestricted IDENT, and quoted prose is real progress. N1 is st |
| 14 | `operation-name` | needs-rework | 14 | (attempt 1/3) add — The proposal makes genuine N2 progress by adding distinct descriptive vocabulary |
| 14 | `search-criterion` | needs-rework | 14 | (attempt 1/3) add — The proposal makes genuine N2 progress by adding distinct descriptive vocabulary |
| 14 | `entity-category` | needs-rework | 14 | (attempt 1/3) add — The proposal makes genuine N2 progress by adding distinct descriptive vocabulary |
| 14 | `role-recipient` | needs-rework | 14 | (attempt 1/3) add — The proposal makes genuine N2 progress by adding distinct descriptive vocabulary |
| 14 | `code-structure` | needs-rework | 14 | (attempt 1/3) add — The proposal makes genuine N2 progress by adding distinct descriptive vocabulary |
| 14 | `artifact-type` | needs-rework | 14 | (attempt 1/3) add — The proposal makes genuine N2 progress by adding distinct descriptive vocabulary |
| 14 | `tone-value` | needs-rework | 14 | (attempt 1/3) add — The proposal makes genuine N2 progress by adding distinct descriptive vocabulary |
| 14 | `Action` | needs-rework | 14 | (attempt 2/3) revise — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `Generate` | needs-rework | 14 | (attempt 2/3) revise — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `operation-name` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `search-criterion` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `code-structure` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `artifact-type` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `attribute-name` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `tone-value` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `role-recipient` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `entity-category` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `literal-form` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `structural-word` | needs-rework | 14 | (attempt 2/3) add — This is meaningful progress on N2 because it adds multiple descriptive vocabular |
| 14 | `Types & Lexicon` | needs-rework | 14 | (attempt 3/3) revise — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `Action` | needs-rework | 14 | (attempt 3/3) revise — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `Generate` | needs-rework | 14 | (attempt 3/3) revise — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `structural-word` | needs-rework | 14 | (attempt 3/3) add — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `literal-form` | needs-rework | 14 | (attempt 3/3) add — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `code-structure` | needs-rework | 14 | (attempt 3/3) add — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `artifact-type` | needs-rework | 14 | (attempt 3/3) add — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `attribute-name` | needs-rework | 14 | (attempt 3/3) add — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `search-value` | needs-rework | 14 | (attempt 3/3) add — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `tone-value` | needs-rework | 14 | (attempt 3/3) add — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `role-recipient` | needs-rework | 14 | (attempt 3/3) add — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | `entity-category` | needs-rework | 14 | (attempt 3/3) add — This is a substantive N2 increment: it introduces descriptive glossary categorie |
| 14 | note N2 [hard] | open | 14 | violated — The proposal makes real progress by adding a Lexicon organization, SYMBOL, struc |
| 15 | `Types & Lexicon` | needs-rework | 15 | (attempt 1/3) revise — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `literal-form` | needs-rework | 15 | (attempt 1/3) add — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `structural-word` | needs-rework | 15 | (attempt 1/3) add — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `key-term` | needs-rework | 15 | (attempt 1/3) add — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `Action` | needs-rework | 15 | (attempt 1/3) revise — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `search-criterion` | needs-rework | 15 | (attempt 1/3) add — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `code-structure` | needs-rework | 15 | (attempt 1/3) add — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `entity-category` | needs-rework | 15 | (attempt 1/3) add — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `location-provider` | needs-rework | 15 | (attempt 1/3) add — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `speech-act` | needs-rework | 15 | (attempt 1/3) add — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `Utterance` | needs-rework | 15 | (attempt 1/3) revise — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `attribute-name` | needs-rework | 15 | (attempt 1/3) add — The increment makes real progress on N2 and improves practical planning structur |
| 15 | `Types & Lexicon` | needs-rework | 15 | (attempt 2/3) revise — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `literal-form` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `Action` | needs-rework | 15 | (attempt 2/3) revise — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `location-provider` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `entity-category` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `spatial-relation` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `search-criterion` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `descriptor-modifier` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `key-term` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `structural-word` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `tone-value` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `artifact-type` | needs-rework | 15 | (attempt 2/3) add — This is meaningful progress on N2: it fixes important lexical defects and adds u |
| 15 | `Types & Lexicon` | needs-rework | 15 | (attempt 3/3) revise — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `literal-form` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `structural-word` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `Action` | needs-rework | 15 | (attempt 3/3) revise — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `operation-vocabulary` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `attribute-name` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `location-provider` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `entity-category` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `spatial-relation` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `search-criterion` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `descriptor-modifier` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `availability-value` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `role-recipient` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `Generate` | needs-rework | 15 | (attempt 3/3) revise — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | `generation-attribute-value` | needs-rework | 15 | (attempt 3/3) add — This is a substantial and useful N2 increment: it restores held-out support cove |
| 15 | note N2 [hard] | open | 15 | violated — The proposal adds substantial structural-word, literal-form, operation, attribut |
| 16 | `structural-word` | needs-rework | 16 | (attempt 1/3) add — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `operation-vocabulary` | needs-rework | 16 | (attempt 1/3) add — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `attribute-name` | needs-rework | 16 | (attempt 1/3) add — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `entity-descriptor` | needs-rework | 16 | (attempt 1/3) add — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `spatial-relation` | needs-rework | 16 | (attempt 1/3) add — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `search-value` | needs-rework | 16 | (attempt 1/3) add — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `role-recipient` | needs-rework | 16 | (attempt 1/3) add — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `tone-value` | needs-rework | 16 | (attempt 1/3) add — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `artifact-specification` | needs-rework | 16 | (attempt 1/3) add — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `Action` | needs-rework | 16 | (attempt 1/3) revise — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `Generate` | needs-rework | 16 | (attempt 1/3) revise — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 16 | `Utterance` | needs-rework | 16 | (attempt 1/3) revise — The proposal makes substantial, sound progress on the N2 vocabulary-building dir |
| 17 | `structural-word` | needs-rework | 17 | (attempt 1/3) add — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `operation-vocabulary` | needs-rework | 17 | (attempt 1/3) add — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `attribute-name` | needs-rework | 17 | (attempt 1/3) add — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `entity-name` | needs-rework | 17 | (attempt 1/3) add — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `spatial-relation` | needs-rework | 17 | (attempt 1/3) add — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `search-value` | needs-rework | 17 | (attempt 1/3) add — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `role-recipient` | needs-rework | 17 | (attempt 1/3) add — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `tone-value` | needs-rework | 17 | (attempt 1/3) add — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `artifact-specification` | needs-rework | 17 | (attempt 1/3) add — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `Action` | needs-rework | 17 | (attempt 1/3) revise — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `Generate` | needs-rework | 17 | (attempt 1/3) revise — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `Utterance` | needs-rework | 17 | (attempt 1/3) revise — The bundle makes meaningful N2 progress by adding genuine vocabulary categories  |
| 17 | `structural-word` | needs-rework | 17 | (attempt 2/3) add — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `operation-vocabulary` | needs-rework | 17 | (attempt 2/3) add — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `attribute-name` | needs-rework | 17 | (attempt 2/3) add — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `entity-name` | needs-rework | 17 | (attempt 2/3) add — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `spatial-relation` | needs-rework | 17 | (attempt 2/3) add — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `search-value` | needs-rework | 17 | (attempt 2/3) add — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `role-recipient` | needs-rework | 17 | (attempt 2/3) add — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `tone-value` | needs-rework | 17 | (attempt 2/3) add — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `artifact-specification` | needs-rework | 17 | (attempt 2/3) add — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `Action` | needs-rework | 17 | (attempt 2/3) revise — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `Generate` | needs-rework | 17 | (attempt 2/3) revise — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `Utterance` | needs-rework | 17 | (attempt 2/3) revise — The bundle makes substantial N2/N3/N7 progress by adding actual lexical categori |
| 17 | `structural-word` | accepted | 17 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `operation-vocabulary` | accepted | 17 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `attribute-name` | accepted | 17 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `entity-name` | accepted | 17 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `search-value` | accepted | 17 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `spatial-relation` | accepted | 17 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `platform-name` | accepted | 17 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `location-name` | accepted | 17 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `descriptive-value` | accepted | 17 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `Action` | accepted | 17 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `Generate` | accepted | 17 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | `Utterance` | accepted | 17 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 17 | note N2 [hard] | stalled | 17 | violated — The glossary moves substantially toward a complete lexicon by adding structural, |
| 18 | `tone-value` | needs-rework | 18 | (attempt 1/3) add — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `format-value` | accepted | 18 | (attempt 1/3) add — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `duration-unit-value` | needs-rework | 18 | (attempt 1/3) add — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `currency-value` | needs-rework | 18 | (attempt 1/3) add — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `recipient-value` | needs-rework | 18 | (attempt 1/3) add — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `search-value` | needs-rework | 18 | (attempt 1/3) revise — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `descriptive-value` | needs-rework | 18 | (attempt 1/3) revise — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `Generate` | needs-rework | 18 | (attempt 1/3) revise — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `Flow-If` | needs-rework | 18 | (attempt 1/3) revise — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `attribute-name` | needs-rework | 18 | (attempt 1/3) revise — The bundle makes substantive progress on N3 by introducing dedicated value categ |
| 18 | `Generate` | needs-rework | 18 | (attempt 2/3) revise — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `Flow-If` | accepted | 18 | (attempt 2/3) revise — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `tone-value` | accepted | 18 | (attempt 2/3) add — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `duration-unit-value` | accepted | 18 | (attempt 2/3) add — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `currency-value` | accepted | 18 | (attempt 2/3) add — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `recipient-value` | accepted | 18 | (attempt 2/3) add — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `artifact-value` | accepted | 18 | (attempt 2/3) add — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `descriptive-value` | accepted | 18 | (attempt 2/3) revise — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `search-value` | accepted | 18 | (attempt 2/3) revise — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `format-value` | needs-rework | 18 | (attempt 2/3) revise — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `product-attribute-value` | accepted | 18 | (attempt 2/3) add — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `attribute-name` | needs-rework | 18 | (attempt 2/3) revise — This bundle makes meaningful N3 progress by separating several attribute value s |
| 18 | `Types & Lexicon` | accepted | 18 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `Generate` | accepted | 18 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `Action` | accepted | 18 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `shape-value` | accepted | 18 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `state-value` | accepted | 18 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `style-value` | accepted | 18 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `locale-value` | accepted | 18 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `metric-value` | accepted | 18 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `descriptive-value` | accepted | 18 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `format-value` | accepted | 18 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | `attribute-name` | accepted | 18 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 18 | note N3 [hard] | open | 18 | violated — Several formerly residual attribute values now have named categories or defined  |
| 19 | `Action` | needs-rework | 19 | (attempt 1/3) revise — This is real progress on N3: it correctly identifies transitional STRING attribu |
| 19 | `Generate` | needs-rework | 19 | (attempt 1/3) revise — This is real progress on N3: it correctly identifies transitional STRING attribu |
| 19 | `Utterance` | accepted | 19 | (attempt 1/3) revise — This is real progress on N3: it correctly identifies transitional STRING attribu |
| 19 | `attribute-name` | accepted | 19 | (attempt 1/3) revise — This is real progress on N3: it correctly identifies transitional STRING attribu |
| 19 | `state-value` | accepted | 19 | (attempt 1/3) revise — This is real progress on N3: it correctly identifies transitional STRING attribu |
| 19 | `descriptive-value` | accepted | 19 | (attempt 1/3) revise — This is real progress on N3: it correctly identifies transitional STRING attribu |
| 19 | `Types & Lexicon` | needs-rework | 19 | (attempt 2/3) revise — The bundle substantively addresses every prior required change: it introduces pr |
| 19 | `Action` | needs-rework | 19 | (attempt 2/3) revise — The bundle substantively addresses every prior required change: it introduces pr |
| 19 | `attribute-name` | needs-rework | 19 | (attempt 2/3) revise — The bundle substantively addresses every prior required change: it introduces pr |
| 19 | `Generate` | needs-rework | 19 | (attempt 2/3) revise — The bundle substantively addresses every prior required change: it introduces pr |
| 19 | `Utterance` | needs-rework | 19 | (attempt 2/3) revise — The bundle substantively addresses every prior required change: it introduces pr |
| 19 | `currency-value` | accepted | 19 | (attempt 2/3) revise — The bundle substantively addresses every prior required change: it introduces pr |
| 19 | `semantic-category-value` | accepted | 19 | (attempt 2/3) add — The bundle substantively addresses every prior required change: it introduces pr |
| 19 | `Types & Lexicon` | needs-rework | 19 | (attempt 3/3) revise — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | `Action` | needs-rework | 19 | (attempt 3/3) revise — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | `attribute-name` | needs-rework | 19 | (attempt 3/3) revise — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | `Generate` | needs-rework | 19 | (attempt 3/3) revise — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | `Utterance` | needs-rework | 19 | (attempt 3/3) revise — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | `semantic-category-value` | needs-rework | 19 | (attempt 3/3) revise — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | `entity-name` | needs-rework | 19 | (attempt 3/3) revise — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | `code-value` | accepted | 19 | (attempt 3/3) add — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | `content-value` | accepted | 19 | (attempt 3/3) add — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | `duration-unit-value` | accepted | 19 | (attempt 3/3) revise — This is real progress on N3: governed code/content symbols, qualified category b |
| 19 | note N3 [hard] | open | 19 | violated — Category-qualified bindings, individually indexed domains, code-value, content-v |
| 20 | `Types & Lexicon` | needs-rework | 20 | (attempt 1/3) revise — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `Action` | needs-rework | 20 | (attempt 1/3) revise — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `Generate` | needs-rework | 20 | (attempt 1/3) revise — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `Utterance` | needs-rework | 20 | (attempt 1/3) revise — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `attribute-name` | needs-rework | 20 | (attempt 1/3) revise — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `entity-name` | accepted | 20 | (attempt 1/3) revise — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `semantic-category-value` | accepted | 20 | (attempt 1/3) revise — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `topic-value` | accepted | 20 | (attempt 1/3) add — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `constraint-value` | accepted | 20 | (attempt 1/3) add — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `transformation-value` | accepted | 20 | (attempt 1/3) add — The bundle makes genuine progress on N3 through exact category provenance and se |
| 20 | `Types & Lexicon` | needs-rework | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `attribute-name` | needs-rework | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `Action` | needs-rework | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `operation-vocabulary` | needs-rework | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `Generate` | needs-rework | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `Utterance` | needs-rework | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `duration-unit-value` | accepted | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `Task` | needs-rework | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `event-value` | accepted | 20 | (attempt 2/3) add — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `character-property-value` | accepted | 20 | (attempt 2/3) add — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `topic-value` | accepted | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `constraint-value` | accepted | 20 | (attempt 2/3) revise — The bundle makes real N3 progress by eliminating unqualified STRING from the rev |
| 20 | `Types & Lexicon` | needs-rework | 20 | (attempt 3/3) revise — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `operation-vocabulary` | needs-rework | 20 | (attempt 3/3) revise — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `Action` | needs-rework | 20 | (attempt 3/3) revise — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `attribute-name` | needs-rework | 20 | (attempt 3/3) revise — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `Generate` | needs-rework | 20 | (attempt 3/3) revise — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `Utterance` | needs-rework | 20 | (attempt 3/3) revise — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `Task` | needs-rework | 20 | (attempt 3/3) revise — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `predicate-value` | needs-rework | 20 | (attempt 3/3) add — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `participant-value` | needs-rework | 20 | (attempt 3/3) add — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `evidence-value` | needs-rework | 20 | (attempt 3/3) add — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `food-value` | needs-rework | 20 | (attempt 3/3) add — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | `dietary-value` | needs-rework | 20 | (attempt 3/3) add — This is real progress on N3: the proposal replaces many unqualified attribute ST |
| 20 | note N3 [hard] | stalled | 20 | violated — Most revised Action, Generate, and Utterance attributes now have named category  |
| 21 | `Canonical-Form` | needs-rework | 21 | (attempt 1/3) add — The bundle has the right N7 objective and makes real progress through a shared c |
| 21 | `Bind` | needs-rework | 21 | (attempt 1/3) revise — The bundle has the right N7 objective and makes real progress through a shared c |
| 21 | `Task` | needs-rework | 21 | (attempt 1/3) revise — The bundle has the right N7 objective and makes real progress through a shared c |
| 21 | `Conversation` | needs-rework | 21 | (attempt 1/3) revise — The bundle has the right N7 objective and makes real progress through a shared c |
| 21 | `Canonical-Form` | needs-rework | 21 | (attempt 2/3) add — This is a meaningful N7-oriented improvement: it makes several formerly discreti |
| 21 | `Bind` | needs-rework | 21 | (attempt 2/3) revise — This is a meaningful N7-oriented improvement: it makes several formerly discreti |
| 21 | `Task` | needs-rework | 21 | (attempt 2/3) revise — This is a meaningful N7-oriented improvement: it makes several formerly discreti |
| 21 | `Conversation` | needs-rework | 21 | (attempt 2/3) revise — This is a meaningful N7-oriented improvement: it makes several formerly discreti |
| 21 | `Flow-If` | needs-rework | 21 | (attempt 2/3) revise — This is a meaningful N7-oriented improvement: it makes several formerly discreti |
| 21 | `Action` | needs-rework | 21 | (attempt 2/3) revise — This is a meaningful N7-oriented improvement: it makes several formerly discreti |
| 21 | `Generate` | needs-rework | 21 | (attempt 2/3) revise — This is a meaningful N7-oriented improvement: it makes several formerly discreti |
| 21 | `Types & Lexicon` | needs-rework | 21 | (attempt 2/3) revise — This is a meaningful N7-oriented improvement: it makes several formerly discreti |
| 21 | `Canonical-Form` | needs-rework | 21 | (attempt 3/3) add — This bundle makes real progress on N7 through explicit request scope, multiplici |
| 21 | `Bind` | needs-rework | 21 | (attempt 3/3) revise — This bundle makes real progress on N7 through explicit request scope, multiplici |
| 21 | `Flow-If` | needs-rework | 21 | (attempt 3/3) revise — This bundle makes real progress on N7 through explicit request scope, multiplici |
| 21 | `Task` | needs-rework | 21 | (attempt 3/3) revise — This bundle makes real progress on N7 through explicit request scope, multiplici |
| 21 | `Conversation` | needs-rework | 21 | (attempt 3/3) revise — This bundle makes real progress on N7 through explicit request scope, multiplici |
| 21 | `Action` | needs-rework | 21 | (attempt 3/3) revise — This bundle makes real progress on N7 through explicit request scope, multiplici |
| 21 | `Generate` | needs-rework | 21 | (attempt 3/3) revise — This bundle makes real progress on N7 through explicit request scope, multiplici |
| 21 | `attribute-name` | accepted | 21 | (attempt 3/3) revise — This bundle makes real progress on N7 through explicit request scope, multiplici |
| 21 | note N7 [hard] | open | 21 | violated — ISR, CSR, CFR, SOR, AOR, deterministic TURN naming, and a lexical collision stra |
| 22 | `canonical-form` | needs-rework | 22 | (attempt 1/3) add — The bundle makes genuine, substantial progress toward deterministic encoding and |
| 22 | `Bind` | needs-rework | 22 | (attempt 1/3) revise — The bundle makes genuine, substantial progress toward deterministic encoding and |
| 22 | `Task` | needs-rework | 22 | (attempt 1/3) revise — The bundle makes genuine, substantial progress toward deterministic encoding and |
| 22 | `Conversation` | needs-rework | 22 | (attempt 1/3) revise — The bundle makes genuine, substantial progress toward deterministic encoding and |
| 22 | `Action` | needs-rework | 22 | (attempt 1/3) revise — The bundle makes genuine, substantial progress toward deterministic encoding and |
| 22 | `Generate` | needs-rework | 22 | (attempt 1/3) revise — The bundle makes genuine, substantial progress toward deterministic encoding and |
| 22 | `Utterance` | needs-rework | 22 | (attempt 1/3) revise — The bundle makes genuine, substantial progress toward deterministic encoding and |
| 22 | `Flow-If` | needs-rework | 22 | (attempt 1/3) revise — The bundle makes genuine, substantial progress toward deterministic encoding and |
| 22 | `duration-unit-value` | accepted | 22 | (attempt 1/3) revise — The bundle makes genuine, substantial progress toward deterministic encoding and |
| 22 | `canonical-form` | needs-rework | 22 | (attempt 2/3) add — The bundle makes substantial, concrete progress on N7 through fixed ordering, na |
| 22 | `operation-vocabulary` | needs-rework | 22 | (attempt 2/3) revise — The bundle makes substantial, concrete progress on N7 through fixed ordering, na |
| 22 | `entity-name` | accepted | 22 | (attempt 2/3) revise — The bundle makes substantial, concrete progress on N7 through fixed ordering, na |
| 22 | `Task` | needs-rework | 22 | (attempt 2/3) revise — The bundle makes substantial, concrete progress on N7 through fixed ordering, na |
| 22 | `Action` | needs-rework | 22 | (attempt 2/3) revise — The bundle makes substantial, concrete progress on N7 through fixed ordering, na |
| 22 | `Bind` | needs-rework | 22 | (attempt 2/3) revise — The bundle makes substantial, concrete progress on N7 through fixed ordering, na |
| 22 | `Generate` | needs-rework | 22 | (attempt 2/3) revise — The bundle makes substantial, concrete progress on N7 through fixed ordering, na |
| 22 | `Utterance` | needs-rework | 22 | (attempt 2/3) revise — The bundle makes substantial, concrete progress on N7 through fixed ordering, na |
| 22 | `Conversation` | needs-rework | 22 | (attempt 2/3) revise — The bundle makes substantial, concrete progress on N7 through fixed ordering, na |
| 22 | `canonical-form` | accepted | 22 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `operation-vocabulary` | accepted | 22 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `attribute-name` | accepted | 22 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `capacity-unit-value` | accepted | 22 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `cuisine-value` | accepted | 22 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `reservation-status-value` | accepted | 22 | (attempt 3/3) add — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `Action` | accepted | 22 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `Task` | accepted | 22 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `format-value` | accepted | 22 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `Utterance` | accepted | 22 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | `Conversation` | accepted | 22 | (attempt 3/3) revise — [Forced acceptance after 3 attempt(s) without a clean accept — the required chan |
| 22 | note N7 [hard] | open | 22 | violated — Fixed ordering intentions, handle conventions, deterministic turn names, explici |
