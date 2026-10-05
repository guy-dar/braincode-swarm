Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM time_point(date="weekend") -> time_point_2 : TERM
    TERM requirement(property="count", value=2) -> requirement_2 : TERM
    TERM temporal_context(activity="school", period=unit_week) -> temporal_context_2 : TERM
    TERM activity(actor=role_daughter, object=style_academic, purpose=temporal_context_2, verb="reward") -> activity_2 : TERM
    TERM activity(actor=role_daughter, purpose=activity_2, verb="spend_day_off") -> activity_3 : TERM
    UTTER ask(target=activity_3, constraints=[requirement_2])
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(object="nature_reserve", verb="visit") -> activity_4 : TERM
    TERM activity(object="pinecone", verb="find") -> activity_5 : TERM
    TERM activity(object=animal_label::butterfly, verb="find") -> activity_6 : TERM
    TERM activity(object=animal_label::bird, verb="hear") -> activity_7 : TERM
    TERM activity(instrument=size_small, object=waterproof_stickers, verb="give_prize") -> activity_8 : TERM
    TERM activity(object="picnic", verb="eat_lunch") -> activity_9 : TERM
    TERM activity(object=food_label::sandwich, verb="pack") -> activity_10 : TERM
    TERM activity(object=food_label::fruit, verb="pack") -> activity_11 : TERM
    TERM activity(object=ice_cream, verb="pack") -> activity_12 : TERM
    TERM activity(object=food_label::cookie, verb="pack") -> activity_13 : TERM
    TERM activity(object=gift, verb="give") -> activity_14 : TERM
    TERM sequence(items=[activity_4, activity_5, activity_6, activity_7, activity_8, activity_9, activity_10, activity_11, activity_12, activity_13, activity_14]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM activity(object=lamp, verb="experiment") -> activity_15 : TERM
    TERM activity(object=style_academic, verb="hold_award_ceremony") -> activity_16 : TERM
    TERM activity(object="science", verb="explain") -> activity_17 : TERM
    TERM activity(object=food_label::popcorn, verb="watch_movie") -> activity_18 : TERM
    TERM sequence(items=[activity_15, activity_16, activity_17, activity_18]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    CLAIM enables(condition=sequence_2, outcome=t1.activity_2) BY role_agent STATUS asserted SOURCE "t2:s21" -> enables_2 : CLAIM
    CLAIM enables(condition=sequence_3, outcome=t1.activity_2) BY role_agent STATUS asserted SOURCE "t2:s21" -> enables_3 : CLAIM
    TERM well_wishes(recipient=role_daughter, sentiment="enjoy_day") -> well_wishes_2 : TERM
    UTTER express_interest(target=well_wishes_2)
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
| n5 | reasoning | unit_week, role_daughter, style_academic, temporal_context, activity | covered |
| n6 | speech_act | propose | covered |
| n7 | action | activity | covered |
| n8 | action | activity | covered |
| n9 | object | animal_label::butterfly | label-preserved |
| n10 | object | animal_label::bird | label-preserved |
| n11 | action | size_small, waterproof_stickers, activity | covered |
| n12 | action | activity | covered |
| n13 | object | food_label::sandwich | label-preserved |
| n14 | object | food_label::fruit | label-preserved |
| n15 | object | ice_cream, activity | covered |
| n16 | object | food_label::cookie, activity | label-preserved |
| n17 | action | gift, activity | covered |
| n18 | speech_act | propose | covered |
| n19 | action | lamp, activity | covered |
| n20 | action | style_academic, activity | covered |
| n21 | action | activity | covered |
| n22 | action | activity | covered |
| n23 | object | food_label::popcorn, activity | label-preserved |
| n24 | claim | enables, role_agent | covered |
| n25 | speech_act | role_daughter, well_wishes, express_interest | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s5 "butterfly" -> animal_label::butterfly (label only); t2:s5 "bird" -> animal_label::bird (label only); t2:s8 "sandwich" -> food_label::sandwich (label only); t2:s8 "fruit" -> food_label::fruit (label only); t2:s8 "cookie" -> food_label::cookie (label only); t2:s20 "popcorn" -> food_label::popcorn (label only)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
