### S1 | type: add | dimension: constructor | symbol: entity_attribute
- Needs: n15 (t1:s9), n16 (t1:s10), n18 (t1:s11), n19 (t1:s12), n20 (t1:s13), n21 (t1:s14), n22 (t1:s15)
- Searches tried: "nice people are cold" -> state_cold; "kind people are not red" -> stereotype, negation; widen "if someone is young then they are rough" -> then, character_trait
- Typed parameters: entity: STRING / TERM, property: STRING / TERM
- Interpretation: A descriptive term representing an entity or variable possessing a property or attribute; purely descriptive, asserts nothing.
- Example: `TERM entity_attribute(entity=character_charlie, property="rough") -> entity_attribute_2 : TERM`
- Proposed record: `{"symbol": "entity_attribute", "kind": "constructor", "signature": "TERM entity_attribute(entity: STRING / TERM, property: STRING / TERM) -> TERM", "definition": "A descriptive term representing an entity or general class possessing a named attribute or property. Purely descriptive, asserts nothing.", "not": "has_attribute (which is an asserted claim relation) or character_trait (which lacks an entity argument)", "aliases": ["has_property", "entity_property", "attribute_term"]}`

### S2 | type: add | dimension: constructor | symbol: deduction_query
- Needs: n23 (t1:s16), n24 (t1:s16), n25 (t1:s16)
- Searches tried: "answer must be True, False, or Unknown" -> metric_order_late, constraint_realistic; widen "base the answer only on the provided theory" -> regression_case, subject
- Typed parameters: claim: CLAIM / TERM, choices?: LIST[STRING], scope?: STRING / TERM
- Interpretation: A query term specifying a deduction problem asking for the truth evaluation of a claim within a specified premise scope over target choice options.
- Example: `TERM deduction_query(choices=["True", "False", "Unknown"], claim=has_attribute_9, scope="theory") -> deduction_query_2 : TERM`
- Proposed record: `{"symbol": "deduction_query", "kind": "constructor", "signature": "TERM deduction_query(claim: CLAIM / TERM, choices?: LIST[STRING], scope?: STRING / TERM) -> TERM", "definition": "Constructs a descriptive representation of a logical deduction query evaluating the truth status of a claim with respect to a designated premise scope against candidate truth values.", "not": "property_question (an open question about an entity property) or confirm (a speech act confirming a claim)", "aliases": ["theory_query", "logic_question", "truth_evaluation_query"]}`
