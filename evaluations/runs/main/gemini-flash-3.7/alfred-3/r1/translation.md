Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelTable
TASK ObjectLabelTable {
  ACTION walk(destination=object_label::table)
  ACTION turn(direction="left")
  ACTION face(target=object_label::table)
  TERM lexical_label(value=color_label::black) -> lexical_label_2 : TERM
  TERM lexical_label(value=food_label::lettuce) -> lexical_label_3 : TERM
  TERM spatial_constraint(object=lexical_label_2, reference=lexical_label_3, relation=next_to) -> spatial_constraint_2 : TERM
  ACTION pick_up(target=object_label::knife, source=object_label::table) -> object_label_knife_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::stove, relation=left_of)
  ACTION place(target=object_label_knife_ref, destination=object_label::pan, location=object_label::burner, relation=in)
  ACTION pick_up(target=object_label::pan, source=object_label::stove) -> object_label_pan_ref : REF[STRING]
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::safe)
  ACTION turn(direction="left")
  ACTION face(target=object_label::table)
  ACTION place(target=object_label_pan_ref, destination=object_label::table, relation=on)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | place, pick_up | covered |
| n2 | action | place | covered |
| n3 | object | object_label::pan | label-preserved |
| n4 | object | object_label::knife | label-preserved |
| n5 | object | object_label::table | label-preserved |
| n6 | constraint | relation=in | covered |
| n7 | action | walk | covered |
| n8 | temporal | sequential execution | covered |
| n9 | action | turn, face | covered |
| n10 | object | object_label::table | label-preserved |
| n11 | constraint | color_label::black | label-preserved |
| n12 | action | pick_up | covered |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | food_label::lettuce | label-preserved |
| n15 | constraint | spatial_constraint, next_to | covered |
| n16 | constraint | pick_up, next_to | covered |
| n17 | action | turn | covered |
| n18 | action | walk | covered |
| n19 | object | object_label::stove | label-preserved |
| n20 | constraint | relation=left_of | covered |
| n21 | action | place | covered |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | object_label::pan | label-preserved |
| n24 | object | object_label::burner | label-preserved |
| n25 | constraint | relation=in, relation=left_of | covered |
| n26 | action | pick_up | covered |
| n27 | object | object_label::pan | label-preserved |
| n28 | object | object_label::stove | label-preserved |
| n29 | action | turn | covered |
| n30 | action | walk | covered |
| n31 | object | object_label::safe | label-preserved |
| n32 | action | turn, face | covered |
| n33 | object | object_label::table, color_label::black | label-preserved |
| n34 | action | place | covered |
| n35 | object | object_label::pan | label-preserved |
| n36 | object | object_label::table | label-preserved |
| n37 | object | food_label::lettuce | label-preserved |
| n38 | constraint | relation=left_of | covered |
| n39 | constraint | relation=on | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s14 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "pan" → object_label::pan, "knife" → object_label::knife, "table" → object_label::table; t2:s2 "table" → object_label::table, "black" → color_label::black; t2:s4 "knife" → object_label::knife, "lettuce" → food_label::lettuce; t2:s6 "stove top" → object_label::stove; t2:s8 "knife" → object_label::knife, "pan" → object_label::pan, "burner" → object_label::burner; t2:s10 "pan" → object_label::pan, "stove top" → object_label::stove; t2:s12 "safe" → object_label::safe, "table" → object_label::table; t2:s14 "pan" → object_label::pan, "table" → object_label::table, "lettuce" → food_label::lettuce
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
