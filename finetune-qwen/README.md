# Fine-tune Qwen 2.5 7B on BrainCode, evaluate on ProofWriter

Does a Qwen 2.5 fine-tuned on BrainCode reason better from a BrainCode translation of a problem than plain Qwen 2.5 does from the English problem?

**Benchmark.** ProofWriter, open-world assumption (OWA), test split of the depth-5 dataset (`tasksource/proofwriter`). It has 70 items:
- 35 questions of proof depth 3 and 35 of depth 4;
- gold labels True / False / Unknown, 12 / 12 / 11 within each depth;
- one question per theory.

The items are in `evaluations/proofwriter/sample.jsonl`.

## The four phases

| # | Phase | Where | Command |
|---|---|---|---|
| 1 | Fine-tune Qwen 2.5 7B Instruct (LoRA) on the validated BrainCode translations | Colab | notebook, Part 1 |
| 2 | Gemini translators (`gemini-flash-3.7`, the swarm's setup: compact spec, glossary g19, RAG, kit, host check) translate the 70 items | local, Docker + vertex proxy | `pw.py setup`, `pw.py translate` |
| 3 | Baseline: plain Qwen 2.5 answers the English items | Colab | notebook, `baseline` |
| 4a | The fine-tuned Qwen solves the successful translations and ends with its conclusion in BrainCode | Colab | notebook, `braincode_ft` |
| 4b | Gemini back-translators read that conclusion (the last BrainCode block only) and turn it into English plus a verdict | local, Docker + vertex proxy | `pw.py backtranslate` |

Phases 1 and 2 are independent; run them in either order. Phases 3 and 4a need phase 2's translations, packaged into `benchmark/`.

## Step by step

```sh
# phase 2 (local; Docker Desktop running, PROXY_API_KEY in swarm/.env)
cd evaluations/proofwriter
python pw.py sample            # done: sample.jsonl is frozen
python pw.py setup             # done: runs/proofwriter has glossary g19 and needs + retrieval for each item
python pw.py translate         # 70 Gemini translator runs (resumable)
python pw.py status
python pw.py package           # -> finetune-qwen/benchmark/

# Colab folder
python finetune-qwen/build_folder.py   # done: data/ (566 translations, as in the Llama run) and braincode_kit/
#   zip finetune-qwen/ as finetune-qwen.zip, upload it to MyDrive, open finetune_qwen_braincode.ipynb
#   Part 1 (phase 1), restart, Part 2 (phases 3 and 4a); download outputs/runs.zip

# phase 4b and the analysis (local)
#   unzip runs.zip into evaluations/proofwriter/runs/   (runs/<condition>/<item>/r<k>/)
python pw.py backtranslate
python pw.py analyze           # -> results/proofwriter.md, results/proofwriter_runs.csv
```

## Design decisions

- **Same instructions in every condition.** Every prompt carries the same open-world rule: True if the theory implies the statement, False if it implies the negation, Unknown otherwise. English runs end with `The answer is: True|False|Unknown`.
- **The fine-tuned model's input** is the BrainCode only, never the English. Its system prompt has the compact spec and the glossary entries the translation uses. It reasons in any form, then writes one self-contained BrainCode block. The block rebuilds the statement and states a `CLAIM BY "solver" STATUS inferred` verdict: the statement holds, its negation holds, or neither can be established.
- **The relevant part** is that final block. The back-translator sees only the block and the English statement in question, never the theory, so it cannot solve the problem itself. It writes the conclusion in English and reports `Verdict: True|False|Unknown|None`. A response without a block, or with verdict None, is scored wrong.
- **Fine-tuning data.** These are the Llama run's 566 validated g19 translations; ProofWriter is not among them. With `READ_DIRECTION = True` (the default), each translation is also trained in reverse, BrainCode → English, because phase 4 asks the model to read BrainCode. Set it to `False` for write-only training, as in the Llama run.
- **Sampling.** Qwen 2.5's own defaults: temperature 0.7, top-p 0.8, top-k 20, repetition penalty 1.05. There are 3 runs per item and condition.
- **One translation per item** by default (`--runs 1`). Its success rate is reported as the phase-2 result.

## What `analyze` reports

- Translation success rate by depth.
- **Paired comparison** on the successfully translated items: accuracy by depth with Wilson CIs, the accuracy difference, exact McNemar on per-item majority votes, and an item-clustered GEE.
- **Intention to treat** on all 70 items: an untranslated item counts as wrong for the BrainCode conditions, so the whole pipeline is measured.
- Accuracy by gold label, and the prediction distribution (a bias toward "Unknown" is common at depth ≥ 3).

Two optional controls separate the effects:
- `braincode_base`: the plain model on BrainCode. Is a gain due to fine-tuning, or to the representation alone?
- `baseline_ft`: the fine-tuned model on English. Did fine-tuning change plain reasoning?
