### S1 | type: add | dimension: vocabulary-member | symbol: instruct
- Needs: n1 (t1:s1); the imperative agent statements at t2:s2, t2:s4, t2:s6, t2:s8, t2:s10, t2:s12, and t2:s14
- Searches tried: widen "user commands agent to place pan with knife on table"; search "speech act issuing an imperative instruction or command to perform described action" → `propose`, `ask`, `respond`, `inform`, and `offer`; none denotes issuing a direct instruction.
- Meaning: A direct command/request that the addressee perform the action or bring about the state described by its TERM target; it neither asserts completion nor merely suggests an option.
- Category: speech_act
- Contextual aliases: command, instruct, direct
- Example: `UTTER instruct(target=action_description_2)`
- Contrast: `propose` suggests an action or idea rather than directing the addressee to perform it.
- Proposed record: {"symbol":"instruct","kind":"speech_act","signature":"UTTER instruct(target: TERM)","definition":"A direct instruction to an addressee to perform the action or bring about the state described by target. Does not assert that the action occurred.","not":"A suggestion (propose), question (ask), or record of completed behavior.","aliases":["command","instruct"]}

### S2 | type: add | dimension: constructor | symbol: action_description
- Needs: n2 (t1:s1), n7 (t2:s2), n9 (t2:s2), n12 (t2:s4), n17–n18 (t2:s6), n21 (t2:s8), n26 (t2:s10), n29–n30 and n32 (t2:s12), n34 (t2:s14)
- Searches tried: widen "agent utterance proposing ordered physical actions: walk, turn, pick up, place, and temporal sequence"; search "structured description of an intended action with destination, direction and constraints" → `activity` has no destination/direction roles, while operation entries are executable REQUEST operations and cannot describe work in TRACE.
- Typed parameters: `verb: STRING`, optional `target/source/destination: TERM`, optional `relation/direction: STRING`, optional `target_qualifiers/destination_qualifiers/constraints: LIST[TERM]`.
- Interpretation: A non-effectful description of an intended or directed action. Role arguments identify the action's participants; relation and direction qualify the described action; qualifier lists apply to the named role, and constraints state additional intended conditions. It is not an operation or evidence that the action occurred.
- Example: `TERM action_description(verb="place", target=pan_term, destination=table_term, relation=on) -> action_description_2 : TERM`
- Contrast: It describes an action in speech or a plan; it does not execute `place` or yield a REF.
- Proposed record: {"symbol":"action_description","kind":"constructor","signature":"TERM action_description(verb: STRING, target?: TERM, source?: TERM, destination?: TERM, relation?: STRING, direction?: STRING, target_qualifiers?: LIST[TERM], destination_qualifiers?: LIST[TERM], constraints?: LIST[TERM]) -> TERM","definition":"A structured, non-effectful description of an intended action and its participants. Direction and relation qualify the action; target_qualifiers and destination_qualifiers constrain those roles, while constraints state additional conditions; it does not execute or assert occurrence.","not":"An external operation, completed event, or runtime object reference.","aliases":[]}

### S3 | type: add | dimension: constructor | symbol: relative_region
- Needs: n25 (t2:s8), n38 (t2:s14)
- Searches tried: widen "on left side above lettuce relative to table" and "burner location relative to stove"; `left_of` expresses a relation between entities, not a subregion of a surface, and no retrieved constructor represents a back-left or left-side region.
- Typed parameters: `reference: TERM`, `directions: LIST[STRING]` (one or more of the explicitly named spatial directions, e.g. `"left"`, `"back"`).
- Interpretation: A spatial subregion of the referenced object/surface, specified by the named directions; direction order does not imply an unstated distance or coordinate system.
- Example: `TERM relative_region(reference=table_term, directions=["left"]) -> relative_region_2 : TERM`
- Contrast: Not an entity to the left of the table; it denotes a region of the table itself.
- Proposed record: {"symbol":"relative_region","kind":"constructor","signature":"TERM relative_region(reference: TERM, directions: LIST[STRING]) -> TERM","definition":"A region of the referenced object or surface identified by one or more source-specified spatial directions (such as left or back). It adds no distance, orientation frame, or geometry not supplied by the source.","not":"A separate entity positioned left of or behind the reference.","aliases":[]}

### S4 | type: add | dimension: vocabulary-member | symbol: above
- Needs: n39 (t2:s14)
- Searches tried: search "put an object on the left side above another object"; available spatial relations include `on`, `under`, and `in_front_of`, but none means higher than.
- Meaning: Positioned at a higher vertical position than the reference; does not imply contact or support.
- Category: spatial-relation
- Contextual aliases: above
- Example: spatial constraint with relation `above`, object pan, and reference lettuce.
- Contrast: `on` means resting atop; `in_front_of` is front/back depth, not vertical height.
- Proposed record: {"symbol":"above","kind":"value","category":"spatial-relation","signature":"STRING","definition":"Positioned at a higher vertical position than the reference. Does not imply contact, support, or a particular vertical distance.","not":"Resting atop or supported by the reference (on).","aliases":[]}

### S5 | type: add | dimension: constructor | symbol: nearest_to
- Needs: n16 (t2:s4)
- Searches tried: widen "pick up closest knife next to lettuce"; `rank_distance` is a search-ranking field, and `similarity` explicitly excludes spatial proximity. Neither expresses selecting a nearest instance relative to a reference.
- Typed parameters: `candidate: TERM`, `reference: TERM`.
- Interpretation: Describes the candidate instance of a class/entity that has the least spatial distance to the stated reference among the relevant candidates. The reference and candidate set must be supplied or established by context; ties remain ambiguous.
- Example: `TERM nearest_to(candidate=lettuce_term, reference=agent_location) -> nearest_to_2 : TERM`
- Contrast: Not semantic similarity, ranking by an unrelated field, or an unanchored claim that something is simply "closest".
- Proposed record: {"symbol":"nearest_to","kind":"constructor","signature":"TERM nearest_to(candidate: TERM, reference: TERM) -> TERM","definition":"Describes a candidate instance having the least spatial distance to the stated reference among the contextually relevant candidates. Requires an identifiable reference and candidate set; tied candidates remain unresolved.","not":"Semantic similarity or a nearestness relation with no reference point.","aliases":["closest to"]}
