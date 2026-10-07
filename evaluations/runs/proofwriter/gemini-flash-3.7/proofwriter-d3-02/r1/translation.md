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
    TERM lexical_label(value=animal_label::baldeagle) -> lexical_label_2 : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    CLAIM attribute_claim(property="color", subject=lexical_label_2, value=lexical_label_3) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_4 : TERM
    CLAIM attribute_claim(property="color", subject=lexical_label_2, value=lexical_label_4) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    TERM lexical_label(value=animal_label::cow) -> lexical_label_5 : TERM
    CLAIM attribute_claim(property="nice", subject=lexical_label_5, value=TRUE) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    TERM lexical_label(value=animal_label::tiger) -> lexical_label_6 : TERM
    TERM activity(actor="cow", object=animal_label::tiger, verb="like") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_2 : CLAIM
    CLAIM meets_needs(beneficiary=lexical_label_5, subject=lexical_label_6) BY role_user STATUS asserted SOURCE "t1:s6" -> meets_needs_2 : CLAIM
    TERM lexical_label(value=animal_label::mouse) -> lexical_label_7 : TERM
    CLAIM attribute_claim(property="nice", subject=lexical_label_7, value=TRUE) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_5 : CLAIM
    CLAIM meets_needs(beneficiary=lexical_label_7, subject=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s8" -> meets_needs_3 : CLAIM
    TERM activity(actor="mouse", object=animal_label::baldeagle, verb="see") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_3 : CLAIM
    TERM activity(actor="tiger", object=animal_label::baldeagle, verb="like") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_4 : CLAIM
    CLAIM meets_needs(beneficiary=lexical_label_6, subject=lexical_label_5) BY role_user STATUS asserted SOURCE "t1:s11" -> meets_needs_4 : CLAIM
    CLAIM meets_needs(beneficiary=lexical_label_6, subject=lexical_label_7) BY role_user STATUS asserted SOURCE "t1:s12" -> meets_needs_5 : CLAIM
    TERM character_trait(property="age", value="young") -> character_trait_2 : TERM
    TERM activity(actor="someone", object=animal_label::tiger, verb="need") -> activity_5 : TERM
    TERM conditional(condition=character_trait_2, consequence=activity_5) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_5 : CLAIM
    TERM activity(actor="tiger", object=animal_label::tiger, verb="young") -> activity_6 : TERM
    TERM conditional(condition=activity_6, consequence=lexical_label_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_6 : CLAIM
    TERM activity(actor="tiger", object=animal_label::baldeagle, verb="see") -> activity_7 : TERM
    TERM conditional(condition=activity_5, consequence=activity_7) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_7 : CLAIM
    TERM activity(actor="someone", object=animal_label::tiger, verb="see") -> activity_8 : TERM
    TERM conjunction(items=[activity_8, activity_4]) -> conjunction_2 : TERM
    TERM activity(actor="baldeagle", object=animal_label::tiger, verb="see") -> activity_9 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_9) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_8 : CLAIM
    TERM activity(actor="someone", object=animal_label::baldeagle, verb="see") -> activity_10 : TERM
    TERM conjunction(items=[lexical_label_3, activity_10]) -> conjunction_3 : TERM
    TERM character_trait(property="temperature", value=state_cold) -> character_trait_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=character_trait_3) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_9 : CLAIM
    TERM activity(actor="someone", object=animal_label::tiger, verb="like") -> activity_11 : TERM
    TERM conjunction(items=[lexical_label_3, activity_11]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_10) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_10 : CLAIM
    TERM conditional(condition=character_trait_3, consequence=character_trait_2) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_11 : CLAIM
    TERM conditional(condition=activity_5, consequence=activity_11) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_12 : CLAIM
    TERM activity(actor="someone", object=animal_label::mouse, verb="need") -> activity_12 : TERM
    TERM conditional(condition=activity_12, consequence=lexical_label_3) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_13 : CLAIM
    TERM requirement(property="context", value="theory_only") -> requirement_2 : TERM
    TERM requirement(property="allowed_answers", value="true_false_unknown") -> requirement_3 : TERM
    TERM property_question(property="truth_value", subject=activity_6) -> property_question_2 : TERM
    UTTER ask(target=property_question_2, constraints=[requirement_2, requirement_3])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject, inform | covered |
| n2 | object | animal_label::baldeagle, lexical_label | label-preserved |
| n3 | object | color_label::green, lexical_label | label-preserved |
| n4 | claim | attribute_claim, lexical_label | covered |
| n5 | object | color_label::red, lexical_label | label-preserved |
| n6 | claim | attribute_claim, lexical_label | covered |
| n7 | object | animal_label::cow, lexical_label | label-preserved |
| n8 | claim | attribute_claim, lexical_label | covered |
| n9 | object | animal_label::tiger, lexical_label | label-preserved |
| n10 | claim | statement, activity, animal_label::tiger | covered |
| n11 | claim | meets_needs, lexical_label | covered |
| n12 | object | animal_label::mouse, lexical_label | label-preserved |
| n13 | claim | attribute_claim, lexical_label | covered |
| n14 | claim | meets_needs, lexical_label | covered |
| n15 | claim | statement, activity, animal_label::baldeagle | covered |
| n16 | claim | statement, activity, animal_label::baldeagle | covered |
| n17 | claim | meets_needs, lexical_label | covered |
| n18 | claim | meets_needs, lexical_label | covered |
| n19 | reasoning | statement, conditional, character_trait, activity, animal_label::tiger | covered |
| n20 | reasoning | statement, conditional, activity, lexical_label | covered |
| n21 | reasoning | statement, conditional, activity, animal_label::baldeagle, animal_label::tiger | covered |
| n22 | reasoning | statement, conditional, conjunction, activity, animal_label::baldeagle, animal_label::tiger | covered |
| n23 | reasoning | statement, conditional, conjunction, character_trait, state_cold, activity, animal_label::baldeagle, lexical_label | covered |
| n24 | reasoning | statement, conditional, conjunction, activity, animal_label::baldeagle, animal_label::tiger, lexical_label | label-preserved |
| n25 | reasoning | statement, conditional, character_trait, state_cold | covered |
| n26 | reasoning | statement, conditional, activity, animal_label::tiger | covered |
| n27 | reasoning | statement, conditional, activity, animal_label::mouse, lexical_label | covered |
| n28 | speech_act | ask, property_question, requirement | covered |
| n29 | constraint | requirement | covered |
| n30 | constraint | requirement | covered |
| n31 | action | property_question, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s23 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" -> animal_label::baldeagle; t1:s2 "green" -> color_label::green; t1:s3 "red" -> color_label::red; t1:s4 "cow" -> animal_label::cow; t1:s5 "tiger" -> animal_label::tiger; t1:s7 "mouse" -> animal_label::mouse
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
