Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="furry", subject="Bob", value=TRUE) BY user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="young", subject="Bob", value=TRUE) BY user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="big", subject="Charlie", value=TRUE) BY user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="furry", subject="Dave", value=TRUE) BY user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="young", subject="Dave", value=TRUE) BY user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="nice", subject="Erin", value=TRUE) BY user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="young", subject="Erin", value=TRUE) BY user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    TERM requirement(property="furry", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="smart", value=TRUE) -> requirement_3 : TERM
    TERM conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
    TERM requirement(property="big", value=TRUE) -> requirement_4 : TERM
    TERM conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM lexical_label(value=color_label::white) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_5 : TERM
    TERM conjunction(items=[requirement_5, requirement_4]) -> conjunction_3 : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    TERM requirement(property="color", value=lexical_label_3) -> requirement_6 : TERM
    TERM conditional(condition=conjunction_3, consequence=requirement_6) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM conditional(condition=requirement_5, consequence=requirement_2) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM requirement(property="nice", value=TRUE) -> requirement_7 : TERM
    TERM conjunction(items=[requirement_7, requirement_2]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=requirement_3) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM conjunction(items=[requirement_2, requirement_6]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=requirement_5) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM requirement(property="young", value=TRUE) -> requirement_8 : TERM
    TERM conjunction(items=[requirement_8, requirement_4]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=requirement_5) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM subject(kind="Erin", qualifier="young") -> subject_2 : TERM
    TERM subject(kind="Erin", qualifier="furry") -> subject_3 : TERM
    TERM conditional(condition=subject_2, consequence=subject_3) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY user STATUS asserted SOURCE "t1:s15" -> statement_8 : CLAIM
    CLAIM attribute_claim(property="color", subject="Erin", value=lexical_label_2) BY user STATUS asserted SOURCE "t1:s17" -> attribute_claim_9 : CLAIM
    TERM requirement(property="theory_only", value=TRUE) -> requirement_9 : TERM
    TERM requirement(property="evaluation_domain", value="true_false_unknown") -> requirement_10 : TERM
    UTTER ask(target=attribute_claim_9, constraints=[requirement_9, requirement_10])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement | covered |
| n2 | claim | attribute_claim | covered |
| n3 | claim | attribute_claim | covered |
| n4 | claim | attribute_claim | covered |
| n5 | claim | attribute_claim | covered |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim | covered |
| n8 | claim | attribute_claim | covered |
| n9 | reasoning | conditional, conjunction, requirement, statement | covered |
| n10 | reasoning | color_label::green, color_label::white, conditional, conjunction, lexical_label, requirement, statement | label-preserved |
| n11 | constraint | color_label::white, lexical_label | label-preserved |
| n12 | constraint | color_label::green, lexical_label | label-preserved |
| n13 | reasoning | conditional, requirement, statement | covered |
| n14 | constraint | color_label::white, lexical_label | label-preserved |
| n15 | reasoning | conditional, conjunction, requirement, statement | covered |
| n16 | reasoning | color_label::green, color_label::white, conditional, conjunction, lexical_label, requirement, statement | label-preserved |
| n17 | constraint | color_label::green, lexical_label | label-preserved |
| n18 | constraint | color_label::white, lexical_label | label-preserved |
| n19 | reasoning | conditional, conjunction, requirement, statement | covered |
| n20 | constraint | color_label::white, lexical_label | label-preserved |
| n21 | reasoning | conditional, statement, subject | covered |
| n22 | speech_act | ask | covered |
| n23 | constraint | requirement | covered |
| n24 | constraint | requirement | covered |
| n25 | claim | attribute_claim | covered |
| n26 | constraint | color_label::white, lexical_label | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s17 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s10 "white" -> color_label::white, t1:s10 "green" -> color_label::green, t1:s11 "white" -> color_label::white, t1:s13 "green" -> color_label::green, t1:s13 "white" -> color_label::white, t1:s14 "white" -> color_label::white, t1:s17 "white" -> color_label::white
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
