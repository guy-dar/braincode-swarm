### S1 | type: add | dimension: constructor | symbol: chg_deprecate
- Needs: n1 (t1:s1)
- Searches tried: search "deprecate" "deprecation" → warning (an alert claim), prohibited (a restriction claim); widen "deprecate Index.is_mixed method" → no deprecation change constructor
- Typed parameters: entity: TERM, message?: STRING, replacement?: TERM
- Interpretation: Constructs a structured change specification describing the deprecation of a code entity or feature; describes intent, asserts nothing.
- Example: `TERM chg_deprecate(entity=code_entity_2) -> chg_deprecate_2 : TERM`
- Proposed record: `{"symbol": "chg_deprecate", "kind": "constructor", "signature": "TERM chg_deprecate(entity: TERM, message?: STRING, replacement?: TERM) -> TERM", "definition": "Constructs a structured change specification describing the deprecation of a code entity or feature.", "not": "an executed runtime deprecation warning (use warning claim)", "aliases": ["deprecate_feature", "deprecation_change"]}`

### S2 | type: add | dimension: constructor | symbol: code_usage
- Needs: n3 (t1:s2)
- Searches tried: search "used in one place" "usage count" "used in codebase" → duplicate_definition (duplicate function definitions, not call sites), user_practice (habitual user workflow); widen "Index.is_mixed is only used in one place in the codebase" → nothing for code entity call/usage count
- Typed parameters: count: NUMBER, entity: TERM, location?: STRING / TERM / ATOM[platform_label]
- Interpretation: Asserts the count of call sites or usages of a code entity within a specified codebase or module.
- Example: `CLAIM code_usage(count=1, entity=code_entity_2, location=platform_label::pandas) BY "user" STATUS asserted SOURCE "t1:s2" -> code_usage_2 : CLAIM`
- Proposed record: `{"symbol": "code_usage", "kind": "claim_relation", "signature": "CLAIM code_usage(count: NUMBER, entity: TERM, location?: STRING / TERM / ATOM[platform_label])", "definition": "Asserts the count of call sites or usages of a code entity within a specified codebase or module.", "not": "duplicate definitions of a function (use duplicate_definition)", "aliases": ["usage_count", "reference_count", "call_count"]}`

### S3 | type: add | dimension: constructor | symbol: breakage
- Needs: n4 (t1:s2), n5 (t1:s2)
- Searches tried: search "code breakage" "failure" "causes" → causes (claim relation cannot be negated by negation), failure (claim relation); widen "removing Index.is_mixed does not break anything" → no constructor for software breakage or regression
- Typed parameters: description?: STRING, target?: TERM
- Interpretation: Constructs a structured descriptor representing software breakage, failure, or regression; describes a defect, asserts nothing.
- Example: `TERM breakage(target=code_entity_2) -> breakage_2 : TERM`
- Proposed record: `{"symbol": "breakage", "kind": "constructor", "signature": "TERM breakage(description?: STRING, target?: TERM) -> TERM", "definition": "Constructs a structured descriptor representing software breakage, failure, or regression.", "not": "an observed runtime system failure claim (use failure claim)", "aliases": ["code_breakage", "software_breakage", "regression_defect"]}`

### S4 | type: add | dimension: constructor | symbol: inconsistent_behavior
- Needs: n6 (t1:s3)
- Searches tried: search "surprising" "inconsistent" "behavior" → unaware, failure, distracts_from; widen "Index.is_mixed exhibits surprising or inconsistent behavior" → no claim relation or descriptor for inconsistent code behavior
- Typed parameters: description?: STRING, entity: TERM
- Interpretation: Asserts that a code entity or system exhibits inconsistent, unexpected, or surprising behavior.
- Example: `CLAIM inconsistent_behavior(description="surprising", entity=code_entity_2) BY "user" STATUS asserted SOURCE "t1:s3" -> inconsistent_behavior_2 : CLAIM`
- Proposed record: `{"symbol": "inconsistent_behavior", "kind": "claim_relation", "signature": "CLAIM inconsistent_behavior(description?: STRING, entity: TERM)", "definition": "Asserts that a code entity or system exhibits inconsistent, unexpected, or surprising behavior.", "not": "a total system crash or failure (use failure)", "aliases": ["surprising_behavior", "unexpected_behavior"]}`

### S5 | type: add | dimension: constructor | symbol: code_eval
- Needs: n7 (t1:s5, t1:s6), n8 (t1:s7, t1:s8)
- Searches tried: search "evaluates to" "repl output" "code execution outcome" → test_condition (expected test outcome, not observed REPL evaluation), outcome (requires EVENT from RECORD ACTION); widen → no constructor for interactive code snippet evaluation result
- Typed parameters: expression: STRING, result: STRING / NUMBER / BOOL
- Interpretation: Constructs a descriptor representing an evaluated code expression and its resulting output value; describes REPL evaluation, asserts nothing.
- Example: `TERM code_eval(expression="pd.Index(['a', np.nan, 'b']).is_mixed()", result=TRUE) -> code_eval_2 : TERM`
- Proposed record: `{"symbol": "code_eval", "kind": "constructor", "signature": "TERM code_eval(expression: STRING, result: STRING / NUMBER / BOOL) -> TERM", "definition": "Constructs a descriptor representing an evaluated code expression and its resulting value.", "not": "an assertion test condition with expected outcome (use test_condition)", "aliases": ["eval_snippet", "repl_evaluation", "evaluates_to"]}`
