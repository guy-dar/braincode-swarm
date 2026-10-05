# Format: translator suggestions

**Final location:** `translator_suggestions/<translator_id>.md`, where `<translator_id>` is `<batch_id>-<tnum_inside_batch>` (e.g. `7-23`). This file is written only when the translation failed.

The host writes the header. The translator writes the suggestions as `/output/suggestions.md`. The inspector counts suggestions by parsing the `### S<k> | type: …` heading lines, so **the heading format is exact**.

## Part 1 — written by the host (shown for reference)

```markdown
# Suggestions from translator 7-23

- Translator ID: 7-23
- Batch: 7
- Dataset: prism
- Item ID: prism-c4905
- Glossary version: 19.0.0-draft.1+g3 (sha 1a2b3c4d5e6f)
- Translation: translations/failed/prism/7-23.md
```

## Part 2 — written by the translator: `/output/suggestions.md`

One `###` block per suggestion, numbered S1, S2, … Make one suggestion, or a few; each one must be needed to make the translation possible. Before suggesting an addition, make sure the concept truly doesn't exist: show the `search` and `widen` queries you tried.

**No values baked into symbols.** Never propose or accept a symbol whose name carries a specific number, size, age, amount or other value (`char_age_18`, `ram_16gb`, `max_5_items`). Build it from constructors with arguments instead: `measure(amount, unit)`, `at_least(...)` / `at_most(...)`, `character_trait(property, value)`, `requirement(property, value)`. Proper names that contain digits (`topic_spider_man_2`) are fine.

**No leaf values as entries.** A word a value group admits is written `group::key` (spec §3.1): never suggest `pear`, `color_ochre`, `curr_zar` or `japan` as symbols. Write `food_label::pear`, `color_label::ochre`, `currency::ZAR`, `country::JP`. When a whole kind of leaf value has no group and an operation needs it, suggest a group (`lexical-group`) instead of its members: one missing platform, language or file format is a reason for a group, not for one more entry. A single-symbol suggestion is for a meaning a label can't carry (an operation, relation, constructor, or a value whose definition matters).

### Heading line (exact)

```
### S<k> | type: add | dimension: <vocabulary-member|member-family|constructor|composite|lexical-group> | symbol: <new_symbol>
### S<k> | type: refine | dimension: <refine-entry|resolve-overlap> | target: <existing id or symbol>[, <second target>…]
```

- **`type`**: `add` means a symbol that didn't exist before. `refine` changes an existing entry, or resolves an overlap between existing entries.
- **Family counting.** A member family is one `add`: one heading, with the members listed inside.

### Required fields per dimension

Keep every field to **one line**: the migrator reads all of a batch's suggestions at once. Use the fields that apply, then end the block with a `Proposed record`: one JSON line with only the authored glossary fields (no `id`, rule links or examples; the host fills those in):

`{"symbol", "kind", "category" (values only), "signature", "definition" (1–2 sentences, restrictions included), "not" (the nearest wrong reading, one line), "aliases", "expansion" (composites only)}`

For a refine, give only the fields that change.

| Dimension | When to use it | Required fields |
|---|---|---|
| `vocabulary-member` | An existing category lacks a useful concept | Meaning, Category, Contextual aliases, Example, Contrast |
| `member-family` | Many related concepts are missing | Shared category rules, Members (explicit list, each with its individual meaning), Exceptions |
| `constructor` | Similar meanings recur with different objects, properties or values | Typed parameters, Interpretation (restrictions included), Example |
| `composite` | A recurring concept can be expressed with existing constructs | Expansion, Parameter mapping |
| `refine-entry` | An entry's meaning, signature or usage is unclear or incomplete | Before, After, Justification, Affected uses, Compatibility |
| `resolve-overlap` | Entries duplicate each other, conflate meanings or have misleading aliases | Decision (merge or split), Distinctions, Preserved references |
| `lexical-group` | A whole kind of leaf value (plants, materials…) is needed by an operation and no group covers it | Domain, Admission (`open_label`, or `standard` with its code list), Key form, Key aliases, Consuming signatures, Illustrative values (1–3, not a whitelist), Positive example, Negative example, Overlap analysis (why no existing group serves), Signature refinements, Compatibility |

A `lexical-group` proposal never lists members and comes with a `refine-entry` for every signature that should accept the group (`target: STRING / ATOM[plant_label]`): a group no signature accepts is unusable. Its proposed record is `{"symbol", "kind": "lexical_group", "definition" (the domain), "group": {"examples": ["plant_label::fern"]}}` plus any non-default `admission`/`key_form`/`key_aliases`.

Every block also has:
- **Needs:** the need ids and source locators that motivated it (e.g. `n2 (t1:s1), n7 (t3:s1)`)
- **Searches tried:** the `search`/`widen` queries, and the closest candidates with why each doesn't fit

### Example

````markdown
### S1 | type: add | dimension: constructor | symbol: group_size
- Needs: n2 (t1:s1), n8 (t4:s1)
- Searches tried: "number of children in a family" → quantity (argument name), minimum_per_period (a per-period minimum); widen "count of members in a group" → nothing
- Typed parameters: group: STRING / TERM, count: NUMBER
- Interpretation: the number of members of the described group (count a nonnegative integer); describes, asserts nothing.
- Example: `TERM group_size(count=2, group="children_in_family") -> group_size_2 : TERM`
- Proposed record: `{"symbol": "group_size", "kind": "constructor", "signature": "TERM group_size(group: STRING / TERM, count: NUMBER) -> TERM", "definition": "The number of members of the described group; count is a nonnegative integer.", "not": "a minimum or maximum bound (use requirement)", "aliases": ["number of", "how many"]}`

### S2 | type: refine | dimension: refine-entry | target: v19/composite/constraint_17_plus
- Needs: n5 (t2:s4)
- Searches tried: entry constraint_17_plus → Needs clarification
- Before: "Rated 17+ or mature" (conflates age threshold and rating system)
- After: requirement(property="minimum_age_years", value=17), only when the source states the age
- Justification: …
- Affected uses: none in the glossary examples
- Compatibility: uses that meant a rating system become unresolved
- Proposed record: `{"expansion": "requirement(property=\"minimum_age_years\", value=17)", "status": "Accepted"}`
````
