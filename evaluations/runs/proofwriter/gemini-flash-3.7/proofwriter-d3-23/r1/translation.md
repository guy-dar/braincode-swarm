Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    UTTER propose(target=subject_2)
    CLAIM attribute_claim(property="cold", subject="Anne", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Anne", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Bob", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="young", subject="Bob", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="kind", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="color", subject="Harry", value=color_label::red) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="young", subject="Harry", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    TERM requirement(property="young", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="color", value=color_label::red) -> requirement_3 : TERM
    TERM conditional(condition=requirement_2, consequence=requirement_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM subject(kind="Harry", qualifier=requirement_2) -> subject_3 : TERM
    TERM requirement(property="smart", value=TRUE) -> requirement_4 : TERM
    TERM subject(kind="Harry", qualifier=requirement_4) -> subject_4 : TERM
    TERM conditional(condition=subject_3, consequence=subject_4) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM requirement(property="rough", value=TRUE) -> requirement_5 : TERM
    TERM subject(kind="Gary", qualifier=requirement_5) -> subject_5 : TERM
    TERM requirement(property="thermal_state", value=state_cold) -> requirement_6 : TERM
    TERM subject(kind="Gary", qualifier=requirement_6) -> subject_6 : TERM
    TERM conditional(condition=subject_5, consequence=subject_6) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM requirement(property="color", value=color_label::blue) -> requirement_7 : TERM
    TERM subject(kind="Gary", qualifier=requirement_7) -> subject_7 : TERM
    TERM conjunction(items=[subject_6, subject_7]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_5) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM requirement(property="kind", value=TRUE) -> requirement_8 : TERM
    TERM conjunction(items=[requirement_4, requirement_8]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_2) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM conditional(condition=requirement_6, consequence=requirement_4) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM conditional(condition=requirement_8, consequence=requirement_5) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_8 : CLAIM
    TERM conjunction(items=[requirement_3, requirement_8]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_6) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_9 : CLAIM
    TERM subject(kind="Gary", qualifier=requirement_4) -> subject_8 : TERM
    TERM negation(target=subject_8) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_10 : CLAIM
    TERM requirement(property="basis", value="theory") -> requirement_9 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(target=negation_2, constraints=[constraint_single_choice_2, requirement_9])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | propose, subject | covered |
| n2 | claim | attribute_claim, state_cold | covered |
| n3 | claim | attribute_claim | covered |
| n4 | claim | attribute_claim | covered |
| n5 | claim | attribute_claim | covered |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim, color_label::red | covered |
| n8 | object | color_label::red | label-preserved |
| n9 | claim | attribute_claim | covered |
| n10 | reasoning | conditional, requirement, statement, color_label::red | label-preserved |
| n11 | object | color_label::red | label-preserved |
| n12 | reasoning | conditional, subject, statement | covered |
| n13 | reasoning | conditional, state_cold, subject, statement | covered |
| n14 | reasoning | conditional, conjunction, state_cold, subject, statement, color_label::blue | covered |
| n15 | object | color_label::blue | label-preserved |
| n16 | reasoning | conditional, conjunction, requirement, statement | covered |
| n17 | reasoning | conditional, requirement, state_cold, statement | covered |
| n18 | reasoning | conditional, requirement, statement | covered |
| n19 | reasoning | conditional, conjunction, requirement, state_cold, statement, color_label::red | covered |
| n20 | object | color_label::red | label-preserved |
| n21 | speech_act | ask | covered |
| n22 | constraint | requirement | covered |
| n23 | constraint | constraint_single_choice | covered |
| n24 | claim | statement, subject | covered |
| n25 | negation | negation, subject | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s18 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s7 "red" → color_label::red (label only; no shade equivalence), t1:s9 "red" → color_label::red, t1:s12 "blue" → color_label::blue, t1:s16 "red" → color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
