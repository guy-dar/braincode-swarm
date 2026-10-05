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
    TERM activity(destination=lexical_label_3, object=lexical_label_2, relation=on, verb="place") -> activity_2 : TERM # REFINED: S1
    CLAIM request(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM activity(direction="left", verb="turn") -> activity_2 : TERM # REFINED: S1
    TERM lexical_label(value=object_label::endtable) -> lexical_label_2 : TERM
    TERM lexical_label(value=color_label::black) -> lexical_label_3 : TERM
    CLAIM attribute_claim(property="color", subject=lexical_label_2, value=lexical_label_3) BY role_agent STATUS asserted SOURCE "t2:s2" -> attribute_claim_2 : CLAIM
    TERM subject(kind=wall) -> subject_2 : TERM
    CLAIM spatial_state(object=lexical_label_2, reference=subject_2, relation=on) BY role_agent STATUS asserted SOURCE "t2:s2" -> spatial_state_2 : CLAIM
    TERM lexical_label(value=object_label::couch) -> lexical_label_4 : TERM
    CLAIM spatial_state(object=lexical_label_2, reference=lexical_label_4, relation=other_side_of) BY role_agent STATUS asserted SOURCE "t2:s2" -> spatial_state_3 : CLAIM
    TERM activity(destination=lexical_label_2, verb="walk") -> activity_3 : TERM # REFINED: S1
    TERM sequence(items=[activity_2, activity_3]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM lexical_label(value=object_label::vase) -> lexical_label_5 : TERM
    TERM lexical_label(value=color_label::white) -> lexical_label_6 : TERM
    CLAIM attribute_claim(property="color", subject=lexical_label_5, value=lexical_label_6) BY role_agent STATUS asserted SOURCE "t2:s4" -> attribute_claim_3 : CLAIM
    CLAIM spatial_state(object=t1.lexical_label_2, reference=lexical_label_5, relation=behind) BY role_agent STATUS asserted SOURCE "t2:s4" -> spatial_state_4 : CLAIM
    CLAIM spatial_state(object=t1.lexical_label_2, reference=lexical_label_2, relation=on) BY role_agent STATUS asserted SOURCE "t2:s4" -> spatial_state_5 : CLAIM
    TERM activity(object=t1.lexical_label_2, verb="pick_up") -> activity_4 : TERM # REFINED: S1
    UTTER propose(target=activity_4)
    TERM activity(direction="around", verb="turn") -> activity_5 : TERM # REFINED: S1
    TERM subject(kind=living_room) -> subject_3 : TERM
    TERM lexical_label(value=color_label::purple) -> lexical_label_7 : TERM
    CLAIM attribute_claim(property="color", subject=t1.lexical_label_3, value=lexical_label_7) BY role_agent STATUS asserted SOURCE "t2:s6" -> attribute_claim_4 : CLAIM
    TERM activity(destination=t1.lexical_label_3, verb="walk", via=[subject_3]) -> activity_6 : TERM # REFINED: S1
    TERM sequence(items=[activity_5, activity_6]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
    TERM lexical_label(value=object_label::cellphone) -> lexical_label_8 : TERM
    TERM spatial_constraint(object=t1.lexical_label_2, reference=lexical_label_8, relation=left_of) -> spatial_constraint_2 : TERM
    TERM activity(constraints=[spatial_constraint_2], destination=t1.lexical_label_3, object=t1.lexical_label_2, relation=on, verb="place") -> activity_7 : TERM # REFINED: S1
    UTTER propose(target=activity_7)
    TERM sequence(items=[sequence_2, activity_4, sequence_3, activity_7]) -> sequence_4 : TERM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity (REFINED: S1), request | proposed |
| n2 | object | lexical_label, object_label::keys | label-preserved |
| n3 | object | lexical_label, object_label::ottoman | label-preserved |
| n4 | action | activity (REFINED: S1), sequence, propose | proposed |
| n5 | action | activity (REFINED: S1), sequence, propose | proposed |
| n6 | constraint | attribute_claim, lexical_label, color_label::black | covered |
| n7 | object | lexical_label, object_label::endtable | label-preserved |
| n8 | constraint | spatial_state, subject, wall, on | covered |
| n9 | constraint | spatial_state, other_side_of | covered |
| n10 | object | lexical_label, object_label::couch | label-preserved |
| n11 | action | activity (REFINED: S1), propose | proposed |
| n12 | object | t1.lexical_label_2, object_label::keys | label-preserved |
| n13 | constraint | spatial_state, behind | covered |
| n14 | constraint | attribute_claim, lexical_label, color_label::white | covered |
| n15 | object | lexical_label, object_label::vase | label-preserved |
| n16 | constraint | spatial_state, on, attribute_claim | covered |
| n17 | action | activity (REFINED: S1), sequence, propose | proposed |
| n18 | action | activity (REFINED: S1), subject, living_room | proposed |
| n19 | object | subject, living_room | covered |
| n20 | constraint | attribute_claim, lexical_label, color_label::purple | label-preserved |
| n21 | object | t1.lexical_label_3, object_label::ottoman | label-preserved |
| n22 | action | activity (REFINED: S1), propose | proposed |
| n23 | object | t1.lexical_label_2, object_label::keys | label-preserved |
| n24 | constraint | spatial_constraint, left_of, activity (REFINED: S1) | proposed |
| n25 | object | lexical_label, object_label::cellphone | label-preserved |
| n26 | constraint | activity (REFINED: S1), on | proposed |

## Why the translation failed

- n1, n4, n5, n11, n17, n18, n22, n24, n26: S1 is required to describe these requested/recommended operations with their roles and conditions. Searches for described placement, action arguments/destination/direction/route, and walking via a room returned `activity` and executable `place`, `turn`, `walk`, `pick_up`. Widening the combined action needs and "describe an action with destination direction and route rather than execute it" returned the same candidates, plus `sequence`, `request` and `propose`. `activity` has no destination, direction, route or constraints slots and does not publish reviewed meanings for these four verb literals. Executable operations are forbidden here; RECORD would falsely report these instructions as performed. `spatial_constraint` alone describes a configuration, not the action producing it. S1 refines the existing constructor rather than adding duplicate operations.
- Qualified-entity search and widened color/location-description search returned `lexical_label`, `subject`, `requirement`, `attribute_claim` and `spatial_state`. The latter two let us attribute the agent's descriptive assertions without inventing observations or additional object-description vocabulary.
- Search "across from couch spatial opposite", "opposite facing across from", and widen "across from the couch" found spatial relations. `other_side_of` explicitly includes an opposite position; this contextual reading represents "across from", not "behind" or adjacency. No new relation is proposed.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation; supplied user request and agent instructions, not evidence of execution.
- Coverage status: partial against the current release; the suggested document requires S1 acceptance.
- Source-span coverage: t1:s1 and substantive spans t2:s2, t2:s4, t2:s6, t2:s8 represented, conditionally on S1. t2:s1, t2:s3, t2:s5, t2:s7 are list numerals; their ordering is represented by ordered speech acts and sequence terms, not invented turns.
- Opaque-text spans: none.
- Label-preserved spans: t1:s1 keys and ottoman; t2:s2 end table, couch and black; t2:s4 keys, vase, white and repeated black end table; t2:s6 ottoman and purple; t2:s8 keys, cell phone and ottoman. Labels preserve source roles only; relations and color attribution are separately structured. `endtable` and `cellphone` are explicit serialization keys for those compound leaf labels, not automatic synonym normalization or hidden clauses.
- Missing constructs: S1 activity signature and reviewed verb meanings for nonexecuting placement, pickup, turning and walking descriptions.
- Unresolved ambiguities: left/right orientation has no supplied coordinate frame; retain the source-relative orientation without inventing one. "On the wall" is retained as the agent's wording/configuration; no mounting mechanism is inferred. In t2:s4, "on the black end table" qualifies the keys; the vase's position is not separately invented. In t2:s8, "on the ottoman" constrains placement of the keys, without separately asserting the phone's location. The plan refines the original goal, not a correction or a completed result.
- Proposed glossary/spec changes: S1 only; no spec change.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported 0 unresolved needs and no unknown-symbol or other warning lines; it flagged n3, n20 and n25 as label-preserved. This heuristic lexical check does not validate signatures: the use of S1's additional activity attributes still requires a failed translation, notwithstanding the lexical matches.
