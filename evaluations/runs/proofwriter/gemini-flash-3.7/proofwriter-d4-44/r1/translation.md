Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="bald_eagle", object=animal_label::cow, verb="visit") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="cow", object=animal_label::rabbit, verb="like") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM activity(actor="cow", object=animal_label::mouse, verb="visit") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    CLAIM statement(fact=requirement_2) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM requirement(property="personality", value="nice") -> requirement_3 : TERM
    CLAIM statement(fact=requirement_3) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM requirement(property="age", value="young") -> requirement_4 : TERM
    CLAIM statement(fact=requirement_4) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::mouse, verb="like") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM activity(actor="something", object=animal_label::rabbit, verb="like") -> activity_6 : TERM
    TERM activity(actor="something", object=animal_label::cow, verb="like") -> activity_7 : TERM
    TERM conditional(condition=activity_6, consequence=activity_7) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM activity(actor="something", object=animal_label::rabbit, verb="visit") -> activity_8 : TERM
    TERM activity(actor="something", object=animal_label::mouse, verb="need") -> activity_9 : TERM
    TERM conjunction(items=[activity_8, activity_9]) -> conjunction_2 : TERM
    TERM activity(actor="something", object=animal_label::rabbit, verb="need") -> activity_10 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_10) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM activity(actor="something", object=animal_label::rabbit, verb="like") -> activity_11 : TERM
    TERM activity(actor="rabbit", object="bald_eagle", verb="need") -> activity_12 : TERM
    TERM conjunction(items=[activity_11, activity_12]) -> conjunction_3 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::rabbit, verb="need") -> activity_13 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_13) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM activity(actor="something", object=animal_label::cow, verb="like") -> activity_14 : TERM
    TERM activity(actor="something", object="bald_eagle", verb="visit") -> activity_15 : TERM
    TERM conditional(condition=activity_14, consequence=activity_15) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM activity(actor="something", object=animal_label::rabbit, verb="need") -> activity_16 : TERM
    TERM conditional(condition=requirement_3, consequence=activity_16) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM conjunction(items=[requirement_3, activity_3]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_2) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM activity(actor="something", object="bald_eagle", verb="visit") -> activity_17 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::rabbit, verb="like") -> activity_18 : TERM
    TERM conditional(condition=activity_17, consequence=activity_18) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM requirement(property="personality", value="kind") -> requirement_5 : TERM
    TERM requirement(property="shape", value=shape_round) -> requirement_6 : TERM
    TERM conjunction(items=[requirement_5, requirement_6]) -> conjunction_5 : TERM
    TERM activity(actor="something", object=animal_label::mouse, verb="like") -> activity_19 : TERM
    TERM conditional(condition=conjunction_5, consequence=activity_19) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM activity(actor="something", object=animal_label::rabbit, verb="visit") -> activity_20 : TERM
    TERM activity(actor="something", object="bald_eagle", verb="like") -> activity_21 : TERM
    TERM conditional(condition=activity_20, consequence=activity_21) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::cow, verb="like") -> activity_22 : TERM
    CLAIM statement(fact=activity_22) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_18 : CLAIM
    TERM property_question(property="truth_value", subject=activity_22) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement | covered |
| n2 | object | bald_eagle | covered |
| n3 | object | animal_label::cow | label-preserved |
| n4 | claim | activity, statement | covered |
| n5 | object | animal_label::rabbit | label-preserved |
| n6 | claim | activity, statement | covered |
| n7 | object | animal_label::mouse | label-preserved |
| n8 | claim | activity, statement | covered |
| n9 | constraint | color_label::green | label-preserved |
| n10 | claim | lexical_label, requirement, statement | covered |
| n11 | claim | requirement, statement | covered |
| n12 | claim | requirement, statement | covered |
| n13 | claim | activity, statement | covered |
| n14 | claim | activity, conditional, statement | covered |
| n15 | claim | activity, conditional, conjunction, statement | covered |
| n16 | claim | activity, conditional, conjunction, statement | covered |
| n17 | claim | activity, conditional, statement | covered |
| n18 | claim | activity, conditional, requirement, statement | covered |
| n19 | claim | activity, conditional, conjunction, requirement, statement | covered |
| n20 | claim | activity, conditional, statement | covered |
| n21 | claim | activity, conditional, conjunction, requirement, shape_round, statement | covered |
| n22 | claim | activity, conditional, statement | covered |
| n23 | speech_act | ask, property_question | covered |
| n24 | constraint | property_question | covered |
| n25 | constraint | property_question | covered |
| n26 | claim | activity, statement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "cow" -> animal_label::cow; t1:s3 "rabbit" -> animal_label::rabbit; t1:s4 "mouse" -> animal_label::mouse; t1:s5 "green" -> color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
