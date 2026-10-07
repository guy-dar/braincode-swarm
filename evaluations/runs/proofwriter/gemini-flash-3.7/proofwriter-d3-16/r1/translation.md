Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # t1:s2 The bear chases the lion.
    TERM activity(actor="bear", object=animal_label::lion, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM

    # t1:s3 The bear chases the squirrel.
    TERM activity(actor="bear", object=animal_label::squirrel, verb="chase") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM

    # t1:s4 The bear is cold.
    TERM lexical_label(value=animal_label::bear) -> lexical_label_2 : TERM
    CLAIM has_state(state=state_cold, subject=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s4" -> has_state_2 : CLAIM

    # t1:s5 The bear needs the lion.
    TERM activity(actor="bear", object=animal_label::lion, verb="need") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_4 : CLAIM

    # t1:s6 The bear needs the squirrel.
    TERM activity(actor="bear", object=animal_label::squirrel, verb="need") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_5 : CLAIM

    # t1:s7 The lion chases the bear.
    TERM activity(actor="lion", object=animal_label::bear, verb="chase") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_6 : CLAIM

    # t1:s8 The lion is cold.
    TERM lexical_label(value=animal_label::lion) -> lexical_label_3 : TERM
    CLAIM has_state(state=state_cold, subject=lexical_label_3) BY role_user STATUS asserted SOURCE "t1:s8" -> has_state_3 : CLAIM

    # t1:s9 The lion needs the bear.
    TERM activity(actor="lion", object=animal_label::bear, verb="need") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_7 : CLAIM

    # t1:s10 The lion does not see the rabbit.
    TERM activity(actor="lion", object=animal_label::rabbit, verb="see") -> activity_8 : TERM
    TERM negation(target=activity_8) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_8 : CLAIM

    # t1:s11 The lion does not see the squirrel.
    TERM activity(actor="lion", object=animal_label::squirrel, verb="see") -> activity_9 : TERM
    TERM negation(target=activity_9) -> negation_3 : TERM
    CLAIM statement(fact=negation_3) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_9 : CLAIM

    # t1:s12 The rabbit needs the lion.
    TERM activity(actor="rabbit", object=animal_label::lion, verb="need") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_10 : CLAIM

    # t1:s13 The squirrel is not big.
    TERM activity(actor="squirrel", verb="big") -> activity_11 : TERM
    TERM negation(target=activity_11) -> negation_4 : TERM
    CLAIM statement(fact=negation_4) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_11 : CLAIM

    # t1:s14 If something needs the rabbit then the rabbit is red.
    TERM lexical_label(value=color_label::red) -> lexical_label_4 : TERM
    TERM activity(actor="something", object=animal_label::rabbit, verb="need") -> activity_12 : TERM
    TERM subject(kind="rabbit", qualifier=lexical_label_4) -> subject_2 : TERM
    TERM conditional(condition=activity_12, consequence=subject_2) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_12 : CLAIM

    # t1:s15 If something sees the rabbit and it does not see the bear then the rabbit is not red.
    TERM activity(actor="something", object=animal_label::rabbit, verb="see") -> activity_13 : TERM
    TERM activity(actor="something", object=animal_label::bear, verb="see") -> activity_14 : TERM
    TERM negation(target=activity_14) -> negation_5 : TERM
    TERM conjunction(items=[activity_13, negation_5]) -> conjunction_2 : TERM
    TERM negation(target=subject_2) -> negation_6 : TERM
    TERM conditional(condition=conjunction_2, consequence=negation_6) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_13 : CLAIM

    # t1:s16 If something is red then it is green.
    TERM lexical_label(value=color_label::green) -> lexical_label_5 : TERM
    TERM subject(kind="something", qualifier=lexical_label_4) -> subject_3 : TERM
    TERM subject(kind="something", qualifier=lexical_label_5) -> subject_4 : TERM
    TERM conditional(condition=subject_3, consequence=subject_4) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_14 : CLAIM

    # t1:s17 If something sees the rabbit and the rabbit is green then it needs the squirrel.
    TERM subject(kind="rabbit", qualifier=lexical_label_5) -> subject_5 : TERM
    TERM conjunction(items=[activity_13, subject_5]) -> conjunction_3 : TERM
    TERM activity(actor="something", object=animal_label::squirrel, verb="need") -> activity_15 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_15) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_15 : CLAIM

    # t1:s18 If something is green then it chases the bear.
    TERM activity(actor="something", object=animal_label::bear, verb="chase") -> activity_16 : TERM
    TERM conditional(condition=subject_4, consequence=activity_16) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_16 : CLAIM

    # t1:s19 If something sees the bear then it does not see the rabbit.
    TERM negation(target=activity_13) -> negation_7 : TERM
    TERM conditional(condition=activity_14, consequence=negation_7) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_17 : CLAIM

    # t1:s20 All red, big things are kind.
    TERM subject(kind="something", qualifier="big") -> subject_6 : TERM
    TERM conjunction(items=[subject_3, subject_6]) -> conjunction_4 : TERM
    TERM subject(kind="something", qualifier="kind") -> subject_7 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_7) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_18 : CLAIM

    # t1:s21 If something is big and it chases the lion then it sees the lion.
    TERM activity(actor="something", object=animal_label::lion, verb="chase") -> activity_17 : TERM
    TERM conjunction(items=[subject_6, activity_17]) -> conjunction_5 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="see") -> activity_18 : TERM
    TERM conditional(condition=conjunction_5, consequence=activity_18) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_19 : CLAIM

    # t1:s22 If something chases the bear then it needs the rabbit.
    TERM conditional(condition=activity_16, consequence=activity_12) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_20 : CLAIM

    # t1:s23 Question: Based only on the theory, is the following statement True, False, or Unknown?
    # t1:s24 The rabbit is not green.
    TERM negation(target=subject_5) -> negation_8 : TERM
    TERM requirement(property="basis", value="theory") -> requirement_2 : TERM
    TERM requirement(property="choice_domain", value="true_false_unknown") -> requirement_3 : TERM
    UTTER ask(target=negation_8, constraints=[requirement_2, requirement_3])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | object | animal_label::bear | label-preserved |
