Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Keys
TASK Keys {
  ACTION turn(direction="left")
  TERM lexical_label(value=color_label::black) -> lexical_label_2 : TERM
  TERM lexical_label(value=object_label::table) -> lexical_label_3 : TERM
  TERM lexical_label(value=object_label::wall) -> lexical_label_4 : TERM
  TERM spatial_constraint(object=lexical_label_3, reference=lexical_label_4, relation=on) -> spatial_constraint_2 : TERM
  TERM lexical_label(value=object_label::couch) -> lexical_label_5 : TERM
  TERM spatial_constraint(object=lexical_label_3, reference=lexical_label_5, relation=other_side_of) -> spatial_constraint_3 : TERM
  ACTION walk(destination=spatial_constraint_2)
  TERM lexical_label(value=color_label::white) -> lexical_label_6 : TERM
  TERM lexical_label(value=object_label::vase) -> lexical_label_7 : TERM
  TERM lexical_label(value=object_label::keys) -> lexical_label_8 : TERM
  TERM spatial_constraint(object=lexical_label_8, reference=lexical_label_7, relation=behind) -> spatial_constraint_4 : TERM
  ACTION pick_up(target=keys, source=table) -> keys_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=living_room)
  TERM lexical_label(value=color_label::purple) -> lexical_label_9 : TERM
  ACTION walk(destination=object_label::ottoman)
  ACTION place(target=keys_ref, destination=object_label::ottoman, location=phone, relation=left_of)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | place | covered |
| n2 | object | keys | covered |
| n3 | object | object_label::ottoman | label-preserved |
| n4 | action | turn | covered |
| n5 | action | walk | covered |
| n6 | constraint | color_label::black | label-preserved |
| n7 | object | table | covered |
| n8 | constraint | spatial_constraint, on | covered |
| n9 | constraint | other_side_of | covered |
| n10 | object | object_label::couch | label-preserved |
| n11 | action | pick_up | covered |
| n12 | object | keys | covered |
| n13 | constraint | spatial_constraint, behind | covered |
| n14 | constraint | color_label::white | label-preserved |
| n15 | object | vase | covered |
| n16 | constraint | table, on | covered |
| n17 | action | turn | covered |
| n18 | action | walk, living_room | covered |
| n19 | object | living_room | covered |
| n20 | constraint | color_label::purple | label-preserved |
| n21 | object | object_label::ottoman | label-preserved |
| n22 | action | place | covered |
| n23 | object | keys | covered |
| n24 | constraint | left_of, phone | covered |
| n25 | object | phone | covered |
| n26 | constraint | on, object_label::ottoman | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s8 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "ottoman" -> object_label::ottoman; t2:s2 "black" -> color_label::black; t2:s2 "couch" -> object_label::couch; t2:s4 "white" -> color_label::white; t2:s6 "purple" -> color_label::purple; t2:s6 "ottoman" -> object_label::ottoman; t2:s8 "ottoman" -> object_label::ottoman
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
