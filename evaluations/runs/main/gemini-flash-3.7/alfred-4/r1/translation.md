Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Apple
TASK Apple {
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::kitchen)
  ACTION face(target=object_label::counter)
  ACTION pick_up(target=food_label::apple, color=color_label::red, source=object_label::counter) -> apple_ref : REF[STRING]
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::stove)
  ACTION face(target=object_label::microwave)
  TERM lexical_label(value=object_label::microwave) -> lexical_label_2 : TERM
  ACTION open(target=lexical_label_2)
  ACTION place(target=apple_ref, destination=object_label::microwave, relation=in)
  ACTION close(target=lexical_label_2)
  ACTION heat(target=apple_ref, destination=object_label::microwave) -> apple_ref_2 : REF[STRING]
  ACTION open(target=lexical_label_2)
  ACTION pick_up(target=food_label::apple, source=object_label::microwave) -> apple_ref_3 : REF[STRING]
  ACTION close(target=lexical_label_2)
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::kitchen)
  ACTION face(target=object_label::shelf)
  ACTION place(target=apple_ref_3, destination=object_label::shelf, location=object_label::table, relation=on)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | place | covered |
| n2 | action | place | covered |
| n3 | object | food_label::apple | label-preserved |
| n4 | constraint | heat | covered |
| n5 | constraint | color_label::black | label-preserved |
| n6 | object | object_label::shelf | label-preserved |
| n7 | action | turn, walk | covered |
| n8 | action | walk | covered |
| n9 | action | turn, face | covered |
| n10 | object | object_label::counter | label-preserved |
| n11 | object | — | not-applicable |
| n12 | object | object_label::stove | label-preserved |
| n13 | action | pick_up | covered |
| n14 | object | food_label::apple | label-preserved |
| n15 | constraint | color_label::red | label-preserved |
| n16 | action | turn, walk | covered |
| n17 | action | walk, face | covered |
| n18 | object | object_label::microwave | label-preserved |
| n19 | action | open | covered |
| n20 | action | place | covered |
| n21 | action | close | covered |
| n22 | action | heat | covered |
| n23 | action | open | covered |
| n24 | action | pick_up | covered |
| n25 | action | close | covered |
| n26 | temporal | heat | covered |
| n27 | action | turn | covered |
| n28 | action | walk | covered |
| n29 | action | face | covered |
| n30 | object | object_label::table | label-preserved |
| n31 | constraint | color_label::white | label-preserved |
| n32 | object | object_label::shelf | label-preserved |
| n33 | constraint | color_label::black | label-preserved |
| n34 | action | place | covered |
| n35 | constraint | on | covered |
| n36 | constraint | food_label::egg | covered |
| n37 | object | food_label::egg | label-preserved |
| n38 | constraint | color_label::brown | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s12 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "apple" -> food_label::apple; t1:s1 "black" -> color_label::black; t1:s1 "shelves" -> object_label::shelf; t2:s2 "counter" -> object_label::counter; t2:s4 "apple" -> food_label::apple; t2:s4 "red" -> color_label::red; t2:s6 "stove" -> object_label::stove; t2:s6 "microwave" -> object_label::microwave; t2:s10 "table" -> object_label::table; t2:s10 "white" -> color_label::white; t2:s10 "shelves" -> object_label::shelf; t2:s10 "black" -> color_label::black; t2:s12 "egg" -> food_label::egg; t2:s12 "brown" -> color_label::brown
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
