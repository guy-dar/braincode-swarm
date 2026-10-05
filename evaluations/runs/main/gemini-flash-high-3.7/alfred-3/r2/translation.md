Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Pan
TASK Pan {
  TERM lexical_label(value=color_label::black) -> lexical_label_2 : TERM
  ACTION walk(destination=object_label::table)
  ACTION turn(direction="left")
  ACTION pick_up(target=object_label::knife, source=object_label::table) -> object_label_knife_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::stove, relation=left_of)
  ACTION place(target=object_label_knife_ref, destination=object_label::pan, location=object_label::burner, relation=in)
  ACTION pick_up(target=object_label::pan, source=object_label::stove) -> object_label_pan_ref : REF[STRING]
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::safe)
  ACTION turn(direction="left")
  ACTION face(target=object_label::table)
  ACTION place(target=object_label_pan_ref, destination=object_label::table, location=object_label::lettuce, relation=on)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | place | covered |
| n2 | action | place | covered |
| n3 | object | object_label::pan | label-preserved |
| n4 | object | object_label::knife | label-preserved |
| n5 | object | object_label::table | label-preserved |
| n6 | constraint | place, in | covered |
| n7 | action | walk | covered |
| n8 | temporal | walk, turn | covered |
| n9 | action | turn | covered |
| n10 | object | object_label::table | label-preserved |
| n11 | constraint | color_label::black, lexical_label | label-preserved |
| n12 | action | pick_up | covered |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | object_label::lettuce | label-preserved |
| n15 | constraint | object_label::lettuce | covered |
| n16 | constraint | pick_up | covered |
| n17 | action | turn | covered |
| n18 | action | walk | covered |
| n19 | object | object_label::stove | label-preserved |
| n20 | constraint | left_of, walk | covered |
| n21 | action | place | covered |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | object_label::pan | label-preserved |
| n24 | object | object_label::burner | label-preserved |
| n25 | constraint | in, object_label::burner | covered |
| n26 | action | pick_up | covered |
| n27 | object | object_label::pan | label-preserved |
| n28 | object | object_label::stove | label-preserved |
| n29 | action | turn | covered |
| n30 | action | walk | covered |
| n31 | object | object_label::safe | label-preserved |
| n32 | action | turn, face | covered |
| n33 | object | object_label::table | label-preserved |
| n34 | action | place | covered |
| n35 | object | object_label::pan | label-preserved |
| n36 | object | object_label::table | label-preserved |
| n37 | object | object_label::lettuce | label-preserved |
| n38 | constraint | place, on | covered |
| n39 | constraint | on, object_label::lettuce | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s14 is represented
- Opaque-text spans: none
- Label-preserved spans: color_label::black, object_label::pan, object_label::knife, object_label::table, object_label::stove, object_label::burner, object_label::safe, object_label::lettuce
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
