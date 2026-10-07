Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM has_attribute(attribute=state_cold, subject="Bob") BY role_user STATUS asserted SOURCE "t1:s2" -> has_attribute_2 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    CLAIM has_attribute(attribute=lexical_label_2, subject="Bob") BY role_user STATUS asserted SOURCE "t1:s3" -> has_attribute_3 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_3 : TERM
    CLAIM has_attribute(attribute=lexical_label_3, subject="Bob") BY role_user STATUS asserted SOURCE "t1:s4" -> has_attribute_4 : CLAIM
    CLAIM has_attribute(attribute=shape_round, subject="Bob") BY role_user STATUS asserted SOURCE "t1:s5" -> has_attribute_5 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_2, subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s6" -> has_attribute_6 : CLAIM
    CLAIM has_attribute(attribute="smart", subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s7" -> has_attribute_7 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_2, subject="Gary") BY role_user STATUS asserted SOURCE "t1:s8" -> has_attribute_8 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_3, subject="Gary") BY role_user STATUS asserted SOURCE "t1:s9" -> has_attribute_9 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_2, subject="Harry") BY role_user STATUS asserted SOURCE "t1:s10" -> has_attribute_10 : CLAIM
    CLAIM has_attribute(attribute="smart", subject="Harry") BY role_user STATUS asserted SOURCE "t1:s11" -> has_attribute_11 : CLAIM
    TERM subject(kind="person", qualifier="smart") -> subject_2 : TERM
    TERM subject(kind="person", qualifier=state_cold) -> subject_3 : TERM
    TERM conditional(condition=subject_2, consequence=subject_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_2 : CLAIM
    TERM subject(kind="person", qualifier=lexical_label_3) -> subject_4 : TERM
    TERM subject(kind="person", qualifier="rough") -> subject_5 : TERM
    TERM conditional(condition=subject_4, consequence=subject_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_3 : CLAIM
    TERM subject(kind="person", qualifier="nice") -> subject_6 : TERM
    TERM conjunction(items=[subject_6, subject_4]) -> conjunction_2 : TERM
    TERM subject(kind="person", qualifier=lexical_label_2) -> subject_7 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_7) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_4 : CLAIM
    TERM conjunction(items=[subject_4, subject_5]) -> conjunction_3 : TERM
    TERM subject(kind="person", qualifier=shape_round) -> subject_8 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_8) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_5 : CLAIM
    TERM conjunction(items=[subject_5, subject_8]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_2) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_6 : CLAIM
    TERM character(name="Gary") -> character_2 : TERM
    TERM character_trait(property="smart", value="Gary") -> character_trait_2 : TERM
    TERM character_trait(property="cold", value="Gary") -> character_trait_3 : TERM
    TERM character_trait(property="nice", value="Gary") -> character_trait_4 : TERM
    TERM conjunction(items=[character_trait_2, character_trait_3]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=character_trait_4) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_7 : CLAIM
    TERM conjunction(items=[subject_7, subject_2]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=subject_4) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_8 : CLAIM
    CLAIM has_attribute(attribute=state_cold, subject="Gary") BY role_user STATUS hypothesized SOURCE "t1:s20" -> has_attribute_12 : CLAIM
    UTTER ask(target=has_attribute_12)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement | covered |
| n2 | claim | has_attribute, state_cold | covered |
| n3 | claim | has_attribute, lexical_label | covered |
| n4 | constraint | color_label::green | label-preserved |
| n5 | claim | has_attribute, lexical_label | covered |
| n6 | constraint | color_label::red | label-preserved |
| n7 | claim | has_attribute, shape_round | covered |
| n8 | claim | has_attribute, lexical_label | covered |
| n9 | constraint | color_label::green | label-preserved |
| n10 | claim | has_attribute | covered |
| n11 | claim | has_attribute, lexical_label | covered |
| n12 | constraint | color_label::green | label-preserved |
| n13 | claim | has_attribute, lexical_label | covered |
| n14 | constraint | color_label::red | label-preserved |
| n15 | claim | has_attribute, lexical_label | covered |
| n16 | constraint | color_label::green | label-preserved |
| n17 | claim | has_attribute | covered |
| n18 | reasoning | conditional, statement, state_cold, subject | covered |
| n19 | reasoning | conditional, lexical_label, statement, subject | covered |
| n20 | constraint | color_label::red | label-preserved |
| n21 | reasoning | conditional, conjunction, lexical_label, statement, subject | label-preserved |
| n22 | constraint | color_label::red | label-preserved |
| n23 | constraint | color_label::green | label-preserved |
| n24 | reasoning | conditional, conjunction, lexical_label, shape_round, statement, subject | covered |
| n25 | constraint | color_label::red | label-preserved |
| n26 | reasoning | conditional, conjunction, shape_round, statement, subject | covered |
| n27 | reasoning | conditional, conjunction, character_trait, statement | covered |
| n28 | reasoning | conditional, conjunction, lexical_label, statement, subject | label-preserved |
| n29 | constraint | color_label::green | label-preserved |
| n30 | constraint | color_label::red | label-preserved |
| n31 | speech_act | ask | covered |
| n32 | constraint | ask | not-applicable |
| n33 | constraint | ask | not-applicable |
| n34 | object | has_attribute, state_cold | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s20 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "green" -> color_label::green, t1:s4 "red" -> color_label::red, t1:s6 "green" -> color_label::green, t1:s8 "green" -> color_label::green, t1:s9 "red" -> color_label::red, t1:s10 "green" -> color_label::green, t1:s13 "red" -> color_label::red, t1:s14 "red" -> color_label::red, "green" -> color_label::green, t1:s15 "red" -> color_label::red, t1:s18 "green" -> color_label::green, "red" -> color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
