### S1 | type: refine | dimension: refine-entry | target: v19/construction/activity
- Needs: n1 (t1:s1)
- Searches tried: entry activity → location only accepts STRING/ATOM[country]; widen "location ATOM[object_label]" → nothing
- Before: `activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM`
- After: `activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country] / ATOM[object_label], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM`
- Justification: spatial destinations like tables are object labels, not countries.
- Compatibility: backward-compatible; no existing uses broken
- Proposed record: `{"signature":"TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country] / ATOM[object_label], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM"}`

### S2 | type: add | dimension: constructor | symbol: entity_reference
- Needs: n15 (t2:s4), n16 (t2:s4), n25 (t2:s8), n39 (t2:s14)
- Searches tried: "closest X to Y" → nothing; "object selection by spatial relation" → nothing
- Typed parameters: kind: ATOM[object_label] / STRING, relation: ATOM[spatial_relation], reference: STRING / TERM / ATOM[object_label], rank?: NUMBER, position?: STRING
- Interpretation: selects a specific object instance of the given kind by its spatial relation to a reference object; optional `rank` for nth‐closest, optional `position` for qualifiers like "back_left" or "above".
- Example:
  TERM entity_reference(kind=object_label::knife, relation=spatial_relation::next_to, reference=object_label::lettuce, rank=1) -> knife_ref : TERM
- Proposed record: `{"symbol":"entity_reference","kind":"constructor","signature":"TERM entity_reference(kind: ATOM[object_label] / STRING, relation: ATOM[spatial_relation], reference: STRING / TERM / ATOM[object_label], rank?: NUMBER, position?: STRING) -> TERM","definition":"Selects a particular object instance of the given kind by its spatial relation to a reference entity; optional rank for closest/second‐closest and position qualifiers like 'back_left' or 'above'.","not":"A CLAIM or execution of the action itself","aliases":["select_object","object_at"]}`

### S3 | type: add | dimension: constructor | symbol: requirement
- Needs: n11 (t2:s2)
- Searches tried: entry requirement → exists, but property parameter only accepts STRING / NUMBER / BOOL / TERM / ATOM[platform_label]; widen "requirement color value" → nothing
- Before: `TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM`
- After: allow `value` to accept ATOM[color_label] for color constraints
- Justification: color constraints use atomic color labels
- Proposed record: `{"signature":"TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label] / ATOM[color_label]) -> TERM","definition":"Specifies a required property constraint with an expected primitive or structured value; supports color labels.","not":"Asserting observation; it only constrains desired properties","aliases":["constraint","property_requirement"]}`
