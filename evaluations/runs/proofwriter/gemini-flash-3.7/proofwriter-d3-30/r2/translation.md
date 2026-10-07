Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="big", subject="Anne", value=size_large) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="round", subject="Anne", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="nice", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="rough", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="rough", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="blue", subject="Gary", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="furry", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    TERM character_trait(property="rough", value="true") -> character_trait_2 : TERM
    TERM character_trait(property="furry", value="true") -> character_trait_3 : TERM
    TERM negation(target=character_trait_3) -> negation_2 : TERM
    TERM conditional(condition=character_trait_2, consequence=negation_2) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM character_trait(property="quiet", value="true") -> character_trait_4 : TERM
    TERM character_trait(property="big", value="true") -> character_trait_5 : TERM
    TERM conditional(condition=character_trait_4, consequence=character_trait_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM negation(target=character_trait_2) -> negation_3 : TERM
    TERM conjunction(items=[lexical_label_2, negation_3]) -> conjunction_2 : TERM
    TERM requirement(property="round", value=shape_round) -> requirement_2 : TERM
    TERM negation(target=requirement_2) -> negation_4 : TERM
    TERM conditional(condition=conjunction_2, consequence=negation_4) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM character_trait(property="nice", value="true") -> character_trait_6 : TERM
    TERM conjunction(items=[character_trait_6, requirement_2]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=character_trait_4) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM conjunction(items=[character_trait_5, character_trait_6]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_2) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM conditional(condition=requirement_2, consequence=lexical_label_2) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM conditional(condition=character_trait_3, consequence=character_trait_6) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_8 : CLAIM
    TERM conditional(condition=character_trait_6, consequence=character_trait_5) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_9 : CLAIM
    TERM conditional(condition=character_trait_2, consequence=character_trait_3) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_10 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Anne", value=TRUE) BY role_user STATUS hypothesized SOURCE "t1:s19" -> attribute_claim_9 : CLAIM
    TERM subject(kind="theory") -> subject_2 : TERM
    UTTER ask(target=character_trait_4, topic=subject_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject, ask, conjunction | covered |
| n2 | claim | attribute_claim, size_large, statement | covered |
| n3 | object | attribute_claim | covered |
| n4 | constraint | size_large | covered |
| n5 | claim | attribute_claim, shape_round | covered |
| n6 | constraint | shape_round | covered |
| n7 | claim | attribute_claim | covered |
| n8 | object | attribute_claim | covered |
| n9 | constraint | attribute_claim | covered |
| n10 | claim | attribute_claim, character_trait | covered |
| n11 | constraint | character_trait, shape_round | covered |
| n12 | claim | attribute_claim, character_trait | covered |
| n13 | object | attribute_claim | covered |
| n14 | claim | attribute_claim, lexical_label, color_label | label-preserved |
| n15 | object | attribute_claim | covered |
| n16 | constraint | color_label::blue | label-preserved |
| n17 | claim | attribute_claim, statement | covered |
| n18 | constraint | attribute_claim | covered |
| n19 | reasoning | conditional | covered |
| n20 | negation | negation | covered |
| n21 | reasoning | conditional | covered |
| n22 | reasoning | conditional, conjunction, shape_round, color_label | covered |
| n23 | negation | negation | covered |
| n24 | negation | negation, shape_round | covered |
| n25 | constraint | color_label::blue | label-preserved |
| n26 | reasoning | conditional, conjunction, shape_round | covered |
| n27 | reasoning | conditional, conjunction, shape_round | covered |
| n28 | reasoning | conditional, shape_round, color_label | covered |
| n29 | constraint | color_label::blue | label-preserved |
| n30 | reasoning | conditional | covered |
| n31 | reasoning | conditional, character_trait, size_large | covered |
| n32 | reasoning | conditional | covered |
| n33 | speech_act | ask, statement, conditional | covered |
| n34 | constraint | subject | covered |
| n35 | constraint | ask | covered |
| n36 | claim | attribute_claim, statement | covered |
| n37 | constraint | character_trait | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s7, t1:s11, t1:s14 "blue" -> color_label::blue (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
