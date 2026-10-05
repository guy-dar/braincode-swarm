Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM raises_exception(exception_type="UnboundLocalError", message="local variable 'seq_length' referenced before assignment") BY role_user STATUS observed SOURCE "t1:s1" -> raises_exception_2 : CLAIM
    TERM greeting(recipient="maintainers") -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
    TERM code_entity(file="models.convbert", kind="class", name="ConvBertForTokenClassification", project=platform_label::transformers) -> code_entity_2 : TERM
    TERM code_entity(kind="method", name="forward", project=platform_label::transformers) -> code_entity_3 : TERM
    TERM activity(instrument=platform_label::transformers, object=code_entity_3, verb="call") -> activity_2 : TERM
    TERM code_entity(file="modeling_convbert.py", kind="line", name="833", project=platform_label::transformers) -> code_entity_4 : TERM
    CLAIM validates_parameter(condition="token_type_ids is None", entity=code_entity_4, parameter="token_type_ids") BY role_user STATUS observed SOURCE "t1:s6" -> validates_parameter_2 : CLAIM
    TERM code_entity(file="modeling_convbert.py", kind="variable", name="seq_length", project=platform_label::transformers) -> code_entity_5 : TERM
    CLAIM leads_to(cause=code_entity_4, effect=code_entity_5) BY role_user STATUS asserted SOURCE "t1:s10" -> leads_to_2 : CLAIM
    CLAIM validates_parameter(condition="inputs_embeds is not None", entity=code_entity_4, parameter="inputs_embeds") BY role_user STATUS observed SOURCE "t1:s16" -> validates_parameter_3 : CLAIM
    TERM test_condition(condition="seq_length_missing_or_misuse", expected=TRUE) -> test_condition_2 : TERM
    UTTER ask(target=test_condition_2)
    CLAIM request(target="ArthurZucker, younesbelkada") BY role_user STATUS asserted SOURCE "t1:s22" -> request_2 : CLAIM
    TERM activity(actor="user", instrument=platform_label::transformers, object="modified_scripts", verb="run") -> activity_3 : TERM
    CLAIM user_practice(activity=activity_3) BY role_user STATUS asserted SOURCE "t1:s25" -> user_practice_2 : CLAIM
    TERM activity(actor="user", instrument=platform_label::transformers, object="custom_dataset", verb="run") -> activity_4 : TERM
    CLAIM user_practice(activity=activity_4) BY role_user STATUS asserted SOURCE "t1:s28" -> user_practice_3 : CLAIM
    TERM code_entity(kind="variable", name="inputs_embeds", project=platform_label::transformers) -> code_entity_6 : TERM
    TERM code_entity(kind="variable", name="attention_mask", project=platform_label::transformers) -> code_entity_7 : TERM
    TERM calculation(inputs=[code_entity_6, code_entity_7], operation="forward", result=code_entity_2) -> calculation_2 : TERM
    TERM activity(instrument=platform_label::transformers, object=calculation_2, verb="reproduce") -> activity_5 : TERM
    CLAIM user_practice(activity=activity_5) BY role_user STATUS asserted SOURCE "t1:s30" -> user_practice_4 : CLAIM
    TERM test_condition(condition="error_free_execution", expected=TRUE) -> test_condition_3 : TERM
    TERM negation(target=test_condition_3) -> negation_2 : TERM
    TERM temporal_context(activity=activity_5) -> temporal_context_2 : TERM
    CLAIM attribute_claim(property="expected_behavior", subject=temporal_context_2, value=negation_2) BY role_user STATUS asserted SOURCE "t1:s32" -> attribute_claim_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM code_entity(file="src/transformers/models/convbert/modeling_convbert.py", kind="source_file", name="modeling_convbert.py", project=platform_label::transformers) -> code_entity_8 : TERM
    TERM chg_modify_code(target=platform_label::transformers, file="src/transformers/models/convbert/modeling_convbert.py", revision=code_entity_8) -> chg_modify_code_2 : TERM
    UTTER propose(target=chg_modify_code_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | raises_exception | covered |
| n2 | speech_act | greeting, acknowledge | covered |
| n3 | object | platform_label::transformers | label-preserved |
| n4 | action | code_entity, activity | covered |
| n5 | object | code_entity | covered |
| n6 | claim | validates_parameter | covered |
| n7 | claim | leads_to, code_entity | covered |
| n8 | claim | validates_parameter | covered |
| n9 | speech_act | test_condition, ask | covered |
| n10 | object | request | covered |
| n11 | claim | activity, user_practice, platform_label::transformers | covered |
| n12 | claim | activity, user_practice, platform_label::transformers | covered |
| n13 | action | calculation, activity, user_practice | covered |
| n14 | constraint | test_condition | covered |
| n15 | negation | negation, temporal_context, attribute_claim | covered |
| n16 | action | code_entity, chg_modify_code, propose | covered |
| n17 | object | platform_label::transformers | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s2 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "transformers" → platform_label::transformers (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
