Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM time_point(date="weekend") -> time_point_2 : TERM
    TERM requirement(property="ideas", value=2) -> requirement_2 : TERM
    TERM subject(kind="performance", qualifier=style_academic, time="week") -> subject_2 : TERM
    TERM activity(actor="user", object=role_daughter, purpose=subject_2, verb="reward") -> activity_2 : TERM
    TERM activity(actor="user", object=role_daughter, purpose=activity_2, verb="spend_day_off") -> activity_3 : TERM
    UTTER ask(target=activity_3, constraints=[requirement_2])
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(actor=role_daughter, object="nature_reserve", verb="visit") -> activity_4 : TERM
    TERM activity(object=object_label::pinecone, verb="find") -> activity_5 : TERM
    TERM activity(object=animal_label::butterfly, verb="spot") -> activity_6 : TERM
    TERM activity(object=animal_label::bird, verb="hear") -> activity_7 : TERM
    TERM conjunction(items=[activity_5, activity_6, activity_7]) -> conjunction_2 : TERM
    TERM activity(object=conjunction_2, verb="scavenger_hunt") -> activity_8 : TERM
    TERM activity(actor="user", instrument=waterproof_stickers, object=role_daughter, purpose=activity_8, verb="give_prize") -> activity_9 : TERM
    TERM activity(object=food_label::sandwich, verb="pack") -> activity_10 : TERM
    TERM activity(object=food_label::fruit, verb="pack") -> activity_11 : TERM
    TERM activity(object=ice_cream, verb="pack") -> activity_12 : TERM
    TERM activity(object=food_label::cookie, verb="pack") -> activity_13 : TERM
    TERM conjunction(items=[activity_10, activity_11, activity_12, activity_13]) -> conjunction_3 : TERM
    TERM activity(object=conjunction_3, verb="picnic") -> activity_14 : TERM
    TERM activity(actor="user", object=gift, verb="give_gift") -> activity_15 : TERM
    TERM sequence(items=[activity_4, activity_8, activity_9, activity_14, activity_15]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM activity(object="science_experiments", verb="setup") -> activity_16 : TERM
    TERM activity(object="craft_project", verb="setup") -> activity_17 : TERM
    TERM conjunction(items=[activity_16, activity_17]) -> conjunction_4 : TERM
    TERM subject(kind="achievement", qualifier=style_academic) -> subject_3 : TERM
    TERM activity(actor="user", object=role_daughter, purpose=subject_3, verb="award_ceremony") -> activity_18 : TERM
    TERM activity(actor="user", object="science", verb="explain") -> activity_19 : TERM
    TERM activity(actor="user", object=role_daughter, purpose=activity_19, verb="collaborate") -> activity_20 : TERM
    TERM activity(instrument=food_label::popcorn, object="movie", verb="watch") -> activity_21 : TERM
    TERM sequence(items=[conjunction_4, activity_18, activity_20, activity_21]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    CLAIM enables(condition=sequence_2, outcome=t1.activity_2) BY role_agent STATUS inferred SOURCE "t2:s21" -> enables_2 : CLAIM
    TERM well_wishes(recipient=role_daughter, sentiment="enjoy_day") -> well_wishes_2 : TERM
    UTTER respond(target=well_wishes_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | temporal | time_point | covered |
| n2 | speech_act | ask, activity | covered |
| n3 | constraint | requirement | covered |
| n4 | object | role_daughter, activity | covered |
| n5 | reasoning | style_academic, subject, activity | covered |
| n6 | speech_act | propose, sequence | covered |
| n7 | action | activity | covered |
| n8 | action | activity, conjunction | covered |
| n9 | object | animal_label::butterfly | label-preserved |
| n10 | object | animal_label::bird | label-preserved |
| n11 | action | activity, waterproof_stickers | covered |
| n12 | action | activity, conjunction | covered |
| n13 | object | food_label::sandwich | label-preserved |
| n14 | object | food_label::fruit | label-preserved |
| n15 | object | ice_cream, activity | covered |
| n16 | object | food_label::cookie | label-preserved |
| n17 | action | activity, gift | covered |
| n18 | speech_act | propose, sequence | covered |
| n19 | action | activity, conjunction | covered |
| n20 | action | activity, subject, style_academic | covered |
| n21 | action | activity | covered |
| n22 | action | activity | covered |
| n23 | object | food_label::popcorn | label-preserved |
| n24 | claim | enables | covered |
| n25 | speech_act | respond, well_wishes, role_daughter | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s22 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s5 "butterfly" → animal_label::butterfly, t2:s5 "bird" → animal_label::bird, t2:s8 "sandwiches" → food_label::sandwich, t2:s8 "fruit" → food_label::fruit, t2:s8 "cookie" → food_label::cookie, t2:s20 "popcorn" → food_label::popcorn
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
