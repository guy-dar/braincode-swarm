Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Microwave
TASK Microwave {
  ACTION turn(direction="right")
  ACTION turn(direction="left")
  ACTION face(target=object_label::sink)
  ACTION pick_up(target=food_label::egg, source=object_label::sink) -> food_label_egg_ref : REF[STRING]
  ACTION turn(direction="right")
  ACTION face(target=object_label::microwave)
  ACTION place(target=food_label_egg_ref, destination=object_label::microwave, relation=in)
  ACTION close(target=object_label::door)
  ACTION turn(direction="right")
  ACTION turn(direction="right")
  ACTION face(target=object_label::saltshaker)
  ACTION pick_up(target=food_label::egg, source=object_label::table) -> food_label_egg_ref_2 : REF[STRING]
  ACTION turn(direction="right")
  ACTION turn(direction="left")
  ACTION turn(direction="right")
  ACTION face(target=object_label::microwave)
  ACTION place(target=food_label_egg_ref_2, destination=object_label::microwave, relation=in)
  ACTION close(target=object_label::door)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | TASK | covered |
| n2 | action | place | covered |
| n3 | object | food_label::egg | label-preserved |
| n4 | constraint | place, pick_up | covered |
| n5 | object | object_label::microwave | covered |
| n6 | action | turn | covered |
| n7 | temporal | turn | covered |
| n8 | action | turn, face | covered |
| n9 | object | object_label::sink | covered |
| n10 | action | pick_up | covered |
| n11 | object | food_label::egg | label-preserved |
| n12 | object | object_label::sink | covered |
| n13 | action | turn, face | covered |
| n14 | object | object_label::microwave | covered |
| n15 | action | place | covered |
| n16 | object | food_label::egg | label-preserved |
| n17 | object | object_label::microwave | covered |
| n18 | action | close | covered |
| n19 | object | object_label::door | covered |
| n20 | action | turn, face | covered |
| n21 | object | object_label::saltshaker | covered |
| n22 | object | object_label::table | covered |
| n23 | action | pick_up | covered |
| n24 | object | food_label::egg | label-preserved |
| n25 | object | object_label::table | covered |
| n26 | action | turn, face | covered |
| n27 | object | object_label::microwave | covered |
| n28 | action | place | covered |
| n29 | object | food_label::egg | label-preserved |
| n30 | object | object_label::microwave | covered |
| n31 | action | close | covered |
| n32 | object | object_label::door | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s16 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "eggs" -> food_label::egg, "microwave" -> object_label::microwave; t2:s2 "sink" -> object_label::sink; t2:s4 "egg" -> food_label::egg, "sink" -> object_label::sink; t2:s6 "microwave" -> object_label::microwave; t2:s8 "egg" -> food_label::egg, "microwave" -> object_label::microwave, "door" -> object_label::door; t2:s10 "salt shaker" -> object_label::saltshaker, "table" -> object_label::table; t2:s12 "egg" -> food_label::egg, "table" -> object_label::table; t2:s14 "microwave" -> object_label::microwave; t2:s16 "egg" -> food_label::egg, "microwave" -> object_label::microwave, "door" -> object_label::door
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
