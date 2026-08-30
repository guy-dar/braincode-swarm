# Discovery

You are translating one trajectory into BrainCode, in an isolated, single-use
invocation with no memory of any other trajectory. There is no document to edit, no
corpus to update, no vocabulary to revise — only the files you write in response to
this one trajectory.

Read `/reference/DESIGN_DOC.md` first — it defines the language: what a BrainCode
document has to look like, its grammar, and its fidelity rules. Then read
`/trajectory.json` — it's already attached to this message; don't search for it.

Naming a construct, in order — stop at the first gate that fails:

1. **Earns existence.** Would the nearest construct you already know lose a distinction that matters if reused here? If not, don't mint a new one. Default to minting when genuinely unsure — vocabulary sprawl is the accepted cost of fidelity.
2. **Altitude.** Swapping the instance should leave the name valid; swapping the intent should break it. `web_search` names an intent; `search_2` names an instance and fails this gate.
3. **Legibility.** Could a reader who's never seen the definition predict what it covers and excludes from the name alone? Roughly two words, unambiguous without relying on its namespace to rescue it.

**No uncanonized strings.** A bare natural-language string standing in for content is not a construct — reaching for one is failing gate 1, not passing it. Bare strings are for narrow, genuinely atomic data taken verbatim from the source: a filename, an exact quoted term, a single word or short phrase copied from the input. They are never acceptable for a judgment, a category, a classification, a summary, or a conclusion you are forming — however short. A sentiment reading of "strongly positive" is a judgment, not quoted data, and needs a construct (an enum member, a labeled result), not a hand-picked string. Composing the subject agent's final response to the user is an operation like any other: decompose what is actually being communicated — which finding, which values, which comparison — into its own constructs. Never fall back to storing the assembled sentence itself as a string argument; that is transcription of the surface text, and the language's fidelity contract draws that line explicitly — translation recovers operations, it does not transcribe prose.

Granularity: the clearest case for a construct is an operation that transforms data or brings new data into existence. A single step of subject-agent activity usually expands into several constructs — expand along operations, not along narration. Operations count even when the source trace never states them outright, whenever a competent reader would confidently assume the operation occurred — this is a materially weaker bar than logical necessity.

Fidelity, applied:

- Recover the operations a competent reader would assume happened — don't limit yourself to what's explicitly narrated, and don't pad in ones that aren't warranted either.
- Never invent reasoning: no motive or deliberation beyond what the source evidences.
- Make human intent explicit, anchored to what the subject agent demonstrably understood the request to be (shown by what it did), not your own reading of the text.
- Encode execution errors using the construct for the operation being performed, not a separate error construct — a miscount is still the counting construct.

This version of the discovery task has no shared corpus or prior translated examples to retrieve against — make the best call from `/reference/DESIGN_DOC.md` and this prompt alone rather than guessing that a reusable construct exists elsewhere.

## Write your output

Actually create four files in `/output` — don't just describe or quote their
contents in your reply instead of creating them. A response that talks about what
these files would contain, without the files existing, is a failed run. **So is a
file that exists but is empty or a placeholder** — every one of the four must
contain real, finished content the first time you write it. Never write a file
with a "TODO" / "will add this" / empty-string placeholder intending to fill it in
later — you don't get a later. Finish composing each file's actual content before
you write it, then write it once.

1. `/output/translation.bc` — the finished BrainCode document, and nothing else in it: no commentary, no code fences, no explanation. Must never be empty.
2. `/output/decisions.md` — the judgment calls you made and why, in plain prose. Naming choices, granularity calls, anything that passed a naming gate narrowly or could plausibly have gone the other way. A later review pass — reading many of these across many trajectories, looking for where independent translations agree, where they conflict, and what patterns recur often enough to be worth canonizing — reads this file first. Write it for that reader, not for yourself. Must never be empty.
3. `/output/uncertainties.md` — anything you were genuinely unsure about and what you decided anyway, stated as an open question plus your resolution (the translation itself still has to commit to one answer — ambiguity gets flagged here, not left unresolved in the document). If there genuinely isn't one, the file must still contain the word "none" — not be left empty.
4. `/output/keywords.md` — five to ten comma-separated search terms for this trajectory: the constructs you minted or used, the domain/topic, anything that would help someone searching across many trajectories find this one. Must never be empty.

All four files existing with real content is not optional and not best-effort — it
is the definition of having done this task. Do this now, for the one trajectory
attached to this message. Create the four files and stop — no further reading, no
other output.
