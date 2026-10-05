### S1 | type: add | dimension: constructor | symbol: object_specification
- Needs: n5 (t2:s2), n6 (t2:s2), n7 (t2:s2), n8 (t2:s2), n9 (t2:s2), n10 (t2:s2), n13 (t2:s4), n14 (t2:s4), n15 (t2:s4), n16 (t2:s4)
- Searches tried: "end table on the wall across from the couch" → location_spec (address fields, wrong meaning); visual_contrast (brightness, wrong); widen "describe object by color and spatial relations" → no constructor
- Typed parameters: type: ATOM[object_label], color?: ATOM[color_label], location?: ATOM[object_label] or TERM, relation?: STRING, reference?: ATOM[object_label]
- Interpretation: describes a specific object by its type, optional color, spatial relation, and reference object; asserts nothing
- Example: `TERM object_specification(type=object_label::vase, color=color_label::white, location=object_label::table, relation="behind", reference=object_label::couch) -> vase_desc_2 : TERM`
- Proposed record: {"symbol":"object_specification","kind":"constructor","signature":"TERM object_specification(type: ATOM[object_label], color?: ATOM[color_label], location?: TERM, relation?: STRING, reference?: ATOM[object_label]) -> TERM","definition":"Describes a specific object by its type, optional color, spatial relation and reference object; asserts nothing.","not":"an action or assertion about the object","aliases":["object description"]}

### S2 | type: add | dimension: constructor | symbol: path_specification
- Needs: n18 (t2:s6), n19 (t2:s6), n20 (t2:s6), n21 (t2:s6)
- Searches tried: "go through the living room to the ottoman" → route planning (external action, wrong); location_spec (address fields, wrong); widen "describe movement through an area to a destination" → no constructor
- Typed parameters: path: STRING, destination: ATOM[object_label], color?: ATOM[color_label]
- Interpretation: describes a movement path through a named area to a destination, optionally noting color context; asserts nothing
- Example: `TERM path_specification(path="through the living room", destination=object_label::ottoman, color=color_label::purple) -> path_desc_2 : TERM`
- Proposed record: {"symbol":"path_specification","kind":"constructor","signature":"TERM path_specification(path: STRING, destination: ATOM[object_label], color?: ATOM[color_label]) -> TERM","definition":"Describes a movement path through a named area to a destination, optionally noting color context; asserts nothing.","not":"a route planning action","aliases":["route description"]}