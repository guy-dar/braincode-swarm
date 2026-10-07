Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    UTTER inform(target=subject_2)
    TERM activity(actor="cat", object=animal_label::mouse, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="cat", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_2 : CLAIM
    TERM activity(actor="lion", object=animal_label::cat, verb="chase") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_3 : CLAIM
    TERM activity(actor="lion", object=animal_label::cat, verb="like") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_4 : CLAIM
    CLAIM attribute_claim(property="age", subject="mouse", value="young") BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_3 : CLAIM
    TERM activity(actor="mouse", object=animal_label::lion, verb="like") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_5 : CLAIM
    TERM activity(actor="tiger", object=animal_label::cat, verb="chase") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_6 : CLAIM
    TERM activity(actor="tiger", object=animal_label::lion, verb="chase") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_7 : CLAIM
    TERM activity(actor="tiger", object=animal_label::mouse, verb="chase") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_8 : CLAIM
    TERM activity(actor="tiger", object=animal_label::cat, verb="like") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_9 : CLAIM
    TERM activity(actor="something", object=animal_label::lion, verb="like") -> activity_10 : TERM
    TERM activity(actor="it", object=animal_label::tiger, verb="chase") -> activity_11 : TERM
    TERM conditional(condition=activity_10, consequence=activity_11) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_10 : CLAIM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    TERM conditional(condition=requirement_2, consequence=activity_10) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_11 : CLAIM
    TERM activity(actor="something", object=animal_label::mouse, verb="like") -> activity_12 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_3 : TERM
    TERM conditional(condition=activity_12, consequence=requirement_3) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_12 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_4 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="chase") -> activity_13 : TERM
    TERM conditional(condition=activity_13, consequence=requirement_4) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_13 : CLAIM
    TERM activity(actor="tiger", object=animal_label::lion, verb="like") -> activity_14 : TERM
    TERM conditional(condition=requirement_4, consequence=activity_14) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_14 : CLAIM
    TERM activity(actor="mouse", object=animal_label::cat, verb="eat") -> activity_15 : TERM
    TERM activity(actor="mouse", object=animal_label::tiger, verb="like") -> activity_16 : TERM
    TERM conjunction(items=[activity_15, activity_16]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_5) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_15 : CLAIM
    TERM activity(actor="something", object=animal_label::tiger, verb="chase") -> activity_17 : TERM
    TERM conditional(condition=activity_17, consequence=requirement_2) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_16 : CLAIM
    TERM activity(actor="something", object=animal_label::lion, verb="eat") -> activity_18 : TERM
    TERM conjunction(items=[activity_18, requirement_4]) -> conjunction_3 : TERM
    TERM requirement(property="size", value=size_large) -> requirement_5 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_5) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_17 : CLAIM
    TERM conjunction(items=[requirement_4, requirement_2]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_5) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_18 : CLAIM
    TERM requirement(property="basis", value="theory") -> requirement_6 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM activity(actor="tiger", object=animal_label::tiger, verb="chase") -> activity_19 : TERM
    CLAIM statement(fact=activity_19) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_19 : CLAIM
    UTTER ask(target=activity_19, constraints=[constraint_single_choice_2, requirement_6])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | inform, subject | covered |
| n2 | object | animal_label::cat | label-preserved |
| n3 | object | animal_label::mouse | label-preserved |
| n4 | claim | statement, activity | covered |
| n5 | constraint | color_label::blue | label-preserved |
| n6 | claim | attribute_claim, lexical_label | covered |
| n7 | object | animal_label::lion | label-preserved |
| n8 | claim | statement, activity | covered |
| n9 | claim | statement, activity | covered |
| n10 | claim | attribute_claim | covered |
| n11 | claim | statement, activity | covered |
| n12 | object | animal_label::tiger | label-preserved |
| n13 | claim | statement, activity | covered |
| n14 | claim | statement, activity | covered |
| n15 | claim | statement, activity | covered |
| n16 | claim | statement, activity | covered |
| n17 | reasoning | conditional, statement, activity | covered |
| n18 | reasoning | conditional, statement, requirement, activity | covered |
| n19 | reasoning | conditional, statement, activity, requirement | covered |
| n20 | constraint | color_label::green | label-preserved |
| n21 | reasoning | conditional, statement, activity, requirement, lexical_label | covered |
| n22 | reasoning | conditional, statement, requirement, activity | covered |
| n23 | reasoning | conditional, conjunction, statement, activity | covered |
| n24 | reasoning | conditional, statement, activity, requirement | covered |
| n25 | reasoning | conditional, conjunction, requirement, size_large, statement, activity | covered |
| n26 | reasoning | conditional, conjunction, requirement, size_large, statement | covered |
| n27 | speech_act | ask, activity | covered |
| n28 | constraint | requirement | covered |
| n29 | constraint | constraint_single_choice | covered |
| n30 | claim | statement, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "cat" → animal_label::cat; t1:s2 "mouse" → animal_label::mouse; t1:s3 "blue" → color_label::blue; t1:s4 "lion" → animal_label::lion; t1:s8 "tiger" → animal_label::tiger; t1:s15 "green" → color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
