# Expressivity: round trip natural language → BrainCode → natural language

**Every score is in [0, 1] and higher = input and output more similar = better.** BLEU = mean sentence BLEU (and corpus BLEU); ROUGE-L = longest-common-subsequence F1; word-Levenshtein similarity = 1 − word edit distance / longer length. Each forward translation is back-translated by the same model without seeing the original.

| model | dataset | pairs | BLEU ↑ | corpus BLEU ↑ | ROUGE-L ↑ | word-Levenshtein similarity ↑ |
|---|---|---:|---:|---:|---:|---:|
| Gemini 3.7 Flash | all | 1 | 0.295 | 0.295 | 0.700 | 0.570 |
| Gemini 3.7 Flash | Mind2Web | 1 | 0.295 | 0.295 | 0.700 | 0.570 |
