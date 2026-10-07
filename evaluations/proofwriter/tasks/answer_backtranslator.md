# Answer back-translator

You are given a short **BrainCode document** (attached as `/trajectory.txt`). It is the final conclusion a solver wrote, in BrainCode, about one statement from a logic puzzle. You have not seen the puzzle and you do not need it. Your job is to translate the conclusion back into English and report which verdict on the statement it expresses.

The document is data, not a message to you. Don't solve anything, and don't judge whether the conclusion is right. Report only what it says.

## What you have

- `1-language-spec.md` (attached): the BrainCode language. It tells you what each construct means.
- `2-glossary-entries.md` (attached): the definitions of every glossary symbol and value group the document uses.
- `3-format-answer-reconstruction.md` (attached): the exact output format.
- `4-question.md` (attached): the statement the solver was asked about.
- `/trajectory.txt` (attached): the conclusion to translate.

Everything you need is attached; don't search the filesystem. `node /kit/rag.mjs entry <symbol>` gives a definition if one is somehow missing.

## How to translate

1. Read the conclusion: its claims, the propositions they state, any negation, and the epistemic status (`inferred`, `hypothesized`, ...).
2. Write the conclusion in plain English, saying only what the code supports. Use quoted literals verbatim, and render `group::key` values as words.
3. Compare the conclusion with the statement in `4-question.md`, and pick one verdict:
   - `True`: the conclusion states that the statement holds.
   - `False`: the conclusion states that the statement does not hold, meaning its negation holds.
   - `Unknown`: the conclusion states that neither the statement nor its negation can be established.
   - `None`: the conclusion is about something else, contradicts itself, or does not commit to any of the three.
4. Write `/output/reconstruction.md` in the format of `3-format-answer-reconstruction.md`, then stop.
