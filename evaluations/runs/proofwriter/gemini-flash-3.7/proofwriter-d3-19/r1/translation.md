Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="bald eagle", object=animal_label::lion, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM requirement(property="color", value=color_label::green) -> requirement_2 : TERM
    TERM negation(target=requirement_2) -> negation_2 : TERM
    CLAIM possesses(item=requirement_2, subject="bald eagle", value=FALSE) BY role_user STATUS asserted SOURCE "t1:s3" -> possesses_2 : CLAIM
    TERM requirement(property="shape", value=shape_round) -> requirement_3 : TERM
    CLAIM possesses(item=requirement_3, subject="bald eagle", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s4" -> possesses_3 : CLAIM
    TERM activity(actor="bald eagle", object=animal_label::lion, verb="like") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_3 : CLAIM
    TERM requirement(property="color", value=color_label::red) -> requirement_4 : TERM
    CLAIM possesses(item=requirement_4, subject="dog", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s6" -> possesses_4 : CLAIM
    TERM activity(actor="lion", object=animal_label::dog, verb="chase") -> activity_4 : TERM
    TERM negation(target=activity_4) -> negation_3 : TERM
    CLAIM statement(fact=negation_3) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_4 : CLAIM
    CLAIM possesses(item=requirement_3, subject="lion", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s8" -> possesses_5 : CLAIM
    TERM requirement(property="age", value="young") -> requirement_5 : TERM
    CLAIM possesses(item=requirement_5, subject="lion", value=FALSE) BY role_user STATUS asserted SOURCE "t1:s9" -> possesses_6 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::dog, verb="chase") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_5 : CLAIM
    TERM activity(actor="rabbit", object=animal_label::lion, verb="eat") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_6 : CLAIM
    TERM activity(actor="something", object=animal_label::dog, verb="chase") -> activity_7 : TERM
    TERM activity(actor="something", object=animal_label::rabbit, verb="like") -> activity_8 : TERM
    TERM conditional(condition=activity_7, consequence=activity_8) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_7 : CLAIM
    TERM activity(actor="something", object=animal_label::lion, verb="chase") -> activity_9 : TERM
    TERM conjunction(items=[requirement_4, activity_9]) -> conjunction_2 : TERM
    TERM activity(actor="lion", object=animal_label::baldeagle, verb="like") -> activity_10 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_10) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_8 : CLAIM
    TERM requirement(property="size", value=size_large) -> requirement_6 : TERM
    TERM activity(actor="something", object=animal_label::rabbit, verb="chase") -> activity_11 : TERM
    TERM conditional(condition=requirement_6, consequence=activity_11) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_9 : CLAIM
    TERM activity(actor="something", object=animal_label::baldeagle, verb="chase") -> activity_12 : TERM
    TERM conjunction(items=[requirement_3, activity_12]) -> conjunction_3 : TERM
    TERM activity(actor="bald eagle", object=animal_label::dog, verb="like") -> activity_13 : TERM
    TERM negation(target=activity_13) -> negation_4 : TERM
    TERM conditional(condition=conjunction_3, consequence=negation_4) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_10 : CLAIM
    TERM activity(actor="something", object=animal_label::lion, verb="like") -> activity_14 : TERM
    TERM conditional(condition=activity_14, consequence=requirement_4) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_11 : CLAIM
    TERM conjunction(items=[requirement_4, requirement_3]) -> conjunction_4 : TERM
    TERM negation(target=activity_12) -> negation_5 : TERM
    TERM conditional(condition=conjunction_4, consequence=negation_5) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_12 : CLAIM
    TERM conjunction(items=[requirement_4, requirement_5]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=activity_12) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_13 : CLAIM
    TERM activity(actor="something", object=animal_label::baldeagle, verb="like") -> activity_15 : TERM
    TERM conjunction(items=[activity_15, activity_2]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=activity_14) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_14 : CLAIM
    TERM activity(actor="something", object=animal_label::baldeagle, verb="eat") -> activity_16 : TERM
    TERM conditional(condition=activity_16, consequence=requirement_4) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_15 : CLAIM
    TERM activity(actor="lion", object=animal_label::lion, verb="like") -> activity_17 : TERM
    TERM negation(target=activity_17) -> negation_6 : TERM
    CLAIM statement(fact=negation_6) BY role_user STATUS hypothesized SOURCE "t1:s22" -> statement_16 : CLAIM
    TERM requirement(property="premise_only", value=TRUE) -> requirement_7 : TERM
    UTTER ask(target=negation_6, constraints=[requirement_7])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement | covered |
| n2 | object | animal_label::baldeagle | label-preserved |
| n3 | object | animal_label::lion | label-preserved |
| n4 | action | activity | covered |
| n5 | claim | statement | covered |
| n6 | constraint | color_label::green | label-preserved |
| n7 | negation | negation | covered |
| n8 | claim | possesses | covered |
| n9 | constraint | shape_round | covered |
| n10 | claim | possesses | covered |
| n11 | action | activity | covered |
| n12 | claim | statement | covered |
| n13 | object | animal_label::dog | label-preserved |
| n14 | constraint | color_label::red | label-preserved |
| n15 | claim | possesses | covered |
| n16 | negation | negation | covered |
| n17 | claim | statement | covered |
| n18 | claim | possesses | covered |
| n19 | constraint | requirement | covered |
| n20 | negation | possesses | covered |
| n21 | claim | possesses | covered |
| n22 | object | animal_label::rabbit | label-preserved |
| n23 | claim | statement | covered |
| n24 | action | activity | covered |
| n25 | claim | statement | covered |
| n26 | reasoning | conditional | covered |
| n27 | reasoning | conditional, conjunction | covered |
| n28 | constraint | size_large | covered |
| n29 | reasoning | conditional | covered |
| n30 | reasoning | conditional, conjunction, negation | covered |
| n31 | reasoning | conditional | covered |
| n32 | reasoning | conditional, conjunction, negation | covered |
| n33 | reasoning | conditional, conjunction | covered |
| n34 | reasoning | conditional, conjunction | covered |
| n35 | reasoning | conditional | covered |
| n36 | speech_act | ask | covered |
| n37 | constraint | requirement | covered |
| n38 | negation | negation | covered |
| n39 | claim | statement | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" → animal_label::baldeagle; t1:s2 "lion" → animal_label::lion; t1:s3 "green" → color_label::green; t1:s6 "dog" → animal_label::dog; t1:s6 "red" → color_label::red; t1:s10 "rabbit" → animal_label::rabbit (open-group labels only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
