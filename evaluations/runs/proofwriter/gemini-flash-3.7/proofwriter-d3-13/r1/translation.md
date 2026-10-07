Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER inform(target=statement_2)
    TERM character_trait(property="kind", value="Anne") -> character_trait_2 : TERM
    TERM negation(target=character_trait_2) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM character_trait(property="quiet", value="Anne") -> character_trait_3 : TERM
    CLAIM statement(fact=character_trait_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    TERM negation(target=lexical_label_2) -> negation_3 : TERM
    CLAIM statement(fact=negation_3) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM character_trait(property="rough", value="Dave") -> character_trait_4 : TERM
    CLAIM statement(fact=character_trait_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM character_trait(property="shape", value=shape_round) -> character_trait_5 : TERM
    CLAIM statement(fact=character_trait_5) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM character_trait(property="smart", value="Dave") -> character_trait_6 : TERM
    CLAIM statement(fact=character_trait_6) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM character_trait(property="quiet", value="Fiona") -> character_trait_7 : TERM
    CLAIM statement(fact=character_trait_7) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM character_trait(property="shape", value=shape_round) -> character_trait_8 : TERM
    CLAIM statement(fact=character_trait_8) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM character_trait(property="smart", value="Gary") -> character_trait_9 : TERM
    CLAIM statement(fact=character_trait_9) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM character_trait(property="young", value="Gary") -> character_trait_10 : TERM
    CLAIM statement(fact=character_trait_10) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM character_trait(property="shape", value=shape_round) -> character_trait_11 : TERM
    TERM character_trait(property="rough", value="people") -> character_trait_12 : TERM
    CLAIM statement(fact=character_trait_11) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    CLAIM statement(fact=character_trait_12) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_13 : CLAIM
    LINK supports(conclusion=statement_13, premise=statement_12) SOURCE "t1:s12"
    TERM character_trait(property="smart", value="someone") -> character_trait_13 : TERM
    TERM character_trait(property="rough", value="someone") -> character_trait_14 : TERM
    CLAIM statement(fact=character_trait_13) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_14 : CLAIM
    CLAIM statement(fact=character_trait_14) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_15 : CLAIM
    LINK supports(conclusion=statement_15, premise=statement_14) SOURCE "t1:s13"
    TERM character_trait(property="young", value="people") -> character_trait_15 : TERM
    TERM character_trait(property="rough", value="people") -> character_trait_16 : TERM
    TERM conjunction(items=[character_trait_15, character_trait_16]) -> conjunction_2 : TERM
    TERM character_trait(property="smart", value="people") -> character_trait_17 : TERM
    CLAIM statement(fact=conjunction_2) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_16 : CLAIM
    CLAIM statement(fact=character_trait_17) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_17 : CLAIM
    LINK supports(conclusion=statement_17, premise=statement_16) SOURCE "t1:s14"
    TERM character_trait(property="rough", value="someone") -> character_trait_18 : TERM
    TERM character_trait(property="kind", value="someone") -> character_trait_19 : TERM
    CLAIM statement(fact=character_trait_18) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_18 : CLAIM
    CLAIM statement(fact=character_trait_19) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_19 : CLAIM
    LINK supports(conclusion=statement_19, premise=statement_18) SOURCE "t1:s15"
    TERM character_trait(property="rough", value="people") -> character_trait_20 : TERM
    TERM character_trait(property="kind", value="people") -> character_trait_21 : TERM
    CLAIM statement(fact=character_trait_20) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_20 : CLAIM
    CLAIM statement(fact=character_trait_21) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_21 : CLAIM
    LINK supports(conclusion=statement_21, premise=statement_20) SOURCE "t1:s16"
    TERM character_trait(property="smart", value="Fiona") -> character_trait_22 : TERM
    TERM character_trait(property="kind", value="Fiona") -> character_trait_23 : TERM
    TERM conjunction(items=[character_trait_22, character_trait_23]) -> conjunction_3 : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    CLAIM statement(fact=conjunction_3) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_23 : CLAIM
    CLAIM statement(fact=lexical_label_3) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_24 : CLAIM
    LINK supports(conclusion=statement_24, premise=statement_23) SOURCE "t1:s17"
    TERM character_trait(property="shape", value=shape_round) -> character_trait_24 : TERM
    TERM character_trait(property="quiet", value="Anne") -> character_trait_25 : TERM
    CLAIM statement(fact=character_trait_24) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_25 : CLAIM
    CLAIM statement(fact=character_trait_25) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_26 : CLAIM
    LINK supports(conclusion=statement_26, premise=statement_25) SOURCE "t1:s18"
    TERM character_trait(property="shape", value=shape_round) -> character_trait_26 : TERM
    TERM character_trait(property="rough", value="people") -> character_trait_27 : TERM
    TERM conjunction(items=[character_trait_26, character_trait_27]) -> conjunction_4 : TERM
    TERM character_trait(property="quiet", value="people") -> character_trait_28 : TERM
    CLAIM statement(fact=conjunction_4) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_27 : CLAIM
    CLAIM statement(fact=character_trait_28) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_28 : CLAIM
    LINK supports(conclusion=statement_28, premise=statement_27) SOURCE "t1:s19"
    TERM character_trait(property="kind", value="people") -> character_trait_29 : TERM
    TERM character_trait(property="young", value="people") -> character_trait_30 : TERM
    CLAIM statement(fact=character_trait_29) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_29 : CLAIM
    CLAIM statement(fact=character_trait_30) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_30 : CLAIM
    LINK supports(conclusion=statement_30, premise=statement_29) SOURCE "t1:s20"
    TERM test_condition(condition="theory_only", expected=TRUE) -> test_condition_2 : TERM
    TERM character_trait(property="young", value="Fiona") -> character_trait_31 : TERM
    TERM negation(target=character_trait_31) -> negation_4 : TERM
    CLAIM statement(fact=negation_4) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_31 : CLAIM
    UTTER ask(target=negation_4, constraints=[test_condition_2])
    UTTER respond(target=statement_31)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | inform | covered |
| n2 | claim | statement | covered |
| n3 | negation | negation | covered |
| n4 | claim | statement | covered |
| n5 | claim | statement | covered |
| n6 | negation | negation | covered |
| n7 | object | color_label::green | label-preserved |
| n8 | claim | statement | covered |
| n9 | claim | statement | covered |
| n10 | claim | statement | covered |
| n11 | claim | statement | covered |
| n12 | claim | statement | covered |
| n13 | claim | statement | covered |
| n14 | claim | statement | covered |
| n15 | claim | statement | covered |
| n16 | reasoning | supports | covered |
| n17 | claim | statement | covered |
| n18 | reasoning | supports | covered |
| n19 | claim | statement | covered |
| n20 | reasoning | supports | covered |
| n21 | claim | statement | covered |
| n22 | reasoning | supports | covered |
| n23 | claim | statement | covered |
| n24 | reasoning | supports | covered |
| n25 | claim | statement | covered |
| n26 | reasoning | supports | covered |
| n27 | object | color_label::green | label-preserved |
| n28 | claim | statement | covered |
| n29 | reasoning | supports | covered |
| n30 | claim | statement | covered |
| n31 | reasoning | supports | covered |
| n32 | claim | statement | covered |
| n33 | reasoning | supports | covered |
| n34 | speech_act | ask | covered |
| n35 | constraint | test_condition | covered |
| n36 | constraint | respond | covered |
| n37 | claim | statement | covered |
| n38 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s4 "green" -> color_label::green; t1:s17 "green" -> color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
