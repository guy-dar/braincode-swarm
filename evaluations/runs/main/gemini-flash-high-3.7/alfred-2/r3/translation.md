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
  TERM lexical_label(value=food_label::lettuce) -> lexical_label_2 : TERM
  ACTION face(target=lexical_label_2)
  ACTION slice(target=lexical_label_2) -> lexical_label_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=object_label::counter)
  ACTION place(target=object_label_knife_ref, destination=object_label::counter)
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=lexical_label_2)
  ACTION pick_up(target=food_label::lettuce, source=object_label::counter, state=state_sliced) -> food_label_lettuce_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::fridge)
  ACTION face(target=object_label::fridge)
  ACTION chill(target=food_label_lettuce_ref, destination=object_label::fridge) -> food_label_lettuce_ref_2 : REF[STRING]
  TERM lexical_label(value=object_label::fridge) -> lexical_label_3 : TERM
  ACTION remove(target=food_label_lettuce_ref_2, source=lexical_label_3)
  ACTION turn(direction="left")
  ACTION face(target=object_label::counter)
  ACTION place(target=food_label_lettuce_ref_2, destination=object_label::counter, location=object_label::sink, relation=right_of)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | chill | covered |
| n2 | object | food_label::lettuce | label-preserved |
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
| n19 | action | turn, face | covered |
| n20 | action | place, right_of | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1, t2:s6, t2:s8, t2:s14, t2:s16, t2:s20, t2:s24 "lettuce" → food_label::lettuce (label only; no sense resolved); t1:s1, t2:s6, t2:s8, t2:s10, t2:s12, t2:s14, t2:s16, t2:s22, t2:s24 "counter" → object_label::counter (label only; no sense resolved); t2:s2, t2:s4, t2:s24 "sink" → object_label::sink (label only; no sense resolved); t2:s4, t2:s12 "knife" → object_label::knife (label only; no sense resolved); t2:s18, t2:s20 "fridge" → object_label::fridge (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
