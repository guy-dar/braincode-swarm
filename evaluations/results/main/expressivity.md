# Expressivity: round trip natural language → BrainCode → natural language

**Every score is in [0, 1] and higher = input and output more similar = better.** BLEU = mean sentence BLEU (and corpus BLEU); ROUGE-L = longest-common-subsequence F1; word-Levenshtein similarity = 1 − word edit distance / longer length. One forward translation per item (its first usable run) is back-translated by the same model without seeing the original.

| model | dataset | pairs | BLEU ↑ | corpus BLEU ↑ | ROUGE-L ↑ | word-Levenshtein similarity ↑ |
|---|---|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash (high effort) | all | 48 | 0.126 | 0.053 | 0.388 | 0.283 |
| Gemini 3.7 Flash (high effort) | Mind2Web | 8 | 0.225 | 0.245 | 0.576 | 0.438 |
| Gemini 3.7 Flash (high effort) | ALFRED | 8 | 0.182 | 0.210 | 0.575 | 0.442 |
| Gemini 3.7 Flash (high effort) | SWE-bench | 8 | 0.222 | 0.206 | 0.414 | 0.318 |
| Gemini 3.7 Flash (high effort) | PRISM | 8 | 0.062 | 0.055 | 0.294 | 0.197 |
| Gemini 3.7 Flash (high effort) | PATHs | 8 | 0.042 | 0.021 | 0.250 | 0.160 |
| Gemini 3.7 Flash (high effort) | ThoughtTrace | 8 | 0.021 | 0.008 | 0.219 | 0.143 |
| Gemini 3.7 Flash | all | 48 | 0.114 | 0.044 | 0.362 | 0.249 |
| Gemini 3.7 Flash | Mind2Web | 8 | 0.218 | 0.233 | 0.544 | 0.397 |
| Gemini 3.7 Flash | ALFRED | 8 | 0.155 | 0.181 | 0.557 | 0.414 |
| Gemini 3.7 Flash | SWE-bench | 8 | 0.213 | 0.181 | 0.409 | 0.281 |
| Gemini 3.7 Flash | PRISM | 8 | 0.058 | 0.059 | 0.275 | 0.174 |
| Gemini 3.7 Flash | PATHs | 8 | 0.019 | 0.010 | 0.196 | 0.116 |
| Gemini 3.7 Flash | ThoughtTrace | 8 | 0.020 | 0.006 | 0.190 | 0.113 |
