Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM character_trait(property="age", value="young") -> character_trait_2 : TERM
    CLAIM attribute_claim(property="age", subject="bald_eagle", value="young") BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM statement(fact=character_trait_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::bear, verb="see") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::bear, verb="visit") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM activity(actor="bear", object=animal_label::squirrel, verb="eat") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    TERM character_trait(property="color", value="blue") -> character_trait_3 : TERM
    TERM negation(target=character_trait_3) -> negation_2 : TERM
    CLAIM attribute_claim(property="color", subject="bear", value="not_blue") BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_3 : CLAIM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    TERM character_trait(property="color", value="green") -> character_trait_4 : TERM
    CLAIM attribute_claim(property="color", subject="bear", value="green") BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_4 : CLAIM
    CLAIM statement(fact=character_trait_4) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM activity(actor="bear", object=animal_label::eagle, verb="visit") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM activity(actor="mouse", object=animal_label::squirrel, verb="eat") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    CLAIM attribute_claim(property="color", subject="mouse", value="green") BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_5 : CLAIM
    CLAIM statement(fact=character_trait_4) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::mouse, verb="eat") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    CLAIM attribute_claim(property="color", subject="squirrel", value="blue") BY role_user STATUS asserted SOURCE "t1:s12" -> attribute_claim_6 : CLAIM
    CLAIM statement(fact=character_trait_3) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM character_trait(property="temperament", value="nice") -> character_trait_5 : TERM
    TERM negation(target=character_trait_5) -> negation_3 : TERM
    CLAIM attribute_claim(property="temperament", subject="squirrel", value="not_nice") BY role_user STATUS asserted SOURCE "t1:s13" -> attribute_claim_7 : CLAIM
    CLAIM statement(fact=negation_3) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::eagle, verb="see") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::mouse, verb="visit") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM activity(actor="someone", object=animal_label::mouse, verb="visit") -> activity_10 : TERM
    TERM conditional(condition=character_trait_5, consequence=activity_10) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM conditional(condition=character_trait_4, consequence=character_trait_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM activity(actor="someone", object=animal_label::bear, verb="see") -> activity_11 : TERM
    TERM activity(actor="bear", object=animal_label::mouse, verb="visit") -> activity_12 : TERM
    TERM conjunction(items=[activity_11, activity_12]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=character_trait_5) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM
    TERM activity(actor="someone", object=animal_label::mouse, verb="see") -> activity_13 : TERM
    TERM activity(actor="someone", object=animal_label::squirrel, verb="visit") -> activity_14 : TERM
    TERM conjunction(items=[activity_13, activity_14]) -> conjunction_3 : TERM
    TERM activity(actor="mouse", object=animal_label::eagle, verb="eat") -> activity_15 : TERM
    TERM negation(target=activity_15) -> negation_4 : TERM
    TERM conditional(condition=conjunction_3, consequence=negation_4) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_19 : CLAIM
    TERM activity(actor="someone", object=animal_label::bear, verb="visit") -> activity_16 : TERM
    TERM conjunction(items=[activity_16, character_trait_4]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_5) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_20 : CLAIM
    TERM activity(actor="mouse", object=animal_label::squirrel, verb="visit") -> activity_17 : TERM
    TERM conditional(condition=activity_9, consequence=activity_17) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_21 : CLAIM
    TERM activity(actor="someone", object=animal_label::eagle, verb="eat") -> activity_18 : TERM
    TERM conjunction(items=[activity_18, activity_2]) -> conjunction_5 : TERM
    TERM activity(actor="someone", object=animal_label::mouse, verb="see") -> activity_19 : TERM
    TERM conditional(condition=conjunction_5, consequence=activity_19) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_22 : CLAIM
    TERM activity(actor="someone", object=animal_label::squirrel, verb="eat") -> activity_20 : TERM
    TERM conditional(condition=activity_10, consequence=activity_20) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_23 : CLAIM
    TERM negation(target=activity_20) -> negation_5 : TERM
    TERM conjunction(items=[character_trait_3, negation_5]) -> conjunction_6 : TERM
    TERM negation(target=character_trait_2) -> negation_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=negation_6) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s24" -> statement_24 : CLAIM
    TERM negation(target=character_trait_5) -> negation_7 : TERM
    CLAIM attribute_claim(property="temperament", subject="bald_eagle", value="not_nice") BY role_user STATUS asserted SOURCE "t1:s26" -> attribute_claim_8 : CLAIM
    CLAIM statement(fact=negation_7) BY role_user STATUS asserted SOURCE "t1:s26" -> statement_25 : CLAIM
    TERM property_question(property="truth_value", subject="theory") -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | claim | statement | covered |
| n3 | object | animal_label::eagle | label-preserved |
| n4 | constraint | character_trait | covered |
| n5 | claim | statement | covered |
| n6 | object | animal_label::bear | label-preserved |
| n7 | action | activity | covered |
| n8 | claim | statement | covered |
| n9 | action | activity | covered |
| n10 | claim | statement | covered |
| n11 | object | animal_label::squirrel | label-preserved |
| n12 | action | activity | covered |
| n13 | claim | statement | covered |
| n14 | negation | negation | covered |
| n15 | constraint | color_label::blue | label-preserved |
| n16 | claim | statement | covered |
| n17 | constraint | color_label::green | label-preserved |
| n18 | claim | statement | covered |
| n19 | claim | statement | covered |
| n20 | object | animal_label::mouse | label-preserved |
| n21 | claim | statement | covered |
| n22 | claim | statement | covered |
| n23 | claim | statement | covered |
| n24 | claim | statement | covered |
| n25 | negation | negation | covered |
| n26 | constraint | character_trait | covered |
| n27 | claim | statement | covered |
| n28 | claim | statement | covered |
| n29 | reasoning | conditional | covered |
| n30 | reasoning | color_label::green | label-preserved |
| n31 | reasoning | conditional | covered |
| n32 | reasoning | conditional | covered |
| n33 | reasoning | conditional | covered |
| n34 | reasoning | conditional | covered |
| n35 | reasoning | conditional | covered |
| n36 | reasoning | conditional | covered |
| n37 | reasoning | conditional | covered |
| n38 | speech_act | ask | covered |
| n39 | constraint | property_question | covered |
| n40 | constraint | property_question | covered |
| n41 | claim | statement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s26 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" -> animal_label::eagle; t1:s3 "bear" -> animal_label::bear; t1:s5 "squirrel" -> animal_label::squirrel; t1:s6 "blue" -> color_label::blue; t1:s7 "green" -> color_label::green; t1:s9 "mouse" -> animal_label::mouse; t1:s17 "green" -> color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
