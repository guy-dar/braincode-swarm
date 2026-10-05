Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM raises_exception(exception_type="UnboundLocalError", message="local variable 'seq_length' referenced before assignment") BY role_user STATUS reported SOURCE "t1:s1" -> raises_exception_2 : CLAIM
    TERM greeting(recipient="all") -> greeting_2 : TERM
    UTTER inform(target=raises_exception_2)
    TERM code_entity(file="src/transformers/models/convbert/modeling_convbert.py", kind="class", name="ConvBertForTokenClassification", project=platform_label::transformers) -> code_entity_2 : TERM
    TERM code_entity(kind="method", name="forward", project=platform_label::transformers) -> code_entity_3 : TERM
    TERM code_entity(file="src/transformers/models/convbert/modeling_convbert.py", kind="source_file", name="modeling_convbert.py", project=platform_label::transformers) -> code_entity_4 : TERM
    TERM code_entity(kind="variable", name="token_type_ids", project=platform_label::transformers) -> code_entity_5 : TERM
    TERM code_entity(kind="variable", name="seq_length", project=platform_label::transformers) -> code_entity_6 : TERM
    CLAIM leads_to(cause=code_entity_5, effect=code_entity_6) BY role_user STATUS inferred SOURCE "t1:s10" -> leads_to_2 : CLAIM
    TERM code_entity(kind="variable", name="inputs_embeds", project=platform_label::transformers) -> code_entity_7 : TERM
    CLAIM request(target="maintainer_review") BY role_user STATUS asserted SOURCE "t1:s22" -> request_2 : CLAIM
    TERM activity(actor="user", verb="run_custom_script") -> activity_2 : TERM
    CLAIM user_practice(activity=activity_2) BY role_user STATUS asserted SOURCE "t1:s25" -> user_practice_2 : CLAIM
    TERM activity(actor="user", verb="run_custom_dataset") -> activity_3 : TERM
    CLAIM user_practice(activity=activity_3) BY role_user STATUS asserted SOURCE "t1:s28" -> user_practice_3 : CLAIM
    TERM issue(number=833, project=platform_label::transformers) -> issue_2 : TERM
    TERM test_condition(condition="no_error", expected=TRUE) -> test_condition_2 : TERM
    TERM negation(target=test_condition_2) -> negation_2 : TERM
    UTTER ask(target=code_entity_6)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM chg_modify_code(target=platform_label::transformers, file="src/transformers/models/convbert/modeling_convbert.py", revision=code_entity_6) -> chg_modify_code_2 : TERM
    RECORD ACTION modify_code(target=platform_label::transformers, file="src/transformers/models/convbert/modeling_convbert.py", revision=chg_modify_code_2) STATUS attempted SOURCE "t2:s2" -> modify_code_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | raises_exception | covered |
| n2 | speech_act | greeting, inform, raises_exception | covered |
| n3 | object | platform_label::transformers | label-preserved |
| n4 | action | code_entity | covered |
| n5 | object | code_entity | covered |
| n6 | claim | raises_exception | covered |
| n7 | claim | leads_to | covered |
| n8 | claim | code_entity | covered |
| n9 | speech_act | ask, raises_exception | covered |
| n10 | object | request, role_user | covered |
| n11 | claim | user_practice, chg_modify_code, leads_to | covered |
| n12 | claim | user_practice, leads_to | covered |
| n13 | action | issue | covered |
| n14 | constraint | raises_exception, test_condition | covered |
| n15 | negation | negation, raises_exception, test_condition | covered |
| n16 | action | chg_modify_code, modify_code | covered |
| n17 | object | chg_modify_code, code_entity, modify_code, platform_label::transformers | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s2 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "ConvBertForTokenClassification" → platform_label::transformers (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
