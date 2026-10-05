### S1 | type: add | dimension: constructor | symbol: spatial_relation
- Needs: n6 (t1:s1), n15 (t2:s4), n20 (t2:s6), n25 (t2:s8), n38 (t2:s14), n39 (t2:s14)
- Searches tried: "next to the lettuce", "on the left side of the table", "above the lettuce" → only bare spatial-relation values (left_of, next_to, on, under), no TERM linking figure and ground
- Typed parameters: relation: STRING, ground: STRING / TERM / ATOM[object_label] / ATOM[food_label], figure?: STRING / TERM / ATOM[object_label] / ATOM[food_label]
- Interpretation: describes a figure standing in the spatial relation to a ground; asserts nothing. A relation `above` value should also be added.
- Example: `TERM spatial_relation(figure=object_label::knife, ground=food_label::lettuce, relation=next_to) -> spatial_relation_2 : TERM`
- Proposed record: `{"symbol": "spatial_relation", "kind": "constructor", "signature": "TERM spatial_relation(relation: STRING, ground: STRING / TERM / ATOM[object_label] / ATOM[food_label], figure?: STRING / TERM / ATOM[object_label] / ATOM[food_label]) -> TERM", "definition": "Describes a figure being in the stated spatial relation to a ground; asserts nothing.", "not": "the place operation or a claim that it holds", "aliases": []}`

### S2 | type: refine | dimension: refine-entry | target: v19/constructor/activity
- Needs: n7 (t2:s2), n9 (t2:s2), n17 (t2:s6), n18 (t2:s6), n29, n32 (t2:s12), n34 (t2:s14)
- Searches tried: "walk forward", "turn left towards" → walk/turn are ACTIONs, unusable in UTTER; activity lacks direction and destination
- Before: activity(verb, actor?, object?, location?, instrument?, purpose?)
- After: add destination?: STRING / TERM / ATOM[object_label] / ATOM[food_label] and modifier?: STRING / TERM (direction, degree or selection criterion)
- Justification: navigation and placement instructions need target place and direction
- Affected uses: none
- Compatibility: additive
- Proposed record: `{"signature": "TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM, destination?: STRING / TERM / ATOM[object_label] / ATOM[food_label], modifier?: STRING / TERM) -> TERM"}`

### S3 | type: refine | dimension: refine-entry | target: v19/constructor/requirement
- Needs: n11 (t2:s2), n33 (t2:s12)
- Searches tried: "black color" → color_label group, but requirement.value accepts only platform_label atoms
- Before: value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]
- After: also ATOM[color_label]
- Justification: color requirement on an object
- Affected uses: none
- Compatibility: additive
- Proposed record: `{"signature": "TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label] / ATOM[color_label]) -> TERM"}`
