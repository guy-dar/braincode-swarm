### S1 | type: add | dimension: constructor | symbol: chg_deprecate_code
- Needs: n1 (t1:s1)
- Searches tried: "deprecate method" → modify_code, calculation, reconcile_code; "method deprecation" → modify_code, negation; widen "deprecate method" → calculation, obligation, remove
- Typed parameters: entity: TERM, project?: STRING / ATOM[platform_label]
- Interpretation: Constructs a structured specification to deprecate a code entity (function, method, class, or module) in a software project; describes intent, asserts nothing.
- Example: `TERM chg_deprecate_code(entity=code_entity_2, project=platform_label::pandas) -> chg_deprecate_code_2 : TERM`
- Proposed record: `{"symbol": "chg_deprecate_code", "kind": "constructor", "signature": "TERM chg_deprecate_code(entity: TERM, project?: STRING / ATOM[platform_label]) -> TERM", "definition": "Constructs a structured change specification describing the deprecation of a source code entity within a project.", "not": "warning (a recorded runtime deprecation warning) or chg_modify_code (a general code modification)", "aliases": ["deprecate_code", "deprecate_function", "deprecate_method"]}`

### S2 | type: add | dimension: constructor | symbol: code_usage
- Needs: n3 (t1:s2)
- Searches tried: "usage count" → quantity, group_size, minimum_per_period; widen "method is only used in one place" → duplicate_definition (asserts duplicate definitions/implementations exist, not usage/call sites)
- Typed parameters: count: NUMBER, entity: TERM, location?: STRING / TERM
- Interpretation: Constructs a descriptor for the count of usage or call-site references to a code entity in a codebase; count is a nonnegative integer.
- Example: `TERM code_usage(count=1, entity=code_entity_2) -> code_usage_2 : TERM`
- Proposed record: `{"symbol": "code_usage", "kind": "constructor", "signature": "TERM code_usage(count: NUMBER, entity: TERM, location?: STRING / TERM) -> TERM", "definition": "Constructs a descriptor for the count of usage or call-site references to a code entity in a codebase; count is a nonnegative integer.", "not": "duplicate_definition (multiple duplicate definitions/implementations of an entity) or group_size (headcount of a group)", "aliases": ["usage_count", "call_count", "used_in_places"]}`

### S3 | type: add | dimension: constructor | symbol: code_breakage
- Needs: n4 (t1:s2)
- Searches tried: "breakage" → state_sliced, failure; "regression breakage" → regression_case, failure, leads_to; widen "removing method does not break anything" → reconcile_code, enables
- Typed parameters: description?: STRING, target?: TERM
- Interpretation: Constructs a descriptive representation of software breakage, test regression, or functionality disruption in a codebase; describes potential or observed breakage, asserts nothing.
- Example: `TERM code_breakage(target=code_entity_2) -> code_breakage_2 : TERM`
- Proposed record: `{"symbol": "code_breakage", "kind": "constructor", "signature": "TERM code_breakage(description?: STRING, target?: TERM) -> TERM", "definition": "Constructs a descriptive representation of software breakage, test regression, or functionality disruption in a codebase.", "not": "failure (a system failure claim hypothesis) or state_sliced (physical slicing)", "aliases": ["software_breakage", "breakage", "code_regression"]}`

### S4 | type: add | dimension: constructor | symbol: code_evaluation
- Needs: n7 (t1:s5, t1:s6), n8 (t1:s7, t1:s8)
- Searches tried: "evaluates" → calculation, test_condition, decision; "evaluates to boolean" → test_condition (not: expected outcome is not an observed result), calculation (arithmetic steps); widen "evaluates as True or False" → test_condition, decision
- Typed parameters: expression: STRING, result: STRING / NUMBER / BOOL / TERM
- Interpretation: Constructs a descriptor representing the evaluation of a source code expression and its evaluated return value in an interactive REPL or interpreter.
- Example: `TERM code_evaluation(expression="pd.Index(['a', np.nan, 'b']).is_mixed()", result=TRUE) -> code_evaluation_2 : TERM`
- Proposed record: `{"symbol": "code_evaluation", "kind": "constructor", "signature": "TERM code_evaluation(expression: STRING, result: STRING / NUMBER / BOOL / TERM) -> TERM", "definition": "Constructs a descriptor representing the evaluation of a source code expression and its evaluated return value.", "not": "test_condition (an expected test outcome, not an observed evaluation result) or calculation (an arithmetic/math step)", "aliases": ["code_eval", "evaluates_to", "repl_result"]}`
