Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=color_label::white) -> lexical_label_white : TERM
    TERM lexical_label(value=color_label::blue) -> lexical_label_blue : TERM
    TERM subject(kind="Anne", qualifier="nice") -> subject_anne_nice : TERM
    TERM negation(target=subject_anne_nice) -> negation_anne_nice : TERM
    CLAIM statement(fact=negation_anne_nice) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_anne_not_nice : CLAIM
    TERM subject(kind="Anne", qualifier=shape_round) -> subject_anne_round : TERM
    CLAIM statement(fact=subject_anne_round) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_anne_round : CLAIM
    TERM subject(kind="Anne", qualifier=lexical_label_white) -> subject_anne_white : TERM
    TERM negation(target=subject_anne_white) -> negation_anne_white : TERM
    CLAIM statement(fact=negation_anne_white) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_anne_not_white : CLAIM
    TERM subject(kind="Anne", qualifier="young") -> subject_anne_young : TERM
    CLAIM statement(fact=subject_anne_young) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_anne_young : CLAIM
    TERM subject(kind="Erin", qualifier=shape_round) -> subject_erin_round : TERM
    CLAIM statement(fact=subject_erin_round) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_erin_round : CLAIM
    TERM subject(kind="Fiona", qualifier=lexical_label_blue) -> subject_fiona_blue : TERM
    CLAIM statement(fact=subject_fiona_blue) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_fiona_blue : CLAIM
    TERM subject(kind="Gary", qualifier="young") -> subject_gary_young : TERM
    CLAIM statement(fact=subject_gary_young) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_gary_young : CLAIM
    TERM subject(kind="person", qualifier="nice") -> subject_nice_person : TERM
    TERM subject(kind="person", qualifier="quiet") -> subject_quiet_person : TERM
    TERM negation(target=subject_quiet_person) -> negation_quiet_person : TERM
    TERM conditional(condition=subject_nice_person, consequence=negation_quiet_person) -> conditional_nice_not_quiet : TERM
    CLAIM statement(fact=conditional_nice_not_quiet) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_nice_not_quiet : CLAIM
    TERM subject(kind="person", qualifier=shape_round) -> subject_round_person : TERM
    TERM conditional(condition=subject_round_person, consequence=subject_quiet_person) -> conditional_round_quiet : TERM
    CLAIM statement(fact=conditional_round_quiet) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_round_quiet : CLAIM
    TERM conditional(condition=subject_anne_nice, consequence=subject_anne_white) -> conditional_anne_nice_white : TERM
    CLAIM statement(fact=conditional_anne_nice_white) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_anne_nice_white : CLAIM
    TERM subject(kind="person", qualifier=lexical_label_blue) -> subject_blue_person : TERM
    TERM conditional(condition=subject_quiet_person, consequence=subject_blue_person) -> conditional_quiet_blue : TERM
    CLAIM statement(fact=conditional_quiet_blue) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_quiet_blue : CLAIM
    TERM subject(kind="Fiona", qualifier=lexical_label_white) -> subject_fiona_white : TERM
    TERM conditional(condition=subject_fiona_white, consequence=subject_fiona_blue) -> conditional_fiona_white_blue : TERM
    CLAIM statement(fact=conditional_fiona_white_blue) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_fiona_white_blue : CLAIM
    TERM subject(kind="person", qualifier="rough") -> subject_rough_person : TERM
    TERM subject(kind="person", qualifier="young") -> subject_young_person : TERM
    TERM conditional(condition=subject_rough_person, consequence=subject_young_person) -> conditional_rough_young : TERM
    CLAIM statement(fact=conditional_rough_young) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_rough_young : CLAIM
    TERM negation(target=subject_blue_person) -> negation_blue_person : TERM
    TERM conjunction(items=[subject_nice_person, negation_blue_person]) -> conjunction_nice_not_blue : TERM
    TERM negation(target=subject_rough_person) -> negation_rough_person : TERM
    TERM conditional(condition=conjunction_nice_not_blue, consequence=negation_rough_person) -> conditional_nice_not_blue_not_rough : TERM
    CLAIM statement(fact=conditional_nice_not_blue_not_rough) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_nice_not_blue_not_rough : CLAIM
    TERM conditional(condition=subject_blue_person, consequence=subject_rough_person) -> conditional_blue_rough : TERM
    CLAIM statement(fact=conditional_blue_rough) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_blue_rough : CLAIM
    TERM subject(kind="Erin", qualifier="young") -> subject_erin_young : TERM
    TERM subject(kind="Erin", qualifier=lexical_label_white) -> subject_erin_white : TERM
    TERM conditional(condition=subject_erin_young, consequence=subject_erin_white) -> conditional_erin_young_white : TERM
    CLAIM statement(fact=conditional_erin_young_white) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_erin_young_white : CLAIM
    TERM subject(kind="Erin", qualifier="rough") -> subject_erin_rough : TERM
    TERM negation(target=subject_erin_rough) -> negation_erin_rough : TERM
    UTTER ask(target=negation_erin_rough)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | conditional, statement, subject | covered |
