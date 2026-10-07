Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # Theory
    TERM activity(actor="bald_eagle", object=animal_label::lion, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM

    TERM activity(actor="bald_eagle", object=animal_label::mouse, verb="chase") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM

    TERM activity(actor="bald_eagle", object=animal_label::lion, verb="visit") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM

    CLAIM attribute_claim(property="rough", subject="lion", value="true") BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_2 : CLAIM

    TERM activity(actor="lion", object=animal_label::eagle, verb="like") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_5 : CLAIM

    TERM activity(actor="lion", object=animal_label::squirrel, verb="like") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_6 : CLAIM

    TERM activity(actor="lion", object=animal_label::mouse, verb="visit") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_7 : CLAIM

    TERM activity(actor="mouse", object=animal_label::lion, verb="chase") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_8 : CLAIM

    TERM activity(actor="mouse", object=animal_label::squirrel, verb="chase") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_9 : CLAIM

    CLAIM attribute_claim(property="rough", subject="mouse", value="true") BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_3 : CLAIM

    CLAIM attribute_claim(property="shape", subject="mouse", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s12" -> attribute_claim_4 : CLAIM

    TERM activity(actor="mouse", object=animal_label::eagle, verb="like") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_10 : CLAIM

    TERM activity(actor="mouse", object=animal_label::eagle, verb="visit") -> activity_11 : TERM
    CLAIM statement(fact=activity_11) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_11 : CLAIM

    TERM activity(actor="squirrel", object=animal_label::lion, verb="chase") -> activity_12 : TERM
    CLAIM statement(fact=activity_12) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_12 : CLAIM

    CLAIM attribute_claim(property="kind", subject="squirrel", value="true") BY role_user STATUS asserted SOURCE "t1:s16" -> attribute_claim_5 : CLAIM

    TERM activity(actor="squirrel", object=animal_label::mouse, verb="like") -> activity_13 : TERM
    CLAIM statement(fact=activity_13) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_13 : CLAIM

    # Rules
    TERM activity(actor="something", object=animal_label::eagle, verb="visit") -> activity_14 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::lion, verb="visit") -> activity_15 : TERM
    TERM conditional(condition=activity_14, consequence=activity_15) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_14 : CLAIM

    TERM character_trait(property="kind", value="true") -> character_trait_2 : TERM
    TERM activity(actor="something", object=animal_label::squirrel, verb="visit") -> activity_16 : TERM
    TERM conditional(condition=character_trait_2, consequence=activity_16) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_15 : CLAIM

    TERM activity(actor="something", object=animal_label::mouse, verb="like") -> activity_17 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="visit") -> activity_18 : TERM
    TERM conditional(condition=activity_17, consequence=activity_18) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_16 : CLAIM

    TERM activity(actor="lion", object=animal_label::squirrel, verb="visit") -> activity_19 : TERM
    TERM conjunction(items=[activity_15, activity_19]) -> conjunction_2 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::squirrel, verb="like") -> activity_20 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_20) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_17 : CLAIM

    TERM activity(actor="something", object=animal_label::lion, verb="like") -> activity_21 : TERM
    TERM conditional(condition=activity_21, consequence=activity_18) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_18 : CLAIM

    TERM conjunction(items=[activity_17, activity_18]) -> conjunction_3 : TERM
    TERM character_trait(property="young", value="true") -> character_trait_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=character_trait_3) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_19 : CLAIM

    TERM conditional(condition=activity_16, consequence=activity_17) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s24" -> statement_20 : CLAIM

    TERM activity(actor="lion", object=animal_label::mouse, verb="chase") -> activity_22 : TERM
    TERM conjunction(items=[activity_18, activity_22]) -> conjunction_4 : TERM
    TERM character_trait(property="young", value="true") -> character_trait_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=character_trait_4) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s25" -> statement_21 : CLAIM

    TERM activity(actor="something", object=animal_label::lion, verb="chase") -> activity_23 : TERM
    TERM conjunction(items=[activity_14, activity_23]) -> conjunction_5 : TERM
    TERM character_trait(property="kind", value="true") -> character_trait_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=character_trait_5) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s26" -> statement_22 : CLAIM

    # Question
    TERM activity(actor="mouse", object=animal_label::lion, verb="visit") -> activity_24 : TERM
    TERM negation(target=activity_24) -> negation_2 : TERM
    TERM property_question(property="truth_value", subject=negation_2) -> property_question_2 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(constraints=[constraint_single_choice_2], target=property_question_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, constraint_single_choice | covered |
| n2 | object | animal_label::eagle | label-preserved |
| n3 | object | animal_label::lion | label-preserved |
| n4 | claim | statement, activity | covered |
| n5 | object | animal_label::mouse | label-preserved |
| n6 | claim | statement, activity | covered |
| n7 | claim | statement, activity | covered |
| n8 | claim | attribute_claim | covered |
| n9 | claim | statement, activity | covered |
| n10 | object | animal_label::squirrel | label-preserved |
| n11 | claim | statement, activity | covered |
| n12 | claim | statement, activity | covered |
| n13 | claim | statement, activity | covered |
| n14 | claim | statement, activity | covered |
| n15 | claim | attribute_claim | covered |
| n16 | claim | attribute_claim, shape_round | covered |
| n17 | claim | statement, activity | covered |
| n18 | claim | statement, activity | covered |
| n19 | claim | statement, activity | covered |
| n20 | claim | attribute_claim, animal_label::squirrel | label-preserved |
| n21 | claim | statement, activity | covered |
| n22 | reasoning | conditional, statement, activity | covered |
| n23 | reasoning | conditional, statement, activity, character_trait, animal_label::squirrel | label-preserved |
| n24 | reasoning | conditional, statement, activity | covered |
| n25 | reasoning | conditional, statement, activity, conjunction | covered |
| n26 | reasoning | conditional, statement, activity | covered |
| n27 | reasoning | conditional, statement, activity, conjunction, character_trait | covered |
| n28 | reasoning | conditional, statement, activity | covered |
| n29 | reasoning | conditional, statement, activity, conjunction, character_trait | covered |
| n30 | reasoning | conditional, statement, activity, conjunction, character_trait, animal_label::lion | label-preserved |
| n31 | speech_act | ask, property_question | covered |
| n32 | constraint | constraint_single_choice | covered |
| n33 | constraint | constraint_single_choice | covered |
| n34 | claim | statement, activity | covered |
| n35 | negation | negation, statement, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s28 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" → animal_label::eagle, t1:s2 "lion" → animal_label::lion, t1:s3 "mouse" → animal_label::mouse, t1:s7 "squirrel" → animal_label::squirrel, t1:s16 "squirrel" → animal_label::squirrel, t1:s19 "squirrel" → animal_label::squirrel, t1:s26 "lion" → animal_label::lion
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
