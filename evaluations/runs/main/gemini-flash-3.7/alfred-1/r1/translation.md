Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelKeys
TASK ObjectLabelKeys {
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::table)
  ACTION pick_up(target=object_label::keys, source=object_label::table) -> object_label_keys_ref : REF[STRING]
  ACTION turn(direction="around")
  ACTION walk(destination=living_room)
  ACTION walk(destination=object_label::ottoman)
  ACTION place(target=object_label_keys_ref, destination=object_label::ottoman, location=object_label::phone, relation=left_of)
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
| n16 | constraint | source | covered |
| n17 | action | turn | covered |
| n18 | action | walk | covered |
| n19 | object | living_room | covered |
| n20 | constraint | — | not-applicable |
| n21 | object | object_label::ottoman | label-preserved |
| n22 | action | place | covered |
| n23 | object | object_label::keys | label-preserved |
| n24 | constraint | left_of | covered |
| n25 | object | object_label::phone | label-preserved |
| n26 | constraint | destination | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1-t2:s8 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "keys" -> object_label::keys; t1:s1 "ottoman" -> object_label::ottoman; t2:s2 "end table" -> object_label::table; t2:s4 "keys" -> object_label::keys; t2:s4 "vase" -> object_label::vase; t2:s6 "ottoman" -> object_label::ottoman; t2:s8 "keys" -> object_label::keys; t2:s8 "cell phone" -> object_label::phone
- Missing constructs: none
- Unresolved ambiguities: none
- Justification for not-applicable needs: n6 (black), n8 (on the wall), n9 (across from couch), n10 (couch), n13 (behind vase), n14 (white), n15 (vase), n20 (purple) are natural language visual disambiguation cues in the trajectory instructions to identify interactable entities; the physical action signatures (turn, walk, pick_up, place) operate directly on the target entities and destinations without accepting ambient landmark modifiers.
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
