### S1 | type: add | dimension: constructor | symbol: spatial_relation
- Needs: n1 (t1:s1), n15 (t2:s4), n20 (t2:s6), n25 (t2:s8), n38-n39 (t2:s14)
- Searches tried: "next to the lettuce", "on the left side of the table", "above the lettuce" → next_to, left_of, on, under (relation values only, no constructor applying them)
- Typed parameters: subject: STRING / TERM / ATOM[object_label] / ATOM[food_label], relation: STRING, reference: STRING / TERM / ATOM[object_label] / ATOM[food_label]
- Interpretation: describes that subject stands in the relation to reference; asserts nothing.
- Example: `TERM spatial_relation(reference=food_label::lettuce, relation=next_to, subject=object_label::knife) -> spatial_relation_2 : TERM`
- Proposed record: `{"symbol": "spatial_relation", "kind": "constructor", "signature": "TERM spatial_relation(subject: STRING / TERM / ATOM[object_label] / ATOM[food_label], relation: STRING, reference: STRING / TERM / ATOM[object_label] / ATOM[food_label]) -> TERM", "definition": "Describes a spatial relation of subject to reference; asserts nothing.", "not": "a place operation", "aliases": []}`
