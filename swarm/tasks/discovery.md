# Discovery

You are translating one trajectory into BrainCode, in an isolated, single-use
invocation with no memory of any other trajectory. There is no document to edit,
no corpus to update, no vocabulary to revise — only the files you write in
response to this one trajectory.

Read `/reference/DESIGN_DOC.md` first; it is the whole specification and it
governs. Then read `/trajectory.txt`: the turns as plain text, already attached
to this message. Don't search for it and don't reformat it, it is readable as-is.

## What to hold on to

The reply in the trajectory has a shape — an opening, sections, claims, a
conclusion. That shape is not your document. Record what the agent *worked out*:
the operations it performed, the facts it established, and how those bear on each
other. A reader holding your document and not the reply should be able to say
what the agent concluded and why.

The failure to watch for in yourself is copying the reply's outline across and
dressing it in syntax. It hides well, because every disguise satisfies the rules:
a phrase sitting in a literal, a sentence turned into a capitalised enum member,
a predicate whose name is its own object, an entity that is only a heading, one
enum per section with the bullets as its members, a whole passage under a
wrapper. When you finish, read your declaration block on its own — if it reads
like a table of contents, start again. Then check every declared name for a noun
in it: those are the composites, and a composite without a definition is not a
well-formed declaration. Reading the definitions on their own is the sharper
version of the table-of-contents check — one that restates its own name is a
heading, and one identical to another is two names for one thing.

Then check what your bindings feed. If nearly all of them are referenced only by
the response composition, you have recorded the topics the agent touched and lost
the reasoning that connected them.

Two habits are worth naming because they are easy to fall into. Never add
anything to satisfy a rule — not an operation, a binding, a field, a field value,
or an enum member; if a rule seems to require it, you have misread the rule. And
don't lean on one generic verb: a single operation appearing again and again with
near-identical arguments means you are walking through the reply rather than
translating it.

## Fidelity, applied

- Recover the operations a competent reader would assume happened — don't limit
  yourself to what's narrated, and don't pad in ones that aren't warranted.
- Record what each operation *produced*, not only that it ran. Where the agent
  made something — a song, a plan, a program, a comparison — what it decided
  about that thing is content, and content is statements. Where the reply shows
  its working, the working goes in a `via` scope.
- Never invent reasoning: no motive or deliberation beyond what the source
  evidences.
- Make human intent explicit, anchored to what the agent demonstrably understood
  the request to be — shown by what it did — not your own reading.
- Encode execution errors with the construct for the operation performed, putting
  the wrong result on its result line.
- Where an edit answers something the trace just surfaced — an error, a
  rejected argument, a search result — ground it in that fact rather than
  stating both side by side. The diagnosis that led to a fix is the reasoning,
  not the fix itself; leaving the link implicit throws away the point of the
  trajectory.
- Prose the agent writes between tool calls is not narration to skip past —
  a stated hypothesis about a failure's cause, a reason it rules out an
  approach, an assumption it flags as unverified: each is reasoning shown,
  same as in a chat reply, and belongs in a `via` scope or an attributed claim,
  not left out because it sits between actions instead of sentences.
- Never paste a whole function, file, or unchanged surrounding code into an
  edit's `old`/`new` (or any field standing in for them, whatever you name
  it). Find the lines that actually differ and translate each as its own
  fact — if you can't tell which lines differ, that's the sign to go back to
  the source, not to paste the block.

There is no shared corpus and no prior translated examples to retrieve against.
Make the best call from the spec and this prompt alone.

## Write your output

Actually create four files in `/output` — don't describe or quote their contents
in your reply instead of creating them. A response that talks about what these
files would contain, without the files existing, is a failed run. So is a file
that exists but is empty or a placeholder. Never write a "TODO" intending to fill
it in later; you don't get a later. Finish composing each file's content before
you write it, then write it once.

### 1. `/output/translation.bc`

The finished BrainCode document and nothing else: no commentary, no code fences,
no explanation. Never empty.

### 2. `/output/decisions.md`

Where the language came up short, plus your naming and granularity calls. Close
calls that could have gone either way belong in `uncertainties.md`; this file is
about what the vocabulary could not do. Open with a table, one row per gap:

| Wanted | Used instead | What it lost |
|---|---|---|
| `concede` | `acknowledge` | the speech act of yielding to a correction; `acknowledge` reads as neutral receipt |

Include a row whenever you invented a structural construct, used an ordinary one
that didn't really fit, or could not express something at all. Keep the `Wanted`
column to construct names or `demands:` terms, since it has to aggregate across
many documents. Use prose below the table for anything else a later reader needs.

### 3. `/output/uncertainties.md`

The hard decisions: only the forks where two or more encodings were genuinely
defensible and you had to pick, where a competent translator reading the same
turns and the same spec could have gone the other way. This file exists to find
where the *specification* is underdetermined, which is a different repair from a
missing construct. One block per fork:

```
## Retrieval vs. recall for the publication date
- Fork: searching (the reply cites a source) vs recalling (no tool call is visible)
- Chose: recalling
- Because: no search is narrated and the date is common knowledge
- Spec ref: none
```

`Spec ref:` is the important line. Cite the section that decided it if one did,
and write `none` when nothing in the spec bears on the choice — that is the
signal a later pass looks for, and guessing a section that doesn't apply destroys
it.

If there were genuinely no hard forks, the file must still contain the word
"none". Don't pad it: a run of trivial forks is worse than an honest "none",
because it hides the real ones.

### 4. `/output/keywords.md`

A classification of this trajectory, using only the terms below. Four lines, each
a label plus comma-separated terms. Don't invent terms, don't add the topic (the
folder name carries it), and don't list constructs you used, which are read from
the `.bc` file. Keep a line even if its list is empty.

```
mode:      argue
demands:   attributed-claim, multi-source-synthesis, citation
stressors: long-input, duplicated-source, heavy-redaction
strained:  cite_source, minted:corroborate
```

- **`mode:`** — exactly one: `lookup`, `explain`, `argue`, `instruct`, `create`,
  `compute`, `advise`, `critique`, `converse`.
- **`demands:`** — what the trajectory required the language to express:
  `attributed-claim`, `multi-source-synthesis`, `quantitative`, `temporal`,
  `conditional`, `procedure`, `code-artifact`, `translation`, `refusal`,
  `persona`, `self-correction`, `comparison`, `classification`, `citation`,
  `attachment`, `counterfactual`, `negation`.
- **`stressors:`** — properties of the *input* that made translation harder:
  `long-input`, `multi-party-input`, `duplicated-source`, `heavy-redaction`,
  `non-latin-fragments`, `multi-turn-revision`, `tool-results-present`,
  `ambiguous-request`, `malformed-source`.
- **`strained:`** — any operation you used that did not really fit what happened,
  plus `minted:<name>` for each structural construct you had to invent. Add
  `inexpressible` if some part of the trajectory could not be expressed at all,
  and say what in `decisions.md`.

The closed vocabulary is the point: free-text keywords don't aggregate, and a
term appearing in one document is worth nothing to the review pass.

---

All four files existing with real content is not optional and not best-effort —
it is the definition of having done this task. Do it now, for the one trajectory
attached to this message. Create the four files and stop.
