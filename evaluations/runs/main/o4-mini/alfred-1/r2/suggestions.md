### S1 | type: add | dimension: lexical-group | symbol: furniture_label
- Needs: n19 (t2:s6)
- Searches tried:  
  • rag search "living room" → found only location-name::living_room (cannot fill object_label slots)  
  • rag widen "indoor furniture label" → no matching group
- Domain: a source-supplied label for indoor furniture items or fixtures; denotes the labeled furniture without inferred properties.
- Admission: open_label
- Key form: lower_word
- Consuming signatures: pick_up.target, place.destination, walk.destination
- Illustrative values: furniture_label::sofa, furniture_label::chair
- Proposed record: {"symbol":"furniture_label","kind":"lexical_group","definition":"A source-supplied label for indoor furniture items or fixtures; denotes that labeled furniture without inferred properties.","group":{"examples":["furniture_label::sofa"]}}

### S2 | type: add | dimension: constructor | symbol: colored_object
- Needs: n6 (t2:s2), n14 (t2:s4), n20 (t2:s6)
- Searches tried:
  • rag search "colored object" → no TERM constructor  
  • rag widen "object with color qualifier" → nothing suitable
- Typed parameters: object: STRING / ATOM[object_label], color: ATOM[color_label]
- Interpretation: describes the specified object qualified by the given color; asserts nothing.
- Example: TERM colored_object(object=object_label::night_stand, color=color_label::black) -> colored_object_2 : TERM
- Proposed record: {"symbol":"colored_object","kind":"constructor","signature":"TERM colored_object(object: STRING / ATOM[object_label], color: ATOM[color_label]) -> TERM","definition":"A description of the specified object qualified by the given color; asserts nothing.","not":"a claim of colored light or surface state","aliases":["colored","color"]}