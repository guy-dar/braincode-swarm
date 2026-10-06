[simonwasser2998@gmail.com](mailto:simonwasser2998@gmail.com) \- your responsibility is to

1. Enrich outlines where needed (e.g, related work, research questions, etc.)  
2. Produce a written essay according to those outlines  
3. Some of the outlines will be linked to documents with more content / code projects \- make sure to use the relevant content  
4. Move to Overleaf \- ask [Lia Soffer](mailto:liasoffer@mail.tau.ac.il) to open the file when relevant, so we could all be collaborators  
5. Make sure all references are valid and refer to the correct papers

—------------------------------------------------------------------------------------------------------------

1. Abstract \- let AI summarize at the end \[make sure it includes a short introduction to the world of formal languages / languages for LLMs (depending on related work), our research question, qualitative objectives, product (BrainCode) introduction, use cases, highlighted results.\]   
2. Introduction [simonwasser2998@gmail.com](mailto:simonwasser2998@gmail.com) \- \[roughly 1 page\]  
   1. Related Work  
   2. Our work  
      1. Possible use cases \-   
         1. Model research tool \- comparison of model translations and examination of the robustness of natural language interpretation on average, linguistic tendencies, etc.  
         2. Reasoning task decomposition   
         3. Prompt compression and formalization  
      2. Defined Qualitative Objectives (that we will test the produced language against) \- for each one note a formal definition  
         1. Coverage  
         2. Determinism  
         3. Expressivity  
         4. Improvement  
         5. Human Interpretability \- unlike other objectives, this objective will be maintained directly during the creation process and therefore will not be quantitatively evaluated later.   
      3. Research Questions \- \[measured by qualitatives above, refer to that in the analysis and conclusions\]  
         1. How robust / subjective will the translation process of natural language be in such language? Could we use the language to analyze model behavior and compare behaviors of different models? (determinism)  
         2. Another interesting exploratory question is the capability of agents to create such complex artifact, which could indirectly tell about model’s understanding and perception of language, and whether this understanding could use for creation a well-functioning language. (coverage, expressivity, interpretability)  
         3. Could a language between formal/deterministic (refine term \- like programming language) and natural language help models improve their performance by using translations? **Find related work that could give justification to this hypothesis and include them in related work section** (improvement)  
