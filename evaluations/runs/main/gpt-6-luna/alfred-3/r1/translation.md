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
    TERM spatial_constraint(relation=in, object=lexical_label_3, reference=lexical_label_2) -> spatial_constraint_2 : TERM
    TERM action_description(verb="place", target=lexical_label_2, destination=lexical_label_4, relation=on, constraints=[spatial_constraint_2]) -> action_description_2 : TERM  # PROPOSED: S2
    UTTER instruct(target=action_description_2)  # PROPOSED: S1
  }
  TURN t2 SPEAKER=AGENT {
    TERM lexical_label(value=object_label::table) -> lexical_label_5 : TERM
    TERM lexical_label(value=object_label::stove) -> lexical_label_6 : TERM
    TERM lexical_label(value=object_label::safe) -> lexical_label_7 : TERM
    TERM lexical_label(value=object_label::burner) -> lexical_label_8 : TERM
    TERM lexical_label(value=food_label::lettuce) -> lexical_label_9 : TERM
    TERM lexical_label(value=color_label::black) -> lexical_label_10 : TERM
    TERM requirement(property="color", value=lexical_label_10) -> requirement_2 : TERM
    TERM relative_region(reference=lexical_label_6, directions=["back", "left"]) -> relative_region_2 : TERM  # PROPOSED: S3
    TERM relative_region(reference=lexical_label_5, directions=["left"]) -> relative_region_3 : TERM  # PROPOSED: S3

    TERM action_description(verb="walk", direction="forward") -> action_description_3 : TERM  # PROPOSED: S2
    TERM action_description(verb="turn", direction="left", destination=lexical_label_5, destination_qualifiers=[requirement_2]) -> action_description_4 : TERM  # PROPOSED: S2
    TERM sequence(items=[action_description_3, action_description_4]) -> sequence_2 : TERM
    UTTER instruct(target=sequence_2)  # PROPOSED: S1

    TERM lexical_label(value=object_label::knife) -> lexical_label_11 : TERM
    TERM lexical_label(value=food_label::lettuce) -> lexical_label_12 : TERM
    TERM spatial_constraint(relation=next_to, object=lexical_label_11, reference=lexical_label_12) -> spatial_constraint_4 : TERM
    TERM action_description(verb="pick_up", target=lexical_label_11, target_qualifiers=[spatial_constraint_4]) -> action_description_5 : TERM  # PROPOSED: S2
    UTTER instruct(target=action_description_5)  # PROPOSED: S1

    TERM action_description(verb="turn", direction="around") -> action_description_6 : TERM  # PROPOSED: S2
    TERM action_description(verb="walk", destination=lexical_label_6) -> action_description_7 : TERM  # PROPOSED: S2
    TERM sequence(items=[action_description_6, action_description_7]) -> sequence_3 : TERM
    UTTER instruct(target=sequence_3)  # PROPOSED: S1

    TERM spatial_constraint(relation=on, object=lexical_label_8, reference=relative_region_2) -> spatial_constraint_5 : TERM  # PROPOSED: S3
    TERM action_description(verb="place", target=lexical_label_11, destination=t1.lexical_label_2, relation=in, constraints=[spatial_constraint_5]) -> action_description_8 : TERM  # PROPOSED: S2
    UTTER instruct(target=action_description_8)  # PROPOSED: S1

    TERM action_description(verb="pick_up", target=t1.lexical_label_2, source=lexical_label_6) -> action_description_9 : TERM  # PROPOSED: S2
    UTTER instruct(target=action_description_9)  # PROPOSED: S1

    TERM action_description(verb="turn", direction="left") -> action_description_10 : TERM  # PROPOSED: S2
    TERM action_description(verb="walk", destination=lexical_label_7) -> action_description_11 : TERM  # PROPOSED: S2
    TERM action_description(verb="turn", direction="left") -> action_description_12 : TERM  # PROPOSED: S2
    TERM action_description(verb="face", target=lexical_label_5, target_qualifiers=[requirement_2]) -> action_description_13 : TERM  # PROPOSED: S2
    TERM sequence(items=[action_description_10, action_description_11, action_description_12, action_description_13]) -> sequence_4 : TERM
    UTTER instruct(target=sequence_4)  # PROPOSED: S1

    TERM spatial_constraint(relation=above, object=lexical_label_2, reference=lexical_label_9) -> spatial_constraint_6 : TERM  # PROPOSED: S4
    TERM action_description(verb="place", target=t1.lexical_label_2, destination=relative_region_3, relation=on, constraints=[spatial_constraint_6]) -> action_description_14 : TERM  # PROPOSED: S2
    UTTER instruct(target=action_description_14)  # PROPOSED: S1
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | instruct (S1) | proposed |
| n2 | action | action_description (S2) | proposed |
| n3 | object | object_label::pan | label-preserved |
| n4 | object | object_label::knife | label-preserved |
| n5 | object | object_label::table | label-preserved |
| n6 | constraint | spatial_constraint(in) | covered |
| n7 | action | action_description (S2) | proposed |
| n8 | temporal | sequence | covered |
| n9 | action | action_description (S2) | proposed |
| n10 | object | object_label::table | label-preserved |
| n11 | constraint | color_label::black, requirement | label-preserved |
| n12 | action | action_description (S2) | proposed |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | food_label::lettuce | label-preserved |
| n15 | constraint | spatial_constraint(next_to) | covered |
| n16 | constraint | — (nearest_to S5 not used; reference unspecified) | unresolved |
| n17 | action | action_description (S2) | proposed |
| n18 | action | action_description (S2) | proposed |
| n19 | object | object_label::stove | label-preserved |
| n20 | constraint | — | unresolved |
| n21 | action | action_description (S2) | proposed |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | object_label::pan | label-preserved |
| n24 | object | object_label::burner | label-preserved |
| n25 | constraint | relative_region (S3), spatial_constraint(on) | proposed |
| n26 | action | action_description (S2) | proposed |
| n27 | object | object_label::pan | label-preserved |
| n28 | object | object_label::stove | label-preserved |
| n29 | action | action_description (S2) | proposed |
| n30 | action | action_description (S2) | proposed |
| n31 | object | object_label::safe | label-preserved |
| n32 | action | action_description (S2) | proposed |
| n33 | object | object_label::table, color_label::black | label-preserved |
| n34 | action | action_description (S2) | proposed |
| n35 | object | object_label::pan | label-preserved |
| n36 | object | object_label::table | label-preserved |
| n37 | object | food_label::lettuce | label-preserved |
| n38 | constraint | relative_region (S3) | proposed |
| n39 | constraint | spatial_constraint(above) (S4) | proposed |

## Why the translation failed

- n1 (t1:s1) and the imperative agent turns need an instruction speech act. Widened "user commands agent to place pan with knife on table" and searched "speech act issuing an imperative instruction or command to perform described action". The retrieved speech acts `propose`, `ask`, `respond`, `inform`, and `offer` do not mean issuing a command; `propose` is suggestion, not instruction. Proposed S1.
- n2, n7, n9, n12, n17–n18, n21, n26, n29–n30, n32, and n34 (agent steps) require structured descriptions of intended physical actions with target/source/destination, direction, spatial constraints, and qualifiers. Widened "agent utterance proposing ordered physical actions: walk, turn, pick up, place, and temporal sequence". Existing `activity` has no destination or direction roles, and REQUEST Actions are forbidden in TRACE; `place`, `walk`, `turn`, and `pick_up` are executable operations, not action-description terms. Proposed reusable constructor S2.
- n20 (t2:s6) says the stove top is "on the left" but does not identify what it is left of or the reference frame, so no reference can be supplied without invention. Widened "burner location relative to stove"; available `left_of` requires a reference entity. This remains unresolved.
- n25 (t2:s8) and n38 (t2:s14) require a region on the back-left or left part of a reference surface/object. Widened "on left side above lettuce relative to table" and "burner location relative to stove". `left_of` relates two entities and does not denote a subregion of a surface; no back-left region constructor was retrieved. Proposed S3.
- n39 (t2:s14) needs an above relation. Searched "put an object on the left side above another object"; available spatial relations include `on`, `under`, and `in_front_of`, none of which means above. Proposed S4.
- n16 (t2:s4) says "the lettuce that is closest" but gives no reference point or comparison set. Widened "pick up closest knife next to lettuce"; `rank_distance` is a search-ranking field, not a general object-selection relation, and `similarity` explicitly excludes spatial proximity. A `nearest_to(candidate, reference)` constructor would express a specified reference (proposed S5), but the source does not say what it is closest to; translation remains unresolved rather than inventing an agent/location reference.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 and all substantive action clauses in t2:s2, t2:s4, t2:s6, t2:s8, t2:s10, t2:s12, and t2:s14 are represented as requests/instructions; numbered labels t2:s1, t2:s3, t2:s5, t2:s7, t2:s9, t2:s11, and t2:s13 carry no action content.
- Opaque-text spans: none
- Label-preserved spans: object/food/color leaves used as open-group values (pan, knife, table, stove, safe, burner, lettuce, black); the groups preserve source labels only and do not add inferred properties.
- Missing constructs: S1 instruction speech act; S2 compositional intended-action description; S3 relative surface/object region; S4 spatial relation above; S5 nearest-object selection relation.
- Unresolved ambiguities: t2:s4 — reference point and comparison set for "closest" are not stated; t2:s6 — "on the left" has no explicit reference frame/landmark. The exact sense of "stove top" is retained as the source label, not resolved beyond the open object label.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` heuristically marks all needs covered (n11 label-only), but semantic review leaves n16 and n20 unresolved. It reports proposed identifiers `action_description`, `instruct`, and `relative_region` as not-glossary symbols and `above` as an unbound attribute value.
