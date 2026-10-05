Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM code_entity(kind="class", name="ConvBertForTokenClassification", project=platform_label::transformers) -> code_entity_2 : TERM
    TERM code_entity(file="modeling_convbert.py", kind="line", name="833", project=platform_label::transformers) -> code_entity_3 : TERM
    TERM code_entity(kind="method", name="forward", project=platform_label::transformers) -> code_entity_4 : TERM
    CLAIM raises_exception(exception_type="UnboundLocalError", message="local variable 'seq_length' referenced before assignment", target=code_entity_3) BY role_user STATUS reported SOURCE "t1:s1" -> raises_exception_2 : CLAIM
    TERM requirement(property="only_argument", value="inputs_embeds") -> requirement_2 : TERM
    TERM activity(object=code_entity_4, verb="call", instrument=platform_label::transformers, purpose=requirement_2) -> activity_2 : TERM
    TERM code_entity(kind="variable", name="token_type_ids", project=platform_label::transformers) -> code_entity_5 : TERM
    CLAIM reads_variable(condition="token_type_ids_is_none", entity=code_entity_3, variable="seq_length") BY role_user STATUS observed SOURCE "t1:s8" -> reads_variable_2 : CLAIM   # PROPOSED: S2
    CLAIM variable_unassigned(path="inputs_embeds_branch", variable="seq_length", entity=code_entity_4) BY role_user STATUS asserted SOURCE "t1:s10" -> variable_unassigned_2 : CLAIM   # PROPOSED: S1
    CLAIM lacks_statement(entity=code_entity_4, statement="batch_size, seq_length = input_shape", branch="inputs_embeds is not None") BY role_user STATUS observed SOURCE "t1:s19" -> lacks_statement_2 : CLAIM   # PROPOSED: S3
    CLAIM leads_to(cause=lacks_statement_2, effect=variable_unassigned_2) BY role_user STATUS inferred SOURCE "t1:s19" -> leads_to_2 : CLAIM
    UTTER inform(target=raises_exception_2)
    UTTER inform(target=lacks_statement_2)
    TERM alternatives(items=["bug_missing_unpacking", "user_misuse_of_model"]) -> alternatives_2 : TERM   # PROPOSED: S4
    UTTER ask(target=alternatives_2)
    TERM activity(verb="request_help", actor=role_user, object="ArthurZucker, younesbelkada") -> activity_3 : TERM
    CLAIM request(target=activity_3) BY role_user STATUS asserted SOURCE "t1:s22" -> request_2 : CLAIM
    TERM activity(verb="run", actor=role_user, object="own_modified_scripts") -> activity_4 : TERM
    CLAIM user_practice(activity=activity_4) BY role_user STATUS asserted SOURCE "t1:s25" -> user_practice_2 : CLAIM
    TERM activity(verb="run", actor=role_user, object="own_task_or_dataset") -> activity_5 : TERM
    CLAIM user_practice(activity=activity_5) BY role_user STATUS asserted SOURCE "t1:s28" -> user_practice_3 : CLAIM
    TERM test_condition(condition="raises_UnboundLocalError", expected=FALSE) -> test_condition_2 : TERM
    CLAIM request(target=test_condition_2) BY role_user STATUS asserted SOURCE "t1:s32" -> request_3 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM code_entity(file="src/transformers/models/convbert/modeling_convbert.py", kind="file", name="modeling_convbert.py", project=platform_label::transformers) -> code_entity_6 : TERM
    TERM activity(verb="modify", object=code_entity_6) -> activity_6 : TERM
    UTTER respond(target=activity_6)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | raises_exception | covered |
| n2 | speech_act | inform | covered |
| n3 | object | code_entity, platform_label::transformers | label-preserved |
| n4 | action | activity, requirement, code_entity | covered |
| n5 | object | code_entity | covered |
| n6 | claim | reads_variable (PROPOSED: S2) | proposed |
| n7 | claim | variable_unassigned (PROPOSED: S1) | proposed |
| n8 | claim | lacks_statement (PROPOSED: S3) | proposed |
| n9 | speech_act | ask, alternatives (PROPOSED: S4) | proposed |
| n10 | object | activity, request | covered |
| n11 | claim | user_practice, activity | covered |
| n12 | claim | user_practice, activity | covered |
| n13 | action | activity, requirement | covered |
| n14 | constraint | test_condition, request | covered |
| n15 | negation | test_condition | covered |
| n16 | action | activity, code_entity, respond | covered |
| n17 | object | platform_label::transformers | label-preserved |

## Why the translation failed

- n6 (slicing uses seq_length when token_type_ids is None): searched candidates (slice, state_sliced, validates_parameter, raises_exception) → none relates a code entity reading a variable under a condition. Proposed S2.
- n7 (seq_length stays unassigned): search "variable unassigned" → raises_exception (the error, not the dataflow state), has_state (physical state of TERM). Proposed S1.
- n8 (branch omits unpacking): duplicate_definition, modify_code don't express an absent statement. Proposed S3.
- n9 (bug or misuse): ask accepts a TERM but no constructor for alternatives (conjunction is "all apply", wrong). Proposed S4.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1–s32 and t2:s2 represented; code snippet lines t1:s6–s8, s13–s17 only via summary claims; markdown headings/checkbox lines (s2, s5, s9, s12, s18, s21, s23, s24, s26, s27, s29, s31) are structure, covered via the claims they qualify. t2:s1 "1." is a list marker.
- Opaque-text spans: none (string args in proposed claims are descriptive and pending S1–S4)
- Label-preserved spans: t1:s3 / t2:s2 "transformers" → platform_label::transformers (label only)
- Missing constructs: S1 variable_unassigned; S2 reads_variable; S3 lacks_statement; S4 alternatives; greeting in s3 omitted (recipient unstated); line 833 expressed via code_entity kind="line"; chg_modify_code revision unspecified in source
- Unresolved ambiguities: t2:s2 agent "modify" is a plan/step, encoded as respond with an activity description; "Hi" greeting not encoded
- Check: pending
