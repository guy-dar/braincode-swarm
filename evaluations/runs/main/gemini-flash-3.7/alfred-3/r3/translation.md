Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    ACTION pick_up(target=knife) -> knife_ref : REF[STRING]
    ACTION place(target=knife_ref, destination=pan, relation=in)
    ACTION pick_up(target=pan) -> pan_ref : REF[STRING]
    ACTION place(target=pan_ref, destination=table, relation=on)
  }
  TURN t2 SPEAKER=AGENT {
    ACTION walk(destination=table)
    ACTION turn(direction="left")
    ACTION pick_up(target=knife, color=color_label::black, source=lettuce) -> knife_ref_2 : REF[STRING]
    ACTION turn(direction="around")
    ACTION walk(destination=stove, relation=left_of)
    ACTION place(target=knife_ref_2, destination=pan, location=object_label::burner, relation=in)
    ACTION pick_up(target=pan, source=stove) -> pan_ref_2 : REF[STRING]
    ACTION turn(direction="left")
    ACTION walk(destination=safe)
    ACTION turn(direction="left")
    ACTION face(target=table)
    ACTION place(target=pan_ref_2, destination=table, location=lettuce, relation=on)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | place | covered |
| n2 | action | place | covered |
| n3 | object | pan | covered |
| n4 | object | knife | covered |
| n5 | object | table | covered |
| n6 | constraint | place, in | covered |
| n7 | action | walk | covered |
| n8 | temporal | walk, turn | covered |
| n9 | action | turn | covered |
| n10 | object | table | covered |
| n11 | constraint | color_label::black | label-preserved |
| n12 | action | pick_up | covered |
| n13 | object | knife | covered |
| n14 | object | lettuce | covered |
| n15 | constraint | pick_up, lettuce | covered |
| n16 | constraint | pick_up | covered |
| n17 | action | turn | covered |
| n18 | action | walk, stove | covered |
| n19 | object | stove | covered |
| n20 | constraint | left_of | covered |
| n21 | action | place | covered |
| n22 | object | knife | covered |
| n23 | object | pan | covered |
| n24 | object | object_label::burner | label-preserved |
| n25 | constraint | in, object_label::burner | covered |
| n26 | action | pick_up | covered |
| n27 | object | pan | covered |
| n28 | object | stove | covered |
| n29 | action | turn | covered |
| n30 | action | walk, safe | covered |
| n31 | object | safe | covered |
| n32 | action | face, table | covered |
| n33 | object | table | covered |
| n34 | action | place | covered |
| n35 | object | pan | covered |
| n36 | object | table | covered |
| n37 | object | lettuce | covered |
| n38 | constraint | on | covered |
| n39 | constraint | on, lettuce | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s14 is represented
- Opaque-text spans: none
- Label-preserved spans: color_label::black (t2:s2), object_label::burner (t2:s8)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
