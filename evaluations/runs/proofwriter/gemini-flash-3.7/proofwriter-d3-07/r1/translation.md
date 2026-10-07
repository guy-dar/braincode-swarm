Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=animal_label::cat) -> lexical_label_2 : TERM
    TERM lexical_label(value=animal_label::squirrel) -> lexical_label_3 : TERM
    TERM lexical_label(value=animal_label::cow) -> lexical_label_4 : TERM
    TERM lexical_label(value=animal_label::rabbit) -> lexical_label_5 : TERM
    TERM lexical_label(value=color_label::blue) -> lexical_label_6 : TERM
    TERM lexical_label(value=color_label::red) -> lexical_label_7 : TERM
    TERM activity(actor="cat", object=animal_label::squirrel, verb="need") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="cow", object=animal_label::squirrel, verb="chase") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    CLAIM attribute_claim(property="color", subject="cow", value=lexical_label_6) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_2 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::cat, verb="chase") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_4 : CLAIM
    CLAIM attribute_claim(property="trait", subject="rabbit", value="kind") BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="color", subject="rabbit", value=lexical_label_7) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_4 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::cat, verb="eat") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_5 : CLAIM
    CLAIM attribute_claim(property="trait", subject="squirrel", value="kind") BY role_user STATUS asserted SOURCE "t1:s9" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="color", subject="squirrel", value=lexical_label_7) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_6 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::cow, verb="need") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_6 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::rabbit, verb="need") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_7 : CLAIM
    TERM activity(actor="something", object=animal_label::cow, verb="need") -> activity_8 : TERM
    TERM activity(actor="something", object=animal_label::cow, verb="eat") -> activity_9 : TERM
    TERM conditional(condition=activity_8, consequence=activity_9) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_8 : CLAIM
    TERM character_trait(property="color", value="red") -> character_trait_2 : TERM
    TERM character_trait(property="size", value="big") -> character_trait_3 : TERM
    TERM conditional(condition=character_trait_2, consequence=character_trait_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_9 : CLAIM
    TERM character_trait(property="color", value="blue") -> character_trait_4 : TERM
    TERM character_trait(property="trait", value="nice") -> character_trait_5 : TERM
    TERM conjunction(items=[character_trait_4, character_trait_5]) -> conjunction_2 : TERM
    TERM activity(actor="something", object=animal_label::cow, verb="chase") -> activity_10 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_10) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_10 : CLAIM
    TERM conditional(condition=character_trait_5, consequence=activity_7) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_11 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::cat, verb="need") -> activity_11 : TERM
    TERM conjunction(items=[activity_2, activity_11]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=character_trait_4) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_12 : CLAIM
    TERM conditional(condition=activity_9, consequence=character_trait_5) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_13 : CLAIM
    TERM activity(actor="something", object=animal_label::rabbit, verb="chase") -> activity_12 : TERM
    TERM conditional(condition=activity_12, consequence=character_trait_4) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_14 : CLAIM
    TERM activity(actor="something", object=animal_label::squirrel, verb="need") -> activity_13 : TERM
    TERM conditional(condition=character_trait_2, consequence=activity_13) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_15 : CLAIM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM test_condition(condition="theory_evaluation", expected=TRUE) -> test_condition_2 : TERM
    TERM activity(actor="squirrel", object=animal_label::rabbit, verb="chase") -> activity_14 : TERM
    CLAIM statement(fact=activity_14) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_16 : CLAIM
    UTTER ask(target=activity_14, constraints=[constraint_single_choice_2, test_condition_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, conditional, conjunction | covered |
| n2 | object | animal_label::cat | label-preserved |
| n3 | object | animal_label::squirrel | label-preserved |
| n4 | object | animal_label::cow | label-preserved |
| n5 | object | animal_label::rabbit | label-preserved |
| n6 | action | activity(verb="need") | covered |
| n7 | action | activity(verb="chase") | covered |
| n8 | action | activity(verb="eat") | covered |
| n9 | constraint | color_label::blue | label-preserved |
| n10 | constraint | color_label::red | label-preserved |
| n11 | constraint | attribute_claim(property="trait", value="kind") | covered |
| n12 | constraint | character_trait(property="trait", value="nice") | covered |
| n13 | constraint | character_trait(property="size", value="big") | covered |
| n14 | claim | statement(fact=activity_2), animal_label::squirrel | label-preserved |
| n15 | claim | statement(fact=activity_3), animal_label::squirrel | label-preserved |
| n16 | claim | attribute_claim(property="color", subject="cow", value=lexical_label_6) | covered |
| n17 | claim | statement(fact=activity_4) | covered |
| n18 | claim | attribute_claim(property="trait", subject="rabbit", value="kind") | covered |
| n19 | claim | attribute_claim(property="color", subject="rabbit", value=lexical_label_7) | covered |
| n20 | claim | statement(fact=activity_5), animal_label::cat | label-preserved |
| n21 | claim | attribute_claim(property="trait", subject="squirrel", value="kind"), animal_label::squirrel | label-preserved |
| n22 | claim | attribute_claim(property="color", subject="squirrel", value=lexical_label_7) | covered |
| n23 | claim | statement(fact=activity_6), animal_label::cow | label-preserved |
| n24 | claim | statement(fact=activity_7) | covered |
| n25 | reasoning | conditional(condition=activity_8, consequence=activity_9), statement | covered |
| n26 | reasoning | conditional(condition=character_trait_2, consequence=character_trait_3), color_label::red | label-preserved |
| n27 | reasoning | conditional(condition=conjunction_2, consequence=activity_10), animal_label::cow | label-preserved |
| n28 | reasoning | conditional(condition=character_trait_5, consequence=activity_7), statement | covered |
| n29 | reasoning | conditional(condition=conjunction_3, consequence=character_trait_4), animal_label::squirrel | label-preserved |
| n30 | reasoning | conditional(condition=activity_9, consequence=character_trait_5), animal_label::cow | label-preserved |
| n31 | reasoning | conditional(condition=activity_12, consequence=character_trait_4), statement | covered |
| n32 | reasoning | conditional(condition=character_trait_2, consequence=activity_13), statement | covered |
| n33 | speech_act | ask, statement, conditional | covered |
| n34 | constraint | test_condition | covered |
| n35 | constraint | constraint_single_choice | covered |
| n36 | claim | statement(fact=activity_14) | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "cat" → animal_label::cat, t1:s2 "squirrel" → animal_label::squirrel, t1:s3 "cow" → animal_label::cow, t1:s5 "rabbit" → animal_label::rabbit, t1:s4 "blue" → color_label::blue, t1:s7 "red" → color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
