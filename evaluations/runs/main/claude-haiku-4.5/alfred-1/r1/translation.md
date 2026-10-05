Status: failed
Mode: TRACE

## Suggested translation

This document presents the best translation possible with the current glossary. Needs marked `PROPOSED: S<k>` would become covered once suggestions S1-S4 are accepted.

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="place", object="keys", location="ottoman") -> place_activity : TERM  # PROPOSED: S3
    UTTER propose(target=place_activity)
  }
  
  TURN t2 SPEAKER=AGENT {
    TERM activity(verb="turn") -> turn_1 : TERM
    TERM activity(verb="go", location=table) -> go_1 : TERM
    UTTER propose(target=turn_1)
    UTTER propose(target=go_1)
    
    TERM activity(verb="pick_up", object="keys") -> pick_up_2 : TERM
    UTTER propose(target=pick_up_2)
    
    TERM activity(verb="turn") -> turn_3 : TERM
    TERM activity(verb="go", location="ottoman") -> go_3 : TERM  # PROPOSED: S3
    UTTER propose(target=turn_3)
    UTTER propose(target=go_3)
    
    TERM activity(verb="place", object="keys", location="ottoman") -> place_4 : TERM  # PROPOSED: S3
    UTTER propose(target=place_4)
  }
}
```

## Why the translation failed

**Spatial relationship constraints (n8, n9, n13, n24, n26):** The item specifies objects by their positions (keys behind vase, ottoman across from couch, end table on wall, keys on left of cell phone). The spatial-relation values (behind, left_of, on, other_side_of, across_from) exist in the glossary but only as operation parameters for place.relation and walk.relation. There is no TERM constructor to express positional relationships descriptively. Solution: S1 (spatial_relation constructor).

**Object property/descriptor constraints (n6, n14, n20):** The item uses color to disambiguate objects (black end table, white vase, purple ottoman). The color_label group values exist, but the activity TERM constructor has no color parameter. No general property descriptor constructor exists. Solution: S2 (object_descriptor constructor).

**Missing furniture entities (n10, n15, n3, n21):** Ottoman and couch are common household objects referenced in the item. Chair explicitly excludes ottoman/sofa. Ottoman and couch are not in the entity-name values. Solution: S3 (add ottoman), S4 (add couch).

**Missing entity for cell phone (n25):** Cell phone appears as a spatial reference. The phone entity-name value exists but was not used because it was embedded in an unresolvable constraint. Once S2 enables property descriptor, phone can be properly used.

Searches attempted for each:
- Spatial relations: searched "behind the vase", "across from the couch", "on the wall" → found spatial-relation values but no TERM constructor
- Colors: searched "black end table", "purple ottoman", "color property" → found color_label values but no TERM parameter to use them
- Furniture: searched "ottoman", "couch" → returned unrelated candidates (food, countries); confirmed via glossary scan they are absent

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity(verb="place") in propose | covered |
| n2 | object | object="keys" in activity | covered |
| n3 | object | location="ottoman" (string, PROPOSED: S3) | proposed |
| n4 | action | activity(verb="turn") in propose | covered |
| n5 | action | activity(verb="go", location=table) in propose | covered |
| n6 | constraint | color_label::black (PROPOSED: S2) | proposed |
| n7 | object | location=table | covered |
| n8 | constraint | spatial_relation(...) (PROPOSED: S1) | proposed |
| n9 | constraint | spatial_relation(...) (PROPOSED: S1) | proposed |
| n10 | object | object_label::couch (PROPOSED: S4) | proposed |
| n11 | action | activity(verb="pick_up") in propose | covered |
| n12 | object | object="keys" in activity | covered |
| n13 | constraint | spatial_relation(...) (PROPOSED: S1) | proposed |
| n14 | constraint | color_label::white (PROPOSED: S2) | proposed |
| n15 | object | object_label::vase (PROPOSED: S2 for properties) | proposed |
| n16 | constraint | spatial_relation(..., object_descriptor(...)) (PROPOSED: S1, S2) | proposed |
| n17 | action | activity(verb="turn") in propose | covered |
| n18 | action | activity(verb="go", location="ottoman") in propose | covered |
| n19 | object | living_room (exists, implicit reference) | covered |
| n20 | constraint | color_label::purple (PROPOSED: S2) | proposed |
| n21 | object | location="ottoman" (string, PROPOSED: S3) | proposed |
| n22 | action | activity(verb="place", object="keys") in propose | covered |
| n23 | object | object="keys" in activity | covered |
| n24 | constraint | spatial_relation(...) (PROPOSED: S1) | proposed |
| n25 | object | object_label::phone (PROPOSED: S2 for constraints) | proposed |
| n26 | constraint | spatial_relation(...) (PROPOSED: S1) | proposed |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: main actions (place, pick_up, turn, go) represented via activity TERMs in t1:s1 and t2:s2,s4,s6,s8; spatial relations and object descriptors in t2:s2,s4,s6,s8 not fully representable
- Opaque-text spans: none
- Label-preserved spans: n3, n21 ("ottoman" as string, not in glossary as location-name or entity-name)
- Missing constructs: constructor for spatial relationships (behind, left_of, across_from, etc. exist as glossary spatial-relation values used in operation signatures, but no TERM constructor to describe positioned objects); constructor for object properties/descriptors (color, size; color_label::* values exist but activity TERM has no color parameter); constructor for location constraints
- Unresolved ambiguities: none
- Proposed glossary changes required for coverage: S1 (spatial_relation constructor), S2 (object_descriptor constructor), S3 (ottoman entity), S4 (couch entity)
