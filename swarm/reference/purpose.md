# BrainCode — project purpose

Condensed from the project proposal (`C:/projects/BrainCode/instructions/Project Proposal.pdf`), based on Guy Dar's BrainCode idea. This file tells the migrator and other glossary-shaping roles what the language is for, so glossary decisions can be judged against the project's goals rather than only against local convenience.

## The idea

**BrainCode: turning human-agent communication into a programming language.** In AI agents, human requests and agent thinking are written in unstructured natural language. Programming languages are concise and structured but lack natural language's expressive power. BrainCode bridges the gap by turning natural language into a programming language that is very rich and "long-tailed".

The language is developed in a semi-automated, iterative process: AI develops meta-concepts in the language through AI debate, based on a large batch of real-world examples, and humans correct it until the outcome is acceptable.

The language should be rich enough to express human requests and agentic thinking, but without redundancy and without dependence on the linguistic style of the specific model. This standardization can later help identify points of difficulty for AI and, in some cases, improve on them.

## Objective

Formalize reasoning tasks (task decomposition) in a way that is:

- **expressive**,
- **wide in coverage**,
- **formal (deterministic)**, and
- **understandable (interpretable)** to both humans and LLMs.

## Preliminary KPIs

| KPI | What it tests |
|---|---|
| **Coverage** | Whether the language can formalize previously unseen domains, for example benchmarks from multiple areas, and whether it generalizes to benchmarks not encountered during language development. This also raises the question of whether additional operators may be needed at inference time. |
| **Expressivity** | An autoencoder-style setup: one model translates a natural-language task into the language, another reconstructs it into natural language, and the difference between the original and reconstructed tasks is measured. |
| **Determinism** | Whether different models, or independent instances of the same model, map the same task to the same expression. |
| **Improvement** | Whether access to the language improves weaker models' solve rate or other benchmark metrics, both on benchmarks used during development and on new ones. |
| **Interpretability** | Clear documentation of the language's foundations must be maintained, and checked throughout development to confirm it remains understandable to people. Ideally this is later evaluated through direct human use. |

## Sources

The debate analyzes reasoning benchmarks, chain-of-thought traces, potentially less structured human task databases, and natural-language human-feedback chats.

## Implications for glossary decisions

These follow from the goals above. They are guidance for the migrator, not part of the proposal text.

- **Coverage over one-offs.** Prefer reusable constructors and families that cover many future items over a symbol that names one phrase ("avoids one symbol per phrase").
- **Determinism.** Every accepted entry must make translators converge. Overlapping or ambiguous entries hurt determinism even when each one is individually reasonable.
- **Expressivity.** An entry must preserve distinctions a back-translation would need (negation, quantity, time, attribution, uncertainty). Renaming a sentence is not a definition.
- **Interpretability.** Definitions, contrasts and examples must be readable by a person without the source item.
- **No style dependence.** Encode content and communicative intent, not wording.
