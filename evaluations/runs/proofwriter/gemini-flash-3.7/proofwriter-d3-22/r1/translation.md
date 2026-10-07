Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="bald_eagle", object=animal_label::cow, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    CLAIM statement(fact=requirement_2) BY user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::squirrel, verb="see") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM activity(actor="cow", object=animal_label::rabbit, verb="chase") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM activity(actor="cow", object=animal_label::rabbit, verb="eat") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    CLAIM statement(fact=requirement_2) BY user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::cow, verb="chase") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::eagle, verb="eat") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM requirement(property="nice", value=TRUE) -> requirement_3 : TERM
    CLAIM statement(fact=requirement_3) BY user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM requirement(property="rough", value=TRUE) -> requirement_4 : TERM
    CLAIM statement(fact=requirement_4) BY user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::cow, verb="eat") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::rabbit, verb="eat") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    CLAIM statement(fact=requirement_3) BY user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::rabbit, verb="see") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM activity(actor="something", object=animal_label::squirrel, verb="chase") -> activity_11 : TERM
    TERM activity(actor="squirrel", object=animal_label::cow, verb="chase") -> activity_12 : TERM
    TERM conditional(condition=activity_11, consequence=activity_12) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM activity(actor="something", object=animal_label::squirrel, verb="eat") -> activity_13 : TERM
    TERM conjunction(items=[activity_11, activity_13]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_12) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM activity(actor="something", object=animal_label::rabbit, verb="eat") -> activity_14 : TERM
    TERM conjunction(items=[activity_14, requirement_4]) -> conjunction_3 : TERM
    TERM requirement(property="shape", value=shape_round) -> requirement_5 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_5) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM
    TERM activity(actor="something", object=animal_label::rabbit, verb="chase") -> activity_15 : TERM
    TERM requirement(property="kind", value=TRUE) -> requirement_6 : TERM
    TERM conditional(condition=activity_15, consequence=requirement_6) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY user STATUS asserted SOURCE "t1:s19" -> statement_19 : CLAIM
    TERM conditional(condition=requirement_6, consequence=activity_11) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY user STATUS asserted SOURCE "t1:s20" -> statement_20 : CLAIM
    TERM activity(actor="something", object=animal_label::cow, verb="chase") -> activity_16 : TERM
    TERM conditional(condition=activity_16, consequence=requirement_6) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY user STATUS asserted SOURCE "t1:s21" -> statement_21 : CLAIM
    TERM negation(target=activity_15) -> negation_2 : TERM
    TERM conjunction(items=[activity_14, negation_2]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_3) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY user STATUS asserted SOURCE "t1:s22" -> statement_22 : CLAIM
    TERM requirement(property="context", value="theory") -> requirement_7 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM negation(target=activity_12) -> negation_3 : TERM
    UTTER ask(target=negation_3, constraints=[requirement_7, constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, conjunction | covered |
| n2 | object | animal_label::eagle | label-preserved |
| n3 | object | animal_label::cow | label-preserved |
| n4 | action | activity | covered |
| n5 | claim | statement | covered |
| n6 | constraint | color_label::red, constraint_single_choice | label-preserved |
| n7 | claim | statement | covered |
| n8 | object | animal_label::squirrel | label-preserved |
| n9 | action | activity | covered |
| n10 | claim | statement | covered |
| n11 | object | animal_label::rabbit | label-preserved |
| n12 | claim | statement | covered |
| n13 | action | activity | covered |
| n14 | claim | statement | covered |
| n15 | claim | statement | covered |
| n16 | claim | statement | covered |
| n17 | claim | statement | covered |
| n18 | constraint | constraint_single_choice, requirement | covered |
| n19 | claim | statement | covered |
| n20 | constraint | constraint_single_choice, requirement | covered |
| n21 | claim | statement | covered |
| n22 | claim | statement | covered |
| n23 | claim | statement | covered |
| n24 | claim | statement | covered |
| n25 | claim | statement | covered |
| n26 | reasoning | conditional | covered |
| n27 | reasoning | conditional | covered |
| n28 | constraint | shape_round, constraint_single_choice | covered |
| n29 | reasoning | shape_round, conditional | covered |
| n30 | constraint | requirement | covered |
| n31 | reasoning | conditional | covered |
| n32 | reasoning | animal_label::squirrel, conditional | label-preserved |
| n33 | reasoning | animal_label::cow, conditional | label-preserved |
| n34 | negation | negation | covered |
| n35 | reasoning | negation, conditional | covered |
| n36 | speech_act | ask, statement, negation | covered |
| n37 | constraint | constraint_single_choice, requirement | covered |
| n38 | constraint | constraint_single_choice, requirement | covered |
| n39 | negation | negation | covered |
| n40 | claim | negation, statement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" → animal_label::eagle, t1:s2 "cow" → animal_label::cow, t1:s3 "red" → color_label::red, t1:s4 "squirrel" → animal_label::squirrel, t1:s5 "rabbit" → animal_label::rabbit, t1:s20 "squirrel" → animal_label::squirrel, t1:s21 "cow" → animal_label::cow
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
