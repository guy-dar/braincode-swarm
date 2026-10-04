# Format: failed translation

**Final location:** `translations/failed/<dataset>/<translator_id>.md`, where `<translator_id>` is `<batch_id>-<tnum_inside_batch>`. A failed translation always comes with a suggestions file, `translator_suggestions/<translator_id>.md` (see `suggestions.md`).

**When to fail.** A translation fails when, after widening the search for every unresolved need, at least one need can only be expressed with a glossary symbol or definition that doesn't exist yet, or with an existing entry whose meaning or signature is wrong for it. Failing is not a mistake: the swarm grows the glossary from exactly these cases.

As with successes, the host writes the header and the original data item (title `# Translation 7-23 — failed`, same metadata lines as `successful_translation.md`). The translator writes only the body, as `/output/translation.md`.

## Part 2 — written by the translator: `/output/translation.md`

````markdown
Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM family_size(count=2) -> family_size_2 : TERM   # PROPOSED: S1
    UTTER ask(target=family_size_2)
  }
  ...
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | object | family_size (PROPOSED: S1) | proposed |
| n7 | claim | — | unresolved |

## Why the translation failed

- n2 "ideal number of children in a family": search "number of children" → only `quantity` (an argument name) and `minimum_per_period` (a per-period minimum, wrong meaning); widen → nothing for counting members of a group. Proposed S1.
- n7 …

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: …
- Opaque-text spans: …
- Missing constructs: S1 family_size constructor; S2 refinement of …
- Unresolved ambiguities: …
- Check: `rag check` reported 2 unresolved needs (n2, n7), 1 unknown symbol (family_size, proposed)
````

### Rules

- **Status line.** The first line is exactly `Status: failed`, and the second is `Mode: REQUEST|TRACE`.
- **Suggested translation.** It is the best complete document the translator can produce if its suggestions were accepted. Every line that uses a proposed or refined symbol carries a `# PROPOSED: S<k>` or `# REFINED: S<k>` comment naming the suggestion that would make it valid. Everything else must already be valid against the current glossary.
- **Needs coverage.** It has the same table as for a success, with two extra status values: `proposed` (covered once suggestion S<k> is accepted) and `unresolved`.
- **Why the translation failed.** Every `proposed` or `unresolved` need gets an entry, listing the searches tried (`search` / `widen` queries and what they returned) and why each close candidate doesn't fit. This is the evidence the migrator weighs.
- **Suggestions.** Every suggestion in the suggestions file must be referenced at least once in this document.
