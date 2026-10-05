### S1 | type: add | dimension: constructor | symbol: object_at_location
- Needs: n11 (t2:s8)
- Searches tried: "object at location" → nothing; "entity at" → no constructor; "location of object" → nothing
- Typed parameters: object: STRING / ATOM[object_label] / ATOM[food_label], location: STRING / ATOM[object_label]
- Interpretation: Describes an object of the specified type at the specified location without asserting movement or existence.
- Example: `TERM object_at_location(object=food_label::lettuce, location=object_label::counter) -> object_at_location_2 : TERM`
- Proposed record: {"symbol":"object_at_location","kind":"constructor","signature":"TERM object_at_location(object: STRING / ATOM[object_label] / ATOM[food_label], location: STRING / ATOM[object_label]) -> TERM","definition":"A description of an object of the specified type at the specified location; asserts no action or movement.","not":"an action like place or move; it only describes a referent.","aliases":["at_location"]}