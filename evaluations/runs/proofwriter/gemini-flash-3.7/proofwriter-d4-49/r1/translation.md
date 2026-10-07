Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # t1:s1 Theory:
    TERM subject(kind="theory") -> subject_2 : TERM

    # t1:s2 Bob is blue.
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    TERM subject(kind="Bob", qualifier=requirement_2) -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM

    # t1:s3 Bob is not young.
    TERM requirement(property="age", value="young") -> requirement_3 : TERM
    TERM negation(target=requirement_3) -> negation_2 : TERM
    TERM subject(kind="Bob", qualifier=negation_2) -> subject_4 : TERM
    CLAIM statement(fact=subject_4) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM

    # t1:s4 Dave is white.
    TERM lexical_label(value=color_label::white) -> lexical_label_3 : TERM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_4 : TERM
    TERM subject(kind="Dave", qualifier=requirement_4) -> subject_5 : TERM
    CLAIM statement(fact=subject_5) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM

    # t1:s5 Fiona is green.
    TERM lexical_label(value=color_label::green) -> lexical_label_4 : TERM
    TERM requirement(property="color", value=lexical_label_4) -> requirement_5 : TERM
    TERM subject(kind="Fiona", qualifier=requirement_5) -> subject_6 : TERM
    CLAIM statement(fact=subject_6) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM

    # t1:s6 Fiona is rough.
    TERM requirement(property="texture", value="rough") -> requirement_6 : TERM
    TERM subject(kind="Fiona", qualifier=requirement_6) -> subject_7 : TERM
    CLAIM statement(fact=subject_7) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM

    # t1:s7 Fiona is smart.
    TERM requirement(property="intelligence", value="smart") -> requirement_7 : TERM
    TERM subject(kind="Fiona", qualifier=requirement_7) -> subject_8 : TERM
    CLAIM statement(fact=subject_8) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM

    # t1:s8 Gary is blue.
    TERM subject(kind="Gary", qualifier=requirement_2) -> subject_9 : TERM
    CLAIM statement(fact=subject_9) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM

    # t1:s9 If something is nice then it is smart.
    TERM requirement(property="character", value="nice") -> requirement_8 : TERM
    TERM conditional(condition=requirement_8, consequence=requirement_7) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM

    # t1:s10 Blue, smart things are green.
    TERM conjunction(items=[requirement_2, requirement_7]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM

    # t1:s11 All rough things are nice.
    TERM conditional(condition=requirement_6, consequence=requirement_8) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM

    # t1:s12 Blue things are nice.
    TERM conditional(condition=requirement_2, consequence=requirement_8) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM

    # t1:s13 All green, smart things are rough.
    TERM conjunction(items=[requirement_5, requirement_7]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_6) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM

    # t1:s14 Green, smart things are blue.
    TERM conditional(condition=conjunction_3, consequence=requirement_2) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM

    # t1:s15 If something is green and not rough then it is white.
    TERM negation(target=requirement_6) -> negation_3 : TERM
    TERM conjunction(items=[requirement_5, negation_3]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_4) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM

    # t1:s16 Rough, green things are not young.
    TERM conjunction(items=[requirement_6, requirement_5]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=negation_2) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM

    # t1:s17 If something is smart and not white then it is young.
    TERM negation(target=requirement_4) -> negation_4 : TERM
    TERM conjunction(items=[requirement_7, negation_4]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=requirement_3) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM

    # t1:s18 Question: Based only on the theory, is the following statement True, False, or Unknown?
    # t1:s19 Bob is not rough.
    TERM subject(kind="Bob", qualifier=negation_3) -> subject_10 : TERM
    TERM requirement(property="premise_source", value="theory_only") -> requirement_9 : TERM
    TERM requirement(property="response_format", value="truth_value_choice") -> requirement_10 : TERM
    UTTER ask(target=subject_10, constraints=[requirement_9, requirement_10], topic=subject_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject | covered |
| n2 | claim | statement, subject | covered |
| n3 | object | subject | covered |
| n4 | constraint | color_label::blue, lexical_label | label-preserved |
| n5 | claim | statement, subject | covered |
| n6 | negation | negation | covered |
| n7 | claim | statement, subject | covered |
| n8 | object | subject | covered |
| n9 | constraint | color_label::white, lexical_label | label-preserved |
| n10 | claim | statement, subject | covered |
| n11 | object | subject | covered |
| n12 | constraint | color_label::green, lexical_label | label-preserved |
| n13 | claim | statement, subject | covered |
| n14 | claim | statement, subject | covered |
| n15 | claim | statement, subject | covered |
| n16 | object | subject | covered |
| n17 | constraint | color_label::blue, lexical_label | label-preserved |
| n18 | claim | statement, conditional | covered |
| n19 | claim | statement, conditional, conjunction | covered |
| n20 | constraint | color_label::blue, lexical_label | label-preserved |
| n21 | constraint | color_label::green, lexical_label | label-preserved |
| n22 | claim | statement, conditional | covered |
| n23 | claim | statement, conditional | covered |
| n24 | constraint | color_label::blue, lexical_label | label-preserved |
| n25 | claim | statement, conditional, conjunction | covered |
| n26 | constraint | color_label::green, lexical_label | label-preserved |
| n27 | claim | statement, conditional, conjunction | covered |
| n28 | constraint | color_label::green, lexical_label | label-preserved |
| n29 | constraint | color_label::blue, lexical_label | label-preserved |
| n30 | claim | statement, conditional, conjunction | covered |
| n31 | negation | negation | covered |
| n32 | constraint | color_label::green, lexical_label | label-preserved |
| n33 | constraint | color_label::white, lexical_label | label-preserved |
| n34 | claim | statement, conditional, conjunction | covered |
| n35 | negation | negation | covered |
| n36 | constraint | color_label::green, lexical_label | label-preserved |
| n37 | claim | statement, conditional, conjunction | covered |
| n38 | negation | negation | covered |
| n39 | constraint | color_label::white, lexical_label | label-preserved |
| n40 | speech_act | ask | covered |
| n41 | constraint | requirement | covered |
| n42 | constraint | requirement | covered |
| n43 | claim | subject, negation | covered |
| n44 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "blue" -> color_label::blue, t1:s4 "white" -> color_label::white, t1:s5 "green" -> color_label::green, t1:s8 "blue" -> color_label::blue, t1:s10 "blue" -> color_label::blue, t1:s10 "green" -> color_label::green, t1:s12 "blue" -> color_label::blue, t1:s13 "green" -> color_label::green, t1:s14 "green" -> color_label::green, t1:s14 "blue" -> color_label::blue, t1:s15 "green" -> color_label::green, t1:s15 "white" -> color_label::white, t1:s16 "green" -> color_label::green, t1:s17 "white" -> color_label::white
- Missing constructs: none
- Unresolved ambiguities: none
- Check: rag check reported 0 unresolved needs and 0 unknown symbols
