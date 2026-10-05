Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM time_point(date="weekend") -> time_point_2 : TERM
    TERM requirement(property="idea_count", value=2) -> requirement_2 : TERM
    TERM activity(actor=role_daughter, verb="spend_day_off") -> activity_2 : TERM
    TERM subject(kind="academic_performance", qualifier=style_academic, time="week") -> subject_2 : TERM
    TERM activity(actor=role_daughter, purpose=subject_2, verb="reward") -> activity_3 : TERM
    TERM conjunction(items=[activity_2, activity_3]) -> conjunction_2 : TERM
    UTTER ask(target=conjunction_2, constraints=[requirement_2], topic=time_point_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="idea", qualifier="mini_adventure_day_out") -> subject_3 : TERM
    UTTER propose(target=subject_3)
    TERM activity(actor=role_daughter, object=object_label::zoo, verb="visit") -> activity_4 : TERM
    TERM activity(actor=role_daughter, object=object_label::pinecone, verb="find") -> activity_5 : TERM
    TERM activity(actor=role_daughter, object=animal_label::butterfly, verb="spot") -> activity_6 : TERM
    TERM activity(actor=role_daughter, object=animal_label::bird, verb="hear") -> activity_7 : TERM
    TERM conjunction(items=[activity_5, activity_6, activity_7]) -> conjunction_3 : TERM
    TERM activity(actor=role_daughter, purpose=conjunction_3, verb="scavenger_hunt") -> activity_8 : TERM
    TERM requirement(property="size", value=size_small) -> requirement_3 : TERM
    TERM activity(actor=role_daughter, object=object_label::sticker, verb="give_prize") -> activity_9 : TERM
    TERM activity(actor=role_daughter, object=object_label::bookmark, verb="give_prize") -> activity_10 : TERM
    TERM activity(actor=role_daughter, object=food_label::sandwich, verb="pack") -> activity_11 : TERM
    TERM activity(actor=role_daughter, object=food_label::fruit, verb="pack") -> activity_12 : TERM
    TERM activity(actor=role_daughter, object=ice_cream, verb="pack_treat") -> activity_13 : TERM
    TERM activity(actor=role_daughter, object=food_label::cookie, verb="pack_treat") -> activity_14 : TERM
    TERM conjunction(items=[activity_11, activity_12, activity_13, activity_14]) -> conjunction_4 : TERM
    TERM activity(actor=role_daughter, purpose=conjunction_4, verb="picnic") -> activity_15 : TERM
    TERM activity(actor=role_daughter, object=object_label::keepsake, verb="pick") -> activity_16 : TERM
    TERM activity(actor=role_daughter, object=object_label::certificate, verb="give") -> activity_17 : TERM
    TERM subject(kind="idea", qualifier="science_celebration_party") -> subject_4 : TERM
    UTTER propose(target=subject_4)
    TERM activity(object=object_label::lamp, verb="experiment") -> activity_18 : TERM
    TERM activity(object=object_label::slime, verb="experiment") -> activity_19 : TERM
    TERM activity(object=object_label::volcano, verb="experiment") -> activity_20 : TERM
    TERM conjunction(items=[activity_18, activity_19, activity_20]) -> conjunction_5 : TERM
    TERM activity(purpose=conjunction_5, verb="set_up") -> activity_21 : TERM
    TERM subject(kind="academic_achievement", qualifier=style_academic) -> subject_5 : TERM
    TERM activity(actor=role_daughter, object=object_label::diploma, verb="create") -> activity_22 : TERM
    TERM activity(actor=role_daughter, object=object_label::trophy, verb="create") -> activity_23 : TERM
    TERM activity(actor=role_daughter, purpose=subject_5, verb="award_ceremony") -> activity_24 : TERM
    TERM activity(actor=role_daughter, verb="do_experiments") -> activity_25 : TERM
    TERM activity(actor=role_daughter, verb="explain_science") -> activity_26 : TERM
    TERM temporal_context(activity=activity_25) -> temporal_context_2 : TERM
    TERM activity(actor=role_daughter, object=object_label::blanket, verb="build_fort") -> activity_27 : TERM
    TERM activity(actor=role_daughter, object=food_label::popcorn, verb="eat") -> activity_28 : TERM
    TERM conjunction(items=[activity_27, activity_28]) -> conjunction_6 : TERM
    TERM activity(actor=role_daughter, purpose=conjunction_6, verb="movie_night") -> activity_29 : TERM
    CLAIM enables(condition=subject_4, outcome=activity_24) BY role_agent STATUS asserted SOURCE "t2:s21" -> enables_2 : CLAIM
    TERM well_wishes(recipient=role_daughter, sentiment="enjoy_day") -> well_wishes_2 : TERM
    UTTER express_interest(target=well_wishes_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | temporal | time_point | covered |
| n2 | speech_act | activity, ask, conjunction, requirement, time_point | covered |
| n3 | constraint | requirement | covered |
| n4 | object | activity, role_daughter | covered |
| n5 | reasoning | activity, role_daughter, style_academic, subject | covered |
| n6 | speech_act | propose, subject | covered |
| n7 | action | activity, object_label::zoo, role_daughter | covered |
| n8 | action | activity, conjunction, role_daughter | covered |
| n9 | object | animal_label::butterfly | label-preserved |
| n10 | object | animal_label::bird | label-preserved |
| n11 | action | activity, object_label::bookmark, object_label::sticker, requirement, role_daughter, size_small | covered |
| n12 | action | activity, conjunction, role_daughter | covered |
| n13 | object | food_label::sandwich | label-preserved |
| n14 | object | food_label::fruit | label-preserved |
| n15 | object | activity, ice_cream, role_daughter | covered |
| n16 | object | food_label::cookie | label-preserved |
| n17 | action | activity, object_label::certificate, object_label::keepsake, role_daughter | covered |
| n18 | speech_act | propose, subject | covered |
| n19 | action | activity, conjunction, object_label::lamp, object_label::slime, object_label::volcano | covered |
| n20 | action | activity, object_label::diploma, object_label::trophy, role_daughter, style_academic, subject | covered |
| n21 | action | activity, role_daughter, temporal_context | covered |
| n22 | action | activity, conjunction, object_label::blanket, role_daughter | covered |
| n23 | object | food_label::popcorn | label-preserved |
| n24 | claim | activity, enables, role_agent, subject | covered |
| n25 | speech_act | express_interest, role_daughter, well_wishes | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s22 is represented.
- Opaque-text spans: none
- Label-preserved spans: t2:s5 "butterfly" → animal_label::butterfly; t2:s5 "bird" → animal_label::bird; t2:s8 "sandwiches" → food_label::sandwich; t2:s8 "fruit" → food_label::fruit; t2:s8 "cookie" → food_label::cookie; t2:s20 "popcorn" → food_label::popcorn
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
