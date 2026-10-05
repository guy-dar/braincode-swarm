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
    TERM describe_entity(label=lexical_label_2, portion=TRUE, quantity=1, state=state_sliced) -> describe_entity_2 : TERM # PROPOSED: S1
    TERM describe_chill(target=describe_entity_2) -> describe_chill_2 : TERM # PROPOSED: S2
    TERM describe_place(target=describe_entity_2, destination=lexical_label_3, relation=on) -> describe_place_2 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_chill_2, describe_place_2]) -> sequence_2 : TERM
    CLAIM request(target=sequence_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM lexical_label(value=object_label::sink) -> lexical_label_2 : TERM
    TERM lexical_label(value=object_label::knife) -> lexical_label_3 : TERM
    TERM lexical_label(value=object_label::fridge) -> lexical_label_4 : TERM
    TERM lexical_label(value=object_label::room) -> lexical_label_5 : TERM
    TERM describe_turn(direction="left") -> describe_turn_2 : TERM # PROPOSED: S2
    TERM describe_walk(destination=lexical_label_2, traverse=lexical_label_5) -> describe_walk_2 : TERM # PROPOSED: S2
    TERM describe_face(target=lexical_label_2) -> describe_face_2 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_turn_2, describe_walk_2, describe_face_2]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM describe_pick_up(target=lexical_label_3, source=lexical_label_2) -> describe_pick_up_2 : TERM # PROPOSED: S2
    UTTER propose(target=describe_pick_up_2)
    TERM describe_entity(label=t1.lexical_label_2, location=t1.lexical_label_3, relation=on) -> describe_entity_2 : TERM # PROPOSED: S1
    TERM describe_turn(direction="around") -> describe_turn_3 : TERM # PROPOSED: S2
    TERM describe_walk(direction="forward", steps=1) -> describe_walk_3 : TERM # PROPOSED: S2
    TERM describe_face(target=describe_entity_2) -> describe_face_3 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_turn_3, describe_walk_3, describe_face_3]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    TERM describe_slice(target=describe_entity_2) -> describe_slice_2 : TERM # PROPOSED: S2
    UTTER propose(target=describe_slice_2)
    TERM describe_face(target=t1.lexical_label_3) -> describe_face_4 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_turn_3, describe_walk_3, describe_face_4]) -> sequence_4 : TERM
    UTTER propose(target=sequence_4)
    TERM describe_place(target=lexical_label_3, destination=t1.lexical_label_3, relation=on) -> describe_place_2 : TERM # PROPOSED: S2
    UTTER propose(target=describe_place_2)
    UTTER propose(target=sequence_3)
    TERM describe_entity(label=t1.lexical_label_2, location=t1.lexical_label_3, portion=TRUE, quantity=1, relation=on, state=state_sliced) -> describe_entity_3 : TERM # PROPOSED: S1
    TERM describe_pick_up(target=describe_entity_3, source=t1.lexical_label_3) -> describe_pick_up_3 : TERM # PROPOSED: S2
    UTTER propose(target=describe_pick_up_3)
    TERM describe_face(target=lexical_label_4) -> describe_face_5 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_turn_3, describe_walk_3, describe_face_5]) -> sequence_5 : TERM
    UTTER propose(target=sequence_5)
    TERM describe_chill(target=describe_entity_3, destination=lexical_label_4) -> describe_chill_2 : TERM # PROPOSED: S2
    TERM describe_remove(target=describe_entity_3, source=lexical_label_4) -> describe_remove_2 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_chill_2, describe_remove_2]) -> sequence_6 : TERM
    UTTER propose(target=sequence_6)
    TERM describe_walk(direction="left", steps=1) -> describe_walk_4 : TERM # PROPOSED: S2
    TERM sequence(items=[describe_walk_4, describe_face_4]) -> sequence_7 : TERM
    UTTER propose(target=sequence_7)
    TERM spatial_constraint(object=t1.lexical_label_3, reference=lexical_label_2, relation=right_of) -> spatial_constraint_2 : TERM
    TERM describe_place(target=describe_entity_3, destination=t1.lexical_label_3, relation=on) -> describe_place_3 : TERM # PROPOSED: S2
    UTTER propose(target=describe_place_3, constraints=[spatial_constraint_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | describe_chill, sequence, request (S2) | proposed |
| n2 | object | food_label::lettuce, describe_entity, state_sliced (S1) | proposed |
| n3 | action | describe_place, on (S2) | proposed |
| n4 | object | object_label::counter, lexical_label | label-preserved |
| n5 | action | describe_turn, describe_walk, describe_face, sequence (S2) | proposed |
| n6 | object | object_label::sink, lexical_label | label-preserved |
| n7 | action | describe_pick_up (S2) | proposed |
| n8 | object | object_label::knife, lexical_label | label-preserved |
| n9 | action | describe_turn, describe_walk, describe_face, describe_entity (S1, S2) | proposed |
| n10 | object | food_label::lettuce, lexical_label | label-preserved |
| n11 | action | describe_slice, describe_entity (S1, S2) | proposed |
| n12 | action | describe_turn, describe_walk, describe_face (S2) | proposed |
| n13 | action | describe_place, on (S2) | proposed |
| n14 | action | describe_turn, describe_walk, describe_face, describe_entity (S1, S2) | proposed |
| n15 | action | describe_pick_up, describe_entity, state_sliced (S1, S2) | proposed |
| n16 | action | describe_turn, describe_walk, describe_face (S2) | proposed |
| n17 | object | object_label::fridge, lexical_label | label-preserved |
| n18 | action | describe_chill, describe_remove, sequence (S2) | proposed |
| n19 | action | describe_walk, describe_face, sequence (S2) | proposed |
| n20 | action | describe_place, spatial_constraint, on, right_of (S2) | proposed |

## Why the translation failed

- n1, n3, n7, n11, n13, n15, n18, n20: widened each supplied need text; additionally searched "nonexecuting description pick up chill slice place physical procedure". Closest entries are executable `chill`, `place`, `pick_up`, `slice`, `remove`. These do not construct TERM action descriptions. The source is a requested goal followed by an imperative plan, not evidence of completed actions, so RECORD is false and bare ACTION is illegal here. S2 supplies non-executing descriptions.
- n5, n9, n12, n14, n16, n19: widened each distinct supplied motion need text (the identical n9/n14 wording was searched once); searched "step forward left turn around single step" and "direction left forward around single step". Closest entries `turn`, `walk`, `face`, `walk_backward` are operations; `walk` additionally lacks step count and across-room traversal, and `walk_backward` has the wrong direction. S2 preserves all motion details as terms.
- n2 and the entity qualifiers in n9, n11, n14, n15: widened "lettuce slice object description"; searched "object description with sliced state and spatial location", "entity description state quantity location", and "describe object with state and location". `state_sliced` is a condition value, not a constructor. `has_state` and `spatial_state` are claims; `location_spec` is geographical; `lexical_label` deliberately adds no properties. `spatial_constraint` can express a relation but does not construct the qualified physical target. S1 supplies a non-asserting selection description, including a single sliced portion.
- S2 is a family of reusable primitive descriptive constructors, not newly inferred events. Existing `activity` is close but its present roles cannot preserve direction, steps, source, destination, traversal, and distinct placement relations. Its verb argument also has no reviewed physical-action profile that could safely supply those meanings.

## Translation report

- Pinned release: spec 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation; user goal followed by an agent's twelve-step proposed procedure.
- Coverage status: partial under the current release; suggested document requires S1 and S2 acceptance and a new pinned glossary revision.
- Source-span coverage: t1:s1 is represented as a request; t2:s2, s4, s6, s8, s10, s12, s14, s16, s18, s20, s22, s24 map in order to the twelve UTTER statements. Odd-numbered t2 spans are list numbering, represented by ordered speech acts, not invented messages or events.
- Opaque-text spans: none.
- Label-preserved spans: t1:s1 and t2:s6/s8/s14/s16/s20/s24 lettuce → food_label::lettuce; t1:s1 and t2:s6/s8/s10/s12/s14/s16/s22/s24 counter → object_label::counter; t2:s2/s4/s24 sink → object_label::sink; t2:s4/s12 knife → object_label::knife; t2:s18/s20 fridge → object_label::fridge; t2:s2 room → object_label::room. These preserve source kind labels, not inferred properties. S1 separately supplies explicit slice and location qualifiers.
- Missing constructs: S1 qualified physical entity/portion description; S2 non-executing physical-action description family with motion parameters.
- Unresolved ambiguities: no execution outcome is supplied; the agent text is encoded as a proposal, not success. The viewpoint for "right of the sink" is unspecified and retained without choosing an absolute coordinate frame. No chilling resource is invented for t1; the fridge is introduced only in t2. The final counter landmark is constrained to the right of the sink; no numeric distance is supplied.
- Proposed glossary/spec changes: S1 and S2 in suggestions.md; no grammar change.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported 0 unresolved candidate-matching needs and 9 unknown symbols: describe_chill, describe_entity, describe_face, describe_pick_up, describe_place, describe_remove, describe_slice, describe_turn, describe_walk. Its candidate matches do not establish semantic coverage; all nine unknown constructors are explicitly proposed under S1/S2, so this remains a failed translation.
