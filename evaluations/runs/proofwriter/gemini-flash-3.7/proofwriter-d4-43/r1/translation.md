Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM character_trait(property="furry", value="furry") -> character_trait_2 : TERM
    CLAIM statement(fact=character_trait_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM character_trait(property="rough", value="rough") -> character_trait_3 : TERM
    CLAIM statement(fact=character_trait_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    CLAIM has_attribute(attribute=state_cold, subject="Dave") BY role_user STATUS asserted SOURCE "t1:s4" -> has_attribute_2 : CLAIM
    CLAIM has_attribute(attribute="quiet", subject="Dave") BY role_user STATUS asserted SOURCE "t1:s5" -> has_attribute_3 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    CLAIM has_attribute(attribute=lexical_label_2, subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s6" -> has_attribute_4 : CLAIM
    CLAIM has_attribute(attribute="furry", subject="Gary") BY role_user STATUS asserted SOURCE "t1:s7" -> has_attribute_5 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    CLAIM has_attribute(attribute=lexical_label_3, subject="Gary") BY role_user STATUS asserted SOURCE "t1:s8" -> has_attribute_6 : CLAIM
    TERM conditional(condition=lexical_label_2, consequence=lexical_label_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_4 : CLAIM
    TERM subject(kind=state_cold) -> subject_2 : TERM
    TERM conditional(condition=subject_2, consequence=lexical_label_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_5 : CLAIM
    TERM conjunction(items=[lexical_label_2, lexical_label_3]) -> conjunction_2 : TERM
    TERM negation(target=subject_2) -> negation_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=negation_2) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_6 : CLAIM
    TERM subject(kind=shape_round) -> subject_3 : TERM
    TERM subject(kind="quiet") -> subject_4 : TERM
    TERM conditional(condition=subject_3, consequence=subject_4) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_7 : CLAIM
    TERM subject(kind="rough", qualifier="Fiona") -> subject_5 : TERM
    TERM subject(kind=shape_round, qualifier="Fiona") -> subject_6 : TERM
    TERM conditional(condition=subject_5, consequence=subject_6) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_8 : CLAIM
    TERM subject(kind="quiet", qualifier="Fiona") -> subject_7 : TERM
    TERM conjunction(items=[subject_6, subject_7]) -> conjunction_3 : TERM
    TERM subject(kind="furry", qualifier="Fiona") -> subject_8 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_8) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_9 : CLAIM
    TERM subject(kind="rough") -> subject_9 : TERM
    TERM conditional(condition=lexical_label_3, consequence=subject_9) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_10 : CLAIM
    UTTER inform(target=statement_4)
    CLAIM has_attribute(attribute="quiet", subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s17" -> has_attribute_7 : CLAIM
    TERM test_condition(condition="Fiona is quiet", expected=TRUE) -> test_condition_2 : TERM
    UTTER ask(target=test_condition_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | inform | covered |
| n2 | claim | statement, character_trait | covered |
| n3 | claim | statement, character_trait | covered |
| n4 | claim | has_attribute, state_cold | covered |
| n5 | claim | has_attribute | covered |
| n6 | claim | has_attribute, lexical_label, color_label | covered |
| n7 | object | color_label::blue | label-preserved |
| n8 | claim | has_attribute | covered |
| n9 | claim | has_attribute, lexical_label, color_label | covered |
| n10 | object | color_label::green | label-preserved |
| n11 | claim | conditional, statement, lexical_label, color_label | label-preserved |
| n12 | object | color_label::blue | label-preserved |
| n13 | object | color_label::green | label-preserved |
| n14 | claim | conditional, statement, state_cold, lexical_label, color_label | covered |
| n15 | object | color_label::green | label-preserved |
| n16 | claim | conditional, statement, conjunction, negation, lexical_label, color_label, state_cold | covered |
| n17 | negation | negation, state_cold | covered |
| n18 | object | color_label::blue | label-preserved |
| n19 | object | color_label::green | label-preserved |
| n20 | claim | conditional, statement, shape_round | covered |
| n21 | claim | conditional, statement, shape_round | covered |
| n22 | claim | conditional, statement, conjunction, shape_round | covered |
| n23 | claim | conditional, statement, lexical_label, color_label, character_trait | covered |
| n24 | object | color_label::green | label-preserved |
| n25 | action | ask, test_condition, conditional, statement | covered |
| n26 | constraint | ask, test_condition, conjunction, subject | covered |
| n27 | constraint | test_condition, statement | covered |
| n28 | object | has_attribute, test_condition, ask, statement | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s17 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s6, t1:s8, t1:s9, t1:s10, t1:s11, t1:s15 "blue", "green" -> color_label::blue, color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
