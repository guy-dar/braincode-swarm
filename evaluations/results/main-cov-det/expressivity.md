# Expressivity: round trip natural language → BrainCode → natural language

**Every score is in [0, 1] and higher = input and output more similar = better.** BLEU = mean sentence BLEU (and corpus BLEU); ROUGE-L = longest-common-subsequence F1; word-Levenshtein similarity = 1 − word edit distance / longer length. One forward translation per item (its first usable run) is back-translated by the same model without seeing the original: the back-translator gets only the BrainCode block of the translation (not the translation report), and the scores compare only the original item text (input) with the reconstructed text (output), turn markers removed.

`items`: `all` = the model's full sample (Gemini: 48 items); `shared` = the 18 items every model translated (use these rows to compare models; o4-mini has back-translations only where its forward run produced a usable translation). Per-dataset rows and the figure use each model's full sample.

`quoted` = share of the BrainCode's characters inside quoted string literals (`content="…"` and other literals). Text carried verbatim in strings comes back almost unchanged, so a high score with a high quoted share measures copying, not how much meaning the symbols encode.

| model | items | dataset | pairs | BLEU ↑ | corpus BLEU ↑ | ROUGE-L ↑ | word-Levenshtein similarity ↑ | quoted |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash (high effort) | shared | all | 17 | 0.129 | 0.038 | 0.384 | 0.282 | 0.11 |
| Gemini 3.7 Flash | shared | all | 17 | 0.112 | 0.029 | 0.354 | 0.246 | 0.12 |
| o4-mini | shared | all | 7 | 0.082 | 0.002 | 0.267 | 0.170 | 0.08 |
| Gemini 3.7 Flash (high effort) | all | all | 46 | 0.114 | 0.041 | 0.380 | 0.275 | 0.10 |
| Gemini 3.7 Flash | all | all | 46 | 0.103 | 0.034 | 0.355 | 0.242 | 0.11 |
| o4-mini | shared | Mind2Web | 1 | 0.017 | 0.017 | 0.295 | 0.191 | 0.12 |
| o4-mini | shared | ALFRED | 1 | 0.360 | 0.360 | 0.677 | 0.478 | 0.08 |
| o4-mini | shared | SWE-bench | 1 | 0.194 | 0.194 | 0.421 | 0.269 | 0.09 |
| o4-mini | shared | PRISM | 3 | 0.001 | 0.000 | 0.110 | 0.058 | 0.05 |
| o4-mini | shared | ThoughtTrace | 1 | 0.000 | 0.000 | 0.146 | 0.075 | 0.15 |
| Gemini 3.7 Flash (high effort) | all | Mind2Web | 8 | 0.225 | 0.245 | 0.576 | 0.438 | 0.13 |
| Gemini 3.7 Flash (high effort) | all | ALFRED | 8 | 0.182 | 0.210 | 0.575 | 0.442 | 0.04 |
| Gemini 3.7 Flash (high effort) | all | SWE-bench | 7 | 0.163 | 0.110 | 0.362 | 0.266 | 0.14 |
| Gemini 3.7 Flash (high effort) | all | PRISM | 8 | 0.062 | 0.055 | 0.294 | 0.197 | 0.12 |
| Gemini 3.7 Flash (high effort) | all | PATHs | 7 | 0.026 | 0.014 | 0.231 | 0.145 | 0.12 |
| Gemini 3.7 Flash (high effort) | all | ThoughtTrace | 8 | 0.021 | 0.008 | 0.219 | 0.143 | 0.09 |
| Gemini 3.7 Flash | all | Mind2Web | 8 | 0.218 | 0.233 | 0.544 | 0.397 | 0.14 |
| Gemini 3.7 Flash | all | ALFRED | 8 | 0.155 | 0.181 | 0.557 | 0.414 | 0.03 |
| Gemini 3.7 Flash | all | SWE-bench | 7 | 0.156 | 0.085 | 0.361 | 0.233 | 0.16 |
| Gemini 3.7 Flash | all | PRISM | 8 | 0.058 | 0.059 | 0.275 | 0.174 | 0.14 |
| Gemini 3.7 Flash | all | PATHs | 7 | 0.010 | 0.007 | 0.179 | 0.104 | 0.12 |
| Gemini 3.7 Flash | all | ThoughtTrace | 8 | 0.020 | 0.006 | 0.190 | 0.113 | 0.09 |
