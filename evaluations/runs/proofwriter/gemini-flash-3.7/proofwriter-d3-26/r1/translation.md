Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY "user" STATUS asserted SOURCE "t1:s1" -> statement_2 : CLAIM
    CLAIM has_attribute(attribute="kind", subject="Bob") BY "user" STATUS asserted SOURCE "t1:s2" -> has_attribute_2 : CLAIM
    CLAIM has_attribute(attribute="young", subject="Bob") BY "user" STATUS asserted SOURCE "t1:s3" -> has_attribute_3 : CLAIM
    CLAIM has_attribute(attribute="kind", subject="Dave") BY "user" STATUS asserted SOURCE "t1:s4" -> has_attribute_4 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    CLAIM has_attribute(attribute=lexical_label_2, subject="Dave") BY "user" STATUS asserted SOURCE "t1:s5" -> has_attribute_5 : CLAIM
    CLAIM has_attribute(attribute="big", subject="Fiona") BY "user" STATUS asserted SOURCE "t1:s6" -> has_attribute_6 : CLAIM
    CLAIM has_attribute(attribute="cold", subject="Fiona") BY "user" STATUS asserted SOURCE "t1:s7" -> has_attribute_7 : CLAIM
    CLAIM has_attribute(attribute="kind", subject="Fiona") BY "user" STATUS asserted SOURCE "t1:s8" -> has_attribute_8 : CLAIM
    CLAIM has_attribute(attribute="smart", subject="Fiona") BY "user" STATUS asserted SOURCE "t1:s9" -> has_attribute_9 : CLAIM
    CLAIM has_attribute(attribute="young", subject="Fiona") BY "user" STATUS asserted SOURCE "t1:s10" -> has_attribute_10 : CLAIM
    CLAIM has_attribute(attribute="big", subject="Harry") BY "user" STATUS asserted SOURCE "t1:s11" -> has_attribute_11 : CLAIM
    TERM subject(kind="person", qualifier="big") -> subject_3 : TERM
    TERM subject(kind="person", qualifier="smart") -> subject_4 : TERM
    TERM conjunction(items=[subject_3, subject_4]) -> conjunction_2 : TERM
    TERM subject(kind="person", qualifier=lexical_label_2) -> subject_5 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_5) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY "user" STATUS asserted SOURCE "t1:s12" -> statement_3 : CLAIM
    TERM subject(kind="person", qualifier="young") -> subject_6 : TERM
    TERM conjunction(items=[subject_6, subject_5]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_3) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY "user" STATUS asserted SOURCE "t1:s13" -> statement_4 : CLAIM
    TERM conditional(condition=subject_4, consequence=subject_5) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY "user" STATUS asserted SOURCE "t1:s14" -> statement_5 : CLAIM
    TERM subject(kind="person", qualifier="kind") -> subject_7 : TERM
    TERM conjunction(items=[subject_3, subject_7]) -> conjunction_4 : TERM
    TERM subject(kind="person", qualifier="rough") -> subject_8 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_8) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY "user" STATUS asserted SOURCE "t1:s15" -> statement_6 : CLAIM
    TERM conjunction(items=[subject_5, subject_3]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=subject_7) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY "user" STATUS asserted SOURCE "t1:s16" -> statement_7 : CLAIM
    TERM subject(kind="person", qualifier="cold") -> subject_9 : TERM
    TERM conditional(condition=subject_6, consequence=subject_9) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY "user" STATUS asserted SOURCE "t1:s17" -> statement_8 : CLAIM
    TERM conditional(condition=subject_7, consequence=subject_4) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY "user" STATUS asserted SOURCE "t1:s18" -> statement_9 : CLAIM
    TERM conjunction(items=[subject_8, subject_4]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=subject_6) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY "user" STATUS asserted SOURCE "t1:s19" -> statement_10 : CLAIM
    TERM conditional(condition=subject_3, consequence=subject_4) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY "user" STATUS asserted SOURCE "t1:s20" -> statement_11 : CLAIM
    TERM requirement(property="basis", value=subject_2) -> requirement_2 : TERM
    TERM requirement(property="response_format", value="truth_value") -> requirement_3 : TERM
    TERM subject(kind="Dave", qualifier="rough") -> subject_10 : TERM
    TERM negation(target=subject_10) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY "user" STATUS hypothesized SOURCE "t1:s22" -> statement_12 : CLAIM
    UTTER ask(target=negation_2, constraints=[requirement_2, requirement_3])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement, subject | covered |
| n2 | claim | has_attribute | covered |
| n3 | claim | has_attribute | covered |
| n4 | claim | has_attribute | covered |
| n5 | claim | has_attribute | covered |
| n6 | constraint | color_label::red | label-preserved |
| n7 | claim | has_attribute | covered |
| n8 | claim | has_attribute | covered |
| n9 | claim | has_attribute | covered |
| n10 | claim | has_attribute | covered |
| n11 | claim | has_attribute | covered |
| n12 | claim | has_attribute | covered |
| n13 | claim | statement, conditional, conjunction, subject | covered |
| n14 | constraint | color_label::red | label-preserved |
| n15 | claim | statement, conditional, conjunction, subject | covered |
| n16 | constraint | color_label::red | label-preserved |
| n17 | claim | statement, conditional, subject | covered |
| n18 | constraint | color_label::red | label-preserved |
| n19 | claim | statement, conditional, conjunction, subject | covered |
| n20 | claim | statement, conditional, conjunction, subject | covered |
| n21 | constraint | color_label::red | label-preserved |
| n22 | claim | statement, conditional, subject | covered |
| n23 | claim | statement, conditional, subject | covered |
| n24 | claim | statement, conditional, conjunction, subject | covered |
| n25 | claim | statement, conditional, subject | covered |
| n26 | speech_act | ask | covered |
| n27 | constraint | requirement, subject | covered |
| n28 | constraint | requirement | covered |
| n29 | claim | statement, negation, subject | covered |
| n30 | negation | negation | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is fully represented
- Opaque-text spans: none
- Label-preserved spans: t1:s5, t1:s12, t1:s13, t1:s14, t1:s16 "red" → color_label::red (open-group color label)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
