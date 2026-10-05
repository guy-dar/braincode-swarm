Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=object_label::keys) -> lexical_label_2 : TERM
    TERM lexical_label(value=object_label::ottoman) -> lexical_label_3 : TERM
    TERM spatial_constraint(object=lexical_label_2, reference=lexical_label_3, relation=on) -> spatial_constraint_2 : TERM
    TERM place_description(target=lexical_label_2, constraints=[spatial_constraint_2], destination=lexical_label_3) -> place_description_2 : TERM # PROPOSED: S2
    CLAIM request(target=place_description_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM object_description(color=color_label::black, label=object_label::endtable) -> object_description_2 : TERM # PROPOSED: S1
    TERM object_description(label=wall) -> object_description_3 : TERM # PROPOSED: S1
    TERM lexical_label(value=object_label::couch) -> lexical_label_2 : TERM
    TERM spatial_constraint(object=object_description_2, reference=object_description_3, relation=at_wall) -> spatial_constraint_2 : TERM # PROPOSED: S6
    TERM spatial_constraint(object=object_description_2, reference=lexical_label_2, relation=across_from) -> spatial_constraint_3 : TERM # PROPOSED: S7
    TERM turn_description(direction="left") -> turn_description_2 : TERM # PROPOSED: S4
    TERM walk_description(destination=object_description_2) -> walk_description_2 : TERM # PROPOSED: S5
    TERM sequence(items=[turn_description_2, walk_description_2]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2, constraints=[spatial_constraint_2, spatial_constraint_3])
    TERM object_description(color=color_label::white, label=object_label::vase) -> object_description_4 : TERM # PROPOSED: S1
    TERM spatial_constraint(object=t1.lexical_label_2, reference=object_description_4, relation=behind) -> spatial_constraint_4 : TERM
    TERM spatial_constraint(object=t1.lexical_label_2, reference=object_description_2, relation=on) -> spatial_constraint_5 : TERM
    TERM pick_up_description(target=t1.lexical_label_2, constraints=[spatial_constraint_4, spatial_constraint_5]) -> pick_up_description_2 : TERM # PROPOSED: S3
    UTTER propose(target=pick_up_description_2)
    TERM object_description(color=color_label::purple, label=object_label::ottoman) -> object_description_5 : TERM # PROPOSED: S1
    TERM turn_description(direction="around") -> turn_description_3 : TERM # PROPOSED: S4
    TERM walk_description(destination=object_description_5, via=living_room) -> walk_description_3 : TERM # PROPOSED: S5
    TERM sequence(items=[turn_description_3, walk_description_3]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    TERM lexical_label(value=object_label::cellphone) -> lexical_label_3 : TERM
    TERM spatial_constraint(object=t1.lexical_label_2, reference=lexical_label_3, relation=left_of) -> spatial_constraint_6 : TERM
    TERM spatial_constraint(object=t1.lexical_label_2, reference=object_description_5, relation=on) -> spatial_constraint_7 : TERM
    TERM place_description(target=t1.lexical_label_2, constraints=[spatial_constraint_6, spatial_constraint_7], destination=object_description_5) -> place_description_2 : TERM # PROPOSED: S2
    UTTER propose(target=place_description_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | place_description (S2), request | proposed |
| n2 | object | object_label::keys, lexical_label | label-preserved |
| n3 | object | object_label::ottoman, lexical_label | label-preserved |
| n4 | action | turn_description (S4), sequence | proposed |
| n5 | action | walk_description (S5) | proposed |
| n6 | constraint | object_description (S1), color_label::black | proposed |
| n7 | object | object_label::endtable | label-preserved |
| n8 | constraint | spatial_constraint, at_wall (S6) | proposed |
| n9 | constraint | spatial_constraint, across_from (S7) | proposed |
| n10 | object | object_label::couch, lexical_label | label-preserved |
| n11 | action | pick_up_description (S3) | proposed |
| n12 | object | t1.lexical_label_2, object_label::keys | label-preserved |
| n13 | constraint | spatial_constraint, behind | covered |
| n14 | constraint | object_description (S1), color_label::white | proposed |
| n15 | object | object_label::vase | label-preserved |
| n16 | constraint | spatial_constraint, on, object_description (S1) | proposed |
| n17 | action | turn_description (S4) | proposed |
| n18 | action | walk_description (S5), via=living_room | proposed |
| n19 | object | living_room | covered |
| n20 | constraint | object_description (S1), color_label::purple | proposed |
| n21 | object | object_label::ottoman | label-preserved |
| n22 | action | place_description (S2) | proposed |
| n23 | object | t1.lexical_label_2, object_label::keys | label-preserved |
| n24 | constraint | spatial_constraint, left_of | covered |
| n25 | object | object_label::cellphone, lexical_label | label-preserved |
| n26 | constraint | spatial_constraint, on | covered |

## Why the translation failed

- n6, n14, n16, n20: search "object description color spatial relation" and "qualified object description"; widen "object description combining kind color and spatial constraints" found lexical_label, spatial_constraint, requirement and subject. None attaches an existing color qualifier to an object-kind description. requirement describes a required property, not an identifying existing color; subject.kind cannot take object atoms. S1 supplies this missing description role.
- n1, n22: search "describe requested placing object on surface relative to another object" and "action description operation arguments"; widen "describe placing keys on ottoman left of phone as requested action" found place, activity, request and spatial_constraint. place is executable, not a TERM; activity lacks a destination role. A spatial goal alone omits the act of placing. S2.
- n11: the same general action-description search and widen "describe picking up keys selected by spatial location" found pick_up, spatial_state and spatial_constraint. RECORD would falsely assert an occurrence, and activity has no reviewed selection-constraint contract. S3.
- n4, n17: search "action intent destination direction" and "ordered action plan turn walk through room"; widen "describe turning left and turning around" found turn and look, both operations. activity has no direction argument or reviewed turning-description expansion. S4.
- n5, n18: those same searches and widen "describe walking to landmark through living room" found walk, living_room and spatial_constraint. walk is executable; activity lacks distinct destination and traversed-region roles. S5.
- n8: search "against wall along wall"; widen "end table on the wall located along wall boundary" found wall, table and shelf. on means resting atop, which does not faithfully encode this boundary-location phrase. next_to would add a particular adjacency interpretation. S6 preserves the broad boundary relation.
- n9: search "across from couch" and "across from facing opposite"; widen "across from the couch opposite facing location" found other_side_of, corner and in_front_of. other_side_of describes the other side of the reference object, not an opposing location across intervening space. A dedicated spatial relation S7 is needed.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19, sha be5d8379f7a6.
- Input kind: conversation; user request followed by an agent's numbered instruction plan, not observed execution.
- Coverage status: partial under the pinned glossary; suggested document requires S1–S7.
- Source-span coverage: t1:s1 and substantive segments t2:s2, t2:s4, t2:s6, t2:s8 represented in source order. t2:s1, s3, s5, s7 are list markers, represented by the ordered speech acts and sequences, not fabricated turns or operations.
- Opaque-text spans: none.
- Label-preserved spans: t1:s1 keys/ottoman; t2:s2 end table/couch/black; t2:s4 keys/vase/white/end table/black; t2:s6 ottoman/purple; t2:s8 keys/cell phone/ottoman. endtable and cellphone preserve source compound noun labels as lower_word keys; they do not assert synonymy with table, night_stand or phone. Colors preserve source labels; S1 supplies only the qualifier relationship, not coordinates or shade equivalence.
- Missing constructs: S1 object_description; S2 place_description; S3 pick_up_description; S4 turn_description; S5 walk_description; S6 at_wall; S7 across_from.
- Unresolved ambiguities: t2:s2 "on the wall" does not establish mounting, contact or distance; S6 deliberately leaves these unspecified. Left/right viewpoint is not supplied; preserve the source-relative viewpoint without assigning compass coordinates. The purple ottoman is the agent's elaboration, not a retroactive user constraint. Reused keys description tracks the same described target, never a runtime REF.
- Proposed glossary/spec changes: S1–S7 in suggestions.md; no spec change proposed.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported 0 heuristic unresolved needs, 5 unknown constructor symbols (object_description, pick_up_description, place_description, turn_description, walk_description), and 2 unbound attribute values (at_wall, across_from), all proposed as S1–S7. It also flagged n3, n20 and n25 as label-only. Its candidate-overlap coverage is not semantic validation; the explicit proposed statuses above identify the actual vocabulary gaps.
