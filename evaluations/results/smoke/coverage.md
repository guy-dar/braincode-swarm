# Coverage: translating unseen test items

Success rate (higher is better) and mean number of missing glossary symbols per failed translation (the distinct symbols its suggestions add). `shared` = the items every model translated; `all` = the full sample (Gemini models).

| company | model | tier | items | runs | success | failed | error | missing symbols / failed | min / run | cost $ |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Gemini | Gemini 3.7 Flash | weak | shared | 1 | 1.00 | 0.00 | 0.00 | — | 2.9 | 0.24 |
| Gemini | Gemini 3.7 Flash | weak | all | 1 | 1.00 | 0.00 | 0.00 | — | 2.9 | 0.24 |
| Claude | Claude Opus 5.5 | strong | shared | 1 | 0.00 | 1.00 | 0.00 | 2.0 | 1.8 | 0.41 |
| Claude | Claude Haiku 4.5 | weak | shared | 1 | 0.00 | 1.00 | 0.00 | 2.0 | 3.9 | 0.24 |
| OpenAI | GPT-6 Astra | strong | shared | 1 | 0.00 | 1.00 | 0.00 | 3.0 | 2.8 | — |
| OpenAI | o4-mini | weak | shared | 1 | 0.00 | 1.00 | 0.00 | 3.0 | 1.3 | 0.09 |

Success rate per dataset:

| model | items | Mind2Web | ALFRED | SWE-bench | PRISM | PATHs | ThoughtTrace |
|---|---|---:|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash | shared | 1.00 | — | — | — | — | — |
| Gemini 3.7 Flash | all | 1.00 | — | — | — | — | — |
| Claude Opus 5.5 | shared | 0.00 | — | — | — | — | — |
| Claude Haiku 4.5 | shared | 0.00 | — | — | — | — | — |
| GPT-6 Astra | shared | 0.00 | — | — | — | — | — |
| o4-mini | shared | 0.00 | — | — | — | — | — |
