Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Keys
TASK Keys {
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::table)
  ACTION pick_up(target=object_label::keys, source=object_label::table) -> keys_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=object_label::ottoman)
  ACTION place(target=keys_ref, destination=object_label::ottoman, location=object_label::phone, relation=left_of)
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
| n6 | constraint | — | not-applicable |
| n7 | object | object_label::table | label-preserved |
| n8 | constraint | — | not-applicable |
| n9 | constraint | — | not-applicable |
| n10 | object | — | not-applicable |
| n11 | action | pick_up | covered |
| n12 | object | object_label::keys | label-preserved |
| n13 | constraint | — | not-applicable |
| n14 | constraint | — | not-applicable |
| n15 | object | — | not-applicable |
| n16 | constraint | source=object_label::table | covered |
| n17 | action | turn | covered |
| n18 | action | walk | covered |
| n19 | object | — | not-applicable |
| n20 | constraint | — | not-applicable |
| n21 | object | object_label::ottoman | label-preserved |
| n22 | action | place | covered |
| n23 | object | object_label::keys | label-preserved |
| n24 | constraint | left_of | covered |
| n25 | object | object_label::phone | label-preserved |
| n26 | constraint | destination=object_label::ottoman | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s8 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "ottoman" → object_label::ottoman (n3); t2:s2 "couch" → object_label::couch (n10); t2:s4 "vase" → object_label::vase (n15); t1:s1 "keys" → object_label::keys (n2); t2:s2 "table" → object_label::table (n7); t2:s4 "keys" → object_label::keys (n12); t2:s6 "ottoman" → object_label::ottoman (n21); t2:s8 "keys" → object_label::keys (n23); t2:s8 "cell phone" → object_label::phone (n25)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
