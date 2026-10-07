Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="bear", object=animal_label::cat, verb="eat") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM requirement(property="nice", value=TRUE) -> requirement_2 : TERM
    CLAIM statement(fact=requirement_2) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM requirement(property="rough", value=TRUE) -> requirement_3 : TERM
    CLAIM statement(fact=requirement_3) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM activity(actor="bear", object=animal_label::cat, verb="like") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM activity(actor="bear", object=animal_label::dog, verb="visit") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM activity(actor="cat", object=animal_label::bear, verb="visit") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM activity(actor="dog", object=animal_label::cat, verb="eat") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    CLAIM has_attribute(attribute=lexical_label_2, subject="dog") BY role_user STATUS asserted SOURCE "t1:s9" -> has_attribute_2 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    CLAIM has_attribute(attribute=lexical_label_3, subject="dog") BY role_user STATUS asserted SOURCE "t1:s10" -> has_attribute_3 : CLAIM
    TERM activity(actor="mouse", object=animal_label::bear, verb="eat") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_9 : CLAIM
    TERM activity(actor="mouse", object=animal_label::bear, verb="visit") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_10 : CLAIM
    TERM activity(actor="someone", object=animal_label::cat, verb="eat") -> activity_9 : TERM
    TERM activity(actor="someone", object=animal_label::cat, verb="visit") -> activity_10 : TERM
    TERM conditional(condition=activity_9, consequence=activity_10) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_11 : CLAIM
    TERM activity(actor="someone", object=animal_label::mouse, verb="eat") -> activity_11 : TERM
    TERM conditional(condition=activity_9, consequence=activity_11) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_12 : CLAIM
    TERM activity(actor="someone", object=animal_label::dog, verb="visit") -> activity_12 : TERM
    TERM activity(actor="dog", object=animal_label::cat, verb="like") -> activity_13 : TERM
    TERM conjunction(items=[activity_12, activity_13]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_2) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_13 : CLAIM
    TERM activity(actor="someone", object=animal_label::mouse, verb="like") -> activity_14 : TERM
    TERM conditional(condition=activity_14, consequence=activity_9) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_14 : CLAIM
    TERM activity(actor="dog", object=animal_label::mouse, verb="visit") -> activity_15 : TERM
    TERM conditional(condition=requirement_2, consequence=activity_15) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_15 : CLAIM
    TERM conjunction(items=[activity_11, activity_7]) -> conjunction_3 : TERM
    TERM activity(actor="someone", object=animal_label::cat, verb="like") -> activity_16 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_16) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_16 : CLAIM
    TERM activity(actor="bear", object=animal_label::dog, verb="like") -> activity_17 : TERM
    TERM activity(actor="dog", object=animal_label::bear, verb="visit") -> activity_18 : TERM
    TERM conditional(condition=activity_17, consequence=activity_18) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_17 : CLAIM
    TERM conditional(condition=requirement_3, consequence=activity_10) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_18 : CLAIM
    TERM activity(actor="dog", object=animal_label::cat, verb="visit") -> activity_19 : TERM
    TERM conjunction(items=[activity_15, activity_19]) -> conjunction_4 : TERM
    TERM activity(actor="mouse", object=animal_label::dog, verb="eat") -> activity_20 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_20) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_19 : CLAIM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM activity(actor="mouse", object=animal_label::cat, verb="like") -> activity_21 : TERM
    UTTER ask(target=activity_21, constraints=[constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | object | animal_label::bear | label-preserved |
| n3 | object | animal_label::cat | label-preserved |
| n4 | claim | statement, activity | covered |
| n5 | claim | statement, requirement | covered |
| n6 | claim | statement, requirement | covered |
| n7 | claim | statement, activity | covered |
| n8 | object | animal_label::dog | label-preserved |
| n9 | claim | statement, activity | covered |
| n10 | claim | statement, activity | covered |
| n11 | claim | statement, activity | covered |
| n12 | constraint | color_label::blue | label-preserved |
| n13 | claim | has_attribute, lexical_label | covered |
| n14 | constraint | color_label::green | label-preserved |
| n15 | claim | has_attribute, lexical_label | covered |
| n16 | object | animal_label::mouse | label-preserved |
| n17 | claim | statement, activity | covered |
| n18 | claim | statement, activity | covered |
| n19 | reasoning | conditional, statement, activity | covered |
| n20 | reasoning | conditional, statement, activity | covered |
| n21 | reasoning | conditional, conjunction, statement, requirement, activity | covered |
| n22 | reasoning | conditional, statement, activity | covered |
| n23 | reasoning | conditional, statement, requirement, activity | covered |
| n24 | reasoning | conditional, conjunction, statement, activity | covered |
| n25 | reasoning | conditional, statement, activity | covered |
| n26 | reasoning | conditional, statement, requirement, activity | covered |
| n27 | reasoning | conditional, conjunction, statement, activity | covered |
| n28 | speech_act | ask | covered |
| n29 | constraint | ask | covered |
| n30 | constraint | constraint_single_choice, requirement | covered |
| n31 | claim | activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s23 is represented.
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bear" -> animal_label::bear, t1:s2 "cat" -> animal_label::cat, t1:s6 "dog" -> animal_label::dog, t1:s9 "blue" -> color_label::blue, t1:s10 "green" -> color_label::green, t1:s11 "mouse" -> animal_label::mouse
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
