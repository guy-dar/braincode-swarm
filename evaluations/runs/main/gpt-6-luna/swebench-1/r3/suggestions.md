### S1 | type: add | dimension: constructor | symbol: code_branch
- Needs: n6 (t1:s6–t1:s8), n7 (t1:s10), n8 (t1:s13–t1:s19)
- Searches tried: widen "code branch unpacks batch_size and seq_length from input_shape" → `code_entity`, `calculation`, `software_version`; search "code variable is not assigned on a conditional execution path" → `conditional`, `code_entity`, `test_condition`. None represents source-code branch statements together with identifiers left unassigned on that path; `state_sliced` denotes a state, not the slicing statement.
- Typed parameters: condition: STRING, statements: LIST[STRING], unassigned: LIST[STRING]
- Interpretation: A descriptive representation of a source-code branch: its condition, exact source statement snippets in order, and identifiers reported unassigned on that path. It describes code and does not execute it or assert runtime behavior beyond the represented source description.
- Example: `TERM code_branch(condition="inputs_embeds is not None", statements=["input_shape = inputs_embeds.size()[:-1]"], unassigned=["batch_size", "seq_length"]) -> code_branch_2 : TERM`
- Contrast: Not a runtime IF and not an assertion that a branch was executed.
- Proposed record: {"symbol":"code_branch","kind":"constructor","signature":"TERM code_branch(condition: STRING, statements: LIST[STRING], unassigned: LIST[STRING]) -> TERM","definition":"Describes a source-code branch by its condition, ordered exact statement snippets, and identifiers specified as unassigned on that path. It describes code and does not execute the branch.","not":"A runtime IF or an assertion that the branch was executed","aliases":[]}

### S2 | type: add | dimension: constructor | symbol: code_invocation
- Needs: n4 (t1:s3), n13 (t1:s30)
- Searches tried: widen "invoke a software model forward method with input_embeds and attention_mask arguments" → `activity`, `code_entity`, `regression_case`; search "method invocation with named arguments" → no candidate with a fitting callable-method and argument signature. The operation candidates are external operations and do not describe the supplied model method call.
- Typed parameters: target: TERM, method: STRING, arguments: LIST[STRING]
- Interpretation: A descriptive representation of invoking a named method on a described code entity with the listed argument names. It does not claim the invocation was actually performed or supply unmentioned argument values.
- Example: `TERM code_invocation(target=model_term, arguments=["inputs_embeds", "attention_mask"], method="forward") -> code_invocation_2 : TERM`
- Contrast: Not an executed external ACTION or a claim of successful execution.
- Proposed record: {"symbol":"code_invocation","kind":"constructor","signature":"TERM code_invocation(target: TERM, method: STRING, arguments: LIST[STRING]) -> TERM","definition":"Describes invocation of a named method on a code entity with the listed argument names. It does not assert that the invocation occurred or provide unmentioned argument values.","not":"An executed external operation or a claim of successful execution","aliases":[]}

### S3 | type: add | dimension: constructor | symbol: diagnostic_question
- Needs: n9 (t1:s20)
- Searches tried: widen "ask whether missing batch_size and seq_length unpacking is a bug or misuse" → `ask`, `test_condition`, `regression_case`; search "question comparing candidate explanations for a code error" → `subject`, `decision`, `conditional`. The candidates describe questions generally, tests, or decisions, but none constructs a question with explicit competing diagnostic explanations.
- Typed parameters: subject: TERM, alternatives: LIST[TERM]
- Interpretation: A question asking which of the listed candidate explanations applies to the described subject; it does not select or endorse an answer.
- Example: `TERM diagnostic_question(subject=code_branch_term, alternatives=[bug_term, misuse_term]) -> diagnostic_question_2 : TERM`
- Contrast: Not a conclusion that any candidate explanation is true.
- Proposed record: {"symbol":"diagnostic_question","kind":"constructor","signature":"TERM diagnostic_question(subject: TERM, alternatives: LIST[TERM]) -> TERM","definition":"Describes a question about which of the listed candidate explanations applies to the subject. It does not select or endorse an answer.","not":"A claim that one of the candidate explanations is true","aliases":[]}

### S4 | type: add | dimension: vocabulary-member | symbol: selected_context
- Needs: n11 (t1:s24–t1:s25), n12 (t1:s27–t1:s28)
- Searches tried: widen "running custom modified script rather than official example" → `modify_code`, `example_of`, `user_practice`; widen "running custom task or dataset rather than standard benchmark" → `run_tests`, `performance_tracking`, `user_practice`. These describe code changes, exemplification, habitual practice, or test execution, not a source-supplied selected/not-selected context checkbox.
- Meaning: Reports the source's explicit selection state for a described context, such as a checked or unchecked option.
- Category: claim_relation
- Typed signature: `CLAIM selected_context(context: TERM, selection: STRING)`
- Contextual aliases: none
- Example: `CLAIM selected_context(context=script_context, selection="selected") BY role_user STATUS reported SOURCE "t1:s25" -> selected_context_2 : CLAIM`
- Contrast: Not a claim that the selected scripts or task were actually run, or that a test passed.
- Proposed record: {"symbol":"selected_context","kind":"claim_relation","category":"claim_relation","signature":"CLAIM selected_context(context: TERM, selection: STRING)","definition":"Reports an explicit source selection state for a described context; selection identifies the supplied selected or unselected state. It does not assert that the context was executed.","not":"A claim that the selected context was run or that its tests passed","aliases":[]}

### S5 | type: add | dimension: vocabulary-member | symbol: potential_helper
- Needs: n10 (t1:s21–t1:s22)
- Searches tried: widen "maintainers explicitly named as people who can help with issue" → `request`, `role_user`, `requirement`; search "named person identified as someone who can help" → no candidate with the meaning of a potential helper. `subject` preserves a name but does not express the assistance relation.
- Meaning: Reports a person identified by the source as someone able to help with the described matter; this is a source's suggestion, not proof of competence or availability.
- Category: claim_relation
- Typed signature: `CLAIM potential_helper(person: TERM)`
- Contextual aliases: none
- Example: `CLAIM potential_helper(person=maintainer_term) BY role_user STATUS reported SOURCE "t1:s22" -> potential_helper_2 : CLAIM`
- Contrast: Not a claim that the named person has accepted a task or provided assistance.
- Proposed record: {"symbol":"potential_helper","kind":"claim_relation","category":"claim_relation","signature":"CLAIM potential_helper(person: TERM)","definition":"Reports a person identified by the source as a potential helper for the matter in context. It does not establish competence, availability, or that assistance occurred.","not":"A claim that the named person accepted a task or provided assistance","aliases":[]}

### S6 | type: refine | dimension: refine-entry | target: v19/support/greeting
- Needs: n2 (t1:s3)
- Searches tried: entry `greeting` → its signature requires a recipient; the source says only "Hi" and does not specify an addressee. Search "greeting without a named recipient" → no separate fitting constructor.
- Before: `TERM greeting(recipient: STRING) -> TERM`
- After: `TERM greeting(recipient?: STRING) -> TERM`; omission means the greeting has no specified recipient.
- Justification: The source contains a greeting but does not identify its recipient. Requiring a value forces an unsupported addressee.
- Affected uses: Existing explicit-recipient uses remain valid; existing callers that assume recipient is mandatory must be reviewed.
- Compatibility: Backward-compatible for explicit recipients; enables recipient omission without assigning one by default.
- Proposed record: {"signature":"TERM greeting(recipient?: STRING) -> TERM","definition":"Constructs a conversational salutation descriptor; an omitted recipient is unspecified.","not":"An assertion that a particular recipient was addressed"}
