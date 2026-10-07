Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="size", subject="Bob", value=size_large) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="Bob", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Bob", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Erin", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="size", subject="Fiona", value=size_large) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_3 : TERM
    CLAIM attribute_claim(property="color", subject="Fiona", value=lexical_label_3) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="temperature", subject="Fiona", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s9" -> attribute_claim_9 : CLAIM
    CLAIM attribute_claim(property="color", subject="Gary", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_10 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_11 : CLAIM
    TERM requirement(property="quiet", value=TRUE) -> requirement_2 : TERM
    TERM subject(kind="Bob", qualifier=requirement_2) -> subject_2 : TERM
    TERM requirement(property="temperature", value=state_cold) -> requirement_3 : TERM
    TERM subject(kind="Bob", qualifier=requirement_3) -> subject_3 : TERM
    TERM conditional(condition=subject_2, consequence=subject_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_2 : CLAIM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_4 : TERM
    TERM subject(kind="person", qualifier=requirement_4) -> subject_4 : TERM
    TERM subject(kind="person", qualifier=requirement_2) -> subject_5 : TERM
    TERM conditional(condition=subject_4, consequence=subject_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_3 : CLAIM
    TERM conjunction(items=[requirement_4, requirement_2]) -> conjunction_2 : TERM
    TERM subject(kind="person", qualifier=conjunction_2) -> subject_6 : TERM
    TERM subject(kind="person", qualifier=requirement_3) -> subject_7 : TERM
    TERM conditional(condition=subject_6, consequence=subject_7) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_4 : CLAIM
    TERM requirement(property="kind", value=TRUE) -> requirement_5 : TERM
    TERM subject(kind="person", qualifier=requirement_5) -> subject_8 : TERM
    TERM requirement(property="size", value=size_large) -> requirement_6 : TERM
    TERM subject(kind="person", qualifier=requirement_6) -> subject_9 : TERM
    TERM conditional(condition=subject_8, consequence=subject_9) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_5 : CLAIM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_7 : TERM
    TERM conjunction(items=[requirement_4, requirement_7]) -> conjunction_3 : TERM
    TERM subject(kind="person", qualifier=conjunction_3) -> subject_10 : TERM
    TERM conditional(condition=subject_10, consequence=subject_8) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_6 : CLAIM
    TERM conjunction(items=[requirement_3, requirement_2]) -> conjunction_4 : TERM
    TERM subject(kind="person", qualifier=conjunction_4) -> subject_11 : TERM
    TERM conditional(condition=subject_11, consequence=subject_4) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_7 : CLAIM
    TERM conjunction(items=[requirement_3, requirement_6]) -> conjunction_5 : TERM
    TERM subject(kind="person", qualifier=conjunction_5) -> subject_12 : TERM
    TERM conditional(condition=subject_12, consequence=subject_8) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_8 : CLAIM
    TERM subject(kind="Erin", qualifier=requirement_6) -> subject_13 : TERM
    TERM subject(kind="Erin", qualifier=requirement_3) -> subject_14 : TERM
    TERM conditional(condition=subject_13, consequence=subject_14) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_9 : CLAIM
    TERM conjunction(items=[requirement_3, requirement_7]) -> conjunction_6 : TERM
    TERM subject(kind="person", qualifier=conjunction_6) -> subject_15 : TERM
    TERM requirement(property="smart", value=TRUE) -> requirement_8 : TERM
    TERM subject(kind="person", qualifier=requirement_8) -> subject_16 : TERM
    TERM conditional(condition=subject_15, consequence=subject_16) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_10 : CLAIM
    CLAIM attribute_claim(property="kind", subject="Gary", value=TRUE) BY role_user STATUS hypothesized SOURCE "t1:s22" -> attribute_claim_12 : CLAIM
    UTTER confirm(target=attribute_claim_12)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | conditional, statement | covered |
| n2 | claim | attribute_claim, size_large | covered |
| n3 | claim | attribute_claim, lexical_label, color_label | covered |
| n4 | object | color_label::red | label-preserved |
| n5 | claim | attribute_claim | covered |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim, size_large | covered |
| n8 | claim | attribute_claim, lexical_label, color_label | covered |
| n9 | object | color_label::blue | label-preserved |
| n10 | claim | attribute_claim, state_cold | covered |
| n11 | claim | attribute_claim | covered |
| n12 | claim | attribute_claim, lexical_label, color_label | covered |
| n13 | object | color_label::red | label-preserved |
| n14 | claim | attribute_claim | covered |
| n15 | reasoning | statement, conditional, subject, requirement, state_cold | covered |
| n16 | reasoning | statement, conditional, subject, requirement, lexical_label, color_label | covered |
| n17 | object | color_label::red | label-preserved |
| n18 | reasoning | statement, conditional, conjunction, subject, requirement, lexical_label, color_label, state_cold | covered |
| n19 | object | color_label::red | label-preserved |
| n20 | reasoning | statement, conditional, subject, requirement, size_large | covered |
| n21 | reasoning | statement, conditional, conjunction, subject, requirement, lexical_label, color_label | covered |
| n22 | object | color_label::red | label-preserved |
| n23 | object | color_label::blue | label-preserved |
| n24 | reasoning | statement, conditional, conjunction, subject, requirement, lexical_label, color_label, state_cold | covered |
| n25 | object | color_label::blue | label-preserved |
| n26 | reasoning | statement, conditional, conjunction, subject, requirement, state_cold, size_large | covered |
| n27 | reasoning | statement, conditional, subject, requirement, size_large, state_cold | covered |
| n28 | reasoning | statement, conditional, conjunction, subject, requirement, lexical_label, color_label, state_cold | covered |
| n29 | object | color_label::blue | label-preserved |
| n30 | speech_act | confirm, statement | covered |
| n31 | constraint | confirm | covered |
| n32 | claim | attribute_claim | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1-t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "red" -> color_label::red; t1:s7 "blue" -> color_label::blue; t1:s10 "red" -> color_label::red; t1:s13 "red" -> color_label::red; t1:s14 "red" -> color_label::red; t1:s16 "red" -> color_label::red, "blue" -> color_label::blue; t1:s17 "blue" -> color_label::blue; t1:s20 "blue" -> color_label::blue
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
