Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind=pan) -> pan_subject : TERM
    TERM subject(kind=knife) -> knife_subject : TERM
    TERM subject(kind=table) -> table_subject : TERM
    TERM spatial_constraint(object=knife_subject, reference=pan_subject, relation=in) -> knife_in_pan : TERM
    TERM activity(verb="place", object=pan_subject, location=table, purpose=knife_in_pan) -> place_pan_with_knife : TERM
    UTTER instruct(target=place_pan_with_knife) # PROPOSE: S1
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind=table, qualifier=color_label::black) -> black_table : TERM # REFINED: S2
    TERM activity(verb="walk forward") -> walk_forward : TERM
    TERM subject(kind="direction", qualifier="left") -> left_direction : TERM
    TERM activity(verb="turn", object=left_direction) -> turn_left : TERM
    TERM sequence(items=[walk_forward, turn_left]) -> approach_black_table : TERM
    UTTER instruct(target=approach_black_table) # PROPOSE: S1

    TERM subject(kind=lettuce) -> lettuce_subject : TERM
    TERM spatial_constraint(object=t1.knife_subject, reference=lettuce_subject, relation=next_to) -> knife_next_to_lettuce : TERM
    TERM activity(verb="pick up", object=t1.knife_subject, purpose=knife_next_to_lettuce) -> pick_up_knife : TERM
    UTTER instruct(target=pick_up_knife) # PROPOSE: S1

    TERM subject(kind="direction", qualifier="around") -> around_direction : TERM
    TERM activity(verb="turn", object=around_direction) -> turn_around : TERM
    TERM subject(kind="agent") -> agent_subject : TERM
    TERM subject(kind=stove) -> subject_stove : TERM
    TERM spatial_constraint(object=subject_stove, reference=agent_subject, relation=left_of) -> stove_left_of_agent : TERM
    TERM activity(verb="walk", object=subject_stove, purpose=stove_left_of_agent) -> walk_to_stove : TERM
    TERM sequence(items=[turn_around, walk_to_stove]) -> approach_left_stove : TERM
    UTTER instruct(target=approach_left_stove) # PROPOSE: S1

    TERM subject(kind="burner") -> burner_subject : TERM
    TERM spatial_constraint(object=burner_subject, reference=subject_stove, relation=left_of) -> burner_left_of_stove : TERM
    TERM spatial_constraint(object=burner_subject, reference=subject_stove, relation=behind) -> burner_behind_stove : TERM
    TERM spatial_constraint(object=t1.pan_subject, reference=burner_subject, relation=on) -> pan_on_burner : TERM
    TERM conjunction(items=[t1.knife_in_pan, pan_on_burner, burner_left_of_stove, burner_behind_stove]) -> pan_and_knife_at_burner : TERM
    TERM activity(verb="place", object=t1.knife_subject, location=pan, purpose=pan_and_knife_at_burner) -> place_knife_in_pan : TERM
    UTTER instruct(target=place_knife_in_pan) # PROPOSE: S1

    TERM activity(verb="pick up", object=t1.pan_subject, location=stove) -> pick_up_pan_from_stove : TERM
    UTTER instruct(target=pick_up_pan_from_stove) # PROPOSE: S1

    TERM activity(verb="turn", object=left_direction) -> turn_left_again : TERM
    TERM subject(kind=safe) -> safe_subject : TERM
    TERM activity(verb="walk", object=safe_subject) -> walk_to_safe : TERM
    TERM activity(verb="turn", object=left_direction) -> turn_left_toward_table : TERM
    TERM activity(verb="face", object=black_table) -> face_black_table : TERM
    TERM sequence(items=[turn_left_again, walk_to_safe, turn_left_toward_table, face_black_table]) -> orient_at_black_table : TERM
    UTTER instruct(target=orient_at_black_table) # PROPOSE: S1

    TERM spatial_constraint(object=t1.pan_subject, reference=t1.table_subject, relation=on_left_side_of) -> pan_left_side_of_table : TERM # PROPOSED: S3
    TERM spatial_constraint(object=t1.pan_subject, reference=lettuce_subject, relation=above) -> pan_above_lettuce : TERM # PROPOSED: S4
    TERM conjunction(items=[pan_left_side_of_table, pan_above_lettuce]) -> final_pan_position : TERM
    TERM activity(verb="place", object=t1.pan_subject, location=table, purpose=final_pan_position) -> place_pan_by_lettuce : TERM
    UTTER instruct(target=place_pan_by_lettuce) # PROPOSE: S1
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | instruct (PROPOSE: S1) | proposed |
| n2 | action | activity, spatial_constraint | covered |
| n3 | object | pan | covered |
| n4 | object | knife | covered |
| n5 | object | table | covered |
| n6 | constraint | spatial_constraint, in | covered |
| n7 | action | activity("walk forward") | covered |
| n8 | temporal | sequence | covered |
| n9 | action | activity("turn"), sequence | covered |
| n10 | object | table | covered |
| n11 | constraint | subject qualifier color_label::black (REFINED: S2) | proposed |
| n12 | action | activity("pick up") | covered |
| n13 | object | knife | covered |
| n14 | object | lettuce | covered |
| n15 | constraint | spatial_constraint, next_to | covered |
| n16 | constraint | — | unresolved |
| n17 | action | activity("turn") | covered |
| n18 | action | activity("walk"), subject | covered |
| n19 | object | stove | covered |
| n20 | constraint | spatial_constraint, left_of | covered |
| n21 | action | activity("place") | covered |
| n22 | object | knife | covered |
| n23 | object | pan | covered |
| n24 | object | subject(kind="burner") | covered |
| n25 | constraint | spatial_constraint, left_of, behind | covered |
| n26 | action | activity("pick up") | covered |
| n27 | object | pan | covered |
| n28 | object | stove | covered |
| n29 | action | activity("turn") | covered |
| n30 | action | activity("walk") | covered |
| n31 | object | safe | covered |
| n32 | action | activity("turn"), activity("face") | covered |
| n33 | object | table, subject qualifier color_label::black (REFINED: S2) | proposed |
| n34 | action | activity("place") | covered |
| n35 | object | pan | covered |
| n36 | object | table | covered |
| n37 | object | lettuce | covered |
| n38 | constraint | spatial_constraint relation=on_left_side_of (PROPOSED: S3) | proposed |
| n39 | constraint | spatial_constraint relation=above (PROPOSED: S4) | proposed |

