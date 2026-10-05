### S1 | type: add | dimension: constructor | symbol: assert_variable_assigned
- Needs: n7 (t1:s10)
- Searches tried: "variable remains unassigned" → nothing; widen "assert variable assigned" → nothing
- Typed parameters: variable: TERM
- Interpretation: Asserts that the specified variable has been assigned a value; no runtime effect.
- Example: TERM assert_variable_assigned(variable=seq_length_var) -> assert_seq_assigned : TERM
- Proposed record: {"symbol":"assert_variable_assigned","kind":"constructor","signature":"TERM assert_variable_assigned(variable: TERM) -> TERM","definition":"Asserts that the specified variable has been assigned a value; no runtime effect.","not":"A test of truthiness or exception raising","aliases":["check_assigned","require_assignment"]}

### S2 | type: add | dimension: constructor | symbol: assert_unpack_missing
- Needs: n8 (t1:s19)
- Searches tried: "missing unpack seq_length" → nothing; widen "report missing unpacking of variable" → nothing
- Typed parameters: variable: TERM
- Interpretation: Denotes that the code path omits unpacking of the specified variable; no execution.
- Example: TERM assert_unpack_missing(variable=inputs_embeds_var) -> assert_unpack_missing : TERM
- Proposed record: {"symbol":"assert_unpack_missing","kind":"constructor","signature":"TERM assert_unpack_missing(variable: TERM) -> TERM","definition":"Denotes that the code path omits unpacking of the specified variable; no execution.","not":"An actual unpack operation","aliases":["missing_unpack","unpack_not_performed"]}