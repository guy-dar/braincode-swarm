Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    ACTION pick_up(target=food_label::egg, quantity=2) -> food_label_egg_refs : LIST[REF[STRING]]
    FOR EACH item IN food_label_egg_refs {
      ACTION place(target=item, destination=object_label::microwave)
    }
  }
  TURN t2 SPEAKER=AGENT {
    ACTION turn(direction="right")
    ACTION turn(direction="left")
    ACTION face(target=object_label::sink)
    ACTION pick_up(target=food_label::egg, source=object_label::sink) -> food_label_egg_ref : REF[STRING]
    ACTION turn(direction="right")
    ACTION face(target=object_label::microwave)
    ACTION place(target=food_label_egg_ref, destination=object_label::microwave)
    ACTION close(target=object_label::door)
    ACTION turn(direction="right")
    ACTION turn(direction="right")
    ACTION face(target=object_label::saltshaker)
    ACTION pick_up(target=food_label::egg, source=object_label::table) -> food_label_egg_ref_2 : REF[STRING]
    ACTION turn(direction="right")
    ACTION turn(direction="left")
    ACTION turn(direction="right")
    ACTION face(target=object_label::microwave)
    ACTION place(target=food_label_egg_ref_2, destination=object_label::microwave)
    ACTION close(target=object_label::door)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | pick_up, place | covered |
| n2 | action | place | covered |
| n3 | object | food_label::egg | label-preserved |
| n4 | constraint | quantity | covered |
| n5 | object | object_label::microwave | label-preserved |
| n6 | action | turn | covered |
| n7 | temporal | turn | covered |
| n8 | action | face, turn | covered |
| n9 | object | object_label::sink | label-preserved |
| n10 | action | pick_up | covered |
| n11 | object | food_label::egg | label-preserved |
| n12 | object | object_label::sink | label-preserved |
| n13 | action | face, turn | covered |
| n14 | object | object_label::microwave | label-preserved |
| n15 | action | place | covered |
| n16 | object | food_label::egg | label-preserved |
| n17 | object | object_label::microwave | label-preserved |
| n18 | action | close | covered |
| n19 | object | object_label::door | label-preserved |
| n20 | action | face, turn | covered |
| n21 | object | object_label::saltshaker | label-preserved |
| n22 | object | object_label::table | label-preserved |
| n23 | action | pick_up | covered |
| n24 | object | food_label::egg | label-preserved |
| n25 | object | object_label::table | label-preserved |
| n26 | action | face, turn | covered |
| n27 | object | object_label::microwave | label-preserved |
| n28 | action | place | covered |
| n29 | object | food_label::egg | label-preserved |
| n30 | object | object_label::microwave | label-preserved |
| n31 | action | close | covered |
| n32 | object | object_label::door | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s16 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "egg" → food_label::egg, t1:s1 "microwave" → object_label::microwave, t2:s2 "sink" → object_label::sink, t2:s8 "door" → object_label::door, t2:s10 "salt shaker" → object_label::saltshaker, t2:s10 "table" → object_label::table
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
