Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object=object_label::lawn, verb="mow") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM lexical_label(value=object_label::mower) -> lexical_label_2 : TERM
    TERM lexical_label(value=object_label::gloves) -> lexical_label_3 : TERM
    TERM lexical_label(value=object_label::eyewear) -> lexical_label_4 : TERM
    TERM conjunction(items=[lexical_label_2, lexical_label_3, lexical_label_4]) -> conjunction_2 : TERM
    TERM requirement(property="equipment", value=conjunction_2) -> requirement_2 : TERM
    CLAIM statement(fact=requirement_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> statement_2 : CLAIM
    TERM activity(object=object_label::lawn, verb="prepare") -> activity_3 : TERM
    TERM activity(object=object_label::debris, verb="remove") -> activity_4 : TERM
    TERM sequence(items=[activity_3, activity_4]) -> sequence_2 : TERM
    CLAIM recommended(target=sequence_2) BY role_agent STATUS asserted SOURCE "t2:s3" -> recommended_2 : CLAIM
    TERM activity(instrument=object_label::mower, object="blade_height", verb="adjust") -> activity_5 : TERM
    TERM measure(amount=33.3, unit=unit_percent) -> measure_2 : TERM
    TERM at_most(measure=measure_2) -> at_most_2 : TERM
    TERM requirement(property="grass_height_cut", value=at_most_2) -> requirement_3 : TERM
    CLAIM constrained_by(activity=activity_5, constraint=requirement_3) BY role_agent STATUS asserted SOURCE "t2:s5" -> constrained_by_2 : CLAIM
    TERM activity(object=object_label::lawn, verb="mow_straight_lines") -> activity_6 : TERM
    TERM activity(object="same_direction", verb="mow") -> activity_7 : TERM
    TERM exclude(item=activity_7) -> exclude_2 : TERM
    CLAIM recommended(target=activity_6) BY role_agent STATUS asserted SOURCE "t2:s7" -> recommended_3 : CLAIM
    CLAIM statement(fact=exclude_2) BY role_agent STATUS asserted SOURCE "t2:s7" -> statement_3 : CLAIM
    TERM activity(object=object_label::lawn, verb="mow") -> activity_8 : TERM
    TERM activity(instrument=object_label::trimmer, object="edges", verb="trim") -> activity_9 : TERM
    TERM sequence(items=[activity_8, activity_9]) -> sequence_3 : TERM
    CLAIM recommended(target=sequence_3) BY role_agent STATUS asserted SOURCE "t2:s9" -> recommended_4 : CLAIM
    TERM activity(object="safety_instructions", verb="follow") -> activity_10 : TERM
    TERM activity(object="safety_gear", verb="wear") -> activity_11 : TERM
    TERM conjunction(items=[activity_10, activity_11]) -> conjunction_3 : TERM
    TERM obligation(activity=conjunction_3, actor="user") -> obligation_2 : TERM
    CLAIM statement(fact=obligation_2) BY role_agent STATUS asserted SOURCE "t2:s10" -> statement_4 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER {
    TERM activity(instrument=object_label::scissors, object=object_label::grass, verb="cut") -> activity_12 : TERM
    UTTER ask(target=activity_12)
  }
  TURN t4 SPEAKER=AGENT {
    TERM subject(kind="lawn", qualifier=size_large) -> subject_2 : TERM
    TERM activity(instrument=object_label::scissors, object=subject_2, verb="cut") -> activity_13 : TERM
    CLAIM statement(fact=activity_13) BY role_agent STATUS asserted SOURCE "t4:s1" -> statement_5 : CLAIM
    TERM requirement(property="efficiency", value="inefficient") -> requirement_4 : TERM
    CLAIM constrained_by(activity=activity_13, constraint=requirement_4) BY role_agent STATUS asserted SOURCE "t4:s1" -> constrained_by_3 : CLAIM
    LINK contrast(first=statement_5, second=constrained_by_3) SOURCE "t4:s1"
    TERM subject(kind="patch", qualifier=size_small) -> subject_3 : TERM
    TERM activity(instrument=object_label::scissors, object=subject_3, verb="cut") -> activity_14 : TERM
    TERM requirement(property="suitability", value="useful") -> requirement_5 : TERM
    CLAIM enables(condition=activity_14, outcome=requirement_5) BY role_agent STATUS asserted SOURCE "t4:s2" -> enables_2 : CLAIM
    TERM activity(instrument=object_label::mower, object=subject_2, verb="mow") -> activity_15 : TERM
    CLAIM recommended(target=activity_15) BY role_agent STATUS asserted SOURCE "t4:s4" -> recommended_5 : CLAIM
    TERM lexical_label(value=object_label::mower) -> lexical_label_5 : TERM
    CLAIM designed_to_be(quality="efficient_cutting", subject=lexical_label_5) BY role_agent STATUS asserted SOURCE "t4:s5" -> designed_to_be_2 : CLAIM
    LINK supports(conclusion=recommended_5, premise=designed_to_be_2) SOURCE "t4:s5"
    TERM offer_help() -> offer_help_3 : TERM
    UTTER offer(target=offer_help_3)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, activity | covered |
| n2 | action | activity | covered |
| n3 | object | object_label::mower | label-preserved |
| n4 | object | object_label::gloves | label-preserved |
| n5 | object | object_label::eyewear | label-preserved |
| n6 | temporal | sequence, activity | covered |
| n7 | action | activity | covered |
| n8 | action | activity | covered |
| n9 | constraint | at_most, measure, requirement, constrained_by | covered |
| n10 | action | activity, recommended | covered |
| n11 | negation | exclude, statement | covered |
| n12 | temporal | sequence, activity | covered |
| n13 | action | activity | covered |
| n14 | object | object_label::trimmer | label-preserved |
| n15 | constraint | obligation, conjunction, activity, statement | covered |
| n16 | speech_act | offer, offer_help | covered |
| n17 | speech_act | ask, activity | covered |
| n18 | object | object_label::scissors | label-preserved |
| n19 | claim | statement, constrained_by, contrast, size_large | covered |
| n20 | claim | enables, size_small, activity | covered |
| n21 | claim | recommended, size_large | covered |
| n22 | reasoning | designed_to_be, supports | covered |
| n23 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s7 is represented.
- Opaque-text spans: none
- Label-preserved spans: t2:s1 "lawn mower" → object_label::mower; t2:s1 "gardening gloves" → object_label::gloves; t2:s1 "protective eyewear" → object_label::eyewear; t2:s9 "string trimmer" → object_label::trimmer; t3:s1 "scissors" → object_label::scissors
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
