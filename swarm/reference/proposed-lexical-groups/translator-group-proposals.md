# Proposed translator suggestion extension

Status: documentation proposal; the current host schema and migrator do not yet implement it.

Once the atomic-group mechanism is implemented, translators can suggest new groups without editing the specification. The glossary owns the group inventory and its consuming signatures. A group is not an inline declaration in a translation.

Keep the existing exact suggestion heading structure and add the dimension `lexical-group`:

```text
### S1 | type: add | dimension: lexical-group | symbol: plant_label
```

Each block retains Needs and Searches tried and supplies: Domain, Admission, Key form, Members (registered only), Key aliases, Consuming signatures, Illustrative values (not a whitelist), Positive example, Negative example, Overlap analysis, Signature refinements, Compatibility, and Proposed record. Each field stays on one line. The proposed record has kind lexical_group, status Proposed, definition, and the nondefault group fields from specification Section 3.1. definition supplies the domain; omit default fields. The host assigns IDs, versions and dependencies after review. Do not use natural-language aliases as automatic key normalization.

Example proposal (illustrative only; this group is absent from the candidate glossary):

```json
{"symbol":"plant_label","kind":"lexical_group","status":"Proposed","definition":"A source-supplied plant-kind label; no inferred species, toxicity or care requirements.","group":{"examples":["plant_label::begonia","plant_label::fern"]}}
```

This proposal must include a companion refine-entry suggestion extending search_web.target with ATOM[plant_label]. The reviewer must decide whether existing object_label already serves the supplied need; reject a redundant group unless the consuming role needs a plant-specific distinction. The example is not automatic justification for adding it.

For registered-member additions or alias changes, use refine-entry on the lexical_group record, preserving the complete existing member map and unchanged sense IDs. For a new consuming position, propose its exact signature in the same transaction; do not duplicate a slot list in the group record. Do not propose a spec edit for an ordinary group or member addition.

Review sequence:

1. Check the source need, existing vocabulary, and whether a label preserves enough meaning. An unresolved English sense cannot be repaired by putting it into a broader group.
2. Compare domain, admission, and consumers against existing groups. Merge genuinely identical same-batch proposals; retain different senses. Aliases must not erase distinctions such as phone versus smartphone.
3. Validate the complete group contract, alias targets, member uniqueness, namespace collisions, and every affected signature. Reject hidden sentences, arbitrary predicates, executable validators, wildcard consumers and implicit casts.
4. Accept the group, dependent signatures and retrieval metadata atomically into a new glossary revision. Keep the current batch frozen and retry affected items using the new release.
5. Preserve old revisions. A breaking domain/identity change requires explicit migration, not reinterpretation of earlier documents.

Compact-glossary acceptance requirements:

- Do not propose an individual row for a new leaf word already admitted by an open group. Translate it directly and report label-only coverage where needed.
- An open group omits members (default empty) and supplies only a few illustrative examples. Do not paste a dataset's entire noun list into examples, aliases or exceptions.
- Group proposals identify standalone rows they can replace and exact consuming signature changes. State whether each mapping preserves a pinned identity or only a nominal label and role. Retain needed semantic exceptions.
- Remove migrated rows from the new active release; retain old releases and an offline audit map. Reject a proposal that merely duplicates the old enumeration without a reason.
- Report net active-record change and total bytes, including any registered member definitions. A smaller record count is not proof that knowledge storage shrank.

One-time host changes required before use: recognize lexical_group and the authored group field; extend suggestion parsing/counting to lexical-group; validate and atomically apply related operations; render/index the full contract; retrieve allowed groups by expected parameter type, even when a new word has no exact vocabulary match; pin all registry data; and report label-preserved spans separately. Existing tooling can reject or omit these new fields, so do not install this folder into the live swarm as if it were already supported.
