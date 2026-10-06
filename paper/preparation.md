# BrainCode paper: evidence map and preparation

Prepared 6 October 2026 from the local repository. This is a research preparation note, not the requested manuscript. The outline and grading materials must be read before the section structure, coverage checklist, and manuscript can be finalized.

## Required sources and access

| Source | Status |
|---|---|
| [User's outline](https://docs.google.com/document/d/1AUCIFR_vfPusXW4_H4L2sRcQneHCl7ZFGaLgtg6Cn1Y/edit?tab=t.0) | Google Docs connector returned permission denied; metadata returned not found. Browser requires sign-in. No outline bullets have been read or checked off. |
| Grading guidelines | No attachment was exposed in this chat or identified in the project folders inspected. Required before a grading-compliance review. |
| Styling reference papers | Not available in the chat. Required before choosing the final paper format and citation style. |
| Attached evaluation and infrastructure adaptations documents | Not available in the chat. Repository evaluation reports are available, but are not assumed to be the requested attachments. |
| [Target Overleaf project](https://www.overleaf.com/project/6ac42bd90c3bcd58a59ac132) | Browser displayed a restricted-access page while signed out. No project files were changed. |
| Original proposal and meeting notes | Read from `C:/projects/BrainCode/instructions/`. Useful background, not substitutes for the outline or rubric. |

The connected Drive account is `lia.soffer@gmail.com`. The user has been asked for access to the outline and links or local paths for the missing supporting material.

## Provisional space allocation

This is an eight-page working budget, **not a reconstruction of the inaccessible outline**. Replace the headings and redistribute space after reading that document. Allocations include tables and figures. Typesetting must establish the actual page count.

| Content | Estimated pages |
|---|---:|
| Title and abstract | 0.50 |
| Introduction and research questions | 0.75 |
| Related work | 0.75 |
| BrainCode representation and worked example | 0.75 |
| Language construction: syntax debate, vocabulary swarm, infrastructure | 1.25 |
| Evaluation design and operational definitions | 1.00 |
| Quantitative and qualitative results | 2.00 |
| Discussion, limitations, and future work | 0.75 |
| Conclusion | 0.25 |
| **Main text total** | **8.00** |

Start the AI disclosure on a new page after the main text. Keep it and subsequent back matter outside the eight-page count, subject to the actual grading instructions. The disclosure should distinguish AI-assisted language development, AI-generated qualitative analyses, and AI assistance in preparing the manuscript. Do not claim that the authors completed checks they have not performed.

## Research argument supported by the current evidence

The project builds an explicitly documented language through a human-steered syntax process and an iterative vocabulary expansion process. Its evidence supports the feasibility of that development workflow and relatively high operational translation coverage for some models. It does not yet establish canonical representations, faithful semantic preservation, human interpretability, or improved downstream reasoning.

The central distinction for the manuscript is between **passing the translation checker**, **preserving task meaning**, and **improving task performance**. These are different outcomes. The current results should be presented as a mixed empirical picture rather than a single success claim.

## Source map

All paths below are relative to `C:/projects/braincode-swarm/`, unless marked otherwise.

| Paper content | Primary implementation or artifact | Writing notes |
|---|---|---|
| Motivation and original aims | `swarm/reference/purpose.md`; original `C:/projects/BrainCode/instructions/Project Proposal.pdf` | Coverage, expressivity, determinism, improvement, interpretability. Proposal authors are Lia Soffer, Noam Yehezkel, and Simon Wasser; mentor is Guy Dar. Author order and affiliation still need confirmation from the outline/template. Do not reproduce student IDs from the proposal. |
| Syntax construction | `syntax-loop/README.md`, `syntax-loop/config/config.yaml`, `syntax-loop/braincode_loop/orchestrator.py`, `decision.py`, `doc_hygiene.py` | Searcher, Shaper, Critic, Documenter; steering notes, bounded rework, examples, documentation. Pre-KPI judgments are qualitative, not powered statistical tests. Configuration defaults do not prove the exact historical model used in a run. |
| Human steering and development history | `syntax-loop/steering/notes.md`, `syntax-loop/docs/changelog.md`, `backlog.md`, `notes-status.json`, `syntax-loop/runs/logs/` | Extract the episodes requested by the outline; inspect their underlying run artifacts before claiming a historical sequence. |
| Language | `swarm/reference/language-spec.md`, `language-spec.compact.md`, `glossary.jsonl`, `reference-manifest.json` | Current manifest identifies `19.0.0-draft.2-lexical-groups+g19`. The glossary source of truth is JSONL; the Markdown glossary is a rendered view. |
| Vocabulary growth | `swarm/loop.py`, `translate_batch.py`, `migrate.py`, `inspector.py`, `tasks/translator.md` | Translation failure supplies additions/refinements, migration consolidates and validates operations, retrieval is rebuilt. Human changes and lexical-group consolidation occurred during development. |
| Retrieval and translator infrastructure | `swarm/kit/README.md`, `swarm/rag/`, `swarm/throttle.py`, `swarm/harnesses/`, `swarm/doc_formats/` | Source-linked needs, keyword and embedding retrieval, dependency expansion, frozen references, isolated translator runs. Match this account to the missing infrastructure adaptations document. |
| Data construction | `swarm/data/README.md`, `swarm/fetch_datasets.py`, `swarm/loop.py` | Local stratified 80/20 splits, seed 42. Dataset report totals 42,180 records. ALFRED split groups annotations by trial. SWE-bench is the full dataset, not Verified. |
| Evaluation sampling | `evaluations/sample.py`, `evaluations/sample.jsonl`, `evaluations/runs/main/items.jsonl` | 48 items, eight per dataset; 18 shared items, three per dataset; maximum 6,000 characters; seed 2026; three forward runs per item. |
| Evaluation setup | `evaluations/run_eval.py`, `evaluations/models.json`, `evaluations/runs/main/reference/`, `evaluations/runs/main/items/` | Frozen reference files and identical precomputed needs/retrieval per item. Use run evidence and model configuration over stale README model labels. |
| Coverage and failure diagnostics | `evaluations/results/main-cov-det/coverage.csv`, `coverage.md`, `failures.csv`; raw `evaluations/runs/main/*/*/r*/result.json` and `check.json` | Denominator includes success, failure, and error. Report each separately. |
| Determinism | `evaluations/metrics.py`, `analyze.py`; `results/main-cov-det/determinism_self.csv`, `determinism_pairs.csv` | Jensen-Shannon divergence of symbol histograms and type histograms. These are distributional measures, not expression identity or semantic equivalence. |
| Expressivity | `evaluations/run_eval.py`, `metrics.py`, `analyze.py`; `results/main-cov-det/expressivity.csv` | Same-model round trips; one usable forward result per item. BLEU, ROUGE-L, and word edit similarity measure textual overlap. |
| Qualitative evidence | `evaluations/results/main-cov-det/qualitative_determinism_js.md`, `qualitative_expressivity_bleu_rouge_levenshtein.md`, adjacent evidence JSON files | Reports identify Claude Opus as their author. Treat model-generated interpretations as candidate analyses; verify examples against the source and reconstructed text. |
| Downstream reasoning | `evaluations/improvement/improve.py`, `sample.jsonl`, `results/improvement.md`, `runs/` | Llama 3.1 8B Instruct, 50 BBEH-mini items from 23 tasks, three runs per condition. |
| Fine-tuning | `finetune-llama/README.md`, `data/manifest.json`, `finetune_llama_braincode.ipynb`, `run_braincode_agentic.py` | Prepared training and benchmark setup. No completed fine-tuned benchmark results were found in either expected local results location. |

## Quantitative checks against raw records

The completed forward evaluation conditions contain **450 runs**: two Gemini settings with 144 each and three other models with 54 each. Cross-model comparisons use **270 runs on 18 shared items**. Two additional interrupted GPT conditions have 45 stored runs in total and zero successes; they are excluded from the saved main comparison. Disclose their exclusion without presenting incomplete runs as a balanced comparison.

| Model label in saved experiment | Shared successes / total | Failed | Error | Shared success rate | All-sample successes / total |
|---|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash, high effort | 49/54 | 2 | 3 | 90.7% | 131/144 (91.0%) |
| Gemini 3.7 Flash | 46/54 | 4 | 4 | 85.2% | 128/144 (88.9%) |
| Claude Sonnet 5.5 | 24/54 | 30 | 0 | 44.4% | Same as shared |
| Claude Haiku 4.5 | 50/54 | 4 | 0 | 92.6% | Same as shared |
| o4-mini | 4/54 | 46 | 4 | 7.4% | Same as shared |

The Gemini pair changes reasoning effort on the same served model, not model size. The Claude comparison is non-monotonic with the assigned tier; do not interpret the tier labels as an experimentally demonstrated capability ordering. Proxy-facing identifiers are `vertex-proxy/gemini-flash` and `vertex-proxy/gemini-flash-high`.

For within-model symbol divergence on shared items, the saved means are 0.092, 0.114, 0.121, 0.173, and 0.330 in the table order above. At least two eligible runs exist for 17, 17, 18, 18, and 16 items, respectively. The Gemini pair's pooled symbol JS is 0.020; their type JS is approximately 0.001. Low histogram divergence cannot establish the same task decomposition or argument bindings.

There are **99 analyzed round-trip pairs**: 46 Flash, 46 high-effort Flash, and seven o4-mini. Raw records show:

| Model | Pairs from successful forward runs | Pairs from failed forward runs |
|---|---:|---:|
| Gemini 3.7 Flash | 45 | 1 |
| Gemini 3.7 Flash, high effort | 43 | 3 |
| o4-mini | 0 | 7 |

All-sample mean BLEU / ROUGE-L / word-Levenshtein similarity are 0.103 / 0.355 / 0.242 for Flash and 0.114 / 0.380 / 0.275 for high-effort Flash. The seven o4-mini pairs score 0.082 / 0.267 / 0.170. Their unequal and failure-conditioned sample makes a direct model ranking inappropriate. Shared Gemini rows each use 17 pairs; verify the actual intersection before any paired statistical comparison.

The vocabulary-development graph table reports 14 batches of 30 translators: **322 successes among 420 attempts**. Per-batch success rises from 5/30 to 30/30, with intervening declines. The glossary table begins at 329 live records, peaks at 685 after batch 10, and reports 678 after batch 13. The reduction around batch 11 coincides with representation changes. Do not equate accepted suggestions with net record growth, or treat a final development batch's 100% as a held-out result. These historical successes have not been re-evaluated here under the later checker.

For downstream reasoning, raw results confirm **18/150 correct baseline responses (12.0%)** and **1/150 BrainCode responses (0.67%)**. Saved item-level majority-vote counts are five baseline-only correct and zero BrainCode-only correct among 50 paired items; exact McNemar p = 0.0625. The saved analysis also reports an item-random-intercept Bayesian logistic estimate and an item-clustered GEE p = 0.0014. They answer different aggregation questions; do not select whichever p-value supports a preferred conclusion. Wilson intervals over all runs are descriptive and do not account for within-item dependence.

The fine-tuning manifest contains 566 retained translations from 279 distinct items: 535 training examples and 31 validation examples, including 334 evaluation-derived translations. The README states that validation items are disjoint from training items and warns against re-evaluation on the original language-evaluation items. Training completion and performance remain unverified.

## Interpretation and reproducibility issues to handle in the manuscript

1. **Local test split is not an unseen domain.** The six datasets contribute to both vocabulary development and evaluation. Mind2Web's upstream splits were pooled before local repartitioning; SWE-bench data are drawn from its training source. Describe held-out local items, not official benchmark test performance or demonstrated unseen-domain generalization. Broader leakage checks against syntax-development samples and legacy one-shot runs remain outstanding.
2. **Coverage is operational.** The checker verifies symbol use, value groups, declared needs, and fallback restrictions; it is not a semantic fidelity oracle. The earlier source-linked need extractor can itself miss information.
3. **The checker changed after some forward runs.** `cmd_regate` documents retrospective checks for opaque needs and long quoted literals. Report that this occurred. In the current raw records, seven errors in each Gemini condition are marked as re-gated. Current o4-mini records contain no `regated` markers, despite an older overview saying three remained; prefer current raw records and document the discrepancy.
4. **Determinism includes failures.** `analyze.py` includes statuses `success` and `failed`, excluding `error`. Partial outputs can distort both symbol distributions and cross-model comparisons. The qualitative report says this inclusion is unclear; the implementation resolves it.
5. **JS = 0 means identical histograms.** It does not imply identical ordering, structure, identifiers, or meaning. Label the corresponding statistic 'identical symbol distributions', not 'identical translations'.
6. **The implementation is weaker than the proposed KPI protocol.** The earlier `C:/projects/BrainCode/instructions/kpi-examination-plan.md` proposes cross-model reconstruction, paraphrase controls, semantic-equivalence tests, structured-format ablations, and human interpretability studies. The available run implements a smaller exploratory evaluation. Clearly distinguish intended design from completed evidence.
7. **Round-trip metrics conflate paraphrase and loss.** Same-model reconstruction cannot isolate information recoverable by an independent decoder. No paraphrase-only control was found. Preserve the qualitative examples of omitted quantities, negation changes, lost discourse, and language switching, after checking raw evidence.
8. **One qualitative report is truncated.** `qualitative_expressivity_bleu_rouge_levenshtein.md` ends mid-word ('paraphras'). Do not invent the missing analysis or present it as a complete report.
9. **Inference cost and treatment differ.** The Llama treatment uses a translation call followed by a new solve conversation and language context; baseline uses a direct solve call. Only 54% of treatment translations contain a recognized BrainCode block; otherwise the entire response is forwarded. This probes the deployed prompting pipeline, not ideal BrainCode or a compute-matched comparison.
10. **Fine-tuning changes the evaluation boundary.** Because the prepared training set uses language-evaluation test items, any tuned model needs a separate held-out evaluation. No claim of fine-tuning improvement can be made from the current files.
11. **Historical configurations require care.** READMEs and configuration comments name several planned or replaced models. Actual result files, sessions, and snapshot hashes are the strongest evidence for an experiment's identity.
12. **Inspector wording differs from the README.** Current code applies stopping thresholds to *accepted* additions/refinements, with a finished-run guard. Verify the historical stop record and any further guards before describing the final convergence criterion.

## Candidate figures

These are available project graphics; final selection depends on the outline. Each chosen graphic needs a self-contained caption stating the sample, metric, exclusions, and whether it reports development or evaluation.

| Purpose | Existing file | Recommendation |
|---|---|---|
| Vocabulary development | `swarm/graphs/success_rate.png` and `glossary_size_by_kind.png` | Combine as two panels; clarify changing batches and human representation changes. The success-rate graphic was visually inspected. |
| Model coverage | `evaluations/results/main-cov-det/coverage_radar_shared.png` | A compact table with numerator/denominator may communicate the small samples more clearly. |
| Symbol convergence | `evaluations/results/main-cov-det/js_heatmap_symbols.png`, `self_divergence.png` | Include the partial-output policy in captions; preserve a distinction between pooled and within-item quantities. |
| Round-trip reconstruction | `evaluations/results/main-cov-det/expressivity.png` | Visually inspected: this graphic shows the two Gemini conditions. Keep o4-mini's selected failures as a separate diagnostic if included. |
| Downstream reasoning | `evaluations/improvement/results/improvement_accuracy.png` | Include the negative result and explain run-level intervals versus item-level paired analysis. |

## Completion checklist once sources are available

- Read every outline tab, list every bullet verbatim in a coverage matrix, and assign a manuscript location and evidence source to each.
- Extract the rubric's requirements and weights; cross-reference them to manuscript sections.
- Read the evaluation and infrastructure adaptations attachments, reconcile them with implementation and saved runs, and identify which experiment snapshot the outline requests.
- Inspect reference papers for typography, section density, figure style, citation format, and expected scientific argument.
- Verify related-work and dataset references against primary publications; local inspiration lists are leads, not checked citations.
- Draft all requested sections, including transparent negative results and limitations.
- Create LaTeX, use the built-in editor and compiler, and verify the eight-page main-text limit with the requested back-matter boundary.
- Publish the checked source and figures into the authorized Overleaf project once the browser has access; compile and verify there.

No experiments were rerun, repository implementation files edited, or cloud project files modified during this preparation.
