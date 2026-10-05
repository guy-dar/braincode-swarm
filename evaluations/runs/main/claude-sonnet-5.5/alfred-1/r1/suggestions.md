### S1 | type: add | dimension: constructor | symbol: entity_description
- Needs: n6 (t2:s2), n14 (t2:s4), n20 (t2:s6), n12 (t2:s4)
- Searches tried: "black color", "white color", "purple color" → color_label (slot-only on search_web/pick_up), no TERM constructor; widen "described object with color" → activity (role verb, not entity)
- Typed parameters: kind: STRING / ATOM[object_label], color?: ATOM[color_label], constraints?: LIST[TERM]
- Interpretation: describes an object of the given kind with optional color and spatial/other constraints; asserts nothing, selects no runtime reference.
- Example: `TERM entity_description(color=color_label::black, kind=object_label::end_table) -> entity_description_2 : TERM`
- Proposed record: `{"symbol": "entity_description", "kind": "constructor", "signature": "TERM entity_description(kind: STRING / ATOM[object_label], color?: ATOM[color_label], constraints?: LIST[TERM]) -> TERM", "definition": "Describes an object of a kind, optionally with a color and constraints; asserts nothing and selects no runtime object.", "not": "a runtime REF or a claim that such an object exists", "aliases": []}`

### S2 | type: add | dimension: constructor | symbol: spatial_relation
- Needs: n8 (t2:s2), n9 (t2:s2), n13 (t2:s4), n16 (t2:s4), n18 (t2:s6), n24 (t2:s8), n26 (t2:s8)
- Searches tried: "on the wall", "across from the couch", "left side of the cell phone" → on, left_of, other_side_of, behind (relation values only accepted by place.relation/walk.relation); no constructor pairing relation with reference entity
- Typed parameters: relation: STRING, reference: STRING / TERM / ATOM[object_label]
- Interpretation: a constraint that the described entity stands in the relation to the reference entity (orientation frame as per spatial-relation rule); asserts nothing. Route relations such as "through" also need a relation value or a separate path constructor.
- Example: `TERM spatial_relation(reference=object_label::ottoman, relation=on) -> spatial_relation_2 : TERM`
- Proposed record: `{"symbol": "spatial_relation", "kind": "constructor", "signature": "TERM spatial_relation(relation: STRING, reference: STRING / TERM / ATOM[object_label]) -> TERM", "definition": "A constraint that an entity stands in the spatial relation to the reference entity; asserts nothing.", "not": "the place operation or an observed position", "aliases": []}`
