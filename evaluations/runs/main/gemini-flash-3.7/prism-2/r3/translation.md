Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object=object_label::lawn, verb="mow") -> activity_2 : TERM
    TERM property_question(property="procedure", subject=activity_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(instrument=object_label::mower, verb="use") -> activity_mower : TERM
    TERM activity(instrument=object_label::gloves, verb="wear") -> activity_gloves : TERM
    TERM activity(instrument=object_label::eyewear, verb="wear") -> activity_eyewear : TERM
    TERM conjunction(items=[activity_mower, activity_gloves, activity_eyewear]) -> conjunction_gear : TERM
    TERM obligation(activity=conjunction_gear, actor="user") -> obligation_gear : TERM
    CLAIM recommended(target=obligation_gear) BY role_agent STATUS asserted SOURCE "t2:s1" -> recommended_gear : CLAIM
    TERM activity(object=object_label::debris, verb="remove") -> activity_debris : TERM
    TERM activity(object=object_label::obstacles, verb="remove") -> activity_obstacles : TERM
    TERM conjunction(items=[activity_debris, activity_obstacles]) -> conjunction_debris_obstacles : TERM
    TERM activity(object=object_label::lawn, purpose=conjunction_debris_obstacles, verb="prepare") -> activity_prepare : TERM
    TERM sequence(items=[activity_prepare, t1.activity_2]) -> sequence_prep_mow : TERM
    CLAIM recommended(target=sequence_prep_mow) BY role_agent STATUS asserted SOURCE "t2:s3" -> recommended_prep : CLAIM
    TERM activity(instrument=object_label::mower, object=object_label::blade, verb="adjust_height") -> activity_blade : TERM
    TERM measure(amount=33.33, unit=unit_percent) -> measure_third : TERM
    TERM at_most(measure=measure_third) -> at_most_third : TERM
    TERM requirement(property="grass_height_cut", value=at_most_third) -> requirement_cut : TERM
    CLAIM constrained_by(activity=activity_blade, constraint=requirement_cut) BY role_agent STATUS asserted SOURCE "t2:s5" -> constrained_by_cut : CLAIM
    TERM requirement(property="pattern", value="straight_lines_back_and_forth") -> requirement_lines : TERM
    TERM requirement(property="pace", value="even") -> requirement_pace : TERM
    TERM conjunction(items=[requirement_lines, requirement_pace]) -> conjunction_pattern : TERM
    TERM activity(object=object_label::lawn, purpose=conjunction_pattern, verb="mow") -> activity_mow_lines : TERM
    CLAIM recommended(target=activity_mow_lines) BY role_agent STATUS asserted SOURCE "t2:s7" -> recommended_lines : CLAIM
    TERM requirement(property="direction", value="same_each_time") -> requirement_same_dir : TERM
    TERM activity(object=object_label::lawn, purpose=requirement_same_dir, verb="mow") -> activity_same_dir : TERM
    TERM exclude(item=activity_same_dir) -> exclude_same_dir : TERM
    CLAIM recommended(target=exclude_same_dir) BY role_agent STATUS asserted SOURCE "t2:s7" -> recommended_avoid_dir : CLAIM
    TERM activity(instrument=object_label::trimmer, object=object_label::edges, verb="trim") -> activity_trimmer : TERM
    TERM activity(instrument=object_label::edger, object=object_label::edges, verb="trim") -> activity_edger : TERM
    TERM conjunction(items=[activity_trimmer, activity_edger]) -> conjunction_trim : TERM
    TERM sequence(items=[t1.activity_2, conjunction_trim]) -> sequence_mow_trim : TERM
    CLAIM recommended(target=sequence_mow_trim) BY role_agent STATUS asserted SOURCE "t2:s9" -> recommended_trim : CLAIM
    TERM activity(instrument=object_label::mower, object=object_label::instructions, verb="follow") -> activity_safety_instructions : TERM
    TERM conjunction(items=[activity_safety_instructions, activity_gloves, activity_eyewear]) -> conjunction_safety : TERM
    TERM obligation(activity=conjunction_safety, actor="user") -> obligation_safety : TERM
    CLAIM recommended(target=obligation_safety) BY role_agent STATUS asserted SOURCE "t2:s10" -> recommended_safety : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER {
    TERM activity(instrument=object_label::scissors, object=object_label::grass, verb="cut") -> activity_cut_scissors : TERM
    TERM property_question(property="possibility", subject=activity_cut_scissors) -> property_question_scissors : TERM
    UTTER ask(target=property_question_scissors)
  }
  TURN t4 SPEAKER=AGENT {
    TERM subject(kind="lawn", qualifier=size_large) -> subject_large_lawn : TERM
    TERM activity(object=subject_large_lawn, verb="mow") -> activity_mow_large_lawn : TERM
    TERM activity(object=object_label::grass, verb="cut") -> activity_cut_grass : TERM
    CLAIM enables(condition=t3.activity_cut_scissors, outcome=activity_cut_grass) BY role_agent STATUS asserted SOURCE "t4:s1" -> enables_scissors : CLAIM
    CLAIM attribute_claim(property="efficiency", subject=t3.activity_cut_scissors, value=FALSE) BY role_agent STATUS asserted SOURCE "t4:s1" -> attribute_claim_inefficient : CLAIM
    LINK contrast(first=enables_scissors, second=attribute_claim_inefficient) SOURCE "t4:s1"
    TERM subject(kind="lawn", qualifier=size_small) -> subject_small_lawn : TERM
    TERM activity(instrument=object_label::scissors, object=subject_small_lawn, verb="groom") -> activity_groom_small : TERM
    TERM activity(instrument=object_label::scissors, object=object_label::obstacles, verb="detail") -> activity_detail_obstacles : TERM
    TERM conjunction(items=[activity_groom_small, activity_detail_obstacles]) -> conjunction_scissors_detail : TERM
    CLAIM enables(condition=t3.activity_cut_scissors, outcome=conjunction_scissors_detail) BY role_agent STATUS asserted SOURCE "t4:s2" -> enables_small_detail : CLAIM
    CLAIM attribute_claim(property="precision", subject=t3.activity_cut_scissors, value=TRUE) BY role_agent STATUS asserted SOURCE "t4:s3" -> attribute_claim_precision : CLAIM
    TERM activity(instrument=object_label::mower, object=subject_large_lawn, verb="mow") -> activity_mower_large : TERM
    CLAIM recommended(target=activity_mower_large) BY role_agent STATUS asserted SOURCE "t4:s4" -> recommended_mower_large : CLAIM
    CLAIM designed_to_be(quality="efficient_cut_large_areas", subject=object_label::mower) BY role_agent STATUS asserted SOURCE "t4:s5" -> designed_to_be_mower : CLAIM
    LINK supports(conclusion=recommended_mower_large, premise=designed_to_be_mower) SOURCE "t4:s5"
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
| n9 | constraint | measure, unit_percent, at_most, requirement, constrained_by | covered |
| n10 | action | activity, requirement, conjunction | covered |
| n11 | negation | exclude, requirement, activity | covered |
| n12 | temporal | sequence | covered |
| n13 | action | activity | covered |
| n14 | object | object_label::trimmer, object_label::edger | label-preserved |
| n15 | constraint | obligation, requirement, conjunction, activity | covered |
| n16 | speech_act | offer, offer_help | covered |
| n17 | speech_act | ask, property_question | covered |
| n18 | object | object_label::scissors | label-preserved |
| n19 | claim | enables, attribute_claim, contrast, size_large | covered |
| n20 | claim | enables, conjunction, activity, size_small, attribute_claim | covered |
| n21 | claim | recommended, size_large, activity | covered |
| n22 | reasoning | designed_to_be, supports | covered |
| n23 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s7 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s1 "lawn mower" → object_label::mower, t2:s1 "gardening gloves" → object_label::gloves, t2:s1 "protective eyewear" → object_label::eyewear, t2:s9 "string trimmer" → object_label::trimmer, t2:s9 "edger" → object_label::edger, t3:s1 "scissors" → object_label::scissors
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
