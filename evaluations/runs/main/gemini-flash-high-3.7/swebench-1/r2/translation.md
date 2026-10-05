Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM code_entity(file="models.convbert", kind="class", name="ConvBertForTokenClassification", project=platform_label::transformers) -> code_entity_2 : TERM
    CLAIM raises_exception(target=code_entity_2, exception_type="UnboundLocalError", message="local variable 'seq_length' referenced before assignment") BY role_user STATUS reported SOURCE "t1:s1" -> raises_exception_2 : CLAIM
    TERM greeting(recipient="maintainers") -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
    UTTER inform(target=raises_exception_2)
    TERM code_entity(kind="method", name="forward") -> code_entity_3 : TERM
    TERM activity(actor="role_user", object=code_entity_3, verb="call") -> activity_2 : TERM
    TERM code_entity(file="modeling_convbert.py", kind="line", name="833", project=platform_label::transformers) -> code_entity_4 : TERM
    TERM requirement(property="is_none", value="token_type_ids") -> requirement_2 : TERM
    TERM requirement(property="uses_variable", value="seq_length") -> requirement_3 : TERM
    TERM conditional(condition=requirement_2, consequence=requirement_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS observed SOURCE "t1:s8" -> statement_2 : CLAIM
    CLAIM attribute_claim(property="assignment_status", subject="seq_length", value="unassigned") BY role_user STATUS observed SOURCE "t1:s10" -> attribute_claim_2 : CLAIM
    TERM requirement(property="branch", value="inputs_embeds") -> requirement_4 : TERM
    TERM requirement(property="unassigned", value="seq_length") -> requirement_5 : TERM
    TERM conditional(condition=requirement_4, consequence=requirement_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS inferred SOURCE "t1:s19" -> statement_3 : CLAIM
    CLAIM leads_to(cause=requirement_4, effect=requirement_5) BY role_user STATUS inferred SOURCE "t1:s19" -> leads_to_2 : CLAIM
    TERM requirement(property="issue_type", value="bug_or_misuse") -> requirement_6 : TERM
    UTTER ask(target=requirement_6)
    CLAIM request(target="ArthurZucker_and_younesbelkada") BY role_user STATUS asserted SOURCE "t1:s22" -> request_2 : CLAIM
    TERM activity(actor="role_user", object="modified_script", verb="run") -> activity_3 : TERM
    CLAIM user_practice(activity=activity_3) BY role_user STATUS asserted SOURCE "t1:s25" -> user_practice_2 : CLAIM
    TERM activity(actor="role_user", object="custom_dataset", verb="run") -> activity_4 : TERM
    CLAIM user_practice(activity=activity_4) BY role_user STATUS asserted SOURCE "t1:s28" -> user_practice_3 : CLAIM
    TERM code_entity(kind="parameter", name="inputs_embeds") -> code_entity_5 : TERM
    TERM code_entity(kind="parameter", name="attention_mask") -> code_entity_6 : TERM
    TERM calculation(inputs=[code_entity_5, code_entity_6], operation="forward") -> calculation_2 : TERM
    TERM activity(actor="role_user", instrument=platform_label::transformers, object=calculation_2, verb="reproduce") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS reported SOURCE "t1:s30" -> statement_4 : CLAIM
    TERM test_condition(condition="execution_without_error", expected=TRUE) -> test_condition_2 : TERM
    CLAIM statement(fact=test_condition_2) BY role_user STATUS asserted SOURCE "t1:s32" -> statement_5 : CLAIM
    TERM requirement(property="error", value=TRUE) -> requirement_7 : TERM
    TERM negation(target=requirement_7) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s32" -> statement_6 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM requirement(property="fix", value=TRUE) -> requirement_8 : TERM
    TERM chg_modify_code(target=platform_label::transformers, file="src/transformers/models/convbert/modeling_convbert.py", revision=requirement_8) -> chg_modify_code_2 : TERM
    UTTER propose(target=chg_modify_code_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | raises_exception | covered |
| n2 | speech_act | greeting, acknowledge, inform | covered |
| n3 | object | platform_label::transformers | label-preserved |
| n4 | action | code_entity, activity | covered |
| n5 | object | code_entity | covered |
| n6 | claim | requirement, conditional, statement | covered |
| n7 | claim | leads_to, attribute_claim | covered |
| n8 | claim | requirement, conditional, statement | covered |
| n9 | speech_act | requirement, ask | covered |
| n10 | object | request | covered |
| n11 | claim | activity, user_practice | covered |
| n12 | claim | activity, user_practice | covered |
| n13 | action | calculation, activity, statement | covered |
| n14 | constraint | test_condition, statement | covered |
| n15 | negation | requirement, negation, statement | covered |
| n16 | action | requirement, chg_modify_code, propose | covered |
| n17 | object | platform_label::transformers | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s2 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "transformers" -> platform_label::transformers; t2:s2 "transformers" -> platform_label::transformers (software library platform label only; no internal semantics resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
