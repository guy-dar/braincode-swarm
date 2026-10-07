Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="size", subject="Anne", value=size_large) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="color", subject="Anne", value=color_label::blue) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="state", subject="Anne", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="furry", subject="Anne", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="color", subject="Anne", value=color_label::red) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Anne", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Anne", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    CLAIM attribute_claim(property="state", subject="Bob", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s9" -> attribute_claim_9 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Bob", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_10 : CLAIM
    CLAIM attribute_claim(property="furry", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_11 : CLAIM
    CLAIM attribute_claim(property="color", subject="Erin", value=color_label::blue) BY role_user STATUS asserted SOURCE "t1:s12" -> attribute_claim_12 : CLAIM
    CLAIM attribute_claim(property="state", subject="Erin", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s13" -> attribute_claim_13 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Erin", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s14" -> attribute_claim_14 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Erin", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s15" -> attribute_claim_15 : CLAIM
    TERM requirement(property="smart", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="color", value=color_label::red) -> requirement_3 : TERM
    TERM conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
    TERM requirement(property="color", value=color_label::blue) -> requirement_4 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_2 : CLAIM
    TERM requirement(property="state", value=state_cold) -> requirement_5 : TERM
    TERM requirement(property="size", value=size_large) -> requirement_6 : TERM
    TERM conjunction(items=[requirement_5, requirement_6]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_3 : CLAIM
    TERM requirement(property="smart", value=TRUE) -> requirement_7 : TERM
    TERM requirement(property="color", value=color_label::red) -> requirement_8 : TERM
    TERM conjunction(items=[requirement_7, requirement_8]) -> conjunction_4 : TERM
    TERM requirement(property="size", value=size_large) -> requirement_9 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_9) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_4 : CLAIM
    TERM requirement(property="shape", value=shape_round) -> requirement_10 : TERM
    TERM requirement(property="furry", value=TRUE) -> requirement_11 : TERM
    TERM conjunction(items=[requirement_10, requirement_11]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=requirement_9) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_5 : CLAIM
    TERM conditional(condition=requirement_10, consequence=requirement_11) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_6 : CLAIM
    TERM conditional(condition=requirement_9, consequence=requirement_3) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_7 : CLAIM
    TERM conditional(condition=requirement_2, consequence=requirement_10) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_8 : CLAIM
    TERM conditional(condition=requirement_9, consequence=requirement_10) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_9 : CLAIM
    TERM conditional(condition=requirement_11, consequence=requirement_9) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s24" -> statement_10 : CLAIM
    TERM requirement(property="color", value=color_label::red) -> requirement_12 : TERM
    TERM negation(target=requirement_12) -> negation_2 : TERM
    TERM attribute_claim(property="color", subject="Bob", value=color_label::red) -> attribute_claim_16 : TERM
    TERM negation(target=attribute_claim_16) -> negation_3 : TERM
    UTTER ask(target=negation_3)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement | covered |
| n2 | claim | attribute_claim, size_large | covered |
| n3 | claim | attribute_claim, color_label::blue | label-preserved |
| n4 | constraint | color_label::blue | label-preserved |
| n5 | claim | attribute_claim, state_cold | covered |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim, color_label::red | label-preserved |
| n8 | constraint | color_label::red | label-preserved |
| n9 | claim | attribute_claim, shape_round | covered |
| n10 | claim | attribute_claim | covered |
| n11 | claim | attribute_claim, state_cold | covered |
| n12 | claim | attribute_claim | covered |
| n13 | claim | attribute_claim | covered |
| n14 | claim | attribute_claim, color_label::blue | label-preserved |
| n15 | claim | attribute_claim, state_cold | covered |
| n16 | claim | attribute_claim, shape_round | covered |
| n17 | claim | attribute_claim | covered |
| n18 | reasoning | conditional, conjunction, requirement, statement, color_label::blue, color_label::red | label-preserved |
| n19 | reasoning | conditional, conjunction, requirement, statement, size_large, state_cold, color_label::red | covered |
| n20 | reasoning | conditional, conjunction, requirement, statement, size_large, color_label::red | covered |
| n21 | reasoning | conditional, conjunction, requirement, statement, shape_round, size_large | covered |
| n22 | reasoning | conditional, requirement, statement, shape_round | covered |
| n23 | reasoning | conditional, requirement, statement, size_large, color_label::red | covered |
| n24 | reasoning | conditional, requirement, statement, shape_round | covered |
| n25 | reasoning | conditional, requirement, statement, shape_round, size_large | covered |
| n26 | reasoning | conditional, requirement, statement, size_large | covered |
| n27 | action | ask | covered |
| n28 | constraint | conjunction | covered |
| n29 | constraint | ask | covered |
| n30 | negation | negation, color_label::red | label-preserved |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s26 is represented.
- Opaque-text spans: none
- Label-preserved spans: t1:s3, t1:s12, t1:s16 "blue" → color_label::blue; t1:s6, t1:s16, t1:s17, t1:s18, t1:s21, t1:s26 "red" → color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
