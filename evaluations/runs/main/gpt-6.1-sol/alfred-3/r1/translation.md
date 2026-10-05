Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=object_label::pan) -> lexical_label_2 : TERM
    TERM lexical_label(value=object_label::knife) -> lexical_label_3 : TERM
    TERM lexical_label(value=object_label::table) -> lexical_label_4 : TERM
    TERM spatial_constraint(object=lexical_label_3, reference=lexical_label_2, relation=in) -> spatial_constraint_2 : TERM
    TERM restrict_entity(base=lexical_label_2, constraints=[spatial_constraint_2]) -> restrict_entity_2 : TERM # PROPOSED: S2
    TERM describe_place(target=restrict_entity_2, destination=lexical_label_4, relation=on) -> describe_place_2 : TERM # PROPOSED: S1
    CLAIM request(target=describe_place_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM lexical_label(value=color_label::black) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    TERM restrict_entity(base=t1.lexical_label_4, constraints=[requirement_2]) -> restrict_entity_2 : TERM # PROPOSED: S2
    TERM describe_walk(direction=orientation_forward) -> describe_walk_2 : TERM # PROPOSED: S1, S4
    TERM describe_turn(direction=orientation_left, facing=restrict_entity_2) -> describe_turn_2 : TERM # PROPOSED: S1, S4
    TERM sequence(items=[describe_walk_2, describe_turn_2]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM lexical_label(value=food_label::lettuce) -> lexical_label_3 : TERM
    TERM spatial_constraint(object=t1.lexical_label_3, reference=lexical_label_3, relation=next_to) -> spatial_constraint_2 : TERM
    TERM restrict_entity(base=t1.lexical_label_3, constraints=[spatial_constraint_2]) -> restrict_entity_3 : TERM # PROPOSED: S2
    TERM describe_pick_up(target=restrict_entity_3) -> describe_pick_up_2 : TERM # PROPOSED: S1
    UTTER propose(target=describe_pick_up_2, content="Pick up the knife next to the lettuce that is closest.")
    TERM lexical_label(value=object_label::stove) -> lexical_label_4 : TERM
    TERM top_surface(entity=lexical_label_4) -> top_surface_2 : TERM # PROPOSED: S3
    TERM requirement(property="relative_side", value=orientation_left) -> requirement_3 : TERM # PROPOSED: S4
    TERM restrict_entity(base=top_surface_2, constraints=[requirement_3]) -> restrict_entity_4 : TERM # PROPOSED: S2
    TERM describe_turn(direction=orientation_around) -> describe_turn_3 : TERM # PROPOSED: S1, S4
    TERM describe_walk(destination=restrict_entity_4) -> describe_walk_3 : TERM # PROPOSED: S1
    TERM sequence(items=[describe_turn_3, describe_walk_3]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    TERM lexical_label(value=object_label::burner) -> lexical_label_5 : TERM
    TERM left_region(entity=top_surface_2) -> left_region_2 : TERM # PROPOSED: S3
    TERM rear_region(entity=left_region_2) -> rear_region_2 : TERM # PROPOSED: S3
    TERM spatial_constraint(object=lexical_label_5, reference=rear_region_2, relation=in) -> spatial_constraint_3 : TERM
    TERM restrict_entity(base=lexical_label_5, constraints=[spatial_constraint_3]) -> restrict_entity_5 : TERM # PROPOSED: S2
    TERM spatial_constraint(object=t1.lexical_label_2, reference=restrict_entity_5, relation=on) -> spatial_constraint_4 : TERM
    TERM restrict_entity(base=t1.lexical_label_2, constraints=[spatial_constraint_4]) -> restrict_entity_6 : TERM # PROPOSED: S2
    TERM describe_place(target=restrict_entity_3, destination=restrict_entity_6, relation=in) -> describe_place_2 : TERM # PROPOSED: S1
    UTTER propose(target=describe_place_2)
    TERM describe_pick_up(target=restrict_entity_6, source=top_surface_2) -> describe_pick_up_3 : TERM # PROPOSED: S1
    UTTER propose(target=describe_pick_up_3)
    TERM lexical_label(value=object_label::safe) -> lexical_label_6 : TERM
    TERM describe_turn(direction=orientation_left) -> describe_turn_4 : TERM # PROPOSED: S1, S4
    TERM describe_walk(destination=lexical_label_6) -> describe_walk_4 : TERM # PROPOSED: S1
    TERM describe_turn(direction=orientation_left, facing=restrict_entity_2) -> describe_turn_5 : TERM # PROPOSED: S1, S4
    TERM sequence(items=[describe_turn_4, describe_walk_4, describe_turn_5]) -> sequence_4 : TERM
    UTTER propose(target=sequence_4)
    TERM left_region(entity=restrict_entity_2) -> left_region_3 : TERM # PROPOSED: S3
    TERM spatial_constraint(object=t1.lexical_label_2, reference=left_region_3, relation=on) -> spatial_constraint_5 : TERM
    TERM spatial_constraint(object=lexical_label_3, reference=t1.lexical_label_2, relation=under) -> spatial_constraint_6 : TERM
    TERM describe_place(target=restrict_entity_6, constraints=[spatial_constraint_5, spatial_constraint_6], destination=restrict_entity_2, relation=on) -> describe_place_3 : TERM # PROPOSED: S1
    UTTER propose(target=describe_place_3)
    TERM sequence(items=[sequence_2, describe_pick_up_2, sequence_3, describe_place_2, describe_pick_up_3, sequence_4, describe_place_3]) -> sequence_5 : TERM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, describe_place (S1) | proposed |
| n2 | action | describe_place (S1), on | proposed |
| n3 | object | object_label::pan | label-preserved |
| n4 | object | object_label::knife | label-preserved |
| n5 | object | object_label::table | label-preserved |
| n6 | constraint | spatial_constraint, in, restrict_entity (S2) | proposed |
| n7 | action | describe_walk (S1), orientation_forward (S4) | proposed |
| n8 | temporal | sequence | covered |
| n9 | action | describe_turn (S1), orientation_left (S4) | proposed |
| n10 | object | object_label::table | label-preserved |
| n11 | constraint | color_label::black, lexical_label, requirement, restrict_entity (S2) | proposed |
| n12 | action | describe_pick_up (S1) | proposed |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | food_label::lettuce | label-preserved |
| n15 | constraint | spatial_constraint, next_to, restrict_entity (S2) | proposed |
| n16 | constraint | UTTER content fallback | opaque |
| n17 | action | describe_turn (S1), orientation_around (S4) | proposed |
| n18 | action | describe_walk (S1), top_surface (S3) | proposed |
| n19 | object | object_label::stove, top_surface (S3) | proposed |
| n20 | constraint | requirement, orientation_left (S4), restrict_entity (S2) | proposed |
| n21 | action | describe_place (S1), in | proposed |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | object_label::pan | label-preserved |
| n24 | object | object_label::burner | label-preserved |
| n25 | constraint | left_region, rear_region (S3), spatial_constraint, on, in, restrict_entity (S2) | proposed |
| n26 | action | describe_pick_up (S1), top_surface (S3) | proposed |
| n27 | object | object_label::pan | label-preserved |
| n28 | object | object_label::stove, top_surface (S3) | proposed |
| n29 | action | describe_turn (S1), orientation_left (S4) | proposed |
| n30 | action | describe_walk (S1) | proposed |
| n31 | object | object_label::safe | label-preserved |
| n32 | action | describe_turn (S1), orientation_left (S4) | proposed |
| n33 | object | object_label::table, requirement, restrict_entity (S2) | proposed |
| n34 | action | describe_place (S1) | proposed |
| n35 | object | object_label::pan | label-preserved |
| n36 | object | object_label::table | label-preserved |
| n37 | object | food_label::lettuce | label-preserved |
| n38 | constraint | left_region (S3), spatial_constraint, on | proposed |
| n39 | constraint | spatial_constraint, under (inverse arguments) | covered |

## Why the translation failed

- n1, n2, n7, n9, n12, n17, n18, n21, n26, n29, n30, n32, n34: search "description physical operation arguments destination direction" and widen each action need returned executable operations and activity. RECORD would falsely claim these imperative plan steps occurred; activity lacks destination, source, direction and governed operation-description meanings. S1 supplies descriptive constructors, not execution.
- n6, n11, n15, n20, n25, n33: search "entity description qualified by constraints color" and widen "qualify entity using spatial and color constraints" returned requirement, lexical_label and spatial_constraint, but nothing binds those restrictions to the selected entity. S2 supplies this missing composition. Related action needs depend on that selection.
- n19, n25, n28, n38 (also n18/n26): search "left region rear burner part" / "upper surface part of object" and widen "top surface and left or rear region of an object" returned table, counter, left_of, behind, other_side_of. Whole objects and relative positions do not denote an object's top surface or internal regions. S3 supplies these descriptions.
- n7, n9, n17, n20, n29, n32: search "direction forward left around" and widen "forward left around direction values" returned turn, walk_backward, left_of and behind. Directions were not admitted values; left_of is a binary positional relation, not a turn or movement direction. S4 supplies defined orientation values.
- n16: search "closest object selection relative distance" / "nearest selection descriptor" and widen "closest one" / "nearest entity description ambiguous closest knife or lettuce" returned rank_distance, sort and search_web. These are runtime/search ranking vocabulary, not a scoped nearest physical-object description. Moreover, "that is closest" may qualify knife or lettuce, and the distance reference is unstated. Preserve the phrase opaquely rather than invent selection scope. No new symbol is used for it.

## Translation report

- Pinned release: spec 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation; user command followed by an agent's seven-step imperative plan, not observations of completed actions.
- Coverage status: partial; suggested document depends on S1–S4 and retains the closest-selection phrase opaquely.
- Source-span coverage: t1:s1 and substantive t2:s2, s4, s6, s8, s10, s12, s14 represented in order; t2:s1, s3, s5, s7, s9, s11, s13 are step numbering, reflected by ordered speech acts, not invented turns or events.
- Opaque-text spans: t2:s4, specifically "that is closest"; full sentence retained in UTTER content to preserve attachment ambiguity. The target independently formalizes pickup and adjacency.
- Label-preserved spans: pan/knife/table in t1:s1; table/black in t2:s2; knife/lettuce in t2:s4; stove in t2:s6; knife/pan/burner in t2:s8; pan/stove in t2:s10; safe/table/black in t2:s12; pan/table/lettuce in t2:s14. Labels alone resolve no dictionary sense; color, containment, spatial qualifiers and top-surface relations are represented separately where possible.
- Missing constructs: S1 described physical operations; S2 restriction-bearing entity descriptions; S3 object surfaces and internal regions; S4 orientation values; scoped physical proximity selection remains opaque.
- Unresolved ambiguities: closest-selection scope and reference at t2:s4; viewpoint for left/back at t2:s6, s8, s14; "above the lettuce" may be vertical or viewer-relative layout. Inverse under preserves the qualitative spatial relation, not a metric or chosen coordinate system. Suggested terms leave frames unspecified. Pan/knife/table handles describe discourse referents, not acquired runtime identities. The user's table is not independently asserted black: that qualifier is in the agent's plan only.
- Proposed glossary/spec changes: S1–S4 in suggestions.md; no grammar change. These proposals are not accepted vocabulary and this is not a canonical valid translation under the pinned release.
- Check: `rag check` reported 0 lexically unresolved needs, 8 unknown constructor symbols (describe_pick_up, describe_place, describe_turn, describe_walk, left_region, rear_region, restrict_entity, top_surface), and 3 unbound values (orientation_around, orientation_forward, orientation_left); all are explicit S1–S4 proposals. It flagged n11 as label-only. Its candidate-overlap heuristic also marked n16 OK despite the semantic proximity gap; the coverage table correctly retains n16 as opaque. No retired bare values, invalid group values, or quoted entities are used. This is not a parser or semantic-fidelity pass.
