Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="knife") -> subject_2 : TERM
    TERM subject(kind="table") -> subject_3 : TERM
    TERM activity(object=object_label::pan, verb="place") -> activity_2 : TERM
    TERM requirement(property="contains", value=subject_2) -> requirement_2 : TERM
    TERM requirement(property="on", value=subject_3) -> requirement_3 : TERM
    CLAIM request(target=activity_2) BY "user" STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
    CLAIM request(target=requirement_2) BY "user" STATUS asserted SOURCE "t1:s1" -> request_3 : CLAIM
    CLAIM request(target=requirement_3) BY "user" STATUS asserted SOURCE "t1:s1" -> request_4 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM activity(verb="walk_forward") -> activity_3 : TERM
    TERM activity(object=subject_3, verb="turn_left_towards") -> activity_4 : TERM
    TERM requirement(property="color", value=color_label::black) -> requirement_4 : TERM
    UTTER propose(target=activity_3)
    UTTER propose(target=activity_4)
    UTTER propose(target=requirement_4)
    TERM subject(kind="lettuce") -> subject_4 : TERM
    TERM activity(object=object_label::knife, verb="pick_up") -> activity_5 : TERM
    TERM requirement(property="next_to", value=subject_4) -> requirement_5 : TERM
    TERM requirement(property="closest", value=rank_distance) -> requirement_6 : TERM
    UTTER propose(target=activity_5)
    UTTER propose(target=requirement_5)
    UTTER propose(target=requirement_6)
    TERM activity(verb="turn_around") -> activity_6 : TERM
    TERM subject(kind="stove_top") -> subject_5 : TERM
    TERM activity(object=subject_5, verb="go_to") -> activity_7 : TERM
    TERM requirement(property="located", value=left_of) -> requirement_7 : TERM
    UTTER propose(target=activity_6)
    UTTER propose(target=activity_7)
    UTTER propose(target=requirement_7)
    TERM subject(kind="pan") -> subject_6 : TERM
    TERM subject(kind="burner", qualifier="back_left") -> subject_7 : TERM
    TERM activity(object=object_label::knife, verb="put_into") -> activity_8 : TERM
    TERM requirement(property="into", value=subject_6) -> requirement_8 : TERM
    TERM requirement(property="on", value=subject_7) -> requirement_9 : TERM
    UTTER propose(target=activity_8)
    UTTER propose(target=requirement_8)
    UTTER propose(target=requirement_9)
    TERM activity(object=object_label::pan, verb="take") -> activity_9 : TERM
    TERM requirement(property="from", value=subject_5) -> requirement_10 : TERM
    UTTER propose(target=activity_9)
    UTTER propose(target=requirement_10)
    TERM activity(verb="turn_left") -> activity_10 : TERM
    TERM subject(kind="safe") -> subject_8 : TERM
    TERM activity(object=subject_8, verb="walk_towards") -> activity_11 : TERM
    TERM activity(object=subject_3, verb="turn_left_to_face") -> activity_12 : TERM
    UTTER propose(target=activity_10)
    UTTER propose(target=activity_11)
    UTTER propose(target=activity_12)
    TERM activity(object=object_label::pan, verb="put_on") -> activity_13 : TERM
    TERM requirement(property="on", value=subject_3) -> requirement_11 : TERM
    TERM requirement(property="left_side_of", value=subject_3) -> requirement_12 : TERM
    TERM requirement(property="above", value=subject_4) -> requirement_13 : TERM
    UTTER propose(target=activity_13)
    UTTER propose(target=requirement_11)
    UTTER propose(target=requirement_12)
    UTTER propose(target=requirement_13)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, propose | covered |
| n2 | action | activity | covered |
| n3 | object | object_label::pan | label-preserved |
| n4 | object | object_label::knife | label-preserved |
| n5 | object | subject | covered |
| n6 | constraint | requirement, subject | covered |
| n7 | action | activity | covered |
| n8 | temporal | propose (source order) | covered |
| n9 | action | activity | covered |
| n10 | object | subject | covered |
| n11 | constraint | requirement, color_label::black | label-preserved |
| n12 | action | activity | covered |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | subject | covered |
| n15 | constraint | requirement | covered |
| n16 | constraint | requirement, rank_distance | covered |
| n17 | action | activity | covered |
| n18 | action | activity | covered |
| n19 | object | subject | covered |
| n20 | constraint | requirement, left_of | covered |
| n21 | action | activity | covered |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | subject | covered |
| n24 | object | subject(kind="burner") | label-preserved |
| n25 | constraint | requirement | covered |
| n26 | action | activity | covered |
| n27 | object | object_label::pan | label-preserved |
| n28 | object | subject | covered |
| n29 | action | activity | covered |
| n30 | action | activity | covered |
| n31 | object | subject | covered |
| n32 | action | activity | covered |
| n33 | object | subject, requirement | covered |
| n34 | action | activity | covered |
| n35 | object | object_label::pan | label-preserved |
| n36 | object | subject | covered |
| n37 | object | subject | covered |
| n38 | constraint | requirement | covered |
| n39 | constraint | requirement | covered |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 and t2:s2–s14 represented; t2 step numbers (s1,s3,…) are list markers, not content
- Opaque-text spans: none
- Label-preserved spans: pan, knife, black, burner (labels only)
- Missing constructs: no spatial-relation/ordering constructor; relations and verbs are carried by requirement property strings and activity verb strings; the "black" of the table is not bound to the table term; "then" order is only source order
- Unresolved ambiguities: agent steps are instructions (proposals), not recorded actions; holder "user" is a plain string
- Check: see host check
