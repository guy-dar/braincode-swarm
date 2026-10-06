from pathlib import Path
import re
p=Path(__file__).parent/'overleaf/main.tex'
s=p.read_text(encoding='utf-8')
a=r'''Formal intermediate languages could expose how large language models interpret natural language. We ask whether agents can construct such a language, whether models interpret it consistently, and whether translation improves reasoning. We introduce \bc{}, a typed language for tasks and conversations, intended for model comparison, reasoning decomposition, and prompt formalization or compression. A multi-model syntax loop and retrieval-assisted glossary swarm pursue coverage, determinism, expressivity, reasoning improvement, and human interpretability. Development across six datasets produces 657 active glossary records. On 18 shared held-out items with three repeats, coverage ranges from 44.4\% for Claude Sonnet to 92.6\% for Claude Haiku among four main conditions; additional OpenAI trials largely fail acceptance. Symbol preferences and strictness differ across models, and round-trip reconstruction loses detail. On 50 BBEH-mini items, Llama 3.1 8B accuracy falls from 12.0\% to 0.7\% after in-context translation. \bc{} exposes behavioral differences, but does not yet establish a model-neutral representation or a reasoning benefit.'''
s=re.sub(r'(?<=\\begin\{abstract\}\n).*?(?=\n\\end\{abstract\})',lambda _:a,s,flags=re.S)
changes={
'Model compatibility is uneven. Haiku exceeds Sonnet despite their expected capability ordering; Gemini exceeds Sonnet and the tested OpenAI conditions, but not Haiku on the shared sample. This is consistent with adaptation to the Gemini-led glossary swarm, yet also with a division between lenient readers (Gemini and Haiku) and stricter readers demanding dedicated constructions. A language whose primitives mix formal constraints with prose meanings can be read differently even by capable models. Our agentic process did not eliminate this ambiguity across the tested model families.':
'Haiku exceeds Sonnet despite their expected capability ordering; Gemini exceeds Sonnet and the OpenAI conditions, but not Haiku. This suggests adaptation to the Gemini-led swarm, or a division between lenient readers (Gemini and Haiku) and stricter readers demanding dedicated constructions. Mixing formal constraints with prose meanings leaves difficult interpretive ambiguities that our process did not resolve across model families.',
'Symbol distributions and repeated encodings reveal distinct decomposition and vocabulary preferences. This makes \\bc{} a promising probe of model behavior, but not a ready-to-use comparative method: construction-model bias, selected failures, and checker strictness may dominate apparent linguistic tendencies. Repeated language construction and independent semantic judgments are needed before interpreting these preferences as robust model characteristics.':
'Symbol distributions reveal decomposition and vocabulary preferences, making \\bc{} a promising behavioral probe. It is not a ready-to-use comparative method: construction-model bias, failures, and checker strictness can confound linguistic tendencies. Repeated construction and independent semantic judgments must establish whether these preferences are robust.',
'Our six sources cover only a small portion of natural language; local held-out items remain within the construction domains. The shared comparison has 18 distinct items, and the reasoning experiment uses one small model and 50 items. Repeats increase observations without creating independent tasks. The effects of loop architecture, retrieval, glossary consolidation, and human intervention are not isolated.':
'Our six sources cover limited natural-language domains, with only 18 shared evaluation items and one reasoning model tested on 50 items. Repeats do not create independent tasks. We do not isolate effects of loop design, retrieval, consolidation, or human intervention.',
'Independent replications of the entire creation process could quantify variation in language structures, coverage, and model preferences. Testing whether preferences recur across independently created languages would strengthen both the agent-capability and comparative-research conclusions.':
'Independent creation runs could quantify structural and behavioral variance, testing whether model preferences recur across languages and strengthening both agent-capability and comparative-research conclusions.',
'It motivates auditable protocols, not a claim that \\bc{} would prevent such incidents. Communication utility, semantic fidelity, and governance would need separate tests.':
'Auditable protocols warrant study; prevention of such incidents by \\bc{} is untested.',
}
for a,b in changes.items():
    assert a in s,a[:70]
    s=s.replace(a,b)
s=s.replace('ACTION pick_up(target=object_label::pillow,\n  quantity=2, source=object_label::sofa)', 'ACTION pick_up(\n  target=object_label::pillow, quantity=2,\n  source=object_label::sofa)')
s=s.replace('The saved Claude-generated qualitative report', 'The saved Claude-generated qualitative report')
# Make the reference material flow in place instead of producing isolated float pages.
s=s.replace('\\usepackage{array}','\\usepackage{array}\n\\usepackage{float}')
main,app=s.split('\\appendix',1)
app=app.replace('\\begin{table*}[t]','\\begin{table}[H]').replace('\\end{table*}','\\end{table}')
app=app.replace('\\begin{table}[t]','\\begin{table}[H]')
app=app.replace('\\begin{figure*}[t]','\\begin{figure}[H]').replace('\\end{figure*}','\\end{figure}')
app=app.replace('\\includegraphics[width=\\textwidth]{appendix-determinism.pdf}','\\includegraphics[width=.95\\textwidth]{appendix-determinism.pdf}')
old='The planned allocation is approximately 0.4 page for the abstract and title, 1.1 pages for the introduction, 2.2 pages for \\bc{}, 2.8 pages for evaluation, and 1.5 pages for conclusions, limitations, and future work, totaling at most eight main-text pages.'
new='Estimated occupied space is 0.5 page for the abstract and title, 0.8 for the introduction, 2.3 for \\bc{}, 3.4 for evaluation, and 1.0 for conclusions, limitations, and future work: eight pages in total. These estimates include floats and shared pages, rather than counting every page touched by a section.'
assert old in app
app=app.replace(old,new)
s=main+'\\clearpage\n\\onecolumn\n\\appendix'+app
p.write_text(s,encoding='utf-8')
print('Reduced main text and organized appendix material in place.')
