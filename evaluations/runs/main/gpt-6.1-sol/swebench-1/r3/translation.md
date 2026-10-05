Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM code_entity(kind="class", name="ConvBertForTokenClassification", project=platform_label::transformers) -> code_entity_2 : TERM
    TERM code_entity(kind="module", name="models.convbert", project=platform_label::transformers) -> code_entity_3 : TERM
    CLAIM attribute_claim(subject=code_entity_2, property="module", value=code_entity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_2 : CLAIM
    TERM code_entity(kind="method", name="ConvBertForTokenClassification.forward", project=platform_label::transformers) -> code_entity_4 : TERM
    TERM code_invocation(argument_names=["input_embeds"], callee=code_entity_4, exhaustive=TRUE) -> code_invocation_2 : TERM # PROPOSED: S1
    CLAIM raises_exception(target=code_invocation_2, exception_type="UnboundLocalError", message="local variable 'seq_length' referenced before assignment") BY role_user STATUS reported SOURCE "t1:s1" -> raises_exception_2 : CLAIM
    TERM greeting(recipient=role_agent) -> greeting_2 : TERM
    UTTER greet(target=greeting_2) # PROPOSED: S5
    UTTER inform(target=raises_exception_2)
    TERM code_entity(file="modeling_convbert.py", kind="file", name="modeling_convbert.py", project=platform_label::transformers) -> code_entity_5 : TERM
    CLAIM attribute_claim(subject=code_entity_5, property="traceback_line", value=833) BY role_user STATUS reported SOURCE "t1:s4" -> attribute_claim_3 : CLAIM
    TERM code_entity(file=code_entity_5, kind="variable", name="token_type_ids") -> code_entity_6 : TERM
    TERM code_entity(file=code_entity_5, kind="variable", name="seq_length") -> code_entity_7 : TERM
    TERM code_entity(file=code_entity_5, kind="attribute", name="self.embeddings") -> code_entity_8 : TERM
    TERM code_entity(file=code_entity_5, kind="attribute", name="self.embeddings.token_type_ids") -> code_entity_9 : TERM
    TERM code_entity(file=code_entity_5, kind="variable", name="buffered_token_type_ids") -> code_entity_10 : TERM
    TERM code_condition(operator="is_none", operands=[code_entity_6]) -> code_condition_2 : TERM # PROPOSED: S2
    TERM code_condition(operator="has_attribute", operands=[code_entity_8], attribute="token_type_ids") -> code_condition_3 : TERM # PROPOSED: S2
    TERM code_slice(dimension=1, stop=code_entity_7, subject=code_entity_9) -> code_slice_2 : TERM # PROPOSED: S2
    TERM code_assignment(targets=[code_entity_10], value=code_slice_2) -> code_assignment_2 : TERM # PROPOSED: S2
    TERM code_branch(condition=code_condition_3, kind="if", statements=[code_assignment_2]) -> code_branch_2 : TERM # PROPOSED: S2
    TERM code_branch(condition=code_condition_2, kind="if", statements=[code_branch_2]) -> code_branch_3 : TERM # PROPOSED: S2
    CLAIM attribute_claim(subject=code_branch_3, property="present_in_source", value=TRUE) BY role_user STATUS reported SOURCE "t1:s8" -> attribute_claim_4 : CLAIM
    CLAIM code_binding_state(assigned=FALSE, context=code_branch_3, variable=code_entity_7) BY role_user STATUS asserted SOURCE "t1:s10" -> code_binding_state_2 : CLAIM # PROPOSED: S2
    TERM code_entity(file=code_entity_5, kind="variable", name="input_ids") -> code_entity_11 : TERM
    TERM code_entity(file=code_entity_5, kind="variable", name="inputs_embeds") -> code_entity_12 : TERM
    TERM code_entity(file=code_entity_5, kind="variable", name="input_shape") -> code_entity_13 : TERM
    TERM code_entity(file=code_entity_5, kind="variable", name="batch_size") -> code_entity_14 : TERM
    TERM code_entity(file=code_entity_5, kind="method", name="input_ids.size") -> code_entity_15 : TERM
    TERM code_entity(file=code_entity_5, kind="method", name="inputs_embeds.size") -> code_entity_16 : TERM
    TERM code_invocation(argument_names=[], callee=code_entity_15, exhaustive=TRUE) -> code_invocation_3 : TERM # PROPOSED: S1
    TERM code_invocation(argument_names=[], callee=code_entity_16, exhaustive=TRUE) -> code_invocation_4 : TERM # PROPOSED: S1
    TERM code_assignment(targets=[code_entity_13], value=code_invocation_3) -> code_assignment_3 : TERM # PROPOSED: S2
    TERM code_assignment(targets=[code_entity_14, code_entity_7], value=code_entity_13) -> code_assignment_4 : TERM # PROPOSED: S2
    TERM code_slice(dimension=0, stop=-1, subject=code_invocation_4) -> code_slice_3 : TERM # PROPOSED: S2
    TERM code_assignment(targets=[code_entity_13], value=code_slice_3) -> code_assignment_5 : TERM # PROPOSED: S2
    TERM code_condition(operator="is_not_none", operands=[code_entity_11]) -> code_condition_4 : TERM # PROPOSED: S2
    TERM code_condition(operator="is_not_none", operands=[code_entity_12]) -> code_condition_5 : TERM # PROPOSED: S2
    TERM code_branch(condition=code_condition_4, kind="elif", statements=[code_assignment_3, code_assignment_4]) -> code_branch_4 : TERM # PROPOSED: S2
    TERM code_branch(condition=code_condition_5, kind="elif", statements=[code_assignment_5]) -> code_branch_5 : TERM # PROPOSED: S2
    TERM sequence(items=[code_branch_4, code_branch_5]) -> sequence_2 : TERM
    CLAIM attribute_claim(subject=sequence_2, property="present_in_source", value=TRUE) BY role_user STATUS reported SOURCE "t1:s17" -> attribute_claim_5 : CLAIM
    CLAIM code_binding_state(assigned=FALSE, context=code_branch_5, variable=code_entity_7) BY role_user STATUS asserted SOURCE "t1:s19" -> code_binding_state_3 : CLAIM # PROPOSED: S2
    TERM code_presence(context=code_branch_5, present=FALSE, statement=code_assignment_4) -> code_presence_2 : TERM # PROPOSED: S2
    TERM incorrect_use(target=code_entity_2) -> incorrect_use_2 : TERM # PROPOSED: S3
    TERM alternative_question(alternatives=[code_presence_2, incorrect_use_2], subject=code_entity_2) -> alternative_question_2 : TERM # PROPOSED: S3
    UTTER ask(target=alternative_question_2)
    TERM property_question(property="assistance", subject=code_entity_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2, recipient="ArthurZucker")
    UTTER ask(target=property_question_2, recipient="younesbelkada")
    TERM subject(kind="script") -> subject_2 : TERM
    CLAIM attribute_claim(subject=subject_2, property="used", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s25" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(subject=subject_2, property="user_modified", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s25" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(subject=subject_2, property="official_example", value=FALSE) BY role_user STATUS asserted SOURCE "t1:s24" -> attribute_claim_8 : CLAIM
    TERM subject(kind="task_or_dataset") -> subject_3 : TERM
    CLAIM attribute_claim(subject=subject_3, property="used", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s28" -> attribute_claim_9 : CLAIM
    CLAIM attribute_claim(subject=subject_3, property="user_custom", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s28" -> attribute_claim_10 : CLAIM
    CLAIM attribute_claim(subject=subject_3, property="officially_supported_examples_task", value=FALSE) BY role_user STATUS asserted SOURCE "t1:s27" -> attribute_claim_11 : CLAIM
    TERM code_invocation(argument_names=["inputs_embeds", "attention_mask"], callee=code_entity_2, exhaustive=TRUE) -> code_invocation_5 : TERM # PROPOSED: S1
    CLAIM attribute_claim(subject=code_invocation_5, property="reproduction_procedure", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s30" -> attribute_claim_12 : CLAIM
    TERM code_exception(target=code_invocation_5) -> code_exception_2 : TERM # PROPOSED: S2
    TERM negation(target=code_exception_2) -> negation_2 : TERM
    TERM requirement(property="execution_outcome", value=negation_2) -> requirement_2 : TERM
    CLAIM request(target=requirement_2) BY role_user STATUS asserted SOURCE "t1:s32" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM chg_modify_code(target=platform_label::transformers, file="src/transformers/models/convbert/modeling_convbert.py") -> chg_modify_code_2 : TERM # REFINED: S4
    UTTER propose(target=chg_modify_code_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | raises_exception | covered |
| n2 | speech_act | greeting, greet (S5), inform | proposed |
| n3 | object | code_entity, attribute_claim | covered |
| n4 | action | code_invocation (S1) | proposed |
| n5 | object | code_entity, attribute_claim | covered |
| n6 | claim | code_condition, code_slice, code_assignment, code_branch (S2), attribute_claim | proposed |
| n7 | claim | code_binding_state (S2) | proposed |
| n8 | claim | code_invocation (S1), code_assignment, code_slice, code_branch, code_binding_state (S2), attribute_claim | proposed |
| n9 | speech_act | code_presence (S2), incorrect_use, alternative_question (S3), ask | proposed |
| n10 | object | property_question, ask, recipient | covered |
| n11 | claim | subject, attribute_claim | covered |
| n12 | claim | subject, attribute_claim | covered |
| n13 | action | code_invocation (S1), attribute_claim | proposed |
| n14 | constraint | code_exception (S2), negation, requirement, request | proposed |
| n15 | negation | code_exception (S2), negation | proposed |
| n16 | action | chg_modify_code (S4), propose | proposed |
| n17 | object | platform_label::transformers | label-preserved |

## Why the translation failed

- n2 (S5): search "greet salutation speech act"; widen "greeting speech act expressing salutation". greeting describes a salutation but does not enact its speech act. respond means answering, acknowledge means receipt/awareness, and neither faithfully represents the initial greeting. Add a speech act consuming the existing greeting descriptor rather than refining answer semantics.
- n4, n13 (S1): search "function call named arguments code execution" and "function invocation arguments"; widen each original need. Closest: code_entity identifies methods, cli_command describes shell commands, calculation describes calculations rather than general method calls with named arguments. None expresses the source's supplied argument names and exclusion of other arguments.
- n6, n7, n8 (S2): search "unassigned local variable branch assignment unpack shape", "runtime variable binding absent assigned", "tensor indexing conditional code", "code assignment missing unpacking", "code condition slice assignment local binding"; widen each original need. code_entity identifies variables but does not express dataflow. state_sliced and slice describe slicing material, not tensor indexing. conditional connects proposition terms but supplies neither None tests nor code branches or binding state. attribute_claim can assert a property but cannot by itself supply these typed structures. The existing code_entity and sequence are reused instead of proposed replacements.
- n9 (S2, S3): search "question alternative bug or misuse", "alternative question uncertainty", "diagnostic question alternative explanations"; widen the original need and "whether omitted assignment is bug versus incorrect model usage". ask supplies the speech act, property_question a single property question, issue an issue-ticket reference requiring a number. None exposes the two tentative explanations or incorrect-use meaning. No answer or established diagnosis is encoded.
- n14, n15 (S2): search "absence expected exception"; widen both original needs. raises_exception is a CLAIM relation and cannot be used as a TERM under negation. test_condition takes an opaque condition string, losing the separately represented execution target and error condition. exclude is an artifact-content constraint, not the desired absence of a runtime error. Reuse negation and requirement once code_exception supplies the descriptive predicate.
- n16 (S4): search "unspecified proposed source file modification" and "proposed code change unspecified revision"; widen the original need with "without specifying a revision". chg_modify_code requires revision: TERM, but the agent supplies only a filename. modify_code has the same requirement and would incorrectly claim execution if recorded. Do not fabricate a patch, successful modification, or unpacking fix.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation.
- Coverage status: partial against the current release; suggested document requires S1–S5.
- Source-span coverage: substantive content of t1:s1, s3–s4, s6–s8, s10, s13–s17, s19–s20, s22, s24–s25, s27–s28, s30, s32 and t2:s2 is represented, some only through proposals. Headings, code fences, connective location wording, and t2:s1's list numeral add no separate claim. The code is represented structurally rather than executed; s8 and s17 anchor their respective supplied multi-line snippets.
- Opaque-text spans: none in the suggested document. Several meanings remain unavailable in the current glossary; they are proposed, not disguised as free-text fallbacks.
- Label-preserved spans: t1:s3 and t2:s2 — transformers → platform_label::transformers; the library identity is preserved only as a source-supported software label. Exact class, module, variable and method identifiers are separately preserved with code_entity.
- Missing constructs: S1 descriptive invocation; S2 source-code conditions, slicing, assignments, branch descriptions, assignment presence, contextual binding state and descriptive exception predicate; S3 alternative diagnostic question and incorrect-use description; S4 optional revision in descriptive code-change requests; S5 greeting speech act.
- Unresolved ambiguities: t1:s3 says input_embeds, while s16–s17 and s30 say inputs_embeds; these spellings are retained, not silently equated. s3 says only one argument, s30 names two; distinct invocation descriptions preserve that discrepancy. t1:s28 does not distinguish task from dataset. The agent's revision details and execution outcome are absent. No version, initial if branch, tensor values, or observed successful fix is invented.
- Proposed glossary/spec changes: S1–S5 in /output/suggestions.md; no grammar changes.
- Check: final `node /kit/rag.mjs check --translation /output/translation.md` reported no unresolved coverage rows, three declared rows (n7, n12, n13), eleven unknown symbols (alternative_question, code_assignment, code_binding_state, code_branch, code_condition, code_exception, code_invocation, code_presence, code_slice, greet, incorrect_use; all proposed), and an n3 label warning. Its lexical n3 warning does not account for the explicit class code_entity and module relation; these preserve more than a label, so n3 is marked covered. Check does not validate proposed signatures, S4's optional argument, or semantic fidelity.
