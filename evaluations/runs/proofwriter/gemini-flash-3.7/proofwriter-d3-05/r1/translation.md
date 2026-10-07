Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    TERM activity(actor="dog", object=animal_label::lion, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="dog", object=animal_label::tiger, verb="chase") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM requirement(property="size", value="big") -> requirement_2 : TERM
    CLAIM statement(fact=requirement_2) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM activity(actor="dog", object=animal_label::tiger, verb="like") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM activity(actor="dog", object=animal_label::lion, verb="see") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM requirement(property="kind", value=TRUE) -> requirement_3 : TERM
    CLAIM statement(fact=requirement_3) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM activity(actor="lion", object=animal_label::mouse, verb="see") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM activity(actor="mouse", object=animal_label::dog, verb="chase") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM activity(actor="mouse", object=animal_label::lion, verb="chase") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM activity(actor="mouse", object=animal_label::tiger, verb="like") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM activity(actor="tiger", object=animal_label::mouse, verb="like") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM requirement(property="kind", value=TRUE) -> requirement_4 : TERM
    TERM activity(actor="someone", object=animal_label::mouse, verb="chase") -> activity_11 : TERM
    TERM conditional(condition=requirement_4, consequence=activity_11) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM requirement(property="shape", value=shape_round) -> requirement_5 : TERM
    TERM activity(actor="someone", object=animal_label::dog, verb="like") -> activity_12 : TERM
    TERM conditional(condition=requirement_5, consequence=activity_12) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_6 : TERM
    TERM activity(actor="someone", object=animal_label::tiger, verb="chase") -> activity_13 : TERM
    TERM conditional(condition=requirement_6, consequence=activity_13) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM activity(actor="someone", object=animal_label::dog, verb="chase") -> activity_14 : TERM
    TERM activity(actor="someone", object=animal_label::mouse, verb="see") -> activity_15 : TERM
    TERM conjunction(items=[activity_14, activity_15]) -> conjunction_2 : TERM
    TERM requirement(property="kind", value=TRUE) -> requirement_7 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_7) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM activity(actor="someone", object=animal_label::dog, verb="chase") -> activity_16 : TERM
    TERM activity(actor="dog", object=animal_label::lion, verb="chase") -> activity_17 : TERM
    TERM conditional(condition=activity_16, consequence=activity_17) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM activity(actor="someone", object=animal_label::mouse, verb="see") -> activity_18 : TERM
    TERM activity(actor="someone", object=animal_label::mouse, verb="chase") -> activity_19 : TERM
    TERM conjunction(items=[activity_18, activity_19]) -> conjunction_3 : TERM
    TERM requirement(property="shape", value=shape_round) -> requirement_8 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_8) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM
    TERM requirement(property="age", value="young") -> requirement_9 : TERM
    TERM activity(actor="someone", object=animal_label::tiger, verb="like") -> activity_20 : TERM
    TERM conjunction(items=[requirement_9, activity_20]) -> conjunction_4 : TERM
    TERM activity(actor="someone", object=animal_label::dog, verb="chase") -> activity_21 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_21) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_19 : CLAIM
    TERM activity(actor="someone", object=animal_label::mouse, verb="chase") -> activity_22 : TERM
    TERM requirement(property="kind", value=TRUE) -> requirement_10 : TERM
    TERM conditional(condition=activity_22, consequence=requirement_10) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_20 : CLAIM
    TERM activity(actor="lion", object=animal_label::dog, verb="like") -> activity_23 : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_11 : TERM
    TERM conditional(condition=activity_23, consequence=requirement_11) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_21 : CLAIM
    TERM activity(actor="lion", object=animal_label::dog, verb="like") -> activity_24 : TERM
    TERM property_question(property="truth_value", subject=activity_24) -> property_question_2 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(target=property_question_2, constraints=[constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject | covered |
| n2 | claim | statement, activity, animal_label::lion | covered |
| n3 | object | animal_label::dog | label-preserved |
| n4 | object | animal_label::lion | label-preserved |
| n5 | claim | statement, activity, animal_label::tiger | covered |
| n6 | object | animal_label::tiger | label-preserved |
| n7 | claim | statement, requirement | covered |
| n8 | claim | statement, activity, animal_label::tiger | covered |
| n9 | claim | statement, activity, animal_label::lion | covered |
| n10 | claim | statement, requirement | covered |
| n11 | claim | statement, activity, animal_label::mouse | covered |
| n12 | object | animal_label::mouse | label-preserved |
| n13 | claim | statement, activity, animal_label::dog | covered |
| n14 | claim | statement, activity, animal_label::lion | covered |
| n15 | claim | statement, activity, animal_label::tiger | covered |
| n16 | claim | statement, activity, animal_label::mouse | covered |
| n17 | reasoning | statement, conditional, activity, requirement, animal_label::mouse | covered |
| n18 | reasoning | statement, conditional, shape_round, activity, requirement, animal_label::dog | covered |
| n19 | reasoning | statement, conditional, lexical_label, color_label::green, activity, requirement, animal_label::tiger | covered |
| n20 | constraint | color_label::green | label-preserved |
| n21 | reasoning | statement, conditional, conjunction, activity, requirement, animal_label::dog, animal_label::mouse | covered |
| n22 | reasoning | statement, conditional, activity, animal_label::dog, animal_label::lion | covered |
| n23 | reasoning | statement, conditional, conjunction, shape_round, activity, requirement, animal_label::mouse | covered |
| n24 | reasoning | statement, conditional, conjunction, activity, requirement, animal_label::tiger, animal_label::dog | covered |
| n25 | reasoning | statement, conditional, activity, requirement, animal_label::mouse | label-preserved |
| n26 | reasoning | statement, conditional, lexical_label, color_label::green, activity, requirement, animal_label::dog | covered |
| n27 | action | property_question, ask | covered |
| n28 | constraint | subject | covered |
| n29 | constraint | constraint_single_choice | covered |
| n30 | object | activity, animal_label::dog | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s23 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "dog" -> animal_label::dog; t1:s2 "lion" -> animal_label::lion; t1:s3 "tiger" -> animal_label::tiger; t1:s8 "mouse" -> animal_label::mouse; t1:s15 "green" -> color_label::green; t1:s20 "mouse" -> animal_label::mouse
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
