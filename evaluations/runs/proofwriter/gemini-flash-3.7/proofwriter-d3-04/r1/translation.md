Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM character_trait(property="size", value=size_large) -> character_trait_2 : TERM
    TERM character_trait(property="sound", value="quiet") -> character_trait_3 : TERM
    TERM character_trait(property="intelligence", value="smart") -> character_trait_4 : TERM
    TERM character_trait(property="temperature", value=state_cold) -> character_trait_5 : TERM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    TERM lexical_label(value=color_label::red) -> lexical_label_3 : TERM
    TERM lexical_label(value=color_label::white) -> lexical_label_4 : TERM
    TERM subject(kind="Anne", qualifier=character_trait_2) -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM subject(kind="Anne", qualifier=character_trait_3) -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM subject(kind="Anne", qualifier=character_trait_4) -> subject_4 : TERM
    TERM negation(target=subject_4) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM subject(kind="Bob", qualifier=lexical_label_2) -> subject_5 : TERM
    CLAIM statement(fact=subject_5) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM subject(kind="Bob", qualifier=character_trait_3) -> subject_6 : TERM
    CLAIM statement(fact=subject_6) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM subject(kind="Dave", qualifier=lexical_label_2) -> subject_7 : TERM
    CLAIM statement(fact=subject_7) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM subject(kind="Fiona", qualifier=character_trait_2) -> subject_8 : TERM
    CLAIM statement(fact=subject_8) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM subject(kind="Fiona", qualifier=character_trait_5) -> subject_9 : TERM
    CLAIM statement(fact=subject_9) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM subject(kind="Fiona", qualifier=character_trait_3) -> subject_10 : TERM
    CLAIM statement(fact=subject_10) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM subject(kind="Fiona", qualifier=character_trait_4) -> subject_11 : TERM
    CLAIM statement(fact=subject_11) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM subject(kind="people", qualifier=character_trait_4) -> subject_12 : TERM
    TERM subject(kind="people", qualifier=character_trait_2) -> subject_13 : TERM
    TERM conditional(condition=subject_12, consequence=subject_13) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM conjunction(items=[lexical_label_2, lexical_label_3]) -> conjunction_2 : TERM
    TERM subject(kind="people", qualifier=conjunction_2) -> subject_14 : TERM
    TERM conditional(condition=subject_14, consequence=subject_13) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM negation(target=lexical_label_2) -> negation_3 : TERM
    TERM conjunction(items=[character_trait_5, negation_3]) -> conjunction_3 : TERM
    TERM subject(kind="someone", qualifier=conjunction_3) -> subject_15 : TERM
    TERM subject(kind="someone", qualifier=lexical_label_3) -> subject_16 : TERM
    TERM conditional(condition=subject_15, consequence=subject_16) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM subject(kind="people", qualifier=character_trait_5) -> subject_17 : TERM
    TERM conditional(condition=subject_17, consequence=subject_12) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM subject(kind="people", qualifier=lexical_label_2) -> subject_18 : TERM
    TERM conditional(condition=subject_18, consequence=subject_17) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM subject(kind="Bob", qualifier=character_trait_2) -> subject_19 : TERM
    TERM subject(kind="Bob", qualifier=character_trait_5) -> subject_20 : TERM
    TERM subject(kind="Bob", qualifier=lexical_label_3) -> subject_21 : TERM
    TERM negation(target=subject_21) -> negation_4 : TERM
    TERM conjunction(items=[subject_19, subject_20]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=negation_4) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM negation(target=lexical_label_3) -> negation_5 : TERM
    TERM conjunction(items=[character_trait_4, negation_5]) -> conjunction_5 : TERM
    TERM subject(kind="someone", qualifier=conjunction_5) -> subject_22 : TERM
    TERM subject(kind="someone", qualifier=lexical_label_4) -> subject_23 : TERM
    TERM conditional(condition=subject_22, consequence=subject_23) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM
    TERM test_condition(condition="theory_evaluation", expected=TRUE) -> test_condition_2 : TERM
    TERM decision(activity=test_condition_2) -> decision_2 : TERM
    UTTER ask(target=subject_19, constraints=[decision_2, test_condition_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, conditional, subject | covered |
| n2 | claim | character_trait, size_large, statement, subject | covered |
| n3 | claim | character_trait, statement, subject | covered |
| n4 | claim | character_trait, statement, subject | covered |
| n5 | negation | ask, negation | covered |
| n6 | claim | color_label, lexical_label, statement, subject | covered |
| n7 | object | color_label::blue | label-preserved |
| n8 | claim | character_trait, statement, subject | covered |
| n9 | claim | color_label, lexical_label, statement, subject | covered |
| n10 | object | color_label::blue | label-preserved |
| n11 | claim | character_trait, size_large, statement, subject | covered |
| n12 | claim | character_trait, state_cold, statement, subject | covered |
| n13 | claim | character_trait, statement, subject | covered |
| n14 | claim | character_trait, statement, subject, test_condition | covered |
| n15 | claim | character_trait, conditional, size_large, statement, subject | covered |
| n16 | claim | color_label, conditional, conjunction, lexical_label, size_large, statement, subject | covered |
| n17 | object | color_label::blue | label-preserved |
| n18 | object | color_label::red | label-preserved |
| n19 | claim | color_label, conditional, conjunction, lexical_label, negation, state_cold, statement, subject | covered |
| n20 | negation | color_label, negation | covered |
| n21 | object | color_label::blue | label-preserved |
| n22 | object | color_label::red | label-preserved |
| n23 | claim | character_trait, conditional, state_cold, statement, subject | covered |
| n24 | claim | character_trait, color_label, conditional, lexical_label, state_cold, statement, subject | covered |
| n25 | object | color_label::blue | label-preserved |
| n26 | claim | character_trait, color_label, conditional, conjunction, lexical_label, negation, state_cold, statement, subject | covered |
| n27 | negation | color_label, negation | covered |
| n28 | object | color_label::red | label-preserved |
| n29 | claim | character_trait, color_label, conditional, conjunction, lexical_label, negation, statement, subject | covered |
| n30 | negation | color_label, negation, state_cold | covered |
| n31 | object | color_label::red | label-preserved |
| n32 | object | color_label::white | label-preserved |
| n33 | action | ask, conditional, decision, statement, test_condition | covered |
| n34 | constraint | decision, subject, test_condition | covered |
| n35 | constraint | decision, test_condition | covered |
| n36 | object | character_trait, size_large, statement, subject | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s20 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s5 "blue" -> color_label::blue; t1:s7 "blue" -> color_label::blue; t1:s13 "blue" -> color_label::blue; t1:s13 "red" -> color_label::red; t1:s14 "blue" -> color_label::blue; t1:s14 "red" -> color_label::red; t1:s16 "blue" -> color_label::blue; t1:s17 "red" -> color_label::red; t1:s18 "red" -> color_label::red; t1:s18 "white" -> color_label::white
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