| n3 | object | animal_label::lion | label-preserved |
| n4 | action | activity | covered |
| n5 | claim | statement | covered |
| n6 | object | animal_label::squirrel | label-preserved |
| n7 | claim | statement | covered |
| n8 | claim | has_state, state_cold | covered |
| n9 | action | activity | covered |
| n10 | claim | statement | covered |
| n11 | claim | statement | covered |
| n12 | claim | statement | covered |
| n13 | claim | has_state, state_cold | covered |
| n14 | claim | statement | covered |
| n15 | object | animal_label::rabbit | label-preserved |
| n16 | action | activity | covered |
| n17 | negation | negation | covered |
| n18 | claim | statement | covered |
| n19 | claim | statement | covered |
| n20 | claim | statement | covered |
| n21 | negation | negation | covered |
| n22 | claim | statement | covered |
| n23 | object | color_label::red | label-preserved |
| n24 | reasoning | conditional | covered |
| n25 | negation | negation | covered |
| n26 | negation | negation | covered |
| n27 | reasoning | conditional | covered |
| n28 | object | color_label::green | label-preserved |
| n29 | reasoning | conditional, color_label::green, color_label::red | label-preserved |
| n30 | reasoning | conditional | covered |
| n31 | reasoning | conditional | covered |
| n32 | negation | negation | covered |
| n33 | reasoning | conditional | covered |
| n34 | reasoning | conditional | covered |
| n35 | reasoning | conditional | covered |
| n36 | reasoning | conditional | covered |
| n37 | speech_act | ask | covered |
| n38 | constraint | requirement | covered |
| n39 | constraint | requirement | covered |
| n40 | negation | negation | covered |
| n41 | claim | statement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bear" → animal_label::bear, t1:s2 "lion" → animal_label::lion, t1:s3 "squirrel" → animal_label::squirrel, t1:s10 "rabbit" → animal_label::rabbit, t1:s14 "red" → color_label::red, t1:s16 "green" → color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
