Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM character(name="Charlie") -> character_charlie : TERM
    TERM character(name="Erin") -> character_erin : TERM
    TERM character(name="Gary") -> character_gary : TERM
    TERM character(name="Harry") -> character_harry : TERM # PROPOSED: S1
    TERM lexical_label(value=color_label::red) -> lexical_label_red : TERM
    CLAIM has_attribute(attribute="furry", subject=character_charlie) BY role_user STATUS asserted SOURCE "t1:s2" -> has_attribute_2 : CLAIM
    CLAIM has_attribute(attribute="furry", subject=character_erin) BY role_user STATUS asserted SOURCE "t1:s3" -> has_attribute_3 : CLAIM
    CLAIM has_attribute(attribute="young", subject=character_erin) BY role_user STATUS asserted SOURCE "t1:s4" -> has_attribute_4 : CLAIM
    CLAIM has_attribute(attribute="furry", subject=character_gary) BY role_user STATUS asserted SOURCE "t1:s5" -> has_attribute_5 : CLAIM
    CLAIM has_attribute(attribute="nice", subject=character_gary) BY role_user STATUS asserted SOURCE "t1:s6" -> has_attribute_6 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_red, subject=character_gary) BY role_user STATUS asserted SOURCE "t1:s7" -> has_attribute_7 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_red, subject=character_harry) BY role_user STATUS asserted SOURCE "t1:s8" -> has_attribute_8 : CLAIM
    TERM entity_attribute(entity="person", property="nice") -> entity_attribute_2 : TERM # PROPOSED: S1
    TERM entity_attribute(entity="person", property="cold") -> entity_attribute_3 : TERM # PROPOSED: S1
    TERM conditional(condition=entity_attribute_2, consequence=entity_attribute_3) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
    TERM entity_attribute(entity="person", property="kind") -> entity_attribute_4 : TERM # PROPOSED: S1
    TERM entity_attribute(entity="person", property=lexical_label_red) -> entity_attribute_5 : TERM # PROPOSED: S1
    TERM negation(target=entity_attribute_5) -> negation_2 : TERM
    TERM conditional(condition=entity_attribute_4, consequence=negation_2) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
    TERM entity_attribute(entity=character_charlie, property="rough") -> entity_attribute_6 : TERM # PROPOSED: S1
    TERM entity_attribute(entity=character_charlie, property="furry") -> entity_attribute_7 : TERM # PROPOSED: S1
    TERM conjunction(items=[entity_attribute_6, entity_attribute_7]) -> conjunction_2 : TERM
    TERM entity_attribute(entity=character_charlie, property=lexical_label_red) -> entity_attribute_8 : TERM # PROPOSED: S1
    TERM conditional(condition=conjunction_2, consequence=entity_attribute_8) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
    TERM entity_attribute(entity="person", property="furry") -> entity_attribute_9 : TERM # PROPOSED: S1
    TERM conditional(condition=entity_attribute_3, consequence=entity_attribute_9) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_5 : CLAIM
    TERM entity_attribute(entity=character_erin, property="cold") -> entity_attribute_10 : TERM # PROPOSED: S1
    TERM entity_attribute(entity=character_erin, property="kind") -> entity_attribute_11 : TERM # PROPOSED: S1
    TERM conditional(condition=entity_attribute_10, consequence=entity_attribute_11) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_6 : CLAIM
    TERM entity_attribute(entity="person", property="young") -> entity_attribute_12 : TERM # PROPOSED: S1
    TERM entity_attribute(entity="person", property="rough") -> entity_attribute_13 : TERM # PROPOSED: S1
    TERM conditional(condition=entity_attribute_12, consequence=entity_attribute_13) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_7 : CLAIM
    TERM conditional(condition=entity_attribute_13, consequence=entity_attribute_2) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_8 : CLAIM
    CLAIM has_attribute(attribute="furry", subject=character_harry) BY role_user STATUS asserted SOURCE "t1:s17" -> has_attribute_9 : CLAIM
    TERM deduction_query(claim=has_attribute_9, choices=["True", "False", "Unknown"], scope="theory") -> deduction_query_2 : TERM # PROPOSED: S2
    UTTER ask(target=deduction_query_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | conditional, statement | covered |
| n2 | claim | has_attribute, statement | covered |
| n3 | object | character | covered |
| n4 | claim | has_attribute, statement | covered |
| n5 | object | character | covered |
| n6 | claim | has_attribute, statement | covered |
| n7 | claim | has_attribute, statement | covered |
| n8 | object | character | covered |
| n9 | claim | has_attribute, statement | covered |
| n10 | claim | has_attribute, statement | covered |
| n11 | object | color_label::red | label-preserved |
| n12 | claim | has_attribute, statement | covered |
| n13 | object | character (PROPOSED: S1) | proposed |
| n14 | object | color_label::red | label-preserved |
| n15 | reasoning | entity_attribute (PROPOSED: S1), conditional, statement | proposed |
| n16 | reasoning | entity_attribute (PROPOSED: S1), conditional, statement | proposed |
| n17 | negation | negation, color_label::red | covered |
| n18 | reasoning | entity_attribute (PROPOSED: S1), conditional, conjunction, statement | proposed |
| n19 | reasoning | entity_attribute (PROPOSED: S1), conditional, statement | proposed |
| n20 | reasoning | entity_attribute (PROPOSED: S1), conditional, statement | proposed |
| n21 | reasoning | entity_attribute (PROPOSED: S1), conditional, statement | proposed |
| n22 | reasoning | entity_attribute (PROPOSED: S1), conditional, statement, has_attribute | proposed |
| n23 | speech_act | ask, deduction_query (PROPOSED: S2) | proposed |
| n24 | constraint | deduction_query (PROPOSED: S2) | proposed |
| n25 | constraint | deduction_query (PROPOSED: S2) | proposed |
| n26 | claim | has_attribute, statement | covered |

## Why the translation failed

- n13 "Harry": Candidate retrieval yielded no character/entity constructors (only topic_spider_man_2, united_kingdom, etc.).
- n15, n16, n18, n19, n20, n21, n22: The logical premises represent conditionals relating descriptive propositions ("if X then Y"). The existing `conditional` constructor connects two `TERM`s, but the glossary lacks a TERM constructor for associating a subject/entity with an attribute/property (`entity_attribute` proposed in S1). Existing `has_attribute` is a `CLAIM`, which cannot be passed as a `condition` or `consequence` argument to `conditional`.
- n23, n24, n25: The question asks for a ternary deduction judgment (True / False / Unknown) based strictly on the provided logical theory. The glossary lacks a constructor to represent closed-theory deduction queries with discrete truth choices (`deduction_query` proposed in S2).

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: every segment t1:s1–t1:s17 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s7 "red" -> color_label::red; t1:s8 "red" -> color_label::red
- Missing constructs: S1 entity_attribute constructor; S2 deduction_query constructor
- Unresolved ambiguities: none
- Check: `rag check` reported proposed needs and unknown symbols
