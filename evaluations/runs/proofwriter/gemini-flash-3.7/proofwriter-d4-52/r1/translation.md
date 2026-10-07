Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=color_label::blue) -> lexical_label_blue : TERM
    TERM lexical_label(value=color_label::green) -> lexical_label_green : TERM
    TERM lexical_label(value=color_label::white) -> lexical_label_white : TERM
    TERM character(name="Anne") -> character_anne : TERM
    TERM character(name="Charlie") -> character_charlie : TERM
    TERM character(name="Fiona") -> character_fiona : TERM
    TERM character(name="Gary") -> character_gary : TERM
    TERM subject(kind="Anne", qualifier="kind") -> subject_anne_kind : TERM
    CLAIM has_attribute(attribute="kind", subject=character_anne) BY role_user STATUS asserted SOURCE "t1:s2" -> has_attribute_anne_kind : CLAIM
    TERM subject(kind="Anne", qualifier=shape_round) -> subject_anne_round : TERM
    CLAIM statement(fact=subject_anne_round) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_anne_round : CLAIM
    TERM subject(kind="Charlie", qualifier=lexical_label_blue) -> subject_charlie_blue : TERM
    CLAIM statement(fact=subject_charlie_blue) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_charlie_blue : CLAIM
    TERM subject(kind="Charlie", qualifier=state_cold) -> subject_charlie_cold : TERM
    CLAIM statement(fact=subject_charlie_cold) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_charlie_cold : CLAIM
    TERM character_trait(property="kind", value="kind") -> character_trait_kind : TERM
    TERM subject(kind="Charlie", qualifier="kind") -> subject_charlie_kind : TERM
    CLAIM has_attribute(attribute=character_trait_kind, subject=character_charlie) BY role_user STATUS asserted SOURCE "t1:s6" -> has_attribute_charlie_kind : CLAIM
    TERM subject(kind="Charlie", qualifier="smart") -> subject_charlie_smart : TERM
    TERM negation(target=subject_charlie_smart) -> negation_charlie_smart : TERM
    CLAIM statement(fact=negation_charlie_smart) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_charlie_not_smart : CLAIM
    TERM subject(kind="Fiona", qualifier="kind") -> subject_fiona_kind : TERM
    TERM negation(target=subject_fiona_kind) -> negation_fiona_kind : TERM
    CLAIM has_attribute(attribute=negation_fiona_kind, subject=character_fiona) BY role_user STATUS asserted SOURCE "t1:s8" -> has_attribute_fiona_not_kind : CLAIM
    TERM subject(kind="Fiona", qualifier="smart") -> subject_fiona_smart : TERM
    CLAIM statement(fact=subject_fiona_smart) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_fiona_smart : CLAIM
    TERM subject(kind="Gary", qualifier=state_cold) -> subject_gary_cold : TERM
    CLAIM statement(fact=subject_gary_cold) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_gary_cold : CLAIM
    TERM subject(kind="Gary", qualifier=lexical_label_green) -> subject_gary_green : TERM
    CLAIM statement(fact=subject_gary_green) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_gary_green : CLAIM
    TERM subject(kind="Gary", qualifier=shape_round) -> subject_gary_round : TERM
    CLAIM statement(fact=subject_gary_round) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_gary_round : CLAIM
    TERM subject(kind="Gary", qualifier=lexical_label_white) -> subject_gary_white : TERM
    CLAIM statement(fact=subject_gary_white) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_gary_white : CLAIM
    TERM subject(kind="Fiona", qualifier=lexical_label_blue) -> subject_fiona_blue : TERM
    TERM subject(kind="Fiona", qualifier=lexical_label_green) -> subject_fiona_green : TERM
    TERM conditional(condition=subject_fiona_blue, consequence=subject_fiona_green) -> conditional_fiona_blue_green : TERM
    CLAIM statement(fact=conditional_fiona_blue_green) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_fiona_blue_green : CLAIM
    TERM subject(kind="Fiona", qualifier=state_cold) -> subject_fiona_cold : TERM
    TERM conditional(condition=subject_fiona_smart, consequence=subject_fiona_cold) -> conditional_fiona_smart_cold : TERM
    CLAIM statement(fact=conditional_fiona_smart_cold) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_fiona_smart_cold : CLAIM
    TERM subject(kind="things", qualifier=lexical_label_white) -> subject_white_things : TERM
    TERM subject(kind="things", qualifier=shape_round) -> subject_round_things : TERM
    TERM conditional(condition=subject_white_things, consequence=subject_round_things) -> conditional_white_round : TERM
    CLAIM statement(fact=conditional_white_round) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_white_round : CLAIM
    TERM subject(kind="things", qualifier=lexical_label_green) -> subject_green_things : TERM
    TERM conjunction(items=[subject_green_things, subject_white_things]) -> conjunction_green_white_things : TERM
    TERM conditional(condition=conjunction_green_white_things, consequence=subject_round_things) -> conditional_green_white_round : TERM
    CLAIM statement(fact=conditional_green_white_round) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_green_white_round : CLAIM
    TERM conditional(condition=subject_green_things, consequence=subject_round_things) -> conditional_green_round : TERM
    CLAIM statement(fact=conditional_green_round) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_green_round : CLAIM
    TERM subject(kind="things", qualifier="smart") -> subject_smart_things : TERM
    TERM conjunction(items=[subject_round_things, subject_smart_things]) -> conjunction_round_smart_things : TERM
    TERM conditional(condition=conjunction_round_smart_things, consequence=subject_white_things) -> conditional_round_smart_white : TERM
    CLAIM statement(fact=conditional_round_smart_white) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_round_smart_white : CLAIM
    TERM subject(kind="things", qualifier=state_cold) -> subject_cold_things : TERM
    TERM subject(kind="things", qualifier=lexical_label_blue) -> subject_blue_things : TERM
    TERM conditional(condition=subject_cold_things, consequence=subject_blue_things) -> conditional_cold_blue : TERM
    CLAIM statement(fact=conditional_cold_blue) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_cold_blue : CLAIM
    TERM subject(kind="Charlie", qualifier=lexical_label_green) -> subject_charlie_green : TERM
    TERM conjunction(items=[subject_charlie_cold, subject_charlie_green]) -> conjunction_charlie_cold_green : TERM
    TERM conditional(condition=conjunction_charlie_cold_green, consequence=subject_charlie_kind) -> conditional_charlie_cold_green_kind : TERM
    CLAIM statement(fact=conditional_charlie_cold_green_kind) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_charlie_cold_green_kind : CLAIM
    TERM subject(kind="Fiona", qualifier=shape_round) -> subject_fiona_round : TERM
    TERM negation(target=subject_fiona_round) -> negation_fiona_round : TERM
    UTTER ask(target=negation_fiona_round)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | subject, conjunction | covered |
