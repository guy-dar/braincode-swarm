### S1 | type: add | dimension: constructor | symbol: procedure_question
- Needs: n1 (t1:s1)
- Searches tried: "how to question" → property_question (wrong kind); widen "procedural question" → nothing
- Typed parameters: action: TERM
- Interpretation: an open request for a description of how to perform the given action; asserts nothing.
- Example: TERM procedure_question(action=activity(verb="mow", object=object_label::lawn)) -> q : TERM
- Proposed record:
  {"symbol":"procedure_question","kind":"constructor","signature":"TERM procedure_question(action: TERM) -> TERM","definition":"An open request for a description of how to perform the given action; asserts nothing.","not":"a property question (use property_question)","aliases":["how to","procedure question"]}

### S2 | type: add | dimension: vocabulary-member | symbol: mower_blade_height
- Needs: n8 (t2:s5)
- Searches tried: entry blade_height → none; widen "blade height" → nothing
- Meaning: the vertical setting of the cutting blades on a mower, in relation to grass height.
- Category: entity-name
- Contextual aliases: ["blade height","mower blade height"]
- Example: object_label::mower_blade_height
- Contrast: not a grass height measurement
- Proposed record:
  {"symbol":"mower_blade_height","kind":"value","category":"entity-name","definition":"The adjustable vertical setting of a lawn mower’s cutting blades relative to the grass surface.","aliases":["blade height","mower blade height"]}

### S3 | type: add | dimension: constructor | symbol: fractional_limit
- Needs: n9 (t2:s5)
- Searches tried: "one third constraint" → at_most (accepts only measures with concrete units); widen "fractional constraint" → nothing
- Typed parameters: fraction: NUMBER, of: TERM
- Interpretation: a constraint that the measured quantity of the given term may be at most the specified fraction of its whole.
- Example: TERM fractional_limit(fraction=0.3333, of=activity(verb="cut", object=object_label::lawn)) -> fl1 : TERM
- Proposed record:
  {"symbol":"fractional_limit","kind":"constructor","signature":"TERM fractional_limit(fraction: NUMBER, of: TERM) -> TERM","definition":"A constraint that the measured quantity of the given term may be at most the specified fraction of its whole.","not":"a concrete unit bound (use at_most)","aliases":["fraction limit","fractional constraint"]}

### S4 | type: add | dimension: vocabulary-member | symbol: straight_back_and_forth
- Needs: n10 (t2:s7)
- Searches tried: "straight back and forth" → nothing; widen "zigzag pattern" → nothing
- Meaning: a traversal pattern moving forward then backward in parallel lines.
- Category: topic-value
- Contextual aliases: ["back and forth","straight lines"]
- Example: TERM straight_back_and_forth() -> sbf : TERM
- Contrast: not a random or circular path
- Proposed record:
  {"symbol":"straight_back_and_forth","kind":"value","category":"topic-value","definition":"A traversal pattern in straight parallel lines forward and backward across an area.","aliases":["back and forth","straight lines"]}

### S5 | type: add | dimension: constructor | symbol: sequence
- Needs: n6, n12 (t2:s3, t2:s9)
- Searches tried: "before … then" → none; widen "sequence" → nothing
- Typed parameters: first: TERM, then: TERM
- Interpretation: denotes that the 'then' activity follows the 'first' activity in order.
- Example: TERM sequence(first=remove_debris_2, then=trim_edges_2) -> seq1 : TERM
- Proposed record:
  {"symbol":"sequence","kind":"constructor","signature":"TERM sequence(first: TERM, then: TERM) -> TERM","definition":"Denotes that the 'then' activity follows the 'first' activity in order.","not":"a logical conjunction (use conjunction)","aliases":["then after","followed by"]}

### S6 | type: add | dimension: constructor | symbol: possibility_question
- Needs: n17 (t3:s1)
- Searches tried: "possibility question" → nothing; widen "can I question" → nothing
- Typed parameters: action: TERM
- Interpretation: an open yes/no question asking whether the given action is possible.
- Example: TERM possibility_question(action=activity(verb="cut", object=object_label::grass, instrument=object_label::scissors)) -> pq : TERM
- Proposed record:
  {"symbol":"possibility_question","kind":"constructor","signature":"TERM possibility_question(action: TERM) -> TERM","definition":"An open yes/no question asking whether the specified action can be performed.","not":"a property question (use property_question)","aliases":["can I","is it possible to"]}

### S7 | type: add | dimension: constructor | symbol: limitation
- Needs: n19 (t4:s1)
- Searches tried: "possible but inefficient" → enables (wrong); widen "inefficient claim" → nothing
- Typed parameters: subject: TERM, quality: STRING
- Interpretation: asserts that the specified subject is possible but has the given limiting quality.
- Example: TERM limitation(subject=activity(verb="cut", object=object_label::grass, instrument=object_label::scissors), quality="inefficient for large lawns") -> lim1 : TERM
- Proposed record:
  {"symbol":"limitation","kind":"constructor","signature":"TERM limitation(subject: TERM, quality: STRING) -> TERM","definition":"Asserts that the specified subject is possible but has the given limiting quality.","not":"an enabling claim (use enables)","aliases":["limitation","drawback","inefficient"]}

### S8 | type: add | dimension: constructor | symbol: equipment_requirement
- Needs: n3, n4, n5 (t2:s1)
- Searches tried: "equipment requirement" → requirement (wrong signature, allows only platform_label); widen "require equipment" → nothing
- Typed parameters: item: ATOM[object_label]
- Interpretation: specifies that the given object is required equipment for an activity; asserts nothing.
- Example: TERM equipment_requirement(item=object_label::lawn_mower) -> eq1 : TERM
- Proposed record:
  {"symbol":"equipment_requirement","kind":"constructor","signature":"TERM equipment_requirement(item: ATOM[object_label]) -> TERM","definition":"Specifies that the given object-label item is required equipment for an activity; asserts nothing.","not":"a general requirement (use requirement for platform_label)","aliases":["equipment requirement","required equipment"]}
