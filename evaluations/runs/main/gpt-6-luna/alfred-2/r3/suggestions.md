### S1 | type: add | dimension: constructor | symbol: food_slice
- Needs: n1 (t1:s1), n2 (t1:s1), n15 (t2:s16), n18 (t2:s20), n20 (t2:s24)
- Searches tried: “TERM description of a food item in a state such as sliced” → state_sliced, has_state; “cut lettuce into slices: resulting object is a slice of lettuce” → state_sliced, slice, activity; widen “cool or chill a food object using a fridge” → chill and food labels, but no individual-slice descriptor. `state_sliced` denotes a condition, not a single resulting food portion; `slice` is an operation, not an object constructor.
- Typed parameters: food: ATOM[food_label]
- Interpretation: Describes one slice/portion of the specified food kind, without asserting that it exists or that a slicing operation succeeded. It identifies the described portion for subsequent activity and recorded-operation descriptions.
- Example: `TERM food_slice(food=food_label::lettuce) -> food_slice_2 : TERM`
- Proposed record: {"symbol": "food_slice", "kind": "constructor", "signature": "TERM food_slice(food: ATOM[food_label]) -> TERM", "definition": "Describes one slice or portion of the specified food kind, without asserting existence or successful preparation.", "not": "the slicing operation or merely the state of being sliced", "aliases": []}

### S2 | type: add | dimension: vocabulary-member | symbol: step
- Needs: n9 (t2:s6), n12 (t2:s10), n14 (t2:s14), n19 (t2:s22)
- Searches tried: “step forward walking toward target” → walk, walk_backward, face; “movement distance step forward extent walk” and widen “take a step left to face the counter” → walk and related navigation terms, but no discrete directional step operation. `walk` means locomotion toward a destination; `walk_backward` means walking backward, neither captures a step forward or sideways.
- Meaning: A single step in the stated direction, without implying a destination or unstated distance.
- Category: action
- Contextual aliases: none
- Example: `RECORD ACTION step(direction="forward") STATUS unknown SOURCE "t2:s6" -> step_event : EVENT`
- Contrast: Not `walk(destination=...)`, which moves toward a destination, and not `turn(direction=...)`, which rotates orientation.
- Proposed record: {"symbol": "step", "kind": "operation", "category": "action", "signature": "(direction: STRING) -> void", "definition": "Take one locomotor step in the stated direction (such as forward or left); does not imply an unstated distance or destination.", "not": "walking toward a destination or rotating orientation", "aliases": []}

### S3 | type: refine | dimension: refine-entry | target: walk
- Needs: n5 (t2:s2)
- Searches tried: “walk across the room to face the sink” and “movement distance step forward extent walk” → `walk(destination, relation?)`; no matching extent parameter or other operation for the across-room extent.
- Before: `walk(destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void`; describes locomotion toward a destination but cannot preserve a stated extent such as “across the room.”
- After: Add optional `extent: STRING` for a source-explicit movement extent; preserve the source wording without deriving a numeric distance.
- Justification: The source distinguishes walking across the room from merely moving toward the sink.
- Affected uses: `RECORD ACTION walk(destination=object_label::sink, extent="across the room")` at t2:s2.
- Compatibility: Existing calls omitting extent retain their meaning; this optional field adds no implied distance to existing uses.
- Proposed record: {"signature": "(destination: STRING / TERM / ATOM[object_label], relation?: STRING, extent?: STRING) -> void", "definition": "Locomote towards a target destination or landmark. Optional extent preserves a source-stated qualitative movement extent without inferring a numeric distance."}
