### S1 | type: add | dimension: constructor | symbol: entity_trait
- Needs: n2 (t1:s2), n3 (t1:s3), n4 (t1:s4), n5 (t1:s5), n6 (t1:s6), n7 (t1:s7), n8 (t1:s8), n9 (t1:s9), n10 (t1:s10), n11 (t1:s11), n12 (t1:s12), n13 (t1:s13), n14 (t1:s14), n15 (t1:s15), n16 (t1:s16), n17 (t1:s17), n18 (t1:s18), n19 (t1:s19), n20 (t1:s20), n24 (t1:s22)
- Searches tried: "Erin is furry" → comfortable, yarn, dog; "Erin is quiet" → comfortable, unaware; "Gary is smart" → right_of, style_catchy; widen "entity property trait" → attribute_claim, character_trait
- Typed parameters: entity: STRING / TERM, property: STRING
- Interpretation: A descriptive term representing that an entity or variable possesses a specified property or trait, suitable for composition inside logical rules and conditions; describes, asserts nothing on its own.
- Example: `TERM entity_trait(entity="Erin", property="furry") -> entity_trait_2 : TERM`
- Proposed record: {"symbol": "entity_trait", "kind": "constructor", "signature": "TERM entity_trait(entity: STRING / TERM, property: STRING) -> TERM", "definition": "A descriptive term representing that an entity or variable possesses a specified property or trait.", "not": "attribute_claim (which is an attributed CLAIM relation, not a composable TERM) or character_trait (restricted to fictional characters)", "aliases": ["trait", "has_property", "predicate"]}

### S2 | type: add | dimension: constructor | symbol: variable
- Needs: n13 (t1:s13), n14 (t1:s14), n15 (t1:s15), n16 (t1:s16), n17 (t1:s17), n18 (t1:s18), n19 (t1:s19)
- Searches tried: "If someone is nice" → comfortable, tone_polite; "All red people" → foreigners, color_label; widen "logical variable or quantifier" → ALL, ANY (structural keywords in check expressions only)
- Typed parameters: name: STRING
- Interpretation: Constructs a descriptive representation of a logical variable or unbound generic entity for quantified rules and implications.
- Example: `TERM variable(name="x") -> variable_2 : TERM`
- Proposed record: {"symbol": "variable", "kind": "constructor", "signature": "TERM variable(name: STRING) -> TERM", "definition": "Constructs a descriptive representation of a logical variable or unbound generic entity in quantified rules and logical propositions.", "not": "subject (which represents concrete qualified subject matter) or a literal entity name", "aliases": ["logic_variable", "generic_subject", "unbound_entity"]}

### S3 | type: add | dimension: constructor | symbol: evaluate_truth
- Needs: n21 (t1:s21), n22 (t1:s21), n23 (t1:s21)
- Searches tried: "Determine the truth value of a statement" → statement, test_condition, failure; "Base evaluation on theory" → test_condition, subject; "Limit answer options to True, False, or Unknown" → select_option, constraint_single_choice; widen "evaluate truth value against theory" → nothing
- Typed parameters: basis?: STRING / TERM, options?: LIST[STRING], statement: TERM
- Interpretation: Constructs a descriptive query requesting evaluation of a statement's truth value relative to a specified theory or basis with given answer options.
- Example: `TERM evaluate_truth(basis="theory", options=["True", "False", "Unknown"], statement=entity_trait_20) -> evaluate_truth_2 : TERM`
- Proposed record: {"symbol": "evaluate_truth", "kind": "constructor", "signature": "TERM evaluate_truth(basis?: STRING / TERM, options?: LIST[STRING], statement: TERM) -> TERM", "definition": "Constructs a descriptive query requesting the truth-value evaluation of a statement relative to a specified theory or knowledge base under given discrete answer options.", "not": "test_condition (software testing assertion) or statement (an attributed factual claim)", "aliases": ["truth_value_query", "evaluate_statement", "query_truth"]}
