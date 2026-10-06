# Outline coverage audit

Source of content: `outline-source.md`, exported from the supplied Google Doc. The manuscript preserves its section order and all substantive requests. The copied outline remains unchanged.

The table below retains every numbered content item from the outline, including organizational headings. Wording is quoted from the outline; links and assignments are source context, not separate instructions to contact people.

## Reconciliation with the evidence

- The outline’s 56/95 GPT constructor suggestions was a preliminary snapshot. Saved current raw trials contain 71/129; the manuscript uses the latter.
- Haiku exceeds both Gemini conditions on the shared sample. The manuscript preserves the proposed construction-model-bias interpretation as a hypothesis, alongside strict versus lenient readings, rather than asserting Gemini beats all Claude models.
- Noun grouping is a central reported problem, but no exhaustive causal coding supports a claim that it is quantitatively the largest source of failures.
- The reasoning decline is explicit. Context load is a hypothesis, not an ablated cause. Clustered analysis and paired item-majority inference differ; both are reported.
- The implemented self-divergence uses arithmetic means, although the initial evaluation design requested harmonic averaging.
- OpenAI models are excluded from the main determinism/expressivity comparison. The outline also requests o4-mini’s type mix; this is retained and marked as a failure-confounded diagnostic.
- Guy’s migration-link placeholder is unfilled in the outline. The repository migration document supplies the evidence for the required three-sentence description.
- No evaluated fine-tuned model exists in the saved results. Preparation and resource limitations are described without inventing an outcome.
- The source qualitative reconstruction report ends mid-sentence. Only its complete, supported analysis is summarized.
- Author names follow the existing Overleaf project (Lia Soffer and Noam Yehezkel). The outline’s assignment to Simon is not treated as evidence of authorship.

## Item-by-item coverage

