Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="kind", subject="Bob", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="Bob", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Bob", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="kind", subject="Charlie", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_2 : TERM
    TERM negation(target=requirement_2) -> negation_2 : TERM
    CLAIM attribute_claim(property="color", subject="Fiona", value=negation_2) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Gary", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    TERM requirement(property="shape", value=shape_round) -> requirement_3 : TERM
    TERM requirement(property="quiet", value=TRUE) -> requirement_4 : TERM
    TERM conditional(condition=requirement_3, consequence=requirement_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM requirement(property="smart", value=TRUE) -> requirement_5 : TERM
    TERM conditional(condition=requirement_5, consequence=requirement_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM requirement(property="furry", value=TRUE) -> requirement_6 : TERM
    TERM conjunction(items=[requirement_6, negation_2]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_5) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM conditional(condition=requirement_4, consequence=requirement_5) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM requirement(property="kind", value=TRUE) -> requirement_7 : TERM
    TERM conjunction(items=[requirement_7, requirement_4]) -> conjunction_3 : TERM
    TERM negation(target=requirement_6) -> negation_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=negation_3) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM conditional(condition=requirement_5, consequence=requirement_7) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM conjunction(items=[requirement_7, negation_3]) -> conjunction_4 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_8 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_8) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_8 : CLAIM
    TERM negation(target=requirement_5) -> negation_4 : TERM
    TERM subject(kind="statement", qualifier=negation_4) -> subject_2 : TERM
    UTTER ask(target=subject_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | UTTER | covered |
| n2 | claim | attribute_claim | covered |
| n3 | object | subject | covered |
| n4 | claim | attribute_claim | covered |
| n5 | object | color_label::red | label-preserved |
| n6 | claim | shape_round | covered |
| n7 | claim | attribute_claim | covered |
| n8 | object | subject | covered |
| n9 | claim | attribute_claim | covered |
| n10 | negation | negation | covered |
| n11 | object | subject | covered |
| n12 | object | color_label::green | label-preserved |
| n13 | claim | attribute_claim | covered |
| n14 | claim | shape_round | covered |
| n15 | object | subject | covered |
| n16 | reasoning | conditional | covered |
| n17 | reasoning | conditional | covered |
| n18 | reasoning | conditional | covered |
| n19 | negation | negation | covered |
| n20 | reasoning | conditional | covered |
| n21 | reasoning | conditional | covered |
| n22 | negation | negation | covered |
| n23 | reasoning | conditional | covered |
| n24 | reasoning | conditional | covered |
| n25 | negation | negation | covered |
| n26 | object | color_label::red | label-preserved |
| n27 | speech_act | ask | covered |
| n28 | constraint | requirement | covered |
| n29 | constraint | requirement | covered |
| n30 | claim | attribute_claim | covered |
| n31 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s17 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "red" -> color_label::red; t1:s6 "green" -> color_label::green; t1:s15 "red" -> color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
