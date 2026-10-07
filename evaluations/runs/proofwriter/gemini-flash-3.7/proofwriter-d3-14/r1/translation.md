Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    UTTER inform(target=subject_2)
    TERM subject(kind="Charlie", qualifier="kind") -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM subject(kind="Charlie", qualifier="nice") -> subject_4 : TERM
    CLAIM statement(fact=subject_4) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM subject(kind="Charlie", qualifier="quiet") -> subject_5 : TERM
    CLAIM statement(fact=subject_5) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM character_trait(property="temperament", value="rough") -> character_trait_2 : TERM
    TERM subject(kind="Dave", qualifier=character_trait_2) -> subject_6 : TERM
    CLAIM statement(fact=subject_6) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM lexical_label(value=color_label::white) -> lexical_label_2 : TERM
    TERM subject(kind="Dave", qualifier=lexical_label_2) -> subject_7 : TERM
    CLAIM statement(fact=subject_7) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM subject(kind="Erin", qualifier="nice") -> subject_8 : TERM
    CLAIM statement(fact=subject_8) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM negation(target=lexical_label_2) -> negation_2 : TERM
    TERM subject(kind="Gary", qualifier=negation_2) -> subject_9 : TERM
    CLAIM statement(fact=subject_9) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM subject(kind="entity", qualifier=state_cold) -> subject_10 : TERM
    TERM subject(kind="entity", qualifier="furry") -> subject_11 : TERM
    TERM negation(target=subject_11) -> negation_3 : TERM
    TERM conditional(condition=subject_10, consequence=negation_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM conditional(condition=subject_5, consequence=subject_4) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM subject(kind="entity", qualifier="kind") -> subject_12 : TERM
    TERM subject(kind="entity", qualifier=lexical_label_2) -> subject_13 : TERM
    TERM conditional(condition=subject_12, consequence=subject_13) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM subject(kind="entity", qualifier="nice") -> subject_14 : TERM
    TERM conditional(condition=subject_14, consequence=subject_12) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM subject(kind="entity", qualifier="rough") -> subject_15 : TERM
    TERM conditional(condition=subject_15, consequence=subject_12) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM subject(kind="entity", qualifier="quiet") -> subject_16 : TERM
    TERM conjunction(items=[subject_10, subject_16]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_15) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM conditional(condition=subject_10, consequence=subject_16) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM conjunction(items=[subject_13, subject_14]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_10) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM subject(kind="Erin", qualifier=state_cold) -> subject_17 : TERM
    TERM conditional(condition=subject_17, consequence=subject_8) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM requirement(property="basis", value="theory") -> requirement_2 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM test_condition(condition="truth_value", expected=TRUE) -> test_condition_2 : TERM
    TERM character_trait(property="temperament", value="rough") -> character_trait_3 : TERM
    TERM subject(kind="Charlie", qualifier=character_trait_3) -> subject_18 : TERM
    TERM negation(target=subject_18) -> negation_4 : TERM
    CLAIM statement(fact=negation_4) BY role_user STATUS hypothesized SOURCE "t1:s19" -> statement_18 : CLAIM
    UTTER ask(target=negation_4, constraints=[constraint_single_choice_2, requirement_2, test_condition_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | inform, subject | covered |
| n2 | claim | statement, subject | covered |
| n3 | claim | statement, subject | covered |
| n4 | claim | statement, subject | covered |
| n5 | claim | statement, subject, character_trait | covered |
| n6 | claim | statement, subject, lexical_label, color_label::white | covered |
| n7 | constraint | color_label::white | label-preserved |
| n8 | claim | statement, subject | covered |
| n9 | claim | statement, subject, negation, lexical_label, color_label::white | covered |
| n10 | negation | negation | covered |
| n11 | constraint | color_label::white | label-preserved |
| n12 | reasoning | statement, conditional, subject, state_cold, negation | covered |
| n13 | negation | negation | covered |
| n14 | reasoning | statement, conditional, subject | covered |
| n15 | reasoning | statement, conditional, subject, lexical_label, color_label::white | covered |
| n16 | constraint | color_label::white | label-preserved |
| n17 | reasoning | statement, conditional, subject | covered |
| n18 | reasoning | statement, conditional, subject | covered |
| n19 | reasoning | statement, conditional, conjunction, subject, state_cold | covered |
| n20 | reasoning | statement, conditional, subject, state_cold | covered |
| n21 | reasoning | statement, conditional, conjunction, subject, state_cold, lexical_label, color_label::white | covered |
| n22 | constraint | color_label::white | label-preserved |
| n23 | reasoning | statement, conditional, subject, state_cold | covered |
| n24 | action | ask, test_condition | covered |
| n25 | constraint | requirement | covered |
| n26 | constraint | constraint_single_choice | covered |
| n27 | claim | statement, subject, negation, character_trait | covered |
| n28 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s6, t1:s8, t1:s11, t1:s16 "white" → color_label::white (open label; leaf color value)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
