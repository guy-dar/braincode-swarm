### S1 | type: add | dimension: constructor | symbol: object_description
- Needs: n6, n7, n8, n14, n15, n16, n20, n21 (t2:s2, t2:s4, t2:s6).
- Searches tried: search "object description color spatial relation", "entity color qualifiers", "qualified object description"; widen "object description combining kind color and spatial constraints" → lexical_label preserves labels without qualifying an object, spatial_constraint supplies location only, requirement imposes a required property rather than an existing identifying color, subject.kind does not accept object atoms.
- Typed parameters: label: STRING / ATOM[object_label], color?: ATOM[color_label]; result TERM; STRING labels must be accepted entity-name or location-name descriptors.
- Interpretation: Describes an object by its source-supplied kind label and optional identifying color qualifier; atom labels retain their opaque group semantics and imply no properties beyond the explicit qualification. It creates neither an assertion nor runtime identity.
- Example: `TERM object_description(color=color_label::black, label=object_label::endtable) -> object_description_2 : TERM`.
- Proposed record: {"symbol":"object_description","kind":"constructor","signature":"TERM object_description(label: STRING / ATOM[object_label], color?: ATOM[color_label]) -> TERM","definition":"Describe an object or landmark by a source-supported kind descriptor and optional identifying color qualifier. STRING labels must be accepted entity-name or location-name descriptors; open atoms remain opaque labels, and this description neither asserts existence nor creates runtime identity.","not":"A requirement to recolor an object or an inferred dictionary sense of an object label.","aliases":[]}

### S2 | type: add | dimension: constructor | symbol: place_description
- Needs: n1 (t1:s1), n22 (t2:s8); n24, n26 constrain the described action.
- Searches tried: search "describe requested placing object on surface relative to another object", "action description operation arguments"; widen "describe placing keys on ottoman left of phone as requested action" → place is an external operation, request tracks a communicative request but requires its content, activity lacks destination and governed placement constraints, spatial_constraint describes a configuration rather than an act of placing.
- Typed parameters: target: TERM, destination: TERM, constraints?: LIST[TERM]; result TERM.
- Interpretation: Describes placing the target at the destination, with optional constraints on its resulting spatial configuration; target and destination are object descriptions, including lexical_label and object_description. Does not acquire a REF, imply completion or invent an acquisition step.
- Example: `TERM place_description(target=keys_description, constraints=[on_ottoman], destination=ottoman_description) -> place_description_2 : TERM`.
- Proposed record: {"symbol":"place_description","kind":"constructor","signature":"TERM place_description(target: TERM, destination: TERM, constraints?: LIST[TERM]) -> TERM","definition":"Describe an act of placing a described object at a described destination; lexical_label and object_description are permitted in these description roles. Optional constraints govern the resulting configuration, not the source selection; construction performs no operation, asserts no completion and creates no runtime reference.","not":"Dropping without a destination, or merely describing an already existing spatial configuration.","aliases":[]}

### S3 | type: add | dimension: constructor | symbol: pick_up_description
- Needs: n11, n13, n16 (t2:s4).
- Searches tried: search "action description operation arguments", "action intent destination direction"; widen "describe picking up keys selected by spatial location" → pick_up is executable; RECORD would claim an occurrence; spatial_state asserts a configuration; spatial_constraint alone omits acquisition; activity lacks reviewed target-selection constraints.
- Typed parameters: target: TERM, constraints?: LIST[TERM]; result TERM.
- Interpretation: Describes picking up the target; optional constraints identify the object in its pre-acquisition state, not its final location. Accepts object descriptions including lexical_label and object_description; supplies no quantity, result or reference when absent in the source.
- Example: `TERM pick_up_description(target=keys_description, constraints=[behind_vase, on_table]) -> pick_up_description_2 : TERM`.
- Proposed record: {"symbol":"pick_up_description","kind":"constructor","signature":"TERM pick_up_description(target: TERM, constraints?: LIST[TERM]) -> TERM","definition":"Describe acquiring a described object by picking it up; lexical_label and object_description are allowed target descriptions. Optional constraints select the target in its pre-acquisition state; construction asserts no occurrence, invents no quantity and creates no runtime reference.","not":"A successful acquisition event or constraints on where to place the object afterward.","aliases":[]}

