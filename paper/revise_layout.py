from pathlib import Path
p=Path(__file__).parent/'overleaf/main.tex'
s=p.read_text(encoding='utf-8')
rows=(p.parent/'improvement-rows.tex').read_text(encoding='utf-8').replace(' Qa',' QA').replace('Nycc','NYCC').replace('Sarc','SARC').replace('Sportqa','SportQA')
s=s.replace('\\input{improvement-rows.tex}',rows.rstrip())
s=s.replace('\\bibliographystyle{acl_natbib}\n','')
changes={
'Natural language expresses tasks, beliefs, uncertainty, and changing intentions with considerable flexibility. This flexibility also permits multiple interpretations of the same request. A shared intermediate representation might make these choices explicit: a request could name its objects, distinguish proposed actions from observed events, and preserve who asserted which claim. We investigate whether language-model agents can build such a representation themselves and whether the resulting artifact transfers beyond its creators.':
'Natural language permits multiple interpretations of tasks, beliefs, and changing intentions. An intermediate representation could name objects, distinguish proposed actions from observed events, and preserve who asserted which claim. We investigate whether language-model agents can build such a representation and whether it transfers beyond its creators.',
'These are exploratory questions about one constructed artifact; they do not presume that successful syntax generation establishes semantic understanding.':
'These exploratory questions concern one artifact; generating syntax need not establish semantic understanding.',
'The syntax loop assigns complementary roles: a Searcher proposes useful constructs, a Shaper revises the specification, a Critic tests it against examples, and a Documenter maintains aligned documentation and glossary entries. The saved configuration uses Gemini 3.1 Pro Preview as Searcher, GPT-5.6 Terra as Critic, and Claude Sonnet 5 as Documenter; the Shaper rotates across these models, with configured fallbacks. An initial sprint explores flat, Python-like statements, explicit attribute/content distinctions, and conversation turns. Subsequent iterations emphasize source-faithful representation, minimal primitives, explicit typing, bounded control flow, and readable canonical names.':
'The syntax loop assigns a Searcher to propose constructs, a Shaper to revise the specification, a Critic to test examples, and a Documenter to maintain definitions and glossary entries. The configuration uses Gemini 3.1 Pro Preview as Searcher, GPT-5.6 Terra as Critic, and Claude Sonnet 5 as Documenter; the Shaper rotates among them, with configured fallbacks. Starting from flat Python-like statements, explicit attribute/content distinctions, and conversation turns, prompts emphasize faithful representation, minimal primitives, explicit typing, bounded control flow, and readable names.',
'Each proposal is critiqued through simulated translations, revised, and checked for consistency among definitions and examples. The loop allows up to three reworks; unresolved human hard constraints prevent acceptance, while some remaining issues can be recorded for later repair. Thus this is an agent-assisted design process with qualitative acceptance criteria, not an autonomous search with a validated numerical objective. Its main structural choices include typed tasks, actions distinct from checks, immutable bindings, bounded iteration, and explicit reply and revision links.':
'Proposals undergo simulated translations, critique, and documentation checks, with up to three reworks. Human hard constraints can block acceptance; other unresolved issues may be deferred. Acceptance is qualitative. The resulting syntax uses typed tasks, actions distinct from checks, immutable bindings, bounded iteration, and explicit reply and revision links.',
'The closed/open distinction is an operational grouping for this study, not a claim that every item has a single correct output.':
'This closed/open grouping does not imply a unique correct output for every task.',
'These are local held-out items from the same sources, not official benchmark test sets or unseen domains.':
'These local splits test new items within known sources, not official benchmark splits or unseen domains.',
'Before translating, a needs extractor identifies source-linked actions, objects, negation, temporal relations, and speech or claim requirements. Long source segments are divided at roughly 400 characters; source references allow retrieved entries to be traced back to the need they address. A heuristic fallback handles failed extraction.':
'A needs extractor identifies source-linked actions, objects, negation, temporal relations, and speech or claim requirements, with a heuristic fallback. Segments of roughly 400 characters retain source references linking retrieval to the original need.',
'The translator can retrieve, search, inspect entries, widen retrieval, and check an output. The in-memory index and cached embeddings are rebuilt after migration.':
'Translators can retrieve, search, inspect entries, widen retrieval, and check outputs; migration rebuilds the in-memory index and embedding cache.',
'All conditions receive the same translator toolkit and precomputed item needs and retrieval, reducing differences in the initial evidence available to them. This does not remove differences in how they use tools or interpret the rules.':
'All conditions share the translator toolkit and precomputed item needs and retrieval, controlling initial evidence but not subsequent tool use or rule interpretation.',
'The latest saved diagnostic snapshot contains 71 constructor additions among 129 proposals, updating the preliminary 56/95 count.':
'The saved snapshot contains 71 constructor additions among 129 proposals.',
'Its cases were selected for high divergence, so these are explanatory examples rather than prevalence estimates. Together with the coverage radar, the results show different representational preferences under different circumstances, not a validated taxonomy of models\' linguistic abilities.':
'Selected high-divergence cases explain patterns rather than estimate their prevalence. Together with the coverage radar, they reveal representational preferences, without validating a taxonomy of linguistic abilities.',
'The available failure reports identify this as a central generalization problem, but do not provide an exhaustive causal count establishing it as the most frequent failure source.':
'Failure reports identify this as a central problem without quantifying its causal share.',
'Agents and human reviewers produced a substantial, interpretable-by-design specification and glossary, and several models accepted most held-out translations.':
'Agents and human reviewers produced a substantial specification and glossary designed for readability; several models accepted most held-out translations.',
'The experiment does not demonstrate an advantage for reasoning decomposition, nor establish context length as the cause of the decline.':
'Neither a decomposition benefit nor context length as the cause is established.',
'A useful next assessment must separate representational value from translation failures and extra prompting costs.':
'Further assessment must separate representation, translation, and prompting costs.',
'Although intended as operational fixes, their indirect effects on the resulting artifact cannot be ruled out. The evaluation snapshot is frozen, but the development trajectory is not a controlled ablation of these changes.':
'Their indirect effects remain unmeasured: a frozen evaluation snapshot does not make development a controlled ablation.',
}
for a,b in changes.items():
    assert a in s,a[:80]
    s=s.replace(a,b)
for code in ['vertex-proxy/gemini-flash','vertex-proxy/gemini-flash-high','anthropic/claude-sonnet-5-5','anthropic/claude-haiku-4-5-20251001','meta-llama/Llama-3.1-8B-Instruct']:
    s=s.replace('\\code{'+code+'}','\\path{'+code+'}')
# Keep long appendix paths readable without stretched justification.
s=s.replace('\\begin{tabular}{p{.28\\textwidth}p{.65\\textwidth}}','\\begin{tabular}{>{\\raggedright\\arraybackslash}p{.25\\textwidth}>{\\raggedright\\arraybackslash}p{.68\\textwidth}}')
s=s.replace('\\usepackage{booktabs}','\\usepackage{booktabs}\n\\usepackage{array}')
p.write_text(s,encoding='utf-8')
print('Applied content-preserving compression, inlined task table, and fixed bibliography setup.')
