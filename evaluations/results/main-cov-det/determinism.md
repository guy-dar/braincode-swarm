# Determinism

Jensen-Shannon divergence (base 2, 0 = identical symbol use, 1 = disjoint; lower = more alike) between the symbol distributions P(symbol | model) and P(symbol type | model), pooled over every translation of the shared items. Same-model divergence: for each item, the mean JS over its pairs of runs; then the mean over items.

## Model pairs

| pair | model A | model B | JS symbols | JS types |
|---|---|---|---:|---:|
| strong vs strong, different companies | Gemini 3.7 Flash (high effort) | Claude Sonnet 5.5 | 0.094 | 0.006 |
| weak vs strong, same company | Gemini 3.7 Flash (high effort) | Gemini 3.7 Flash | 0.020 | 0.001 |
| weak vs strong, same company | Claude Sonnet 5.5 | Claude Haiku 4.5 | 0.069 | 0.002 |
| weak vs weak, different companies | Gemini 3.7 Flash | Claude Haiku 4.5 | 0.098 | 0.007 |
| weak vs weak, different companies | Gemini 3.7 Flash | o4-mini | 0.183 | 0.050 |
| weak vs weak, different companies | Claude Haiku 4.5 | o4-mini | 0.165 | 0.051 |

## Same model, repeated runs

| model | items | items with ≥2 runs | JS symbols (mean ± sd) | JS types | identical run pairs |
|---|---|---:|---:|---:|---:|
| Gemini 3.7 Flash (high effort) | shared | 17 | 0.092 ± 0.073 | 0.025 | 0.08 |
| Gemini 3.7 Flash (high effort) | all | 46 | 0.114 ± 0.078 | 0.032 | 0.04 |
| Gemini 3.7 Flash | shared | 17 | 0.114 ± 0.079 | 0.034 | 0.00 |
| Gemini 3.7 Flash | all | 46 | 0.135 ± 0.090 | 0.046 | 0.04 |
| Claude Sonnet 5.5 | shared | 18 | 0.121 ± 0.048 | 0.034 | 0.02 |
| Claude Haiku 4.5 | shared | 18 | 0.173 ± 0.079 | 0.049 | 0.02 |
| o4-mini | shared | 16 | 0.330 ± 0.163 | 0.162 | 0.00 |
