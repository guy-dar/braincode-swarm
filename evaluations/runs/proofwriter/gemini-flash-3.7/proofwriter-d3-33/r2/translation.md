Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="furry", subject="Erin", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Erin", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="color", subject="Fiona", value=color_label::red) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
    CLAIM attribute_claim(property="smart", subject="Gary", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
    CLAIM attribute_claim(property="color", subject="Harry", value=color_label::blue) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
    CLAIM attribute_claim(property="furry", subject="Harry", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s8" -> attribute_claim_8 : CLAIM
    CLAIM attribute_claim(property="nice", subject="Harry", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s9" -> attribute_claim_9 : CLAIM
    CLAIM attribute_claim(property="quiet", subject="Harry", value=TRUE) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_10 : CLAIM
    CLAIM attribute_claim(property="color", subject="Harry", value=color_label::red) BY role_user STATUS asserted SOURCE "t1:s11" -> attribute_claim_11 : CLAIM
    TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
    TERM subject(kind="Gary", qualifier=lexical_label_2) -> subject_2 : TERM
    TERM subject(kind="Gary", qualifier="furry") -> subject_3 : TERM
    TERM conditional(condition=subject_2, consequence=subject_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_2 : CLAIM
    TERM subject(kind="person", qualifier="nice") -> subject_4 : TERM
    TERM subject(kind="person", qualifier="young") -> subject_5 : TERM
    TERM conditional(condition=subject_4, consequence=subject_5) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_3 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_3 : TERM
    TERM subject(kind="person", qualifier=lexical_label_3) -> subject_6 : TERM
    TERM conditional(condition=subject_6, consequence=subject_4) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_4 : CLAIM
    TERM subject(kind="person", qualifier="quiet") -> subject_7 : TERM
    TERM subject(kind="person", qualifier=lexical_label_2) -> subject_8 : TERM
    TERM conjunction(items=[subject_5, subject_8]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_7) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_5 : CLAIM
    TERM conjunction(items=[subject_4, subject_7]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_6) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_6 : CLAIM
    TERM subject(kind="person", qualifier="smart") -> subject_9 : TERM
    TERM conjunction(items=[subject_9, subject_7]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_6) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_7 : CLAIM
    TERM conditional(condition=subject_6, consequence=subject_7) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_8 : CLAIM
    TERM conjunction(items=[subject_6, subject_5]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=subject_8) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_9 : CLAIM
    TERM subject(kind="Harry", qualifier="quiet") -> subject_10 : TERM
    TERM subject(kind="Harry", qualifier="furry") -> subject_11 : TERM
    TERM conditional(condition=subject_10, consequence=subject_11) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_10 : CLAIM
    TERM subject(kind="Erin", qualifier=lexical_label_3) -> subject_12 : TERM
    TERM property_question(property="truth_value", subject=subject_12) -> property_question_2 : TERM
    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    UTTER ask(target=property_question_2, constraints=[constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | claim | attribute_claim | covered |
| n3 | claim | attribute_claim | covered |
| n4 | claim | attribute_claim, color_label::red | label-preserved |
| n5 | claim | attribute_claim | covered |
| n6 | claim | attribute_claim | covered |
| n7 | claim | attribute_claim, color_label::blue | label-preserved |
| n8 | claim | attribute_claim | covered |
| n9 | claim | attribute_claim | covered |
| n10 | claim | attribute_claim | covered |
| n11 | claim | attribute_claim, color_label::red | label-preserved |
| n12 | claim | conditional, lexical_label, statement, color_label::blue | label-preserved |
| n13 | claim | conditional, statement | covered |
| n14 | claim | conditional, lexical_label, statement, color_label::red | label-preserved |
| n15 | claim | conditional, conjunction, lexical_label, statement, color_label::blue | label-preserved |
| n16 | claim | conditional, conjunction, lexical_label, statement, color_label::red | label-preserved |
| n17 | claim | conditional, conjunction, lexical_label, statement, color_label::red | label-preserved |
| n18 | claim | conditional, lexical_label, statement, color_label::red | label-preserved |
| n19 | claim | conditional, conjunction, lexical_label, statement, color_label::blue, color_label::red | label-preserved |
| n20 | claim | conditional, statement | covered |
| n21 | action | ask, property_question | covered |
| n22 | constraint | property_question, subject | covered |
| n23 | constraint | ask, constraint_single_choice | covered |
| n24 | object | lexical_label, subject, color_label::red | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s4 "red" → color_label::red; t1:s7 "blue" → color_label::blue; t1:s11 "red" → color_label::red; t1:s12 "blue" → color_label::blue; t1:s14 "red" → color_label::red; t1:s15 "blue" → color_label::blue; t1:s16 "red" → color_label::red; t1:s17 "red" → color_label::red; t1:s18 "red" → color_label::red; t1:s19 "red" → color_label::red, "blue" → color_label::blue; t1:s22 "red" → color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
