Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM property_question(property="how_to_mow", subject=object_label::lawn) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM requirement(property="required_tools", value=object_label::mower) -> requirement_2 : TERM
    TERM requirement(property="protective_gear", value=object_label::gloves) -> requirement_3 : TERM
    TERM requirement(property="protective_gear", value=object_label::eyewear) -> requirement_4 : TERM
    TERM activity(object=object_label::debris, verb="remove") -> activity_2 : TERM
    TERM activity(object=object_label::lawn, purpose=activity_2, verb="prepare") -> activity_3 : TERM
    TERM measure(amount=33.33, unit=unit_percent) -> measure_2 : TERM
    TERM at_most(measure=measure_2) -> at_most_2 : TERM
    TERM requirement(property="grass_height_cut_fraction", value=at_most_2) -> requirement_5 : TERM
    TERM activity(instrument=object_label::mower, purpose=requirement_5, verb="adjust_blade_height") -> activity_4 : TERM
    TERM activity(instrument=object_label::mower, object=object_label::lawn, verb="mow_straight_lines") -> activity_5 : TERM
    TERM activity(object=object_label::lawn, verb="mow_same_direction") -> activity_6 : TERM
    TERM exclude(item=activity_6) -> exclude_2 : TERM
    TERM conjunction(items=[activity_5, exclude_2]) -> conjunction_2 : TERM
    TERM activity(instrument=object_label::trimmer, object=object_label::lawn, verb="trim_edges") -> activity_7 : TERM
    TERM sequence(items=[activity_3, activity_4, conjunction_2, activity_7]) -> sequence_2 : TERM
    TERM requirement(property="follow_safety_instructions_and_gear", value=TRUE) -> requirement_6 : TERM
    TERM conjunction(items=[sequence_2, requirement_6]) -> conjunction_3 : TERM
    TERM obligation(activity=conjunction_3, actor=role_user) -> obligation_2 : TERM
    UTTER propose(target=obligation_2)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER {
    TERM activity(instrument=object_label::scissors, object=object_label::grass, verb="cut") -> activity_8 : TERM
    TERM property_question(property="feasibility", subject=activity_8) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM attribute_claim(property="efficient_for_large_lawns", subject=t3.activity_8, value=FALSE) BY role_agent STATUS asserted SOURCE "t4:s1" -> attribute_claim_2 : CLAIM
    TERM activity(object=object_label::garden, verb="precision_grooming") -> activity_9 : TERM
    CLAIM enables(condition=t3.activity_8, outcome=activity_9) BY role_agent STATUS asserted SOURCE "t4:s2" -> enables_2 : CLAIM
    TERM activity(instrument=object_label::mower, object=object_label::lawn, verb="mow") -> activity_10 : TERM
    CLAIM recommended(target=activity_10) BY role_agent STATUS asserted SOURCE "t4:s4" -> recommended_2 : CLAIM
    CLAIM designed_to_be(quality="efficient_cutting_large_areas", subject=object_label::mower) BY role_agent STATUS asserted SOURCE "t4:s5" -> designed_to_be_2 : CLAIM
    LINK supports(conclusion=recommended_2, premise=designed_to_be_2) SOURCE "t4:s5"
    TERM offer_help() -> offer_help_3 : TERM
    UTTER offer(target=offer_help_3)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question | covered |
| n2 | action | obligation, propose, property_question | covered |
| n3 | object | object_label::mower | label-preserved |
| n4 | object | object_label::gloves | label-preserved |
| n5 | object | object_label::eyewear | label-preserved |
| n6 | temporal | sequence | covered |
| n7 | action | activity, exclude, obligation, propose | covered |
| n8 | action | activity, obligation | covered |
| n9 | constraint | at_most, measure, requirement | covered |
| n10 | action | activity | covered |
| n11 | negation | exclude | covered |
| n12 | temporal | sequence | covered |
| n13 | action | activity, obligation, propose | covered |
| n14 | object | object_label::trimmer | label-preserved |
| n15 | constraint | requirement | covered |
| n16 | speech_act | offer, offer_help | covered |
| n17 | speech_act | ask, property_question | covered |
| n18 | object | object_label::scissors | label-preserved |
| n19 | claim | attribute_claim | covered |
| n20 | claim | enables | covered |
| n21 | claim | recommended | covered |
| n22 | reasoning | designed_to_be, supports | covered |
| n23 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s7 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s1 "lawn mower" -> object_label::mower, t2:s1 "gardening gloves" -> object_label::gloves, t2:s1 "protective eyewear" -> object_label::eyewear, t2:s9 "string trimmer" -> object_label::trimmer, t3:s1 "scissors" -> object_label::scissors
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
