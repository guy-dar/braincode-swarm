Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Knife
TASK Knife {
  ACTION walk(destination=object_label::table)
  ACTION turn(direction="left")
  ACTION pick_up(target=object_label::knife, source=object_label::table) -> knife_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::stove)
  ACTION place(target=knife_ref, destination=object_label::pan, location=object_label::burner, relation=in)
  ACTION pick_up(target=object_label::pan, source=object_label::stove) -> pan_ref : REF[STRING]
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::safe)
  ACTION turn(direction="left")
  ACTION face(target=object_label::table)
  ACTION place(target=pan_ref, destination=object_label::table, relation=on)
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
| n8 | temporal | sequential execution order | not-applicable |
| n9 | action | turn | covered |
| n10 | object | object_label::table | label-preserved |
| n11 | constraint | visual modifier not accepted by walk | not-applicable |
| n12 | action | pick_up | covered |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | scene landmark not in target signature | not-applicable |
| n15 | constraint | scene landmark not in pick_up signature | not-applicable |
| n16 | constraint | scene landmark not in pick_up signature | not-applicable |
| n17 | action | turn | covered |
| n18 | action | walk | covered |
| n19 | object | object_label::stove | label-preserved |
| n20 | constraint | turn, walk | covered |
| n21 | action | place | covered |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | object_label::pan | label-preserved |
| n24 | object | object_label::burner | label-preserved |
| n25 | constraint | location=object_label::burner | covered |
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
| n37 | object | scene landmark not in place signature | not-applicable |
| n38 | constraint | destination=object_label::table | covered |
| n39 | constraint | relation=on | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s14 is represented in the sequential action steps of Task Knife.
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "pan" -> object_label::pan; t1:s1 "knife" -> object_label::knife; t1:s1 "table" -> object_label::table; t2:s6 "stove" -> object_label::stove; t2:s8 "burner" -> object_label::burner; t2:s12 "safe" -> object_label::safe
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols; all open-group labels and declared not-applicable items are documented.
