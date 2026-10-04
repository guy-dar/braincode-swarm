# Format: migration operations (drafters) and review decisions (migrator)

Nobody edits glossary files directly. **Drafters** turn consolidated suggestions into glossary operations, and the **migrator** reviews those drafts with decisions. The host then:
1. assembles the final operations;
2. applies them to `glossary.jsonl` and validates the result;
3. regenerates `glossary.md`;
4. appends provenance;
5. rebuilds the RAG index;
6. writes the migration log.

## Records: write only the authored fields

A glossary record you write has **only** these fields. The host adds `id`, `version`, shared rules, dependencies and provenance.

| field | content |
|---|---|
| `symbol` | BrainCode identifier (`snake_case`) |
| `kind` | `value`, `operation`, `speech_act`, `constructor`, `composite`, `claim_relation`, `link`, `attribute`, or `lexical_group` |
| `category` | values only: their category (e.g. `entity-name`) |
| `signature` | operations, speech acts, constructors, composites, relations and links: the typed call shape |
| `definition` | 1–2 sentences, with restrictions included. It must draw the boundary of the meaning. |
| `not` | one line: the nearest wrong reading (what this symbol does *not* mean) |
| `aliases` | contextual phrases that suggest it (optional) |
| `expansion` | composites only: the typed expansion into existing entries |
| `group` | lexical groups only: the contract (spec §3.1), defaults omitted. `{"examples": ["plant_label::fern"]}` for an open group (1–3 examples, never members); `{"admission": "standard", "standard": "iso4217", "key_form": "upper_code", "examples": [...]}` for a standard one; optional `key_aliases` {alias: canonical} |

**Leaf values are never records.** An object kind, food, animal, color, genre, country or currency that a group admits is written `group::key` and needs no op. A new group comes with an `update` of every signature that should accept it (`target: STRING / ATOM[plant_label]`) in the same ops, or it is unusable.

## 1. Drafter output: `/output/ops.jsonl`

One JSON object per line. Every consolidated suggestion of your slice must be named by at least one op, through `suggestions`, as `C#S<k>`. A rejected suggestion still needs a `reject` op.

| op | Fields | Effect |
|---|---|---|
| `add` | `record`, `suggestions` | New record. |
| `update` | `id` (or symbol), `set` {field: value}, optional `append` {`aliases`/`related`: [..]}, `reason`, `suggestions` | Changes authored fields of an existing record. |
| `merge` | `into`, `from` [ids], `notes`, `suggestions` | `from` records are deprecated into `into`; their symbols become aliases; references are re-pointed. |
| `split` | `id`, `into` [≥ 2 records], `notes`, `suggestions` | Adds the new records and deprecates the old one. |
| `deprecate` | `id`, `reason`, optional `superseded_by`, `suggestions` | Keeps the record, marked Deprecated. |
| `retire` | `id`, `reason`, `replacement` (the group value, e.g. `object_label::pillow`), `suggestions` | Deletes a leaf-value record that a group now covers. Only for leaf values; fails while anything still references it. |
| `reject` | `suggestions`, `reason` | Changes nothing; records why (e.g. "expressible as `activity(verb="walk")`"). |

```json
{"op": "add", "suggestions": ["C#S4"], "record": {"symbol": "group_size", "kind": "constructor", "signature": "TERM group_size(group: STRING / TERM, count: NUMBER) -> TERM", "definition": "The number of members of the described group; count is a nonnegative integer.", "not": "a minimum or maximum bound (use requirement)", "aliases": ["number of", "how many"]}}
{"op": "reject", "suggestions": ["C#S9"], "reason": "expressible with existing walk + destination; no new operation needed"}
```

## 2. Migrator review: `/output/review.jsonl` (+ optional `/output/rag_hints.json`)

You receive every draft op numbered `D<k>`, with the host's validation note for each. Write **one line per draft op**, plus any extra ops you add:

```json
{"draft": "D1", "decision": "approve", "reason": "clear boundary; general enough"}
{"draft": "D2", "decision": "replace", "op": {"op": "add", "suggestions": ["C#S2"], "record": {…}}, "reason": "narrowed the definition; walk_to and go_to are one operation"}
{"draft": "D3", "decision": "drop", "reason": "duplicate of D1"}
{"decision": "add", "op": {"op": "merge", "into": "v19/operation-vocabulary/walk", "from": ["v19/operation-vocabulary/walk_to"], "notes": "…", "suggestions": ["C#S5"]}, "reason": "…"}
```

- **`approve`** keeps the draft op as it is. **`replace`** uses your op instead. **`drop`** removes it. **`add`** appends a new op.
- **Every consolidated suggestion must end up named by at least one final op**, including the rejected ones (a `reject` op).
- **Keep reasons to one line.** The host builds `migration_log.md` from your decisions and reasons.

`rag_hints.json` (optional) adds retrieval cues to existing records: `{"aliases": {id: [..]}, "related": {id: [ids]}}`.

## What the host validates (one repair round, then nothing is installed)

- The fields each kind requires are present.
- Symbols are unique BrainCode identifiers.
- Every referenced id resolves.
- Composite expansions are acyclic.
- Nothing is removed except by `retire` (leaf values a group now covers), and no live record depends on a deprecated one.
- A value group's contract is valid (open groups: 1–3 examples, lower-case keys, no members; standard groups: a bundled code list) and a standard group's code list is never changed.
