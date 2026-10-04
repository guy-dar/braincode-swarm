# Determinism

Jensen-Shannon divergence (base 2, 0 = identical symbol use, 1 = disjoint; lower = more alike) between the symbol distributions P(symbol | model) and P(symbol type | model), pooled over every translation of the shared items. Same-model divergence: for each item, the mean JS over its pairs of runs; then the mean over items.

## Model pairs

| pair | model A | model B | JS symbols | JS types |
|---|---|---|---:|---:|
| strong vs strong, different companies | Claude Opus 5.5 | GPT-6 Astra | 0.118 | 0.018 |
| weak vs strong, same company | Claude Opus 5.5 | Claude Haiku 4.5 | 0.079 | 0.020 |
| weak vs strong, same company | GPT-6 Astra | o4-mini | 0.754 | 0.173 |
| weak vs weak, different companies | Gemini 3.7 Flash | Claude Haiku 4.5 | 0.035 | 0.021 |
| weak vs weak, different companies | Gemini 3.7 Flash | o4-mini | 0.626 | 0.121 |
| weak vs weak, different companies | Claude Haiku 4.5 | o4-mini | 0.650 | 0.185 |

## Same model, repeated runs

| model | items | items with ≥2 runs | JS symbols (mean ± sd) | JS types | identical run pairs |
|---|---|---:|---:|---:|---:|
| Gemini 3.7 Flash | shared | 0 | — ± — | — | — |
| Gemini 3.7 Flash | all | 0 | — ± — | — | — |
| Claude Opus 5.5 | shared | 0 | — ± — | — | — |
| Claude Haiku 4.5 | shared | 0 | — ± — | — | — |
| GPT-6 Astra | shared | 0 | — ± — | — | — |
| o4-mini | shared | 0 | — ± — | — | — |
