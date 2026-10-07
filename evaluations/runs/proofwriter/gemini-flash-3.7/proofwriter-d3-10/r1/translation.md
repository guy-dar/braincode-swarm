Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    UTTER inform(topic=subject_2)
    TERM activity(actor="bald_eagle", object=animal_label::dog, verb="chase") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::tiger, verb="chase") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="bald_eagle", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="texture", subject="bald_eagle", value="rough") BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_3 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::lion, verb="need") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_4 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::dog, verb="see") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_5 : CLAIM
    TERM activity(actor="dog", object=animal_label::lion, verb="chase") -> activity_6 : TERM
    TERM negation(target=activity_6) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_6 : CLAIM
    TERM character_trait(property="texture", value="rough") -> character_trait_2 : TERM
    TERM negation(target=character_trait_2) -> negation_3 : TERM
    CLAIM statement(fact=negation_3) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_7 : CLAIM
    TERM activity(actor="dog", object=animal_label::eagle, verb="see") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_8 : CLAIM
    TERM activity(actor="dog", object=animal_label::tiger, verb="see") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_9 : CLAIM
    CLAIM attribute_claim(property="texture", subject="lion", value="rough") BY role_user STATUS asserted SOURCE "t1:s12" -> attribute_claim_4 : CLAIM
    TERM activity(actor="lion", object=animal_label::eagle, verb="need") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_10 : CLAIM
    TERM activity(actor="lion", object=animal_label::dog, verb="need") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_11 : CLAIM
    TERM activity(actor="lion", object=animal_label::tiger, verb="need") -> activity_11 : TERM
    CLAIM statement(fact=activity_11) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_12 : CLAIM
    TERM activity(actor="lion", object=animal_label::eagle, verb="see") -> activity_12 : TERM
    CLAIM statement(fact=activity_12) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_13 : CLAIM
    CLAIM attribute_claim(property="color", subject="tiger", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s17" -> attribute_claim_5 : CLAIM
    TERM character_trait(property="shape", value=shape_round) -> character_trait_3 : TERM
    TERM conjunction(items=[activity_12, activity_3]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=character_trait_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_14 : CLAIM
    TERM activity(actor="someone", object=animal_label::lion, verb="see") -> activity_13 : TERM
    TERM activity(actor="lion", object=animal_label::dog, verb="chase") -> activity_14 : TERM
    TERM conjunction(items=[activity_13, activity_14]) -> conjunction_3 : TERM
    TERM activity(actor="dog", object=animal_label::lion, verb="need") -> activity_15 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_15) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_15 : CLAIM
    TERM character_trait(property="personality", value="kind") -> character_trait_4 : TERM
    TERM activity(actor="someone", object=animal_label::eagle, verb="chase") -> activity_16 : TERM
    TERM conjunction(items=[character_trait_4, activity_16]) -> conjunction_4 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::dog, verb="need") -> activity_17 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_17) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_16 : CLAIM
    TERM conjunction(items=[activity_13, character_trait_2]) -> conjunction_5 : TERM
    TERM activity(actor="someone", object=animal_label::lion, verb="chase") -> activity_18 : TERM
    TERM conditional(condition=conjunction_5, consequence=activity_18) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_17 : CLAIM
    TERM activity(actor="someone", object=animal_label::dog, verb="need") -> activity_19 : TERM
    TERM conjunction(items=[activity_19, character_trait_4]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=activity_7) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_18 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::lion, verb="chase") -> activity_20 : TERM
    TERM conjunction(items=[activity_7, activity_20]) -> conjunction_7 : TERM
    TERM character_trait(property="color", value="red") -> character_trait_5 : TERM
    TERM conditional(condition=conjunction_7, consequence=character_trait_5) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_19 : CLAIM
    TERM conjunction(items=[character_trait_5, character_trait_2]) -> conjunction_8 : TERM
    TERM conditional(condition=conjunction_8, consequence=activity_13) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s24" -> statement_20 : CLAIM
    TERM activity(actor="someone", object=animal_label::lion, verb="need") -> activity_21 : TERM
    TERM conditional(condition=activity_21, consequence=activity_10) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s25" -> statement_21 : CLAIM
    TERM character_trait(property="age", value="young") -> character_trait_6 : TERM
    TERM conditional(condition=character_trait_6, consequence=character_trait_2) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s26" -> statement_22 : CLAIM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM requirement(property="basis", value="theory") -> requirement_2 : TERM
    CLAIM attribute_claim(property="color", subject="lion", value=lexical_label_2) BY role_user STATUS hypothesized SOURCE "t1:s28" -> attribute_claim_6 : CLAIM
    UTTER ask(target=attribute_claim_6, constraints=[constraint_single_choice_2, requirement_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject, inform | covered |
| n2 | claim | activity, statement | covered |
| n3 | object | animal_label::eagle | label-preserved |
| n4 | object | animal_label::dog | label-preserved |
| n5 | claim | activity, statement | covered |
| n6 | object | animal_label::tiger | label-preserved |
| n7 | claim | lexical_label, attribute_claim | covered |
| n8 | constraint | color_label::red | label-preserved |
| n9 | claim | attribute_claim | covered |
| n10 | claim | activity, statement | covered |
| n11 | object | animal_label::lion | label-preserved |
| n12 | claim | activity, statement | covered |
| n13 | claim | activity, negation, statement | covered |
| n14 | negation | negation | covered |
| n15 | claim | character_trait, negation, statement | covered |
| n16 | negation | negation | covered |
| n17 | claim | activity, statement | covered |
| n18 | claim | activity, statement | covered |
| n19 | claim | attribute_claim | covered |
| n20 | claim | activity, statement | covered |
| n21 | claim | activity, statement | covered |
| n22 | claim | activity, statement | covered |
| n23 | claim | activity, statement | covered |
| n24 | claim | lexical_label, attribute_claim | covered |
| n25 | reasoning | character_trait, conjunction, conditional, statement | covered |
| n26 | reasoning | activity, conjunction, conditional, statement | covered |
| n27 | reasoning | character_trait, activity, conjunction, conditional, statement | covered |
| n28 | reasoning | conjunction, activity, conditional, statement | covered |
| n29 | reasoning | activity, conjunction, conditional, statement | covered |
| n30 | reasoning | activity, conjunction, character_trait, conditional, statement | covered |
| n31 | reasoning | conjunction, conditional, statement | covered |
| n32 | reasoning | activity, conditional, statement | covered |
| n33 | reasoning | character_trait, conditional, statement | covered |
| n34 | speech_act | ask | covered |
| n35 | constraint | requirement | covered |
| n36 | constraint | constraint_single_choice | covered |
| n37 | claim | lexical_label, attribute_claim | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s28 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" -> animal_label::eagle (label only; no sense resolved), t1:s2 "dog" -> animal_label::dog (label only; no sense resolved), t1:s3 "tiger" -> animal_label::tiger (label only; no sense resolved), t1:s4 "red" -> color_label::red (label only; no sense resolved), t1:s6 "lion" -> animal_label::lion (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
