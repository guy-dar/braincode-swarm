### S1 | type: add | dimension: constructor | symbol: property_question
- Needs: n2 (t2:s5, t2:s7, t2:s9, t2:s11, t2:s13)
- Searches tried: "ask questions to gather trip requirements" → ask, requirement, group_size (no question constructor); not widened further
- Typed parameters: subject: STRING / TERM, property: STRING
- Interpretation: asks for the named property of the subject, presupposing no answer; asserts nothing.
- Example: `TERM property_question(property="destination", subject="trip") -> property_question_2 : TERM`
- Proposed record: `{"symbol": "property_question", "kind": "constructor", "signature": "TERM property_question(subject: STRING / TERM, property: STRING) -> TERM", "definition": "Asks for the named property of the subject without presupposing an answer.", "not": "an assertion of the answer", "aliases": []}`

### S2 | type: add | dimension: constructor | symbol: desires
- Needs: n3 (t3:s1), n5, n6, n7, n8, n9 (t3:s1, t3:s2)
- Searches tried: "user wants to travel / requests" → recommended, requirement, obligation (wrong attitude)
- Typed parameters: target: TERM
- Interpretation: CLAIM relation that the holder wants the described activity or requirement to hold; does not assert it occurs.
- Example: `CLAIM desires(target=activity_2) BY user STATUS asserted SOURCE "t3:s1" -> desires_2 : CLAIM`
- Proposed record: `{"symbol": "desires", "kind": "claim_relation", "signature": "CLAIM desires(target: TERM)", "definition": "The holder wants the described activity or requirement to be realized.", "not": "obligation or recommendation", "aliases": ["wants"]}`

### S3 | type: add | dimension: constructor | symbol: has_property
- Needs: n11 (t4:s15, t4:s16), n14 (t4:s44)
- Searches tried: "property of destination heat crowds expensive" → heat (operation), outcome, provides, important; none fit
- Typed parameters: subject: STRING / TERM, property: STRING, value: STRING / NUMBER / BOOL / TERM
- Interpretation: CLAIM that the subject has the property with the value.
- Example: `CLAIM has_property(subject=activity_3, property="hot_in_july", value=TRUE) BY agent STATUS asserted SOURCE "t4:s15" -> has_property_2 : CLAIM`
- Proposed record: `{"symbol": "has_property", "kind": "claim_relation", "signature": "CLAIM has_property(subject: STRING / TERM, property: STRING, value: STRING / NUMBER / BOOL / TERM)", "definition": "The subject has the named property with the given value.", "not": "a requirement constraint", "aliases": ["attribute_claim"]}`
