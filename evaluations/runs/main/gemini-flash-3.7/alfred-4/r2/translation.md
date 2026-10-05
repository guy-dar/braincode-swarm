Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Counter
TASK Counter {
  ACTION turn(direction="left")
  ACTION walk(destination=counter)
  ACTION face(target=counter)
  ACTION pick_up(target=apple, color=color_label::red, source=counter) -> apple_ref : REF[STRING]
  ACTION turn(direction="left")
  ACTION walk(destination=stove)
  ACTION face(target=microwave)
  ACTION open(target=microwave)
  ACTION place(target=apple_ref, destination=microwave, relation=in)
  ACTION close(target=microwave)
  ACTION heat(target=apple_ref, destination=microwave) -> apple_ref_2 : REF[STRING]
  ACTION open(target=microwave)
  ACTION pick_up(target=apple, source=microwave) -> apple_ref_3 : REF[STRING]
  ACTION close(target=microwave)
  ACTION turn(direction="around")
  ACTION walk(destination=table)
  ACTION face(target=shelf)
  ACTION place(target=apple_ref_3, destination=shelf, location=corner, relation=on)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | place | covered |
| n2 | action | heat, place | covered |
| n3 | object | apple | covered |
| n4 | constraint | heat | covered |
| n5 | constraint | color_label::black | label-preserved |
| n6 | object | shelf | covered |
| n7 | action | turn | covered |
| n8 | action | walk | covered |
| n9 | action | face | covered |
| n10 | object | counter | covered |
| n11 | object | counter | covered |
| n12 | object | stove | covered |
| n13 | action | pick_up | covered |
| n14 | object | apple | covered |
| n15 | constraint | color_label::red | label-preserved |
| n16 | action | turn | covered |
| n17 | action | face, walk | covered |
| n18 | object | microwave | covered |
| n19 | action | open | covered |
| n20 | action | in, place | covered |
| n21 | action | close | covered |
| n22 | action | heat | covered |
| n23 | action | open | covered |
| n24 | action | pick_up | covered |
| n25 | action | close | covered |
| n26 | temporal | close, heat, open, pick_up, place | covered |
| n27 | action | turn | covered |
| n28 | action | walk | covered |
| n29 | action | face | covered |
| n30 | object | table | covered |
| n31 | constraint | on | covered |
| n32 | object | shelf | covered |
| n33 | constraint | color_label::black | label-preserved |
| n34 | action | place | covered |
| n35 | constraint | corner, on | covered |
| n36 | constraint | place | covered |
| n37 | object | place | covered |
| n38 | constraint | color_label::brown | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s12 is represented
- Opaque-text spans: none
- Label-preserved spans: n5 (color_label::black), n15 (color_label::red), n33 (color_label::black), n38 (color_label::brown)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
