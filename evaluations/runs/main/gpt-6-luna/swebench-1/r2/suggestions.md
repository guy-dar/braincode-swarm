### S1 | type: add | dimension: constructor | symbol: code_call
- Needs: n4 (t1:s3), n13 (t1:s30)
- Searches tried: widen "reproduce bug by passing inputs_embeds and attention_mask to ConvBertForTokenClassification" → `cli_command` describes command-line invocation, `activity` is a broad action description, and neither records named method arguments; search "program variable assigned or unassigned on conditional path and code uses variable in slice" → no code-call constructor.
- Typed parameters: callee: TERM, arguments: LIST[TERM]
- Interpretation: Describes a call to a named code entity with the listed argument descriptors in order; does not execute the call or claim an outcome.
- Example: `TERM code_call(callee=forward_method, arguments=[inputs_embeds_argument, attention_mask_argument]) -> code_call_2 : TERM`
- Contrast: Not `cli_command` (a command-line invocation), and not a runtime call or EVENT.
- Proposed record: {"symbol": "code_call", "kind": "constructor", "signature": "TERM code_call(callee: TERM, arguments: LIST[TERM]) -> TERM", "definition": "Describes a code-method invocation with an identified callee and ordered argument descriptors. It does not execute the call or assert an outcome.", "not": "an executed runtime call or command-line invocation", "aliases": []}

### S2 | type: add | dimension: vocabulary-member | symbol: variable_status_on_path
- Needs: n7 (t1:s10), n8 (t1:s13–s19)
- Searches tried: widen "seq_length remains unassigned on execution path" → `unaware` concerns awareness and `raises_exception` concerns a raised exception; search "program variable assigned or unassigned on conditional path" → `conditional` is only a descriptive constructor and no relation records variable binding state.
- Meaning: The named variable has the specified assignment state along a described code path. In this item, state `unassigned` means no assignment has occurred on that path; it does not assert why or what later consequence follows.
- Category: claim_relation
- Contextual aliases: none
- Example: `CLAIM variable_status_on_path(path=branch_term, state="unassigned", variable="seq_length") ...`
- Contrast: Not a claim that the variable is universally undefined or that an exception was observed.
- Proposed record: {"symbol": "variable_status_on_path", "kind": "claim_relation", "signature": "CLAIM variable_status_on_path(path: TERM, state: STRING, variable: STRING)", "definition": "Asserts the named variable's assignment state on the described code path. State unassigned means it has not been assigned along that path; the claim is limited to that path.", "not": "a universal claim that the variable is undefined, or a claim that an exception occurred", "aliases": []}

### S3 | type: add | dimension: vocabulary-member | symbol: uses_variable_in_operation
- Needs: n6 (t1:s6–s8)
- Searches tried: widen "token_type_ids slicing uses seq_length variable when token_type_ids is None" → `slice` is an external slicing operation and `state_sliced` is a state; search "program variable assigned or unassigned on conditional path and code uses variable in slice" → no claim relation connects a code operation, variable, and guard.
- Meaning: The identified code operation reads/uses the named variable under an optional stated condition. This records source-code structure, not runtime execution.
- Category: claim_relation
- Contextual aliases: none
- Example: `CLAIM uses_variable_in_operation(condition=guard_term, operation=slice_expression, variable="seq_length") ...`
- Contrast: Not the external operation `slice`, and not a claim that the code path actually ran.
- Proposed record: {"symbol": "uses_variable_in_operation", "kind": "claim_relation", "signature": "CLAIM uses_variable_in_operation(operation: TERM, variable: STRING, condition?: TERM)", "definition": "Asserts that the identified code operation uses the named variable, optionally under the stated code condition. It describes source structure and does not assert runtime execution.", "not": "an external slice operation or evidence that the code path executed", "aliases": []}

### S4 | type: add | dimension: vocabulary-member | symbol: checked_option
- Needs: n11 (t1:s24–s25), n12 (t1:s27–s28)
- Searches tried: widen "running custom modified script rather than official example scripts" → `example_of` expresses exemplification, not a checked state; widen "running custom task or dataset rather than standard benchmark" → `user_preference` expresses preference, not the explicit selected/unselected form status; search "reported checkbox selection custom script official example selected task dataset official benchmark" → no matching claim relation.
- Meaning: Records that a named option in a supplied form/checklist was explicitly selected or not selected; this does not by itself claim that the selected activity was performed.
- Category: claim_relation
- Contextual aliases: none
- Example: `CLAIM checked_option(option="own modified scripts", selected=TRUE) ...`
- Contrast: Not a user preference in general and not evidence that a script or task was run.
- Proposed record: {"symbol": "checked_option", "kind": "claim_relation", "signature": "CLAIM checked_option(option: STRING, selected: BOOL)", "definition": "Asserts the explicitly represented selected or unselected state of a named option in a supplied form or checklist. Selection alone does not establish that the option's activity occurred.", "not": "a general preference or an assertion that the selected activity was performed", "aliases": []}

