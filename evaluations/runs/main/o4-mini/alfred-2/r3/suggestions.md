### S1 | type: add | dimension: vocabulary-member | symbol: chill
- Needs: n1 (t1:s1)
- Searches tried: "cool lettuce slice" → no chill or cool operation; widen "chill" → no candidates
- Meaning: an operation that cools or chills the specified object in the given destination
- Category: operation
- Contextual aliases: cool, chill
- Example: `ACTION chill(target=lettuce_slice_ref, destination=object_label::fridge) -> chilled_ref : REF[STRING]`
- Contrast: not `rinse` (washing) or `heat` (warming), but lowering temperature
- Proposed record: {"symbol": "chill", "kind": "operation", "signature": "(target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING]", "definition": "Cool or chill the specified object using the given resource destination, preserving object identity.", "aliases": ["cool"]}