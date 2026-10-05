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
    TERM qualified_entity(base=lexical_label_2, constraints=[spatial_constraint_2]) -> qualified_entity_2 : TERM # PROPOSED: S2
    TERM described_place(target=qualified_entity_2, destination=lexical_label_4, relation=on) -> described_place_2 : TERM # PROPOSED: S1
    CLAIM request(target=described_place_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM lexical_label(value=color_label::black) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    TERM qualified_entity(base=t1.lexical_label_4, constraints=[requirement_2]) -> qualified_entity_2 : TERM # PROPOSED: S2
    TERM described_walk(direction=motion_forward) -> described_walk_2 : TERM # PROPOSED: S3, S6
    TERM described_turn(target=qualified_entity_2, direction=motion_left) -> described_turn_2 : TERM # PROPOSED: S4, S6
    TERM sequence(items=[described_walk_2, described_turn_2]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)

    TERM lexical_label(value=food_label::lettuce) -> lexical_label_3 : TERM
    TERM spatial_constraint(object=t1.lexical_label_3, reference=lexical_label_3, relation=next_to) -> spatial_constraint_2 : TERM
    TERM qualified_entity(base=t1.lexical_label_3, constraints=[spatial_constraint_2]) -> qualified_entity_3 : TERM # PROPOSED: S2
    TERM described_pick_up(target=qualified_entity_3) -> described_pick_up_2 : TERM # PROPOSED: S5
    UTTER propose(target=described_pick_up_2, content="Pick up the knife next to the lettuce that is closest.")

    TERM described_turn(direction=motion_around) -> described_turn_3 : TERM # PROPOSED: S4, S6
    TERM lexical_label(value=object_label::stove) -> lexical_label_4 : TERM
    TERM spatial_region(side=region_top, whole=lexical_label_4) -> spatial_region_2 : TERM # PROPOSED: S7, S6
    TERM spatial_region(side=region_left) -> spatial_region_3 : TERM # PROPOSED: S7, S6
    TERM spatial_constraint(object=spatial_region_2, reference=spatial_region_3, relation=in) -> spatial_constraint_3 : TERM
    TERM qualified_entity(base=spatial_region_2, constraints=[spatial_constraint_3]) -> qualified_entity_4 : TERM # PROPOSED: S2
    TERM described_walk(destination=qualified_entity_4) -> described_walk_3 : TERM # PROPOSED: S3
    TERM sequence(items=[described_turn_3, described_walk_3]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)

    TERM lexical_label(value=object_label::burner) -> lexical_label_5 : TERM
    TERM spatial_region(side=region_left, whole=lexical_label_4) -> spatial_region_4 : TERM # PROPOSED: S7, S6
    TERM spatial_region(side=region_back, whole=lexical_label_4) -> spatial_region_5 : TERM # PROPOSED: S7, S6
    TERM spatial_constraint(object=lexical_label_5, reference=spatial_region_4, relation=in) -> spatial_constraint_4 : TERM
    TERM spatial_constraint(object=lexical_label_5, reference=spatial_region_5, relation=in) -> spatial_constraint_5 : TERM
    TERM qualified_entity(base=lexical_label_5, constraints=[spatial_constraint_4, spatial_constraint_5]) -> qualified_entity_5 : TERM # PROPOSED: S2
    TERM spatial_constraint(object=t1.lexical_label_2, reference=qualified_entity_5, relation=on) -> spatial_constraint_6 : TERM
    TERM qualified_entity(base=t1.lexical_label_2, constraints=[spatial_constraint_6]) -> qualified_entity_6 : TERM # PROPOSED: S2
    TERM described_place(target=qualified_entity_3, destination=qualified_entity_6, relation=in) -> described_place_2 : TERM # PROPOSED: S1
    UTTER propose(target=described_place_2)

    TERM described_pick_up(target=qualified_entity_6, source=spatial_region_2) -> described_pick_up_3 : TERM # PROPOSED: S5
    UTTER propose(target=described_pick_up_3)

    TERM described_turn(direction=motion_left) -> described_turn_4 : TERM # PROPOSED: S4, S6
    TERM lexical_label(value=object_label::safe) -> lexical_label_6 : TERM
    TERM described_walk(destination=lexical_label_6) -> described_walk_4 : TERM # PROPOSED: S3
    TERM described_turn(target=qualified_entity_2, direction=motion_left) -> described_turn_5 : TERM # PROPOSED: S4, S6
    TERM sequence(items=[described_turn_4, described_walk_4, described_turn_5]) -> sequence_4 : TERM
    UTTER propose(target=sequence_4)

    TERM spatial_region(side=region_left, whole=qualified_entity_2) -> spatial_region_6 : TERM # PROPOSED: S7, S6
    TERM spatial_constraint(object=qualified_entity_6, reference=spatial_region_6, relation=in) -> spatial_constraint_7 : TERM
    TERM spatial_constraint(object=lexical_label_3, reference=qualified_entity_6, relation=under) -> spatial_constraint_8 : TERM
    TERM described_place(target=qualified_entity_6, constraints=[spatial_constraint_7, spatial_constraint_8], destination=qualified_entity_2, relation=on) -> described_place_3 : TERM # PROPOSED: S1
    UTTER propose(target=described_place_3)
    TERM sequence(items=[sequence_2, described_pick_up_2, sequence_3, described_place_2, described_pick_up_3, sequence_4, described_place_3]) -> sequence_5 : TERM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, described_place (S1), qualified_entity (S2) | proposed |
| n2 | action | described_place (S1) | proposed |
| n3 | object | object_label::pan, lexical_label | label-preserved |
| n4 | object | object_label::knife, lexical_label | label-preserved |
| n5 | object | object_label::table, lexical_label | label-preserved |
| n6 | constraint | spatial_constraint, in, qualified_entity (S2) | proposed |
| n7 | action | described_walk (S3), motion_forward (S6) | proposed |
| n8 | temporal | sequence | covered |
| n9 | action | described_turn (S4), motion_left (S6) | proposed |
| n10 | object | object_label::table, lexical_label | label-preserved |
| n11 | constraint | color_label::black, lexical_label, requirement, qualified_entity (S2) | proposed |
| n12 | action | described_pick_up (S5) | proposed |
| n13 | object | object_label::knife, lexical_label | label-preserved |
| n14 | object | food_label::lettuce, lexical_label | label-preserved |
| n15 | constraint | spatial_constraint, next_to, qualified_entity (S2) | proposed |
| n16 | constraint | UTTER propose content fallback | opaque |
| n17 | action | described_turn (S4), motion_around (S6) | proposed |
| n18 | action | described_walk (S3), spatial_region (S7) | proposed |
| n19 | object | object_label::stove, lexical_label, spatial_region (S7), region_top (S6) | proposed |
| n20 | constraint | spatial_constraint, in, spatial_region (S7), region_left (S6), qualified_entity (S2) | proposed |
| n21 | action | described_place (S1), in | proposed |
| n22 | object | object_label::knife, lexical_label | label-preserved |
| n23 | object | object_label::pan, lexical_label | label-preserved |
| n24 | object | object_label::burner, lexical_label | label-preserved |
| n25 | constraint | spatial_constraint, on, in, qualified_entity (S2), spatial_region (S7), region_left, region_back (S6) | proposed |
| n26 | action | described_pick_up (S5), spatial_region (S7) | proposed |
| n27 | object | object_label::pan, lexical_label | label-preserved |
| n28 | object | object_label::stove, lexical_label, spatial_region (S7), region_top (S6) | proposed |
| n29 | action | described_turn (S4), motion_left (S6) | proposed |
| n30 | action | described_walk (S3) | proposed |
| n31 | object | object_label::safe, lexical_label | label-preserved |
| n32 | action | described_turn (S4), motion_left (S6) | proposed |
| n33 | object | object_label::table, lexical_label, color_label::black, requirement, qualified_entity (S2) | proposed |
| n34 | action | described_place (S1), on | proposed |
| n35 | object | object_label::pan, lexical_label | label-preserved |
| n36 | object | object_label::table, lexical_label | label-preserved |
| n37 | object | food_label::lettuce, lexical_label | label-preserved |
| n38 | constraint | spatial_constraint, in, spatial_region (S7), region_left (S6) | proposed |
| n39 | constraint | spatial_constraint, under | covered |

## Why the translation failed

- n1, n2, n21, n34: search "description object spatial relation containing knife pan" and widen "description of requested placement operation with destination and spatial constraints" returned place, spatial_constraint, request and activity. place is executable/recordable, not a TERM description of an instruction; RECORD would falsely claim occurrence. activity lacks destination/relation roles. S1 supplies the description.
- n6, n11, n15, n33: search "entity description qualifier color constraints" and "qualified entity constraints description" plus widen "pan containing the knife qualified object description" returned requirement, lexical_label, include and conjunction. These describe requirements or components, but do not select the base entity subject to those requirements. S2 supplies that role. n20 and n25 also need S2 to attach spatial identification constraints.
- n7, n18, n30: search "walk forward turn left direction" and "move action described target destination source direction"; widen "walk forward turn left towards black table described instructions" and "turn around go stove top on left" returned walk and walk_backward. walk requires a destination and is not a descriptive constructor; activity.location is not a motion destination and accepts neither the needed TERM destination nor direction. S3 supplies the description.
- n9, n17, n29, n32: search "turning body description" and the motion searches/widens above returned turn and face. Neither constructs a TERM instruction with both turning direction and intended facing target. S4 supplies it.
- n12, n26: search "action description operation arguments" and widen "described pick up knife take pan from stove" returned activity, pick_up and remove. activity lacks a source role; pick_up cannot describe the planned selection using the required TERM qualifiers. S5 supplies a nonexecuting description, not an acquisition event.
- n7, n9, n17, n20, n25, n29, n32, n38: search "forward left around direction" and widen "motion direction forward left turn around and spatial side top rear" returned left_of, behind, other_side_of and turn. Binary spatial relations are not motion-direction values or regions within a whole. S6 supplies governed direction/region selectors, not opaque labels.
- n19, n20, n25, n28, n38: search "left side part back burner" and "part whole spatial top left region"; widen "back left burner left side of table above lettuce" returned left_of, behind, on and other_side_of. Left of the table is not its left-side region; a rear-left burner needs subregions of the stove. S7 supplies regions, including the stove's top.
- n16: search "nearest knife next to lettuce" and "nearest constraint reference distance"; widen "closest knife next to lettuce selection" returned rank_distance and search-ranking attributes. Those do not express the attachment/reference of a closest-object selection inside this described pickup. The source also leaves whether the knife or lettuce is closest, and to what, unresolved. Exact wording is retained as opaque content rather than guessed.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation; one user message and one agent message containing seven numbered instructions.
- Coverage status: partial; this is a noncanonical suggested document pending S1–S7, with an opaque closest-selection span even after acceptance.
- Source-span coverage: t1:s1 and substantive spans t2:s2, s4, s6, s8, s10, s12, s14 are represented; ordinal markers t2:s1, s3, s5, s7, s9, s11, s13 are represented by source order and sequence_5. The imperatives are recommendations/instructions, not observed operations. No success events or results are invented.
- Opaque-text spans: t2:s4, specifically "that is closest"; its full sentence is retained in UTTER content for attachment audit. No other content fallback.
- Label-preserved spans: t1:s1 pan/knife/table; t2:s2 table/black; t2:s4 knife/lettuce; t2:s6 stove; t2:s8 knife/pan/burner; t2:s10 pan/stove; t2:s12 safe/table/black; t2:s14 pan/table/lettuce. Their kind/color words remain open labels; no physical properties or extra senses are inferred.
- Missing constructs: S1 described_place; S2 qualified_entity; S3 described_walk; S4 described_turn; S5 described_pick_up; S6 governed motion/region values; S7 spatial_region. Closest selection remains opaque. Proposals are not accepted vocabulary.
- Unresolved ambiguities: t2:s4 closest may modify knife or lettuce and supplies no explicit distance reference; t2:s6 contextual left, t2:s8 rear/left orientation, and t2:s14 left/above require the source's spatial frame, not an invented compass orientation. under with reversed arguments preserves the stated above relation but does not resolve whether the scene uses a vertical or image-plane axis. A left turn is not assigned an invented angle. The proposed region without a whole preserves the implicit contextual frame.
- Proposed glossary/spec changes: S1–S7 in /output/suggestions.md; no grammar or type changes.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported six unknown constructor symbols (described_pick_up, described_place, described_turn, described_walk, qualified_entity, spatial_region) and six unbound proposed selector values (motion_around, motion_forward, motion_left, region_back, region_left, region_top). All are addressed by S1–S7. It flagged n11 as label-only; the suggested qualified color selection remains proposal-dependent. It listed no unresolved needs, but its candidate-overlap matches do not establish semantic coverage: the table above explicitly records the genuine proposed and opaque gaps.
