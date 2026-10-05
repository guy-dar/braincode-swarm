Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM raises_exception(exception_type="UnboundLocalError", message="local variable 'seq_length' referenced before assignment") BY role_user STATUS observed SOURCE "t1:s1" -> raises_exception_2 : CLAIM
    
    TERM subject(kind="ConvBertForTokenClassification", qualifier=platform_label::transformers) -> model_subject : TERM
    
    UTTER inform(target=raises_exception_2)
    
    TERM code_entity(file="src/transformers/models/convbert/modeling_convbert.py", kind="method", name="forward", project=platform_label::transformers) -> forward_method : TERM
    
    CLAIM raises_exception(target=forward_method) BY role_user STATUS observed SOURCE "t1:s4" -> raises_exception_at_line : CLAIM
    
    TERM conditional(
      condition="token_type_ids is None",
      consequence="slice token_type_ids by seq_length"
    ) -> conditional_token_type_check : TERM
    
    CLAIM leads_to(
      cause=conditional_token_type_check,
      effect="requires seq_length value"
    ) BY role_user STATUS inferred SOURCE "t1:s8" -> leads_to_seq_length_requirement : CLAIM
    
    TERM conditional(
      condition="input_ids is not None",
      consequence="assign batch_size and seq_length"
    ) -> conditional_input_ids : TERM
    
    TERM conditional(
      condition="inputs_embeds is not None",
      consequence="assign input_shape without seq_length"
    ) -> conditional_inputs_embeds : TERM
    
    CLAIM leads_to(
      cause=conditional_inputs_embeds,
      effect=raises_exception_2
    ) BY role_user STATUS inferred SOURCE "t1:s19" -> leads_to_error : CLAIM
    
    TERM activity(verb="call", object="forward", instrument=model_subject, purpose="pass input_embeds") -> call_forward_activity : TERM
    
    UTTER ask(target=leads_to_error)
    
    CLAIM request(target="ArthurZucker") BY role_user STATUS asserted SOURCE "t1:s22" -> request_arthur : CLAIM
    
    CLAIM request(target="younesbelkada") BY role_user STATUS asserted SOURCE "t1:s22" -> request_younes : CLAIM
    
    CLAIM example_of(example="own modified scripts", concept="script source") BY role_user STATUS asserted SOURCE "t1:s25" -> example_modified_scripts : CLAIM
    
    CLAIM example_of(example="own task or dataset", concept="evaluation setup") BY role_user STATUS asserted SOURCE "t1:s28" -> example_custom_task : CLAIM
    
    TERM activity(verb="pass", instrument=model_subject, object="inputs_embeds and attention_mask") -> reproduce_activity : TERM
    
    UTTER inform(target=reproduce_activity)
    
    TERM test_condition(condition="inputs_embeds provided to forward", expected=TRUE) -> test_no_error : TERM
    
    UTTER ask(target=test_no_error)
  }
  
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM chg_modify_code(
      target=platform_label::transformers,
      file="src/transformers/models/convbert/modeling_convbert.py",
      revision="assign seq_length in inputs_embeds branch"
    ) -> modification : TERM
    
    UTTER offer(target=modification)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | raises_exception | covered |
| n2 | speech_act | utter inform, subject TERM | covered |
| n3 | object | subject constructor with kind and qualifier | covered |
| n4 | action | call_forward_activity TERM | covered |
| n5 | object | code_entity for modeling_convbert.py | covered |
| n6 | claim | conditional_token_type_check, leads_to_seq_length_requirement | covered |
| n7 | claim | conditional_inputs_embeds, leads_to_error | covered |
| n8 | claim | conditional_inputs_embeds showing missing assignment | covered |
| n9 | speech_act | utter ask with leads_to_error target | covered |
| n10 | object | request claims for maintainers | covered |
| n11 | claim | example_of for modified scripts | covered |
| n12 | claim | example_of for custom task/dataset | covered |
| n13 | action | reproduce_activity TERM | covered |
| n14 | constraint | test_condition with expected=TRUE | covered |
| n15 | negation | constraint in ask speech act | covered |
| n16 | action | chg_modify_code | covered |
| n17 | object | platform_label::transformers in multiple places | covered |

## Translation report

- Input kind: conversation (GitHub issue report)
- Coverage status: complete
- Source-span coverage: t1:s1-s32 recorded; t2:s1-s2 recorded. All needs expressed.
- Opaque-text spans: none
- Label-preserved spans: none (n3 checker flag is due to subject() constructor using platform_label qualifier; structure is semantic, not label-only)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` run completed; all glossary symbols valid; n3 flagged by checker but uses semantic subject() constructor
