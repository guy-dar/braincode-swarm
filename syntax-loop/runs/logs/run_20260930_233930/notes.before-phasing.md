# BrainCode fundamental notes

Your steering notes for the syntax loop. The loop only **reads** this file — it never edits it.
While any note below is open, each sprint focuses on the next open one (hard notes first, then
file order) instead of a random seed task; every role sees all notes in every sprint, and the
Critic judges each one per attempt. Status is tracked in `docs/notes-status.json` — editing a
note's text reopens it. See `config/config.yaml -> run.steering`.

Format — one level-2 heading per note, optional explanation lines underneath:

    ## N<number> [hard|direction] <one-line statement>
    Optional detail: why, what "done" looks like, examples.

- `hard` — a constraint. No change may violate it; the Shaper cannot argue against it.
- `direction` — a goal. The Shaper should realize it, but may contest it with evidence; the
  Critic rules on that argument (an accepted contest marks the note `declined`).

<!-- Examples (inside this comment, so they're ignored):

## N1 [hard] No construct may take another construct inline as an argument.
Composition always goes through a named Bind — keep it that way in every change.

## N2 [direction] Collapse ACTION, UTTER and GENERATE into a single effect construct.
They differ only in what the effect targets; one construct with a `kind` attribute should do.

-->

## Notes

## N1 [hard] Closed vocabulary: every symbol used in a BrainCode expression is defined in the glossary.
No token may appear in an expression unless the glossary defines it directly, or defines the rule
that produces it. This covers keywords, operators, construct names, types, attribute names,
attribute values, actions, objects and identifiers. A defining rule can be, for example, a
category such as "object" whose members are glossary entries, or a literal form such as NUMBER.
A reader holding only the spec and the glossary must be able to look up every token in any
expression. Done when: the grammar has no free-text slot, and the Critic can trace every token
in every simulated item to a glossary entry or to a glossary-defined category.

## N2 [hard] The glossary is the complete lexicon of the language, covering every kind of word, not only operators.
The glossary is organized by category and covers three groups. (a) Structural words: keywords,
operators, delimiters and types. (b) Key terms: construct names and what they do. (c) Descriptive
vocabulary: actions/verbs, objects and entities, roles and recipients, attributes (e.g. tone,
register, priority, format), and each attribute's allowed values. Every category gets a
plain-language gloss, its members (or the rule that defines membership), and a worked example.
Today the glossary has one entry per construct only; the descriptive vocabulary must be added as
glossary categories of its own.

## N3 [hard] Every attribute value is a glossary symbol, or is derived from glossary symbols by a glossary-defined rule.
An attribute such as tone, register, format or content accepts only the values the glossary
defines for that attribute, e.g. tone = one of {formal, polite, neutral, urgent, ...}. A value may
also be reached indirectly: a list of such values, a reference to a bound variable holding one,
or a member of a glossary category. A value may never be an undefined word, a phrase, or a
free-form description. Each attribute's entry in the glossary lists its value set.

## N4 [hard] No natural-language sentences or fragments anywhere inside an expression.
No attribute, argument or payload may contain full or partial natural-language text. That
includes free-form tone descriptions and message content, e.g.
content="ask for a two-day extension, politely" is not allowed. Prose inside an expression hurts
Expressivity, because meaning hides in text the language does not structure. It also hurts
Determinism, because two translators will phrase the same content differently. Content must be
expressed with glossary symbols and constructs instead, e.g. an intent symbol request_extension
with duration=2 and unit=day, and tone=polite. If the language cannot express something yet, the
language must be extended; prose is never the fallback. This overrides the earlier allowance for
opaque prose payloads in open, conversational items: their content, not only their
meta-structure (intent, recipient, register, constraints), must now be encoded symbolically. The
only exception is the atomic literals defined under N5.

## N5 [hard] The language is self-contained; natural language may contribute only atomic symbols that the glossary defines as such.
Reading or writing BrainCode must not depend on English grammar or an English dictionary;
everything the language uses is pre-defined in its own spec and glossary. A natural-language word
may be used only when the glossary adopts it as an atomic symbol with its own definition, e.g.
the action symbol send or the object symbol mug. Its meaning then comes from the glossary entry,
not from English. It cannot be inflected, conjugated, or combined using English syntax. Genuinely
open-ended values need a glossary-defined literal category with a precise, atomic form (a single
token, never a phrase). Examples are proper names, numbers, dates, times, URLs and file paths.
This keeps them atomic even though their exact values cannot all be listed in advance.

## N6 [direction] Write the syntax assuming the full glossary already exists.
The grammar is defined over glossary categories (e.g. <action>, <object>, <tone-value>), not over
the particular words that happen to be listed today. When a simulated item needs a word the
glossary does not list yet (e.g. a specific object), assume the complete glossary contains it in
the right category and write it as that category's symbol. Do not reshape the syntax around a
missing entry, and do not fall back to prose (N4). The Critic should not penalize a missing
entry within an existing category. It should penalize a missing category: if no category could
hold the needed symbol, the language has a real gap and must add that category.

## N7 [hard] Encoding is deterministic; decoding should be as deterministic as richness allows.
Encoding (natural-language request to BrainCode) is the hard constraint. It must yield one
canonical expression per meaning, which requires three things. First, a fixed order for
arguments and attributes, or a canonical ordering rule. Second, exactly one construct per
concept, with no two equivalent ways to say the same thing. Third, one canonical symbol wherever
natural language has synonyms: the glossary names the canonical symbol and lists the
natural-language synonyms that map to it. Done when: independent translators (different models,
or repeated runs) produce the same expression for the same request.
Decoding (BrainCode back to meaning or to natural language) is a goal, not a constraint. Every
expression must still have exactly one parse. Its reading should be as precise as possible, but
complete determinism in this direction is acknowledged to be impossible. A symbolic expression
cannot pin down every nuance a natural-language rendering could carry, and the richer the
language, the more ways a decoder can render it. Imperfect decoding determinism therefore does
not by itself violate this note, while ambiguous parsing does. The Critic judges the quality of
decoding under N8, as a trade-off against richness.

## N8 [direction] Keep the language as rich as possible within the determinism and closed-vocabulary constraints.
The closed vocabulary (N1-N5) and determinism (N7) should not make the language poor. Prefer an
expressive glossary over collapsing distinct meanings into one coarse symbol: fine-grained
attribute values, composable modifiers, quantities, conditions, references and relations.
Determinism wins where the two genuinely conflict. Before giving up richness, though, the Shaper
should look for a way to keep both, e.g. a deterministic composition rule over glossary symbols
instead of one broad symbol. The Critic should flag any simulated item whose meaning was lost to
over-coarse symbols. This note also covers decoding (see N7). Richness may cost some decoding
determinism, but a reader or model decoding an expression should still converge on the same core
meaning (intent, participants, constraints, ordering), even if the surface wording differs. Where
extra richness makes the decoded meaning itself diverge, the Critic should weigh that against the
expressivity it adds.
