Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=color_label::blue) -> lexical_label_blue : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_green : TERM
    CLAIM attribute_claim(property="size", subject="Bob", value=size_large) BY user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="color", subject="Bob", value=lexical_label_blue) BY user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="color", subject="Bob", value=lexical_label_green) BY user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="shape", subject="Bob", value=shape_round) BY user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="intelligence", subject="Bob", value="smart") BY user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="age", subject="Bob", value="young") BY user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="color", subject="Charlie", value=lexical_label_green) BY user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    TERM character_trait(property="nice", value=1) -> character_trait_nice : TERM
    TERM negation(target=character_trait_nice) -> negation_nice : TERM
    CLAIM statement(fact=negation_nice) BY user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM character_trait(property="young", value=1) -> character_trait_young : TERM
    TERM negation(target=character_trait_young) -> negation_young : TERM
    CLAIM statement(fact=negation_young) BY user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    CLAIM attribute_claim(property="color", subject="Erin", value=lexical_label_blue) BY user STATUS asserted SOURCE "t1:s11" -> attribute_claim_9 : CLAIM
    CLAIM attribute_claim(property="age", subject="Harry", value="young") BY user STATUS asserted SOURCE "t1:s12" -> attribute_claim_10 : CLAIM
    TERM requirement(property="color", value=lexical_label_blue) -> req_erin_blue : TERM
    TERM requirement(property="age", value="young") -> req_erin_young : TERM
    TERM conjunction(items=[req_erin_blue, req_erin_young]) -> conj_erin : TERM
    TERM requirement(property="intelligence", value="smart") -> req_erin_smart : TERM
    CLAIM enables(condition=conj_erin, outcome=req_erin_smart) BY user STATUS asserted SOURCE "t1:s13" -> enables_2 : CLAIM
    TERM requirement(property="shape", value=shape_round) -> req_someone_round : TERM
    TERM conditional(condition=req_someone_round, consequence=req_erin_young) -> cond_round_young : TERM
    CLAIM statement(fact=cond_round_young) BY user STATUS asserted SOURCE "t1:s14" -> statement_4 : CLAIM
    TERM requirement(property="color", value=lexical_label_green) -> req_people_green : TERM
    TERM conditional(condition=req_erin_blue, consequence=req_people_green) -> cond_blue_green : TERM
    CLAIM statement(fact=cond_blue_green) BY user STATUS asserted SOURCE "t1:s15" -> statement_5 : CLAIM
    TERM requirement(property="size", value=size_large) -> req_harry_big : TERM
    TERM conditional(condition=req_erin_blue, consequence=req_harry_big) -> cond_harry : TERM
    CLAIM statement(fact=cond_harry) BY user STATUS asserted SOURCE "t1:s16" -> statement_6 : CLAIM
    TERM conjunction(items=[req_people_green, req_erin_young]) -> conj_charlie : TERM
    CLAIM enables(condition=conj_charlie, outcome=character_trait_nice) BY user STATUS asserted SOURCE "t1:s17" -> enables_3 : CLAIM
    TERM conditional(condition=req_harry_big, consequence=req_someone_round) -> cond_big_round : TERM
    CLAIM statement(fact=cond_big_round) BY user STATUS asserted SOURCE "t1:s18" -> statement_7 : CLAIM
    TERM conjunction(items=[req_someone_round, req_people_green]) -> conj_round_green : TERM
    TERM conditional(condition=conj_round_green, consequence=req_harry_big) -> cond_round_green_big : TERM
    CLAIM statement(fact=cond_round_green_big) BY user STATUS asserted SOURCE "t1:s19" -> statement_8 : CLAIM
    TERM conjunction(items=[req_erin_blue, req_people_green]) -> conj_blue_green : TERM
    TERM conditional(condition=conj_blue_green, consequence=req_harry_big) -> cond_blue_green_big : TERM
    CLAIM statement(fact=cond_blue_green_big) BY user STATUS asserted SOURCE "t1:s20" -> statement_9 : CLAIM
    CLAIM considered(subject=req_harry_big) BY user STATUS asserted SOURCE "t1:s21" -> considered_2 : CLAIM
    TERM constraint_realistic() -> constraint_realistic_2 : TERM
    UTTER ask(target=req_harry_big, constraints=[constraint_realistic_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, statement | covered |
| n2 | claim | attribute_claim, size_large | covered |
| n3 | claim | attribute_claim, lexical_label | covered |
| n4 | object | color_label::blue | label-preserved |
| n5 | claim | attribute_claim, lexical_label | covered |
| n6 | object | color_label::green | label-preserved |
| n7 | claim | attribute_claim, shape_round | covered |
| n8 | claim | attribute_claim | covered |
| n9 | claim | attribute_claim | covered |
| n10 | claim | attribute_claim, lexical_label | covered |
| n11 | object | color_label::green | label-preserved |
| n12 | claim | statement, character_trait, negation | covered |
| n13 | negation | negation | covered |
| n14 | claim | statement, character_trait, negation | covered |
| n15 | negation | negation | covered |
| n16 | claim | attribute_claim, lexical_label | covered |
| n17 | object | color_label::blue | label-preserved |
| n18 | claim | attribute_claim | covered |
| n19 | claim | enables, conjunction, requirement, lexical_label | covered |
| n20 | object | color_label::blue | label-preserved |
| n21 | claim | statement, conditional, requirement, shape_round | covered |
| n22 | claim | statement, conditional, requirement, lexical_label | covered |
| n23 | object | color_label::blue | label-preserved |
| n24 | object | color_label::green | label-preserved |
| n25 | claim | statement, conditional, requirement, size_large, lexical_label | covered |
| n26 | object | color_label::blue | label-preserved |
| n27 | claim | enables, conjunction, requirement, character_trait, lexical_label | covered |
| n28 | object | color_label::green | label-preserved |
| n29 | claim | statement, conditional, requirement, size_large, shape_round | covered |
| n30 | claim | statement, conditional, conjunction, requirement, size_large, shape_round, lexical_label | covered |
| n31 | object | color_label::green | label-preserved |
| n32 | claim | statement, conditional, conjunction, requirement, size_large, lexical_label | covered |
| n33 | object | color_label::blue | label-preserved |
| n34 | object | color_label::green | label-preserved |
| n35 | action | considered, ask | covered |
| n36 | constraint | subject | covered |
| n37 | constraint | constraint_realistic | covered |
| n38 | object | considered, requirement, size_large | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "blue" -> color_label::blue, t1:s4 "green" -> color_label::green, t1:s8 "green" -> color_label::green, t1:s11 "blue" -> color_label::blue, t1:s13 "blue" -> color_label::blue, t1:s15 "blue" -> color_label::blue, t1:s15 "green" -> color_label::green, t1:s16 "blue" -> color_label::blue, t1:s17 "green" -> color_label::green, t1:s19 "green" -> color_label::green, t1:s20 "blue" -> color_label::blue, t1:s20 "green" -> color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
