# Coverage: translating unseen test items

Success rate (higher is better) and mean number of missing glossary symbols per failed translation (the distinct symbols its suggestions add). `shared` = the items every model translated; `all` = the full sample (Gemini models).

| company | model | tier | items | runs | success | failed | error | missing symbols / failed | min / run | cost $ |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Gemini | Gemini 3.7 Flash (high effort) | strong | shared | 54 | 0.96 | 0.04 | 0.00 | 1.0 | 21.7 | 24.76 |
| Gemini | Gemini 3.7 Flash (high effort) | strong | all | 144 | 0.96 | 0.04 | 0.00 | 1.7 | 22.2 | 65.76 |
| Gemini | Gemini 3.7 Flash | weak | shared | 54 | 0.93 | 0.07 | 0.00 | 1.8 | 9.2 | 14.61 |
| Gemini | Gemini 3.7 Flash | weak | all | 144 | 0.94 | 0.06 | 0.00 | 2.1 | 9.8 | 41.02 |
| Claude | Claude Sonnet 5.5 | strong | shared | 54 | 0.46 | 0.54 | 0.00 | 1.8 | 2.9 | 11.08 |
| Claude | Claude Haiku 4.5 | weak | shared | 54 | 0.91 | 0.07 | 0.02 | 2.5 | 5.6 | 15.20 |
| OpenAI | o4-mini (Flash-tier probe) | weak | shared | 18 | 0.17 | 0.67 | 0.17 | 1.8 | 5.1 | 2.10 |

Success rate per dataset:

| model | items | Mind2Web | ALFRED | SWE-bench | PRISM | PATHs | ThoughtTrace |
|---|---|---:|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash (high effort) | shared | 0.78 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Gemini 3.7 Flash (high effort) | all | 0.92 | 0.92 | 0.92 | 1.00 | 1.00 | 1.00 |
| Gemini 3.7 Flash | shared | 0.78 | 1.00 | 1.00 | 0.78 | 1.00 | 1.00 |
| Gemini 3.7 Flash | all | 0.92 | 1.00 | 0.83 | 0.92 | 0.96 | 1.00 |
| Claude Sonnet 5.5 | shared | 0.67 | 0.33 | 0.67 | 0.44 | 0.11 | 0.56 |
| Claude Haiku 4.5 | shared | 0.78 | 0.89 | 1.00 | 1.00 | 0.78 | 1.00 |
| o4-mini (Flash-tier probe) | shared | 0.00 | 0.00 | 0.00 | 0.67 | 0.33 | 0.00 |