| n2 | object | subject | covered |
| n3 | claim | statement, subject | covered |
| n4 | negation | negation, statement, subject | covered |
| n5 | claim | shape_round, statement, subject | covered |
| n6 | claim | color_label::white, lexical_label, statement, subject | label-preserved |
| n7 | negation | color_label::white, lexical_label, negation, statement, subject | covered |
| n8 | constraint | color_label::white, lexical_label | label-preserved |
| n9 | claim | statement, subject | covered |
| n10 | object | subject | covered |
| n11 | claim | shape_round, statement, subject | covered |
| n12 | object | subject | covered |
| n13 | claim | color_label::blue, lexical_label, statement, subject | label-preserved |
| n14 | constraint | color_label::blue, lexical_label | label-preserved |
| n15 | object | subject | covered |
| n16 | claim | statement, subject | covered |
| n17 | reasoning | conditional, negation, statement, subject | covered |
| n18 | negation | negation | covered |
| n19 | reasoning | conditional, shape_round, statement, subject | covered |
| n20 | reasoning | color_label::white, conditional, lexical_label, statement, subject | label-preserved |
| n21 | constraint | color_label::white, lexical_label | label-preserved |
| n22 | reasoning | color_label::blue, conditional, lexical_label, statement, subject | label-preserved |
| n23 | constraint | color_label::blue, lexical_label | label-preserved |
| n24 | reasoning | color_label::blue, color_label::white, conditional, lexical_label, statement, subject | label-preserved |
| n25 | constraint | color_label::white, lexical_label | label-preserved |
| n26 | constraint | color_label::blue, lexical_label | label-preserved |
| n27 | reasoning | conditional, statement, subject | covered |
| n28 | reasoning | color_label::blue, conditional, conjunction, lexical_label, negation, statement, subject | label-preserved |
| n29 | negation | color_label::blue, lexical_label, negation | covered |
| n30 | negation | negation | covered |
| n31 | constraint | color_label::blue, lexical_label | label-preserved |
| n32 | reasoning | color_label::blue, conditional, lexical_label, statement, subject | label-preserved |
| n33 | constraint | color_label::blue, lexical_label | label-preserved |
| n34 | reasoning | color_label::white, conditional, lexical_label, statement, subject | label-preserved |
| n35 | constraint | color_label::white, lexical_label | label-preserved |
| n36 | speech_act | ask, negation, subject | covered |
| n37 | constraint | ask | covered |
| n38 | constraint | ask | covered |
| n39 | action | ask | covered |
| n40 | claim | subject | covered |
| n41 | negation | negation, subject | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s4 "white" → color_label::white; t1:s7 "blue" → color_label::blue; t1:s11 "white" → color_label::white; t1:s12 "blue" → color_label::blue; t1:s13 "white" → color_label::white, "blue" → color_label::blue; t1:s15 "blue" → color_label::blue; t1:s16 "blue" → color_label::blue; t1:s17 "white" → color_label::white
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
