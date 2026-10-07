Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    TERM subject(kind="Bob", qualifier=lexical_label_2) -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM subject(kind="Bob", qualifier="kind") -> subject_4 : TERM
    CLAIM statement(fact=subject_4) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM subject(kind="Charlie", qualifier="nice") -> subject_5 : TERM
    CLAIM statement(fact=subject_5) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM subject(kind="Erin", qualifier="kind") -> subject_6 : TERM
    CLAIM statement(fact=subject_6) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM subject(kind="Erin", qualifier="nice") -> subject_7 : TERM
    CLAIM statement(fact=subject_7) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM lexical_label(value=color_label::white) -> lexical_label_3 : TERM
    TERM subject(kind="Erin", qualifier=lexical_label_3) -> subject_8 : TERM
    CLAIM statement(fact=subject_8) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM subject(kind="Gary", qualifier="young") -> subject_9 : TERM
    CLAIM statement(fact=subject_9) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM subject(kind="thing", qualifier="young") -> subject_10 : TERM
    TERM subject(kind="thing", qualifier=lexical_label_3) -> subject_11 : TERM
    TERM conditional(condition=subject_10, consequence=subject_11) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM conditional(condition=subject_11, consequence=subject_10) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM subject(kind="thing", qualifier="nice") -> subject_12 : TERM
    TERM subject(kind="thing", qualifier=lexical_label_2) -> subject_13 : TERM
    TERM conjunction(items=[subject_12, subject_13]) -> conjunction_2 : TERM
    TERM subject(kind="thing", qualifier="kind") -> subject_14 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_14) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM subject(kind="thing", qualifier="furry") -> subject_15 : TERM
    TERM conditional(condition=subject_10, consequence=subject_15) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM conditional(condition=subject_14, consequence=subject_12) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM conditional(condition=conjunction_2, consequence=subject_11) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM subject(kind="thing", qualifier=state_cold) -> subject_16 : TERM
    TERM conjunction(items=[subject_16, subject_14]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_13) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM conjunction(items=[subject_12, subject_10]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_15) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM conditional(condition=subject_15, consequence=subject_16) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM subject(kind="Charlie", qualifier="young") -> subject_17 : TERM
    TERM negation(target=subject_17) -> negation_2 : TERM
    UTTER ask(target=negation_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject | covered |
| n2 | claim | statement | covered |
| n3 | object | subject | covered |
| n4 | constraint | color_label::green | label-preserved |
| n5 | claim | statement | covered |
| n6 | object | subject | covered |
| n7 | claim | statement | covered |
| n8 | object | subject | covered |
| n9 | claim | statement | covered |
| n10 | object | subject | covered |
| n11 | claim | statement | covered |
| n12 | object | subject | covered |
| n13 | claim | statement | covered |
| n14 | object | subject | covered |
| n15 | constraint | color_label::white | label-preserved |
| n16 | claim | statement | covered |
| n17 | object | subject | covered |
| n18 | claim | statement | covered |
| n19 | constraint | color_label::white | label-preserved |
| n20 | claim | statement | covered |
| n21 | constraint | color_label::white | label-preserved |
| n22 | claim | color_label::green, statement | label-preserved |
| n23 | constraint | color_label::green | label-preserved |
| n24 | claim | statement | covered |
| n25 | claim | statement | covered |
| n26 | claim | color_label::green, color_label::white, statement | label-preserved |
| n27 | constraint | color_label::green | label-preserved |
| n28 | constraint | color_label::white | label-preserved |
| n29 | claim | state_cold, color_label::green, statement | label-preserved |
| n30 | constraint | color_label::green | label-preserved |
| n31 | claim | statement | covered |
| n32 | claim | state_cold, statement | covered |
| n33 | speech_act | ask | covered |
| n34 | constraint | subject | covered |
| n35 | constraint | ask | covered |
| n36 | claim | negation | covered |
| n37 | object | subject | covered |
| n38 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2, t1:s11, t1:s14, t1:s15 "green" → color_label::green; t1:s7, t1:s9, t1:s10, t1:s14 "white" → color_label::white
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
