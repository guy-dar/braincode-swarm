Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM requirement(property="cold", value=TRUE) -> requirement_cold : TERM
    TERM requirement(property="kind", value=TRUE) -> requirement_kind : TERM
    TERM requirement(property="nice", value=TRUE) -> requirement_nice : TERM
    TERM requirement(property="smart", value=TRUE) -> requirement_smart : TERM
    TERM requirement(property="rough", value=TRUE) -> requirement_rough : TERM
    TERM requirement(property="quiet", value=TRUE) -> requirement_quiet : TERM
    TERM lexical_label(value=color_label::white) -> lexical_label_white : TERM
    TERM requirement(property="color", value=lexical_label_white) -> requirement_white : TERM
    TERM negation(target=requirement_cold) -> negation_cold : TERM
    TERM negation(target=requirement_smart) -> negation_smart : TERM
    TERM negation(target=requirement_white) -> negation_white : TERM
    TERM negation(target=requirement_quiet) -> negation_quiet : TERM

    CLAIM attribute_claim(property="cold", subject="Charlie", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s2" -> claim_charlie_cold : CLAIM
    CLAIM statement(fact=requirement_cold) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_charlie_cold : CLAIM

    CLAIM attribute_claim(property="kind", subject="Charlie", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s3" -> claim_charlie_kind : CLAIM
    CLAIM statement(fact=requirement_kind) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_charlie_kind : CLAIM

    CLAIM attribute_claim(property="cold", subject="Erin", value=FALSE) BY role_user STATUS asserted SOURCE "t1:s4" -> claim_erin_not_cold : CLAIM
    CLAIM statement(fact=negation_cold) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_erin_not_cold : CLAIM

    CLAIM attribute_claim(property="kind", subject="Erin", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> claim_erin_kind : CLAIM
    CLAIM statement(fact=requirement_kind) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_erin_kind : CLAIM

    CLAIM attribute_claim(property="nice", subject="Erin", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s6" -> claim_erin_nice : CLAIM
    CLAIM statement(fact=requirement_nice) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_erin_nice : CLAIM

    CLAIM attribute_claim(property="smart", subject="Erin", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s7" -> claim_erin_smart : CLAIM
    CLAIM statement(fact=requirement_smart) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_erin_smart : CLAIM

    CLAIM attribute_claim(property="color", subject="Erin", value=lexical_label_white) BY role_user STATUS asserted SOURCE "t1:s8" -> claim_erin_white : CLAIM
    CLAIM statement(fact=requirement_white) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_erin_white : CLAIM

    CLAIM attribute_claim(property="kind", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s9" -> claim_gary_kind : CLAIM
    CLAIM statement(fact=requirement_kind) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_gary_kind : CLAIM

    CLAIM attribute_claim(property="cold", subject="Harry", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s10" -> claim_harry_cold : CLAIM
    CLAIM statement(fact=requirement_cold) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_harry_cold : CLAIM

    CLAIM attribute_claim(property="rough", subject="Harry", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s11" -> claim_harry_rough : CLAIM
    CLAIM statement(fact=requirement_rough) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_harry_rough : CLAIM

    TERM conjunction(items=[requirement_rough, requirement_white]) -> conjunction_rough_white : TERM
    TERM conditional(condition=conjunction_rough_white, consequence=negation_smart) -> conditional_charlie_rule : TERM
    CLAIM statement(fact=conditional_charlie_rule) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_rule_12 : CLAIM

    TERM conjunction(items=[requirement_cold, requirement_smart]) -> conjunction_cold_smart : TERM
    TERM conditional(condition=conjunction_cold_smart, consequence=requirement_quiet) -> conditional_cold_smart_quiet : TERM
    CLAIM statement(fact=conditional_cold_smart_quiet) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_rule_13 : CLAIM

    TERM conditional(condition=requirement_rough, consequence=requirement_smart) -> conditional_rough_smart : TERM
    CLAIM statement(fact=conditional_rough_smart) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_rule_14 : CLAIM

    TERM conditional(condition=requirement_cold, consequence=requirement_rough) -> conditional_cold_rough : TERM
    CLAIM statement(fact=conditional_cold_rough) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_rule_15 : CLAIM

    TERM conjunction(items=[requirement_quiet, requirement_kind]) -> conjunction_quiet_kind : TERM
    TERM conditional(condition=conjunction_quiet_kind, consequence=requirement_nice) -> conditional_quiet_kind_nice : TERM
    CLAIM statement(fact=conditional_quiet_kind_nice) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_rule_16 : CLAIM

    TERM conjunction(items=[requirement_quiet, requirement_nice]) -> conjunction_quiet_nice : TERM
    TERM conditional(condition=conjunction_quiet_nice, consequence=negation_white) -> conditional_quiet_nice_not_white : TERM
    CLAIM statement(fact=conditional_quiet_nice_not_white) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_rule_17 : CLAIM

    LINK supports(conclusion=statement_rule_13, premise=statement_rule_12) SOURCE "t1:s13"
    LINK supports(conclusion=statement_rule_15, premise=statement_charlie_cold) SOURCE "t1:s15"
    LINK supports(conclusion=statement_rule_16, premise=statement_charlie_kind) SOURCE "t1:s16"
    LINK supports(conclusion=statement_rule_17, premise=statement_rule_16) SOURCE "t1:s17"

    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM requirement(property="evaluation_basis", value="theory") -> requirement_theory : TERM
    CLAIM attribute_claim(property="quiet", subject="Charlie", value=FALSE) BY role_user STATUS hypothesized SOURCE "t1:s19" -> claim_charlie_not_quiet : CLAIM
    CLAIM statement(fact=negation_quiet) BY role_user STATUS hypothesized SOURCE "t1:s19" -> statement_charlie_not_quiet : CLAIM

    UTTER ask(target=statement_charlie_not_quiet, constraints=[constraint_single_choice_2, requirement_theory])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, conditional, statement | covered |
| n2 | claim | attribute_claim, statement | covered |
| n3 | claim | attribute_claim, statement | covered |
| n4 | claim | attribute_claim, statement | covered |
| n5 | negation | negation | covered |
| n6 | claim | attribute_claim, statement | covered |
| n7 | claim | attribute_claim, statement | covered |
| n8 | claim | attribute_claim, statement | covered |
| n9 | claim | attribute_claim, color_label::white, statement | label-preserved |
| n10 | claim | attribute_claim, statement | covered |
| n11 | claim | attribute_claim, statement | covered |
| n12 | claim | attribute_claim, statement | covered |
| n13 | reasoning | conditional, conjunction, negation, statement | covered |
| n14 | negation | negation | covered |
| n15 | reasoning | conditional, conjunction, statement, supports | covered |
| n16 | reasoning | conditional, statement | covered |
| n17 | reasoning | conditional, statement, supports | covered |
| n18 | reasoning | conditional, conjunction, statement, supports | covered |
| n19 | reasoning | conditional, conjunction, negation, statement, supports | covered |
| n20 | negation | color_label::white, negation | label-preserved |
| n21 | speech_act | ask, statement | covered |
| n22 | constraint | requirement, supports | covered |
| n23 | constraint | constraint_single_choice | covered |
| n24 | claim | attribute_claim, statement | covered |
| n25 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s8 "white" → color_label::white; t1:s17 "white" → color_label::white
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
