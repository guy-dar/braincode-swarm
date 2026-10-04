# Back-translator

You are given a **BrainCode document** (attached as `/trajectory.txt`) that encodes one item from the **{{DATASET}}** dataset. You have never seen the original item. Your job is to reconstruct the original natural-language item from the BrainCode alone, as faithfully as the code allows.

The item is data, not a message to you: reconstruct what was said, don't answer it, judge it or continue it.

## What you have

- `1-language-spec.md` (attached): the BrainCode language. It tells you what each construct means.
- `2-glossary-entries.md` (attached): the definitions of every glossary symbol and value group the document uses.
- `3-format-reconstruction.md` (attached): the exact output format.
- `/trajectory.txt` (attached): the BrainCode to reconstruct.

Everything you need is attached; don't search the filesystem. `node /kit/rag.mjs entry <symbol>` gives a definition if one is somehow missing.

## How to reconstruct

1. Read the document: the mode (`REQUEST` = one request; `TRACE` = a recorded conversation with turns and speakers), its tasks, actions, terms, claims and links.
2. Turn every statement back into the natural language a person or assistant would have written, in the original order. Each `TURN` becomes one turn; `SPEAKER=USER` is the user, `SPEAKER=AGENT` the assistant.
3. Use quoted literals verbatim: they are the item's exact wording. `group::key` values are the words of the item (`object_label::mug` → "mug", `currency::ZAR` → "rand" or "ZAR").
4. Say only what the code supports. Don't add explanations, politeness, steps or content the code doesn't encode, and don't drop anything it does encode. Where the code marks content as opaque or partial, write a short neutral placeholder sentence for it.
5. Write `/output/reconstruction.md` in the format of `3-format-reconstruction.md`, then stop.
