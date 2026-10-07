Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    CLAIM has_attribute(attribute=shape_round, subject="Anne") BY role_user STATUS asserted SOURCE "t1:s2" -> has_attribute_2 : CLAIM
    CLAIM has_attribute(attribute=size_large, subject="Bob") BY role_user STATUS asserted SOURCE "t1:s3" -> has_attribute_3 : CLAIM
    CLAIM has_attribute(attribute=shape_round, subject="Bob") BY role_user STATUS asserted SOURCE "t1:s4" -> has_attribute_4 : CLAIM
    TERM lexical_label(value=color_label::white) -> lexical_label_2 : TERM
    CLAIM has_attribute(attribute=lexical_label_2, subject="Bob") BY role_user STATUS asserted SOURCE "t1:s5" -> has_attribute_5 : CLAIM
    CLAIM has_attribute(attribute=size_large, subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s6" -> has_attribute_6 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    CLAIM has_attribute(attribute=lexical_label_3, subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s7" -> has_attribute_7 : CLAIM
    CLAIM has_attribute(attribute=property_label::kind, subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s8" -> has_attribute_8 : CLAIM # PROPOSED: S1, REFINED: S2
    CLAIM has_attribute(attribute=shape_round, subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s9" -> has_attribute_9 : CLAIM
    CLAIM has_attribute(attribute=property_label::young, subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s10" -> has_attribute_10 : CLAIM # PROPOSED: S1, REFINED: S2
    CLAIM has_attribute(attribute=property_label::nice, subject="Gary") BY role_user STATUS asserted SOURCE "t1:s11" -> has_attribute_11 : CLAIM # PROPOSED: S1, REFINED: S2
    CLAIM has_attribute(attribute=shape_round, subject="Gary") BY role_user STATUS asserted SOURCE "t1:s12" -> has_attribute_12 : CLAIM
    TERM subject(kind=property_label::nice) -> subject_3 : TERM # PROPOSED: S1, REFINED: S3
    TERM subject(kind=size_large) -> subject_4 : TERM
    TERM conjunction(items=[subject_3, subject_4]) -> conjunction_2 : TERM
    TERM subject(kind=property_label::kind) -> subject_5 : TERM # PROPOSED: S1, REFINED: S3
    TERM conditional(condition=conjunction_2, consequence=subject_5) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_2 : CLAIM
    TERM subject(kind="Anne", qualifier=shape_round) -> subject_6 : TERM
    TERM subject(kind="Anne", qualifier=property_label::young) -> subject_7 : TERM # PROPOSED: S1, REFINED: S3
    TERM conjunction(items=[subject_6, subject_7]) -> conjunction_3 : TERM
    TERM subject(kind="Anne", qualifier=lexical_label_3) -> subject_8 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_8) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_3 : CLAIM
    TERM conditional(condition=subject_4, consequence=subject_3) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_4 : CLAIM
    TERM subject(kind="thing", qualifier=lexical_label_2) -> subject_9 : TERM
    TERM conditional(condition=subject_5, consequence=subject_9) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_5 : CLAIM
    TERM subject(kind="Anne", qualifier=property_label::kind) -> subject_10 : TERM # PROPOSED: S1, REFINED: S3
    TERM conjunction(items=[subject_10, subject_6]) -> conjunction_4 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_7) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_6 : CLAIM
    TERM subject(kind="thing", qualifier=lexical_label_3) -> subject_11 : TERM
    TERM conjunction(items=[subject_11, subject_9]) -> conjunction_5 : TERM
    TERM subject(kind=shape_round) -> subject_12 : TERM
    TERM conditional(condition=conjunction_5, consequence=subject_12) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_7 : CLAIM
    TERM conditional(condition=subject_12, consequence=subject_4) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_8 : CLAIM
    TERM subject(kind="Anne", qualifier=lexical_label_2) -> subject_13 : TERM
    TERM negation(target=subject_13) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS hypothesized SOURCE "t1:s21" -> statement_9 : CLAIM
    UTTER ask(target=negation_2, topic=subject_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject, ask, conjunction | covered |
| n2 | claim | has_attribute, shape_round | covered |
| n3 | claim | has_attribute, size_large, statement | covered |
| n4 | claim | has_attribute, shape_round | covered |
| n5 | claim | has_attribute, statement, color_label::white | covered |
| n6 | claim | has_attribute, size_large, statement | covered |
| n7 | claim | has_attribute, statement, color_label::green | covered |
| n8 | claim | has_attribute, statement, property_label::kind (PROPOSED: S1, REFINED: S2) | proposed |
| n9 | claim | has_attribute, shape_round | covered |
| n10 | claim | has_attribute, property_label::young (PROPOSED: S1, REFINED: S2) | proposed |
| n11 | claim | has_attribute, property_label::nice (PROPOSED: S1, REFINED: S2) | proposed |
| n12 | claim | has_attribute, shape_round | covered |
| n13 | reasoning | conditional, conjunction, statement, subject, size_large, property_label::nice, property_label::kind (PROPOSED: S1, REFINED: S3) | proposed |
| n14 | reasoning | conditional, conjunction, statement, subject, shape_round, color_label::green, property_label::young (PROPOSED: S1, REFINED: S3) | proposed |
| n15 | reasoning | conditional, statement, subject, size_large, property_label::nice (PROPOSED: S1, REFINED: S3) | proposed |
| n16 | reasoning | conditional, statement, subject, color_label::white, property_label::kind (PROPOSED: S1, REFINED: S3) | proposed |
| n17 | reasoning | conditional, conjunction, statement, subject, shape_round, property_label::kind, property_label::young (PROPOSED: S1, REFINED: S3) | proposed |
| n18 | reasoning | conditional, conjunction, statement, subject, shape_round, color_label::white, color_label::green | covered |
| n19 | reasoning | conditional, statement, subject, shape_round, size_large | covered |
| n20 | action | statement | covered |
| n21 | constraint | subject, conjunction | covered |
| n22 | constraint | ask | covered |
| n23 | object | statement, negation, color_label::white | covered |
| n24 | negation | negation, color_label::white | covered |
| n25 | object | color_label::white | label-preserved |
| n26 | object | color_label::green | label-preserved |

## Why the translation failed

- n8, n13, n16, n17 "kind": search "kind" → object_label, animal_label, style_catchy, tone_polite; widen → no general descriptor or value group for personality traits/behavioral attributes. Proposed S1 (property_label) and S2/S3.
- n10, n14, n17 "young": search "young" → constraint_17_plus (an age-rating restriction), size_small; widen → no descriptor or value group for age/developmental attributes. Proposed S1 (property_label) and S2/S3.
- n11, n13, n15 "nice": search "nice" → tone_polite, well_wishes, style_catchy, condition_perfect; widen → no descriptor or value group for pleasantness/personality traits. Proposed S1 (property_label) and S2/S3.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: every segment t1:s1–t1:s21 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s5 "white" → color_label::white; t1:s7 "green" → color_label::green; t1:s14 "green" → color_label::green; t1:s16 "white" → color_label::white; t1:s18 "green" → color_label::green, "white" → color_label::white; t1:s21 "white" → color_label::white
- Missing constructs: S1 property_label lexical-group for open qualitative entity properties/traits; S2 refinement of has_attribute to accept ATOM[property_label]; S3 refinement of subject to accept ATOM[property_label] in kind and qualifier
- Unresolved ambiguities: none
- Check: `rag check` reported 4 proposed/refined needs (n8, n10, n11, n13), 0 unknown symbols outside proposed constructs
