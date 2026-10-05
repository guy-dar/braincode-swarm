Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelMicrowave
TASK ObjectLabelMicrowave {
  ACTION walk(destination=object_label::microwave)
  ACTION face(target=object_label::microwave)
  ACTION pick_up(target=food_label::potato, source=object_label::microwave) -> food_label_potato_ref : REF[STRING]
  ACTION walk(destination=object_label::sink)
  ACTION face(target=object_label::sink)
  ACTION rinse(target=food_label_potato_ref, destination=object_label::sink) -> food_label_potato_ref_2 : REF[STRING]
  ACTION walk(destination=object_label::fridge)
  ACTION face(target=object_label::fridge)
  ACTION place(target=food_label_potato_ref_2, destination=object_label::fridge, relation=in)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | place, rinse, in | covered |
| n2 | action | place, in | covered |
| n3 | object | food_label::potato | label-preserved |
| n4 | constraint | rinse | covered |
| n5 | object | object_label::fridge | covered |
| n6 | temporal | TASK | covered |
| n7 | action | walk, face | covered |
| n8 | object | object_label::microwave | covered |
| n9 | action | pick_up | covered |
| n10 | object | food_label::potato | label-preserved |
| n11 | object | object_label::microwave | covered |
| n12 | action | walk, face | covered |
| n13 | object | object_label::sink | covered |
| n14 | action | rinse | covered |
| n15 | action | rinse | covered |
| n16 | object | food_label::potato | label-preserved |
| n17 | object | object_label::sink | covered |
| n18 | action | walk, face | covered |
| n19 | object | object_label::fridge | covered |
| n20 | action | place, in | covered |
| n21 | object | food_label::potato | label-preserved |
| n22 | object | object_label::fridge | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s12 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "potato" → food_label::potato; t2:s4 "potato" → food_label::potato; t2:s8 "potato" → food_label::potato; t2:s12 "potato" → food_label::potato
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