| n2 | claim | has_attribute | covered |
| n3 | object | character | covered |
| n4 | claim | shape_round | covered |
| n5 | claim | color_label | label-preserved |
| n6 | object | character | covered |
| n7 | constraint | color_label::blue | label-preserved |
| n8 | claim | state_cold | covered |
| n9 | claim | character_trait | covered |
| n10 | claim | subject, ask | covered |
| n11 | negation | negation | covered |
| n12 | claim | has_attribute | covered |
| n13 | negation | negation | covered |
| n14 | object | character | covered |
| n15 | claim | subject | covered |
| n16 | claim | state_cold | covered |
| n17 | object | subject | covered |
| n18 | claim | color_label | label-preserved |
| n19 | constraint | color_label::green | label-preserved |
| n20 | claim | shape_round | covered |
| n21 | claim | color_label, statement | covered |
| n22 | constraint | color_label::white | label-preserved |
| n23 | reasoning | color_label | label-preserved |
| n24 | constraint | color_label::blue | label-preserved |
| n25 | constraint | color_label::green | label-preserved |
| n26 | reasoning | state_cold | covered |
| n27 | reasoning | shape_round | covered |
| n28 | constraint | color_label::white | label-preserved |
| n29 | reasoning | shape_round | covered |
| n30 | constraint | color_label::green | label-preserved |
| n31 | constraint | color_label::white | label-preserved |
| n32 | reasoning | shape_round | covered |
| n33 | constraint | color_label::green | label-preserved |
| n34 | reasoning | shape_round | covered |
| n35 | constraint | color_label::white | label-preserved |
| n36 | reasoning | state_cold, color_label | covered |
| n37 | constraint | color_label::blue | label-preserved |
| n38 | reasoning | state_cold | covered |
| n39 | constraint | color_label::green | label-preserved |
| n40 | speech_act | ask, statement, conditional, negation | covered |
| n41 | constraint | subject, conjunction | covered |
| n42 | constraint | ask | covered |
| n43 | claim | shape_round | covered |
| n44 | negation | shape_round, negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s23 is represented.
- Opaque-text spans: none
- Label-preserved spans: t1:s4, t1:s11, t1:s13, t1:s14, t1:s16, t1:s17, t1:s18, t1:s19, t1:s20, t1:s21 color_label::blue, color_label::green, color_label::white
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
