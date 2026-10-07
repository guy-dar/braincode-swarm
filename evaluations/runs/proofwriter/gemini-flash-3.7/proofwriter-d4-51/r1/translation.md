Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="Bob", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    CLAIM attribute_claim(property="color", subject="Bob", value=lexical_label_3) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Bob", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="color", subject="Fiona", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="color", subject="Fiona", value=lexical_label_3) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Fiona", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    CLAIM attribute_claim(property="temperature", subject="Gary", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s9" -> attribute_claim_9 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_4 : TERM
    CLAIM attribute_claim(property="color", subject="Gary", value=lexical_label_4) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_10 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Gary", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_11 : CLAIM
    CLAIM attribute_claim(property="color", subject="Harry", value=lexical_label_4) BY role_user STATUS asserted SOURCE "t1:s12" -> attribute_claim_12 : CLAIM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_2 : TERM
    TERM requirement(property="size", value=size_large) -> requirement_3 : TERM
    TERM conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
    TERM requirement(property="quiet", value=TRUE) -> requirement_4 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_2 : CLAIM
    TERM requirement(property="color", value=lexical_label_4) -> requirement_5 : TERM
    TERM conditional(condition=requirement_5, consequence=requirement_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_3 : CLAIM
    TERM requirement(property="shape", value=shape_round) -> requirement_6 : TERM
    TERM conditional(condition=requirement_3, consequence=requirement_6) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_4 : CLAIM
    TERM conjunction(items=[requirement_4, requirement_2]) -> conjunction_3 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_7 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_7) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_5 : CLAIM
    TERM conjunction(items=[requirement_4, requirement_3]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_5) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_6 : CLAIM
    TERM conditional(condition=requirement_6, consequence=requirement_2) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_7 : CLAIM
    TERM subject(kind="Harry", qualifier=requirement_4) -> subject_2 : TERM
    TERM negation(target=subject_2) -> negation_2 : TERM
    TERM requirement(property="scope", value="theory_only") -> requirement_8 : TERM
    TERM requirement(property="allowed_answers", value="truth_value") -> requirement_9 : TERM
    UTTER ask(target=negation_2, constraints=[requirement_8, requirement_9])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement | covered |
| n2 | claim | attribute_claim | covered |
| n3 | object | subject="Bob" | covered |
| n4 | constraint | color_label::blue | label-preserved |
| n5 | claim | attribute_claim | covered |
| n6 | constraint | color_label::green | label-preserved |
| n7 | claim | attribute_claim | covered |
| n8 | claim | attribute_claim | covered |
| n9 | object | subject="Fiona" | covered |
| n10 | constraint | color_label::blue | label-preserved |
| n11 | claim | attribute_claim | covered |
| n12 | constraint | color_label::green | label-preserved |
| n13 | claim | attribute_claim | covered |
| n14 | claim | shape_round, attribute_claim | covered |
| n15 | claim | state_cold, attribute_claim | covered |
| n16 | object | subject="Gary" | covered |
| n17 | claim | attribute_claim | covered |
| n18 | constraint | color_label::red | label-preserved |
| n19 | claim | shape_round, attribute_claim | covered |
| n20 | claim | attribute_claim | covered |
| n21 | object | subject="Harry" | covered |
| n22 | constraint | color_label::red | label-preserved |
| n23 | claim | conditional, conjunction, statement | covered |
| n24 | claim | conditional, statement | covered |
| n25 | claim | conditional, statement | covered |
| n26 | claim | color_label::blue | label-preserved |
| n27 | claim | conditional, conjunction, statement | covered |
| n28 | claim | conditional, statement | covered |
| n29 | speech_act | ask | covered |
| n30 | constraint | requirement | covered |
| n31 | constraint | requirement | covered |
| n32 | claim | negation, subject | covered |
| n33 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s20 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2, t1:s5 "blue" -> color_label::blue (n4, n10); t1:s3, t1:s6 "green" -> color_label::green (n6, n12); t1:s10, t1:s12 "red" -> color_label::red (n18, n22); t1:s16 "blue" -> color_label::blue (n26)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
