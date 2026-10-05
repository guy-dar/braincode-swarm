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
    TERM spatial_constraint(relation=on, object=lexical_label_2, reference=lexical_label_3) -> spatial_constraint_2 : TERM
    TERM action_description(action="place", object=lexical_label_2, constraints=[spatial_constraint_2]) -> action_description_2 : TERM  # PROPOSED: S1
    CLAIM request(target=action_description_2) BY role_user STATUS observed SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM action_description(action="turn", direction="left") -> action_description_3 : TERM  # PROPOSED: S1
    CLAIM request(target=action_description_3) BY role_agent STATUS observed SOURCE "t2:s2" -> request_3 : CLAIM

    TERM subject(kind=end_table) -> subject_2 : TERM  # PROPOSED: S3
    TERM lexical_label(value=color_label::black) -> lexical_label_5 : TERM
    TERM qualified_entity(entity=subject_2, qualifier=lexical_label_5) -> qualified_entity_2 : TERM  # PROPOSED: S2
    TERM lexical_label(value=object_label::wall) -> lexical_label_6 : TERM
    TERM spatial_constraint(relation=on, object=qualified_entity_2, reference=lexical_label_6) -> spatial_constraint_3 : TERM
    TERM lexical_label(value=object_label::couch) -> lexical_label_7 : TERM
    TERM spatial_constraint(relation=other_side_of, object=qualified_entity_2, reference=lexical_label_7) -> spatial_constraint_4 : TERM
    TERM action_description(action="walk", destination=qualified_entity_2, constraints=[spatial_constraint_3, spatial_constraint_4]) -> action_description_4 : TERM  # PROPOSED: S1
    CLAIM request(target=action_description_4) BY role_agent STATUS observed SOURCE "t2:s2" -> request_4 : CLAIM

    TERM lexical_label(value=object_label::keys) -> lexical_label_8 : TERM
    TERM lexical_label(value=object_label::vase) -> lexical_label_9 : TERM
    TERM lexical_label(value=color_label::white) -> lexical_label_10 : TERM
    TERM qualified_entity(entity=lexical_label_9, qualifier=lexical_label_10) -> qualified_entity_3 : TERM  # PROPOSED: S2
    TERM spatial_constraint(relation=behind, object=lexical_label_8, reference=qualified_entity_3) -> spatial_constraint_5 : TERM
    TERM spatial_constraint(relation=on, object=lexical_label_8, reference=qualified_entity_2) -> spatial_constraint_6 : TERM
    TERM action_description(action="pick_up", object=lexical_label_8, constraints=[spatial_constraint_5, spatial_constraint_6]) -> action_description_5 : TERM  # PROPOSED: S1
    CLAIM request(target=action_description_5) BY role_agent STATUS observed SOURCE "t2:s4" -> request_5 : CLAIM

    TERM action_description(action="turn", direction="around") -> action_description_6 : TERM  # PROPOSED: S1
    CLAIM request(target=action_description_6) BY role_agent STATUS observed SOURCE "t2:s6" -> request_6 : CLAIM
    TERM subject(kind=living_room) -> subject_3 : TERM
    TERM lexical_label(value=object_label::ottoman) -> lexical_label_12 : TERM
    TERM lexical_label(value=color_label::purple) -> lexical_label_13 : TERM
    TERM qualified_entity(entity=lexical_label_12, qualifier=lexical_label_13) -> qualified_entity_4 : TERM  # PROPOSED: S2
    TERM action_description(action="walk", destination=qualified_entity_4, path=[subject_3]) -> action_description_7 : TERM  # PROPOSED: S1
    CLAIM request(target=action_description_7) BY role_agent STATUS observed SOURCE "t2:s6" -> request_7 : CLAIM

    TERM lexical_label(value=object_label::phone) -> lexical_label_14 : TERM
    TERM spatial_constraint(relation=left_of, object=lexical_label_8, reference=lexical_label_14) -> spatial_constraint_7 : TERM
    TERM spatial_constraint(relation=on, object=lexical_label_8, reference=qualified_entity_4) -> spatial_constraint_8 : TERM
    TERM action_description(action="place", object=lexical_label_8, constraints=[spatial_constraint_7, spatial_constraint_8]) -> action_description_8 : TERM  # PROPOSED: S1
    CLAIM request(target=action_description_8) BY role_agent STATUS observed SOURCE "t2:s8" -> request_8 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | action_description (PROPOSED: S1) | proposed |
