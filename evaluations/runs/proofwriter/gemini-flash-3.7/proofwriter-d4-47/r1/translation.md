Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="baldeagle", object=animal_label::cat, verb="see") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM

    TERM requirement(property="shape", value=shape_round) -> requirement_2 : TERM
    CLAIM statement(fact=requirement_2) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM

    TERM activity(actor="cat", object=animal_label::rabbit, verb="need") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM

    TERM activity(actor="cat", object=animal_label::lion, verb="see") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM

    TERM activity(actor="cat", object=animal_label::lion, verb="visit") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM

    TERM requirement(property="size", value=size_large) -> requirement_3 : TERM
    CLAIM statement(fact=requirement_3) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM

    TERM requirement(property="state", value=state_cold) -> requirement_4 : TERM
    CLAIM statement(fact=requirement_4) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM

    TERM requirement(property="nice", value=TRUE) -> requirement_5 : TERM
    CLAIM statement(fact=requirement_5) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM

    TERM activity(actor="lion", object=animal_label::rabbit, verb="visit") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM

    TERM requirement(property="nice", value=TRUE) -> requirement_6 : TERM
    CLAIM statement(fact=requirement_6) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM

    TERM requirement(property="shape", value=shape_round) -> requirement_7 : TERM
    CLAIM statement(fact=requirement_7) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM

    TERM activity(actor="rabbit", object=animal_label::cat, verb="see") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM

    TERM conditional(condition=requirement_5, consequence=requirement_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM

    TERM requirement(property="kind", value=TRUE) -> requirement_8 : TERM
    TERM activity(actor="something", object=animal_label::rabbit, verb="see") -> activity_8 : TERM
    TERM conjunction(items=[requirement_8, activity_8]) -> conjunction_2 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="need") -> activity_9 : TERM
    CLAIM leads_to(cause=conjunction_2, effect=activity_9) BY role_user STATUS asserted SOURCE "t1:s15" -> leads_to_2 : CLAIM

    TERM activity(actor="something", object=animal_label::rabbit, verb="need") -> activity_10 : TERM
    TERM conditional(condition=activity_10, consequence=requirement_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_15 : CLAIM

    TERM conjunction(items=[requirement_4, requirement_3]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_8) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_16 : CLAIM

    TERM activity(actor="something", object=animal_label::baldeagle, verb="see") -> activity_11 : TERM
    TERM conjunction(items=[activity_11, requirement_5]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_10) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_17 : CLAIM

    TERM activity(actor="something", object=animal_label::lion, verb="see") -> activity_12 : TERM
    TERM activity(actor="something", object=animal_label::rabbit, verb="visit") -> activity_13 : TERM
    CLAIM leads_to(cause=activity_12, effect=activity_13) BY role_user STATUS asserted SOURCE "t1:s19" -> leads_to_3 : CLAIM

    TERM activity(actor="baldeagle", object=animal_label::rabbit, verb="visit") -> activity_14 : TERM
    TERM conditional(condition=activity_2, consequence=activity_14) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_18 : CLAIM

    TERM conditional(condition=activity_13, consequence=activity_10) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_19 : CLAIM

    TERM conditional(condition=requirement_3, consequence=requirement_4) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_20 : CLAIM

    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM requirement(property="theory_only", value=TRUE) -> requirement_9 : TERM
    TERM subject(kind="baldeagle", qualifier=requirement_3) -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY role_user STATUS hypothesized SOURCE "t1:s24" -> statement_21 : CLAIM
    UTTER ask(target=statement_21, constraints=[constraint_single_choice_2, requirement_9])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, statement, activity | covered |
| n2 | claim | statement, activity, animal_label::cat | covered |
| n3 | object | animal_label::baldeagle | label-preserved |
| n4 | object | animal_label::cat | label-preserved |
| n5 | claim | statement, requirement, shape_round | covered |
| n6 | object | animal_label::cat | label-preserved |
| n7 | claim | statement, activity, animal_label::rabbit | covered |
| n8 | object | animal_label::cat | label-preserved |
| n9 | object | animal_label::rabbit | label-preserved |
| n10 | claim | statement, activity, animal_label::lion | covered |
| n11 | object | animal_label::cat | label-preserved |
| n12 | object | animal_label::lion | label-preserved |
| n13 | claim | statement, activity, animal_label::lion | covered |
| n14 | object | animal_label::cat | label-preserved |
| n15 | object | animal_label::lion | label-preserved |
| n16 | claim | statement, requirement, size_large | covered |
| n17 | object | animal_label::lion | label-preserved |
| n18 | claim | statement, requirement, state_cold | covered |
| n19 | object | animal_label::lion | label-preserved |
| n20 | claim | statement, requirement | covered |
| n21 | object | animal_label::lion | label-preserved |
| n22 | claim | statement, activity, animal_label::rabbit | covered |
| n23 | object | animal_label::lion | label-preserved |
| n24 | object | animal_label::rabbit | label-preserved |
| n25 | claim | statement, requirement | covered |
| n26 | object | animal_label::rabbit | label-preserved |
| n27 | claim | statement, requirement, shape_round | covered |
| n28 | object | animal_label::rabbit | label-preserved |
| n29 | claim | statement, activity, animal_label::cat | covered |
| n30 | object | animal_label::rabbit | label-preserved |
| n31 | object | animal_label::cat | label-preserved |
| n32 | claim | statement, conditional, requirement, size_large | covered |
| n33 | claim | leads_to, conjunction, activity, animal_label::rabbit, animal_label::lion | covered |
| n34 | claim | statement, conditional, activity, requirement | covered |
| n35 | claim | statement, conditional, conjunction, requirement, state_cold, size_large | covered |
| n36 | claim | statement, conditional, conjunction, activity, animal_label::baldeagle, requirement | covered |
| n37 | claim | leads_to, activity, animal_label::lion, animal_label::rabbit | covered |
| n38 | claim | statement, conditional, activity, animal_label::cat, animal_label::rabbit | covered |
| n39 | claim | statement, conditional, activity, animal_label::rabbit | covered |
| n40 | claim | statement, conditional, requirement, size_large, state_cold | covered |
| n41 | speech_act | ask, statement | covered |
| n42 | constraint | requirement | covered |
| n43 | constraint | constraint_single_choice | covered |
| n44 | claim | statement, subject, requirement, size_large | covered |
| n45 | object | animal_label::baldeagle | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2, t1:s18, t1:s20, t1:s24 "bald eagle" → animal_label::baldeagle; t1:s2, t1:s3, t1:s4, t1:s5, t1:s6, t1:s13, t1:s20 "cat" → animal_label::cat; t1:s4, t1:s10, t1:s11, t1:s12, t1:s13, t1:s15, t1:s16, t1:s18, t1:s19, t1:s20, t1:s21 "rabbit" → animal_label::rabbit; t1:s5, t1:s6, t1:s7, t1:s8, t1:s9, t1:s10, t1:s12, t1:s15, t1:s19 "lion" → animal_label::lion
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
