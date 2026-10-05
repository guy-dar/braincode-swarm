Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(topic="cool a lettuce slice and place it on the counter")
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s2" -> turn_event_1 : EVENT
    RECORD ACTION walk(destination=object_label::sink) STATUS succeeded SOURCE "t2:s2" -> walk_event_1 : EVENT
    RECORD ACTION face(target=object_label::sink) STATUS succeeded SOURCE "t2:s2" -> face_event_1 : EVENT
    RECORD ACTION pick_up(target=object_label::knife, source=object_label::sink) STATUS succeeded SOURCE "t2:s4" -> pick_up_knife_event : EVENT
    RECORD ACTION turn(direction="around") STATUS succeeded SOURCE "t2:s6" -> turn_event_2 : EVENT
    RECORD ACTION face(target=food_label::lettuce) STATUS succeeded SOURCE "t2:s6" -> face_event_2 : EVENT
    RECORD ACTION pick_up(target=food_label::lettuce, quantity=1, source=object_label::counter) STATUS succeeded SOURCE "t2:s8" -> pick_up_lettuce_event : EVENT
    RECORD ACTION slice(target=food_label::lettuce) STATUS succeeded SOURCE "t2:s8" -> slice_event : EVENT
    RECORD ACTION place(target=object_label::knife, destination=object_label::counter) STATUS succeeded SOURCE "t2:s12" -> place_knife_event : EVENT
    RECORD ACTION turn(direction="around") STATUS succeeded SOURCE "t2:s10" -> turn_event_3 : EVENT
    RECORD ACTION face(target=object_label::counter) STATUS succeeded SOURCE "t2:s10" -> face_event_3 : EVENT
    RECORD ACTION turn(direction="around") STATUS succeeded SOURCE "t2:s14" -> turn_event_4 : EVENT
    RECORD ACTION face(target=food_label::lettuce) STATUS succeeded SOURCE "t2:s14" -> face_event_4 : EVENT
    RECORD ACTION pick_up(target=food_label::lettuce, quantity=1, state=state_sliced, source=object_label::counter) STATUS succeeded SOURCE "t2:s16" -> pick_up_slice_event : EVENT
    RECORD ACTION turn(direction="around") STATUS succeeded SOURCE "t2:s18" -> turn_event_5 : EVENT
    RECORD ACTION face(target=object_label::fridge) STATUS succeeded SOURCE "t2:s18" -> face_event_5 : EVENT
    RECORD ACTION chill(target=food_label::lettuce, destination=object_label::fridge) STATUS succeeded SOURCE "t2:s20" -> chill_event : EVENT
    RECORD ACTION remove(target=food_label::lettuce, source=object_label::fridge) STATUS succeeded SOURCE "t2:s20" -> remove_event : EVENT
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s22" -> turn_event_6 : EVENT
    RECORD ACTION face(target=object_label::counter) STATUS succeeded SOURCE "t2:s22" -> face_event_6 : EVENT
    RECORD ACTION place(target=food_label::lettuce, destination=object_label::counter, relation=right_of, location=object_label::sink) STATUS succeeded SOURCE "t2:s24" -> place_slice_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | chill | covered |
| n2 | object | food_label::lettuce | covered |
| n3 | action | place | covered |
| n4 | object | object_label::counter | covered |
| n5 | action | turn, walk, face | covered |
| n6 | object | object_label::sink | covered |
| n7 | action | pick_up | covered |
| n8 | object | object_label::knife | covered |
| n9 | action | turn, face | covered |
| n10 | object | food_label::lettuce | covered |
| n11 | action | pick_up, slice | covered |
| n12 | action | turn, face | covered |
| n13 | action | place | covered |
| n14 | action | turn, face | covered |
| n15 | action | pick_up, state_sliced | covered |
| n16 | action | turn, face | covered |
| n17 | object | object_label::fridge | covered |
| n18 | action | chill, remove | covered |
| n19 | action | turn, face | covered |
| n20 | action | place, right_of | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: all segments t1:s1 through t2:s24 are represented
- Opaque-text spans: none
- Label-preserved spans: none; all objects use food_label and object_label groups appropriately
- Missing constructs: none
- Unresolved ambiguities: none
- Check: running `rag check` to verify all symbols are in glossary
```

Now let me verify this with the check tool:
<function_calls>
<invoke name="bash">
<parameter name="command">cd / && node /kit/rag.mjs check --translation /output/translation.md 2>&1