3. BrainCode \- [Lia Soffer](mailto:liasoffer@mail.tau.ac.il) \- \[roughly 2 pages\]  
   1. Syntax Creation \[should be relatively short\]  
      1. Syntax Loop \- {[code & prompts link](https://github.com/liasoffer/BrainCode/tree/main/syntax-loop)} \[use the code project to describe the following\]:  
         1. Participating models  
         2. Loop structure and iteration flow, prompt emphasis  
         3. Main ideas it found proper to use  
      2. Migration with Guy’s template \- {enter migration documentation link}  
         \[This part should not be more than 2-3 sentences total\]  
         1. Advantages and disadvantages related to initial purposes and general language qualities  
         2. Migrated characteristics from Guy’s design document  
   2. Glossary creation process using a swarm  
      1. Swarm infrastructure \[1-2 sentences\] {link to the code project}   
         1. Still required human in the loop in our case: runtime fixes, few language corrections along the way  
      2. Loop and RAG implementation {[link to description](https://docs.google.com/document/d/1YsI4XpcpP2G_JcHwFXu_032AkAbX9WhoS8HDixHRNJ0/edit?usp=sharing)}  
      3. Visualization of \#suggestions over batches \- by dataset, distinct close ended and open ended by color, and by type of suggestion  
   3. BrainCode Language Description  
      1. Language specs \- summary   
      2. Glossary \- size, types of symbols (add a table of quantities of symbols / groups of symbols by type?)  
      3. Translation examples \- 1 task, 1 short conversation  
4. Evaluations / Experiments \- \[For each objective, describe the research question it’s related to, the way we evaluated it \- describe the experiment, SAMPLE SIZES, metrics and results, add relevant visualizations. Read C:\\projects\\braincode-swarm\\evaluations\\evaluations.docx\] \[roughly 2-3 pages\]  
   1. Coverage  
      1. OpenAI models failed completely in translations, both weak and strong: **Why GPT-6.1 Sol and GPT-6 Luna fail.** Both OpenAI models read the glossary far more strictly than Gemini or Claude. They won't express a requested task, such as "search for flights" or "filter IT jobs", through the language's general constructs (activity(verb=…), requirement(…), search\_web). They argue those either execute work or lack a defined meaning for that exact role, so they declare failure and propose a dedicated constructor instead (flight\_search\_request, job\_search, search\_request). Constructors make up 56 of their 95 suggestions so far, and their translations are otherwise coherent; Luna's are nearly identical to the successful Claude Sonnet ones. So their 0% success rate mostly measures how strictly they read the glossary, plus a few real gaps every model hits (such as unit\_watt), not an inability to write BrainCode.   
         We tried o4 mini to see if it will behave more similarly to gemini 3.7 flash, yet it had only 4 success translations (7%). Therefore we excluded openAI models from further analyses. It also had more tendency to go over the specifications and use full natural language quotations in many ways, which we disqualified as errors.    
         Claude’s success rate is way less better than Gemini. Surprisingly the weaker Claude model had a better success rate, probably because of resemblance to flash models while approaching the language. The findings point overfitting to Gemini models while swarm training and language composition.   
      2. Quantitive results (graphs \+ descriptions):   
         1. Success rate per model table  
         2. Coverage radar (shared)  
   2. Determinism  
      1. Quantitive results (graphs \+ descriptions) \[put side by side in overleaf\]:   
         1. Js\_heatmap\_symbols  
         2. Self divergence  
         3. Symbol type mix \- slight differences between Claude and Gemini models with little to no correlation to success rate, major differences compared to o4-mini’s approach to the language usage.   
      2. Refer to coverage radar: you can see different approaches of models through success rates in different datasets  
      3. Claude’s qualitative md analysis in a nutshell \[short paragraph\]  
      4. Thoughts: we could see \[through all analyses\] that models approach differently to the language, achieve different performance in different circumstances and tend to use it differently, with diverse preferences to different symbol types.   
   3. Expressivity \- {maybe use terms encoding & decoding in description?}  
      1. Quantitative results (graphs \+ descriptions):   
         1. Expressivity graph  
      2. Qualitative md analysis in a nutshell \[short paragraph\]  
   4. Improvement  
      1. Unfortunately the success rate have gotten much worse using BrainCode. That could be because of the wide usage of context window to enable proper access to the language specifications and relevant glossary items. That is added to the fact that the model wasn’t trained on the language as we did not have the resources for that.    
      2. Table of success rate of the 2 groups \- by task type and total

      

5. Conclusions and Discussion \- \[roughly 0.5-0.75 pages\]  
   1. Conclusions \- \[try referring to each qualitative by it’s matching research question\]  
      1. Agentic research question  
         1. Main problem is noun grouping \- arranging objects into groups that contain deterministic values that could be used without pre-definition. That’s the main reason for failed translation in both train and test, and it showed that the models in use had hard time generalizing natural language objects into groups well.  
         2. Several model overfitting signs:   
         3. It seems Claude Haiku did much better than Sonnet, even though Sonnet is a stronger model.   
         4. gemini models did way better in translation success rate than Claude, OpenAI  
             These findings imply overfitting to the models during the glossary creation, that was held by Gemini agents (the swarm). The partition could also be lenient readers (Gemini, Haiku) against strict ones that keep asking for explicit constructions.   
         5. We learn that different models (of different companies or size) approach the language very differently, read and “understand” it’s rules and constructions differently. The agentic process wasn’t able to generalize the language specifications and glossary in a way that will be clear to models that highly differ than the training models, yet it’s noteworthy that this level of generalization could be an extremely hard task when it comes to a language that is between natural and strict.   
      2. Potential research tool (determinism)  
         1. We could see different preferences of models in language crafting and understanding under diverse circumstances. One could infer some linguistic tendencies of the models, and although it’s not a ready-to-use research method, the differences show it could be useful as a research comparative tool and linguistic tendencies exploration.   
      3. Reasoning task decomposition improvement (Improvement)  
         1. The language usage only harmed performance (significantly), probably due to majorly exploiting context window. We believe that a valid assessment to value in reasoning task decomposition improvement could be achieved by fine tuning a model to work with the language, as we tried but failed to achieve with our resources.   
   2. Limitations \- \[roughly 0.5 pages\]  
      1. Datasets \- limited coverage of natural language  
      2. Effect of loop and swarm design choices and human-in-the-loop involvement is unmeasurable  
      3. Compute resources limitation \- limited rate of proxy requests (LLM calls) limited our ability to train the swarm and could affect the extent of created glossary. In addition it required our intervention and optimization during runs \- such as prompt adaptations and changes in access to commands depending on circumstances. Theoretically those are very indirect effects on the agents work, but we cannot know for sure.   
      4. No benchmarks \- Since the evaluations are not standard and tailored for the language and it’s purposes, most of them are not comparable and are mostly explorative. (however, we could still notice differences between models and use as a research tool).   
      5. We excluded runtime and token-efficiency from our goals, and believe the current setup only harm them. However, we believe that a more careful implementation \+ more training data and resources could make those measurements much less harmed and maybe even improved.   
      6. Overfitting to training model affects the ability to use the language as a comparative research tool \- it puts strong emphasis on comparison to the training model while using this tool.   
   3. Future Work \- \[roughly 0.5 pages\]  
      1. we believe having more resources and thoughtful pipeline creation could yield much better results while repeating the experiment:   
         1. Automate process of syntax \+ glossary creation (remove human in the loop)  
         2. Try entering a few-shot learning and improve RAG efficiency (both time and token volume) to see if it improves model-language compatibility / performance.   
         3. Involve agents of different models from different companies in the swarm during training (we didn’t have the possibility \- all other companies experiments were from our own budget) to reduce overfit to a certain model  
         4. Finetune a model over language successful translations, instead of giving it the entire language documentation and / or RAG acces.   
      2. . replicating several processes of language creation, measuring quantitatively and qualitatively the variance between outcomes \- could validate and expand understanding regarding our research questions (specifically potential as a comparative research tool and agentic capabilities creating a language)  
         1. We could see if models language usage preferences are reproducible (as much as possible under limitation of different languages)  
      3. Research related to swarm communication using a language product (cite papers including the recent Huggingface incident)   
6. AI Disclosure  
   1. Code implementation according to given instructions, design and refinements (syntax loop, changes in Guy’s swarm infrastructure, evaluations), monitoring and improvement suggestions along the way, datasets retrieval and design consultation \- used OpenAI Astra 6 (Medium level), Claude Opus 5.5 (mostly).  
   2. Used for Language specs and initial glossary refinement, comparison against Guy’s pre-defined syntax, and merge Guy’s syntax into syntax loop’s products \- used OpenAI Astra 6 (Medium level).  
   3. Writing according to our content outlines.   
7. References [simonwasser2998@gmail.com](mailto:simonwasser2998@gmail.com)  
   1. All datasets  
   2. Improvement benchmark  
   3. Related work papers  
8. Appendix   
   1. Git Repository  
   2. [Noam Yehezkel](mailto:noamyehezkel@mail.tau.ac.il) additional visualizations from evaluations?  
   3. Additional graphs  
      1. Determinism vs coverage \- rate models in description  
      2. Self divergence by dataset