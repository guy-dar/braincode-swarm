Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # USER requests to put the keys on the ottoman
    # (Implied instruction encoded by ACTIONs below)
  }
  TURN t2 SPEAKER=AGENT {
    ACTION turn(direction="left")
    ACTION walk(destination=object_label::table)  # walks to end table (color and location constraints currently unencoded)
    ACTION pick_up(target=object_label::keys, source=object_label::table) -> keys_ref : REF[STRING]
    ACTION turn(direction="around")
    ACTION walk(destination=object_label::ottoman)
    ACTION place(target=keys_ref, destination=object_label::ottoman)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | turn, walk, pick_up, place | covered |
| n2 | object | object_label::keys | covered |
| n3 | object | object_label::ottoman | covered |
| n4 | action | turn(direction="left") | covered |
| n5 | action | walk(destination=object_label::table) | covered |
| n6 | constraint | color_label::black | unresolved |
| n7 | object | object_label::table | covered |
| n8 | constraint | on (wall) | unresolved |
| n9 | constraint | across_from | unresolved |
| n10 | object | object_label::couch | covered |
| n11 | action | pick_up | covered |
| n12 | object | object_label::keys | covered |
| n13 | constraint | behind | unresolved |
| n14 | constraint | color_label::white | unresolved |
| n15 | object | object_label::vase | covered |
| n16 | constraint | on (object_label::table) | unresolved |
| n17 | action | turn(direction="around") | covered |
| n18 | action | walk(destination=object_label::ottoman) | covered |
| n19 | object | object_label::living_room | unresolved |
| n20 | constraint | color_label::purple | unresolved |
| n21 | object | object_label::ottoman | covered |
| n22 | action | place | covered |
| n23 | object | object_label::keys | covered |
| n24 | constraint | on (left_of cellphone) | unresolved |
| n25 | object | object_label::phone | covered |
| n26 | constraint | on (object_label::ottoman) | covered |

## Why the translation failed

Several spatial and color constraints describe composite object references (e.g., “the black end table on the wall, across from the couch” or “behind the white vase”) that cannot be expressed with the current glossary. There is no constructor or composite to combine an object label with color and spatial-location qualifiers.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all sentences mapped to ACTIONs, but color and spatial qualifiers omitted
- Opaque-text spans: none
- Label-preserved spans: n7 ("end table" → object_label::table), n15 ("vase" → object_label::vase), n25 ("cell phone" → object_label::phone)
- Missing constructs: constructors or composites for enriched object descriptions with color and location
- Unresolved ambiguities: none beyond missing capabilities
- Check: `rag check` reported unresolved needs: color and spatial qualifiers (n6, n8, n9, n13, n14, n16, n19, n20, n24)