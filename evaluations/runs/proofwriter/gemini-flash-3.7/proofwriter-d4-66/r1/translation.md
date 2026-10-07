Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="cold", subject="Bob", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Bob", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="cold", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="nice", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Harry", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    TERM requirement(property="quiet", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="cold", value=TRUE) -> requirement_3 : TERM
    TERM conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
    TERM requirement(property="rough", value=TRUE) -> requirement_4 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM requirement(property="nice", value=TRUE) -> requirement_5 : TERM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_6 : TERM
    TERM conditional(condition=requirement_5, consequence=requirement_6) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM requirement(property="big", value=TRUE) -> requirement_7 : TERM
    TERM conditional(condition=requirement_7, consequence=requirement_5) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM conditional(condition=requirement_6, consequence=requirement_2) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM conjunction(items=[requirement_2, requirement_4]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_7) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM requirement(property="fiona_red", value=lexical_label_2) -> requirement_8 : TERM
    TERM requirement(property="fiona_cold", value=TRUE) -> requirement_9 : TERM
    TERM conditional(condition=requirement_8, consequence=requirement_9) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM requirement(property="smart", value=TRUE) -> requirement_10 : TERM
    TERM conjunction(items=[requirement_6, requirement_5]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_10) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_8 : CLAIM
    TERM conjunction(items=[requirement_2, requirement_10]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=requirement_4) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_9 : CLAIM
    TERM conditional(condition=requirement_3, consequence=requirement_7) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_10 : CLAIM
    TERM requirement(property="subject", value="Harry") -> requirement_11 : TERM
    TERM conjunction(items=[requirement_11, requirement_2]) -> conjunction_6 : TERM
    TERM negation(target=conjunction_6) -> negation_2 : TERM
    TERM requirement(property="rely_only_on_theory", value=TRUE) -> requirement_12 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(target=negation_2, constraints=[requirement_12, constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, statement | covered |
| n2 | claim | attribute_claim | covered |
| n3 | claim | attribute_claim | covered |
| n4 | claim | attribute_claim | covered |
| n5 | claim | attribute_claim | covered |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim | covered |
| n8 | claim | attribute_claim | covered |
| n9 | reasoning | conditional, conjunction, requirement, statement | covered |
| n10 | reasoning | conditional, requirement, statement | covered |
| n11 | object | color_label::red | label-preserved |
| n12 | reasoning | conditional, requirement, statement | covered |
| n13 | reasoning | conditional, requirement, statement | covered |
| n14 | reasoning | conditional, conjunction, requirement, statement | covered |
| n15 | reasoning | conditional, requirement, statement | covered |
| n16 | reasoning | conditional, conjunction, requirement, statement | covered |
| n17 | reasoning | conditional, conjunction, requirement, statement | covered |
| n18 | reasoning | conditional, requirement, statement | covered |
| n19 | action | ask, statement | covered |
| n20 | constraint | requirement | covered |
| n21 | constraint | constraint_single_choice | covered |
| n22 | claim | negation, requirement | covered |
| n23 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s10 "red" -> color_label::red (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
