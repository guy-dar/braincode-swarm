### S1 | type: add | dimension: constructor | symbol: wants
- Needs: n1 (t1:s1), n3 (t3:s1)
- Searches tried: "planning a trip", "want to go to Rome" → art_itinerary (artifact), search_travel (query operation), walk (locomotion); no claim relation for a holder's desire/intent
- Typed parameters: content: TERM
- Interpretation: CLAIM relation: the holder wants/intends the described activity; does not assert it occurs.
- Example: `CLAIM wants(content=activity_2) BY "user" STATUS asserted SOURCE "t1:s1" -> wants_2 : CLAIM`
- Proposed record: `{"symbol": "wants", "kind": "claim_relation", "signature": "CLAIM wants(content: TERM)", "definition": "The holder wants or intends the described activity or state; does not assert it occurs or will occur.", "not": "a request speech act or an executed action", "aliases": ["want to", "intend to", "planning"]}`

### S2 | type: add | dimension: constructor | symbol: property_question
- Needs: n2 (t2:s5, t2:s7, t2:s9, t2:s11, t2:s13)
- Searches tried: "ask destination dates party size budget" → ask, requirement, group_size (assert/specify values, not questions); widen → nothing
- Typed parameters: subject: STRING / TERM, property: STRING
- Interpretation: asks for the named property of the subject, without presupposing an answer; asserts nothing.
- Example: `TERM property_question(property="destination", subject=activity_3) -> property_question_2 : TERM`
- Proposed record: `{"symbol": "property_question", "kind": "constructor", "signature": "TERM property_question(subject: STRING / TERM, property: STRING) -> TERM", "definition": "Asks for the named property of the subject, without presupposing an answer.", "not": "an assertion of a property value (use attribute_claim)", "aliases": ["what is the property of"]}`
