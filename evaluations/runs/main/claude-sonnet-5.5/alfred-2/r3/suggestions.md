### S1 | type: add | dimension: constructor | symbol: entity_description
- Needs: n11 (t2:s8), n1 (t1:s1)
- Searches tried: "cut the lettuce on the counter" → slice, state_sliced, counter (slice needs REF/TERM, no TERM constructor for an unacquired object); calculation, presentation_slide (wrong meaning)
- Typed parameters: kind: STRING / ATOM[food_label] / ATOM[object_label], location?: STRING / ATOM[object_label], state?: STRING
- Interpretation: describes an object kind, optionally where it is and its state; asserts nothing, acquires no REF.
- Example: `TERM entity_description(kind=food_label::lettuce, location=object_label::counter) -> entity_description_2 : TERM`
- Proposed record: `{"symbol": "entity_description", "kind": "constructor", "signature": "TERM entity_description(kind: STRING / ATOM[food_label] / ATOM[object_label], location?: STRING / ATOM[object_label], state?: STRING) -> TERM", "definition": "Describes an entity by kind, optional location and state; asserts nothing and yields no runtime reference.", "not": "a REF to a selected object", "aliases": []}`

### S2 | type: add | dimension: vocabulary-member | symbol: step
- Needs: n9 (t2:s6), n12 (t2:s10), n14 (t2:s14), n16 (t2:s18), n19 (t2:s22)
- Searches tried: "step forward" → walk (requires destination), walk_backward (backward only), turn; "step to the left" → left_of (spatial relation), turn
- Meaning: move one short step in a given direction without a destination.
- Category: operation
- Contextual aliases: step forward, take a step
- Example: `ACTION step(direction="forward")`
- Contrast: walk (to a destination), walk_backward
- Proposed record: `{"symbol": "step", "kind": "operation", "signature": "(direction: STRING) -> void", "definition": "Move one short step in the given direction (forward, left, right, backward); no destination implied.", "not": "walk (to a destination)", "aliases": ["step forward", "take a step"]}`
