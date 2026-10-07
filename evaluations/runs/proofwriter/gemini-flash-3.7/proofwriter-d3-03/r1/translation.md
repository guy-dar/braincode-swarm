Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    TERM activity(actor="bald_eagle", verb="kind") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::bear, verb="need") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM activity(actor="bear", verb="kind") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM activity(actor="lion", object=animal_label::bear, verb="need") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM activity(actor="squirrel", verb="kind") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::eagle, verb="need") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::lion, verb="visit") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM activity(actor="someone", object=lexical_label_2, verb="is") -> activity_9 : TERM
    TERM activity(actor="someone", verb="rough") -> activity_10 : TERM
    TERM conjunction(items=[activity_9, activity_10]) -> conjunction_2 : TERM
    TERM activity(actor="someone", object=animal_label::bear, verb="need") -> activity_11 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_11) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM activity(actor="someone", object=animal_label::eagle, verb="need") -> activity_12 : TERM
    TERM activity(actor="someone", object=lexical_label_2, verb="is") -> activity_13 : TERM
    TERM conditional(condition=activity_12, consequence=activity_13) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM activity(actor="someone", object=animal_label::lion, verb="need") -> activity_14 : TERM
    TERM activity(actor="someone", object=animal_label::lion, verb="eat") -> activity_15 : TERM
    TERM conditional(condition=activity_14, consequence=activity_15) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM activity(actor="someone", object=animal_label::bear, verb="eat") -> activity_16 : TERM
    TERM activity(actor="bear", verb="kind") -> activity_17 : TERM
    TERM conditional(condition=activity_16, consequence=activity_17) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM activity(actor="someone", object=lexical_label_2, verb="is") -> activity_18 : TERM
    TERM activity(actor="someone", object=animal_label::bear, verb="visit") -> activity_19 : TERM
    TERM conditional(condition=activity_18, consequence=activity_19) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM activity(actor="lion", verb="rough") -> activity_20 : TERM
    TERM activity(actor="lion", object=animal_label::squirrel, verb="eat") -> activity_21 : TERM
    TERM conjunction(items=[activity_20, activity_21]) -> conjunction_3 : TERM
    TERM activity(actor="lion", object=lexical_label_2, verb="is") -> activity_22 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_22) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM activity(actor="someone", object=lexical_label_2, verb="is") -> activity_23 : TERM
    TERM activity(actor="someone", object=animal_label::bear, verb="visit") -> activity_24 : TERM
    TERM conjunction(items=[activity_23, activity_24]) -> conjunction_4 : TERM
    TERM activity(actor="bear", object=animal_label::eagle, verb="need") -> activity_25 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_25) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM requirement(property="basis", value="provided_theory") -> requirement_2 : TERM
    TERM requirement(property="allowed_answers", value="true_false_unknown") -> requirement_3 : TERM
    TERM activity(actor="bear", object=animal_label::eagle, verb="need") -> activity_26 : TERM
    CLAIM statement(fact=activity_26) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_16 : CLAIM
    TERM property_question(property="truth_value", subject=statement_16) -> property_question_2 : TERM
    UTTER ask(target=property_question_2, constraints=[requirement_2, requirement_3])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | claim | statement, activity | covered |
| n3 | object | animal_label::eagle | label-preserved |
| n4 | claim | statement, activity | covered |
| n5 | object | animal_label::eagle | label-preserved |
| n6 | object | animal_label::bear | label-preserved |
| n7 | claim | statement, activity | covered |
| n8 | object | animal_label::bear | label-preserved |
| n9 | claim | statement, activity | covered |
| n10 | object | animal_label::lion | label-preserved |
| n11 | object | animal_label::bear | label-preserved |
| n12 | claim | statement, activity | covered |
| n13 | object | animal_label::squirrel | label-preserved |
| n14 | claim | statement, activity | covered |
| n15 | object | animal_label::squirrel | label-preserved |
| n16 | object | animal_label::eagle | label-preserved |
| n17 | claim | statement, activity | covered |
| n18 | object | animal_label::squirrel | label-preserved |
| n19 | object | animal_label::lion | label-preserved |
| n20 | claim | statement, conditional, conjunction, activity | covered |
| n21 | object | color_label::blue, lexical_label | label-preserved |
| n22 | object | animal_label::bear | label-preserved |
| n23 | claim | statement, conditional, activity | covered |
| n24 | object | animal_label::eagle | label-preserved |
| n25 | object | color_label::blue, lexical_label | label-preserved |
| n26 | claim | statement, conditional, activity | covered |
| n27 | object | animal_label::lion | label-preserved |
| n28 | claim | statement, conditional, activity | covered |
| n29 | object | animal_label::bear | label-preserved |
| n30 | claim | statement, conditional, activity | covered |
| n31 | object | color_label::blue, lexical_label | label-preserved |
| n32 | object | animal_label::bear | label-preserved |
| n33 | claim | statement, conditional, conjunction, activity | covered |
| n34 | object | animal_label::lion | label-preserved |
| n35 | object | animal_label::squirrel | label-preserved |
| n36 | object | color_label::blue, lexical_label | label-preserved |
| n37 | claim | statement, conditional, conjunction, activity | covered |
| n38 | object | color_label::blue, lexical_label | label-preserved |
| n39 | object | animal_label::bear | label-preserved |
| n40 | object | animal_label::eagle | label-preserved |
| n41 | speech_act | ask | covered |
| n42 | constraint | requirement | covered |
| n43 | constraint | requirement | covered |
| n44 | claim | statement, activity | covered |
| n45 | object | animal_label::bear | label-preserved |
| n46 | object | animal_label::eagle | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s17 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2, t1:s3, t1:s7, t1:s10, t1:s15, t1:s17 "bald eagle" → animal_label::eagle; t1:s3, t1:s4, t1:s5, t1:s9, t1:s12, t1:s13, t1:s15, t1:s17 "bear" → animal_label::bear; t1:s5, t1:s8, t1:s11, t1:s14 "lion" → animal_label::lion; t1:s6, t1:s7, t1:s8, t1:s14 "squirrel" → animal_label::squirrel; t1:s9, t1:s10, t1:s13, t1:s14, t1:s15 "blue" → color_label::blue
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
