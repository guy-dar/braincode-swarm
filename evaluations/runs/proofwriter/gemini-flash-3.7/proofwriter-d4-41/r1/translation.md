Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="dog", object=animal_label::lion, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="dog", object=animal_label::rabbit, verb="chase") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    CLAIM attribute_claim(property="size", subject="dog", value=size_large) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="age", subject="dog", value="young") BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_3 : CLAIM
    TERM activity(actor="dog", object=animal_label::lion, verb="like") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_4 : CLAIM
    TERM activity(actor="dog", object=animal_label::mouse, verb="like") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_5 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="lion", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_4 : CLAIM
    TERM activity(actor="mouse", object=animal_label::rabbit, verb="chase") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_6 : CLAIM
    CLAIM attribute_claim(property="shape", subject="mouse", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_5 : CLAIM
    TERM activity(actor="mouse", object=animal_label::dog, verb="like") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_7 : CLAIM
    TERM activity(actor="mouse", object=animal_label::lion, verb="like") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_8 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::lion, verb="chase") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_9 : CLAIM
    TERM requirement(property="shape", value=shape_round) -> requirement_2 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="see") -> activity_10 : TERM
    TERM conjunction(items=[requirement_2, activity_10]) -> conjunction_2 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="chase") -> activity_11 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_11) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_10 : CLAIM
    TERM activity(actor="something", object=animal_label::mouse, verb="like") -> activity_12 : TERM
    TERM requirement(property="state", value=state_cold) -> requirement_3 : TERM
    TERM conditional(condition=activity_12, consequence=requirement_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_11 : CLAIM
    TERM activity(actor="something", object=animal_label::mouse, verb="chase") -> activity_13 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="see") -> activity_14 : TERM
    TERM conditional(condition=activity_13, consequence=activity_14) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_12 : CLAIM
    TERM activity(actor="something", object=animal_label::lion, verb="see") -> activity_15 : TERM
    TERM requirement(property="state", value=state_cold) -> requirement_4 : TERM
    TERM conditional(condition=activity_15, consequence=requirement_4) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_13 : CLAIM
    TERM requirement(property="size", value=size_large) -> requirement_5 : TERM
    TERM requirement(property="shape", value=shape_round) -> requirement_6 : TERM
    TERM conjunction(items=[requirement_5, requirement_6]) -> conjunction_3 : TERM
    TERM activity(actor="something", object=animal_label::rabbit, verb="chase") -> activity_16 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_16) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_14 : CLAIM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_7 : TERM
    TERM activity(actor="mouse", object=animal_label::lion, verb="like") -> activity_17 : TERM
    TERM conditional(condition=requirement_7, consequence=activity_17) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_15 : CLAIM
    TERM requirement(property="state", value=state_cold) -> requirement_8 : TERM
    TERM activity(actor="something", object=animal_label::mouse, verb="chase") -> activity_18 : TERM
    TERM conditional(condition=requirement_8, consequence=activity_18) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_16 : CLAIM
    TERM requirement(property="state", value=state_cold) -> requirement_9 : TERM
    TERM activity(actor="rabbit", object=animal_label::lion, verb="chase") -> activity_19 : TERM
    TERM conjunction(items=[requirement_9, activity_19]) -> conjunction_4 : TERM
    TERM activity(actor="rabbit", object=animal_label::mouse, verb="chase") -> activity_20 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_20) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_17 : CLAIM
    TERM requirement(property="basis", value="theory") -> requirement_10 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    CLAIM attribute_claim(property="state", subject="lion", value=state_cold) BY role_user STATUS hypothesized SOURCE "t1:s23" -> attribute_claim_6 : CLAIM
    UTTER ask(target=attribute_claim_6, constraints=[constraint_single_choice_2, requirement_10])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement | covered |
| n2 | object | animal_label::dog | label-preserved |
| n3 | object | animal_label::lion | label-preserved |
| n4 | claim | activity, statement | covered |
| n5 | object | animal_label::rabbit | label-preserved |
| n6 | claim | activity, statement | covered |
| n7 | claim | attribute_claim, size_large | covered |
| n8 | claim | attribute_claim | covered |
| n9 | claim | activity, statement | covered |
| n10 | object | animal_label::mouse | label-preserved |
| n11 | claim | activity, statement | covered |
| n12 | constraint | color_label::blue | label-preserved |
| n13 | claim | attribute_claim, lexical_label | covered |
| n14 | claim | activity, statement | covered |
| n15 | claim | attribute_claim, shape_round | covered |
| n16 | claim | activity, statement | covered |
| n17 | claim | activity, statement | covered |
| n18 | claim | activity, statement | covered |
| n19 | claim | activity, conditional, conjunction, shape_round, statement | covered |
| n20 | claim | activity, conditional, requirement, state_cold, statement | covered |
| n21 | claim | activity, conditional, statement | covered |
| n22 | claim | activity, conditional, requirement, state_cold, statement | covered |
| n23 | claim | activity, conditional, conjunction, requirement, shape_round, size_large, statement | covered |
| n24 | claim | activity, conditional, lexical_label, requirement, statement | covered |
| n25 | claim | activity, conditional, requirement, state_cold, statement | covered |
| n26 | claim | activity, conditional, conjunction, requirement, state_cold, statement | covered |
| n27 | speech_act | ask | covered |
| n28 | constraint | requirement | covered |
| n29 | constraint | constraint_single_choice | covered |
| n30 | claim | attribute_claim, state_cold | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s23 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "dog" → animal_label::dog, t1:s2 "lion" → animal_label::lion, t1:s3 "rabbit" → animal_label::rabbit, t1:s7 "mouse" → animal_label::mouse, t1:s8 "blue" → color_label::blue
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
