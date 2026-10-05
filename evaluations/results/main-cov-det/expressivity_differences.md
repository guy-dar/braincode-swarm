# Expressivity: types of input-output differences (BLEU / ROUGE-L / word-Levenshtein round trip)

Measured on every scored round trip (original item text vs the reconstruction written from the BrainCode alone). Shares are the fraction of pairs; `lost` columns are the mean share of the original's numbers / capitalised names / code-like identifiers missing from the reconstruction; `added words` is the share of reconstruction words that never occur in the original. `language switch` = original mostly non-English, reconstruction English. `turns differ` = number of user/assistant turns differs; `steps differ` = numbered/bulleted steps differ by 2 or more.

## Per model (each model's full sample)

| model | pairs | ROUGE-L | length ratio | compressed (<0.6) | expanded (>1.4) | language switch | turns differ | steps differ | numbers lost | names lost | identifiers lost | added words |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash | 46 | 0.355 | 0.58 | 0.65 | 0.02 | 0.09 | 0.13 | 0.57 | 0.67 | 0.46 | 0.69 | 0.21 |
| Gemini 3.7 Flash (high effort) | 46 | 0.380 | 0.67 | 0.54 | 0.04 | 0.07 | 0.13 | 0.50 | 0.53 | 0.43 | 0.69 | 0.22 |
| o4-mini | 7 | 0.267 | 0.36 | 0.71 | 0.00 | 0.14 | 0.29 | 0.71 | 0.90 | 0.73 | 0.50 | 0.26 |

## Per model (the 18 shared items only)

| model | pairs | ROUGE-L | length ratio | compressed (<0.6) | expanded (>1.4) | language switch | turns differ | steps differ | numbers lost | names lost | identifiers lost | added words |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash | 17 | 0.354 | 0.56 | 0.71 | 0.06 | 0.18 | 0.18 | 0.65 | 0.64 | 0.41 | 0.74 | 0.22 |
| Gemini 3.7 Flash (high effort) | 17 | 0.384 | 0.60 | 0.53 | 0.00 | 0.12 | 0.18 | 0.59 | 0.56 | 0.42 | 0.73 | 0.23 |
| o4-mini | 7 | 0.267 | 0.36 | 0.71 | 0.00 | 0.14 | 0.29 | 0.71 | 0.90 | 0.73 | 0.50 | 0.26 |

## Per dataset (all models)

| dataset | pairs | ROUGE-L | length ratio | compressed (<0.6) | expanded (>1.4) | language switch | turns differ | steps differ | numbers lost | names lost | identifiers lost | added words |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Mind2Web | 17 | 0.544 | 0.85 | 0.18 | 0.00 | 0.35 | 0.00 | 0.29 | 0.32 | 0.11 | — | 0.12 |
| ALFRED | 17 | 0.572 | 0.74 | 0.29 | 0.06 | 0.00 | 0.76 | 1.00 | 0.94 | 0.73 | — | 0.10 |
| SWE-bench | 15 | 0.366 | 0.94 | 0.47 | 0.13 | 0.00 | 0.00 | 0.60 | 0.59 | 0.41 | 0.31 | 0.33 |
| PRISM | 19 | 0.257 | 0.45 | 0.84 | 0.00 | 0.00 | 0.05 | 0.26 | 0.54 | 0.50 | — | 0.25 |
| PATHs | 14 | 0.205 | 0.31 | 0.93 | 0.00 | 0.00 | 0.00 | 0.14 | 0.46 | 0.39 | 1.00 | 0.24 |
| ThoughtTrace | 17 | 0.201 | 0.33 | 0.94 | 0.00 | 0.12 | 0.00 | 0.94 | 0.78 | 0.69 | 1.00 | 0.29 |
