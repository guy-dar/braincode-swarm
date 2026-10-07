Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="state", subject="Bob", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="personality", subject="Bob", value="nice") BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="temperament", subject="Bob", value="quiet") BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Bob", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    TERM lexical_label(value=color_label::white) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="Bob", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="texture", subject="Fiona", value="rough") BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="intelligence", subject="Fiona", value="smart") BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Gary", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s9" -> attribute_claim_9 : CLAIM
    CLAIM attribute_claim(property="state", subject="Harry", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_10 : CLAIM
    CLAIM attribute_claim(property="intelligence", subject="Harry", value="smart") BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_11 : CLAIM
    TERM subject(kind="person", qualifier=lexical_label_2) -> subject_2 : TERM
    TERM subject(kind="person", qualifier=state_cold) -> subject_3 : TERM
    TERM conditional(condition=subject_2, consequence=subject_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_2 : CLAIM
    TERM subject(kind="person", qualifier=shape_round) -> subject_4 : TERM
    TERM conditional(condition=subject_4, consequence=subject_2) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_3 : CLAIM
    TERM subject(kind="person", qualifier="rough") -> subject_5 : TERM
    TERM subject(kind="person", qualifier="quiet") -> subject_6 : TERM
    TERM conjunction(items=[subject_5, subject_6]) -> conjunction_2 : TERM
    TERM subject(kind="person", qualifier="nice") -> subject_7 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_7) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_4 : CLAIM
    TERM conditional(condition=subject_7, consequence=subject_4) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_5 : CLAIM
    TERM conjunction(items=[subject_5, subject_2]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_6) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_6 : CLAIM
    TERM conditional(condition=subject_3, consequence=subject_4) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_7 : CLAIM
    TERM conditional(condition=subject_5, consequence=subject_6) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_8 : CLAIM
    TERM subject(kind="Fiona", qualifier=shape_round) -> subject_8 : TERM
    TERM negation(target=subject_8) -> negation_2 : TERM
    TERM test_condition(condition="statement_truth_value", expected=TRUE) -> test_condition_2 : TERM
    UTTER ask(target=negation_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject | covered |
| n2 | claim | attribute_claim, state_cold | covered |
| n3 | object | Bob | covered |
| n4 | object | state_cold | covered |
| n5 | claim | attribute_claim | covered |
| n6 | object | nice | covered |
| n7 | claim | attribute_claim | covered |
| n8 | object | quiet | covered |
| n9 | claim | attribute_claim, shape_round | covered |
| n10 | object | shape_round | covered |
| n11 | claim | attribute_claim, color_label | covered |
| n12 | object | color_label::white | label-preserved |
| n13 | claim | attribute_claim | covered |
| n14 | object | Fiona | covered |
| n15 | object | rough | covered |
| n16 | claim | attribute_claim | covered |
| n17 | object | smart | covered |
| n18 | claim | attribute_claim, shape_round | covered |
| n19 | object | Gary | covered |
| n20 | claim | attribute_claim, state_cold | covered |
| n21 | object | Harry | covered |
| n22 | claim | attribute_claim | covered |
| n23 | reasoning | conditional, statement, state_cold, color_label | covered |
| n24 | reasoning | conditional, statement, shape_round, color_label | covered |
| n25 | reasoning | conditional, statement, conjunction | covered |
| n26 | reasoning | conditional, statement, shape_round | covered |
| n27 | reasoning | conditional, statement, conjunction, color_label | covered |
| n28 | reasoning | conditional, statement, state_cold, shape_round | covered |
| n29 | reasoning | conditional, statement | covered |
| n30 | speech_act | ask | covered |
| n31 | action | test_condition | covered |
| n32 | constraint | subject | covered |
| n33 | constraint | test_condition | covered |
| n34 | claim | statement, shape_round | covered |
| n35 | negation | negation, shape_round | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s20 is represented.
- Opaque-text spans: none
- Label-preserved spans: t1:s6, t1:s12, t1:s13, t1:s16 "white" -> color_label::white (open-label qualifier)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unknown symbols and passed.
