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
  ACTION pick_up(target=object_label::knife, source=object_label::sink) -> object_label_knife_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=food_label::lettuce)
  ACTION slice(target=food_label::lettuce) -> food_label_lettuce_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=object_label::counter)
  ACTION place(target=object_label_knife_ref, destination=object_label::counter)
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=food_label::lettuce)
  ACTION pick_up(target=food_label::lettuce, source=object_label::counter, state=state_sliced) -> food_label_lettuce_ref_2 : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::fridge)
  ACTION face(target=object_label::fridge)
  ACTION chill(target=food_label_lettuce_ref_2, destination=object_label::fridge) -> food_label_lettuce_ref_3 : REF[STRING]
  ACTION remove(target=food_label_lettuce_ref_3, source=object_label::fridge)
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=object_label::counter)
  ACTION place(target=food_label_lettuce_ref_3, destination=object_label::counter, location=object_label::sink, relation=right_of)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | chill | covered |
| n2 | object | food_label::lettuce, state_sliced | label-preserved |
| n3 | action | place | covered |
| n4 | object | object_label::counter | label-preserved |
| n5 | action | turn, walk, face | covered |
| n6 | object | object_label::sink | label-preserved |
| n7 | action | pick_up | covered |
| n8 | object | object_label::knife | label-preserved |
| n9 | action | turn, walk, face | covered |
| n10 | object | food_label::lettuce | label-preserved |
| n11 | action | slice | covered |
| n12 | action | turn, walk, face | covered |
| n13 | action | place | covered |
| n14 | action | turn, walk, face | covered |
| n15 | action | pick_up, state_sliced | covered |
| n16 | action | turn, walk, face | covered |
| n17 | object | object_label::fridge | label-preserved |
| n18 | action | chill, remove | covered |
| n19 | action | turn, walk, face | covered |
| n20 | action | place, right_of | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: food_label::lettuce, object_label::counter, object_label::sink, object_label::knife, object_label::fridge
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
