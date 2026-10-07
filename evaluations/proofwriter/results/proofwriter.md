# ProofWriter (OWA, depth-5 test, proof depth 3/4): Qwen 2.5 vs fine-tuned Qwen 2.5 on BrainCode

70 items (35 per depth, labels balanced). Translator: gemini-flash-3.7; back-translator: gemini-flash-3.7. Errored runs left out: none; awaiting back-translation: {'braincode_base': 83, 'braincode_ft': 201}.

## Phase 2: translation

| depth | items | successful translations | rate |
|---|---:|---:|---:|
| 3 | 35 | 35 | 100% |
| 4 | 35 | 32 | 91% |
| all | 70 | 67 | 96% |

## Accuracy on the successfully translated items (the paired comparison)

67 items: every condition answers the same items. Cells: accuracy (runs).

| condition | depth 3 | depth 4 | all | 95% CI (Wilson) |
|---|---:|---:|---:|---|
| Qwen 2.5, English (baseline) | 50.5% (105) | 58.3% (96) | 54.2% (201) | 47.3%–61.0% |
| Fine-tuned Qwen 2.5, BrainCode → English answer | 29.5% (105) | 24.0% (96) | 26.9% (201) | 21.2%–33.4% |
| Qwen 2.5, BrainCode → BrainCode verdict (no fine-tuning) | 42.9% (105) | 69.2% (13) | 45.8% (118) | 37.0%–54.7% |
| Qwen 2.5, BrainCode → English answer (no fine-tuning) | 54.3% (105) | 38.5% (96) | 46.8% (201) | 40.0%–53.7% |
| Fine-tuned Qwen 2.5, English | 41.0% (105) | 43.8% (96) | 42.3% (201) | 35.7%–49.2% |
| Gemini 3.7 Flash, English (solvability reference) | 94.3% (35) | 100.0% (32) | 97.0% (67) | 89.8%–99.2% |
| Gemini 3.7 Flash, BrainCode → English answer (solvability) | 91.4% (35) | 90.6% (32) | 91.0% (67) | 81.8%–95.8% |

## Accuracy on all items (intention to treat)

An item without a successful translation counts as wrong for the BrainCode conditions: the whole pipeline is measured, translation included.

| condition | depth 3 | depth 4 | all | 95% CI (Wilson) |
|---|---:|---:|---:|---|
| Qwen 2.5, English (baseline) | 50.5% (105) | 59.0% (105) | 54.8% (210) | 48.0%–61.3% |
| Fine-tuned Qwen 2.5, BrainCode → English answer | 29.5% (105) | 21.9% (105) | 25.7% (210) | 20.3%–32.0% |
| Qwen 2.5, BrainCode → BrainCode verdict (no fine-tuning) | 42.9% (105) | 40.9% (22) | 42.5% (127) | 34.3%–51.2% |
| Qwen 2.5, BrainCode → English answer (no fine-tuning) | 54.3% (105) | 35.2% (105) | 44.8% (210) | 38.2%–51.5% |
| Fine-tuned Qwen 2.5, English | 41.0% (105) | 44.8% (105) | 42.9% (210) | 36.4%–49.6% |
| Gemini 3.7 Flash, English (solvability reference) | 94.3% (35) | 100.0% (32) | 97.0% (67) | 89.8%–99.2% |
| Gemini 3.7 Flash, BrainCode → English answer (solvability) | 91.4% (35) | 90.6% (32) | 91.0% (67) | 81.8%–95.8% |

## Fine-tuned Qwen 2.5, BrainCode → English answer vs baseline (paired, 67 items)

Accuracy difference -27.4% (percentage points, all runs). McNemar, exact, on the per-item majority vote over runs:

| | braincode_ft_english correct | wrong |
|---|---:|---:|
| baseline correct | 14 | 21 |
| baseline wrong | 6 | 26 |

Discordant pairs: 21 baseline-only vs 6 braincode_ft_english-only; exact p = 0.0059.
GEE (item-clustered logistic): log-odds -1.171, p = 0.0000.

## Qwen 2.5, BrainCode → BrainCode verdict (no fine-tuning) vs baseline (paired, 67 items)

Accuracy difference -8.5% (percentage points, all runs). McNemar, exact, on the per-item majority vote over runs:

| | braincode_base correct | wrong |
|---|---:|---:|
| baseline correct | 10 | 25 |
| baseline wrong | 9 | 23 |

Discordant pairs: 25 baseline-only vs 9 braincode_base-only; exact p = 0.0090.
GEE (item-clustered logistic): log-odds -0.317, p = 0.2790.

