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
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM activity(instrument=object_label::mower, object=object_label::lawn, verb="mow") -> activity_3 : TERM
    TERM activity(object=object_label::gloves, verb="wear") -> activity_4 : TERM
    TERM activity(object=object_label::eyewear, verb="wear") -> activity_5 : TERM
    TERM activity(object=object_label::debris, verb="remove") -> activity_6 : TERM
    TERM activity(object=object_label::lawn, purpose=activity_6, verb="prepare") -> activity_7 : TERM
    TERM sequence(items=[activity_7, activity_3]) -> sequence_2 : TERM
    TERM activity(instrument=object_label::mower, object=object_label::blades, verb="adjust") -> activity_8 : TERM
    TERM measure(amount=33.33, unit=unit_percent) -> measure_2 : TERM
    TERM at_most(measure=measure_2) -> at_most_2 : TERM
    TERM requirement(property="max_cut_fraction", value=at_most_2) -> requirement_2 : TERM
    TERM activity(object=object_label::lawn, verb="mow_straight_lines") -> activity_9 : TERM
    TERM activity(object=object_label::lawn, verb="mow_same_direction") -> activity_10 : TERM
    TERM negation(target=activity_10) -> negation_2 : TERM
    TERM activity(instrument=object_label::trimmer, object=object_label::edges, verb="trim") -> activity_11 : TERM
    TERM activity(instrument=object_label::edger, object=object_label::edges, verb="trim") -> activity_12 : TERM
    TERM sequence(items=[activity_3, activity_11]) -> sequence_3 : TERM
    TERM activity(object=object_label::instructions, verb="follow") -> activity_13 : TERM
    TERM obligation(activity=activity_13, actor=role_user) -> obligation_2 : TERM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(instrument=object_label::scissors, object=object_label::grass, verb="cut") -> activity_14 : TERM
    UTTER ask(target=activity_14)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM activity(instrument=object_label::scissors, object=object_label::grass, verb="cut") -> activity_15 : TERM
    TERM subject(kind="lawn", qualifier=size_large) -> subject_2 : TERM
    CLAIM has_attribute(attribute="inefficient", subject=activity_15) BY role_agent STATUS asserted SOURCE "t4:s1" -> has_attribute_2 : CLAIM
    TERM subject(kind="patch", qualifier=size_small) -> subject_3 : TERM
    CLAIM enables(condition=activity_15, outcome=subject_3) BY role_agent STATUS asserted SOURCE "t4:s2" -> enables_2 : CLAIM
    TERM activity(instrument=object_label::mower, object=subject_2, verb="mow") -> activity_16 : TERM
    CLAIM recommended(target=activity_16) BY role_agent STATUS asserted SOURCE "t4:s4" -> recommended_2 : CLAIM
    TERM subject(kind="mower") -> subject_4 : TERM
    CLAIM designed_to_be(quality="efficient_cutting", subject=subject_4) BY role_agent STATUS asserted SOURCE "t4:s5" -> designed_to_be_2 : CLAIM
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
| n10 | action | activity | covered |
| n11 | negation | negation | covered |
| n12 | temporal | sequence | covered |
| n13 | action | activity | covered |
| n14 | object | object_label::trimmer, object_label::edger | label-preserved |
| n15 | constraint | obligation, role_user | covered |
| n16 | speech_act | offer, offer_help | covered |
| n17 | speech_act | ask | covered |
| n18 | object | object_label::scissors | label-preserved |
| n19 | claim | has_attribute, size_large | covered |
| n20 | claim | enables, size_small | covered |
| n21 | claim | recommended | covered |
| n22 | reasoning | designed_to_be, supports | covered |
| n23 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s7 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s1 "lawn mower" -> object_label::mower; t2:s1 "gardening gloves" -> object_label::gloves; t2:s1 "protective eyewear" -> object_label::eyewear; t2:s9 "string trimmer" -> object_label::trimmer; t2:s9 "edger" -> object_label::edger; t3:s1 "scissors" -> object_label::scissors
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
