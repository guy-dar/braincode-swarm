Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # t1:s2 The cow eats the lion.
    TERM activity(actor="cow", object=animal_label::lion, verb="eat") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM

    # t1:s3 The cow is young.
    TERM character_trait(property="age", value="young") -> character_trait_2 : TERM
    CLAIM statement(fact=character_trait_2) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM

    # t1:s4 The cow likes the squirrel.
    TERM activity(actor="cow", object=animal_label::squirrel, verb="like") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM

    # t1:s5 The lion eats the rabbit.
    TERM activity(actor="lion", object=animal_label::rabbit, verb="eat") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM

    # t1:s6 The lion eats the squirrel.
    TERM activity(actor="lion", object=animal_label::squirrel, verb="eat") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM

    # t1:s7 The lion does not like the squirrel.
    TERM activity(actor="lion", object=animal_label::squirrel, verb="like") -> activity_6 : TERM
    TERM negation(target=activity_6) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM

    # t1:s8 The rabbit is blue.
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    CLAIM statement(fact=requirement_2) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM

    # t1:s9 The rabbit likes the cow.
    TERM activity(actor="rabbit", object=animal_label::cow, verb="like") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM

    # t1:s10 The rabbit likes the lion.
    TERM activity(actor="rabbit", object=animal_label::lion, verb="like") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM

    # t1:s11 The squirrel likes the lion.
    TERM activity(actor="squirrel", object=animal_label::lion, verb="like") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM

    # t1:s12 The squirrel likes the rabbit.
    TERM activity(actor="squirrel", object=animal_label::rabbit, verb="like") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM

    # t1:s13 If someone visits the lion then the lion eats the cow.
    TERM activity(actor="someone", object=animal_label::lion, verb="visit") -> activity_11 : TERM
    TERM activity(actor="lion", object=animal_label::cow, verb="eat") -> activity_12 : TERM
    TERM conditional(condition=activity_11, consequence=activity_12) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM

    # t1:s14 If someone visits the cow then they are round.
    TERM activity(actor="someone", object=animal_label::cow, verb="visit") -> activity_13 : TERM
    TERM character_trait(property="shape", value=shape_round) -> character_trait_3 : TERM
    TERM conditional(condition=activity_13, consequence=character_trait_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM

    # t1:s15 If the squirrel visits the cow and the squirrel is not young then the cow likes the rabbit.
    TERM activity(actor="squirrel", object=animal_label::cow, verb="visit") -> activity_14 : TERM
    TERM negation(target=character_trait_2) -> negation_3 : TERM
    TERM conjunction(items=[activity_14, negation_3]) -> conjunction_2 : TERM
    TERM activity(actor="cow", object=animal_label::rabbit, verb="like") -> activity_15 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_15) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM

    # t1:s16 If someone eats the squirrel and they eat the cow then they visit the rabbit.
    TERM activity(actor="someone", object=animal_label::squirrel, verb="eat") -> activity_16 : TERM
    TERM activity(actor="someone", object=animal_label::cow, verb="eat") -> activity_17 : TERM
    TERM conjunction(items=[activity_16, activity_17]) -> conjunction_3 : TERM
    TERM activity(actor="someone", object=animal_label::rabbit, verb="visit") -> activity_18 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_18) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM

    # t1:s17 If someone likes the cow then they are nice.
    TERM activity(actor="someone", object=animal_label::cow, verb="like") -> activity_19 : TERM
    TERM character_trait(property="personality", value="nice") -> character_trait_4 : TERM
    TERM conditional(condition=activity_19, consequence=character_trait_4) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM

    # t1:s18 If someone eats the cow and the cow visits the rabbit then they eat the lion.
    TERM activity(actor="cow", object=animal_label::rabbit, verb="visit") -> activity_20 : TERM
    TERM conjunction(items=[activity_17, activity_20]) -> conjunction_4 : TERM
    TERM activity(actor="someone", object=animal_label::lion, verb="eat") -> activity_21 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_21) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM

    # t1:s19 If someone is nice then they visit the cow.
    TERM conditional(condition=character_trait_4, consequence=activity_13) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_19 : CLAIM

    # t1:s20 If someone eats the squirrel and they like the cow then they do not visit the squirrel.
    TERM conjunction(items=[activity_16, activity_19]) -> conjunction_5 : TERM
    TERM activity(actor="someone", object=animal_label::squirrel, verb="visit") -> activity_22 : TERM
    TERM negation(target=activity_22) -> negation_4 : TERM
    TERM conditional(condition=conjunction_5, consequence=negation_4) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_20 : CLAIM

    # t1:s21 If someone visits the cow then the cow is nice.
    TERM conditional(condition=activity_13, consequence=character_trait_4) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_21 : CLAIM

    # t1:s22 Question: Based only on the theory, is the following statement True, False, or Unknown?
    # t1:s23 The rabbit is round.
    TERM requirement(property="basis", value="theory") -> requirement_3 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(target=character_trait_3, constraints=[requirement_3, constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement, ask | covered |
| n2 | claim | statement, activity | covered |
| n3 | object | animal_label::cow | label-preserved |
| n4 | object | animal_label::lion | label-preserved |
| n5 | action | activity | covered |
| n6 | claim | statement, character_trait | covered |
| n7 | constraint | character_trait | covered |
| n8 | claim | statement, activity | covered |
| n9 | object | animal_label::squirrel | label-preserved |
| n10 | action | activity | covered |
| n11 | claim | statement, activity | covered |
| n12 | object | animal_label::rabbit | label-preserved |
| n13 | claim | statement, activity | covered |
| n14 | claim | statement, negation, activity | covered |
| n15 | negation | negation | covered |
| n16 | claim | statement, requirement, lexical_label | covered |
| n17 | constraint | color_label::blue, lexical_label | label-preserved |
| n18 | claim | statement, activity | covered |
| n19 | claim | statement, activity | covered |
| n20 | claim | statement, activity | covered |
| n21 | claim | statement, activity | covered |
| n22 | reasoning | conditional, activity | covered |
| n23 | action | activity | covered |
| n24 | reasoning | conditional, character_trait, shape_round | covered |
| n25 | constraint | shape_round, character_trait | covered |
| n26 | reasoning | conditional, conjunction, negation, activity | covered |
| n27 | negation | negation | covered |
| n28 | reasoning | conditional, conjunction, activity | covered |
| n29 | reasoning | conditional, character_trait, activity | covered |
| n30 | constraint | character_trait | covered |
| n31 | reasoning | conditional, conjunction, activity | covered |
| n32 | reasoning | conditional, character_trait, activity | covered |
| n33 | reasoning | conditional, conjunction, negation, activity | covered |
| n34 | negation | negation | covered |
| n35 | reasoning | conditional, character_trait, activity | covered |
| n36 | speech_act | ask, statement | covered |
| n37 | constraint | requirement | covered |
| n38 | constraint | constraint_single_choice | covered |
| n39 | claim | character_trait, shape_round, statement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s23 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 animal_label::cow, animal_label::lion (n3, n4); t1:s4 animal_label::squirrel (n8, n9); t1:s5 animal_label::rabbit (n12); t1:s13 animal_label::lion, animal_label::cow (n22); t1:s15 animal_label::squirrel, animal_label::cow, animal_label::rabbit (n26); t1:s19 animal_label::cow (n32); t1:s21 animal_label::cow (n35)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
