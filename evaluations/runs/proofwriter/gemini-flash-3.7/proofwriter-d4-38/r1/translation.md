Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=animal_label::bear) -> lexical_label_2 : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    TERM character_trait(property="color", value="green") -> character_trait_2 : TERM
    CLAIM statement(fact=character_trait_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM character_trait(property="shape", value=shape_round) -> character_trait_3 : TERM
    CLAIM statement(fact=character_trait_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM activity(actor="bear", object=animal_label::cow, verb="likes") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM activity(actor="bear", object=animal_label::lion, verb="sees") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM activity(actor="cow", object=animal_label::bear, verb="eats") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM character_trait(property="texture", value="rough") -> character_trait_4 : TERM
    CLAIM statement(fact=character_trait_4) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM character_trait(property="age", value="young") -> character_trait_5 : TERM
    CLAIM statement(fact=character_trait_5) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM activity(actor="cow", object=animal_label::bear, verb="likes") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM activity(actor="lion", object=animal_label::squirrel, verb="sees") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::bear, verb="eats") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM character_trait(property="texture", value="rough") -> character_trait_6 : TERM
    CLAIM statement(fact=character_trait_6) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::bear, verb="sees") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM activity(actor="something", object=animal_label::lion, verb="eats") -> activity_9 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="sees") -> activity_10 : TERM
    TERM conjunction(items=[activity_9, activity_10]) -> conjunction_2 : TERM
    TERM activity(actor="lion", object=animal_label::squirrel, verb="likes") -> activity_11 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_11) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM character_trait(property="state", value=state_cold) -> character_trait_7 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="eats") -> activity_12 : TERM
    TERM conditional(condition=character_trait_7, consequence=activity_12) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM activity(actor="something", object=animal_label::cow, verb="eats") -> activity_13 : TERM
    TERM activity(actor="something", object=animal_label::bear, verb="eats") -> activity_14 : TERM
    TERM conjunction(items=[activity_13, activity_14]) -> conjunction_3 : TERM
    TERM activity(actor="cow", object=animal_label::lion, verb="sees") -> activity_15 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_15) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM character_trait(property="color", value="green") -> character_trait_8 : TERM
    TERM character_trait(property="state", value=state_cold) -> character_trait_9 : TERM
    TERM conditional(condition=character_trait_8, consequence=character_trait_9) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM activity(actor="something", object=animal_label::squirrel, verb="sees") -> activity_16 : TERM
    TERM activity(actor="squirrel", object=animal_label::bear, verb="sees") -> activity_17 : TERM
    TERM conditional(condition=activity_16, consequence=activity_17) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM
    TERM activity(actor="something", object=animal_label::bear, verb="sees") -> activity_18 : TERM
    TERM character_trait(property="age", value="young") -> character_trait_10 : TERM
    TERM conditional(condition=activity_18, consequence=character_trait_10) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_19 : CLAIM
    TERM activity(actor="cow", object=animal_label::bear, verb="likes") -> activity_19 : TERM
    TERM activity(actor="cow", object=animal_label::lion, verb="eats") -> activity_20 : TERM
    TERM conjunction(items=[activity_19, activity_20]) -> conjunction_4 : TERM
    TERM character_trait(property="texture", value="rough") -> character_trait_11 : TERM
    TERM conditional(condition=conjunction_4, consequence=character_trait_11) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_20 : CLAIM
    TERM character_trait(property="texture", value="rough") -> character_trait_12 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="likes") -> activity_21 : TERM
    TERM conditional(condition=character_trait_12, consequence=activity_21) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_21 : CLAIM
    TERM character_trait(property="age", value="young") -> character_trait_13 : TERM
    TERM character_trait(property="color", value="green") -> character_trait_14 : TERM
    TERM conditional(condition=character_trait_13, consequence=character_trait_14) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_22 : CLAIM
    TERM requirement(property="basis", value="theory") -> requirement_2 : TERM
    TERM requirement(property="format", value="true_false_unknown") -> requirement_3 : TERM
    TERM character_trait(property="texture", value="rough") -> character_trait_15 : TERM
    CLAIM statement(fact=character_trait_15) BY role_user STATUS hypothesized SOURCE "t1:s24" -> statement_23 : CLAIM
    UTTER ask(target=statement_23, constraints=[requirement_2, requirement_3])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, statement | covered |
| n2 | object | animal_label::bear, lexical_label | label-preserved |
| n3 | constraint | color_label::green, lexical_label | label-preserved |
| n4 | claim | character_trait, statement | covered |
| n5 | constraint | shape_round, character_trait | covered |
| n6 | claim | shape_round, character_trait, statement | covered |
| n7 | object | animal_label::cow, activity | label-preserved |
| n8 | claim | animal_label::cow, activity, statement | covered |
| n9 | object | animal_label::lion, activity | label-preserved |
| n10 | claim | animal_label::lion, activity, statement | covered |
| n11 | claim | animal_label::bear, animal_label::cow, activity, statement | covered |
| n12 | constraint | character_trait | covered |
| n13 | claim | character_trait, statement | covered |
| n14 | constraint | character_trait | covered |
| n15 | claim | character_trait, statement | covered |
| n16 | claim | animal_label::bear, animal_label::cow, activity, statement | covered |
| n17 | object | animal_label::squirrel, activity | label-preserved |
| n18 | claim | animal_label::squirrel, activity, statement | covered |
| n19 | claim | animal_label::bear, activity, statement | covered |
| n20 | claim | character_trait, statement | covered |
| n21 | claim | animal_label::bear, activity, statement | covered |
| n22 | reasoning | animal_label::lion, animal_label::squirrel, activity, conjunction, conditional, statement | covered |
| n23 | reasoning | animal_label::lion, state_cold, character_trait, activity, conditional, statement | covered |
| n24 | reasoning | animal_label::cow, animal_label::bear, animal_label::lion, activity, conjunction, conditional, statement | covered |
| n25 | reasoning | state_cold, character_trait, conditional, statement | covered |
| n26 | reasoning | animal_label::squirrel, animal_label::bear, activity, conditional, statement | covered |
| n27 | reasoning | animal_label::bear, activity, character_trait, conditional, statement | covered |
| n28 | reasoning | animal_label::bear, animal_label::cow, animal_label::lion, activity, conjunction, character_trait, conditional, statement | covered |
| n29 | reasoning | animal_label::lion, character_trait, activity, conditional, statement | covered |
| n30 | reasoning | character_trait, conditional, statement | covered |
| n31 | speech_act | requirement, statement, ask | covered |
| n32 | constraint | requirement | covered |
| n33 | constraint | requirement | covered |
| n34 | claim | character_trait, statement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bear" → animal_label::bear, "green" → color_label::green; t1:s4 "cow" → animal_label::cow; t1:s5 "lion" → animal_label::lion; t1:s10 "squirrel" → animal_label::squirrel
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
