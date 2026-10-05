Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM time_point(date="weekend") -> time_point_2 : TERM
    TERM requirement(property="ideas_count", value=2) -> requirement_2 : TERM
    TERM activity(actor="user", object=role_daughter, verb="spend_day_off") -> activity_2 : TERM
    TERM subject(kind="academic_performance", qualifier=style_academic, time=unit_week) -> subject_2 : TERM
    TERM activity(actor="user", object=role_daughter, purpose=subject_2, verb="reward") -> activity_3 : TERM
    TERM conjunction(items=[activity_2, activity_3]) -> conjunction_2 : TERM
    UTTER ask(target=conjunction_2, constraints=[requirement_2])
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(verb="visit_nature_spot") -> activity_4 : TERM
    TERM activity(object=animal_label::butterfly, verb="find_nature_item") -> activity_5 : TERM
    TERM activity(object=animal_label::bird, verb="hear_call") -> activity_6 : TERM
    TERM activity(object=object_label::sticker, verb="give_prize") -> activity_7 : TERM
    TERM activity(object=food_label::sandwich, verb="picnic_lunch") -> activity_8 : TERM
    TERM activity(object=food_label::fruit, verb="eat_fruit") -> activity_9 : TERM
    TERM activity(object=ice_cream, verb="eat_treat") -> activity_10 : TERM
    TERM activity(object=food_label::cookie, verb="eat_cookie") -> activity_11 : TERM
    TERM activity(object=gift, verb="give_keepsake") -> activity_12 : TERM
    TERM sequence(items=[activity_4, activity_5, activity_6, activity_7, activity_8, activity_9, activity_10, activity_11, activity_12]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM activity(object=object_label::lamp, verb="science_experiments") -> activity_13 : TERM
    TERM activity(object=object_label::diploma, purpose=t1.subject_2, verb="award_ceremony") -> activity_14 : TERM
    TERM activity(verb="explain_science") -> activity_15 : TERM
    TERM temporal_context(activity=activity_15) -> temporal_context_2 : TERM
    TERM activity(object=food_label::popcorn, verb="movie_night") -> activity_16 : TERM
    TERM sequence(items=[activity_13, activity_14, activity_15, activity_16]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    CLAIM enables(condition=sequence_2, outcome=t1.activity_3) BY agent STATUS asserted SOURCE "t2:s21" -> enables_2 : CLAIM
    TERM well_wishes(recipient=role_daughter, sentiment="enjoy_day") -> well_wishes_2 : TERM
    UTTER respond(target=well_wishes_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | temporal | time_point, unit_week | covered |
| n2 | speech_act | ask, activity | covered |
| n3 | constraint | requirement | covered |
| n4 | object | role_daughter, activity | covered |
| n5 | reasoning | activity, role_daughter, style_academic, subject, unit_week | covered |
| n6 | speech_act | propose, sequence | covered |
| n7 | action | activity | covered |
| n8 | action | activity | covered |
| n9 | object | animal_label::butterfly | label-preserved |
| n10 | object | animal_label::bird | label-preserved |
| n11 | action | activity, object_label::sticker | covered |
| n12 | action | activity | covered |
| n13 | object | food_label::sandwich | label-preserved |
| n14 | object | food_label::fruit | label-preserved |
| n15 | object | ice_cream | covered |
| n16 | object | food_label::cookie | label-preserved |
| n17 | action | activity, gift | covered |
| n18 | speech_act | propose, sequence | covered |
| n19 | action | activity, object_label::lamp | covered |
| n20 | action | activity, object_label::diploma, style_academic | covered |
| n21 | action | activity, temporal_context | covered |
| n22 | action | activity | covered |
| n23 | object | food_label::popcorn | label-preserved |
| n24 | claim | enables, style_academic | covered |
| n25 | speech_act | well_wishes, respond, role_daughter | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s5 "butterfly" -> animal_label::butterfly, t2:s5 "bird" -> animal_label::bird, t2:s8 "sandwich" -> food_label::sandwich, t2:s8 "fruit" -> food_label::fruit, t2:s8 "cookie" -> food_label::cookie, t2:s20 "popcorn" -> food_label::popcorn
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
