Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    CLAIM has_attribute(attribute=lexical_label_2, subject="Bob") BY role_user STATUS asserted SOURCE "t1:s2" -> has_attribute_2 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_3 : TERM
    CLAIM has_attribute(attribute=lexical_label_3, subject="Bob") BY role_user STATUS asserted SOURCE "t1:s3" -> has_attribute_3 : CLAIM
    CLAIM has_attribute(attribute="young", subject="Bob") BY role_user STATUS asserted SOURCE "t1:s4" -> has_attribute_4 : CLAIM
    CLAIM has_attribute(attribute="big", subject="Dave") BY role_user STATUS asserted SOURCE "t1:s5" -> has_attribute_5 : CLAIM
    CLAIM has_attribute(attribute="nice", subject="Dave") BY role_user STATUS asserted SOURCE "t1:s6" -> has_attribute_6 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_3, subject="Dave") BY role_user STATUS asserted SOURCE "t1:s7" -> has_attribute_7 : CLAIM
    CLAIM has_attribute(attribute="nice", subject="Erin") BY role_user STATUS asserted SOURCE "t1:s8" -> has_attribute_8 : CLAIM
    CLAIM has_attribute(attribute="young", subject="Erin") BY role_user STATUS asserted SOURCE "t1:s9" -> has_attribute_9 : CLAIM
    CLAIM has_attribute(attribute="big", subject="Gary") BY role_user STATUS asserted SOURCE "t1:s10" -> has_attribute_10 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_3, subject="Gary") BY role_user STATUS asserted SOURCE "t1:s11" -> has_attribute_11 : CLAIM
    TERM character_trait(property="nice", value="true") -> character_trait_2 : TERM
    TERM character_trait(property="furry", value="true") -> character_trait_3 : TERM
    TERM character_trait(property="big", value="true") -> character_trait_4 : TERM
    TERM conjunction(items=[character_trait_2, character_trait_3]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=character_trait_4) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_2 : CLAIM
    TERM character_trait(property="green", value="true") -> character_trait_5 : TERM
    TERM character_trait(property="red", value="true") -> character_trait_6 : TERM
    TERM conjunction(items=[character_trait_5, character_trait_2]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=character_trait_6) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_3 : CLAIM
    TERM conditional(condition=character_trait_2, consequence=character_trait_3) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_4 : CLAIM
    TERM conditional(condition=character_trait_4, consequence=character_trait_3) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_5 : CLAIM
    TERM character_trait(property="young", value="true") -> character_trait_7 : TERM
    TERM conditional(condition=character_trait_3, consequence=character_trait_7) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_6 : CLAIM
    TERM conjunction(items=[character_trait_2, character_trait_7]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=character_trait_5) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_7 : CLAIM
    TERM conjunction(items=[character_trait_3, character_trait_4]) -> conjunction_5 : TERM
    TERM conditional(condition=conjunction_5, consequence=character_trait_5) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_8 : CLAIM
    TERM character_trait(property="kind", value="true") -> character_trait_8 : TERM
    TERM negation(target=character_trait_8) -> negation_2 : TERM
    TERM conjunction(items=[character_trait_6, character_trait_3]) -> conjunction_6 : TERM
    TERM conditional(condition=conjunction_6, consequence=negation_2) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_9 : CLAIM
    TERM negation(target=character_trait_3) -> negation_3 : TERM
    TERM conditional(condition=negation_3, consequence=character_trait_7) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_10 : CLAIM
    TERM negation(target=lexical_label_3) -> negation_4 : TERM
    CLAIM has_attribute(attribute=negation_4, subject="Erin") BY role_user STATUS asserted SOURCE "t1:s22" -> has_attribute_12 : CLAIM
    TERM subject(kind="theory") -> subject_2 : TERM
    TERM property_question(property="truth_value", subject="Erin") -> property_question_2 : TERM
    UTTER ask(target=property_question_2, constraints=[subject_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement, subject, ask | covered |
| n2 | claim | has_attribute, lexical_label, color_label::green | label-preserved |
| n3 | object | "Bob" | covered |
| n4 | object | color_label::green, lexical_label | label-preserved |
| n5 | claim | has_attribute, lexical_label, color_label::red | covered |
| n6 | object | color_label::red, lexical_label | label-preserved |
| n7 | claim | has_attribute | covered |
| n8 | claim | has_attribute | covered |
| n9 | object | "Dave" | covered |
| n10 | claim | has_attribute | covered |
| n11 | claim | has_attribute, lexical_label, color_label::red | covered |
| n12 | claim | has_attribute | covered |
| n13 | object | "Erin" | covered |
| n14 | claim | has_attribute | covered |
| n15 | claim | has_attribute | covered |
| n16 | object | "Gary" | covered |
| n17 | claim | has_attribute, lexical_label, color_label::red | covered |
| n18 | claim | character_trait, conjunction, conditional, statement | covered |
| n19 | claim | character_trait, conjunction, conditional, statement | label-preserved |
| n20 | claim | character_trait, conditional, statement | covered |
| n21 | claim | character_trait, conditional, statement | covered |
| n22 | claim | character_trait, conditional, statement | covered |
| n23 | claim | character_trait, conjunction, conditional, statement | covered |
| n24 | claim | character_trait, conjunction, conditional, statement | covered |
| n25 | claim | character_trait, conjunction, conditional, negation, statement | covered |
| n26 | negation | negation, character_trait | covered |
| n27 | claim | character_trait, conditional, negation, statement | covered |
| n28 | negation | negation | covered |
| n29 | speech_act | ask, property_question, statement | covered |
| n30 | constraint | subject | covered |
| n31 | constraint | subject | covered |
| n32 | claim | has_attribute, negation | covered |
| n33 | negation | negation, color_label::red | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "green" → color_label::green, t1:s3 "red" → color_label::red, t1:s7 "red" → color_label::red, t1:s11 "red" → color_label::red, t1:s13 "green" → color_label::green, "red" → color_label::red, t1:s22 "red" → color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
