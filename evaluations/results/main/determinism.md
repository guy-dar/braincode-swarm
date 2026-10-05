# Determinism

Jensen-Shannon divergence (base 2, 0 = identical symbol use, 1 = disjoint; lower = more alike) between the symbol distributions P(symbol | model) and P(symbol type | model), pooled over every translation of the shared items. Same-model divergence: for each item, the mean JS over its pairs of runs; then the mean over items.

## Model pairs

| pair | model A | model B | JS symbols | JS types |
|---|---|---|---:|---:|
| strong vs strong, different companies | Gemini 3.7 Flash (high effort) | Claude Sonnet 5.5 | 0.086 | 0.006 |
| strong vs strong, different companies | Gemini 3.7 Flash (high effort) | GPT-6.1 Sol | 0.349 | 0.032 |
| strong vs strong, different companies | Claude Sonnet 5.5 | GPT-6.1 Sol | 0.342 | 0.029 |
| weak vs strong, same company | Gemini 3.7 Flash (high effort) | Gemini 3.7 Flash | 0.020 | 0.001 |
| weak vs strong, same company | Claude Sonnet 5.5 | Claude Haiku 4.5 | 0.067 | 0.003 |
| weak vs strong, same company | GPT-6.1 Sol | GPT-6 Luna | 0.122 | 0.032 |
| weak vs strong, same company | GPT-6.1 Sol | o4-mini (Flash-tier probe) | 0.373 | 0.092 |
| weak vs strong, same company | GPT-6 Luna | o4-mini (Flash-tier probe) | 0.344 | 0.153 |
| weak vs weak, different companies | Gemini 3.7 Flash | Claude Haiku 4.5 | 0.088 | 0.007 |
| weak vs weak, different companies | Gemini 3.7 Flash | GPT-6 Luna | 0.276 | 0.030 |
| weak vs weak, different companies | Gemini 3.7 Flash | o4-mini (Flash-tier probe) | 0.318 | 0.135 |
| weak vs weak, different companies | Claude Haiku 4.5 | GPT-6 Luna | 0.318 | 0.051 |
| weak vs weak, different companies | Claude Haiku 4.5 | o4-mini (Flash-tier probe) | 0.308 | 0.118 |

## Same model, repeated runs

| model | items | items with ≥2 runs | JS symbols (mean ± sd) | JS types | identical run pairs |
|---|---|---:|---:|---:|---:|
| Gemini 3.7 Flash (high effort) | shared | 18 | 0.098 ± 0.075 | 0.028 | 0.07 |
| Gemini 3.7 Flash (high effort) | all | 48 | 0.118 ± 0.078 | 0.032 | 0.03 |
| Gemini 3.7 Flash | shared | 18 | 0.115 ± 0.077 | 0.035 | 0.00 |
| Gemini 3.7 Flash | all | 48 | 0.135 ± 0.088 | 0.046 | 0.03 |
| Claude Sonnet 5.5 | shared | 18 | 0.119 ± 0.045 | 0.032 | 0.02 |
| Claude Haiku 4.5 | shared | 18 | 0.183 ± 0.094 | 0.063 | 0.00 |
| GPT-6.1 Sol | shared | 8 | 0.109 ± 0.080 | 0.030 | 0.08 |
| GPT-6 Luna | shared | 7 | 0.250 ± 0.178 | 0.112 | 0.00 |
| o4-mini (Flash-tier probe) | shared | 0 | — ± — | — | — |