| Outline ID | Original requested content | Manuscript location |
|---|---|---|
| 1 | Abstract \- let AI summarize at the end \[make sure it includes a short introduction to the world of formal languages / languages for LLMs (depending on related work), our research question, qualitative objectives, product (BrainCode) introduction, use cases, highlighted results.\] | Abstract |
| 2 | Introduction [simonwasser2998@gmail.com](mailto:simonwasser2998@gmail.com) \- \[roughly 1 page\] | §1 Introduction |
| 2.1 | Related Work | §1, Related work |
| 2.2 | Our work | §1 Introduction |
| 2.2.1 | Possible use cases \- | §1, Our work and objectives |
| 2.2.1.1 | Model research tool \- comparison of model translations and examination of the robustness of natural language interpretation on average, linguistic tendencies, etc. | §1, Our work and objectives |
| 2.2.1.2 | Reasoning task decomposition | §1, Our work and objectives |
| 2.2.1.3 | Prompt compression and formalization | §1, Our work and objectives |
| 2.2.2 | Defined Qualitative Objectives (that we will test the produced language against) \- for each one note a formal definition | §1, definitions; operational metrics in §3 |
| 2.2.2.1 | Coverage | §1, definitions; operational metrics in §3 |
| 2.2.2.2 | Determinism | §1, definitions; operational metrics in §3 |
| 2.2.2.3 | Expressivity | §1, definitions; operational metrics in §3 |
| 2.2.2.4 | Improvement | §1, definitions; operational metrics in §3 |
| 2.2.2.5 | Human Interpretability \- unlike other objectives, this objective will be maintained directly during the creation process and therefore will not be quantitatively evaluated later. | §1, definitions; operational metrics in §3 |
| 2.2.3 | Research Questions \- \[measured by qualitatives above, refer to that in the analysis and conclusions\] | §1, Research questions; answers in §4.1 |
| 2.2.3.1 | How robust / subjective will the translation process of natural language be in such language? Could we use the language to analyze model behavior and compare behaviors of different models? (determinism) | §1, Research questions; answers in §4.1 |
| 2.2.3.2 | Another interesting exploratory question is the capability of agents to create such complex artifact, which could indirectly tell about model’s understanding and perception of language, and whether this understanding could use for creation a well-functioning language. (coverage, expressivity, interpretability) | §1, Research questions; answers in §4.1 |
| 2.2.3.3 | Could a language between formal/deterministic (refine term \- like programming language) and natural language help models improve their performance by using translations? **Find related work that could give justification to this hypothesis and include them in related work section** (improvement) | §1, Research questions; answers in §4.1 |
| 3 | BrainCode \- [Lia Soffer](mailto:liasoffer@mail.tau.ac.il) \- \[roughly 2 pages\] | §2 BrainCode |
| 3.1 | Syntax Creation \[should be relatively short\] | §2 BrainCode |
| 3.1.1 | Syntax Loop \- {[code & prompts link](https://github.com/liasoffer/BrainCode/tree/main/syntax-loop)} \[use the code project to describe the following\]: | §2.1, Syntax creation |
| 3.1.1.1 | Participating models | §2.1, Syntax creation |
| 3.1.1.2 | Loop structure and iteration flow, prompt emphasis | §2.1, Syntax creation |
| 3.1.1.3 | Main ideas it found proper to use | §2.1, Syntax creation |
| 3.1.2 | Migration with Guy’s template \- {enter migration documentation link} | §2.1, final paragraph (three sentences) |
| 3.1.2.1 | Advantages and disadvantages related to initial purposes and general language qualities | §2.1, final paragraph (three sentences) |
| 3.1.2.2 | Migrated characteristics from Guy’s design document | §2.1, final paragraph (three sentences) |
| 3.2 | Glossary creation process using a swarm | §2 BrainCode |
| 3.2.1 | Swarm infrastructure \[1-2 sentences\] {link to the code project} | §2.2, opening paragraph (two sentences) |
| 3.2.1.1 | Still required human in the loop in our case: runtime fixes, few language corrections along the way | §2.2, opening paragraph (two sentences) |
| 3.2.2 | Loop and RAG implementation {[link to description](https://docs.google.com/document/d/1YsI4XpcpP2G_JcHwFXu_032AkAbX9WhoS8HDixHRNJ0/edit?usp=sharing)} | §2.2, Data and loop; Retrieval and checking |
| 3.2.3 | Visualization of \#suggestions over batches \- by dataset, distinct close ended and open ended by color, and by type of suggestion | Figure 2, proposal counts by dataset and type |
| 3.3 | BrainCode Language Description | §2 BrainCode |
| 3.3.1 | Language specs \- summary | §2.3, Language and glossary |
| 3.3.2 | Glossary \- size, types of symbols (add a table of quantities of symbols / groups of symbols by type?) | §2.3 and Table 1 |
| 3.3.3 | Translation examples \- 1 task, 1 short conversation | §2.3, task and conversation listings |
| 4 | Evaluations / Experiments \- \[For each objective, describe the research question it’s related to, the way we evaluated it \- describe the experiment, SAMPLE SIZES, metrics and results, add relevant visualizations. Read C:\\projects\\braincode-swarm\\evaluations\\evaluations.docx\] \[roughly 2-3 pages\] | §3 Evaluations |
| 4.1 | Coverage | §3.1, coverage and diagnostic OpenAI trials |
| 4.1.1 | OpenAI models failed completely in translations, both weak and strong: **Why GPT-6.1 Sol and GPT-6 Luna fail.** Both OpenAI models read the glossary far more strictly than Gemini or Claude. They won't express a requested task, such as "search for flights" or "filter IT jobs", through the language's general constructs (activity(verb=…), requirement(…), search\_web). They argue those either execute work or lack a defined meaning for that exact role, so they declare failure and propose a dedicated constructor instead (flight\_search\_request, job\_search, search\_request). Constructors make up 56 of their 95 suggestions so far, and their translations are otherwise coherent; Luna's are nearly identical to the successful Claude Sonnet ones. So their 0% success rate mostly measures how strictly they read the glossary, plus a few real gaps every model hits (such as unit\_watt), not an inability to write BrainCode. | §3.1, coverage and diagnostic OpenAI trials |
| 4.1.2 | Quantitive results (graphs \+ descriptions): | §3.1, coverage and diagnostic OpenAI trials |
| 4.1.2.1 | Success rate per model table | Table 2, success/failure/error counts and rates |
| 4.1.2.2 | Coverage radar (shared) | Figure 3, shared coverage radar |
| 4.2 | Determinism | §3.2, determinism, qualitative report, and interpretation |
| 4.2.1 | Quantitive results (graphs \+ descriptions) \[put side by side in overleaf\]: | §3.2, determinism, qualitative report, and interpretation |
| 4.2.1.1 | Js\_heatmap\_symbols | Figure 4, left panel |
| 4.2.1.2 | Self divergence | Figure 4, right panel (side by side) |
| 4.2.1.3 | Symbol type mix \- slight differences between Claude and Gemini models with little to no correlation to success rate, major differences compared to o4-mini’s approach to the language usage. | Figure 5 and §3.2, type mix including diagnostic o4-mini |
| 4.2.2 | Refer to coverage radar: you can see different approaches of models through success rates in different datasets | §3.2, determinism, qualitative report, and interpretation |
| 4.2.3 | Claude’s qualitative md analysis in a nutshell \[short paragraph\] | §3.2, determinism, qualitative report, and interpretation |
| 4.2.4 | Thoughts: we could see \[through all analyses\] that models approach differently to the language, achieve different performance in different circumstances and tend to use it differently, with diverse preferences to different symbol types. | §3.2, determinism, qualitative report, and interpretation |
| 4.3 | Expressivity \- {maybe use terms encoding & decoding in description?} | §3.3 and Figure 6, encoding/decoding and qualitative reconstruction |
| 4.3.1 | Quantitative results (graphs \+ descriptions): | §3.3 and Figure 6, encoding/decoding and qualitative reconstruction |
| 4.3.1.1 | Expressivity graph | §3.3 and Figure 6, encoding/decoding and qualitative reconstruction |
| 4.3.2 | Qualitative md analysis in a nutshell \[short paragraph\] | §3.3 and Figure 6, encoding/decoding and qualitative reconstruction |
| 4.4 | Improvement | §3.4 and Table 3, all 23 task types and total |
| 4.4.1 | Unfortunately the success rate have gotten much worse using BrainCode. That could be because of the wide usage of context window to enable proper access to the language specifications and relevant glossary items. That is added to the fact that the model wasn’t trained on the language as we did not have the resources for that. | §3.4 and Table 3, all 23 task types and total |
| 4.4.2 | Table of success rate of the 2 groups \- by task type and total | §3.4 and Table 3, all 23 task types and total |
| 5 | Conclusions and Discussion \- \[roughly 0.5-0.75 pages\] | §4 Conclusions and Discussion |
| 5.1 | Conclusions \- \[try referring to each qualitative by it’s matching research question\] | §4 Conclusions and Discussion |
| 5.1.1 | Agentic research question | §4.1, Agent-created language (RQ2) |
| 5.1.1.1 | Main problem is noun grouping \- arranging objects into groups that contain deterministic values that could be used without pre-definition. That’s the main reason for failed translation in both train and test, and it showed that the models in use had hard time generalizing natural language objects into groups well. | §4.1, Agent-created language (RQ2) |
| 5.1.1.2 | Several model overfitting signs: | §4.1, Agent-created language (RQ2) |
| 5.1.1.3 | It seems Claude Haiku did much better than Sonnet, even though Sonnet is a stronger model. | §4.1, Agent-created language (RQ2) |
| 5.1.1.4 | gemini models did way better in translation success rate than Claude, OpenAI | §4.1, Agent-created language (RQ2) |
| 5.1.1.5 | We learn that different models (of different companies or size) approach the language very differently, read and “understand” it’s rules and constructions differently. The agentic process wasn’t able to generalize the language specifications and glossary in a way that will be clear to models that highly differ than the training models, yet it’s noteworthy that this level of generalization could be an extremely hard task when it comes to a language that is between natural and strict. | §4.1, Agent-created language (RQ2) |
| 5.1.2 | Potential research tool (determinism) | §4.1, Comparative research (RQ1) |
| 5.1.2.1 | We could see different preferences of models in language crafting and understanding under diverse circumstances. One could infer some linguistic tendencies of the models, and although it’s not a ready-to-use research method, the differences show it could be useful as a research comparative tool and linguistic tendencies exploration. | §4.1, Comparative research (RQ1) |
| 5.1.3 | Reasoning task decomposition improvement (Improvement) | §4.1, Reasoning (RQ3) |
| 5.1.3.1 | The language usage only harmed performance (significantly), probably due to majorly exploiting context window. We believe that a valid assessment to value in reasoning task decomposition improvement could be achieved by fine tuning a model to work with the language, as we tried but failed to achieve with our resources. | §4.1, Reasoning (RQ3) |
| 5.2 | Limitations \- \[roughly 0.5 pages\] | §4.2, Limitations |
| 5.2.1 | Datasets \- limited coverage of natural language | §4.2, Limitations |
| 5.2.2 | Effect of loop and swarm design choices and human-in-the-loop involvement is unmeasurable | §4.2, Limitations |
| 5.2.3 | Compute resources limitation \- limited rate of proxy requests (LLM calls) limited our ability to train the swarm and could affect the extent of created glossary. In addition it required our intervention and optimization during runs \- such as prompt adaptations and changes in access to commands depending on circumstances. Theoretically those are very indirect effects on the agents work, but we cannot know for sure. | §4.2, Limitations |
| 5.2.4 | No benchmarks \- Since the evaluations are not standard and tailored for the language and it’s purposes, most of them are not comparable and are mostly explorative. (however, we could still notice differences between models and use as a research tool). | §4.2, Limitations |
| 5.2.5 | We excluded runtime and token-efficiency from our goals, and believe the current setup only harm them. However, we believe that a more careful implementation \+ more training data and resources could make those measurements much less harmed and maybe even improved. | §4.2, Limitations |
| 5.2.6 | Overfitting to training model affects the ability to use the language as a comparative research tool \- it puts strong emphasis on comparison to the training model while using this tool. | §4.2, Limitations |
| 5.3 | Future Work \- \[roughly 0.5 pages\] | §4.3, Future work |
| 5.3.1 | we believe having more resources and thoughtful pipeline creation could yield much better results while repeating the experiment: | §4.3, Future work |
| 5.3.1.1 | Automate process of syntax \+ glossary creation (remove human in the loop) | §4.3, Future work |
| 5.3.1.2 | Try entering a few-shot learning and improve RAG efficiency (both time and token volume) to see if it improves model-language compatibility / performance. | §4.3, Future work |
| 5.3.1.3 | Involve agents of different models from different companies in the swarm during training (we didn’t have the possibility \- all other companies experiments were from our own budget) to reduce overfit to a certain model | §4.3, Future work |
| 5.3.1.4 | Finetune a model over language successful translations, instead of giving it the entire language documentation and / or RAG acces. | §4.3, Future work |
| 5.3.2 | . replicating several processes of language creation, measuring quantitatively and qualitatively the variance between outcomes \- could validate and expand understanding regarding our research questions (specifically potential as a comparative research tool and agentic capabilities creating a language) | §4.3, Future work |
| 5.3.2.1 | We could see if models language usage preferences are reproducible (as much as possible under limitation of different languages) | §4.3, Future work |
| 5.3.3 | Research related to swarm communication using a language product (cite papers including the recent Huggingface incident) | §4.3, Future work |
| 6 | AI Disclosure | AI Disclosure |
| 6.1 | Code implementation according to given instructions, design and refinements (syntax loop, changes in Guy’s swarm infrastructure, evaluations), monitoring and improvement suggestions along the way, datasets retrieval and design consultation \- used OpenAI Astra 6 (Medium level), Claude Opus 5.5 (mostly). | AI Disclosure |
| 6.2 | Used for Language specs and initial glossary refinement, comparison against Guy’s pre-defined syntax, and merge Guy’s syntax into syntax loop’s products \- used OpenAI Astra 6 (Medium level). | AI Disclosure |
| 6.3 | Writing according to our content outlines. | AI Disclosure |
| 7 | References [simonwasser2998@gmail.com](mailto:simonwasser2998@gmail.com) | References |
| 7.1 | All datasets | References |
| 7.2 | Improvement benchmark | References |
| 7.3 | Related work papers | References |
| 8 | Appendix | Appendices A–C |
| 8.1 | Git Repository | Appendix A, linked Git repository and evidence map |
| 8.2 | [Noam Yehezkel](mailto:noamyehezkel@mail.tau.ac.il) additional visualizations from evaluations? | Appendix B, additional visualizations |
| 8.3 | Additional graphs | Appendices A–C |
| 8.3.1 | Determinism vs coverage \- rate models in description | Appendix B and Figure 7 left, both rankings in text |
| 8.3.2 | Self divergence by dataset | Appendix B and Figure 7 right, self-divergence by dataset |

**Total numbered content items mapped: 99.**

## Grading checklist

| Rubric area | Evidence in manuscript |
|---|---|
| Research question (10%) | Three explicit questions; objectives defined in §1 and conclusions mapped back in §4.1. |
| Ambition and effort (10%) | Syntax loop, semantic migration, swarm, retrieval, six data sources, multi-model evaluation, and reasoning pipeline. |
| Literature review (20%) | Semantic representations, reasoning/actions, program-aided reasoning, decomposition, formalization, compression, and multi-agent communication; all six datasets and BBEH cited. |
| Method (20%) | Split seeds, sample sizes, frozen versions, model identifiers, metrics, selection/exclusion rules, prompts, decoding settings, and repository evidence map. |
| Results and discussion (20%) | All requested graphs, complete reasoning task table, negative results, qualitative cases, alternative explanations, and statistical limitations. |
| Presentation (20%) | Official ACL style, author-year citations, vector PDF figures, descriptive captions, code examples, and separate back matter. Final rendering and page count recorded in page-budget.md. |
