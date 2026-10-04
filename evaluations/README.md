# BrainCode evaluations

Implements `evaluations.docx`: **coverage**, **determinism** and **expressivity** of BrainCode as produced by the swarm,
measured on unseen test items with six models translating under exactly the swarm translators' setup.

| Company | Strong | Weak | Route | Items × runs |
|---|---|---|---|---|
| Gemini | Gemini 3.7 Flash, high effort (stands in for 3.1 Pro) | Gemini 3.7 Flash (the swarm's own model) | vertex proxy (`PROXY_API_KEY`) | 48 × 3 |
| Claude | Claude Opus 5.5 | Claude Haiku 4.5 | Anthropic API (`CLAUDE_API_KEY`) | 18 × 3 |
| OpenAI | GPT-6 Astra | o4-mini | OpenAI API (`OPENAI_API_KEY` / `OPENAI_API_KEY_PERSONAL`) | 18 × 3 |

The 18 items are a stratified subset of the 48 (3 per dataset), so every model is compared on the same items.
Expressivity runs only for the Gemini models. Gemini 3.1 Pro is not served by the vertex proxy (`gemini-3.1-pro-preview` is
rejected as an invalid model name), so the strong Gemini is `gemini-flash-high`: the same 3.7 Flash at high
reasoning effort. The Gemini pair therefore contrasts reasoning effort, not model size; state this in the paper.

## Setup shared by every model

- **Sample** (`sample.py` → `sample.jsonl`, frozen): test splits only; the same stratification as the swarm's plan
  (`swarm/loop.py` `STRATIFY_KEYS`); items of at most 6,000 characters; 8 per dataset.
- **Frozen release:** `run_eval.py setup` copies the reference files (spec, compact spec, glossary g19 at the time of
  writing) into `runs/<run>/reference/` and serves a private RAG server from that copy, on port 8775.
- **Identical inputs:** each item's needs are extracted once (Gemini 3.7 Flash) and its retrieval context is rendered
  once. Every model and every run gets the same `rag_context.md`, `needs.json`, attachments, kit, formats and
  translator prompt (`swarm/tasks/translator.md`). The context-limits extension, timeout and host success gate are the
  swarm's too.
- **Keys:** keys reach containers by name only (`docker run -e NAME`), never as values.

## Running

```sh
python sample.py                                   # once (refuses to overwrite)
python run_eval.py setup --run main                # freeze reference, needs and contexts for the sample
python run_eval.py translate --run main            # all models (resumable; --models a,b; --max-usd per model)
python run_eval.py backtranslate --run main        # expressivity (Gemini models)
python run_eval.py status --run main
python analyze.py --run main                       # tables and figures -> results/main/
python qualitative.py --run main                   # Claude's qualitative report -> results/main/qualitative.md
```

Run outputs are in `runs/<run>/<model>/<item>/r<k>/`:
- `translation.md` (and `suggestions.md` when the translation failed), plus `check.json` from the host check;
- `result.json`: status, attempts, time, tokens and cost;
- `session.jsonl`: the full conversation (view it with `swarm/show_session.py`);
- `attempt<N>.log` and `back/` (the reconstruction).

## Measures

**Coverage.** The success rate is the share of runs whose translation passes the host gate with `Status: success`. For
a failed translation, the number of *missing symbols* is the number of distinct symbols its `add` suggestions
introduce, or, without suggestions, its distinct `# PROPOSED: S<k>` markers.

**Symbol distributions.** For a translation, count every occurrence in its BrainCode of a glossary symbol, and every
value-group atom `g::k`. Comments, quoted literals and grammar tokens are excluded. The *type* of a symbol is its
glossary kind (`operation`, `constructor`, `claim_relation`, `value`, …), or `group_value` for an atom. P(symbol |
model) and P(type | model) are these counts pooled over all of a model's translations of the shared items,
normalized.

**Jensen-Shannon divergence** (base 2, range [0, 1], 0 = identical):

$$\mathrm{JS}(P\,\|\,Q) = \tfrac12 \sum_x P(x)\log_2\frac{P(x)}{M(x)} + \tfrac12 \sum_x Q(x)\log_2\frac{Q(x)}{M(x)},\qquad M = \tfrac12(P+Q)$$

Model pairs: weak vs strong of the same company; weak vs weak and strong vs strong across companies.

**Same-model divergence.** For item *i* with runs *r₁, r₂, r₃*:
D_i = mean{JS(P_{r₁}, P_{r₂}), JS(P_{r₁}, P_{r₃}), JS(P_{r₂}, P_{r₃})}. The model's value is the arithmetic mean of
D_i over items. The share of identical run pairs (JS = 0) is reported next to it.

**Expressivity** compares the original item *x* with the reconstruction *y* (BrainCode → natural language by the same
model, which never sees *x*). Both are lower-cased and tokenized into words, with turn markers removed. Every score is
in [0, 1], and **higher = more similar = better**:

- BLEU (Papineni et al., 2002), sentence-level with exponential smoothing (sacrebleu), and corpus-level:
  $\mathrm{BLEU} = \mathrm{BP}\cdot\exp\big(\sum_{n=1}^{4}\tfrac14\log p_n\big)$, where $p_n$ is the modified n-gram
  precision and the brevity penalty is $\mathrm{BP}=\min(1, e^{1-|x|/|y|})$.
- ROUGE-L F1 (Lin, 2004): with $L=\mathrm{LCS}(x,y)$, $R=L/|x|$, $P=L/|y|$, $F_1 = 2PR/(P+R)$.
- Word-level Levenshtein similarity: $1 - d_w(x,y)/\max(|x|,|y|)$, where $d_w$ is the minimum number of word
  insertions, deletions and substitutions turning *x* into *y*.

## Outputs (`results/<run>/`)

Every figure has a table next to it:

- **Coverage:** `coverage.md`/`.csv`, `coverage_radar_shared.png` (one subplot per company, both models overlaid, one
  axis per dataset), `coverage_radar_gemini.png`.
- **Determinism:** `determinism.md`, `determinism_pairs.csv`, `determinism_self.csv`, `js_heatmap_symbols.png`,
  `js_heatmap_types.png`, `self_divergence.png`, `self_divergence_by_dataset.png`, `symbol_type_mix.png`,
  `determinism_vs_coverage.png`.
- **Expressivity:** `expressivity.md`/`.csv`, `expressivity.png`.
- **Qualitative:** `qualitative.md` and the evidence it was given, `qualitative_evidence.json`.