## Why the translation failed

- **n1 (t1:s1; also the agent's imperative step messages t2:s2–t2:s14):** Widened “user commands agent to place pan containing knife on table” and searched “imperative directive instruct someone to perform an action” and “user requests an action to be performed.” The closest results were `propose`, `ask`, `request` (a claim relation), and `obligation` (a TERM constructor); none is a speech act for issuing an imperative. `propose` would change a command/instruction into a suggestion. Proposed S1, `instruct(target: TERM)`, records the directive without asserting it was carried out.
- **n11 and n33 (t2:s2, t2:s12):** The source specifies a black table. The current `subject.qualifier` accepts STRING, TERM, or ATOM[platform_label], but not ATOM[color_label]. Using an ungoverned quoted color would not meet the typed group contract. Proposed S2 to permit the color group in this qualifier.
- **n16 (t2:s4):** Widened “closest knife next to lettuce selection criterion” and searched “choose closest item next to named object” and “nearest object selected using spatial proximity.” `rank_distance` is a ranking field, not a spatial relation or a definition of which lettuce is closest. The source does not say what the lettuce is closest to, so the comparison reference is ambiguous and cannot be supplied without invention. The `next_to` relation is represented, but “closest” remains unresolved.
- **n38 (t2:s14):** Widened “left side of table and above another object spatial constraints.” Existing `left_of` means to the left of the reference object; it does not mean positioned on the left-side region of a surface. Proposed S3 for the distinct surface-location relation.
- **n39 (t2:s14):** The retrieved spatial vocabulary has `under` but no inverse `above` relation. Proposed S4; `under` is not interchangeable with above.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 is represented as a directive with a structured placement and containment target; all agent step spans t2:s2, t2:s4, t2:s6, t2:s8, t2:s10, t2:s12, and t2:s14 are represented as ordered instructed activities and spatial constraints, except the unresolved closest-reference detail in t2:s4.
- Opaque-text spans: none
- Label-preserved spans: none; named objects use glossary-defined values or explicit structured subject descriptions.
- Missing constructs: S1 imperative/instruction speech act; S2 acceptance of color_label atoms by subject.qualifier; S3 left-side-of-surface relation; S4 above spatial relation.
- Unresolved ambiguities: t2:s4 “closest” has no stated comparison reference. The text does not establish whether the agent's listed steps were executed or succeeded; they are encoded as agent instructions, not recorded events.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported unknown symbol `instruct` and unrecognized attribute values `above` and `on_left_side_of`; these proposed/refined identifiers are marked in the BrainCode. It mechanically marked all 39 needs OK; semantic review leaves n16 unresolved because the comparison reference is absent from the source.
