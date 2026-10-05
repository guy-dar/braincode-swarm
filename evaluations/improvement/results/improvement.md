# Improvement: BBEH mini, Llama 3.1 8B Instruct, baseline vs BrainCode

50 items (23 tasks). Scoring: BBEH's evaluate.py. Errored runs left out: none.

## Accuracy (all runs)

| condition | runs | correct | accuracy | 95% CI (Wilson) |
|---|---:|---:|---:|---|
| Baseline | 150 | 18 | 12.0% | 7.7%–18.2% |
| BrainCode first (in-context) | 150 | 1 | 0.7% | 0.1%–3.7% |

## BrainCode first (in-context) vs baseline (50 paired items)

McNemar, exact, on the per-item majority vote over runs:

| | BrainCode first (in-context) correct | wrong |
|---|---:|---:|
| baseline correct | 0 | 5 |
| baseline wrong | 0 | 45 |

Discordant pairs: 5 baseline-only vs 0 braincode-only; exact p = 0.0625.

- Mixed-effects logistic model `correct ~ condition + (1 | item)`: effect (log-odds) -3.096 (posterior SD 0.737); odds ratio 0.05 (≈95% interval 0.01–0.19); item random-effect SD 1.59
- GEE check (item-clustered): log-odds -3.012, p = 0.0014

One model and one benchmark, so the model and benchmark terms of the design formula (`Correct ~ condition + model + benchmark + condition × model + (1|item)`) drop out.

## Accuracy per task

| task | Baseline | BrainCode first (in-context) |
|---|---:|---:|
| boardgame qa | 17% | 0% |
| boolean expressions | 0% | 0% |
| buggy tables | 0% | 0% |
| causal understanding | 17% | 0% |
| disambiguation qa | 83% | 17% |
| dyck languages | 0% | 0% |
| geometric shapes | 0% | 0% |
| hyperbaton | 0% | 0% |
| linguini | 0% | 0% |
| movie recommendation | 17% | 0% |
| multistep arithmetic | 0% | 0% |
| nycc | 33% | 0% |
| object counting | 0% | 0% |
| object properties | 0% | 0% |
| sarc triples | 50% | 0% |
| shuffled objects | 22% | 0% |
| spatial reasoning | 0% | 0% |
| sportqa | 0% | 0% |
| temporal sequence | 0% | 0% |
| time arithmetic | 17% | 0% |
| web of lies | 0% | 0% |
| word sorting | 11% | 0% |
| zebra puzzles | 17% | 0% |

## Diagnostics

- Baseline: answers with the required prefix 79%; cost $0.013
- BrainCode first (in-context): answers with the required prefix 98%; translations with a braincode block 54%; cost $0.200
