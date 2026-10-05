Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object="lawn", verb="mow") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(instrument=object_label::mower, object="lawn", verb="mow") -> activity_3 : TERM
    TERM activity(object=object_label::gloves, verb="wear") -> activity_4 : TERM
    TERM activity(object=object_label::eyewear, verb="wear") -> activity_5 : TERM
    TERM activity(object="lawn", verb="prepare") -> activity_6 : TERM
    TERM activity(location="lawn", object="debris", verb="remove") -> activity_7 : TERM
    TERM activity(location="lawn", object="obstacle", verb="remove") -> activity_8 : TERM
    TERM activity(instrument=object_label::mower, object="blade_height", verb="adjust") -> activity_9 : TERM
    TERM measure(amount=33.33, unit=unit_percent) -> measure_2 : TERM
    TERM at_most(measure=measure_2) -> at_most_2 : TERM
    TERM requirement(property="cut_height_fraction", value=at_most_2) -> requirement_2 : TERM
    TERM activity(object="lawn", verb="mow") -> activity_10 : TERM
    TERM requirement(property="pattern", value="straight_lines") -> requirement_3 : TERM
    TERM requirement(property="pace", value="even") -> requirement_4 : TERM
    TERM activity(location="same_direction", verb="mow") -> activity_11 : TERM
    TERM negation(target=activity_11) -> negation_2 : TERM
    TERM activity(instrument=object_label::trimmer, object="edges", verb="trim") -> activity_12 : TERM
    TERM activity(instrument=object_label::edger, object="edges", verb="trim") -> activity_13 : TERM
    TERM sequence(items=[activity_6, activity_9, activity_10, activity_12]) -> sequence_2 : TERM
    TERM activity(object="safety_instructions", verb="follow") -> activity_14 : TERM
    TERM obligation(activity=activity_14, actor=role_user) -> obligation_2 : TERM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER propose(target=sequence_2)
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER {
    TERM activity(instrument=scissors, object="grass", verb="cut") -> activity_15 : TERM
    UTTER ask(target=activity_15)
  }
  TURN t4 SPEAKER=AGENT {
    TERM activity(instrument=scissors, object="grass", verb="cut") -> activity_16 : TERM
    CLAIM enables(condition=scissors, outcome=activity_16) BY role_agent STATUS asserted SOURCE "t4:s1" -> enables_2 : CLAIM
    TERM subject(kind="lawn", qualifier=size_large) -> subject_2 : TERM
    TERM activity(instrument=scissors, object=subject_2, verb="mow") -> activity_17 : TERM
    CLAIM attribute_claim(property="efficient", subject=activity_17, value=FALSE) BY role_agent STATUS asserted SOURCE "t4:s1" -> attribute_claim_2 : CLAIM
    LINK contrast(first=enables_2, second=attribute_claim_2) SOURCE "t4:s1"
    TERM subject(kind="patch", qualifier=size_small) -> subject_3 : TERM
    TERM activity(instrument=scissors, object=subject_3, verb="cut") -> activity_18 : TERM
    CLAIM enables(condition=scissors, outcome=activity_18) BY role_agent STATUS asserted SOURCE "t4:s2" -> enables_3 : CLAIM
    CLAIM important(target=activity_18) BY role_agent STATUS asserted SOURCE "t4:s2" -> important_2 : CLAIM
    TERM activity(instrument=object_label::mower, object=subject_2, verb="mow") -> activity_19 : TERM
    CLAIM recommended(target=activity_19) BY role_agent STATUS asserted SOURCE "t4:s4" -> recommended_2 : CLAIM
    CLAIM designed_to_be(quality="efficient", subject=object_label::mower) BY role_agent STATUS asserted SOURCE "t4:s5" -> designed_to_be_2 : CLAIM
    LINK supports(conclusion=recommended_2, premise=designed_to_be_2) SOURCE "t4:s5"
    TERM offer_help() -> offer_help_3 : TERM
    UTTER offer(target=offer_help_3)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | action | activity | covered |
| n3 | object | object_label::mower | label-preserved |
| n4 | object | object_label::gloves | label-preserved |
| n5 | object | object_label::eyewear | label-preserved |
| n6 | temporal | sequence | covered |
| n7 | action | activity | covered |
| n8 | action | activity | covered |
| n9 | constraint | at_most, measure, requirement, unit_percent | covered |
| n10 | action | activity, requirement | covered |
| n11 | negation | negation | covered |
| n12 | temporal | sequence | covered |
| n13 | action | activity | covered |
| n14 | object | object_label::trimmer, object_label::edger | label-preserved |
| n15 | constraint | obligation, activity | covered |
| n16 | speech_act | offer, offer_help | covered |
| n17 | speech_act | ask | covered |
| n18 | object | scissors | covered |
| n19 | claim | enables, attribute_claim, contrast, size_large | covered |
| n20 | claim | enables, important, size_small | covered |
| n21 | claim | recommended | covered |
| n22 | reasoning | designed_to_be, supports | covered |
| n23 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s7 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s1 "lawn mower" -> object_label::mower, "gardening gloves" -> object_label::gloves, "protective eyewear" -> object_label::eyewear; t2:s9 "string trimmer" -> object_label::trimmer, "edger" -> object_label::edger
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
