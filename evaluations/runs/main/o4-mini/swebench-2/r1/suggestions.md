### S1 | type: add | dimension: constructor | symbol: implement_method
- Needs: n2 (t1:s1), n3 (t1:s1)
- Searches tried: "Implement __nonzero__" → modify_code (requires a TERM revision), chg_modify_code (requires a TERM revision description); widen "method implementation term" → no candidates
- Typed parameters: subject: TERM
- Interpretation: Describes the implementation of the specified method or code entity; asserts no execution or outcome.
- Example: `TERM implement_method(subject=code_entity(kind="method", name="__nonzero__", project=platform_label::pandas)) -> implement_method_2 : TERM`
- Proposed record: {"symbol":"implement_method","kind":"constructor","signature":"TERM implement_method(subject: TERM) -> TERM","definition":"Describes the implementation of the specified method or code entity; asserts nothing.","not":"A runtime action or factual claim of completion","aliases":["add_method","create_method"]}

### S2 | type: add | dimension: constructor | symbol: test_truthiness
- Needs: n5 (t1:s2), n6 (t1:s2)
- Searches tried: "test boolean emptiness" → test_condition (expects condition string), widen "boolean test for object emptiness" → no candidates
- Typed parameters: subject: TERM
- Interpretation: Describes a test checking the truthiness of the subject as a boolean; asserts nothing.
- Example: `TERM test_truthiness(subject=code_entity(kind="class", name="DataFrame", project=platform_label::pandas)) -> test_truthiness_2 : TERM`
- Proposed record: {"symbol":"test_truthiness","kind":"constructor","signature":"TERM test_truthiness(subject: TERM) -> TERM","definition":"A descriptive term for testing the truthiness of the given subject as a boolean; does not assert an actual evaluation result.","not":"A factual claim of test execution or outcome","aliases":["check_truthiness","boolean_test"]}