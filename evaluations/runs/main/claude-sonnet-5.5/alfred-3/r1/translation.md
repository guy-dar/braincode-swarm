Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM spatial_relation(figure=object_label::knife, ground=object_label::pan, relation=in) -> spatial_relation_2 : TERM   # PROPOSED: S1
    TERM activity(verb="put", object=spatial_relation_2, destination=object_label::table) -> activity_2 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM activity(verb="walk", modifier="forward") -> activity_3 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_3)
    TERM requirement(property="color", value=color_label::black) -> requirement_2 : TERM   # PROPOSED: S3
    TERM spatial_relation(figure=object_label::table, ground=object_label::table, relation=left_of) -> spatial_relation_3 : TERM   # PROPOSED: S1
    TERM activity(verb="turn", modifier="left", destination=requirement_2) -> activity_4 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_4)
    TERM spatial_relation(figure=object_label::knife, ground=food_label::lettuce, relation=next_to) -> spatial_relation_4 : TERM   # PROPOSED: S1
    TERM requirement(property="rank_field", value=rank_distance) -> requirement_3 : TERM
    TERM activity(verb="pick_up", object=spatial_relation_4, modifier=requirement_3) -> activity_5 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_5)
    TERM activity(verb="turn", modifier="around") -> activity_6 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_6)
    TERM spatial_relation(figure=object_label::stove, ground=object_label::stove, relation=left_of) -> spatial_relation_5 : TERM   # PROPOSED: S1
    TERM activity(verb="walk", destination=spatial_relation_5) -> activity_7 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_7)
    TERM spatial_relation(figure=object_label::pan, ground=object_label::burner, relation=on) -> spatial_relation_6 : TERM   # PROPOSED: S1
    TERM activity(verb="put", object=object_label::knife, destination=spatial_relation_6) -> activity_8 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_8)
    TERM activity(verb="pick_up", object=object_label::pan, location=object_label::stove) -> activity_9 : TERM
    UTTER propose(target=activity_9)
    TERM activity(verb="turn", modifier="left") -> activity_10 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_10)
    TERM activity(verb="walk", destination=object_label::safe) -> activity_11 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_11)
    TERM activity(verb="turn", modifier="left", destination=requirement_2) -> activity_12 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_12)
    TERM spatial_relation(figure=object_label::pan, ground=object_label::table, relation=on) -> spatial_relation_7 : TERM   # PROPOSED: S1
    TERM activity(verb="put", object=food_label::lettuce, destination=spatial_relation_7) -> activity_13 : TERM   # PROPOSED: S2
    UTTER propose(target=activity_13)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | propose, activity | proposed |
| n2 | action | activity (put) | proposed |
| n3 | object | object_label::pan | label-preserved |
| n4 | object | object_label::knife | label-preserved |
| n5 | object | object_label::table | label-preserved |
| n6 | constraint | spatial_relation (PROPOSED S1) | proposed |
| n7 | action | activity | proposed |
| n8 | temporal | source order only | unresolved |
| n9 | action | activity, object_label::table | proposed |
| n10 | object | object_label::table | label-preserved |
| n11 | constraint | requirement, color_label::black | proposed |
| n12 | action | activity | proposed |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | food_label::lettuce | label-preserved |
| n15 | constraint | spatial_relation, next_to | proposed |
| n16 | constraint | requirement, rank_distance | covered |
| n17 | action | activity | proposed |
| n18 | action | activity | proposed |
| n19 | object | object_label::stove | label-preserved |
| n20 | constraint | spatial_relation, left_of | proposed |
| n21 | action | activity | proposed |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | object_label::pan | label-preserved |
| n24 | object | object_label::burner | label-preserved |
| n25 | constraint | spatial_relation, on | proposed |
| n26 | action | activity | covered |
| n27 | object | object_label::pan | label-preserved |
| n28 | object | object_label::stove | label-preserved |
| n29 | action | activity | proposed |
| n30 | action | activity | proposed |
| n31 | object | object_label::safe | label-preserved |
| n32 | action | activity | proposed |
| n33 | object | requirement, object_label::table | proposed |
| n34 | action | activity | proposed |
| n35 | object | object_label::pan | label-preserved |
| n36 | object | object_label::table | label-preserved |
| n37 | object | food_label::lettuce | label-preserved |
| n38 | constraint | spatial_relation, left_of | proposed |
| n39 | constraint | spatial_relation | unresolved |

## Why the translation failed

- n6, n15, n20, n25, n38, n39: search "in/next to/left of/on/above" → only bare spatial-relation values (`in_front_of`, `left_of`, `next_to`, `on`, `under`) with no TERM constructor to relate a figure to a ground; place.relation only exists inside operation ACTION. Proposed S1. No `above` value exists (n39 unresolved; `under` is the opposite).
- n7, n9, n17, n29, n32: operations walk/turn are ACTIONs, not usable inside UTTER; `activity` has no direction/destination argument. Proposed S2.
- n11, n33: `requirement.value` does not accept ATOM[color_label]. Proposed S3.
- n8 "then": `then` link requires EVENTs, which do not exist in REQUEST; order is source order only.
- n24 "back left burner": `resource_heater` is abstract; burner as label-preserved; "back" has no value.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all of t1:s1, t2:s2–t2:s14 represented; step numbers ("1.") are list markers and omitted; "above" (t2:s14), "back" (t2:s8), "then" (t2:s2), "face" of t2:s12 only approximated
- Opaque-text spans: none
- Label-preserved spans: pan, knife, table, lettuce, stove, burner, safe → group labels only
- Missing constructs: S1 spatial_relation; S2 activity modifier/destination; S3 requirement color
- Unresolved ambiguities: t2:s14 "on the left side of the table above the lettuce" attachments unclear (the lettuce object of put is a mis-parse risk; likely pan placed on table, left side, above lettuce); relations for "left side of table" approximated; "put the pan on the table" attachments simplified
- Check: not run
