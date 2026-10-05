Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object=object_label::lawn, verb="mow") -> activity_2 : TERM
    TERM property_question(property="instructions", subject=activity_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(instrument=object_label::mower, object=object_label::lawn, verb="mow") -> activity_3 : TERM
    TERM activity(instrument=object_label::gloves, object=object_label::lawn, verb="mow") -> activity_4 : TERM
    TERM activity(instrument=object_label::eyewear, object=object_label::lawn, verb="mow") -> activity_5 : TERM
    TERM activity(object=object_label::debris, verb="remove") -> activity_6 : TERM
    TERM activity(object=object_label::obstacle, verb="remove") -> activity_7 : TERM
    TERM conjunction(items=[activity_6, activity_7]) -> conjunction_2 : TERM
    TERM activity(object=object_label::lawn, purpose=conjunction_2, verb="prepare") -> activity_8 : TERM
    TERM activity(instrument=object_label::mower, object=object_label::blade, verb="adjust") -> activity_9 : TERM
    TERM measure(amount=33.3333333333, unit=unit_percent) -> measure_2 : TERM
    TERM at_most(measure=measure_2) -> at_most_2 : TERM
    TERM requirement(property="grass_cut_height", value=at_most_2) -> requirement_2 : TERM
    TERM requirement(property="pace", value="even") -> requirement_3 : TERM
    TERM requirement(property="pattern", value="straight_lines_back_and_forth") -> requirement_4 : TERM
    TERM activity(object=object_label::lawn, verb="mow_same_direction") -> activity_10 : TERM
    TERM negation(target=activity_10) -> negation_2 : TERM
    TERM exclude(item="same_direction") -> exclude_2 : TERM
    TERM activity(instrument=object_label::trimmer, object=object_label::edge, verb="trim") -> activity_11 : TERM
    TERM sequence(items=[activity_8, activity_9, activity_3, activity_11]) -> sequence_2 : TERM
    TERM requirement(property="follow_safety_instructions", value=TRUE) -> requirement_5 : TERM
    TERM requirement(property="wear_protective_gear", value=TRUE) -> requirement_6 : TERM
    UTTER respond(target=sequence_2)
    TERM property_question(property="safety_and_process", subject=t1.activity_2) -> property_question_3 : TERM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER {
    TERM activity(instrument=object_label::scissors, object=object_label::grass, verb="cut") -> activity_12 : TERM
    TERM property_question(property="feasibility", subject=activity_12) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
  }
  TURN t4 SPEAKER=AGENT {
    TERM subject(kind="lawn", qualifier=size_large) -> subject_2 : TERM
    TERM activity(instrument=object_label::scissors, location="lawn", object=object_label::grass, verb="cut") -> activity_13 : TERM
    CLAIM enables(condition=activity_13, outcome=subject_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> enables_2 : CLAIM
    CLAIM attribute_claim(property="efficient", subject=activity_13, value=FALSE) BY role_agent STATUS asserted SOURCE "t4:s1" -> attribute_claim_2 : CLAIM
    TERM subject(kind="lawn_patch", qualifier=size_small) -> subject_3 : TERM
    CLAIM important(target=activity_13) BY role_agent STATUS asserted SOURCE "t4:s2" -> important_2 : CLAIM
    CLAIM attribute_claim(property="useful_for", subject=object_label::scissors, value=subject_3) BY role_agent STATUS asserted SOURCE "t4:s2" -> attribute_claim_3 : CLAIM
    TERM activity(instrument=object_label::mower, location="lawn", object=object_label::grass, verb="cut") -> activity_14 : TERM
    CLAIM recommended(target=activity_14) BY role_agent STATUS asserted SOURCE "t4:s4" -> recommended_2 : CLAIM
    CLAIM designed_to_be(quality="efficient_large_area_cutting", subject=object_label::mower) BY role_agent STATUS asserted SOURCE "t4:s5" -> designed_to_be_2 : CLAIM
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
| n2 | action | activity | covered |
| n3 | object | object_label::mower | label-preserved |
| n4 | object | object_label::gloves | label-preserved |
| n5 | object | object_label::eyewear | label-preserved |
| n6 | temporal | sequence | covered |
| n7 | action | activity, conjunction | covered |
| n8 | action | activity | covered |
| n9 | constraint | at_most, measure, requirement, unit_percent | covered |
| n10 | action | activity, requirement | covered |
| n11 | negation | exclude, negation | covered |
| n12 | temporal | sequence | covered |
| n13 | action | activity | covered |
| n14 | object | object_label::trimmer | label-preserved |
| n15 | constraint | requirement | covered |
| n16 | speech_act | offer, offer_help, property_question, respond | covered |
| n17 | speech_act | ask, property_question | covered |
| n18 | object | object_label::scissors | label-preserved |
| n19 | claim | attribute_claim, enables, size_large | covered |
| n20 | claim | attribute_claim, important, size_small | covered |
| n21 | claim | recommended | covered |
| n22 | reasoning | designed_to_be, supports | covered |
| n23 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s7 is represented
- Opaque-text spans: none
- Label-preserved spans:
  - t2:s1 "lawn mower" -> object_label::mower (open label)
  - t2:s1 "gardening gloves" -> object_label::gloves (open label)
  - t2:s1 "protective eyewear" -> object_label::eyewear (open label)
  - t2:s9 "string trimmer" -> object_label::trimmer (open label)
  - t3:s1 "scissors" -> object_label::scissors (open label)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
