Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Textbook
TASK Textbook {
  ACTION turn(direction="around")
  ACTION walk(destination=living_room)
  ACTION walk(destination=trash_can, relation=in_front_of)
  ACTION turn(direction="right")
  ACTION walk(destination=desk)
  ACTION pick_up(target=textbook, source=mug) -> textbook_ref : REF[STRING]
  ACTION turn(direction="right")
  ACTION walk(destination=bed)
  ACTION place(target=textbook_ref, destination=bed, location=laptop, relation=in_front_of)
  ACTION turn(direction="around")
  ACTION walk(destination=desk)
  ACTION pick_up(target=textbook, source=lamp) -> textbook_ref_2 : REF[STRING]
  ACTION turn(direction="right")
  ACTION walk(destination=bed)
  ACTION place(target=textbook_ref_2, destination=bed, location=object_label::bear, relation=other_side_of)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | pick_up, place, walk | covered |
| n2 | action | pick_up, place, walk | covered |
| n3 | object | textbook | covered |
| n4 | constraint | pick_up | covered |
| n5 | object | desk | covered |
| n6 | object | bed | covered |
| n7 | action | turn | covered |
| n8 | action | walk, living_room | covered |
| n9 | object | living_room | covered |
| n10 | action | turn | covered |
| n11 | constraint | trash_can, in_front_of | covered |
| n12 | constraint | — | not-applicable |
| n13 | object | trash_can | covered |
| n14 | action | walk, desk | covered |
| n15 | object | desk | covered |
| n16 | action | pick_up, textbook | covered |
| n17 | object | textbook | covered |
| n18 | constraint | mug | covered |
| n19 | object | mug | covered |
| n20 | action | turn | covered |
| n21 | action | walk, bed | covered |
| n22 | object | bed | covered |
| n23 | action | place, bed, textbook | covered |
| n24 | object | textbook | covered |
| n25 | object | bed | covered |
| n26 | constraint | in_front_of | covered |
| n27 | object | laptop | covered |
| n28 | action | turn | covered |
| n29 | action | walk, desk | covered |
| n30 | object | desk | covered |
| n31 | action | pick_up, textbook | covered |
| n32 | object | textbook | covered |
| n33 | constraint | lamp | covered |
| n34 | object | lamp | covered |
| n35 | action | turn | covered |
| n36 | action | walk, bed | covered |
| n37 | object | bed | covered |
| n38 | action | place, bed, textbook | covered |
| n39 | object | textbook | covered |
| n40 | object | bed | covered |
| n41 | constraint | other_side_of | covered |
| n42 | object | object_label::bear | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: all segments t1:s1–t2:s16 are represented
- Opaque-text spans: none
- Label-preserved spans: t2:s16 "stuffed bear" -> object_label::bear (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
