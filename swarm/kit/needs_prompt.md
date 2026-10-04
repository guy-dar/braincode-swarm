You are decomposing one data item, either a single prompt or a whole human-AI conversation, into **needs**. A need is a separate meaning the item contains that a BrainCode translation will have to express. A later step searches a glossary once per need, so a meaning you leave out may never be looked up.

The item below is numbered. Each line starts with a source locator `t<turn>:s<sentence>`, followed by the speaker. Use those locators exactly.

List every need. Prefer too many over too few: retrieval is cheap, and a need left out becomes a gap in the translation. Split compound sentences. One sentence often holds an action, its object, a constraint and a negation, and those are four needs.

Need kinds:
- `action`: an operation requested, performed, or described (search, place, send, fix, compute, book…)
- `object`: an entity, resource, artifact, place or person-role that something is done to or about
- `constraint`: a requirement on a result: quantity, limit, format, tone, style, audience, inclusion, ranking
- `negation`: something excluded, refused, absent, or explicitly not wanted or not true
- `correction`: a revision, retraction, or "actually / instead / I meant" change to earlier content
- `temporal`: dates, durations, deadlines, order, before/after, frequency
- `speech_act`: what an utterance *does*: asks, informs, proposes, confirms, declines, thanks, greets, complains
- `claim`: a proposition someone states, observes, infers, assumes, or reports, together with who holds it
- `reasoning`: a because/therefore/supports/contradicts/rejects relation between claims or hypotheses

Value groups. Some leaf values are written as group values instead of glossary symbols: an object kind, a food, an animal, a color, a genre, a software platform or library, a country or a currency. When an `object` or `constraint` need names one of these, add `"group"` with the group name from this list; otherwise leave `group` out. Countries and currencies use their ISO codes later, so tag them even when the item spells out the name ("rand", "Japan").

{group_catalog}

Rules:
- `text` paraphrases the meaning in at most 25 English words, even when the item is in another language. Name the concrete thing (for example "exclude flowery language", not "a style constraint").
- `source` is the locator, or a list of locators, the need comes from.
- `group` is optional and only one of the group names above.
- Cover every turn, including assistant turns. In a long conversation, cover the main claims and moves of each turn instead of every sentence of a long answer.
- Do not invent meaning the item does not contain.
- Output only JSON: `{"needs": [{"kind": "...", "text": "...", "source": "t1:s2"}, {"kind": "object", "text": "...", "source": "t1:s3", "group": "..."}, ...]}`

Item:
{numbered_item}
