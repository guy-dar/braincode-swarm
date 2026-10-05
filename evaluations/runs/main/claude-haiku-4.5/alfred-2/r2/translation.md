Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="cool", object=food_label::lettuce) -> cool_activity : TERM
    TERM activity(verb="place", object=food_label::lettuce, location=object_label::counter) -> place_activity : TERM
    CLAIM request(target=sequence(items=[cool_activity, place_activity])) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s2" -> turn_event_1 : EVENT
    RECORD ACTION walk(destination=object_label::sink) STATUS succeeded SOURCE "t2:s2" -> walk_event_1 : EVENT
    RECORD ACTION pick_up(target=object_label::knife, source=object_label::sink) STATUS succeeded SOURCE "t2:s4" -> pick_up_event_1 : EVENT
    RECORD ACTION turn(direction="right") STATUS succeeded SOURCE "t2:s6" -> turn_event_2 : EVENT
    RECORD ACTION face(target=food_label::lettuce) STATUS succeeded SOURCE "t2:s6" -> face_event_1 : EVENT
    RECORD ACTION slice(target=food_label::lettuce) STATUS succeeded SOURCE "t2:s8" -> slice_event : EVENT
    RECORD ACTION turn(direction="right") STATUS succeeded SOURCE "t2:s10" -> turn_event_3 : EVENT
    RECORD ACTION face(target=object_label::counter) STATUS succeeded SOURCE "t2:s10" -> face_event_2 : EVENT
    RECORD ACTION place(target=object_label::knife, destination=object_label::counter) STATUS succeeded SOURCE "t2:s12" -> place_event_1 : EVENT
    RECORD ACTION turn(direction="right") STATUS succeeded SOURCE "t2:s14" -> turn_event_4 : EVENT
    RECORD ACTION face(target=food_label::lettuce) STATUS succeeded SOURCE "t2:s14" -> face_event_3 : EVENT
    RECORD ACTION pick_up(target=food_label::lettuce, state=state_sliced, source=object_label::counter) STATUS succeeded SOURCE "t2:s16" -> pick_up_event_2 : EVENT
    RECORD ACTION turn(direction="right") STATUS succeeded SOURCE "t2:s18" -> turn_event_5 : EVENT
    RECORD ACTION face(target=object_label::fridge) STATUS succeeded SOURCE "t2:s18" -> face_event_4 : EVENT
    RECORD ACTION chill(target=food_label::lettuce, destination=object_label::fridge) STATUS succeeded SOURCE "t2:s20" -> chill_event : EVENT
    RECORD ACTION remove(target=food_label::lettuce, source=object_label::fridge) STATUS succeeded SOURCE "t2:s20" -> remove_event : EVENT
    RECORD ACTION face(target=object_label::counter) STATUS succeeded SOURCE "t2:s22" -> face_event_5 : EVENT
    RECORD ACTION place(target=food_label::lettuce, destination=object_label::counter, location=object_label::sink, relation=right_of) STATUS succeeded SOURCE "t2:s24" -> place_event_2 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | chill | covered |
| n2 | object | food_label::lettuce with state=state_sliced | label-preserved |
| n3 | action | place | covered |
| n4 | object | object_label::counter | label-preserved |
| n5 | action | turn, walk, face | covered |
| n6 | object | object_label::sink | label-preserved |
| n7 | action | pick_up | covered |
| n8 | object | object_label::knife | label-preserved |
| n9 | action | turn, face | covered |
| n10 | object | food_label::lettuce | label-preserved |
| n11 | action | slice | covered |
| n12 | action | turn, face | covered |
| n13 | action | place | covered |
| n14 | action | turn, face | covered |
| n15 | action | pick_up with state=state_sliced qualifier | covered |
| n16 | action | turn, face | covered |
| n17 | object | object_label::fridge | label-preserved |
| n18 | action | chill, remove | covered |
| n19 | action | face | covered |
| n20 | action | place with location and spatial relation | covered |

## Translation report

- Input kind: conversation (multi-turn exchange)
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s24 is represented with t1 recording the user's request and t2 recording the agent's action sequence
- Opaque-text spans: none
- Label-preserved spans: n2, n4, n6, n8, n10, n17 — entities expressed via open-group labels (object_label::*, food_label::*) with their role and domain preserved without additional semantic elaboration
- Missing constructs: none
- Unresolved ambiguities: none (n19 "take a step to the left to face the counter" interpreted as face action toward counter; n20 spatial relation "to the right of the sink" expressed via place location and relation parameters)
- Check: passing validation
```

Perfect! Now let me verify the syntax is valid by checking a few key symbols and structure:
<function_calls>
<invoke name="bash">
<parameter name="command">cd /output && node /kit/rag.mjs check --translation translation.md 2>&1 | head -100