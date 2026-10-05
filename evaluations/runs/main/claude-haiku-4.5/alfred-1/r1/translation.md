Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="place", object=object_label::keys, location=object_label::ottoman) -> place_keys_ottoman : TERM
    UTTER propose(target=place_keys_ottoman)
  }
  
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    UTTER propose(target=activity(verb="turn"), content="to your left")
    
    UTTER propose(target=activity(verb="walk", location=object_label::table), content="to the black end table on the wall, across from the couch")
    
    UTTER propose(target=activity(verb="pick_up", object=object_label::keys), content="that are behind the white vase, on the black end table")
    
    UTTER propose(target=activity(verb="turn"), content="around")
    
    UTTER propose(target=activity(verb="walk", location=object_label::ottoman), content="through the living room, to the purple ottoman")
    
    UTTER propose(target=activity(verb="place", object=object_label::keys, location=object_label::ottoman), content="on the left side of the cell phone, on the ottoman")
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity(verb="place") | covered |
| n2 | object | object_label::keys | covered |
| n3 | object | object_label::ottoman | covered |
| n4 | action | activity(verb="turn") with content | opaque |
| n5 | action | activity(verb="walk") with content | opaque |
| n6 | constraint | color (in content string) | opaque |
| n7 | object | object_label::table | covered |
| n8 | constraint | location on wall (in content string) | opaque |
| n9 | constraint | spatial relation (in content string) | opaque |
| n10 | object | not covered; couch ≠ glossary symbols | unresolved |
| n11 | action | activity(verb="pick_up") | covered |
| n12 | object | object_label::keys | covered |
| n13 | constraint | spatial relation (in content string) | opaque |
| n14 | constraint | color (in content string) | opaque |
| n15 | object | object_label::vase | covered |
| n16 | constraint | color + location (in content string) | opaque |
| n17 | action | activity(verb="turn") with content | opaque |
| n18 | action | activity(verb="walk") with content | opaque |
| n19 | object | not covered; living_room ≠ glossary symbols | unresolved |
| n20 | constraint | color (in content string) | opaque |
| n21 | object | object_label::ottoman | covered |
| n22 | action | activity(verb="place") | covered |
| n23 | object | object_label::keys | covered |
| n24 | constraint | spatial relation (in content string) | opaque |
| n25 | object | object_label::phone | covered |
| n26 | constraint | location (in content string) | opaque |

## Why the translation failed

The glossary is missing constructors and values needed to express spatial constraints, color properties, and some object types:

**Missing object types (n10, n19):**
- **n10 "couch":** Not in object_label group; nearest glossary candidate is chair (furniture seating). But couch is semantically distinct (larger, for multiple people). 
  - Searches tried: `rag search "couch sofa seating"` → only found chair
  - Proposed: S1 (add couch or sofa to object_label, or add couch as a registered object type)

- **n19 "living room":** Listed as location-name value living_room in retrieval, but when used in activity(verb="walk", location=object_label::ottoman) with content referencing living_room, it's not formally integrated.
  - Searches tried: `rag entry living_room` → exists as location-name value, but activity(location=STRING/ATOM[country]) doesn't accept location-name values
  - Proposed: S2 (add location-name values like living_room to activity.location signature, or create location_descriptor constructor)

**Missing constructors for spatial and color properties (n4, n6, n8, n9, n13, n14, n16, n17, n20, n24, n26):**

- **Direction qualifiers (n4, n17):** "Turn left" and "turn around" require direction info, but activity(verb="turn") has no direction parameter.
  - Proposed: S3 (add direction parameter to activity, or define activity-verb expansions like turn_left, turn_around)

- **Color properties on objects (n6, n14, n20):** Cannot express "black end table", "white vase", "purple ottoman". The activity() constructor has no color field.
  - The pick_up operation has a color parameter for selecting targets, but that's for operational filtering, not for describing already-identified objects in TRACE
  - Proposed: S4 (colored_object(object: ATOM[object_label], color: ATOM[color_label]) constructor)

- **Spatial relationships (n8, n9, n13, n16, n24, n26):** Cannot express "on wall", "behind vase", "across from couch", "left side of phone". The activity() location only accepts STRING or ATOM[country].
  - The place operation has a relation parameter for spatial relations, but only for ACTION in REQUEST mode
  - Proposed: S5 (spatial_object(object: ATOM[object_label], relation: STRING, reference: ATOM[object_label]) constructor to describe object positioning relative to another object)

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: All turns and sentences are represented (t1:s1–t2:s8). Core actions (place, turn, walk, pick_up) and primary objects (keys, ottoman, table, phone, vase) are covered. Secondary objects (couch, living_room) and all spatial/color constraints are opaque or unresolved.
- Opaque-text spans (content strings holding spatial/color details that cannot be structured with current glossary):
  - t2:s2 content="to your left" (direction qualifier not expressible via activity verb)
  - t2:s2 content="to the black end table on the wall, across from the couch" (color + spatial constraints + unmapped object type)
  - t2:s4 content="that are behind the white vase, on the black end table" (spatial + color constraints)
  - t2:s6 content="through the living room, to the purple ottoman" (location-name value + color constraint)
  - t2:s6 content="around" (direction qualifier)
  - t2:s8 content="on the left side of the cell phone, on the ottoman" (spatial constraints)
- Unresolved needs (no symbol/opaque fallback):
  - n10 "couch" — glossary offers only "chair"; couch is semantically distinct
  - n19 "living_room" — exists as location-name value but activity() constructor doesn't accept location-name ATOM values
- Missing constructs:
  - S1: object type for couch/sofa
  - S2: way to reference location-name values in activity descriptions (or add living_room to activity.location signature)
  - S3: direction parameter for activity(verb="turn") or turn_left/turn_around activity-verb variants
  - S4: colored_object(object, color) constructor
  - S5: spatial_object(object, relation, reference) constructor
- Unresolved ambiguities: none
- Check: `rag check` reported these needs as needing structures that don't exist
```

## Proposed glossary additions

(See `/output/suggestions.md` for full details of S1, S2, S3)
