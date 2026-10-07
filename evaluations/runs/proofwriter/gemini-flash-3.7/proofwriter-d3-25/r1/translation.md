Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # Theory facts
    TERM subject(kind="Anne") -> subject_2 : TERM
    TERM requirement(property="rough", value=TRUE) -> requirement_2 : TERM
    TERM negation(target=requirement_2) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM

    TERM subject(kind="Bob") -> subject_3 : TERM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_3 : TERM
    CLAIM statement(fact=requirement_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM

    TERM subject(kind="Erin") -> subject_4 : TERM
    TERM requirement(property="furry", value=TRUE) -> requirement_4 : TERM
    TERM negation(target=requirement_4) -> negation_3 : TERM
    CLAIM statement(fact=negation_3) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM

    TERM lexical_label(value=color_label::red) -> lexical_label_3 : TERM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_5 : TERM
    CLAIM statement(fact=requirement_5) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM

    TERM subject(kind="Gary") -> subject_5 : TERM
    TERM requirement(property="size", value=size_large) -> requirement_6 : TERM
    CLAIM statement(fact=requirement_6) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM

    TERM requirement(property="temperature", value=state_cold) -> requirement_7 : TERM
    TERM negation(target=requirement_7) -> negation_4 : TERM
    CLAIM statement(fact=negation_4) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM

    CLAIM statement(fact=requirement_4) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM

    # Theory rules
    # s9: If something is blue then it is rough.
    TERM conditional(condition=requirement_3, consequence=requirement_2) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM

    # s10: Red things are rough.
    TERM conditional(condition=requirement_5, consequence=requirement_2) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM

    # s11: If Gary is rough then Gary is not blue.
    TERM negation(target=requirement_3) -> negation_5 : TERM
    TERM conditional(condition=requirement_2, consequence=negation_5) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM

    # s12: Rough things are red.
    TERM conditional(condition=requirement_2, consequence=requirement_5) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM

    # s13: Big things are quiet.
    TERM requirement(property="quiet", value=TRUE) -> requirement_8 : TERM
    TERM conditional(condition=requirement_6, consequence=requirement_8) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM

    # s14: All cold things are big.
    TERM conditional(condition=requirement_7, consequence=requirement_6) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM

    # s15: If something is red then it is big.
    TERM conditional(condition=requirement_5, consequence=requirement_6) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM

    # s16: If something is blue and not rough then it is big.
    TERM conjunction(items=[requirement_3, negation_2]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_6) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM

    # s17: Quiet, big things are not cold.
    TERM conjunction(items=[requirement_8, requirement_6]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=negation_4) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM

    # Question (s18, s19)
    # s18: Question: Based only on the theory, is the following statement True, False, or Unknown?
    # s19: Gary is not rough.
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_18 : CLAIM
    TERM property_question(property="truth_value", subject="theory") -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject | covered |
| n2 | claim | statement | covered |
| n3 | negation | negation | covered |
| n4 | object | subject | covered |
| n5 | claim | statement, color_label | covered |
| n6 | object | subject | covered |
| n7 | constraint | color_label | label-preserved |
| n8 | claim | statement, negation | covered |
| n9 | negation | negation | covered |
| n10 | object | subject | covered |
| n11 | claim | statement, color_label | covered |
| n12 | object | subject | covered |
| n13 | constraint | color_label | label-preserved |
| n14 | claim | statement, size_large | covered |
| n15 | object | subject | covered |
| n16 | claim | statement, state_cold | covered |
| n17 | negation | negation, state_cold | covered |
| n18 | object | subject | covered |
| n19 | claim | statement | covered |
| n20 | object | subject | covered |
| n21 | reasoning | conditional, color_label | label-preserved |
| n22 | constraint | color_label | label-preserved |
| n23 | reasoning | conditional, color_label | label-preserved |
| n24 | constraint | color_label | label-preserved |
| n25 | reasoning | conditional, color_label | label-preserved |
| n26 | negation | negation, color_label | covered |
| n27 | constraint | color_label | label-preserved |
| n28 | reasoning | conditional, color_label | label-preserved |
| n29 | constraint | color_label | label-preserved |
| n30 | reasoning | conditional, size_large | covered |
| n31 | reasoning | conditional, state_cold, size_large | covered |
| n32 | reasoning | conditional, color_label, size_large | covered |
| n33 | constraint | color_label | label-preserved |
| n34 | reasoning | conditional, color_label, negation, size_large | covered |
| n35 | negation | negation | covered |
| n36 | constraint | color_label | label-preserved |
| n37 | reasoning | conditional, state_cold, size_large, negation | covered |
| n38 | negation | negation, state_cold | covered |
| n39 | speech_act | ask, statement | covered |
| n40 | constraint | subject, property_question | covered |
| n41 | constraint | subject, property_question | covered |
| n42 | claim | statement | covered |
| n43 | negation | negation | covered |
| n44 | object | subject | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "blue" -> color_label::blue; t1:s5 "red" -> color_label::red; t1:s9 "blue" -> color_label::blue; t1:s10 "red" -> color_label::red; t1:s11 "blue" -> color_label::blue; t1:s12 "red" -> color_label::red; t1:s15 "red" -> color_label::red; t1:s16 "blue" -> color_label::blue
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
