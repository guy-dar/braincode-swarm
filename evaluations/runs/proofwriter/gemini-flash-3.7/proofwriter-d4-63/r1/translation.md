Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="shape", subject="Bob", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="size", subject="Dave", value=size_large) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="age", subject="Dave", value="young") BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="temperament", subject="Fiona", value="quiet") BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="state", subject="Gary", value=state_cold) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="Gary", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="age", subject="Gary", value="young") BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    TERM requirement(property="state", value=state_cold) -> requirement_2 : TERM
    TERM requirement(property="size", value=size_large) -> requirement_3 : TERM
    TERM conditional(condition=requirement_2, consequence=requirement_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM requirement(property="temperament", value="quiet") -> requirement_4 : TERM
    TERM requirement(property="age", value="young") -> requirement_5 : TERM
    TERM conditional(condition=requirement_4, consequence=requirement_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM requirement(property="shape", value=shape_round) -> requirement_6 : TERM
    TERM conjunction(items=[requirement_6, requirement_2]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_7 : TERM
    TERM conjunction(items=[requirement_5, requirement_3]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_7) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM conjunction(items=[requirement_3, requirement_7]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_6) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM conditional(condition=requirement_5, consequence=requirement_2) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM subject(kind="Bob", qualifier=requirement_3) -> subject_2 : TERM
    TERM negation(target=subject_2) -> negation_2 : TERM
    TERM property_question(property="truth_value", subject=negation_2) -> property_question_2 : TERM
    TERM requirement(property="evaluation_basis", value="theory") -> requirement_8 : TERM
    TERM requirement(property="allowed_answers", value="true_false_unknown") -> requirement_9 : TERM
    UTTER ask(target=property_question_2, constraints=[requirement_8, requirement_9])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement, attribute_claim, ask | covered |
| n2 | claim | attribute_claim, shape_round | covered |
| n3 | object | "Bob" | covered |
| n4 | claim | attribute_claim, size_large | covered |
| n5 | object | "Dave" | covered |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim | covered |
| n8 | object | "Fiona" | covered |
| n9 | claim | attribute_claim, state_cold | covered |
| n10 | object | "Gary" | covered |
| n11 | claim | attribute_claim | covered |
| n12 | object | color_label::red | label-preserved |
| n13 | claim | attribute_claim | covered |
| n14 | claim | statement, conditional, requirement, state_cold, size_large | covered |
| n15 | claim | statement, conditional, requirement | covered |
| n16 | claim | statement, conditional, conjunction, requirement, shape_round, state_cold | covered |
| n17 | claim | statement, conditional, conjunction, requirement, size_large, color_label::green | covered |
| n18 | object | color_label::green | label-preserved |
| n19 | claim | statement, conditional, conjunction, requirement, size_large, color_label::green, shape_round | covered |
| n20 | object | color_label::green | label-preserved |
| n21 | claim | statement, conditional, requirement, state_cold | covered |
| n22 | action | ask, property_question | covered |
| n23 | constraint | requirement | covered |
| n24 | constraint | requirement | covered |
| n25 | claim | negation, subject, requirement, size_large | covered |
| n26 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s16 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s7 "red" -> color_label::red (label only; no sense resolved); t1:s12 "green" -> color_label::green (label only; no sense resolved); t1:s13 "green" -> color_label::green (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
