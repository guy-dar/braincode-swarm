Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    TERM lexical_label(value=object_label::bob) -> lexical_label_2 : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    CLAIM has_attribute(attribute=lexical_label_3, subject=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s2" -> has_attribute_2 : CLAIM
    TERM lexical_label(value=color_label::white) -> lexical_label_4 : TERM
    CLAIM has_attribute(attribute=lexical_label_4, subject=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s3" -> has_attribute_3 : CLAIM
    TERM lexical_label(value=object_label::dave) -> lexical_label_5 : TERM
    TERM lexical_label(value=color_label::blue) -> lexical_label_6 : TERM
    CLAIM has_attribute(attribute=lexical_label_6, subject=lexical_label_5) BY role_user STATUS asserted SOURCE "t1:s4" -> has_attribute_4 : CLAIM
    CLAIM has_state(state=state_cold, subject=lexical_label_5) BY role_user STATUS asserted SOURCE "t1:s5" -> has_state_2 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_3, subject=lexical_label_5) BY role_user STATUS asserted SOURCE "t1:s6" -> has_attribute_5 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_4, subject=lexical_label_5) BY role_user STATUS asserted SOURCE "t1:s7" -> has_attribute_6 : CLAIM
    TERM lexical_label(value=object_label::fiona) -> lexical_label_7 : TERM
    CLAIM has_state(state=state_cold, subject=lexical_label_7) BY role_user STATUS asserted SOURCE "t1:s8" -> has_state_3 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_3, subject=lexical_label_7) BY role_user STATUS asserted SOURCE "t1:s9" -> has_attribute_7 : CLAIM
    CLAIM has_attribute(attribute=lexical_label_4, subject=lexical_label_7) BY role_user STATUS asserted SOURCE "t1:s10" -> has_attribute_8 : CLAIM
    TERM lexical_label(value=trait_label::young) -> lexical_label_8 : TERM   # PROPOSED: S1, S2
    CLAIM has_attribute(attribute=lexical_label_8, subject=lexical_label_7) BY role_user STATUS asserted SOURCE "t1:s11" -> has_attribute_9 : CLAIM   # PROPOSED: S1, S2
    TERM lexical_label(value=object_label::gary) -> lexical_label_9 : TERM
    TERM lexical_label(value=trait_label::kind) -> lexical_label_10 : TERM   # PROPOSED: S1, S2
    CLAIM has_attribute(attribute=lexical_label_10, subject=lexical_label_9) BY role_user STATUS asserted SOURCE "t1:s12" -> has_attribute_10 : CLAIM   # PROPOSED: S1, S2
    CLAIM has_attribute(attribute=lexical_label_4, subject=lexical_label_9) BY role_user STATUS asserted SOURCE "t1:s13" -> has_attribute_11 : CLAIM
    TERM lexical_label(value=trait_label::furry) -> lexical_label_11 : TERM   # PROPOSED: S1, S2
    TERM requirement(property="cold", value=TRUE) -> requirement_2 : TERM
    TERM conjunction(items=[requirement_2, lexical_label_4]) -> conjunction_2 : TERM
    TERM conditional(condition=conjunction_2, consequence=lexical_label_11) -> conditional_2 : TERM   # PROPOSED: S1, S2
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_2 : CLAIM   # PROPOSED: S1, S2
    TERM conditional(condition=lexical_label_11, consequence=lexical_label_3) -> conditional_3 : TERM   # PROPOSED: S1, S2
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_3 : CLAIM   # PROPOSED: S1, S2
    TERM conditional(condition=requirement_2, consequence=lexical_label_8) -> conditional_4 : TERM   # PROPOSED: S1, S2
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_4 : CLAIM   # PROPOSED: S1, S2
    TERM conjunction(items=[lexical_label_10, lexical_label_8]) -> conjunction_3 : TERM   # PROPOSED: S1, S2
    TERM conditional(condition=conjunction_3, consequence=lexical_label_6) -> conditional_5 : TERM   # PROPOSED: S1, S2
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_5 : CLAIM   # PROPOSED: S1, S2
    TERM conditional(condition=lexical_label_11, consequence=lexical_label_6) -> conditional_6 : TERM   # PROPOSED: S1, S2
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_6 : CLAIM   # PROPOSED: S1, S2
    TERM conjunction(items=[lexical_label_4, lexical_label_10]) -> conjunction_4 : TERM   # PROPOSED: S1, S2
    TERM conditional(condition=conjunction_4, consequence=lexical_label_8) -> conditional_7 : TERM   # PROPOSED: S1, S2
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_7 : CLAIM   # PROPOSED: S1, S2
    TERM conjunction(items=[lexical_label_10, lexical_label_6]) -> conjunction_5 : TERM   # PROPOSED: S1, S2
    TERM conditional(condition=conjunction_5, consequence=requirement_2) -> conditional_8 : TERM   # PROPOSED: S1, S2
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_8 : CLAIM   # PROPOSED: S1, S2
    TERM conditional(condition=lexical_label_6, consequence=lexical_label_10) -> conditional_9 : TERM   # PROPOSED: S1, S2
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_9 : CLAIM   # PROPOSED: S1, S2
    CLAIM has_attribute(attribute=lexical_label_10, subject=lexical_label_2) BY role_user STATUS hypothesized SOURCE "t1:s23" -> has_attribute_12 : CLAIM   # PROPOSED: S1, S2
    TERM property_question(property="truth_value", subject=lexical_label_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject | covered |
| n2 | claim | has_attribute, color_label::green | covered |
| n3 | object | object_label::bob | label-preserved |
| n4 | constraint | color_label::green | label-preserved |
| n5 | claim | has_attribute, color_label::white | covered |
| n6 | object | object_label::bob | label-preserved |
| n7 | constraint | color_label::white | label-preserved |
| n8 | claim | has_attribute, color_label::blue | covered |
| n9 | object | object_label::dave | label-preserved |
| n10 | constraint | color_label::blue | label-preserved |
| n11 | claim | has_state, state_cold | covered |
| n12 | object | object_label::dave | label-preserved |
| n13 | constraint | state_cold | covered |
| n14 | claim | has_attribute, color_label::green | covered |
| n15 | object | object_label::dave | label-preserved |
| n16 | constraint | color_label::green | label-preserved |
| n17 | claim | has_attribute, color_label::white | covered |
| n18 | object | object_label::dave | label-preserved |
| n19 | constraint | color_label::white | label-preserved |
| n20 | claim | has_state, state_cold | covered |
| n21 | object | object_label::fiona | label-preserved |
| n22 | constraint | state_cold | covered |
| n23 | claim | has_attribute, color_label::green | covered |
| n24 | object | object_label::fiona | label-preserved |
| n25 | constraint | color_label::green | label-preserved |
| n26 | claim | has_attribute, color_label::white | covered |
| n27 | object | object_label::fiona | label-preserved |
| n28 | constraint | color_label::white | label-preserved |
| n29 | claim | has_attribute, trait_label::young (PROPOSED: S1, S2) | proposed |
| n30 | object | object_label::fiona | label-preserved |
| n31 | constraint | trait_label::young (PROPOSED: S1) | proposed |
| n32 | claim | has_attribute, trait_label::kind (PROPOSED: S1, S2) | proposed |
| n33 | object | object_label::gary | label-preserved |
| n34 | constraint | trait_label::kind (PROPOSED: S1) | proposed |
| n35 | claim | has_attribute, color_label::white | covered |
| n36 | object | object_label::gary | label-preserved |
| n37 | constraint | color_label::white | label-preserved |
| n38 | reasoning | conditional, conjunction, statement, trait_label::furry (PROPOSED: S1, S2) | proposed |
| n39 | constraint | requirement, state_cold | covered |
| n40 | constraint | color_label::white | label-preserved |
| n41 | constraint | trait_label::furry (PROPOSED: S1) | proposed |
| n42 | reasoning | conditional, statement, trait_label::furry (PROPOSED: S1, S2) | proposed |
| n43 | constraint | trait_label::furry (PROPOSED: S1) | proposed |
| n44 | constraint | color_label::green | label-preserved |
| n45 | reasoning | conditional, statement, trait_label::young (PROPOSED: S1, S2) | proposed |
| n46 | constraint | requirement, state_cold | covered |
| n47 | constraint | trait_label::young (PROPOSED: S1) | proposed |
| n48 | reasoning | conditional, conjunction, statement, trait_label::kind, trait_label::young (PROPOSED: S1, S2) | proposed |
| n49 | constraint | trait_label::kind (PROPOSED: S1) | proposed |
| n50 | constraint | trait_label::young (PROPOSED: S1) | proposed |
| n51 | constraint | color_label::blue | label-preserved |
| n52 | reasoning | conditional, statement, trait_label::furry (PROPOSED: S1, S2) | proposed |
| n53 | constraint | trait_label::furry (PROPOSED: S1) | proposed |
| n54 | constraint | color_label::blue | label-preserved |
| n55 | reasoning | conditional, conjunction, statement, trait_label::kind, trait_label::young (PROPOSED: S1, S2) | proposed |
| n56 | constraint | color_label::white | label-preserved |
| n57 | constraint | trait_label::kind (PROPOSED: S1) | proposed |
| n58 | constraint | trait_label::young (PROPOSED: S1) | proposed |
| n59 | reasoning | conditional, conjunction, statement, trait_label::kind (PROPOSED: S1, S2) | proposed |
| n60 | constraint | trait_label::kind (PROPOSED: S1) | proposed |
| n61 | constraint | color_label::blue | label-preserved |
| n62 | constraint | requirement, state_cold | covered |
| n63 | reasoning | conditional, statement, trait_label::kind (PROPOSED: S1, S2) | proposed |
| n64 | object | object_label::bob | label-preserved |
| n65 | constraint | color_label::blue | label-preserved |
| n66 | constraint | trait_label::kind (PROPOSED: S1) | proposed |
| n67 | speech_act | ask, property_question | covered |
| n68 | constraint | subject | covered |
| n69 | constraint | property_question | covered |
| n70 | claim | has_attribute, trait_label::kind (PROPOSED: S1, S2) | proposed |
| n71 | object | object_label::bob | label-preserved |
| n72 | constraint | trait_label::kind (PROPOSED: S1) | proposed |

## Why the translation failed

- n29, n31, n45, n47, n48, n50, n55, n58 ("young"): search "young" → constraint_17_plus, constraint_budget_limited, unit_sentence; widen found no symbol or value group for general age or youth traits. Proposed S1 (trait_label) and S2 (refine lexical_label).
- n32, n34, n48, n49, n55, n57, n59, n60, n63, n66, n70, n72 ("kind"): search "kind" → enables, comfortable, important, tone_polite, well_wishes; widen found no symbol or value group for kind / disposition traits. Proposed S1 (trait_label) and S2 (refine lexical_label).
- n38, n41, n42, n43, n52, n53 ("furry"): search "furry" → dog, yarn, cat_limited_time_offers; widen found no symbol or value group for physical texture / coat traits. Proposed S1 (trait_label) and S2 (refine lexical_label).

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: every segment t1:s1–t1:s23 is represented.
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "Bob" → object_label::bob, "green" → color_label::green; t1:s3 "Bob" → object_label::bob, "white" → color_label::white; t1:s4 "Dave" → object_label::dave, "blue" → color_label::blue; t1:s6 "Dave" → object_label::dave, "green" → color_label::green; t1:s7 "Dave" → object_label::dave, "white" → color_label::white; t1:s8 "Fiona" → object_label::fiona; t1:s9 "Fiona" → object_label::fiona, "green" → color_label::green; t1:s10 "Fiona" → object_label::fiona, "white" → color_label::white; t1:s11 "Fiona" → object_label::fiona; t1:s12 "Gary" → object_label::gary; t1:s13 "Gary" → object_label::gary, "white" → color_label::white; t1:s14 "white" → color_label::white; t1:s15 "green" → color_label::green; t1:s17 "blue" → color_label::blue; t1:s18 "blue" → color_label::blue; t1:s19 "white" → color_label::white; t1:s20 "blue" → color_label::blue; t1:s21 "Bob" → object_label::bob, "blue" → color_label::blue; t1:s23 "Bob" → object_label::bob
- Missing constructs: S1 lexical-group trait_label; S2 refine lexical_label to accept ATOM[trait_label]
- Unresolved ambiguities: none
- Check: `rag check` verified against current glossary and proposed additions
