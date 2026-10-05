# Suggestions from translator alfred-1-r1

### S1 | type: add | dimension: vocabulary-member | symbol: couch

- Needs: n10 (t2:s2)
- Searches tried: `rag search "couch sofa seating"` → chair (incorrect; chair is individual seat, couch is larger multiperson furniture); `rag entry chair` → distinct category
- Meaning: A couch, sofa, or loveseat; a furniture piece used for sitting or reclining, typically larger than a single chair and accommodating multiple people
- Category: entity-name
- Contextual aliases: sofa, settee, loveseat, divan
- Example: "across from the couch" in a room description; in UTTER propose activity to move objects in relation to a couch
- Contrast: `chair` (single-person seating with backrest); `bed` (sleeping surface, not seating); `mattress` (sleeping cushion, not furniture frame)
- Proposed record: `{"symbol": "couch", "kind": "value", "category": "entity-name", "definition": "A sofa, couch, or loveseat furniture piece used for sitting or reclining; larger and typically for multiple people, distinct from a single-person chair.", "not": "chair (single-person seating) or bed (sleeping furniture)", "aliases": ["sofa", "settee", "loveseat"]}`

### S2 | type: refine | dimension: refine-entry | target: v19/constructor/activity

- Needs: n19 (t2:s6), n5 (t2:s2), n18 (t2:s6)
- Searches tried: `rag entry activity` → location parameter is `STRING / ATOM[country]`, does not accept location-name values; `rag search "living room location activity"` → no constructor accepts location-name values in TRACE mode
- Before: `activity(..., location?: STRING / ATOM[country], ...)` — location parameter only accepts free strings or country atoms
- After: Extend location parameter to accept ATOM[location-name] in addition to STRING / ATOM[country], or create a separate location_descriptor constructor
- Justification: In TRACE mode, when describing navigation activities like "go to the living room" or "walk to the corner", the destination may be a location-name value (living_room, corner, wall) rather than a country or free string. The current signature forces these to be encoded as opaque content strings.
- Option A (signature refinement): Change activity.location to `location?: STRING / ATOM[country] / ATOM[location_name]`
- Option B (new constructor): Create `location_descriptor(location: ATOM[location_name], detail?: TERM) -> TERM` for explicit location descriptions, use in activity content or as separate TERM
- Affected uses: t2:s2 "go to the ... end table on the wall" (wall is location-name), t2:s6 "go through the living room, to the purple ottoman" (living_room is location-name)
- Compatibility: Option A extends the signature, backward compatible. Option B adds new constructor, no compatibility issue.
- Proposed record: `{"signature": "TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country] / ATOM[location_name], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM"}`

### S3 | type: add | dimension: constructor | symbol: activity_with_direction

- Needs: n4 (t2:s2), n17 (t2:s6)
- Searches tried: `rag entry activity` → verb is STRING but no structured direction/orientation parameter; `rag search "turn left right direction qualifier"` → turn operation accepts direction: STRING, but activity constructor has no equivalent
- Interpretation: A direction-qualified activity, specifically for rotation/turning actions where direction (left, right, around) is essential to the meaning
- Alternatives considered: 
  1. Add direction parameter directly to activity: `activity(..., direction?: STRING)` — extends activity for all verbs even when not applicable
  2. Define activity-verb variants as composites: `turn_left() -> TERM`, `turn_right() -> TERM`, `turn_around() -> TERM` — more restrictive but explicit
  3. Create a separate constructor: `directional_activity(verb: STRING, direction: STRING, ...) -> TERM` — new separate construct
- Proposed approach: Define activity-verb variant composites (option 2) for directional turns:
  - `turn_left(): -> TERM` expands to `activity(verb="turn", direction="left")`
  - `turn_right(): -> TERM` expands to `activity(verb="turn", direction="right")`  
  - `turn_around(): -> TERM` expands to `activity(verb="turn", direction="around")`
  These allow direct encoding: `UTTER propose(target=turn_left())` instead of `UTTER propose(target=activity(verb="turn"), content="to your left")`
- Example usage: `UTTER propose(target=turn_left())` for t2:s2 "Turn to your left"
- Proposed record (3 composites as a member-family S3a, S3b, S3c):
  - S3a: `{"symbol": "turn_left", "kind": "composite", "definition": "A turning motion to the left", "expansion": "activity(verb=\"turn\", direction=\"left\")"}`
  - S3b: `{"symbol": "turn_right", "kind": "composite", "definition": "A turning motion to the right", "expansion": "activity(verb=\"turn\", direction=\"right\")"}`
  - S3c: `{"symbol": "turn_around", "kind": "composite", "definition": "A turning motion to rotate 180 degrees", "expansion": "activity(verb=\"turn\", direction=\"around\")"}`

