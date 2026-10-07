Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER inform(topic="theory")
    TERM requirement(property="cold", value=TRUE) -> requirement_2 : TERM
    TERM negation(target=requirement_2) -> negation_2 : TERM
    TERM subject(kind="Dave", qualifier=negation_2) -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM subject(kind="Erin", qualifier=requirement_2) -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM requirement(property="furry", value=TRUE) -> requirement_3 : TERM
    TERM subject(kind="Erin", qualifier=requirement_3) -> subject_4 : TERM
    CLAIM statement(fact=subject_4) BY user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM subject(kind="Fiona", qualifier=requirement_2) -> subject_5 : TERM
    CLAIM statement(fact=subject_5) BY user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM requirement(property="quiet", value=TRUE) -> requirement_4 : TERM
    TERM subject(kind="Fiona", qualifier=requirement_4) -> subject_6 : TERM
    CLAIM statement(fact=subject_6) BY user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM requirement(property="smart", value=TRUE) -> requirement_5 : TERM
    TERM subject(kind="Harry", qualifier=requirement_5) -> subject_7 : TERM
    CLAIM statement(fact=subject_7) BY user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM lexical_label(value=color_label::white) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_6 : TERM
    TERM subject(kind="Harry", qualifier=requirement_6) -> subject_8 : TERM
    CLAIM statement(fact=subject_8) BY user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM conjunction(items=[requirement_5, requirement_2]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_6) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_7 : TERM
    TERM subject(kind="Dave", qualifier=requirement_7) -> subject_9 : TERM
    TERM lexical_label(value=color_label::blue) -> lexical_label_4 : TERM
    TERM requirement(property="color", value=lexical_label_4) -> requirement_8 : TERM
    TERM negation(target=requirement_8) -> negation_3 : TERM
    TERM subject(kind="Dave", qualifier=negation_3) -> subject_10 : TERM
    TERM conditional(condition=subject_9, consequence=subject_10) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM subject(kind="Erin", qualifier=requirement_7) -> subject_11 : TERM
    TERM subject(kind="Erin", qualifier=requirement_5) -> subject_12 : TERM
    TERM conditional(condition=subject_11, consequence=subject_12) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM conjunction(items=[requirement_6, requirement_3]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_5) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM conjunction(items=[subject_5, subject_6]) -> conjunction_4 : TERM
    TERM subject(kind="Fiona", qualifier=requirement_5) -> subject_13 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_13) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM conditional(condition=requirement_3, consequence=requirement_7) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM conjunction(items=[requirement_7, requirement_6]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=requirement_3) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM conjunction(items=[requirement_6, requirement_4]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=requirement_3) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM conjunction(items=[requirement_7, requirement_4]) -> conjunction_7 : TERM
    TERM conditional(condition=conjunction_7, consequence=requirement_8) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM subject(kind="Harry", qualifier=requirement_3) -> subject_14 : TERM
    CLAIM statement(fact=subject_14) BY user STATUS hypothesized SOURCE "t1:s19" -> statement_18 : CLAIM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(target=statement_18, constraints=[constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | inform | covered |
| n2 | claim | statement, subject, negation, requirement | covered |
| n3 | negation | negation | covered |
| n4 | claim | statement, subject, requirement | covered |
| n5 | claim | statement, subject, requirement | covered |
| n6 | claim | statement, subject, requirement | covered |
| n7 | claim | statement, subject, requirement | covered |
| n8 | claim | statement, subject, requirement | covered |
| n9 | claim | statement, subject, requirement, lexical_label | covered |
| n10 | constraint | color_label::white | label-preserved |
| n11 | claim | conditional, conjunction, statement, requirement | covered |
| n12 | constraint | color_label::white | label-preserved |
| n13 | claim | conditional, subject, negation, requirement, lexical_label | covered |
| n14 | negation | negation | covered |
| n15 | constraint | color_label::green | label-preserved |
| n16 | constraint | color_label::blue | label-preserved |
| n17 | claim | conditional, subject, requirement | covered |
| n18 | constraint | color_label::green | label-preserved |
| n19 | claim | conditional, conjunction, statement, requirement | covered |
| n20 | constraint | color_label::white | label-preserved |
| n21 | claim | conditional, conjunction, subject, statement, requirement | covered |
| n22 | claim | conditional, statement, requirement | covered |
| n23 | constraint | color_label::green | label-preserved |
| n24 | claim | conditional, conjunction, statement, requirement | covered |
| n25 | constraint | color_label::green | label-preserved |
| n26 | constraint | color_label::white | label-preserved |
| n27 | claim | conditional, conjunction, statement, requirement | covered |
| n28 | constraint | color_label::white | label-preserved |
| n29 | claim | conditional, conjunction, statement, requirement | covered |
| n30 | constraint | color_label::green | label-preserved |
| n31 | constraint | color_label::blue | label-preserved |
| n32 | speech_act | ask | covered |
| n33 | constraint | ask | covered |
| n34 | constraint | constraint_single_choice | covered |
| n35 | claim | statement, subject, requirement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s8 "white" -> color_label::white, t1:s9 "white" -> color_label::white, t1:s10 "green" -> color_label::green, t1:s10 "blue" -> color_label::blue, t1:s11 "green" -> color_label::green, t1:s12 "white" -> color_label::white, t1:s14 "green" -> color_label::green, t1:s15 "green" -> color_label::green, t1:s15 "white" -> color_label::white, t1:s16 "white" -> color_label::white, t1:s17 "green" -> color_label::green, t1:s17 "blue" -> color_label::blue
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
