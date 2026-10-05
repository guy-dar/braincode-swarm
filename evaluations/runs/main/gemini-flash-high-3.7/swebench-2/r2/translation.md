Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM code_entity(kind="method", name="__nonzero__", project=platform_label::pandas) -> code_entity_2 : TERM
    CLAIM request(target=code_entity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
    TERM code_entity(kind="class", name="DataFrame", project=platform_label::pandas) -> code_entity_3 : TERM
    CLAIM instantiates(target=code_entity_3, entity=code_entity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> instantiates_2 : CLAIM
    TERM test_condition(condition=state_empty, expected=TRUE) -> test_condition_2 : TERM
    CLAIM enables(condition=code_entity_2, outcome=test_condition_2) BY role_user STATUS asserted SOURCE "t1:s2" -> enables_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM chg_modify_code(target=platform_label::pandas, file="RELEASE.rst", revision=t1.code_entity_2) -> chg_modify_code_2 : TERM
    UTTER propose(target=chg_modify_code_2)
    TERM chg_modify_code(target=platform_label::pandas, file="doc/source/v0.11.1.txt", revision=t1.code_entity_2) -> chg_modify_code_3 : TERM
    UTTER propose(target=chg_modify_code_3)
    TERM chg_modify_code(target=platform_label::pandas, file="pandas/core/frame.py", revision=t1.code_entity_2) -> chg_modify_code_4 : TERM
    UTTER propose(target=chg_modify_code_4)
    TERM chg_modify_code(target=platform_label::pandas, file="pandas/core/generic.py", revision=t1.code_entity_2) -> chg_modify_code_5 : TERM
    UTTER propose(target=chg_modify_code_5)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request | covered |
| n2 | action | code_entity, request | covered |
| n3 | object | code_entity | covered |
| n4 | object | code_entity, instantiates | covered |
| n5 | action | test_condition, state_empty | covered |
| n6 | constraint | test_condition | covered |
| n7 | claim | enables | covered |
| n8 | action | chg_modify_code, propose | covered |
| n9 | object | chg_modify_code | covered |
| n10 | action | chg_modify_code, propose | covered |
| n11 | object | chg_modify_code | covered |
| n12 | action | chg_modify_code, propose | covered |
| n13 | object | chg_modify_code | covered |
| n14 | object | platform_label::pandas | label-preserved |
| n15 | action | chg_modify_code, propose | covered |
| n16 | object | chg_modify_code | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s8 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s6 "pandas" → platform_label::pandas (open label platform name)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
