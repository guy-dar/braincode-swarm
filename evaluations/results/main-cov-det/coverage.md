# Coverage: translating unseen test items

Success rate (higher is better) and mean number of missing glossary symbols per failed translation (the distinct symbols its suggestions add). `shared` = the items every model translated; `all` = the full sample (Gemini models).

`rejected` = claimed successes and declared failures counted as errors because they carry source text instead of encoding it (needs marked opaque, or quoted strings of 8+ words outside names/titles; spec §13). They are included in `error` and left out of the determinism and expressivity analyses.

| company | model | tier | items | runs | success | failed | error | rejected | missing symbols / failed | min / run | cost $ |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemini | Gemini 3.7 Flash (high effort) | strong | shared | 54 | 0.91 | 0.04 | 0.06 | 3 | 1.0 | 21.7 | 24.76 |
| Gemini | Gemini 3.7 Flash (high effort) | strong | all | 144 | 0.91 | 0.04 | 0.05 | 7 | 1.7 | 22.2 | 65.76 |
| Gemini | Gemini 3.7 Flash | weak | shared | 54 | 0.85 | 0.07 | 0.07 | 4 | 1.8 | 9.2 | 14.61 |
| Gemini | Gemini 3.7 Flash | weak | all | 144 | 0.89 | 0.06 | 0.05 | 7 | 2.1 | 9.8 | 41.02 |
| Claude | Claude Sonnet 5.5 | strong | shared | 54 | 0.44 | 0.56 | 0.00 | 0 | 1.8 | 2.8 | 11.06 |
| Claude | Claude Haiku 4.5 | weak | shared | 54 | 0.93 | 0.07 | 0.00 | 0 | 2.5 | 6.3 | 16.45 |
| OpenAI | o4-mini | weak | shared | 54 | 0.07 | 0.85 | 0.07 | 0 | 2.4 | 4.6 | 6.18 |

Success rate per dataset:

| model | items | Mind2Web | ALFRED | SWE-bench | PRISM | PATHs | ThoughtTrace |
|---|---|---:|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash (high effort) | shared | 0.78 | 1.00 | 0.67 | 1.00 | 1.00 | 1.00 |
| Gemini 3.7 Flash (high effort) | all | 0.92 | 0.92 | 0.75 | 1.00 | 0.88 | 1.00 |
| Gemini 3.7 Flash | shared | 0.78 | 1.00 | 0.67 | 0.78 | 1.00 | 0.89 |
| Gemini 3.7 Flash | all | 0.92 | 1.00 | 0.71 | 0.92 | 0.83 | 0.96 |
| Claude Sonnet 5.5 | shared | 0.67 | 0.33 | 0.56 | 0.44 | 0.22 | 0.44 |
| Claude Haiku 4.5 | shared | 0.89 | 0.89 | 0.89 | 1.00 | 0.89 | 1.00 |
| o4-mini | shared | 0.11 | 0.11 | 0.11 | 0.00 | 0.11 | 0.00 |
