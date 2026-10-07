Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER inform(topic="theory")
    CLAIM attribute_claim(property="age", subject="bald_eagle", value="young") BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::bear, verb="like") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_2 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="bear", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="color", subject="cat", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_4 : CLAIM
    TERM activity(actor="cat", object=animal_label::eagle, verb="like") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_3 : CLAIM
    TERM activity(actor="cat", object=animal_label::cow, verb="see") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_4 : CLAIM
    TERM activity(actor="cat", object=animal_label::eagle, verb="visit") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_5 : CLAIM
    CLAIM attribute_claim(property="color", subject="cow", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s9" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="temperament", subject="cow", value="nice") BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="shape", subject="cow", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_7 : CLAIM
    TERM activity(actor="cow", object=animal_label::bear, verb="like") -> activity_6 : TERM
    TERM negation(target=activity_6) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_6 : CLAIM
    TERM activity(actor="cow", object=animal_label::bear, verb="see") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_7 : CLAIM
    TERM activity(object=animal_label::eagle, verb="see") -> activity_8 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::cow, verb="see") -> activity_9 : TERM
    TERM conditional(condition=activity_8, consequence=activity_9) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_8 : CLAIM
    TERM activity(object=animal_label::cow, verb="see") -> activity_10 : TERM
    TERM activity(object=animal_label::cat, verb="see") -> activity_11 : TERM
    TERM conditional(condition=activity_10, consequence=activity_11) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_9 : CLAIM
    TERM activity(object=animal_label::cow, verb="like") -> activity_12 : TERM
    TERM conditional(condition=activity_11, consequence=activity_12) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_10 : CLAIM
    TERM activity(actor="cat", object=animal_label::eagle, verb="see") -> activity_13 : TERM
    TERM conditional(condition=activity_11, consequence=activity_13) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_11 : CLAIM
    TERM character_trait(property="shape", value=shape_round) -> character_trait_2 : TERM
    TERM conjunction(items=[activity_12, character_trait_2]) -> conjunction_2 : TERM
    TERM activity(actor="cow", object=animal_label::eagle, verb="see") -> activity_14 : TERM
    TERM negation(target=activity_14) -> negation_3 : TERM
    TERM conditional(condition=conjunction_2, consequence=negation_3) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_12 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::cat, verb="see") -> activity_15 : TERM
    TERM requirement(property="basis", value="theory") -> requirement_2 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(target=activity_15, constraints=[requirement_2, constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | inform | covered |
| n2 | object | animal_label::eagle | label-preserved |
| n3 | claim | attribute_claim | covered |
| n4 | object | animal_label::eagle | label-preserved |
| n5 | object | animal_label::bear | label-preserved |
| n6 | claim | activity, statement | covered |
| n7 | object | animal_label::bear | label-preserved |
| n8 | constraint | color_label::blue, lexical_label | label-preserved |
| n9 | claim | attribute_claim | covered |
| n10 | object | animal_label::cat | label-preserved |
| n11 | constraint | color_label::blue, lexical_label | label-preserved |
| n12 | claim | attribute_claim | covered |
| n13 | object | animal_label::cat | label-preserved |
| n14 | object | animal_label::eagle | label-preserved |
| n15 | claim | activity, statement | covered |
| n16 | object | animal_label::cat | label-preserved |
| n17 | object | animal_label::cow | label-preserved |
| n18 | claim | activity, statement | covered |
| n19 | object | animal_label::cat | label-preserved |
| n20 | object | animal_label::eagle | label-preserved |
| n21 | claim | activity, statement | covered |
| n22 | object | animal_label::cow | label-preserved |
| n23 | constraint | color_label::blue, lexical_label | label-preserved |
| n24 | claim | attribute_claim | covered |
| n25 | object | animal_label::cow | label-preserved |
| n26 | claim | attribute_claim | covered |
| n27 | object | animal_label::cow | label-preserved |
| n28 | claim | attribute_claim, shape_round | covered |
| n29 | object | animal_label::cow | label-preserved |
| n30 | object | animal_label::bear | label-preserved |
| n31 | negation | negation | covered |
| n32 | claim | activity, negation, statement | covered |
| n33 | object | animal_label::cow | label-preserved |
| n34 | object | animal_label::bear | label-preserved |
| n35 | claim | activity, statement | covered |
| n36 | reasoning | activity, conditional, statement | covered |
| n37 | reasoning | activity, conditional, statement | covered |
| n38 | reasoning | activity, conditional, statement | covered |
| n39 | reasoning | activity, conditional, statement | covered |
| n40 | reasoning | character_trait, conditional, conjunction, negation, shape_round, statement | covered |
| n41 | negation | negation | covered |
| n42 | speech_act | ask | covered |
| n43 | constraint | requirement | covered |
| n44 | constraint | constraint_single_choice | covered |
| n45 | object | animal_label::eagle | label-preserved |
| n46 | object | animal_label::cat | label-preserved |
| n47 | claim | activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s20 is represented.
- Opaque-text spans: none
- Label-preserved spans: t1:s2, t1:s3, t1:s6, t1:s8, t1:s14, t1:s17, t1:s18, t1:s20 "bald eagle" → animal_label::eagle; t1:s3, t1:s4, t1:s12, t1:s13 "bear" → animal_label::bear; t1:s5, t1:s6, t1:s7, t1:s8, t1:s15, t1:s16, t1:s17, t1:s20 "cat" → animal_label::cat; t1:s7, t1:s9, t1:s10, t1:s11, t1:s12, t1:s13, t1:s14, t1:s15, t1:s16, t1:s18 "cow" → animal_label::cow; t1:s4, t1:s5, t1:s9 "blue" → color_label::blue
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
