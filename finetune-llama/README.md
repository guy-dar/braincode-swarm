# Fine-tune Llama 3.1 8B on BrainCode (Google Colab)

This folder is self-contained. Upload it to Google Drive, open the notebook in Colab, and run it top to bottom.

## What's here

| Path | What it is |
|---|---|
| `finetune_llama_braincode.ipynb` | The notebook. Part 1 fine-tunes; Part 2 serves the model and runs the benchmark. |
| `data/train.jsonl`, `data/val.jsonl` | 535 / 31 training examples: a task (`item`) and its BrainCode (`braincode`). Validation items are disjoint from training items. |
| `data/translations/` | The full successful translation documents the examples come from, by source and dataset. |
| `data/manifest.json` | Counts by source, dataset and model, and what was filtered out and why. |
| `run_braincode_agentic.py` | Runs the 50 BBEH-mini items in the agentic BrainCode setup against an OpenAI-compatible endpoint, scored with BBEH's scorer. |
| `braincode_kit/` | BrainCode glossary g19, the compact spec, value-group standards, the swarm's retrieval and checker code, and its prebuilt search index. |
| `benchmark/` | The 50 sampled BBEH-mini items (`sample.jsonl`) and the glossary entries retrieved for each (`items/<key>/rag_context.md`). These are the same items and retrieved entries as the in-context runs. |
| `build_folder.py` | Rebuilds `data/`, `braincode_kit/` and `benchmark/` from the repository; run locally, not in Colab. |

## The training data

The data is every successful translation that still passes today's checker against glossary g19. Any example that fails one of these checks was dropped:
- no unknown symbols;
- no invalid or retired group values;
- no quoted string of 8+ words outside names and titles;
- no needs marked opaque.

Identical BrainCode is kept once. That leaves 566 examples:
- **Swarm translations:** 232, written by Gemini Flash.
- **Evaluation translations:** 334, from Gemini, Claude and o4-mini.

The median example is about 1.2k tokens.

**Contamination warning.** The evaluation's translations come from the datasets' *test* splits. A model tuned on them must not be scored again on those evaluation items (coverage, determinism, expressivity). The BBEH benchmark is not in the training data.

## Steps

1. **Upload this folder to Drive** at `MyDrive/finetune-llama`. Remove `braincode_kit/rag/models/` and `runs/` first if they exist: they're local test leftovers, and the embedding model downloads itself in Colab.
2. **Open the notebook in Colab.** Use `File → Upload notebook`, or open it from Drive.
3. **Choose a GPU runtime:** `Runtime → Change runtime type → GPU`. An A100 is best; an L4 works. A T4 (free tier) also works: the notebook then trains and serves the pre-quantized 4-bit model with a 16k-token context and caps tool outputs, so the agent sees less of the spec and glossary at once than on an A100.
4. **Run Part 1, about 10–25 minutes.** It installs Unsloth, fine-tunes a LoRA adapter, and saves it to `MyDrive/finetune-llama/outputs/braincode-llama-lora`. It also translates one held-out item and runs the checker on it.
5. **Restart the session:** `Runtime → Restart session`.
6. **Run Part 2.** It installs vLLM and serves your adapter on top of Llama 3.1 8B Instruct as `braincode-llama`. It then runs a 2-item smoke test, followed by the full benchmark of 50 items × 3 runs.
7. **Optional control:** the fine-tuned model without BrainCode (`baseline_ft`).
8. **Download the results:** `MyDrive/finetune-llama/outputs/runs.zip`.

## The agentic benchmark flow

For each item and run:
1. **Translate.** The model sees the task and has these tools:
   - `read_spec`: the language specification;
   - `get_retrieved_context`: the glossary entries retrieved for this item, with the value-group catalog, the same entries as the in-context runs;
   - `search_glossary`: the swarm's hybrid keyword and embedding search;
   - `glossary_entries`: full glossary records;
   - `check_braincode`: the swarm's checker;
   - `submit_braincode`.
2. **Solve.** In a new conversation the model sees only its BrainCode, never the task text, plus the same reading tools. It answers with `The answer is: …`.

The answer is scored with BBEH's own `evaluate.py` logic. Each run is saved in `runs/<condition>/<item>/r<k>/`:

| File | What it is |
|---|---|
| `result.json` | Status, prediction, correctness and token counts |
| `translation.md` | The BrainCode the model submitted |
| `response.md` | The model's final answer |
| `transcript.json` | Every message and tool call |

Llama 3.1 sometimes writes tool calls as text, `<function=name>{...}</function>`, instead of structured calls. The runner understands both forms. Errored runs are redone when you rerun the cell; finished runs are kept.

## After fine-tuning: using the model

The adapter is a small set of weights (about 170 MB) that sits on top of `meta-llama/Llama-3.1-8B-Instruct`. Ways to use it:

- **In Colab, as in Part 2.** Run `vllm serve unsloth/Meta-Llama-3.1-8B-Instruct --enable-lora --lora-modules braincode-llama=<adapter dir> --max-lora-rank 16 …` and send any OpenAI-compatible request with `model: "braincode-llama"`. You can point `run_braincode_agentic.py`, or your own code, at `http://localhost:8000/v1`.
- **On the Hugging Face Hub.** Set `PUSH_TO_HUB = True` in Part 1 to upload the adapter to a private repository. This needs the Colab secret `HF_TOKEN` with write permission. Anyone with access can load it with `peft` or Unsloth on top of the base model.

  Hugging Face's Inference Providers, the API used for the in-context runs, serve only base models. To call the tuned model as an API, deploy a **Hugging Face Inference Endpoint**, paid per hour, from the adapter repo, or serve it with vLLM on any GPU machine.
- **As one merged model.** In Part 1, after training, `model.save_pretrained_merged('/content/merged', tokenizer, save_method='merged_16bit')` writes standalone 16-bit weights (about 16 GB, too big for a free Drive). `model.save_pretrained_gguf('/content/gguf', tokenizer, quantization_method='q4_k_m')` writes a GGUF file (about 5 GB) for running locally with llama.cpp or Ollama.

## Bringing the results back into the repository

1. Unzip `runs.zip`.
2. Copy its condition folders into `evaluations/improvement/runs/`:
   - `braincode_agentic_ft`;
   - optionally `baseline_ft`.

   The `baseline/` and `braincode/` folders are already there; don't overwrite them.
3. Run:

   ```
   python evaluations/improvement/improve.py analyze
   ```

`results/improvement.md` then reports every condition against the baseline:
- accuracy with 95% CIs;
- exact McNemar on per-item majority votes;
- the mixed-effects logistic model `correct ~ condition + (1|item)`, with a GEE check;
- accuracy per task, and two figures.
