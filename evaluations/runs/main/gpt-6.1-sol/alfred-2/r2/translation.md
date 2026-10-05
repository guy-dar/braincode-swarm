Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=food_label::lettuce) -> lexical_label_2 : TERM
    TERM lexical_label(value=object_label::counter) -> lexical_label_3 : TERM
    TERM slice_portion(material=lexical_label_2, quantity=1) -> slice_portion_2 : TERM # PROPOSED: S1
    TERM describe_chill(target=slice_portion_2) -> describe_chill_2 : TERM # PROPOSED: S2
    TERM describe_place(target=slice_portion_2, destination=lexical_label_3, relation=on) -> describe_place_2 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_chill_2, describe_place_2]) -> sequence_2 : TERM
    CLAIM request(target=sequence_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM lexical_label(value=object_label::sink) -> lexical_label_2 : TERM
    TERM lexical_label(value=object_label::knife) -> lexical_label_3 : TERM
    TERM lexical_label(value=object_label::fridge) -> lexical_label_4 : TERM
    TERM spatial_constraint(object=t1.lexical_label_2, reference=t1.lexical_label_3, relation=on) -> spatial_constraint_2 : TERM
    TERM describe_turn(direction="left") -> describe_turn_2 : TERM # PROPOSED: S2
    TERM describe_walk(destination=lexical_label_2, extent="across_room") -> describe_walk_2 : TERM # PROPOSED: S2
    TERM describe_face(target=lexical_label_2) -> describe_face_2 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_turn_2, describe_walk_2, describe_face_2]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM describe_pick_up(target=lexical_label_3, relation=in, source=lexical_label_2) -> describe_pick_up_2 : TERM # PROPOSED: S2
    UTTER propose(target=describe_pick_up_2)
    TERM describe_turn(direction="around") -> describe_turn_3 : TERM # PROPOSED: S2
    TERM describe_walk(direction="forward", steps=1) -> describe_walk_3 : TERM # PROPOSED: S2
    TERM describe_face(target=t1.lexical_label_2, constraints=[spatial_constraint_2]) -> describe_face_3 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_turn_3, describe_walk_3, describe_face_3]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    TERM describe_slice(target=t1.lexical_label_2, constraints=[spatial_constraint_2]) -> describe_slice_2 : TERM # PROPOSED: S2
    UTTER propose(target=describe_slice_2)
    TERM describe_face(target=t1.lexical_label_3) -> describe_face_4 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_turn_3, describe_walk_3, describe_face_4]) -> sequence_4 : TERM
    UTTER propose(target=sequence_4)
    TERM describe_place(target=lexical_label_3, destination=t1.lexical_label_3, relation=on) -> describe_place_2 : TERM # PROPOSED: S2
    UTTER propose(target=describe_place_2)
    UTTER propose(target=sequence_3)
    TERM describe_pick_up(target=t1.slice_portion_2, relation=on, source=t1.lexical_label_3) -> describe_pick_up_3 : TERM # PROPOSED: S2
    UTTER propose(target=describe_pick_up_3)
    TERM describe_face(target=lexical_label_4) -> describe_face_5 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_turn_3, describe_walk_3, describe_face_5]) -> sequence_5 : TERM
    UTTER propose(target=sequence_5)
    TERM describe_chill(target=t1.slice_portion_2, destination=lexical_label_4) -> describe_chill_2 : TERM # PROPOSED: S2
    TERM describe_remove(target=t1.slice_portion_2, source=lexical_label_4) -> describe_remove_2 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_chill_2, describe_remove_2]) -> sequence_6 : TERM
    UTTER propose(target=sequence_6)
    TERM describe_walk(direction="left", steps=1) -> describe_walk_4 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_walk_4, describe_face_4]) -> sequence_7 : TERM
    UTTER propose(target=sequence_7)
    TERM spatial_constraint(object=t1.slice_portion_2, reference=lexical_label_2, relation=right_of) -> spatial_constraint_3 : TERM
    TERM describe_place(target=t1.slice_portion_2, constraints=[spatial_constraint_3], destination=t1.lexical_label_3, relation=on) -> describe_place_3 : TERM # PROPOSED: S2
    UTTER propose(target=describe_place_3)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | describe_chill (S2), slice_portion (S1), request | proposed |
