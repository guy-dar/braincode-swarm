Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="bear", object=animal_label::dog, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    UTTER inform(target=statement_2)
    TERM subject(kind="bear", qualifier="young") -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM activity(actor="dog", object=animal_label::tiger, verb="chase") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM activity(actor="dog", object=animal_label::bear, verb="like") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM activity(actor="dog", object=animal_label::lion, verb="like") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM activity(actor="dog", object=animal_label::tiger, verb="like") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM activity(actor="lion", object=animal_label::tiger, verb="chase") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM activity(actor="lion", object=animal_label::bear, verb="eat") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM activity(actor="lion", object=animal_label::bear, verb="like") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM activity(actor="lion", object=animal_label::dog, verb="like") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM activity(actor="tiger", object=animal_label::lion, verb="eat") -> activity_11 : TERM
    CLAIM statement(fact=activity_11) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM subject(kind="tiger") -> subject_3 : TERM
    CLAIM has_state(state=state_cold, subject=subject_3) BY role_user STATUS asserted SOURCE "t1:s13" -> has_state_2 : CLAIM
    TERM subject(kind="tiger", qualifier="young") -> subject_4 : TERM
    CLAIM statement(fact=subject_4) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_13 : CLAIM
    TERM activity(actor="tiger", object=animal_label::bear, verb="like") -> activity_12 : TERM
    CLAIM statement(fact=activity_12) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_14 : CLAIM
    TERM activity(actor="something", object=animal_label::lion, verb="like") -> activity_13 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="chase") -> activity_14 : TERM
    TERM conditional(condition=activity_13, consequence=activity_14) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_15 : CLAIM
    TERM activity(actor="something", object=animal_label::dog, verb="chase") -> activity_15 : TERM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    TERM subject(kind="something", qualifier=lexical_label_2) -> subject_5 : TERM
    TERM conjunction(items=[activity_15, subject_5]) -> conjunction_2 : TERM
    TERM subject(kind="dog", qualifier=state_cold) -> subject_6 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_6) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_16 : CLAIM
    TERM activity(actor="something", object=animal_label::tiger, verb="like") -> activity_16 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="like") -> activity_17 : TERM
    TERM conditional(condition=activity_16, consequence=activity_17) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_17 : CLAIM
    TERM activity(actor="something", object=animal_label::bear, verb="chase") -> activity_18 : TERM
    TERM subject(kind="bear", qualifier=shape_round) -> subject_7 : TERM
    TERM conjunction(items=[activity_18, subject_7]) -> conjunction_3 : TERM
    TERM activity(actor="bear", object=animal_label::lion, verb="chase") -> activity_19 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_19) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_18 : CLAIM
    TERM activity(actor="something", object=animal_label::lion, verb="chase") -> activity_20 : TERM
    TERM conditional(condition=activity_20, consequence=subject_5) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_19 : CLAIM
    TERM activity(actor="something", object=animal_label::dog, verb="eat") -> activity_21 : TERM
    TERM activity(actor="dog", object=animal_label::lion, verb="chase") -> activity_22 : TERM
    TERM conditional(condition=activity_21, consequence=activity_22) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_20 : CLAIM
    TERM subject(kind="something", qualifier=shape_round) -> subject_8 : TERM
    TERM activity(actor="something", object=animal_label::tiger, verb="like") -> activity_23 : TERM
    TERM conditional(condition=subject_8, consequence=activity_23) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_21 : CLAIM
    TERM subject(kind="thing", qualifier="young") -> subject_9 : TERM
    TERM subject(kind="thing", qualifier=shape_round) -> subject_10 : TERM
    TERM conditional(condition=subject_9, consequence=subject_10) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_22 : CLAIM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM activity(actor="tiger", object=animal_label::lion, verb="chase") -> activity_24 : TERM
    TERM negation(target=activity_24) -> negation_2 : TERM
    UTTER ask(target=negation_2, constraints=[constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | inform | covered |
| n2 | claim | statement, activity | covered |
| n3 | object | animal_label::bear | label-preserved |
| n4 | object | animal_label::dog | label-preserved |
| n5 | claim | statement, subject | covered |
| n6 | claim | statement, activity | covered |
| n7 | object | animal_label::tiger | label-preserved |
| n8 | claim | statement, activity | covered |
| n9 | claim | statement, activity | covered |
| n10 | object | animal_label::lion | label-preserved |
| n11 | claim | statement, activity | covered |
| n12 | claim | statement, activity | covered |
| n13 | claim | statement, activity | covered |
| n14 | claim | statement, activity | covered |
| n15 | claim | statement, activity | covered |
| n16 | claim | statement, activity | covered |
| n17 | claim | has_state, state_cold | covered |
| n18 | claim | statement, subject | covered |
| n19 | claim | statement, activity | covered |
| n20 | reasoning | conditional, statement, activity | covered |
| n21 | reasoning | conditional, conjunction, statement, activity, state_cold, lexical_label, color_label::red | covered |
| n22 | constraint | color_label::red | label-preserved |
| n23 | reasoning | conditional, statement, activity | covered |
| n24 | reasoning | conditional, conjunction, statement, activity, shape_round | covered |
| n25 | reasoning | conditional, statement, activity | covered |
| n26 | reasoning | conditional, statement, activity | covered |
| n27 | reasoning | conditional, statement, activity, shape_round | covered |
| n28 | reasoning | conditional, statement, shape_round, subject | covered |
| n29 | action | ask, statement | covered |
| n30 | constraint | ask | covered |
| n31 | constraint | constraint_single_choice | covered |
| n32 | claim | activity, statement | covered |
| n33 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s25 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bear" -> animal_label::bear, t1:s2 "dog" -> animal_label::dog, t1:s4 "tiger" -> animal_label::tiger, t1:s6 "lion" -> animal_label::lion, t1:s17 "red" -> color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: rag check reported 0 unresolved needs and 0 unknown symbols
