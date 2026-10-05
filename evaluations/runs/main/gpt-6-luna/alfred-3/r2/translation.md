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
    TERM placement_with_contents(content=lexical_label_3, destination=lexical_label_4, object=lexical_label_2) -> placement_with_contents_2 : TERM # PROPOSED: S7
    CLAIM request(target=placement_with_contents_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM qualified_entity(color=color_label::black, kind=object_label::table) -> qualified_entity_2 : TERM # PROPOSED: S4
    RECORD ACTION walk_forward() STATUS unknown SOURCE "t2:s2" -> walk_forward_event : EVENT # PROPOSED: S1
    RECORD ACTION turn(direction="left") STATUS unknown SOURCE "t2:s2" -> turn_event : EVENT
    RECORD ACTION face(target=qualified_entity_2) STATUS unknown SOURCE "t2:s2" -> face_event : EVENT # PROPOSED: S4
    LINK then(next=turn_event, previous=walk_forward_event) SOURCE "t2:s2"

    TERM lexical_label(value=object_label::lettuce) -> lexical_label_5 : TERM
    TERM nearest_to(item=lexical_label_3, reference=lexical_label_5, relation=next_to) -> nearest_to_2 : TERM # PROPOSED: S3
    RECORD ACTION pick_up(target=nearest_to_2) STATUS unknown SOURCE "t2:s4" -> pick_up_event : EVENT # REFINED: S2

    RECORD ACTION turn(direction="around") STATUS unknown SOURCE "t2:s6" -> turn_2_event : EVENT
    RECORD ACTION walk(destination=object_label::stovetop) STATUS unknown SOURCE "t2:s6" -> walk_event : EVENT

    TERM lexical_label(value=object_label::burner) -> lexical_label_6 : TERM
    TERM spatial_constraint(object=lexical_label_2, reference=lexical_label_6, relation=on) -> spatial_constraint_3 : TERM
    RECORD ACTION place(target=lexical_label_3, destination=object_label::pan, relation=in, constraints=[spatial_constraint_5]) STATUS unknown SOURCE "t2:s8" -> place_event : EVENT # REFINED: S6

    RECORD ACTION pick_up(target=object_label::pan, source=object_label::stovetop) STATUS unknown SOURCE "t2:s10" -> pick_up_2_event : EVENT

    RECORD ACTION turn(direction="left") STATUS unknown SOURCE "t2:s12" -> turn_3_event : EVENT
    RECORD ACTION walk(destination=safe) STATUS unknown SOURCE "t2:s12" -> walk_2_event : EVENT
    RECORD ACTION turn(direction="left") STATUS unknown SOURCE "t2:s12" -> turn_4_event : EVENT
    RECORD ACTION face(target=qualified_entity_2) STATUS unknown SOURCE "t2:s12" -> face_2_event : EVENT # PROPOSED: S4

    TERM spatial_constraint(object=lexical_label_2, reference=lexical_label_4, relation=left_of) -> spatial_constraint_4 : TERM
    TERM spatial_constraint(object=lexical_label_2, reference=lexical_label_5, relation=above) -> spatial_constraint_5 : TERM # PROPOSED: S5
    RECORD ACTION place(target=lexical_label_2, destination=qualified_entity_2, relation=on, constraints=[spatial_constraint_4, spatial_constraint_5]) STATUS unknown SOURCE "t2:s14" -> place_2_event : EVENT # REFINED: S6
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, placement_with_contents (PROPOSED: S7) | proposed |
| n2 | action | placement_with_contents (PROPOSED: S7), place | proposed |
| n3 | object | object_label::pan | label-preserved |
| n4 | object | object_label::knife | label-preserved |
| n5 | object | object_label::table | label-preserved |
| n6 | constraint | spatial_constraint | covered |
| n7 | action | walk_forward (PROPOSED: S1) | proposed |
| n8 | temporal | then | covered |
| n9 | action | turn | covered |
| n10 | object | object_label::table | label-preserved |
| n11 | constraint | color_label::black, qualified_entity (PROPOSED: S4) | proposed |
| n12 | action | pick_up | proposed |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | object_label::lettuce | label-preserved |
| n15 | constraint | nearest_to (PROPOSED: S3), next_to | proposed |
| n16 | constraint | nearest_to (PROPOSED: S3) | proposed |
| n17 | action | turn | covered |
| n18 | action | walk | covered |
| n19 | object | object_label::stovetop | label-preserved |
| n20 | constraint | — | unresolved |
| n21 | action | place | covered |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | object_label::pan | label-preserved |
| n24 | object | object_label::burner | label-preserved |
| n25 | constraint | — | unresolved |
| n26 | action | pick_up | covered |
| n27 | object | object_label::pan | label-preserved |
| n28 | object | object_label::stovetop | label-preserved |
| n29 | action | turn | covered |
| n30 | action | walk | covered |
| n31 | object | safe | covered |
| n32 | action | turn, face | proposed |
| n33 | object | qualified_entity, object_label::table (PROPOSED: S4) | proposed |
| n34 | action | place | proposed |
| n35 | object | object_label::pan | label-preserved |
| n36 | object | object_label::table | label-preserved |
| n37 | object | object_label::lettuce | label-preserved |
| n38 | constraint | spatial_constraint, left_of | proposed |
| n39 | constraint | spatial_constraint, above (PROPOSED: S5) | proposed |

## Why the translation failed

- n1/n2 (t1:s1): `request` can encode an active request only when its target TERM represents the requested action. Widen/search for a command to place a containing object found `activity`, `include`, and `spatial_constraint`, but none composes “place the pan containing the knife on the table” as one requested placement. S7 proposes that reusable composition.
- n7 (t2:s2): widen “walk forward without a destination” and search “walking forward in place no target movement direction” returned `walk` and `walk_backward`; `walk` requires a destination and `walk_backward` is explicitly backward. S1 proposes the missing forward operation.
- n11 (t2:s2) and n33 (t2:s12): `color_label::black` is only a color label and cannot qualify the table by itself. Search for a structured entity with a color qualifier found no fitting constructor. S4 proposes one.
- n12/n15/n16 (t2:s4): `pick_up` does not accept a TERM describing a relationally selected object, and there is no constructor for selecting the closest knife satisfying “next to the lettuce.” Widen/search returned `rank_distance` (a search ranking value), `spatial_constraint` (a relation descriptor, not a selector), and `pick_up` (no proximity arguments). S2 refines the target signature; S3 adds a reusable nearest-to selector.
- n20 (t2:s6): “on the left” supplies no explicit reference frame/landmark, and the spatial glossary warns that left/right orientation requires context. Widen/search found `left_of`, but its definition requires a reference and does not identify one here. Unresolved; no unsupported reference was invented.
- n25 (t2:s8): “back left burner” requires a rear/left location relation and reference frame. Searches for spatial placement returned `left_of`, `behind`, `on`, and `spatial_constraint`, but no exact back-left relation or explicit reference frame. Unresolved.
- n32/n33/n34/n38/n39 (t2:s12–s14): `face` can express orienting to an entity, but the black-table qualifier needs S4. The final placement needs two simultaneous spatial constraints (left side of the table and above the lettuce); `place` currently has only one `relation`, and no `above` spatial value exists. Search/widen for “above relation” returned `under`, `in_front_of`, `spatial_constraint`, and `spatial_state`, none of which means above. S5 adds the missing `above` relation; S6 refines `place` to accept a constraint list.

## Translation report

- Pinned release: BrainCode 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation.
- Coverage status: partial.
- Source-span coverage: t1:s1 and t2:s2–t2:s14 represented; gaps and proposed constructs are listed in Needs coverage and Why the translation failed.
- Opaque-text spans: none.
- Label-preserved spans: open-group object labels for pan, knife, table, lettuce, stove top, and burner; these preserve labels only, not resolved senses/properties. `safe` is a glossary-defined entity value.
- Missing constructs: S1 forward-walk operation; S2 TERM-capable pick-up target; S3 nearest-to selector; S4 qualified entity description; S5 above relation; S6 multi-constraint placement profile; S7 placement-with-contents constructor.
- Unresolved ambiguities: t2:s6 “on the left” has no stated reference frame; t2:s8 “back left burner” has no explicit spatial reference frame.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported four unrecognized proposed symbols (`nearest_to`, `placement_with_contents`, `qualified_entity`, `walk_forward`), the proposed attribute value `above`, and n24 as label-preserved; no invalid group values were reported. The document is intentionally failed pending the listed glossary changes.
