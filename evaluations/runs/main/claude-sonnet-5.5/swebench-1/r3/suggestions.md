### S1 | type: add | dimension: constructor | symbol: variable_unassigned
- Needs: n7 (t1:s10)
- Searches tried: "variable unassigned in execution path" → raises_exception (the error itself), has_state (physical state), leads_to; widen → nothing
- Typed parameters: variable: STRING, entity: TERM, path?: STRING / TERM
- Interpretation: claim relation; the variable has no value on the described execution path of the code entity.
- Example: `CLAIM variable_unassigned(variable="seq_length", entity=code_entity_4, path="inputs_embeds_branch")`
- Proposed record: `{"symbol": "variable_unassigned", "kind": "claim_relation", "signature": "CLAIM variable_unassigned(variable: STRING, entity: TERM, path?: STRING / TERM)", "definition": "The variable is not assigned on the described execution path of the code entity.", "not": "raises_exception (the resulting error)", "aliases": ["unbound_variable"]}`

### S2 | type: add | dimension: constructor | symbol: reads_variable
- Needs: n6 (t1:s6, s7, s8)
- Searches tried: "slicing uses variable" → slice, state_sliced, validates_parameter; none fits
- Typed parameters: entity: TERM, variable: STRING, condition?: STRING / TERM
- Interpretation: claim relation; the code entity reads the variable, optionally only under the condition.
- Example: `CLAIM reads_variable(entity=code_entity_3, variable="seq_length", condition="token_type_ids_is_none")`
- Proposed record: `{"symbol": "reads_variable", "kind": "claim_relation", "signature": "CLAIM reads_variable(entity: TERM, variable: STRING, condition?: STRING / TERM)", "definition": "The code entity reads the variable, optionally only when the condition holds.", "not": "validates_parameter", "aliases": ["uses_variable"]}`

### S3 | type: add | dimension: constructor | symbol: lacks_statement
- Needs: n8 (t1:s13–s19)
- Searches tried: "branch omits assignment unpacking" → duplicate_definition, modify_code, code_entity; none fits
- Typed parameters: entity: TERM, statement: STRING, branch?: STRING / TERM
- Interpretation: claim relation; the code entity lacks the exact statement in the branch.
- Example: `CLAIM lacks_statement(entity=code_entity_4, statement="batch_size, seq_length = input_shape", branch="inputs_embeds is not None")`
- Proposed record: `{"symbol": "lacks_statement", "kind": "claim_relation", "signature": "CLAIM lacks_statement(entity: TERM, statement: STRING, branch?: STRING / TERM)", "definition": "The code entity does not contain the literal statement, within the branch if given.", "not": "exclude (a requirement)", "aliases": ["missing_statement"]}`

### S4 | type: add | dimension: constructor | symbol: alternatives
- Needs: n9 (t1:s20)
- Searches tried: "either bug or misuse" → conjunction (all apply), conditional, sequence; none is a disjunction
- Typed parameters: items: LIST[STRING] / LIST[TERM]
- Interpretation: describes a set of mutually considered alternatives (one-of); asserts nothing.
- Example: `TERM alternatives(items=["bug_missing_unpacking", "user_misuse_of_model"])`
- Proposed record: `{"symbol": "alternatives", "kind": "constructor", "signature": "TERM alternatives(items: LIST[STRING] / LIST[TERM]) -> TERM", "definition": "At least the described alternatives are the candidate options; asserts none.", "not": "conjunction (all apply)", "aliases": ["either_or", "one_of"]}`
