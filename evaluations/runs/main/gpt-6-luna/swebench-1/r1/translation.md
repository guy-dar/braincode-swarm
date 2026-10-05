Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM code_entity(file="src/transformers/models/convbert/modeling_convbert.py", kind="method", name="forward", project=platform_label::transformers) -> code_entity_2 : TERM
    TERM code_entity(kind="class", name="ConvBertForTokenClassification", project=platform_label::transformers) -> code_entity_3 : TERM
    CLAIM raises_exception(message="local variable 'seq_length' referenced before assignment", target=code_entity_2, exception_type="UnboundLocalError") BY role_user STATUS reported SOURCE "t1:s1" -> raises_exception_2 : CLAIM
    UTTER inform(target=raises_exception_2)
    TERM code_statement(entity=code_entity_2, form="call", reads=["input_embeds"], writes=[]) -> code_statement_2 : TERM  # PROPOSED: S1
    CLAIM statement(fact=code_statement_2) BY role_user STATUS reported SOURCE "t1:s3" -> statement_2 : CLAIM
    TERM code_entity(file="src/transformers/models/convbert/modeling_convbert.py", kind="source_file", name="modeling_convbert.py", project=platform_label::transformers) -> code_entity_4 : TERM
    TERM code_statement(entity=code_entity_2, form="source_location", reads=[], writes=[], location="line 833") -> code_statement_7 : TERM  # PROPOSED: S1
    CLAIM statement(fact=code_statement_7) BY role_user STATUS reported SOURCE "t1:s4" -> statement_8 : CLAIM
    TERM test_condition(condition="token_type_ids_is_none", expected=TRUE) -> test_condition_2 : TERM
    TERM code_statement(entity=code_entity_2, form="slice_assignment", reads=["self.embeddings.token_type_ids", "seq_length"], writes=["buffered_token_type_ids"], condition=test_condition_2) -> code_statement_3 : TERM  # PROPOSED: S1
    CLAIM statement(fact=code_statement_3) BY role_user STATUS reported SOURCE "t1:s6" -> statement_3 : CLAIM
    TERM test_condition(condition="input_ids_is_not_none", expected=TRUE) -> test_condition_3 : TERM
    TERM code_statement(entity=code_entity_2, form="tuple_unpack_assignment", reads=["input_shape"], writes=["batch_size", "seq_length"], condition=test_condition_3) -> code_statement_4 : TERM  # PROPOSED: S1
    CLAIM statement(fact=code_statement_4) BY role_user STATUS reported SOURCE "t1:s13" -> statement_4 : CLAIM
    TERM test_condition(condition="inputs_embeds_is_not_none", expected=TRUE) -> test_condition_4 : TERM
    TERM code_statement(entity=code_entity_2, form="assignment", reads=["inputs_embeds.size()[:-1]"], writes=["input_shape"], condition=test_condition_4, unassigned=["batch_size", "seq_length"]) -> code_statement_5 : TERM  # PROPOSED: S1
    CLAIM statement(fact=code_statement_5) BY role_user STATUS reported SOURCE "t1:s16" -> statement_5 : CLAIM
    TERM property_question(property="whether_missing_batch_size_and_seq_length_unpacking_is_a_bug_or_model_misuse", subject=code_entity_3) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    CLAIM attribute_claim(property="listed_as_person_who_can_help_with_text_models", subject="ArthurZucker", value=TRUE) BY role_user STATUS reported SOURCE "t1:s22" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="listed_as_person_who_can_help_with_text_models", subject="younesbelkada", value=TRUE) BY role_user STATUS reported SOURCE "t1:s22" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="official_example_scripts_used", subject="issue_report", value=FALSE) BY role_user STATUS reported SOURCE "t1:s24" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="own_modified_scripts_used", subject="issue_report", value=TRUE) BY role_user STATUS reported SOURCE "t1:s25" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="officially_supported_examples_task_or_dataset_used", subject="issue_report", value=FALSE) BY role_user STATUS reported SOURCE "t1:s27" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="own_task_or_dataset_used", subject="issue_report", value=TRUE) BY role_user STATUS reported SOURCE "t1:s28" -> attribute_claim_7 : CLAIM
    TERM code_statement(entity=code_entity_2, form="call", reads=["inputs_embeds", "attention_mask"], writes=[]) -> code_statement_6 : TERM  # PROPOSED: S1
    CLAIM statement(fact=code_statement_6) BY role_user STATUS reported SOURCE "t1:s30" -> statement_6 : CLAIM
    TERM test_condition(condition="model_execution_raises_UnboundLocalError", expected=FALSE) -> test_condition_5 : TERM
    CLAIM statement(fact=test_condition_5) BY role_user STATUS asserted SOURCE "t1:s32" -> statement_7 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(object=code_entity_4, verb="modify") -> activity_2 : TERM
    CLAIM request(target=activity_2) BY role_agent STATUS reported SOURCE "t2:s2" -> request_2 : CLAIM
    UTTER inform(target=request_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | raises_exception | covered |
| n2 | speech_act | inform, raises_exception; salutation span not represented | opaque |
| n3 | object | code_entity, platform_label::transformers | label-preserved |
| n4 | action | code_statement (PROPOSED: S1) | proposed |
| n5 | object | code_entity, code_statement (PROPOSED: S1) | proposed |
| n6 | claim | code_statement (PROPOSED: S1), statement | proposed |
| n7 | claim | code_statement (PROPOSED: S1), statement | proposed |
| n8 | claim | code_statement (PROPOSED: S1), statement | proposed |
| n9 | speech_act | property_question, ask | covered |
| n10 | object | attribute_claim | covered |
| n11 | claim | attribute_claim | covered |
| n12 | claim | attribute_claim | covered |
| n13 | action | code_statement (PROPOSED: S1), statement | proposed |
| n14 | constraint | test_condition, statement | covered |
| n15 | negation | test_condition, statement | covered |
| n16 | action | activity, request | covered |
| n17 | object | platform_label::transformers | covered |

## Why the translation failed

- n4 (t1:s3), n6 (t1:s6–s8), n7 (t1:s10), n8 (t1:s13–s19), and n13 (t1:s30): `widen` searches for “conditional code branch leaves local variable unassigned,” “source code assigns variable in one branch but not another,” “token_type_ids is None and seq_length used to slice tensor,” “tuple unpacking omitted from input shape in code,” and “reproduce bug by passing inputs_embeds and attention_mask to model,” plus `search` queries for code-branch assignment, omitted tuple unpacking, and unbound-local exceptions. Candidates included `conditional`, `code_entity`, `slice`, and `raises_exception`; these describe conditional terms, code entities, a physical/material slicing operation, and runtime exceptions respectively, but none can represent source-code syntax and variable read/write/assignment structure. S1 supplies a typed syntax-description constructor for those facts, source locations, and call arguments. The named `code_statement` lines are proposed pending acceptance.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1–t1:s32 and t2:s2 represented, except the greeting at t1:s3 is opaque.
- Opaque-text spans: t1:s3 — the salutation “Hi” has no matching speech-act signature; no unsupported speech act was invented.
- Label-preserved spans: t1:s3 — `platform_label::transformers` preserves the software-project label; the model's exact class identifier is separately retained as a code-entity name.
- Missing constructs: S1 `code_statement` constructor for structured source-code syntax, source locations, and call/assignment facts.
- Unresolved ambiguities: none
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported unknown symbol `code_statement`; n3 label-preserved; and DECL for n7, n11, n12, n13, and n16. The generic `statement` claims for n7/n13, issue-form `attribute_claim`s for n11/n12, and the structured request for n16 are explicitly present; the checker did not credit them. The missing code-syntax constructor remains the substantive glossary gap.
