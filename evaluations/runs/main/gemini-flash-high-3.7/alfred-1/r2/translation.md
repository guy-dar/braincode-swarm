Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelKeys
TASK ObjectLabelKeys {
  ACTION turn(direction="left")
  TERM lexical_label(value=color_label::black) -> lexical_label_2 : TERM
  TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
  TERM lexical_label(value=object_label::table) -> lexical_label_3 : TERM
  TERM lexical_label(value=object_label::couch) -> lexical_label_4 : TERM
  TERM spatial_constraint(object=lexical_label_3, reference=lexical_label_4, relation=other_side_of) -> spatial_constraint_2 : TERM
  TERM lexical_label(value=object_label::wall) -> lexical_label_5 : TERM
  TERM spatial_constraint(object=lexical_label_3, reference=lexical_label_5, relation=on) -> spatial_constraint_3 : TERM
  ACTION walk(destination=spatial_constraint_2)
  TERM lexical_label(value=color_label::white) -> lexical_label_6 : TERM
  TERM requirement(property="color", value=lexical_label_6) -> requirement_3 : TERM
  TERM lexical_label(value=object_label::vase) -> lexical_label_7 : TERM
  TERM lexical_label(value=object_label::keys) -> lexical_label_8 : TERM
  TERM spatial_constraint(object=lexical_label_8, reference=lexical_label_7, relation=behind) -> spatial_constraint_4 : TERM
  TERM spatial_constraint(object=lexical_label_8, reference=lexical_label_3, relation=on) -> spatial_constraint_5 : TERM
  ACTION pick_up(target=object_label::keys, source=object_label::table) -> object_label_keys_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=living_room)
  TERM lexical_label(value=color_label::purple) -> lexical_label_9 : TERM
  TERM requirement(property="color", value=lexical_label_9) -> requirement_4 : TERM
  TERM lexical_label(value=object_label::ottoman) -> lexical_label_10 : TERM
  ACTION walk(destination=object_label::ottoman)
  ACTION place(target=object_label_keys_ref, destination=object_label::ottoman, location=phone, relation=left_of)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | place | covered |
| n2 | object | object_label::keys | label-preserved |
| n3 | object | object_label::ottoman | label-preserved |
| n4 | action | turn | covered |
| n5 | action | walk | covered |
| n6 | constraint | color_label::black, requirement | label-preserved |
| n7 | object | object_label::table | label-preserved |
| n8 | constraint | on, spatial_constraint | covered |
| n9 | constraint | other_side_of, spatial_constraint | covered |
| n10 | object | object_label::couch | label-preserved |
| n11 | action | pick_up | covered |
| n12 | object | object_label::keys | label-preserved |
| n13 | constraint | behind, spatial_constraint | covered |
| n14 | constraint | color_label::white, requirement | label-preserved |
| n15 | object | object_label::vase | label-preserved |
| n16 | constraint | on, spatial_constraint | covered |
| n17 | action | turn | covered |
| n18 | action | walk | covered |
| n19 | object | living_room | covered |
| n20 | constraint | color_label::purple, requirement | label-preserved |
| n21 | object | object_label::ottoman | label-preserved |
| n22 | action | place | covered |
| n23 | object | object_label::keys | label-preserved |
| n24 | constraint | left_of | covered |
| n25 | object | phone | covered |
| n26 | constraint | on, place | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s8 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "keys" -> object_label::keys, t1:s1 "ottoman" -> object_label::ottoman, t2:s2 "black" -> color_label::black, t2:s2 "end table" -> object_label::table, t2:s2 "couch" -> object_label::couch, t2:s4 "keys" -> object_label::keys, t2:s4 "white" -> color_label::white, t2:s4 "vase" -> object_label::vase, t2:s6 "purple" -> color_label::purple, t2:s6 "ottoman" -> object_label::ottoman, t2:s8 "keys" -> object_label::keys
- Missing constructs: none
- Unresolved ambiguities: none
- Check: rag check reported 0 unresolved needs and 0 unknown symbols
