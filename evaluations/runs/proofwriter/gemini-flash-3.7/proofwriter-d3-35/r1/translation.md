Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY role_user STATUS asserted SOURCE "t1:s1" -> statement_2 : CLAIM

    TERM subject(kind="Bob") -> subject_3 : TERM
    TERM subject(kind="Erin") -> subject_4 : TERM
    TERM subject(kind="Gary") -> subject_5 : TERM
    TERM subject(kind="Harry") -> subject_6 : TERM

    TERM subject(kind="green") -> subject_7 : TERM
    TERM subject(kind="rough") -> subject_8 : TERM
    TERM subject(kind="cold") -> subject_9 : TERM
    TERM subject(kind="smart") -> subject_10 : TERM
    TERM subject(kind="white") -> subject_11 : TERM
    TERM subject(kind="quiet") -> subject_12 : TERM
    TERM subject(kind="blue") -> subject_13 : TERM

    # t1:s2 Bob is green.
    CLAIM attribute_claim(property="color", subject=subject_3, value=color_label::green) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM

    # t1:s3 Erin is rough.
    CLAIM attribute_claim(property="texture", subject=subject_4, value="rough") BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM

    # t1:s4 Gary is cold.
    CLAIM attribute_claim(property="temperature", subject=subject_5, value=state_cold) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM

    # t1:s5 Gary is smart.
    CLAIM attribute_claim(property="intelligence", subject=subject_5, value="smart") BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM

    # t1:s6 Harry is green.
    CLAIM attribute_claim(property="color", subject=subject_6, value=color_label::green) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM

    # t1:s7 Harry is smart.
    CLAIM attribute_claim(property="intelligence", subject=subject_6, value="smart") BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM

    # t1:s8 Harry is white.
    CLAIM attribute_claim(property="color", subject=subject_6, value=color_label::white) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM

    # t1:s9 If something is white then it is green.
    TERM conditional(condition=subject_11, consequence=subject_7) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_3 : CLAIM

    # t1:s10 All rough things are quiet.
    TERM conditional(condition=subject_8, consequence=subject_12) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_4 : CLAIM

    # t1:s11 If something is green and smart then it is cold.
    TERM conjunction(items=[subject_7, subject_10]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_9) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_5 : CLAIM

    # t1:s12 All quiet things are blue.
    TERM conditional(condition=subject_12, consequence=subject_13) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_6 : CLAIM

    # t1:s13 All quiet things are white.
    TERM conditional(condition=subject_12, consequence=subject_11) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_7 : CLAIM

    # t1:s14 All white things are rough.
    TERM conditional(condition=subject_11, consequence=subject_8) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_8 : CLAIM

    # t1:s15 Quiet, green things are smart.
    TERM conjunction(items=[subject_12, subject_7]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_10) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_9 : CLAIM

    # t1:s16 Question: Based only on the theory, is the following statement True, False, or Unknown?
    # t1:s17 Bob is quiet.
    CLAIM attribute_claim(property="temperament", subject=subject_3, value="quiet") BY role_user STATUS hypothesized SOURCE "t1:s17" -> attribute_claim_9 : CLAIM
    TERM subject(kind="statement", qualifier=subject_3) -> subject_14 : TERM
    TERM property_question(property="truth_value", subject=subject_14) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement, subject | covered |
| n2 | claim | attribute_claim, color_label::green, statement | covered |
| n3 | object | subject | covered |
| n4 | constraint | color_label::green | label-preserved |
| n5 | claim | attribute_claim, statement | covered |
| n6 | object | subject | covered |
| n7 | constraint | attribute_claim | covered |
| n8 | claim | attribute_claim, state_cold, statement | covered |
| n9 | object | subject | covered |
| n10 | constraint | state_cold | covered |
| n11 | claim | attribute_claim, statement | covered |
| n12 | object | subject | covered |
| n13 | constraint | attribute_claim | covered |
| n14 | claim | attribute_claim, color_label::green, statement | covered |
| n15 | object | subject | covered |
| n16 | constraint | color_label::green | label-preserved |
| n17 | claim | attribute_claim, statement | covered |
| n18 | object | subject | covered |
| n19 | constraint | attribute_claim | covered |
| n20 | claim | attribute_claim, color_label::white, statement | covered |
| n21 | object | subject | covered |
| n22 | constraint | color_label::white | label-preserved |
| n23 | reasoning | conditional, statement, color_label::white, color_label::green | label-preserved |
| n24 | constraint | color_label::white | label-preserved |
| n25 | constraint | color_label::green | label-preserved |
| n26 | reasoning | conditional, statement | covered |
| n27 | constraint | attribute_claim | covered |
| n28 | constraint | state_cold | covered |
| n29 | reasoning | conditional, conjunction, statement, state_cold | covered |
| n30 | constraint | color_label::green | label-preserved |
| n31 | constraint | attribute_claim | covered |
| n32 | constraint | state_cold | covered |
| n33 | reasoning | conditional, statement, color_label::blue | label-preserved |
| n34 | constraint | state_cold | covered |
| n35 | constraint | color_label::blue | label-preserved |
| n36 | reasoning | conditional, statement, color_label::white | covered |
| n37 | constraint | state_cold | covered |
| n38 | constraint | color_label::white | label-preserved |
| n39 | reasoning | conditional, statement, color_label::white | label-preserved |
| n40 | constraint | color_label::white | label-preserved |
| n41 | constraint | attribute_claim | covered |
| n42 | reasoning | conditional, conjunction, statement, color_label::green | covered |
| n43 | constraint | state_cold | covered |
| n44 | constraint | color_label::green | label-preserved |
| n45 | constraint | attribute_claim | covered |
| n46 | speech_act | ask, statement, property_question | covered |
| n47 | constraint | subject | covered |
| n48 | constraint | subject | covered |
| n49 | action | ask, attribute_claim, property_question, statement | covered |
| n50 | object | subject | covered |
| n51 | claim | attribute_claim, statement | covered |
| n52 | constraint | state_cold | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s17 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "green" → color_label::green, t1:s6 "green" → color_label::green, t1:s8 "white" → color_label::white, t1:s9 "white", "green" → color_label::white, color_label::green, t1:s11 "green" → color_label::green, t1:s12 "blue" → color_label::blue, t1:s13 "white" → color_label::white, t1:s14 "white" → color_label::white, t1:s15 "green" → color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