| n2 | object | object_label::keys | label-preserved |
| n3 | object | object_label::ottoman | label-preserved |
| n4 | action | action_description (PROPOSED: S1) | proposed |
| n5 | action | action_description (PROPOSED: S1) | proposed |
| n6 | constraint | color_label::black | label-preserved |
| n7 | object | end_table (PROPOSED: S3) | proposed |
| n8 | constraint | spatial_constraint, on | covered |
| n9 | constraint | spatial_constraint, other_side_of | covered |
| n10 | object | object_label::couch | label-preserved |
| n11 | action | action_description (PROPOSED: S1) | proposed |
| n12 | object | object_label::keys | label-preserved |
| n13 | constraint | spatial_constraint, behind | covered |
| n14 | constraint | color_label::white | label-preserved |
| n15 | object | object_label::vase | label-preserved |
| n16 | constraint | spatial_constraint, on | covered |
| n17 | action | action_description (PROPOSED: S1) | proposed |
| n18 | action | action_description (PROPOSED: S1) | proposed |
| n19 | object | living_room via subject | covered |
| n20 | constraint | color_label::purple | label-preserved |
| n21 | object | object_label::ottoman | label-preserved |
| n22 | action | action_description (PROPOSED: S1) | proposed |
| n23 | object | object_label::keys | label-preserved |
| n24 | constraint | spatial_constraint, left_of | covered |
| n25 | object | object_label::phone | label-preserved |
| n26 | constraint | spatial_constraint, on | covered |

## Why the translation failed

- **S1 / n1, n4, n5, n11, n17, n18, n22:** `place`, `turn`, `walk`, and `pick_up` are REQUEST operations, not descriptions of operations in this TRACE; the agent's numbered imperatives are not evidence that those operations occurred. Widened searches for “describe turning and walking to locations as instructed actions, not performed operations”, “a speaker instructs or directs an addressee to perform an action”, “imperative steps spoken by agent are recommendations or instructions, not completed events”, and “a directive speech act instructing someone to do something, command” returned `activity`, `propose`, and other speech acts, but none preserves operation roles such as direction, destination, object, route and spatial constraints. `activity` describes an action but has no destination/path/spatial-constraint arguments; `propose` means suggest, not issue a direct instruction. Proposed S1 is a reusable descriptive action constructor. Existing `request(target: TERM)` records the request/constraint state without falsely claiming performance.
- **S2 / n6, n14, n20, n21:** colors and object labels can each be represented with `lexical_label`, but the current glossary has no constructor to combine an entity TERM and a color-qualifier TERM while retaining both as distinct structured arguments. `subject` supports one qualifier, but its kind is STRING and it does not compose an open-group object label with a separately structured color label. Proposed S2 supplies that composition. Until accepted, the group leaves in the suggested document preserve labels only.
- **S3 / n7:** widened search for “end table as a distinct small furniture table, not a nightstand” returned `table`, `night_stand` and other nearby furniture/location entries. `table` is only a table surface; `night_stand` is specifically a bedside table, which is not supported by the source. There is no exact retained value for an end table; S3 proposes a location-name value preserving the destination's distinction.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 and t2:s2, t2:s4, t2:s6, t2:s8 are represented; the standalone numbering segments t2:s1, t2:s3, t2:s5 and t2:s7 carry no additional semantic content.
- Opaque-text spans: none
- Label-preserved spans: t1:s1 “keys”, “ottoman”; t2:s2 “black”, “couch”; t2:s4 “keys”, “white”, “vase”; t2:s6 “purple”, “ottoman”; t2:s8 “keys”, “phone”. These are represented as open-group leaf labels and do not imply additional properties. The end-table need is proposed as a distinct location-name value, not treated as a label-preserved match.
- Missing constructs: S1 descriptive action/instruction constructor; S2 structured composition of an object label and a color qualifier; S3 the exact end-table location descriptor.
- Unresolved ambiguities: “on the wall” is encoded with spatial relation `on`; the supplied glossary distinguishes `on` from `in`, but does not clarify whether the source means attached to the wall or merely at the wall. “Across from the couch” is represented by `other_side_of`, whose definition is opposite/other side of a reference object.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reports n3 and n20 as label-preserved, flags `action_description` and `qualified_entity` as unknown symbols, and flags `end_table` as an unbound glossary value. These correspond to proposed S1, S2 and S3; no invalid value-group atoms remain. This is a failed translation because the needed proposed definitions are not in the pinned glossary.
