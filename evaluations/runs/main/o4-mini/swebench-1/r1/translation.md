Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM raises_exception(target=NONE, exception_type="UnboundLocalError", message="local variable 'seq_length' referenced before assignment")
      BY role_user STATUS observed SOURCE "t1:s1" -> raises_exception_2 : CLAIM
    UTTER inform(target=raises_exception_2)

    UTTER greeting(recipient=role_agent)

    TERM code_entity(kind="class", name="ConvBertForTokenClassification", project=platform_label::transformers)
      -> model_entity : TERM
    UTTER inform(target=model_entity)

    LET forward_method = TERM code_entity(kind="method", name="forward", project=platform_label::transformers)
      -> forward_method : TERM
    TERM activity(verb="call", object=forward_method, instrument=model_entity) -> call_forward : TERM
    UTTER inform(target=call_forward)

    TERM code_entity(file="src/transformers/models/convbert/modeling_convbert.py", kind="file", name="modeling_convbert.py", project=platform_label::transformers)
      -> file_entity : TERM
    UTTER inform(target=file_entity)

    LET token_type_ids_entity = TERM code_entity(kind="attribute", name="token_type_ids", project=platform_label::transformers)
      -> token_type_ids_entity : TERM
    CLAIM has_state(subject=token_type_ids_entity, state=state_sliced)
      BY role_user STATUS observed SOURCE "t1:s6" -> sliced_state : CLAIM
    UTTER inform(target=sliced_state)

    LET seq_length_var = TERM code_entity(kind="variable", name="seq_length", project=platform_label::transformers)
      -> seq_length_var : TERM
    TERM assert_variable_assigned(variable=seq_length_var) -> assert_seq_assigned : TERM  # PROPOSED: S1
    UTTER inform(target=assert_seq_assigned)

    LET inputs_embeds_var = TERM code_entity(kind="parameter", name="inputs_embeds", project=platform_label::transformers)
      -> inputs_embeds_var : TERM
    TERM assert_unpack_missing(variable=inputs_embeds_var) -> assert_unpack_missing : TERM  # PROPOSED: S2
    UTTER inform(target=assert_unpack_missing)

    UTTER ask(target=q_topic)
  }

  TURN t2 SPEAKER=AGENT {
    ACTION modify_code(target=platform_label::transformers,
                       file="src/transformers/models/convbert/modeling_convbert.py",
                       revision=assert_seq_assigned)
  }
}
```

## Needs coverage

| need | kind       | expressed by                     | status     |
|------|------------|-----------------------------------|------------|
| n1   | claim      | raises_exception                  | covered    |
| n2   | speech_act | greeting                          | covered    |
| n3   | object     | code_entity                       | covered    |
| n4   | action     | activity                          | covered    |
| n5   | object     | code_entity                       | covered    |
| n6   | claim      | has_state                         | covered    |
| n7   | claim      | assert_variable_assigned          | proposed   |
| n8   | claim      | assert_unpack_missing             | proposed   |
| n9   | speech_act | ask                               | covered    |
| n10  | object     | —                                 | unresolved |
| n11  | claim      | —                                 | unresolved |
| n12  | claim      | —                                 | unresolved |
| n13  | action     | —                                 | unresolved |
| n14  | constraint | test_condition                    | covered    |
| n15  | negation   | test_condition                    | covered    |
| n16  | action     | modify_code                       | covered    |
| n17  | object     | code_entity                       | covered    |

## Why the translation failed

- n7 “seq_length variable remains unassigned in execution path”: no existing constructor or relation asserts that a variable is assigned.
- n8 “inputs_embeds branch extracts input_shape but omits unpacking seq_length”: no symbol to express a missing unpack operation.
- n10 “requested maintainers ArthurZucker and younesbelkada”: no lexical group or constructor for user-handle identifiers.
- n11 “running custom modified script rather than official example”: no claim relation for distinguishing custom vs. official script.
- n12 “running custom task or dataset rather than standard benchmark”: no claim relation for custom dataset vs. standard benchmark.
- n13 “reproduce bug by passing inputs_embeds and attention_mask”: no operation or constructor to represent calling a method with specified arguments.

## Translation report

- Input kind: prompt | conversation
- Coverage status: partial
- Source-span coverage: represented t1:s1–t1:s6, t1:s10, t1:s19, t1:s32, t2:s2; other spans require missing symbols
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1, S2
- Unresolved ambiguities: maintainers’ identifiers (n10)
- Check: `rag check` reported unresolved needs n7, n8, n10, n11, n12, n13 and unknown symbols assert_variable_assigned, assert_unpack_missing
