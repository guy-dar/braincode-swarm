### S1 | type: add | dimension: constructor | symbol: action_description
- Needs: n1 (t1:s1), n4–n5 (t2:s2), n11 (t2:s4), n17–n18 (t2:s6), n22 (t2:s8)
- Searches tried: search “describe action and its object destination plus spatial relation as a TERM, without performing it” → `activity`, `spatial_constraint`, `walk`, `place`; widen “turn left and go to the end table located on the wall across from couch” → `turn`, `walk`, `activity`; widen “agent directs recipient to perform steps in numbered order” → `sequence`, `obligation`, `walk`. `activity` lacks destination/source/direction/route roles; the action operations are not legal as executed statements in TRACE; `sequence` only orders existing terms.
- Typed parameters: `verb: STRING`, `object?: TERM`, `source?: TERM`, `destination?: TERM`, `direction?: STRING`, `route?: LIST[TERM]`, `constraints?: LIST[TERM]`
- Interpretation: Describes an action and its participant, direction, route, destination, and/or spatial constraints without asserting that it occurred or making it executable. `route` is ordered; constraints preserve the distinct spatial conditions supplied by the source.
- Example: `TERM action_description(verb="place", object=keys_term, destination=ottoman_term, constraints=[placement_term]) -> action_description_2 : TERM`
- Contrast: Unlike an operation such as `place` or `walk`, this is a TERM usable in a TRACE and does not perform or report an action.
- Proposed record: {"symbol":"action_description","kind":"constructor","signature":"TERM action_description(verb: STRING, object?: TERM, source?: TERM, destination?: TERM, direction?: STRING, route?: LIST[TERM], constraints?: LIST[TERM]) -> TERM","definition":"A structured description of an action with optional object, source, destination, direction, ordered route, and spatial constraints. The verb is a concise source-supplied action label, not free-form sentence content; a label matching an operation describes that action without invoking it. It describes an action without asserting that it occurred or executing it.","not":"An executable Action or a claim that the described action occurred.","aliases":[]}

### S2 | type: add | dimension: vocabulary-member | symbol: across_from
- Needs: n9 (t2:s2)
- Searches tried: search “across from couch spatial relation” and widen “across from / opposite across a room spatial relation” → `other_side_of`, `between`, and spatial relation values; `other_side_of` means positioned on the opposite or other side, and `between` means middle of reference entities. Neither record defines the source's “across from” relation.
- Meaning: A spatial relation in which one entity is across from another; distinct from adjacency, between-ness, or merely being on the opposite side.
- Category: spatial-relation
- Contextual aliases: None proposed; retain “across from” as the exact phrase for this relation.
- Example: `TERM spatial_constraint(relation=across_from, object=end_table_term, reference=couch_term) -> table_across_couch : TERM`
- Contrast: Not `between` and not the broader/ambiguous `other_side_of`.
- Proposed record: {"symbol":"across_from","kind":"value","category":"spatial-relation","definition":"Positioned across from a reference entity. This relation is distinct from adjacency, between-ness, and a general opposite-side relation.","not":"between or other_side_of","aliases":["across from"]}
