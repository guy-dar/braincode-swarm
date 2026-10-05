### S1 | type: add | dimension: constructor | symbol: spatial_relation
- Needs: n8, n9, n13, n16, n24, n26 (t2:s2, t2:s4, t2:s8)
- Searches tried: "behind the vase", "on the left side of the cell phone" → left_of/behind/on (STRING values for place.relation only); no constructor with figure and ground
- Typed parameters: relation: STRING, figure: STRING / TERM / ATOM[object_label], ground: STRING / TERM / ATOM[object_label]
- Interpretation: describes that the figure stands in the relation to the ground; asserts nothing.
- Example: `TERM spatial_relation(figure=object_label::keys, ground=object_label::vase, relation=behind) -> spatial_relation_2 : TERM`
- Proposed record: `{"symbol": "spatial_relation", "kind": "constructor", "signature": "TERM spatial_relation(relation: STRING, figure: STRING / TERM / ATOM[object_label], ground: STRING / TERM / ATOM[object_label]) -> TERM", "definition": "Describes a spatial relation (spatial-relation category value) of a figure to a ground entity; asserts nothing.", "not": "place.relation, which only parameterizes the place operation", "aliases": []}`

### S2 | type: add | dimension: constructor | symbol: described_entity
- Needs: n6, n14, n20 (t2:s2, t2:s4, t2:s6)
- Searches tried: "black color", "white vase", "purple ottoman" → color_label (only pick_up/search_web slots), color_pink; nothing attaches a color/constraints to an entity
- Typed parameters: kind: ATOM[object_label], color?: ATOM[color_label], constraints?: LIST[TERM]
- Interpretation: description of an entity kind narrowed by color and constraints; asserts nothing.
- Example: `TERM described_entity(color=color_label::black, kind=object_label::endtable) -> described_entity_2 : TERM`
- Proposed record: `{"symbol": "described_entity", "kind": "constructor", "signature": "TERM described_entity(kind: ATOM[object_label], color?: ATOM[color_label], constraints?: LIST[TERM]) -> TERM", "definition": "An entity description: a kind narrowed by an optional color and constraints; selects nothing and asserts nothing.", "not": "a REF to a particular runtime object", "aliases": []}`