### S4 | type: add | dimension: constructor | symbol: colored_object

- Needs: n6 (t2:s2), n14 (t2:s4), n20 (t2:s6)
- Searches tried: `rag entry pick_up` → has color parameter `color?: STRING / ATOM[color_label]`, but applies to target selection in operations, not to describing already-identified objects; `rag search "colored black object property descriptor"` → no constructor found
- Typed parameters: object: ATOM[object_label], color: ATOM[color_label]
- Interpretation: Describes an object with a specific color property. Assertion neither asserts existence nor makes claims about the color being correct or exhaustive; it's a description of a visually described object. Used in TRACE mode to encode "the black end table", "the white vase", "the purple ottoman".
- Example: `TERM colored_object(object=object_label::table, color=color_label::black) -> black_table : TERM` then use in `activity(verb="walk", location=black_table)` instead of relying on content strings
- Not: a color constraint (use constraints parameter in GENERATE), an assertion of color accuracy, or a color sorting criterion (use sort operation with rank fields)
- Aliases: object with color, colored entity
- Proposed record: `{"symbol": "colored_object", "kind": "constructor", "signature": "TERM colored_object(object: ATOM[object_label], color: ATOM[color_label]) -> TERM", "definition": "Description of an object with a specific color property. Preserves the object kind and color description without asserting the color's accuracy or exhaustiveness.", "not": "a constraint in GENERATE.constraints (use constraints parameter); a color assertion or claim of truth", "aliases": ["object with color"]}`

### S5 | type: add | dimension: constructor | symbol: spatial_object

- Needs: n8 (t2:s2), n9 (t2:s2), n13 (t2:s4), n16 (t2:s4), n24 (t2:s8), n26 (t2:s8)
- Searches tried: `rag search "behind across from left of spatial relation"` → found spatial-relation string values (behind, on, left_of, other_side_of, etc.) but they are operation parameters, not constructor fields; `rag entry place` → relation parameter exists for operations only; `rag search "describe object positioned"` → no constructor found for spatial descriptions in TRACE
- Typed parameters: object: ATOM[object_label], relation: STRING, reference: ATOM[object_label]
- Interpretation: Describes an object's spatial position relative to another reference object. The relation parameter uses the same values as place.relation (behind, on, left_of, right_of, between, in_front_of, other_side_of, under). Used to structure spatial constraints like "keys behind the vase", "table on the wall", "keys on the left side of the phone". Does not assert spatial accuracy or execute placement; purely descriptive.
- Example usages: 
  - `TERM spatial_object(object=object_label::keys, relation="behind", reference=object_label::vase) -> keys_behind_vase : TERM`
  - `TERM spatial_object(object=object_label::table, relation="on", reference=location_name::wall) -> table_on_wall : TERM` [if S2 accepts location_name in reference]
  - Composition: `TERM colored_object(object=object_label::table, color=color_label::black) -> black_table : TERM` then `TERM spatial_object(object=black_table, relation="on", reference=location_name::wall) -> black_table_on_wall : TERM`
- Not: place.relation (an operation parameter, not a constructor); a constraint in GENERATE.constraints; an assertion that the spatial relation is correct or complete; movement or state change (that's activity or action)
- Aliases: positioned object, object positioning, object location relative to reference
- Proposed record: `{"symbol": "spatial_object", "kind": "constructor", "signature": "TERM spatial_object(object: ATOM[object_label] / TERM, relation: STRING, reference: ATOM[object_label] / ATOM[location_name]) -> TERM", "definition": "Description of an object's spatial position relative to a reference object. The relation parameter uses values (behind, on, left_of, right_of, between, in_front_of, other_side_of, under) defined in rule_category_spatial_relation. Does not assert spatial accuracy or execute placement.", "not": "place.relation (operation parameter), a constraint in GENERATE, an assertion of truth, or movement", "aliases": ["positioned object", "object relative to"]}`

---

## Summary

These 5 suggestions address the core gaps preventing faithful translation:

1. **S1** adds the missing object type (couch) for environmental descriptions
2. **S2** extends activity to reference location-name values, or creates a location_descriptor constructor
3. **S3** adds direction-qualified activity variants (turn_left, turn_right, turn_around) for directional movements
4. **S4** adds colored_object constructor to describe objects with color properties in TRACE mode
5. **S5** adds spatial_object constructor to describe spatial relationships between objects

With these additions, every need in the translation can be fully structured without relying on opaque content strings.
