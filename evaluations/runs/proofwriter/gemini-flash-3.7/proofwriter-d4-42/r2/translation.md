Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    TERM lexical_label(value=animal_label::baldeagle) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="rough", subject=lexical_label_2, value=TRUE) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    TERM lexical_label(value=animal_label::dog) -> lexical_label_3 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::dog, verb="likes") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_2 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::dog, verb="visits") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_3 : CLAIM
    TERM lexical_label(value=animal_label::rabbit) -> lexical_label_4 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::rabbit, verb="visits") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_4 : CLAIM
    TERM activity(actor="dog", object=animal_label::baldeagle, verb="visits") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_5 : CLAIM
    TERM lexical_label(value=animal_label::mouse) -> lexical_label_5 : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_6 : TERM
    CLAIM attribute_claim(property="color", subject=lexical_label_5, value=lexical_label_6) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="shape", subject=lexical_label_5, value=shape_round) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_4 : CLAIM
    TERM activity(actor="mouse", object=animal_label::rabbit, verb="visits") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_6 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::baldeagle, verb="eats") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_7 : CLAIM
    CLAIM attribute_claim(property="rough", subject=lexical_label_4, value=TRUE) BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_5 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::baldeagle, verb="likes") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_8 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::mouse, verb="likes") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_9 : CLAIM
    TERM activity(actor="mouse", object=animal_label::dog, verb="visits") -> activity_10 : TERM
    TERM conjunction(items=[activity_6, activity_10]) -> conjunction_2 : TERM
    TERM activity(actor="mouse", object=animal_label::rabbit, verb="eats") -> activity_11 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_11) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_10 : CLAIM
    TERM requirement(property="rough", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="size", value=size_large) -> requirement_3 : TERM
    TERM conditional(condition=requirement_2, consequence=requirement_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_11 : CLAIM
    TERM activity(actor="something", object=animal_label::mouse, verb="likes") -> activity_12 : TERM
    TERM activity(actor="mouse", object=animal_label::rabbit, verb="likes") -> activity_13 : TERM
    TERM conjunction(items=[activity_12, activity_13]) -> conjunction_3 : TERM
    TERM activity(actor="something", object=animal_label::rabbit, verb="likes") -> activity_14 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_14) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_12 : CLAIM
    TERM activity(actor="something", object=animal_label::dog, verb="likes") -> activity_15 : TERM
    TERM activity(actor="something", object=animal_label::dog, verb="visits") -> activity_16 : TERM
    TERM conditional(condition=activity_15, consequence=activity_16) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_13 : CLAIM
    TERM activity(actor="something", object=animal_label::mouse, verb="visits") -> activity_17 : TERM
    TERM requirement(property="shape", value=shape_round) -> requirement_4 : TERM
    TERM conditional(condition=activity_17, consequence=requirement_4) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_14 : CLAIM
    TERM requirement(property="color", value=lexical_label_6) -> requirement_5 : TERM
    TERM conditional(condition=requirement_5, consequence=requirement_2) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_15 : CLAIM
    TERM conditional(condition=requirement_2, consequence=requirement_5) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_16 : CLAIM
    TERM conjunction(items=[requirement_3, requirement_5]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_15) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_17 : CLAIM
    TERM property_question(property="truth_value", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    CLAIM statement(fact=activity_10) BY role_user STATUS hypothesized SOURCE "t1:s23" -> statement_18 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject | covered |
| n2 | claim | attribute_claim | covered |
| n3 | object | lexical_label, animal_label::baldeagle | label-preserved |
| n4 | constraint | attribute_claim | covered |
| n5 | claim | statement, activity | covered |
| n6 | object | lexical_label, animal_label::baldeagle | label-preserved |
| n7 | object | lexical_label, animal_label::dog | label-preserved |
| n8 | action | activity | covered |
| n9 | claim | statement, activity | covered |
| n10 | object | lexical_label, animal_label::baldeagle | label-preserved |
| n11 | object | lexical_label, animal_label::dog | label-preserved |
| n12 | action | activity | covered |
| n13 | claim | statement, activity | covered |
| n14 | object | lexical_label, animal_label::baldeagle | label-preserved |
| n15 | object | lexical_label, animal_label::rabbit | label-preserved |
| n16 | action | activity | covered |
| n17 | claim | statement, activity | covered |
| n18 | object | lexical_label, animal_label::dog | label-preserved |
| n19 | object | lexical_label, animal_label::baldeagle | label-preserved |
| n20 | action | activity | covered |
| n21 | claim | attribute_claim | covered |
| n22 | object | lexical_label, animal_label::mouse | label-preserved |
| n23 | constraint | lexical_label, color_label::green | label-preserved |
| n24 | claim | attribute_claim, shape_round | covered |
| n25 | object | lexical_label, animal_label::mouse | label-preserved |
| n26 | constraint | shape_round | covered |
| n27 | claim | statement, activity | covered |
| n28 | object | lexical_label, animal_label::mouse | label-preserved |
| n29 | object | lexical_label, animal_label::rabbit | label-preserved |
| n30 | action | activity | covered |
| n31 | claim | statement, activity | covered |
| n32 | object | lexical_label, animal_label::rabbit | label-preserved |
| n33 | object | lexical_label, animal_label::baldeagle | label-preserved |
| n34 | action | activity | covered |
| n35 | claim | attribute_claim | covered |
| n36 | object | lexical_label, animal_label::rabbit | label-preserved |
| n37 | constraint | attribute_claim | covered |
| n38 | claim | statement, activity | covered |
| n39 | object | lexical_label, animal_label::rabbit | label-preserved |
| n40 | object | lexical_label, animal_label::baldeagle | label-preserved |
| n41 | action | activity | covered |
| n42 | claim | statement, activity | covered |
| n43 | object | lexical_label, animal_label::rabbit | label-preserved |
| n44 | object | lexical_label, animal_label::mouse | label-preserved |
| n45 | action | activity | covered |
| n46 | reasoning | conditional, conjunction, activity, statement | covered |
| n47 | reasoning | conditional, requirement, size_large, statement | covered |
| n48 | constraint | size_large | covered |
| n49 | reasoning | conditional, conjunction, activity, statement | covered |
| n50 | reasoning | conditional, activity, statement | covered |
| n51 | reasoning | conditional, activity, requirement, shape_round, statement | covered |
| n52 | reasoning | conditional, requirement, lexical_label, color_label::green, statement | covered |
| n53 | reasoning | conditional, requirement, lexical_label, color_label::green, statement | covered |
| n54 | reasoning | conditional, conjunction, requirement, size_large, activity, statement | covered |
| n55 | speech_act | ask, property_question | covered |
| n56 | constraint | subject | covered |
| n57 | constraint | property_question | covered |
| n58 | claim | statement, activity | covered |
| n59 | object | lexical_label, animal_label::mouse | label-preserved |
| n60 | object | lexical_label, animal_label::dog | label-preserved |
| n61 | action | activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s23 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" → animal_label::baldeagle, t1:s3 "dog" → animal_label::dog, t1:s5 "rabbit" → animal_label::rabbit, t1:s7 "mouse" → animal_label::mouse, t1:s7 "green" → color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: rag check reported 0 unresolved needs and 0 unknown symbols