### S4 | type: add | dimension: constructor | symbol: turn_description
- Needs: n4 (t2:s2), n17 (t2:s6).
- Searches tried: search "ordered action plan turn walk through room", "action intent destination direction"; widen "describe turning left and turning around" → turn is an external operation, look adjusts camera gaze instead, activity lacks a direction field and a reviewed directional-turning interpretation.
- Typed parameters: direction: STRING; result TERM; controlled literals "left", "right", "around" only.
- Interpretation: Describes rotation of the addressed actor's body/view orientation; left and right are relative to that actor's current orientation, while around reverses facing direction without choosing a clockwise or counterclockwise path. The literals are defined directional parameters, not entity or operation strings.
- Example: `TERM turn_description(direction="around") -> turn_description_2 : TERM`.
- Proposed record: {"symbol":"turn_description","kind":"constructor","signature":"TERM turn_description(direction: STRING) -> TERM","definition":"Describe rotation of the addressed actor's body/view orientation; direction is one of the controlled literals left, right or around. Left/right remain actor-relative and around reverses facing without specifying the rotation path; no operation or occurrence is asserted.","not":"Camera-only gaze adjustment, a circular object shape, or a world-coordinate direction.","aliases":[]}

### S5 | type: add | dimension: constructor | symbol: walk_description
- Needs: n5 (t2:s2), n18, n19 (t2:s6).
- Searches tried: search "ordered action plan turn walk through room", "path through waypoint", "action intent destination direction"; widen "describe walking to landmark through living room" → walk executes locomotion and has no traversed-region parameter, activity lacks distinct destination and via roles, spatial_constraint relates static objects instead of describing traversal.
- Typed parameters: destination: TERM, via?: STRING / TERM; result TERM; STRING via must be an accepted location-name descriptor.
- Interpretation: Describes walking to the destination and, when supplied, through the specified region en route. Destination and TERM via permit object/landmark descriptions including lexical_label and object_description; no route length, extra waypoint, starting location or completion is inferred.
- Example: `TERM walk_description(destination=purple_ottoman_description, via=living_room) -> walk_description_2 : TERM`.
- Proposed record: {"symbol":"walk_description","kind":"constructor","signature":"TERM walk_description(destination: TERM, via?: STRING / TERM) -> TERM","definition":"Describe walking to a described destination, optionally traversing the explicitly supplied region en route. Destination and TERM via accept object/landmark descriptions including lexical_label and object_description; STRING via must be an accepted location-name descriptor, and no starting point, distance or completed movement is implied.","not":"Web-page navigation or merely being located in a room.","aliases":[]}

### S6 | type: add | dimension: vocabulary-member | symbol: at_wall
- Needs: n8 (t2:s2).
- Searches tried: search "against wall along wall"; widen "end table on the wall located along wall boundary" → wall names a landmark, on means resting atop, next_to specifies adjacency, shelf names a different object; none supplies the source's broad wall-boundary location without resolving mounting/contact.
- Meaning: Located at a wall boundary; attachment, contact and precise distance remain unspecified unless separately represented.
- Category: spatial-relation.
- Contextual aliases: "on the wall" only in boundary-location readings; never unconditional normalization of on.
- Example: `TERM spatial_constraint(object=endtable_description, reference=wall_description, relation=at_wall) -> spatial_constraint_2 : TERM`.
- Contrast: on means resting atop; at_wall does not establish support or wall mounting.
- Proposed record: {"symbol":"at_wall","kind":"value","category":"spatial-relation","signature":"STRING","definition":"Located at a wall boundary, with the reference required to describe a wall. Does not specify attachment, contact, support or exact distance, which require separate source-supported constraints.","not":"Resting atop a wall or necessarily mounted to it.","aliases":[]}

### S7 | type: add | dimension: vocabulary-member | symbol: across_from
- Needs: n9 (t2:s2).
- Searches tried: search "across from couch", "across from facing opposite"; widen "across from the couch opposite facing location" → other_side_of specifies the other side of the reference object rather than an opposing location across space; in_front_of specifies frontness, not opposition; next_to is adjacency.
- Meaning: Positioned opposite the reference landmark across intervening space, without prescribing distance or the object's own facing direction.
- Category: spatial-relation.
- Contextual aliases: "across from", "opposite" in spatial-location contexts only.
- Example: `TERM spatial_constraint(object=endtable_description, reference=couch_description, relation=across_from) -> spatial_constraint_2 : TERM`.
- Contrast: other_side_of can put an object beyond the reference; across_from relates opposing locations without implying that the reference lies between observer and object.
- Proposed record: {"symbol":"across_from","kind":"value","category":"spatial-relation","signature":"STRING","definition":"Positioned opposite a reference landmark across intervening space. This specifies opposing locations without prescribing distance, object orientation or an observer-relative far side of the reference.","not":"Adjacent to the reference or necessarily beyond it on its other side.","aliases":["across from"]}
