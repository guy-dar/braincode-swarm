### S1 | type: add | dimension: vocabulary-member | symbol: walk_forward
- Needs: n7 (t2:s2)
- Searches tried: widen “walk forward without a destination” and search “walking forward in place no target movement direction” → `walk`, `walk_backward`; `walk` requires a destination and `walk_backward` means the opposite direction.
- Meaning: Forward locomotion without a stated destination, preserving that no destination was supplied.
- Category: operation
- Contextual aliases: forward walk
- Example: `RECORD ACTION walk_forward() STATUS unknown SOURCE "t2:s2" -> walk_forward_event : EVENT`
- Contrast: Not `walk` toward a destination or `walk_backward`.
- Proposed record: `{"symbol":"walk_forward","kind":"operation","signature":"() -> void","definition":"Locomote forward without specifying a destination. Does not assert a particular distance or endpoint.","not":"Walking backward or walking toward a named destination.","aliases":["walk forward"]}`

### S2 | type: refine | dimension: refine-entry | target: pick_up
- Needs: n12 (t2:s4)
- Searches tried: widen “pick up object selected by nearest-to spatial criterion” and search “object located closest to a reference object” → `pick_up`, `rank_distance`, `spatial_constraint`; no candidate permits a TERM selector as the pick-up target.
- Before: `target: STRING / ATOM[object_label] / ATOM[food_label]`
- After: Add `TERM` to the target alternatives, restricted to a glossary-defined entity-selection descriptor such as `nearest_to`; preserve the existing string and atom alternatives and result rules.
- Justification: The requested target is selected by its relation and proximity to another object, not merely by its object-kind label.
- Affected uses: t2:s4 selection of the closest knife next to lettuce; existing label-target calls remain valid.
- Compatibility: Backward-compatible for existing target arguments; new TERM targets are valid only when their constructors resolve an entity selection.
- Proposed record: `{"signature":"(target: STRING / ATOM[object_label] / ATOM[food_label] / TERM, quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]]"}`

### S3 | type: add | dimension: constructor | symbol: nearest_to
- Needs: n15 (t2:s4), n16 (t2:s4)
- Searches tried: widen “closest knife next to lettuce” and search “object located closest to a reference object / nearest entity” → `rank_distance` (search ranking field), `spatial_constraint` (spatial descriptor), and `next_to` (adjacency only); none selects the closest matching object.
- Typed parameters: `item: TERM`, `reference: TERM`, `relation?: STRING`; output `TERM`.
- Interpretation: Selects/describes the item of the given kind or description nearest to the reference, optionally requiring the stated spatial relation. It describes selection criteria and does not itself acquire the object.
- Example: `TERM nearest_to(item=knife_term, reference=lettuce_term, relation=next_to) -> nearest_to_2 : TERM`
- Proposed record: `{"symbol":"nearest_to","kind":"constructor","signature":"TERM nearest_to(item: TERM, reference: TERM, relation?: STRING) -> TERM","definition":"A selection descriptor for the item nearest to a reference, optionally constrained by a spatial relation. It describes selection criteria and does not acquire or assert an object.","not":"A distance ranking of arbitrary search results or a claim that an object has been acquired.","aliases":["closest to","nearest to"]}`

### S4 | type: add | dimension: constructor | symbol: qualified_entity
- Needs: n11 (t2:s2), n33 (t2:s12)
- Searches tried: search “structured description entity object with color qualifier” → `lexical_label`, `spatial_constraint`, `color_label`; no constructor combines an entity-kind label with a color qualifier.
- Typed parameters: `kind: ATOM[object_label]`, `color?: ATOM[color_label]`; output `TERM`.
- Interpretation: Describes an entity kind with an explicitly supplied qualifier; adds no unprovided properties or identity.
- Example: `TERM qualified_entity(kind=object_label::table, color=color_label::black) -> qualified_entity_2 : TERM`
- Contrast: A color label alone does not identify a black table; `format_table` is a layout, not a table entity.
- Proposed record: `{"symbol":"qualified_entity","kind":"constructor","signature":"TERM qualified_entity(kind: ATOM[object_label], color?: ATOM[color_label]) -> TERM","definition":"Describes an entity kind with the supplied color qualifier. Adds no other properties, spatial position, or runtime identity.","not":"A color label alone or an assertion that a particular physical object has been observed.","aliases":[]}`

### S5 | type: add | dimension: vocabulary-member | symbol: above
- Needs: n39 (t2:s14)
- Searches tried: widen “above spatial relation higher than lettuce” and search “above relation spatial location” → `under`, `in_front_of`, `behind`, `spatial_constraint`, and `spatial_state`; none means above.
- Meaning: Positioned vertically higher than the reference.
- Category: spatial-relation
- Contextual aliases: above
- Example: `TERM spatial_constraint(object=pan_term, reference=lettuce_term, relation=above) -> spatial_constraint_2 : TERM`
- Contrast: Not `on` (resting atop) or `in_front_of` (front/back orientation).
- Proposed record: `{"symbol":"above","kind":"value","category":"spatial-relation","definition":"Positioned vertically higher than the reference object.","not":"Not necessarily resting atop the reference (on) or positioned in front of it.","aliases":["above"]}`

### S6 | type: refine | dimension: refine-entry | target: place
- Needs: n25 (t2:s8), n38 (t2:s14), n39 (t2:s14)
- Searches tried: widen “place pan on back-left burner” and “place pan on left side of table and above lettuce”; search “spatial composition on left side of table above lettuce” → `place`, `spatial_constraint`, `left_of`; no current `place` signature accepts multiple independent spatial constraints, and its destination disallows a qualified-entity TERM.
- Before: `(target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void`
- After: Add `destination: TERM` as an alternative and add optional `constraints?: LIST[TERM]` describing additional simultaneous spatial constraints; retain existing arguments and explicit-relation requirements.
- Justification: The source specifies a destination qualified as a table and two placement relations: left of the table and above the lettuce.
- Affected uses: t2:s14 final placement. Existing calls remain valid.
- Compatibility: Backward-compatible for existing calls; TERM destinations and constraint lists are new typed uses.
- Proposed record: `{"signature":"(target: REF[STRING], destination: STRING / ATOM[object_label] / TERM, location?: STRING / ATOM[object_label], relation?: STRING, constraints?: LIST[TERM]) -> void"}`

### S7 | type: add | dimension: constructor | symbol: placement_with_contents
- Needs: n1 (t1:s1), n2 (t1:s1), n6 (t1:s1)
- Searches tried: widen “command to put a pan containing a knife on a table” and “put an object inside another object and place the containing object on a surface” → `activity`, `include`, `spatial_constraint`, and `place`; these can describe component relations or a single placement, but do not compose the containment with the requested placement as one target.
- Typed parameters: `object: TERM`, `content: TERM`, `destination: TERM`; output `TERM`.
- Interpretation: Describes the requested placement of an object that contains the specified content onto the specified destination; asserts no completed action.
- Example: `TERM placement_with_contents(object=pan_term, content=knife_term, destination=table_term) -> placement_with_contents_2 : TERM`
- Contrast: Not a trace of a completed placement and not merely a claim that the objects are near one another.
- Proposed record: `{"symbol":"placement_with_contents","kind":"constructor","signature":"TERM placement_with_contents(object: TERM, content: TERM, destination: TERM) -> TERM","definition":"Describes a requested placement of an object containing the specified content onto the specified destination. Constructs an action description only; it does not assert execution or success.","not":"A recorded placement event or mere adjacency between the objects.","aliases":[]}`
