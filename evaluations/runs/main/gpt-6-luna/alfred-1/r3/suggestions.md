### S1 | type: add | dimension: constructor | symbol: action_description
- Needs: n1 (t1:s1), n4 (t2:s2), n5 (t2:s2), n11 (t2:s4), n17 (t2:s6), n18 (t2:s6), n22 (t2:s8)
- Searches tried: widen "describe turning and walking to locations as instructed actions, not performed operations" → activity, propose and related entries, but no descriptive action with destination/path/role arguments; search "TERM description of placement action object destination spatial relation", "TERM described movement turn direction destination", and "utterance imperative agent proposed action" → spatial_constraint, activity, turn, walk, propose; widen "a speaker instructs or directs an addressee to perform an action" and search "directive speech act instructing someone to do something, command" → no direct-instruction speech act fitting the imperative.
- Typed parameters: action: STRING, object?: TERM, destination?: TERM, direction?: STRING, constraints?: LIST[TERM], path?: LIST[TERM]
- Interpretation: Describes an intended or instructed action and its role fillers without executing it or asserting that it occurred. `constraints` carries structured conditions on the action or its spatial roles; `path` is an ordered list of described intermediate waypoints.
- Example: `TERM action_description(action="walk", destination=ottoman_term, path=[living_room_term]) -> action_description_2 : TERM`
- Contrast: Unlike an Action operation, this constructor is descriptive and valid in TRACE; unlike `activity`, it distinguishes object, destination, direction, route and constraints.
- Proposed record: {"symbol":"action_description","kind":"constructor","signature":"TERM action_description(action: STRING, object?: TERM, destination?: TERM, direction?: STRING, constraints?: LIST[TERM], path?: LIST[TERM]) -> TERM","definition":"Describes an intended or instructed action and its role fillers without executing it or asserting that it occurred. Constraints carry structured conditions on the action or its spatial roles; path is an ordered list of described intermediate waypoints.","not":"An executable operation or a claim that the action occurred.","aliases":[]}

### S2 | type: add | dimension: constructor | symbol: qualified_entity
- Needs: n6 (t2:s2), n7 (t2:s2), n14 (t2:s4), n15 (t2:s4), n20 (t2:s6), n21 (t2:s6)
- Searches tried: widen "color qualifier used to identify a specific object like black end table, white vase, purple ottoman" and widen "color as a descriptive qualifier for a physical object" → color_label, object_label, subject and lexical_label; search "TERM object description with color property qualifier", "object kind and color qualifier as structured entity description", and "distinct color and object kind as structured entity description" → no constructor combines separate entity-label and color-label TERM descriptions. `subject` has a single qualifier and its `kind` is STRING; `lexical_label` wraps only one atom.
- Typed parameters: entity: TERM, qualifier: TERM
- Interpretation: Combines a TERM describing an entity with a separate TERM describing a source-supplied qualifier, preserving both as structured parts of one entity description. It asserts no additional property beyond the supplied entity and qualifier descriptions.
- Example: `TERM qualified_entity(entity=end_table_term, qualifier=black_term) -> qualified_entity_2 : TERM`
- Contrast: Unlike a claim relation such as `has_attribute`, it makes no assertion that an entity actually has a property; unlike concatenating words in a label, it retains entity and qualifier as separate arguments.
- Proposed record: {"symbol":"qualified_entity","kind":"constructor","signature":"TERM qualified_entity(entity: TERM, qualifier: TERM) -> TERM","definition":"Combines a TERM describing an entity with a separate TERM describing a source-supplied qualifier, preserving both as structured parts of one entity description. It asserts no additional property beyond the supplied entity and qualifier descriptions.","not":"A claim that the entity actually possesses the described qualifier.","aliases":[]}

### S3 | type: add | dimension: vocabulary-member | symbol: end_table
- Needs: n7 (t2:s2)
- Searches tried: widen "end table as a distinct small furniture table, not a nightstand" → `table`, `night_stand`, `desk` and other furniture; `table` only denotes a table surface, while `night_stand` is specifically bedside furniture. Neither preserves the stated kind without inferring bedside placement.
- Meaning: An end table, a small table furnishing used as an end/side table; no particular location relative to a couch is implied.
- Category: location-name
- Contextual aliases: end table
- Example: `walk(destination=end_table)`
- Contrast: Not a nightstand specifically, and not merely an unspecified table surface.
- Proposed record: {"symbol":"end_table","kind":"value","category":"location-name","signature":"STRING","definition":"An end table, a small table furnishing used as an end/side table; no particular location relative to a couch is implied.","not":"A bedside nightstand specifically or an unspecified table surface.","aliases":["end table"]}
