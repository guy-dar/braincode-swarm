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
    TERM describe_place(target=lexical_label_2, destination=lexical_label_3, relation=on) -> describe_place_2 : TERM # PROPOSED: S1
    CLAIM request(target=describe_place_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM describe_turn_left() -> describe_turn_left_2 : TERM # PROPOSED: S1
    UTTER propose(target=describe_turn_left_2)
    TERM lexical_label(value=object_label::endtable) -> lexical_label_2 : TERM
    TERM lexical_label(value=color_label::black) -> lexical_label_3 : TERM
    CLAIM attribute_claim(property="color", subject=lexical_label_2, value=lexical_label_3) BY role_agent STATUS asserted SOURCE "t2:s2" -> attribute_claim_2 : CLAIM
    TERM lexical_label(value=object_label::wall) -> lexical_label_4 : TERM
    TERM lexical_label(value=object_label::couch) -> lexical_label_5 : TERM
    TERM spatial_constraint(object=lexical_label_2, reference=lexical_label_4, relation=wall_position) -> spatial_constraint_2 : TERM # PROPOSED: S2
    TERM spatial_constraint(object=lexical_label_2, reference=lexical_label_5, relation=across_from) -> spatial_constraint_3 : TERM # PROPOSED: S2
    TERM describe_walk(destination=lexical_label_2) -> describe_walk_2 : TERM # PROPOSED: S1
    UTTER propose(target=describe_walk_2, constraints=[spatial_constraint_2, spatial_constraint_3])
    TERM lexical_label(value=object_label::vase) -> lexical_label_6 : TERM
    TERM lexical_label(value=color_label::white) -> lexical_label_7 : TERM
    CLAIM attribute_claim(property="color", subject=lexical_label_6, value=lexical_label_7) BY role_agent STATUS asserted SOURCE "t2:s4" -> attribute_claim_3 : CLAIM
    TERM spatial_constraint(object=t1.lexical_label_2, reference=lexical_label_6, relation=behind) -> spatial_constraint_4 : TERM
    TERM spatial_constraint(object=t1.lexical_label_2, reference=lexical_label_2, relation=on) -> spatial_constraint_5 : TERM
    TERM describe_pick_up(target=t1.lexical_label_2) -> describe_pick_up_2 : TERM # PROPOSED: S1
    UTTER propose(target=describe_pick_up_2, constraints=[spatial_constraint_4, spatial_constraint_5])
    TERM describe_turn_around() -> describe_turn_around_2 : TERM # PROPOSED: S1
    UTTER propose(target=describe_turn_around_2)
    TERM lexical_label(value=color_label::purple) -> lexical_label_8 : TERM
    CLAIM attribute_claim(property="color", subject=t1.lexical_label_3, value=lexical_label_8) BY role_agent STATUS asserted SOURCE "t2:s6" -> attribute_claim_4 : CLAIM
    TERM subject(kind=living_room) -> subject_2 : TERM
    TERM describe_walk(destination=t1.lexical_label_3, via=[subject_2]) -> describe_walk_3 : TERM # PROPOSED: S1
    UTTER propose(target=describe_walk_3)
    TERM lexical_label(value=object_label::cellphone) -> lexical_label_9 : TERM
    TERM spatial_constraint(object=t1.lexical_label_2, reference=lexical_label_9, relation=left_of) -> spatial_constraint_6 : TERM
    TERM describe_place(target=t1.lexical_label_2, destination=t1.lexical_label_3, relation=on) -> describe_place_2 : TERM # PROPOSED: S1
    UTTER propose(target=describe_place_2, constraints=[spatial_constraint_6])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | describe_place (S1), request | proposed |
| n2 | object | object_label::keys, lexical_label | label-preserved |
| n3 | object | object_label::ottoman, lexical_label | label-preserved |
| n4 | action | describe_turn_left (S1) | proposed |
| n5 | action | describe_walk (S1) | proposed |
| n6 | constraint | attribute_claim, lexical_label, color_label::black | covered |
| n7 | object | object_label::endtable, lexical_label | label-preserved |
| n8 | constraint | spatial_constraint, wall_position (S2) | proposed |
| n9 | constraint | spatial_constraint, across_from (S2) | proposed |
| n10 | object | object_label::couch, lexical_label | label-preserved |
| n11 | action | describe_pick_up (S1) | proposed |
| n12 | object | t1.lexical_label_2, object_label::keys | label-preserved |
| n13 | constraint | spatial_constraint, behind | covered |
| n14 | constraint | attribute_claim, lexical_label, color_label::white | covered |
| n15 | object | object_label::vase, lexical_label | label-preserved |
| n16 | constraint | spatial_constraint, on, attribute_claim | covered |
| n17 | action | describe_turn_around (S1) | proposed |
| n18 | action | describe_walk (S1), via, subject | proposed |
| n19 | object | subject, living_room | covered |
| n20 | constraint | attribute_claim, lexical_label, color_label::purple | label-preserved |
| n21 | object | t1.lexical_label_3, object_label::ottoman | label-preserved |
| n22 | action | describe_place (S1) | proposed |
| n23 | object | t1.lexical_label_2, object_label::keys | label-preserved |
| n24 | constraint | spatial_constraint, left_of | covered |
| n25 | object | object_label::cellphone, lexical_label | label-preserved |
| n26 | constraint | describe_place (S1), relation=on | proposed |

## Why the translation failed

- n1, n4, n5, n11, n17, n18, n22, n26: S1 supplies pure descriptions of placement, acquisition, oriented turning and routed walking. Searches "describe requested placement spatial relation destination", "action description ordered procedure", "described movement destination direction route" and "pick up description source behind vase", plus widened searches "describe placing acquired keys on ottoman without execution" and "turn left turn around go through living room to purple ottoman described instruction", found executable place/pick_up/walk/turn and the general activity constructor. Executable operations cannot appear as recommendations in TRACE, RECORD would fabricate execution, and activity lacks destination, direction, route and placement-relation slots. sequence orders descriptions but cannot construct the missing descriptions. No new runtime actions are needed.
- n8, n9: S2 supplies descriptive spatial values. Search "across from opposite facing" and "at wall boundary" and widen "on wall at boundary across from couch" found other_side_of, on, wall and spatial_constraint. other_side_of locates something on the other side of the reference object, not across an intervening room area facing it; on means resting atop and cannot describe an end table positioned on a room's boundary wall. These interpretations cannot be obtained from leaf labels. Searches and widen for qualified black/white/purple objects returned color_label and attribute_claim; those existing entries suffice for colors, so no color proposal is made.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation (supplied user request and agent instructions, not observed execution).
- Coverage status: partial under the pinned release; suggested document requires S1 and S2.
- Source-span coverage: t1:s1 and substantive t2:s2, t2:s4, t2:s6, t2:s8 are represented provisionally. t2:s1, s3, s5, s7 are step numbering, preserved by speech-act order, not separate claims. No actions or successes are recorded.
- Opaque-text spans: none.
- Label-preserved spans: t1:s1 keys/ottoman; t2:s2 end table/couch/black; t2:s4 keys/vase/white; t2:s6 ottoman/purple; t2:s8 keys/cell phone/ottoman. Object labels use source-supported kind roles only. endtable and cellphone are explicit opaque leaf keys for the multiword labels, not aliases to table or phone; no automatic equivalence is claimed. Color names remain labels, while their association with the relevant objects is structured by attribute_claim. wall is also label-preserved as the landmark in t2:s2.
- Missing constructs: S1 pure action-description family with destination, relation and route semantics; S2 wall-position/across-from spatial values.
- Unresolved ambiguities: t2:s2 "on the wall" supplies boundary placement but no precise mounting/support geometry; S2 deliberately preserves this limitation. Left/right perspective is the instructed addressee's orientation; the cell-phone placement has no supplied global coordinate frame. t2:s4 "on the black end table" may modify the vase as well as the keys; the document represents the keys on the table, without adding an independent assertion that the vase rests there. t2:s8 similarly does not independently assert the phone's position on the ottoman.
- Proposed glossary/spec changes: S1 and S2 in /output/suggestions.md; no grammar change proposed.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported 0 unresolved needs by its candidate-overlap heuristic; 5 unknown constructor symbols (describe_pick_up, describe_place, describe_turn_around, describe_turn_left, describe_walk) and 2 unbound attribute values (across_from, wall_position), all proposed by S1/S2. It flagged n3, n20 and n25 as label-only. Candidate-overlap results do not establish semantic coverage: the action and relation gaps above remain genuine. No invalid groups, retired bare symbols, quoted-entity warnings or absent claimed coverage symbols were reported.
