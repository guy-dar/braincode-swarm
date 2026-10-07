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
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    CLAIM attribute_claim(property="color", subject="Anne", value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="rough", subject="Anne", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="young", subject="Bob", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    TERM subject(kind="Dave") -> subject_3 : TERM
    CLAIM has_state(state=state_cold, subject=subject_3) BY role_user STATUS asserted SOURCE "t1:s5" -> has_state_2 : CLAIM
    CLAIM attribute_claim(property="kind", subject="Dave", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="size", subject="Fiona", value=size_large) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="young", subject="Fiona", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_7 : CLAIM
    TERM character_trait(property="cold", value="true") -> character_trait_2 : TERM
    TERM character_trait(property="young", value="true") -> character_trait_3 : TERM
    TERM character_trait(property="furry", value="true") -> character_trait_4 : TERM
    TERM conjunction(items=[character_trait_2, character_trait_3]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=character_trait_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM character_trait(property="rough", value="true") -> character_trait_5 : TERM
    TERM character_trait(property="kind", value="true") -> character_trait_6 : TERM
    TERM conjunction(items=[character_trait_5, character_trait_6]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=lexical_label_2) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM conditional(condition=conjunction_3, consequence=lexical_label_2) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM character_trait(property="big", value="true") -> character_trait_7 : TERM
    TERM conjunction(items=[character_trait_3, character_trait_7]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=character_trait_5) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM conditional(condition=character_trait_5, consequence=character_trait_4) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM conjunction(items=[character_trait_2, character_trait_5]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=lexical_label_2) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM conjunction(items=[character_trait_4, character_trait_5]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=character_trait_6) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_8 : CLAIM
    TERM conjunction(items=[character_trait_3, character_trait_2]) -> conjunction_7 : TERM
    TERM conditional(condition=conjunction_7, consequence=character_trait_6) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_9 : CLAIM
    TERM conditional(condition=character_trait_3, consequence=character_trait_7) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_10 : CLAIM
    TERM requirement(property="basis", value="theory") -> requirement_2 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM character_trait(property="furry", value="true") -> character_trait_8 : TERM
    TERM negation(target=character_trait_8) -> negation_2 : TERM
    TERM subject(kind="Bob", qualifier=negation_2) -> subject_4 : TERM
    UTTER ask(target=subject_4, constraints=[constraint_single_choice_2, requirement_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | propose, subject | covered |
| n2 | claim | attribute_claim, color_label::red, lexical_label | label-preserved |
| n3 | claim | attribute_claim | covered |
| n4 | claim | attribute_claim | covered |
| n5 | claim | has_state, state_cold, subject | covered |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim, size_large | covered |
| n8 | claim | attribute_claim | covered |
| n9 | reasoning | conditional, conjunction, character_trait, statement | covered |
| n10 | reasoning | conditional, conjunction, character_trait, statement, color_label::red, lexical_label | label-preserved |
| n11 | reasoning | conditional, conjunction, character_trait, statement, color_label::red, lexical_label | label-preserved |
| n12 | reasoning | conditional, conjunction, character_trait, statement | covered |
| n13 | reasoning | conditional, character_trait, statement | covered |
| n14 | reasoning | conditional, conjunction, character_trait, statement, color_label::red, lexical_label | label-preserved |
| n15 | reasoning | conditional, conjunction, character_trait, statement | covered |
| n16 | reasoning | conditional, conjunction, character_trait, statement | covered |
| n17 | reasoning | conditional, character_trait, statement | covered |
| n18 | speech_act | ask | covered |
| n19 | constraint | requirement | covered |
| n20 | constraint | constraint_single_choice, requirement | covered |
| n21 | object | negation, subject, character_trait | covered |
| n22 | negation | negation, character_trait | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2, t1:s10, t1:s11, t1:s14 "red" → color_label::red (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
