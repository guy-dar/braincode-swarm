Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="drawing_correctness", subject=platform_label::qiskit_terra, value=FALSE) BY role_user STATUS asserted SOURCE "t1:s1" -> attribute_claim_2 : CLAIM
    TERM software_version(project=platform_label::qiskit_terra, version="0.18.0.dev0+2ecf45d") -> software_version_2 : TERM
    CLAIM statement(fact=software_version_2) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_2 : CLAIM
    TERM software_version(project=platform_label::python, version="3.7") -> software_version_3 : TERM
    CLAIM statement(fact=software_version_3) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_3 : CLAIM
    CLAIM attribute_claim(property="composite_gate_drawing", subject=platform_label::qiskit_terra, value=FALSE) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="drawing_order_sensitivity", subject=platform_label::qiskit_terra, value="non_ascending_register_list") BY role_user STATUS hypothesized SOURCE "t1:s9" -> attribute_claim_4 : CLAIM
    TERM code_entity(kind="example_snippet", name="reproduction_circuit", project=platform_label::qiskit_terra) -> code_entity_2 : TERM
    CLAIM example_of(concept=code_entity_2, example=code_entity_2) BY role_user STATUS asserted SOURCE "t1:s10" -> example_of_2 : CLAIM
    TERM captioned_figure(caption="qiskit_text_error", label="https://user-images.githubusercontent.com/51048173/113936418-5b64cd00-9815-11eb-9ce2-7ac910e99d1d.png") -> captioned_figure_2 : TERM
    CLAIM attribute_claim(property="active_wire_numbering", subject=platform_label::qiskit_terra, value=FALSE) BY role_user STATUS asserted SOURCE "t1:s23" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="root_cause", subject=platform_label::qiskit_terra, value="component_drawing_order") BY role_user STATUS hypothesized SOURCE "t1:s25" -> attribute_claim_6 : CLAIM
    CLAIM causes(cause=attribute_claim_6, effect=attribute_claim_3) BY role_user STATUS hypothesized SOURCE "t1:s25" -> causes_2 : CLAIM
    TERM code_entity(file="qiskit/visualization/text.py", kind="function", name="line_1211", project=platform_label::qiskit_terra) -> code_entity_3 : TERM
    CLAIM statement(fact=code_entity_3) BY role_user STATUS asserted SOURCE "t1:s26" -> statement_4 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM chg_modify_code(target=platform_label::qiskit_terra, file="qiskit/visualization/text.py", revision=t1.code_entity_3) -> chg_modify_code_2 : TERM
    UTTER propose(target=chg_modify_code_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | attribute_claim | covered |
| n2 | object | platform_label::qiskit_terra | label-preserved |
| n3 | constraint | software_version, statement | covered |
| n4 | object | platform_label::python | label-preserved |
| n5 | constraint | software_version, statement | covered |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim | covered |
| n8 | object | code_entity, example_of | covered |
| n9 | object | captioned_figure | covered |
| n10 | claim | attribute_claim | covered |
| n11 | reasoning | attribute_claim, causes | covered |
| n12 | object | code_entity, statement | covered |
| n13 | action | chg_modify_code, propose | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s2 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s5 "Qiskit Terra" → platform_label::qiskit_terra; t1:s6 "Python" → platform_label::python
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