### S5 | type: add | dimension: vocabulary-member | symbol: maintainer_of
- Needs: n10 (t1:s22)
- Searches tried: widen "text models maintainers ArthurZucker and younesbelkada" → recipient roles do not preserve either named person or their relation; widen "maintainer of software library project" → `software_version`, `pull_request`, and `code_entity` describe software artifacts, with no maintainer relation.
- Meaning: The named person is identified as a maintainer of the named software project; the attribution remains that of the supplied source.
- Category: claim_relation
- Contextual aliases: none
- Example: `CLAIM maintainer_of(person="@ArthurZucker", project=platform_label::transformers) ...`
- Contrast: Not merely a recipient role or an assertion that the person authored a particular change.
- Proposed record: {"symbol": "maintainer_of", "kind": "claim_relation", "signature": "CLAIM maintainer_of(person: STRING, project: ATOM[platform_label])", "definition": "Asserts that the named person is a maintainer of the identified software project, according to the attributed source.", "not": "a generic recipient role or authorship of a particular change", "aliases": []}

### S6 | type: add | dimension: vocabulary-member | symbol: greet
- Needs: n2 (t1:s3)
- Searches tried: widen "greet and report an issue with ConvBertForTokenClassification" → `greeting` is a TERM constructor and cannot head UTTER; `inform` requires a CLAIM and is not a salutation.
- Meaning: Records a speech act greeting the specified recipient; it does not imply agreement, a substantive report, or any other speech act.
- Category: speech_act
- Contextual aliases: none
- Example: `UTTER greet(recipient=role_agent)`
- Contrast: Not the descriptive TERM `greeting` alone and not `inform`.
- Proposed record: {"symbol": "greet", "kind": "speech_act", "signature": "UTTER greet(recipient: STRING)", "definition": "A speech act greeting the specified recipient. It carries no substantive report or implication of agreement.", "not": "a descriptive greeting TERM without an utterance, or an informative assertion", "aliases": []}

### S7 | type: add | dimension: vocabulary-member | symbol: expect
- Needs: n14 (t1:s32), n15 (t1:s32)
- Searches tried: widen "expected execution without raising UnboundLocalError" → `test_condition` describes an expected Boolean test outcome but is a TERM, not a speech act; widen "no error should occur during model execution" → `raises_exception` represents exception occurrence, while `negation` is a TERM constructor and does not express the user's speech act.
- Meaning: Records a speaker's stated expected behavior as a TERM target; it is not an observation that the behavior occurred.
- Category: speech_act
- Contextual aliases: none
- Example: `UTTER expect(target=expected_behavior_term)`
- Contrast: Not an observed CLAIM, a runtime test, or an assertion that the expectation was met.
- Proposed record: {"symbol": "expect", "kind": "speech_act", "signature": "UTTER expect(target: TERM)", "definition": "A speech act stating expected behavior described by a TERM target. It does not claim that the behavior occurred or was verified.", "not": "an observed outcome or a claim that the expectation was satisfied", "aliases": []}

### S8 | type: add | dimension: vocabulary-member | symbol: code_statement_on_path
- Needs: n8 (t1:s13–s19)
- Searches tried: widen "inputs_embeds branch extracts input_shape but omits unpacking seq_length" → `code_entity` can describe a source entity but does not assert branch membership; search "source code statement occurs in conditional branch path" → no matching claim relation. `conditional` only composes descriptive terms and does not make a source-code occurrence claim.
- Meaning: Asserts that the identified code statement occurs on the described code path; it does not assert execution at runtime.
- Category: claim_relation
- Contextual aliases: none
- Example: `CLAIM code_statement_on_path(path=inputs_embeds_branch, statement=input_shape_assignment) ...`
- Contrast: Not a runtime execution record or a claim that the branch was taken.
- Proposed record: {"symbol": "code_statement_on_path", "kind": "claim_relation", "signature": "CLAIM code_statement_on_path(path: TERM, statement: TERM)", "definition": "Asserts that an identified source-code statement belongs to the described code path. This is a source-structure claim and does not assert that the path executed.", "not": "an EVENT or a claim that the branch was taken at runtime", "aliases": []}
