Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="cool a lettuce slice and place it on the counter")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO=t1 {
    RECORD ACTION turn(direction="left") STATUS attempted SOURCE "t2:s2" -> turn_1_event : EVENT
    RECORD ACTION walk(destination=sink) STATUS attempted SOURCE "t2:s2" -> walk_1_event : EVENT
    RECORD ACTION pick_up(target=knife, source=sink) STATUS attempted SOURCE "t2:s4" -> pick_up_1_event : EVENT
    RECORD ACTION turn(direction="around") STATUS attempted SOURCE "t2:s6" -> turn_2_event : EVENT
    RECORD ACTION face(target=lettuce) STATUS attempted SOURCE "t2:s6" -> face_1_event : EVENT
    RECORD ACTION slice(target=lettuce) STATUS attempted SOURCE "t2:s8" -> slice_1_event : EVENT
    RECORD ACTION turn(direction="around") STATUS attempted SOURCE "t2:s10" -> turn_3_event : EVENT
    RECORD ACTION face(target=counter) STATUS attempted SOURCE "t2:s10" -> face_2_event : EVENT
    RECORD ACTION place(target=knife, destination=counter) STATUS attempted SOURCE "t2:s12" -> place_1_event : EVENT
    RECORD ACTION turn(direction="around") STATUS attempted SOURCE "t2:s14" -> turn_4_event : EVENT
    RECORD ACTION face(target=lettuce) STATUS attempted SOURCE "t2:s14" -> face_3_event : EVENT
    RECORD ACTION pick_up(target=lettuce, state=state_sliced, source=counter) STATUS attempted SOURCE "t2:s16" -> pick_up_2_event : EVENT
    RECORD ACTION turn(direction="around") STATUS attempted SOURCE "t2:s18" -> turn_5_event : EVENT
    RECORD ACTION face(target=fridge) STATUS attempted SOURCE "t2:s18" -> face_4_event : EVENT
    RECORD ACTION chill(target=lettuce, destination=fridge) STATUS attempted SOURCE "t2:s20" -> chill_1_event : EVENT
    RECORD ACTION remove(target=lettuce, source=fridge) STATUS attempted SOURCE "t2:s20" -> remove_1_event : EVENT
    RECORD ACTION face(target=counter) STATUS attempted SOURCE "t2:s22" -> face_5_event : EVENT
    RECORD ACTION place(target=lettuce, destination=counter, location=sink, relation=right_of) STATUS attempted SOURCE "t2:s24" -> place_2_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | chill | covered |
| n2 | object | lettuce | covered |
| n3 | action | place | covered |
| n4 | object | counter | covered |
| n5 | action | turn, walk | covered |
| n6 | object | sink | covered |
| n7 | action | pick_up | covered |
| n8 | object | knife | covered |
| n9 | action | turn, face | covered |
| n10 | object | lettuce | covered |
| n11 | action | slice | covered |
| n12 | action | turn, face | covered |
| n13 | action | place | covered |
| n14 | action | turn, face | covered |
| n15 | action | pick_up | covered |
| n16 | action | turn, face | covered |
| n17 | object | fridge | covered |
| n18 | action | chill, remove | covered |
| n19 | action | face | covered |
| n20 | action | place | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: all source segments t1:s1 and t2:s2 through t2:s24 are represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` should report 0 unresolved needs and 0 unknown symbols
