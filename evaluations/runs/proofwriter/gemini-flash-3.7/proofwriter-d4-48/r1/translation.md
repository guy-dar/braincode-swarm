Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="cold", subject="bald_eagle", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::bear, verb="see") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_2 : CLAIM
    CLAIM attribute_claim(property="size", subject="bear", value="big") BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="rough", subject="bear", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="rough", subject="dog", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_5 : CLAIM
    TERM activity(actor="dog", object=animal_label::bear, verb="visit") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_3 : CLAIM
    CLAIM attribute_claim(property="age", subject="lion", value="young") BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_6 : CLAIM
    TERM activity(actor="lion", object=animal_label::eagle, verb="like") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_4 : CLAIM
    TERM activity(actor="lion", object=animal_label::eagle, verb="see") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_5 : CLAIM
    TERM activity(actor="lion", object=animal_label::bear, verb="see") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_6 : CLAIM
    TERM activity(actor="lion", object=animal_label::bear, verb="visit") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_7 : CLAIM
    TERM activity(actor="lion", object=animal_label::dog, verb="visit") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_8 : CLAIM
    TERM activity(actor="something", object=animal_label::dog, verb="visit") -> activity_9 : TERM
    TERM activity(actor="dog", object=animal_label::lion, verb="see") -> activity_10 : TERM
    TERM conditional(condition=activity_9, consequence=activity_10) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_9 : CLAIM
    TERM activity(actor="something", object=animal_label::eagle, verb="like") -> activity_11 : TERM
    TERM activity(actor="it", object=animal_label::dog, verb="see") -> activity_12 : TERM
    TERM conditional(condition=activity_11, consequence=activity_12) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_10 : CLAIM
    TERM activity(actor="something", object=animal_label::lion, verb="like") -> activity_13 : TERM
    TERM activity(actor="it", object=animal_label::bear, verb="visit") -> activity_14 : TERM
    TERM conditional(condition=activity_13, consequence=activity_14) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_11 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    TERM subject(kind="bald_eagle", qualifier="cold") -> subject_2 : TERM
    TERM subject(kind="bald_eagle", qualifier=lexical_label_2) -> subject_3 : TERM
    TERM conditional(condition=subject_2, consequence=subject_3) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_12 : CLAIM
    TERM subject(kind="something", qualifier="rough") -> subject_4 : TERM
    TERM activity(actor="it", object=animal_label::bear, verb="see") -> activity_15 : TERM
    TERM conjunction(items=[subject_4, activity_15]) -> conjunction_2 : TERM
    TERM activity(actor="it", object=animal_label::lion, verb="visit") -> activity_16 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_16) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_13 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::lion, verb="visit") -> activity_17 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::lion, verb="like") -> activity_18 : TERM
    TERM conditional(condition=activity_17, consequence=activity_18) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_14 : CLAIM
    TERM subject(kind="something", qualifier=lexical_label_2) -> subject_5 : TERM
    TERM subject(kind="something", qualifier="rough") -> subject_6 : TERM
    TERM conditional(condition=subject_5, consequence=subject_6) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_15 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::lion, verb="like") -> activity_19 : TERM
    TERM negation(target=activity_19) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_16 : CLAIM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(target=negation_2, constraints=[constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, subject, conjunction | covered |
| n2 | claim | attribute_claim | covered |
| n3 | object | animal_label::eagle | label-preserved |
| n4 | claim | statement, activity | covered |
| n5 | object | animal_label::bear | label-preserved |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim | covered |
| n8 | claim | attribute_claim | covered |
| n9 | object | animal_label::dog | label-preserved |
| n10 | claim | statement, activity | covered |
| n11 | claim | attribute_claim | covered |
| n12 | object | animal_label::lion | label-preserved |
| n13 | claim | statement, activity | covered |
| n14 | claim | statement, activity | covered |
| n15 | claim | statement, activity | covered |
| n16 | claim | statement, activity | covered |
| n17 | claim | statement, activity | covered |
| n18 | reasoning | conditional, activity, statement | covered |
| n19 | reasoning | conditional, activity, statement | covered |
| n20 | reasoning | conditional, activity, statement | covered |
| n21 | reasoning | conditional, subject, statement | covered |
| n22 | constraint | lexical_label, color_label::red | label-preserved |
| n23 | reasoning | conditional, conjunction, activity, subject, statement | covered |
| n24 | reasoning | conditional, activity, statement | covered |
| n25 | reasoning | conditional, subject, statement | covered |
| n26 | speech_act | ask | covered |
| n27 | constraint | ask | covered |
| n28 | constraint | constraint_single_choice | covered |
| n29 | claim | statement, negation, activity | covered |
| n30 | negation | negation | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" → animal_label::eagle (label only; no sense resolved); t1:s3 "bear" → animal_label::bear (label only; no sense resolved); t1:s6 "dog" → animal_label::dog (label only; no sense resolved); t1:s8 "lion" → animal_label::lion (label only; no sense resolved); t1:s17 "red" → color_label::red (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
