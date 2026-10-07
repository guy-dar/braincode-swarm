Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="bald_eagle", object=animal_label::rabbit, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::rabbit, verb="like") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::tiger, verb="like") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::rabbit, verb="see") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM activity(actor="mouse", object=animal_label::eagle, verb="chase") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM activity(actor="mouse", object=animal_label::tiger, verb="chase") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM activity(actor="mouse", object=animal_label::rabbit, verb="like") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM activity(actor="mouse", object=animal_label::eagle, verb="see") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::tiger, verb="chase") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM activity(actor="rabbit", verb="is_big") -> activity_11 : TERM
    CLAIM statement(fact=activity_11) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    TERM activity(actor="rabbit", object=lexical_label_2, verb="is_red") -> activity_12 : TERM
    CLAIM statement(fact=activity_12) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::mouse, verb="like") -> activity_13 : TERM
    CLAIM statement(fact=activity_13) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::tiger, verb="like") -> activity_14 : TERM
    CLAIM statement(fact=activity_14) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM activity(actor="tiger", object=animal_label::eagle, verb="like") -> activity_15 : TERM
    CLAIM statement(fact=activity_15) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM activity(actor="something", object=animal_label::tiger, verb="like") -> activity_16 : TERM
    TERM activity(actor="something", object=animal_label::tiger, verb="see") -> activity_17 : TERM
    TERM conditional(condition=activity_16, consequence=activity_17) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM activity(actor="something", object=animal_label::rabbit, verb="like") -> activity_18 : TERM
    TERM activity(actor="rabbit", verb="is_rough") -> activity_19 : TERM
    TERM conjunction(items=[activity_18, activity_19]) -> conjunction_2 : TERM
    TERM activity(actor="rabbit", object=animal_label::eagle, verb="chase") -> activity_20 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_20) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM activity(actor="tiger", verb="is_rough") -> activity_21 : TERM
    TERM activity(actor="tiger", object=animal_label::mouse, verb="like") -> activity_22 : TERM
    TERM conjunction(items=[activity_21, activity_22]) -> conjunction_3 : TERM
    TERM activity(actor="mouse", object=animal_label::eagle, verb="like") -> activity_23 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_23) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM
    TERM activity(actor="something", object=animal_label::eagle, verb="like") -> activity_24 : TERM
    TERM activity(actor="bald_eagle", verb="is_kind") -> activity_25 : TERM
    TERM conjunction(items=[activity_24, activity_25]) -> conjunction_4 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::mouse, verb="see") -> activity_26 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_26) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_19 : CLAIM
    TERM activity(actor="mouse", object=animal_label::eagle, verb="see") -> activity_27 : TERM
    TERM activity(actor="mouse", object=animal_label::rabbit, verb="like") -> activity_28 : TERM
    TERM conditional(condition=activity_27, consequence=activity_28) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_20 : CLAIM
    TERM activity(actor="something", verb="is_kind") -> activity_29 : TERM
    TERM activity(actor="something", object=animal_label::eagle, verb="like") -> activity_30 : TERM
    TERM conjunction(items=[activity_29, activity_30]) -> conjunction_5 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::tiger, verb="like") -> activity_31 : TERM
    TERM conditional(condition=conjunction_5, consequence=activity_31) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_21 : CLAIM
    TERM activity(actor="something", object=animal_label::eagle, verb="like") -> activity_32 : TERM
    TERM activity(actor="something", verb="is_kind") -> activity_33 : TERM
    TERM conditional(condition=activity_32, consequence=activity_33) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_22 : CLAIM
    TERM activity(actor="something", object=animal_label::tiger, verb="see") -> activity_34 : TERM
    TERM activity(actor="something", verb="is_rough") -> activity_35 : TERM
    TERM conditional(condition=activity_34, consequence=activity_35) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_23 : CLAIM
    TERM activity(actor="something", verb="is_rough") -> activity_36 : TERM
    TERM activity(actor="something", object=animal_label::eagle, verb="like") -> activity_37 : TERM
    TERM conditional(condition=activity_36, consequence=activity_37) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s24" -> statement_24 : CLAIM
    TERM requirement(property="theory_only", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="choice_options", value="true_false_unknown") -> requirement_3 : TERM
    TERM activity(actor="mouse", verb="is_kind") -> activity_38 : TERM
    TERM negation(target=activity_38) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s26" -> statement_25 : CLAIM
    UTTER ask(target=negation_2, constraints=[requirement_2, requirement_3])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement, activity, conditional | covered |
| n2 | claim | statement, activity | covered |
| n3 | object | animal_label::eagle | label-preserved |
| n4 | object | animal_label::rabbit | label-preserved |
| n5 | claim | statement, activity | covered |
| n6 | claim | statement, activity | covered |
| n7 | object | animal_label::tiger | label-preserved |
| n8 | claim | statement, activity | covered |
| n9 | claim | statement, activity | covered |
| n10 | object | animal_label::mouse | label-preserved |
| n11 | claim | statement, activity | covered |
| n12 | claim | statement, activity | covered |
| n13 | claim | statement, activity | covered |
| n14 | claim | statement, activity | covered |
| n15 | claim | statement, activity | covered |
| n16 | claim | statement, activity, lexical_label | covered |
| n17 | constraint | color_label::red | label-preserved |
| n18 | claim | statement, activity | covered |
| n19 | claim | statement, activity | covered |
| n20 | claim | statement, activity | covered |
| n21 | reasoning | conditional, statement, activity | covered |
| n22 | reasoning | conditional, conjunction, statement, activity | covered |
| n23 | reasoning | conditional, conjunction, statement, activity | covered |
| n24 | reasoning | conditional, conjunction, statement, activity | covered |
| n25 | reasoning | conditional, statement, activity | covered |
| n26 | reasoning | conditional, conjunction, statement, activity | covered |
| n27 | reasoning | conditional, statement, activity | covered |
| n28 | reasoning | conditional, statement, activity | covered |
| n29 | reasoning | conditional, statement, activity | covered |
| n30 | speech_act | ask, statement | covered |
| n31 | constraint | requirement | covered |
| n32 | constraint | requirement | covered |
| n33 | claim | statement, negation, activity | covered |
| n34 | negation | negation | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s26 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" -> animal_label::eagle, t1:s2 "rabbit" -> animal_label::rabbit, t1:s4 "tiger" -> animal_label::tiger, t1:s6 "mouse" -> animal_label::mouse, t1:s12 "red" -> color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: rag check reported 0 unresolved needs and 0 unknown symbols