| n2 | object | food_label::lettuce, slice_portion (S1) | proposed |
| n3 | action | describe_place (S2), on | proposed |
| n4 | object | object_label::counter, lexical_label | label-preserved |
| n5 | action | describe_turn, describe_walk, describe_face (S2), sequence | proposed |
| n6 | object | object_label::sink, lexical_label | label-preserved |
| n7 | action | describe_pick_up (S2), in | proposed |
| n8 | object | object_label::knife, lexical_label | label-preserved |
| n9 | action | describe_turn, describe_walk, describe_face (S2), spatial_constraint | proposed |
| n10 | object | food_label::lettuce, lexical_label | label-preserved |
| n11 | action | describe_slice (S2), spatial_constraint | proposed |
| n12 | action | describe_turn, describe_walk, describe_face (S2), sequence | proposed |
| n13 | action | describe_place (S2), on | proposed |
| n14 | action | describe_turn, describe_walk, describe_face (S2), spatial_constraint | proposed |
| n15 | action | describe_pick_up (S2), slice_portion (S1), on | proposed |
| n16 | action | describe_turn, describe_walk, describe_face (S2), sequence | proposed |
| n17 | object | object_label::fridge, lexical_label | label-preserved |
| n18 | action | describe_chill, describe_remove (S2), sequence | proposed |
| n19 | action | describe_walk, describe_face (S2), sequence | proposed |
| n20 | action | describe_place (S2), spatial_constraint, on, right_of | proposed |

## Why the translation failed

- n1, n3, n5, n7, n9, n11–n16, n18–n20: widened every distinct action need using its table wording (n14 repeats n9). Closest matches were executable chill/place/turn/walk/face/pick_up/slice/remove. These cannot describe instructions inside TRACE: RECORD would fabricate observed execution. Search "action description target destination source direction distance state" and "chill description place description turn description walk description", followed by widen "nonexecuting structured descriptions of physical actions with destination source direction steps and constraints", found activity, spatial_constraint, sequence and operations, but no sufficiently typed descriptive profile. activity lacks source/destination, direction, step count and selection constraints; its verb is not an unrestricted license to invent physical predicates. Proposed S2 supplies these descriptions without effects or results.
- n2 (also n1, n15, n18, n20): widen "lettuce slice" and "structured term for a slice portion of material", search "slice portion of material constructor" and "object description sliced portion lettuce" found state_sliced and slice. A sliced state does not distinguish one slice from an entire sliced head; slice denotes an operation, not a portion. Proposed S1.
- Search "physical object description location state portion" found spatial_state/has_state claims and geographical location_spec; these cannot silently assert proposed plan prerequisites. Existing spatial_constraint is used descriptively instead.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation; one supplied user message and one supplied agent message containing a numbered proposed procedure.
- Coverage status: partial against the pinned glossary; suggested document depends on S1 and S2 and is not canonical accepted BrainCode.
- Source-span coverage: t1:s1 and every substantive agent segment t2:s2, s4, s6, s8, s10, s12, s14, s16, s18, s20, s22, s24 correspond in order to the request claim and twelve UTTERs. Odd agent segments are numbering markers preserved by statement order, not invented turns. No execution, success, tool output, or reasoning evidence is supplied.
- Opaque-text spans: none.
- Label-preserved spans: lettuce at t1:s1, t2:s6, s8, s14, s16, s20, s24 → food_label::lettuce; counter at t1:s1, t2:s6, s8, s10, s12, s14, s16, s22, s24 → object_label::counter; sink at t2:s2, s4, s24 → object_label::sink; knife at t2:s4, s12 → object_label::knife; fridge at t2:s18, s20 → object_label::fridge. Labels preserve supplied roles, not inferred capabilities. Slice meaning requires S1.
- Missing constructs: S1 slice_portion; S2 eight typed, nonexecuting physical-action description constructors.
- Unresolved ambiguities: left/around/forward use the acting agent's local frame; the final right-of frame is not supplied and remains context-dependent. No absolute orientation or metric distance is invented. The agent's instructions are represented as proposals, not performed actions; the source does not establish actual execution. Slicing is not attributed explicitly to the knife merely because the plan acquired it.
- Proposed glossary/spec changes: glossary additions S1–S2 only; no grammar or type-rule changes.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported 0 unresolved needs by its lexical heuristic and 9 unknown constructor symbols: slice_portion plus describe_chill, describe_face, describe_pick_up, describe_place, describe_remove, describe_slice, describe_turn, describe_walk. All are explicitly proposed in S1–S2. Its need matches via nouns do not establish structured action coverage; the semantic gaps above remain.
