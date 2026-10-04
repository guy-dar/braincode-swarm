# Glossary RAG kit

This kit is for any model that has to find BrainCode glossary symbols: translators in containers, the migrator, or anything added later. The glossary holds the symbols you are allowed to use. This kit is how you find the right ones without reading the whole glossary.

## What is where

| Path (inside a container) | What it is |
|---|---|
| `/rag_context.md` | Already done for you: your item's needs, the candidate symbols for each need, and the full retrieved records and rules. **Read this first.** |
| `/needs.json` | The same needs as JSON, with their candidates. `check` reads this file. |
| `/kit/rag.mjs` | Command-line client for live lookups (below). |
| `/reference/glossary.md` | The whole glossary, one table row per symbol. This is the fallback. |

## The 7-step algorithm

The host has already done steps 1–4. You do steps 5–7.

1. **Extract needs.** The item is split into separate, source-linked needs: actions, objects, constraints, negations, corrections, temporal relations, speech acts, claims and reasoning links. Each need has a source locator (`t2:s3`) that matches the numbered item in `/trajectory.txt`.
2. **Search each need** by exact name or alias, by keyword, and by meaning.
3. **Combine and rerank** each need's candidates against its conversation context. An exact name or alias match is never dropped.
4. **Expand.** Pull in the full definitions of the candidates, everything they depend on, and the shared rules that govern them.
5. **Translate, then check.** After drafting, run `node /kit/rag.mjs check`. It lists needs your translation does not cover yet, and any symbol you used that is not in the glossary.
6. **Widen before you give up.** For every unresolved need, run `node /kit/rag.mjs widen "<need text>"`, and also try `search` with different wording (a synonym, the general category, the opposite). Only when widened searches find nothing usable is the need a real glossary gap.
7. **Fallback.** If the server can't be reached, or you suspect a symbol exists under a name you haven't tried, read or grep `/reference/glossary.md` (one table row per symbol).

## Commands

```sh
node /kit/rag.mjs search "at most twenty minutes of walking between stops" "cheapest first" "inside the sink"   # several needs, one call
node /kit/rag.mjs widen  "user withdraws the earlier budget" --kind correction
node /kit/rag.mjs entry  pick_up place rinse     # several records at once, compact
node /kit/rag.mjs check  --translation /output/translation.md
node /kit/rag.mjs retrieve                        # re-run steps 1-4 on /item_raw.txt
```

Need kinds you can pass with `--kind`: `action`, `object`, `constraint`, `negation`, `correction`, `temporal`, `speech_act`, `claim`, `reasoning`.

## Reading results

- **Candidates are ranked best first.** `exact` means a symbol or alias phrase literally occurs in the need. `keyword` and `semantic` mean the need was found by words or by meaning. A candidate can be wrong: read its definition and its `not:` contrast before you use it.
- **Every record names its shared rules.** Those rules bind you (for example, "Cheapest usually requires both rank_price and dir_asc").
- **Aliases are hints, not equivalences.** If the context suggests another meaning, report the ambiguity instead of forcing the alias.
- **Statuses:**
  - `Needs clarification` records are listed, but you must not rely on them in a final translation without saying so.
  - `Deprecated` records point to their replacement in `use instead:`.

## For host-side code

Python code can query the same index:

```python
from rag.client import RagClient
RagClient().search("cheapest first", kind="constraint", format="text")
```

`kit/tool_schema.json` defines the same operations for function-calling models.
