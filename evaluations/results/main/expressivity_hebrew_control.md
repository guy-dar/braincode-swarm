# Expressivity control: BrainCode vs Hebrew round trips

**Every score is in [0, 1]; higher = the reconstruction is closer to the original = better.** Both round trips start from the same English item and end in English, written by the same model, which never sees the original on the way back. They are scored with the same functions (`metrics.py`): sentence BLEU, ROUGE-L F1 and word-Levenshtein similarity on lower-cased words, turn markers removed.

- **BrainCode (BC):** English → BrainCode → English, with the swarm translator's setup (spec, glossary g19, RAG, kit). From `results/main/expressivity.md`.
- **Hebrew (HE):** English → Hebrew → English, with the same container harness and proxy, but no BrainCode, no glossary and no RAG. Code, paths, URLs, identifiers, UI labels and names stay verbatim in the Hebrew.
- **copied:** text carried over unchanged, which comes back almost for free. BC: share of the BrainCode's characters inside quoted literals. HE: share of the Hebrew's words still in Latin script.

Hebrew is the reference for an ordinary, fluent translation: the gap BC − HE is how much more a BrainCode round trip loses than a translation into another natural language.

Round trips available: Gemini 3.7 Flash: BrainCode 46, Hebrew 48, Gemini 3.7 Flash (high effort): BrainCode 46, Hebrew 48. Compared: items with both, per model.

## Means per model and dataset (Hebrew in bold)

| model | dataset | pairs | BLEU BC | BLEU HE | ROUGE-L BC | ROUGE-L HE | word-Levenshtein similarity BC | word-Levenshtein similarity HE | copied BC | copied HE |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash | all | 46 | 0.103 | **0.770** | 0.355 | **0.893** | 0.242 | **0.860** | 0.11 | 0.18 |
| Gemini 3.7 Flash | ALFRED | 8 | 0.155 | **0.600** | 0.557 | **0.828** | 0.414 | **0.767** | 0.03 | 0.01 |
| Gemini 3.7 Flash | Mind2Web | 8 | 0.218 | **0.918** | 0.544 | **0.967** | 0.397 | **0.952** | 0.14 | 0.50 |
| Gemini 3.7 Flash | PATHs | 7 | 0.010 | **0.781** | 0.179 | **0.900** | 0.104 | **0.871** | 0.12 | 0.06 |
| Gemini 3.7 Flash | PRISM | 8 | 0.058 | **0.797** | 0.275 | **0.913** | 0.174 | **0.886** | 0.14 | 0.01 |
| Gemini 3.7 Flash | SWE-bench | 7 | 0.156 | **0.843** | 0.361 | **0.940** | 0.233 | **0.917** | 0.16 | 0.47 |
| Gemini 3.7 Flash | ThoughtTrace | 8 | 0.020 | **0.689** | 0.190 | **0.819** | 0.113 | **0.774** | 0.09 | 0.05 |
| Gemini 3.7 Flash (high effort) | all | 46 | 0.114 | **0.781** | 0.380 | **0.898** | 0.275 | **0.866** | 0.10 | 0.17 |
| Gemini 3.7 Flash (high effort) | ALFRED | 8 | 0.182 | **0.630** | 0.575 | **0.850** | 0.442 | **0.794** | 0.04 | 0.01 |
| Gemini 3.7 Flash (high effort) | Mind2Web | 8 | 0.225 | **0.920** | 0.576 | **0.965** | 0.438 | **0.951** | 0.13 | 0.47 |
| Gemini 3.7 Flash (high effort) | PATHs | 7 | 0.026 | **0.782** | 0.231 | **0.902** | 0.145 | **0.872** | 0.12 | 0.05 |
| Gemini 3.7 Flash (high effort) | PRISM | 8 | 0.062 | **0.783** | 0.294 | **0.904** | 0.197 | **0.873** | 0.12 | 0.00 |
| Gemini 3.7 Flash (high effort) | SWE-bench | 7 | 0.163 | **0.900** | 0.362 | **0.956** | 0.266 | **0.940** | 0.14 | 0.46 |
| Gemini 3.7 Flash (high effort) | ThoughtTrace | 8 | 0.021 | **0.684** | 0.219 | **0.819** | 0.143 | **0.776** | 0.09 | 0.04 |

## Paired comparison per item

Difference = BrainCode − Hebrew on the same item (negative = BrainCode loses more). Wilcoxon signed-rank, two-sided, on the per-item differences.

| model | metric | pairs | BrainCode mean | Hebrew mean | difference (BC − HE) | median per-item difference | items where BrainCode is higher | Wilcoxon p |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash | BLEU | 46 | 0.103 | 0.770 | -0.666 | -0.725 | 0 of 46 | 2.8e-14 |
| Gemini 3.7 Flash | ROUGE-L | 46 | 0.355 | 0.893 | -0.539 | -0.625 | 1 of 46 | 5.7e-14 |
| Gemini 3.7 Flash | word-Levenshtein similarity | 46 | 0.242 | 0.860 | -0.617 | -0.706 | 0 of 46 | 2.8e-14 |
| Gemini 3.7 Flash (high effort) | BLEU | 46 | 0.114 | 0.781 | -0.667 | -0.720 | 0 of 46 | 2.8e-14 |
| Gemini 3.7 Flash (high effort) | ROUGE-L | 46 | 0.380 | 0.898 | -0.518 | -0.590 | 0 of 46 | 2.8e-14 |
| Gemini 3.7 Flash (high effort) | word-Levenshtein similarity | 46 | 0.275 | 0.866 | -0.591 | -0.654 | 0 of 46 | 3.5e-09 |

## Corpus BLEU

| model | pairs | corpus BLEU, BrainCode | corpus BLEU, Hebrew |
|---|---:|---:|---:|
| Gemini 3.7 Flash | 46 | 0.034 | 0.754 |
| Gemini 3.7 Flash (high effort) | 46 | 0.041 | 0.749 |
