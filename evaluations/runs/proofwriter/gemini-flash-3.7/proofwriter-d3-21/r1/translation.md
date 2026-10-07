Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM character(name="Bob") -> character_2 : TERM
    TERM character(name="Fiona") -> character_3 : TERM
    TERM character(name="Gary") -> character_4 : TERM
    TERM character(name="Harry") -> character_5 : TERM
    TERM lexical_label(value=color_label::white) -> lexical_label_2 : TERM
    TERM lexical_label(value=color_label::blue) -> lexical_label_3 : TERM
    TERM character_trait(property="color", value="white") -> character_trait_2 : TERM
    TERM character_trait(property="state", value=state_cold) -> character_trait_3 : TERM
    TERM character_trait(property="texture", value="rough") -> character_trait_4 : TERM
    TERM character_trait(property="size", value=size_large) -> character_trait_5 : TERM
    TERM character_trait(property="personality", value="nice") -> character_trait_6 : TERM
    TERM character_trait(property="texture", value="furry") -> character_trait_7 : TERM
    TERM character_trait(property="color", value="blue") -> character_trait_8 : TERM
    TERM subject(kind="Bob", qualifier=character_trait_2) -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM subject(kind="Fiona", qualifier=character_trait_3) -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM subject(kind="Fiona", qualifier=character_trait_4) -> subject_4 : TERM
    CLAIM statement(fact=subject_4) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM subject(kind="Gary", qualifier=character_trait_5) -> subject_5 : TERM
    CLAIM statement(fact=subject_5) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM subject(kind="Gary", qualifier=character_trait_4) -> subject_6 : TERM
    CLAIM statement(fact=subject_6) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM subject(kind="Gary", qualifier=character_trait_2) -> subject_7 : TERM
    CLAIM statement(fact=subject_7) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM subject(kind="Harry", qualifier=character_trait_6) -> subject_8 : TERM
    CLAIM statement(fact=subject_8) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM conjunction(items=[character_trait_2, character_trait_3]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=character_trait_8) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM subject(kind="Bob", qualifier=character_trait_6) -> subject_9 : TERM
    TERM subject(kind="Bob", qualifier=character_trait_7) -> subject_10 : TERM
    TERM conditional(condition=subject_9, consequence=subject_10) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM conjunction(items=[character_trait_5, character_trait_3]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=character_trait_8) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM subject(kind="Fiona", qualifier=character_trait_7) -> subject_11 : TERM
    TERM subject(kind="Fiona", qualifier=character_trait_2) -> subject_12 : TERM
    TERM conditional(condition=subject_11, consequence=subject_12) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM conditional(condition=character_trait_5, consequence=character_trait_3) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM subject(kind="Bob", qualifier=character_trait_8) -> subject_13 : TERM
    TERM conjunction(items=[subject_13, subject_9]) -> conjunction_4 : TERM
    TERM subject(kind="Bob", qualifier=character_trait_3) -> subject_14 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_14) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM conjunction(items=[character_trait_8, character_trait_3]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=character_trait_6) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM conditional(condition=character_trait_2, consequence=character_trait_5) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM negation(target=subject_13) -> negation_2 : TERM
    TERM requirement(property="context", value="theory") -> requirement_2 : TERM
    TERM requirement(property="allowed_answers", value="truth_value") -> requirement_3 : TERM
    UTTER ask(target=negation_2, constraints=[requirement_2, requirement_3])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | conditional, statement, subject | covered |
| n2 | claim | statement, subject | covered |
| n3 | object | character | covered |
| n4 | constraint | color_label::white | label-preserved |
| n5 | claim | character_trait, state_cold, statement | covered |
| n6 | object | character | covered |
| n7 | claim | character_trait, statement | covered |
| n8 | claim | size_large, statement | covered |
| n9 | object | character | covered |
| n10 | claim | statement | covered |
| n11 | claim | color_label::white, statement | covered |
| n12 | constraint | color_label::white | label-preserved |
| n13 | claim | statement | covered |
| n14 | object | character | covered |
| n15 | reasoning | conditional, conjunction, state_cold | covered |
| n16 | constraint | color_label::white | label-preserved |
| n17 | constraint | color_label::blue | label-preserved |
| n18 | reasoning | conditional, statement, subject | covered |
| n19 | reasoning | conditional, conjunction, size_large, state_cold | covered |
| n20 | constraint | color_label::blue | label-preserved |
| n21 | reasoning | conditional, statement | covered |
| n22 | constraint | color_label::white | label-preserved |
| n23 | reasoning | conditional, size_large, state_cold | covered |
| n24 | reasoning | conditional, conjunction, state_cold | covered |
| n25 | constraint | color_label::blue | label-preserved |
| n26 | reasoning | conditional, conjunction, state_cold | covered |
| n27 | constraint | color_label::blue | label-preserved |
| n28 | reasoning | conditional, size_large | covered |
| n29 | constraint | color_label::white | label-preserved |
| n30 | speech_act | ask, statement | covered |
| n31 | constraint | requirement, subject | covered |
| n32 | constraint | requirement | covered |
| n33 | claim | statement | covered |
| n34 | negation | negation | covered |
| n35 | constraint | color_label::blue | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s18 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "white" -> color_label::white; t1:s7 "white" -> color_label::white; t1:s9 "white" -> color_label::white, "blue" -> color_label::blue; t1:s11 "blue" -> color_label::blue; t1:s12 "white" -> color_label::white; t1:s14 "blue" -> color_label::blue; t1:s15 "blue" -> color_label::blue; t1:s16 "white" -> color_label::white; t1:s18 "blue" -> color_label::blue
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
