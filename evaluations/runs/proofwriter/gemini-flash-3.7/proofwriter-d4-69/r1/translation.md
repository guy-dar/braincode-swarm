Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    TERM lexical_label(value=color_label::white) -> lexical_label_3 : TERM
    CLAIM attribute_claim(property="furry", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="color", subject="Dave", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="kind", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="kind", subject="Erin", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Erin", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="color", subject="Fiona", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s9" -> attribute_claim_9 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_10 : CLAIM
    CLAIM attribute_claim(property="kind", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_11 : CLAIM
    CLAIM attribute_claim(property="color", subject="Gary", value=lexical_label_3) BY role_user STATUS asserted SOURCE "t1:s12" -> attribute_claim_12 : CLAIM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    TERM requirement(property="smart", value=TRUE) -> requirement_3 : TERM
    TERM requirement(property="quiet", value=TRUE) -> requirement_4 : TERM
    TERM conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_2 : CLAIM
    TERM subject(kind="Erin", qualifier=requirement_3) -> subject_2 : TERM
    TERM subject(kind="Erin", qualifier=requirement_4) -> subject_3 : TERM
    TERM conditional(condition=subject_2, consequence=subject_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_3 : CLAIM
    TERM requirement(property="kind", value=TRUE) -> requirement_5 : TERM
    TERM requirement(property="furry", value=TRUE) -> requirement_6 : TERM
    TERM conjunction(items=[requirement_5, requirement_6]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_2) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_4 : CLAIM
    TERM conditional(condition=requirement_6, consequence=requirement_5) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_5 : CLAIM
    TERM requirement(property="rough", value=TRUE) -> requirement_7 : TERM
    TERM conditional(condition=requirement_5, consequence=requirement_7) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_6 : CLAIM
    TERM conjunction(items=[requirement_5, requirement_7]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_3) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_7 : CLAIM
    TERM conjunction(items=[requirement_4, requirement_5]) -> conjunction_5 : TERM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_8 : TERM
    TERM conditional(condition=conjunction_5, consequence=requirement_8) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_8 : CLAIM
    TERM conjunction(items=[requirement_8, requirement_3]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=requirement_6) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_9 : CLAIM
    CLAIM attribute_claim(property="rough", subject="Fiona", value=TRUE) BY role_user STATUS hypothesized SOURCE "t1:s22" -> attribute_claim_13 : CLAIM
    TERM requirement(property="grounding", value="theory") -> requirement_9 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(target=attribute_claim_13, constraints=[requirement_9, constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject | covered |
| n2 | object | conjunction | covered |
| n3 | claim | attribute_claim | covered |
| n4 | claim | color_label::green, attribute_claim | label-preserved |
| n5 | constraint | color_label::green | label-preserved |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim | covered |
| n8 | object | subject | covered |
| n9 | claim | statement, attribute_claim | covered |
| n10 | claim | attribute_claim | covered |
| n11 | object | attribute_claim | covered |
| n12 | claim | color_label::green, attribute_claim | label-preserved |
| n13 | constraint | color_label::green | label-preserved |
| n14 | claim | attribute_claim | covered |
| n15 | claim | attribute_claim | covered |
| n16 | object | attribute_claim | covered |
| n17 | claim | attribute_claim | covered |
| n18 | claim | color_label::white, attribute_claim | label-preserved |
| n19 | constraint | color_label::white | label-preserved |
| n20 | claim | conditional | covered |
| n21 | claim | conditional | covered |
| n22 | claim | conditional | covered |
| n23 | claim | conditional | covered |
| n24 | claim | conditional | covered |
| n25 | claim | conditional | covered |
| n26 | claim | conditional | covered |
| n27 | claim | conditional | covered |
| n28 | speech_act | ask, statement, conditional | covered |
| n29 | constraint | subject, conjunction | covered |
| n30 | constraint | constraint_single_choice | covered |
| n31 | claim | attribute_claim | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "green" → color_label::green; t1:s8 "green" → color_label::green; t1:s12 "white" → color_label::white
- Missing constructs: none
- Unresolved ambiguities: none
- Check: rag check reported 0 unresolved needs and 0 unknown symbols