## Qwen 2.5, BrainCode → English answer (no fine-tuning) vs baseline (paired, 67 items)

Accuracy difference -7.5% (percentage points, all runs). McNemar, exact, on the per-item majority vote over runs:

| | braincode_base_english correct | wrong |
|---|---:|---:|
| baseline correct | 15 | 20 |
| baseline wrong | 16 | 16 |

Discordant pairs: 20 baseline-only vs 16 braincode_base_english-only; exact p = 0.6177.
GEE (item-clustered logistic): log-odds -0.299, p = 0.2157.

## Fine-tuned Qwen 2.5, English vs baseline (paired, 67 items)

Accuracy difference -11.9% (percentage points, all runs). McNemar, exact, on the per-item majority vote over runs:

| | baseline_ft correct | wrong |
|---|---:|---:|
| baseline correct | 20 | 15 |
| baseline wrong | 7 | 25 |

Discordant pairs: 15 baseline-only vs 7 baseline_ft-only; exact p = 0.1338.
GEE (item-clustered logistic): log-odds -0.480, p = 0.0076.

## Gemini 3.7 Flash, English (solvability reference) vs baseline (paired, 67 items)

Accuracy difference +42.8% (percentage points, all runs). McNemar, exact, on the per-item majority vote over runs:

| | gemini_english correct | wrong |
|---|---:|---:|
| baseline correct | 35 | 0 |
| baseline wrong | 30 | 2 |

Discordant pairs: 0 baseline-only vs 30 gemini_english-only; exact p = 0.0000.
GEE (item-clustered logistic): log-odds +3.312, p = 0.0000.

## Gemini 3.7 Flash, BrainCode → English answer (solvability) vs baseline (paired, 67 items)

Accuracy difference +36.8% (percentage points, all runs). McNemar, exact, on the per-item majority vote over runs:

| | gemini_braincode correct | wrong |
|---|---:|---:|
| baseline correct | 32 | 3 |
| baseline wrong | 29 | 3 |

Discordant pairs: 3 baseline-only vs 29 gemini_braincode-only; exact p = 0.0000.
GEE (item-clustered logistic): log-odds +2.150, p = 0.0000.

## BrainCode conditions: English answer (call 1) vs BrainCode verdict (call 2)

The model reasons in English from the BrainCode problem and ends with an answer (call 1), then writes that decision as a BrainCode verdict block, which a Gemini back-translator reads (call 2). *Usable* = the back-translator found a True/False/Unknown verdict; *agrees* = the verdict says what the English answer said.

| condition | runs | English answer accuracy | BrainCode verdict accuracy | verdict block written | verdict usable | verdict agrees with English answer |
|---|---:|---:|---:|---:|---:|---:|
| braincode_ft | 201 | 27% | — | 100% | — | — |
| braincode_base | 201 | 47% | 46% | 100% | 70% | 84% |

## Accuracy by gold label (translated items)

| condition | True | False | Unknown |
|---|---:|---:|---:|
| Qwen 2.5, English (baseline) | 41% | 50% | 73% |
| Fine-tuned Qwen 2.5, BrainCode → English answer | 6% | 11% | 65% |
| Qwen 2.5, BrainCode → BrainCode verdict (no fine-tuning) | 67% | 33% | 31% |
| Qwen 2.5, BrainCode → English answer (no fine-tuning) | 65% | 39% | 35% |
| Fine-tuned Qwen 2.5, English | 29% | 23% | 76% |
| Gemini 3.7 Flash, English (solvability reference) | 100% | 100% | 91% |
| Gemini 3.7 Flash, BrainCode → English answer (solvability) | 83% | 100% | 91% |

## Predictions (translated items)

| condition | true | false | unknown | other |
|---|---:|---:|---:|---:|
| Qwen 2.5, English (baseline) | 42 | 42 | 117 | 0 |
| Fine-tuned Qwen 2.5, BrainCode → English answer | 9 | 12 | 150 | 30 |
| Qwen 2.5, BrainCode → BrainCode verdict (no fine-tuning) | 48 | 17 | 18 | 35 |
| Qwen 2.5, BrainCode → English answer (no fine-tuning) | 88 | 40 | 60 | 13 |
| Fine-tuned Qwen 2.5, English | 34 | 20 | 135 | 12 |
| Gemini 3.7 Flash, English (solvability reference) | 24 | 23 | 20 | 0 |
| Gemini 3.7 Flash, BrainCode → English answer (solvability) | 19 | 24 | 24 | 0 |
