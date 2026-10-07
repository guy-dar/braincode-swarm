Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    CLAIM has_attribute(attribute=lexical_label_2, subject="Dave") BY role_user STATUS asserted SOURCE "t1:s2" -> has_attribute_2 : CLAIM
    CLAIM has_attribute(attribute="quiet", subject="Dave") BY role_user STATUS asserted SOURCE "t1:s3" -> has_attribute_3 : CLAIM
    CLAIM has_attribute(attribute="young", subject="Dave") BY role_user STATUS asserted SOURCE "t1:s4" -> has_attribute_4 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_3 : TERM
    CLAIM has_attribute(attribute=lexical_label_3, subject="Erin") BY role_user STATUS asserted SOURCE "t1:s5" -> has_attribute_5 : CLAIM
    TERM lexical_label(value=color_label::white) -> lexical_label_4 : TERM
    CLAIM has_attribute(attribute=lexical_label_4, subject="Erin") BY role_user STATUS asserted SOURCE "t1:s6" -> has_attribute_6 : CLAIM
    CLAIM has_attribute(attribute="quiet", subject="Gary") BY role_user STATUS asserted SOURCE "t1:s7" -> has_attribute_7 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_3, subject="Harry") BY role_user STATUS asserted SOURCE "t1:s8" -> has_attribute_8 : CLAIM
    TERM subject(kind="thing", qualifier=state_cold) -> subject_2 : TERM
    TERM subject(kind="thing", qualifier=lexical_label_2) -> subject_3 : TERM
    TERM conjunction(items=[subject_2, subject_3]) -> conjunction_2 : TERM
    TERM subject(kind="thing", qualifier="kind") -> subject_4 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM subject(kind="thing", qualifier="quiet") -> subject_5 : TERM
    TERM conditional(condition=subject_5, consequence=subject_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM conditional(condition=subject_2, consequence=subject_4) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM conjunction(items=[subject_5, subject_4]) -> conjunction_3 : TERM
    TERM subject(kind="thing", qualifier=lexical_label_4) -> subject_6 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_6) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM conditional(condition=subject_2, consequence=subject_5) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM subject(kind="Dave", qualifier=state_cold) -> subject_7 : TERM
    TERM subject(kind="Dave", qualifier="kind") -> subject_8 : TERM
    TERM conditional(condition=subject_7, consequence=subject_8) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM conditional(condition=subject_3, consequence=subject_2) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_8 : CLAIM
    TERM conjunction(items=[subject_2, subject_6]) -> conjunction_4 : TERM
    TERM subject(kind="thing", qualifier="young") -> subject_9 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_9) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_9 : CLAIM
    TERM subject(kind="Harry", qualifier="kind") -> subject_10 : TERM
    TERM negation(target=subject_10) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS hypothesized SOURCE "t1:s18" -> statement_10 : CLAIM
    UTTER ask(target=negation_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, conditional, conjunction, subject | covered |
| n2 | claim | color_label, has_attribute, lexical_label | covered |
| n3 | object | Dave | covered |
| n4 | constraint | color_label::green, lexical_label | label-preserved |
| n5 | claim | has_attribute | covered |
| n6 | object | Dave | covered |
| n7 | constraint | quiet | covered |
| n8 | claim | has_attribute | covered |
| n9 | object | Dave | covered |
| n10 | constraint | young | covered |
| n11 | claim | color_label, has_attribute, lexical_label | covered |
| n12 | object | Erin | covered |
| n13 | constraint | color_label::blue, lexical_label | label-preserved |
| n14 | claim | color_label, has_attribute, lexical_label | covered |
| n15 | object | Erin | covered |
| n16 | constraint | color_label::white, lexical_label | label-preserved |
| n17 | claim | has_attribute | covered |
| n18 | object | Gary | covered |
| n19 | constraint | quiet | covered |
| n20 | claim | color_label, has_attribute, lexical_label | covered |
| n21 | object | Harry | covered |
| n22 | constraint | color_label::blue, lexical_label | label-preserved |
| n23 | claim | color_label, conditional, conjunction, statement, state_cold | covered |
| n24 | claim | color_label, conditional, statement | label-preserved |
| n25 | claim | conditional, statement, state_cold | covered |
| n26 | claim | color_label, conditional, conjunction, statement | covered |
| n27 | claim | conditional, statement, state_cold | covered |
| n28 | claim | conditional, statement, state_cold | covered |
| n29 | claim | color_label, conditional, statement, state_cold | covered |
| n30 | claim | color_label, conditional, conjunction, statement, state_cold | covered |
| n31 | speech_act | ask, statement | covered |
| n32 | constraint | subject | covered |
| n33 | constraint | ask | covered |
| n34 | claim | has_attribute, statement | covered |
| n35 | negation | negation | covered |
| n36 | object | Harry | covered |
| n37 | constraint | kind | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s18 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "green" → color_label::green; t1:s5 "blue" → color_label::blue; t1:s6 "white" → color_label::white; t1:s8 "blue" → color_label::blue; t1:s10 "green" → color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
