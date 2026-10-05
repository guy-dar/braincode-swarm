Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM spatial_relation(reference=object_label::pan, relation="in", subject=object_label::knife) -> spatial_relation_1 : TERM   # PROPOSED: S1
    TERM spatial_relation(reference=object_label::table, relation=on, subject=object_label::pan) -> spatial_relation_2 : TERM   # PROPOSED: S1
    TERM activity(object=object_label::pan, verb="place") -> activity_1 : TERM
    UTTER propose(target=activity_1)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM activity(verb="walk_forward") -> activity_2 : TERM
    TERM activity(object=object_label::table, verb="turn_left_towards") -> activity_3 : TERM
    TERM activity(object=object_label::knife, verb="pick_up") -> activity_4 : TERM
    TERM spatial_relation(reference=food_label::lettuce, relation=next_to, subject=object_label::knife) -> spatial_relation_3 : TERM   # PROPOSED: S1
    TERM activity(verb="turn_around") -> activity_5 : TERM
    TERM activity(object=object_label::stove, verb="go_to") -> activity_6 : TERM
    TERM activity(object=object_label::knife, verb="put_in") -> activity_7 : TERM
    TERM activity(object=object_label::pan, verb="take_from") -> activity_8 : TERM
    TERM activity(verb="turn_left") -> activity_9 : TERM
    TERM activity(object=object_label::safe, verb="walk_towards") -> activity_10 : TERM
    TERM activity(object=object_label::table, verb="turn_left_to_face") -> activity_11 : TERM
    TERM activity(object=object_label::pan, verb="put_on") -> activity_12 : TERM
    TERM spatial_relation(reference=food_label::lettuce, relation="above", subject=object_label::table) -> spatial_relation_4 : TERM   # PROPOSED: S1
    UTTER propose(target=activity_2)
    UTTER propose(target=activity_3)
    UTTER propose(target=activity_4)
    UTTER propose(target=activity_5)
    UTTER propose(target=activity_6)
    UTTER propose(target=activity_7)
    UTTER propose(target=activity_8)
    UTTER propose(target=activity_9)
    UTTER propose(target=activity_10)
    UTTER propose(target=activity_11)
    UTTER propose(target=activity_12)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1-n6 | speech_act/object/constraint | propose, activity, spatial_relation (PROPOSED: S1) | proposed |
| n7-n10 | action/temporal | activity, propose | proposed |
| n11 | constraint | black color (no color_label qualifier slot on a table) | unresolved |
| n12-n39 | action/object/constraint | activity, spatial_relation (PROPOSED: S1), propose | proposed |

## Why the translation failed

- Spatial constraints (pan containing knife, next to lettuce, on left, back-left burner, above lettuce, closest): search found only spatial relation values (next_to, left_of, on...) with no constructor to apply them to subject/reference. Proposed S1.
- n11 "black table": color_label only accepted in search_web/pick_up slots; no descriptor constructor for qualified entities. Covered by S1-style entity qualification not available; unresolved.
- Walk/turn/pick_up/place operations exist but the trace describes agent-suggested instructions, not recorded events; modelled as activity descriptions with string verbs (weak: verbs are opaque).

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1, t2:s2-t2:s14 represented; numeric step markers (t2:s1,s3,...) are list numbering, not-applicable
- Opaque-text spans: none
- Label-preserved spans: pan, knife, table, lettuce, stove, safe as labels
- Missing constructs: S1 spatial_relation; black color qualifier; burner back-left position
- Unresolved ambiguities: "closest one" and "back left burner" not encoded; lettuce/stove top objects only labels
- Check: not fully clean
