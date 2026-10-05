Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelSink
TASK ObjectLabelSink {
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::sink)
  ACTION face(target=object_label::sink)
  ACTION pick_up(target=object_label::knife, source=object_label::sink) -> knife_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=object_label::counter)
  TERM lexical_label(value=food_label::lettuce) -> lexical_label_2 : TERM
  ACTION slice(target=lexical_label_2) -> lettuce_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=object_label::counter)
  ACTION place(target=knife_ref, destination=object_label::counter)
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=object_label::counter)
  ACTION pick_up(target=food_label::lettuce, source=object_label::counter, state=state_sliced) -> lettuce_ref_2 : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::fridge)
  ACTION face(target=object_label::fridge)
  ACTION chill(target=lettuce_ref_2, destination=object_label::fridge) -> lettuce_ref_3 : REF[STRING]
  ACTION remove(target=lettuce_ref_3, source=object_label::fridge)
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=object_label::counter)
  ACTION place(target=lettuce_ref_3, destination=object_label::counter, location=object_label::sink, relation=right_of)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | chill, slice | covered |
| n2 | object | food_label::lettuce, state_sliced | label-preserved |
| n3 | action | place | covered |
| n4 | object | object_label::counter | label-preserved |
| n5 | action | face, turn, walk | covered |
| n6 | object | object_label::sink | label-preserved |
| n7 | action | pick_up | covered |
| n8 | object | object_label::knife | label-preserved |
| n9 | action | face, turn, walk | covered |
| n10 | object | food_label::lettuce | label-preserved |
| n11 | action | slice | covered |
| n12 | action | face, turn, walk | covered |
| n13 | action | place | covered |
| n14 | action | face, turn, walk | covered |
| n15 | action | pick_up, state_sliced | covered |
| n16 | action | face, turn, walk | covered |
| n17 | object | object_label::fridge | label-preserved |
| n18 | action | chill, remove | covered |
| n19 | action | face, turn, walk | covered |
| n20 | action | place, right_of | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "lettuce" → food_label::lettuce, t1:s1 "counter" → object_label::counter, t2:s2 "sink" → object_label::sink, t2:s4 "knife" → object_label::knife, t2:s6 "lettuce" → food_label::lettuce, t2:s18 "fridge" → object_label::fridge
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
