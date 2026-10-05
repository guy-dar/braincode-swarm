Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=object_label::knife) -> lexical_label_2 : TERM
    TERM lexical_label(value=object_label::pan) -> lexical_label_3 : TERM
    TERM lexical_label(value=object_label::table) -> lexical_label_4 : TERM
    TERM describe_entity(base=lexical_label_3, contains=lexical_label_2) -> describe_entity_2 : TERM # PROPOSED: S2
    TERM describe_place(target=describe_entity_2, destination=lexical_label_4, relation=on) -> describe_place_2 : TERM # PROPOSED: S1
    CLAIM request(target=describe_place_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM describe_entity(base=t1.lexical_label_4, color=color_label::black) -> describe_entity_2 : TERM # PROPOSED: S2
    TERM describe_walk(forward=TRUE) -> describe_walk_2 : TERM # PROPOSED: S1
    TERM describe_turn(left=TRUE, toward=describe_entity_2) -> describe_turn_2 : TERM # PROPOSED: S1
    TERM sequence(items=[describe_walk_2, describe_turn_2]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM lexical_label(value=food_label::lettuce) -> lexical_label_2 : TERM
    TERM describe_entity(base=t1.lexical_label_2, next_to=lexical_label_2) -> describe_entity_3 : TERM # PROPOSED: S2
    TERM closest_constraint() -> closest_constraint_2 : TERM # PROPOSED: S4
    TERM describe_acquire(target=describe_entity_3) -> describe_acquire_2 : TERM # PROPOSED: S1
    UTTER propose(target=describe_acquire_2, constraints=[closest_constraint_2])
    TERM describe_turn(around=TRUE) -> describe_turn_3 : TERM # PROPOSED: S1
    TERM lexical_label(value=object_label::stove) -> lexical_label_3 : TERM
    TERM spatial_region(left=TRUE) -> spatial_region_2 : TERM # PROPOSED: S3
    TERM describe_entity(base=lexical_label_3, region=spatial_region_2) -> describe_entity_4 : TERM # PROPOSED: S2
    TERM spatial_region(reference=describe_entity_4, surface=TRUE) -> spatial_region_3 : TERM # PROPOSED: S3
    TERM describe_walk(destination=spatial_region_3) -> describe_walk_3 : TERM # PROPOSED: S1
    TERM sequence(items=[describe_turn_3, describe_walk_3]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    TERM lexical_label(value=object_label::burner) -> lexical_label_4 : TERM
    TERM spatial_region(back=TRUE, left=TRUE, reference=spatial_region_3) -> spatial_region_4 : TERM # PROPOSED: S3
    TERM describe_entity(base=lexical_label_4, region=spatial_region_4) -> describe_entity_5 : TERM # PROPOSED: S2
    TERM describe_entity(base=t1.lexical_label_3, on=describe_entity_5) -> describe_entity_6 : TERM # PROPOSED: S2
    TERM describe_place(target=describe_entity_3, destination=describe_entity_6, relation=in) -> describe_place_2 : TERM # PROPOSED: S1
    UTTER propose(target=describe_place_2)
    TERM describe_acquire(target=describe_entity_6, source=spatial_region_3) -> describe_acquire_3 : TERM # PROPOSED: S1
    UTTER propose(target=describe_acquire_3)
    TERM describe_turn(left=TRUE) -> describe_turn_4 : TERM # PROPOSED: S1
    TERM lexical_label(value=object_label::safe) -> lexical_label_5 : TERM
    TERM describe_walk(destination=lexical_label_5) -> describe_walk_4 : TERM # PROPOSED: S1
    TERM describe_turn(facing=describe_entity_2, left=TRUE) -> describe_turn_5 : TERM # PROPOSED: S1
    TERM sequence(items=[describe_turn_4, describe_walk_4, describe_turn_5]) -> sequence_4 : TERM
    UTTER propose(target=sequence_4)
    TERM spatial_region(left=TRUE, reference=describe_entity_2) -> spatial_region_5 : TERM # PROPOSED: S3
    TERM spatial_constraint(object=lexical_label_2, reference=describe_entity_6, relation=under) -> spatial_constraint_2 : TERM
    TERM describe_place(target=describe_entity_6, destination=spatial_region_5, relation=on) -> describe_place_3 : TERM # PROPOSED: S1
    UTTER propose(target=describe_place_3, constraints=[spatial_constraint_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, describe_place (S1) | proposed |
| n2 | action | describe_place (S1), on | proposed |
| n3 | object | object_label::pan, lexical_label | label-preserved |
| n4 | object | object_label::knife, lexical_label | label-preserved |
| n5 | object | object_label::table, lexical_label | label-preserved |
| n6 | constraint | describe_entity.contains (S2) | proposed |
| n7 | action | describe_walk.forward (S1) | proposed |
| n8 | temporal | sequence | covered |
| n9 | action | describe_turn.left/toward (S1) | proposed |
| n10 | object | object_label::table, lexical_label | label-preserved |
| n11 | constraint | describe_entity.color (S2), color_label::black | proposed |
| n12 | action | describe_acquire (S1) | proposed |
| n13 | object | object_label::knife, lexical_label | label-preserved |
| n14 | object | food_label::lettuce, lexical_label | label-preserved |
| n15 | constraint | describe_entity.next_to (S2) | proposed |
| n16 | constraint | closest_constraint (S4) | proposed |
| n17 | action | describe_turn.around (S1) | proposed |
| n18 | action | describe_walk (S1), spatial_region.surface (S3) | proposed |
| n19 | object | object_label::stove, spatial_region.surface (S3) | proposed |
| n20 | constraint | spatial_region.left (S3), describe_entity.region (S2) | proposed |
| n21 | action | describe_place (S1), in | proposed |
| n22 | object | object_label::knife, lexical_label | label-preserved |
| n23 | object | object_label::pan, lexical_label | label-preserved |
| n24 | object | object_label::burner, lexical_label | label-preserved |
| n25 | constraint | spatial_region.back/left (S3), describe_entity.on/region (S2) | proposed |
| n26 | action | describe_acquire.source (S1) | proposed |
| n27 | object | object_label::pan, lexical_label | label-preserved |
| n28 | object | object_label::stove, spatial_region.surface (S3) | proposed |
| n29 | action | describe_turn.left (S1) | proposed |
| n30 | action | describe_walk (S1) | proposed |
| n31 | object | object_label::safe, lexical_label | label-preserved |
| n32 | action | describe_turn.left/facing (S1) | proposed |
| n33 | object | object_label::table, describe_entity.color (S2) | proposed |
| n34 | action | describe_place (S1), on | proposed |
| n35 | object | object_label::pan, lexical_label | label-preserved |
| n36 | object | object_label::table, lexical_label | label-preserved |
| n37 | object | food_label::lettuce, lexical_label | label-preserved |
| n38 | constraint | spatial_region.left/reference (S3) | proposed |
| n39 | constraint | spatial_constraint, under (lettuce beneath pan) | covered |

## Why the translation failed

- n1, n2, n7, n9, n12, n17, n18, n21, n26, n29, n30, n32, n34: S1 supplies missing non-executing action descriptions with explicit roles. Searches `description of requested place action with destination and relation`, `ordered procedure action descriptions`, and `described action destination direction source`; widening each original need plus `described place action target destination relation`, `described pickup target source`, `described walk forward and turn left around facing a target` returned executable place/pick_up/walk/turn/face and generic activity. RECORD would falsely claim occurrence; activity lacks destination/source/direction roles and does not admit operation symbols as verb values. request already describes the user's communicative request, so no command speech-act addition is needed.
- n6, n11, n15, n20, n25, n33: S2 supplies entity qualification, not additional nouns. Searches `entity description spatial containment color nearest`, `object description qualifiers nearest color`; widening each original qualifier need and `object description with color containing adjacent and location qualifiers` found lexical_label, color_label, spatial_constraint and geographical location_spec. None constructs a referent qualified by these restrictions. Spatial constraints alone are not object descriptions; color_label supplies no subject/color relationship.
- n18, n19, n20, n25, n28, n38: S3 supplies object-relative surface and subregion descriptions. Searches `surface part side burner back left`, `object surface left back region`; widening each original need and `surface and left back region of an object` returned table, left_of, behind and place. left_of/behind describe external relationships, not the left/back parts of the named surface. location_spec describes administrative geography, not a stovetop or the left side of a table.
- n16: S4 supplies a descriptive closest-selection constraint. Searches `object description qualifiers nearest color`, `nearest object modifier ambiguity`; widen `closest one` and `nearest object with ambiguous modifier attachment` returned rank_distance, sort, spatial_constraint and similarity. rank_distance is a sort field, not a nearest-object constraint; runtime sorting cannot represent an agent's recommendation in TRACE; similarity explicitly excludes spatial proximity. Attachment and distance reference remain unresolved rather than being guessed.
- Every proposed or refined construct was also checked against the targeted fallback glossary search for description, referent, nearest, direction, region, part, and motion words. No usable equivalent was found. All original non-leaf need texts were widened; original leaf labels are admissible without proposals.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19, sha be5d8379f7a6.
- Input kind: conversation; one user message and one numbered agent plan.
- Coverage status: partial under the pinned release; suggested code depends on S1–S4 and is not a canonical accepted translation.
- Source-span coverage: t1:s1 and substantive t2:s2, s4, s6, s8, s10, s12, s14 are represented in order. t2:s1, s3, s5, s7, s9, s11, s13 are list numbering, reflected by ordered speech acts and sequence terms; they assert no separate claims. No action has evidence of execution or completion, so there are no RECORDs or outcome claims.
- Opaque-text spans: none; unresolved attachments/frames are documented below, not silently resolved by invented facts.
- Label-preserved spans: t1:s1 pan/knife/table; t2:s2 table and the color word black; t2:s4 knife/lettuce; t2:s6 stove; t2:s8 knife/pan/burner; t2:s10 pan/stove; t2:s12 safe/table/black; t2:s14 pan/table/lettuce. These use object_label, food_label or color_label; no physical properties, taxonomy or shade equivalence are inferred. The proposed constructors express relationships separately from these labels.
- Missing constructs: S1 describe_place/describe_acquire/describe_walk/describe_turn family; S2 describe_entity; S3 spatial_region; S4 closest_constraint.
- Unresolved ambiguities: t2:s4 "that is closest" could qualify knife or lettuce, and its distance reference/comparison set is unstated. closest_constraint is consequently scoped to the pickup speech act without specifying its target or reference. No translator uncertainty is attributed to the agent. t2:s6 left and t2:s8 back/left lack an explicit coordinate frame; t2:s14 above may be a visual/table-layout relationship rather than gravity-relative height. under is used only as the inverse directional description, not as evidence of stacking or contact. The report leaves the coordinate frame unresolved. The pan-with-knife request is represented as containment per the decomposed need; the agent separately proposes inserting the knife, not that it was already inserted. The later definite knife/pan/table descriptions reuse the plan's intended referents without establishing runtime REF identities.
- Proposed glossary/spec changes: S1–S4 in /output/suggestions.md; no grammar or coercion change.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` completed: 0 needs reported missing; n12, n17, n21 and n29 were declaration-only matches; n11 was flagged label-only; 7 unknown symbols were reported (closest_constraint, describe_acquire, describe_entity, describe_place, describe_turn, describe_walk, spatial_region), all explicitly proposed in S1–S4. No unbound-value, invalid-atom, retired-symbol, quoted-entity or unused-coverage-symbol warning was emitted. Its broad candidate matches do not establish semantic coverage: the proposal-dependent rows remain failed against the pinned glossary.
