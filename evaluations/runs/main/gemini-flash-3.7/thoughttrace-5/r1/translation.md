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
    TERM subject(kind="reward", qualifier=style_academic, time="week") -> subject_2 : TERM
    TERM activity(actor=role_daughter, purpose=subject_2, verb="spend_day_off") -> activity_2 : TERM
    CLAIM request(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
    UTTER ask(target=activity_2, constraints=[requirement_2])
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(object="nature_reserve", verb="visit") -> activity_3 : TERM
    TERM activity(object=animal_label::butterfly, verb="search") -> activity_4 : TERM
    TERM activity(object=animal_label::bird, verb="search") -> activity_5 : TERM
    TERM activity(instrument=gift, object="sticker", verb="give_prize") -> activity_6 : TERM
    TERM activity(object=food_label::sandwich, verb="eat") -> activity_7 : TERM
    TERM activity(object=food_label::fruit, verb="eat") -> activity_8 : TERM
    TERM activity(object=food_label::icecream, verb="eat") -> activity_9 : TERM
    TERM activity(object=food_label::cookie, verb="eat") -> activity_10 : TERM
    TERM activity(instrument=gift, object="certificate", verb="give_keepsake") -> activity_11 : TERM
    TERM sequence(items=[activity_3, activity_4, activity_5, activity_6, activity_7, activity_8, activity_9, activity_10, activity_11]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM activity(object="lava_lamp", verb="experiment") -> activity_12 : TERM
    TERM activity(instrument=gift, object=style_academic, verb="celebrate") -> activity_13 : TERM
    TERM temporal_context(activity="explain_science") -> temporal_context_2 : TERM
    TERM activity(purpose=temporal_context_2, verb="do_experiments") -> activity_14 : TERM
    TERM activity(object=food_label::popcorn, verb="watch_movie") -> activity_15 : TERM
    TERM sequence(items=[activity_12, activity_13, activity_14, activity_15]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    TERM subject(kind="ideas", qualifier=style_academic, time="week") -> subject_3 : TERM
    CLAIM recommended(target=subject_3) BY role_agent STATUS inferred SOURCE "t2:s21" -> recommended_2 : CLAIM
    TERM well_wishes(recipient=role_daughter, sentiment="enjoy_day") -> well_wishes_2 : TERM
    UTTER propose(target=well_wishes_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | temporal | time_point | covered |
| n2 | speech_act | ask, request | covered |
| n3 | constraint | requirement | covered |
| n4 | object | role_daughter, activity | covered |
| n5 | reasoning | style_academic, subject, activity | covered |
| n6 | speech_act | propose, sequence | covered |
| n7 | action | activity | covered |
| n8 | action | activity | covered |
| n9 | object | animal_label::butterfly | label-preserved |
| n10 | object | animal_label::bird | label-preserved |
| n11 | action | activity, gift | covered |
| n12 | action | activity | covered |
| n13 | object | food_label::sandwich | label-preserved |
| n14 | object | food_label::fruit | label-preserved |
| n15 | object | food_label::icecream | label-preserved |
| n16 | object | food_label::cookie | label-preserved |
| n17 | action | activity, gift | covered |
| n18 | speech_act | propose, sequence | covered |
| n19 | action | activity | covered |
| n20 | action | activity, gift, style_academic | covered |
| n21 | action | activity, temporal_context | covered |
| n22 | action | activity | covered |
| n23 | object | food_label::popcorn | label-preserved |
| n24 | claim | recommended, subject, style_academic | covered |
| n25 | speech_act | well_wishes, role_daughter | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s22 is represented.
- Opaque-text spans: none
- Label-preserved spans: t2:s5 "butterfly" -> animal_label::butterfly, t2:s5 "bird" -> animal_label::bird, t2:s8 "sandwich" -> food_label::sandwich, t2:s8 "fruit" -> food_label::fruit, t2:s8 "ice cream" -> food_label::icecream, t2:s8 "cookie" -> food_label::cookie, t2:s20 "popcorn" -> food_label::popcorn (labels only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
