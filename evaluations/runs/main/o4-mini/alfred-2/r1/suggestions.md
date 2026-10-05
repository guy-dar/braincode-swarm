### S1 | type: add | dimension: vocabulary-member | symbol: chill
- Needs: n18 (t2:s20)
- Searches tried: `rag search "cool"` → heat, rinse; `rag widen "lower temperature"` → nothing on cooling operations
- Meaning: Lower the temperature of the specified object using the stated resource; returns the same tracked identity.
- Category: operation vocabulary
- Contextual aliases: cool
- Example: `RECORD ACTION chill(target=REF[STRING], destination=ATOM[object_label]) STATUS succeeded SOURCE "t?:s?" -> chill_event : EVENT`
- Contrast: not a heating or washing operation; does not assert temperature measurement
- Proposed record: {"symbol":"chill","kind":"operation","signature":"(target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING]","definition":"Lower the temperature of the given object using the stated resource, preserving tracked identity.","not":"a heating or washing operation","aliases":["cool"]}

### S2 | type: add | dimension: constructor | symbol: object_at_location
- Needs: n11 (t2:s8), n13 (t2:s12), n15 (t2:s16), n18 (t2:s20), n20 (t2:s24)
- Searches tried: `rag search "object at location"` → none; `rag widen "object located on surface constructor"` → nothing
- Typed parameters: object: REF[STRING] / TERM, location: ATOM[object_label]
- Interpretation: Constructs a descriptive TERM for the given object at the specified location; asserts nothing.
- Example: `TERM object_at_location(object=object_label::lettuce, location=object_label::counter) -> obj_loc_2 : TERM`
- Contrast: not an executable operation or a claim; purely descriptive
- Proposed record: {"symbol":"object_at_location","kind":"constructor","signature":"TERM object_at_location(object: REF[STRING] / TERM, location: ATOM[object_label]) -> TERM","definition":"A descriptive term indicating the specified object is at the given location.","not":"an executable action or claim","aliases":["at_location"]}