Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="rough", subject="Dave", value=TRUE) BY user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="Erin", value=lexical_label_2) BY user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="nice", subject="Erin", value=TRUE) BY user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    TERM character_trait(property="rough", value="rough") -> character_trait_2 : TERM
    TERM negation(target=character_trait_2) -> negation_2 : TERM
    CLAIM attribute_claim(property="rough", subject="Fiona", value=FALSE) BY user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_3 : TERM
    CLAIM attribute_claim(property="color", subject="Gary", value=lexical_label_3) BY user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="nice", subject="Gary", value=TRUE) BY user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="rough", subject="Gary", value=TRUE) BY user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    TERM character_trait(property="shape", value=shape_round) -> character_trait_3 : TERM
    TERM conjunction(items=[character_trait_3, negation_2]) -> conjunction_2 : TERM
    TERM character_trait(property="nice", value="nice") -> character_trait_4 : TERM
    TERM conditional(condition=conjunction_2, consequence=character_trait_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM character_trait(property="size", value="big") -> character_trait_5 : TERM
    TERM conditional(condition=lexical_label_2, consequence=character_trait_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM conditional(condition=character_trait_3, consequence=lexical_label_2) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM character_trait(property="kind", value="kind") -> character_trait_6 : TERM
    TERM conditional(condition=character_trait_2, consequence=character_trait_6) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM conjunction(items=[character_trait_2, lexical_label_2]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=character_trait_6) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM conjunction(items=[lexical_label_2, character_trait_5]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=lexical_label_3) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM conditional(condition=character_trait_6, consequence=character_trait_3) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY user STATUS asserted SOURCE "t1:s15" -> statement_8 : CLAIM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM requirement(property="basis", value="theory") -> requirement_2 : TERM
    TERM negation(target=character_trait_5) -> negation_3 : TERM
    TERM subject(kind="Fiona", qualifier=negation_3) -> subject_2 : TERM
    UTTER ask(target=subject_2, constraints=[constraint_single_choice_2, requirement_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | claim | attribute_claim | covered |
| n3 | claim | attribute_claim, lexical_label | covered |
| n4 | object | color_label::green | label-preserved |
| n5 | claim | attribute_claim | covered |
| n6 | claim | attribute_claim | covered |
| n7 | negation | negation | covered |
| n8 | claim | attribute_claim, lexical_label | covered |
| n9 | object | color_label::blue | label-preserved |
| n10 | claim | attribute_claim | covered |
| n11 | claim | attribute_claim | covered |
| n12 | claim | conditional, statement, shape_round | covered |
| n13 | negation | negation | covered |
| n14 | claim | conditional, statement, lexical_label | covered |
| n15 | object | color_label::green | label-preserved |
| n16 | claim | conditional, statement, shape_round, lexical_label | covered |
| n17 | object | color_label::green | label-preserved |
| n18 | claim | conditional, statement | covered |
| n19 | claim | conditional, statement, lexical_label | covered |
| n20 | object | color_label::green | label-preserved |
| n21 | claim | conditional, statement, lexical_label | covered |
| n22 | object | color_label::green | label-preserved |
| n23 | object | color_label::blue | label-preserved |
| n24 | claim | conditional, statement, shape_round | covered |
| n25 | speech_act | ask | covered |
| n26 | constraint | requirement | covered |
| n27 | constraint | constraint_single_choice | covered |
| n28 | claim | subject | covered |
| n29 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s17 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "green" → color_label::green, t1:s6 "blue" → color_label::blue, t1:s10 "green" → color_label::green, t1:s11 "green" → color_label::green, t1:s13 "green" → color_label::green, t1:s14 "green" → color_label::green, t1:s14 "blue" → color_label::blue
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
