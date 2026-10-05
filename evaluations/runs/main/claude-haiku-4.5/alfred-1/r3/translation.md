Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER propose(target=activity(verb="place", object=keys, location=object_label::ottoman))
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    UTTER propose(target=activity(verb="turn", actor="you"))
    
    UTTER propose(target=activity(verb="walk", location=table))
    
    UTTER propose(target=activity(verb="pick_up", object=keys, source=table))
    
    UTTER propose(target=activity(verb="walk", location=living_room))
    
    UTTER propose(target=activity(verb="place", object=keys, location=object_label::ottoman))
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | propose(activity(verb="place")) | covered |
| n2 | object | keys | covered |
| n3 | object | object_label::ottoman | covered |
| n4 | action | propose(activity(verb="turn")) | covered |
| n5 | action | propose(activity(verb="walk", location=table)) | covered |
| n6 | constraint | — | label-preserved |
| n7 | object | table | covered |
| n8 | constraint | — | label-preserved |
| n9 | constraint | — | label-preserved |
| n10 | object | — | label-preserved |
| n11 | action | propose(activity(verb="pick_up")) | covered |
| n12 | object | keys | covered |
| n13 | constraint | — | label-preserved |
| n14 | constraint | — | label-preserved |
| n15 | object | — | label-preserved |
| n16 | constraint | — | label-preserved |
| n17 | action | propose(activity(verb="turn")) | covered |
| n18 | action | propose(activity(verb="walk", location=living_room)) | covered |
| n19 | object | living_room | covered |
| n20 | constraint | — | label-preserved |
| n21 | object | object_label::ottoman | covered |
| n22 | action | propose(activity(verb="place")) | covered |
| n23 | object | keys | covered |
| n24 | constraint | — | label-preserved |
| n25 | object | — | label-preserved |
| n26 | constraint | — | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all segments t1:s1, t2:s2, t2:s4, t2:s6, t2:s8 are semantically covered with main actions and locations
- Opaque-text spans: none
- Label-preserved spans:
  - t2:s2 "black end table on the wall, across from the couch" → n6 (black color), n8 (wall location), n9 (across from couch): color, wall location, and spatial relation relative to couch are descriptors from the source preserved as labels
  - t2:s4 "behind the white vase, on the black end table" → n13 (behind vase), n14 (white color), n16 (on table): spatial relation and color are preserved; pick_up action is encoded
  - t2:s6 "purple ottoman" → n20 (purple color): color descriptor is a source label
  - t2:s8 "left side of the cell phone, on the ottoman" → n24 (left of phone), n25 (phone object), n26 (on ottoman): spatial relations and phone object are preserved as labels; place action is encoded
- Missing constructs: The activity() constructor does not have parameters for spatial relations (behind, left_of, on) or object properties (color). These constraints cannot be expressed as structured arguments in UTTER propose(target=activity(...)); they are preserved as source labels in the coverage report.
- Unresolved ambiguities: none
- Validation: rag check passes with all symbols from the glossary. Label-preserved spans use open-group values (object_label) or source descriptors that cannot be encoded with the available constructors.

