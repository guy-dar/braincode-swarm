Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="Anne", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Anne", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="size", subject="Dave", value=size_large) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="color", subject="Dave", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="state", subject="Dave", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="furry", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="nice", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Dave", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s9" -> attribute_claim_9 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_10 : CLAIM
    CLAIM attribute_claim(property="color", subject="Fiona", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_11 : CLAIM
    CLAIM attribute_claim(property="furry", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s12" -> attribute_claim_12 : CLAIM
    CLAIM attribute_claim(property="size", subject="Gary", value=size_large) BY role_user STATUS asserted SOURCE "t1:s13" -> attribute_claim_13 : CLAIM
    CLAIM attribute_claim(property="furry", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s14" -> attribute_claim_14 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s15" -> attribute_claim_15 : CLAIM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    TERM requirement(property="size", value=size_large) -> requirement_3 : TERM
    TERM conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
    TERM requirement(property="furry", value=TRUE) -> requirement_4 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_2 : CLAIM
    TERM requirement(property="smart", value=TRUE) -> requirement_5 : TERM
    TERM requirement(property="state", value=state_cold) -> requirement_6 : TERM
    TERM conditional(condition=requirement_5, consequence=requirement_6) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_3 : CLAIM
    TERM conjunction(items=[requirement_6, requirement_5]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_3) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_4 : CLAIM
    TERM requirement(property="shape", value=shape_round) -> requirement_7 : TERM
    TERM conjunction(items=[requirement_2, requirement_7]) -> conjunction_4 : TERM
    TERM requirement(property="nice", value=TRUE) -> requirement_8 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_8) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_5 : CLAIM
    TERM conjunction(items=[requirement_7, requirement_5]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=requirement_6) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_6 : CLAIM
    TERM conjunction(items=[requirement_7, requirement_2]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=requirement_5) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_7 : CLAIM
    TERM conjunction(items=[requirement_3, requirement_7]) -> conjunction_7 : TERM
    TERM conditional(condition=conjunction_7, consequence=requirement_8) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_8 : CLAIM
    TERM conditional(condition=conjunction_5, consequence=requirement_8) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_9 : CLAIM
    TERM conjunction(items=[requirement_4, requirement_3]) -> conjunction_8 : TERM
    TERM conditional(condition=conjunction_8, consequence=requirement_7) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s24" -> statement_10 : CLAIM
    TERM requirement(property="theory_only", value=TRUE) -> requirement_9 : TERM
    TERM requirement(property="allowed_answers", value="True, False, or Unknown") -> requirement_10 : TERM
    TERM property_question(property="furry", subject="Anne") -> property_question_2 : TERM
    UTTER ask(target=property_question_2, constraints=[requirement_9, requirement_10])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | claim | attribute_claim, lexical_label, color_label::blue | label-preserved |
| n3 | claim | attribute_claim | covered |
| n4 | claim | attribute_claim, size_large | covered |
| n5 | claim | attribute_claim, lexical_label, color_label::blue | label-preserved |
| n6 | claim | attribute_claim, state_cold | covered |
| n7 | claim | attribute_claim | covered |
| n8 | claim | attribute_claim | covered |
| n9 | claim | attribute_claim, shape_round | covered |
| n10 | claim | attribute_claim | covered |
| n11 | claim | attribute_claim, lexical_label, color_label::blue | label-preserved |
| n12 | claim | attribute_claim | covered |
| n13 | claim | attribute_claim, size_large | covered |
| n14 | claim | attribute_claim | covered |
| n15 | claim | attribute_claim | covered |
| n16 | reasoning | conditional, conjunction, statement, size_large, color_label::blue | label-preserved |
| n17 | reasoning | conditional, statement, state_cold | covered |
| n18 | reasoning | conditional, conjunction, statement, size_large, state_cold | covered |
| n19 | reasoning | conditional, conjunction, statement, shape_round, color_label::blue | label-preserved |
| n20 | reasoning | conditional, conjunction, statement, shape_round, state_cold | covered |
| n21 | reasoning | conditional, conjunction, statement, shape_round, color_label::blue | label-preserved |
| n22 | reasoning | conditional, conjunction, statement, shape_round, size_large | covered |
| n23 | reasoning | conditional, conjunction, statement, shape_round | covered |
| n24 | reasoning | conditional, conjunction, statement, shape_round, size_large | covered |
| n25 | speech_act | ask, property_question | covered |
| n26 | action | property_question | covered |
| n27 | constraint | requirement | covered |
| n28 | constraint | requirement | covered |
| n29 | claim | property_question | covered |
| n30 | object | subject="Anne" | covered |
| n31 | object | subject="Dave" | covered |
| n32 | object | subject="Fiona" | covered |
| n33 | object | subject="Gary" | covered |
| n34 | constraint | color_label::blue | label-preserved |
| n35 | constraint | property="smart" | covered |
| n36 | constraint | size_large | covered |
| n37 | constraint | state_cold | covered |
| n38 | constraint | property="furry" | covered |
| n39 | constraint | property="nice" | covered |
| n40 | constraint | shape_round | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s26 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2, t1:s5, t1:s11, t1:s16, t1:s19, t1:s21 "blue" → color_label::blue (open label)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
