Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="place", object="pan", location="table") -> activity_2 : TERM
    UTTER propose(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION walk(destination=object_label::table) STATUS succeeded SOURCE "t2:s2" -> walk_event_1 : EVENT
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s2" -> turn_event_1 : EVENT
    RECORD ACTION pick_up(target=object_label::knife) STATUS succeeded SOURCE "t2:s4" -> knife_ref : TERM
    RECORD ACTION turn(direction="around") STATUS succeeded SOURCE "t2:s6" -> turn_event_2 : EVENT
    RECORD ACTION walk(destination=object_label::stove) STATUS succeeded SOURCE "t2:s6" -> walk_event_2 : EVENT
    RECORD ACTION place(target=knife_ref, destination=object_label::pan) STATUS succeeded SOURCE "t2:s8" -> place_knife_event : EVENT
    RECORD ACTION pick_up(target=object_label::pan) STATUS succeeded SOURCE "t2:s10" -> pan_ref : TERM
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s12" -> turn_event_3 : EVENT
    RECORD ACTION walk(destination=object_label::safe) STATUS succeeded SOURCE "t2:s12" -> walk_event_3 : EVENT
    RECORD ACTION face(target=object_label::table) STATUS succeeded SOURCE "t2:s12" -> face_event : EVENT
    RECORD ACTION place(target=pan_ref, destination=object_label::table, location=object_label::lettuce, relation="left_of") STATUS succeeded SOURCE "t2:s14" -> place_pan_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | propose | covered |
| n2 | action | place | covered |
| n3 | object | object_label::pan | label-preserved |
| n4 | object | object_label::knife | label-preserved |
| n5 | object | object_label::table | label-preserved |
| n6 | constraint | place(target=knife_ref, destination=pan) | covered |
| n7 | action | walk | covered |
| n8 | temporal | — | not-applicable |
| n9 | action | turn, walk | covered |
| n10 | object | object_label::table | label-preserved |
| n11 | constraint | color black (context only) | label-preserved |
| n12 | action | pick_up | covered |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | object_label::lettuce | label-preserved |
| n15 | constraint | context-only spatial qualifier | not-applicable |
| n16 | constraint | closest (context only) | label-preserved |
| n17 | action | turn | covered |
| n18 | action | walk | covered |
| n19 | object | object_label::stove | label-preserved |
| n20 | constraint | left location (context only) | label-preserved |
| n21 | action | place | covered |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | object_label::pan | label-preserved |
| n24 | object | object_label burner context | label-preserved |
| n25 | constraint | back left burner (context only) | label-preserved |
| n26 | action | pick_up | covered |
| n27 | object | object_label::pan | label-preserved |
| n28 | object | object_label::stove | label-preserved |
| n29 | action | turn | covered |
| n30 | action | walk | covered |
| n31 | object | object_label::safe | label-preserved |
| n32 | action | turn, face | covered |
| n33 | object | object_label::table | label-preserved |
| n34 | action | place | covered |
| n35 | object | object_label::pan | label-preserved |
| n36 | object | object_label::table | label-preserved |
| n37 | object | object_label::lettuce | label-preserved |
| n38 | constraint | left_of (partial) | covered |
| n39 | constraint | spatial constraint beyond available relations | not-applicable |

## Translation report

- Input kind: conversation (multi-turn dialogue with observed behavior)
- Coverage status: partial
- Source-span coverage: All main actions and navigation steps are represented (t1:s1, t2:s2–t2:s14). The USER's request is preserved as a proposed action. The AGENT's seven navigation and object-manipulation steps are recorded as a sequence of RECORD ACTION statements with their corresponding source locators.
- Opaque-text spans: none
- Label-preserved spans: 
  - All object references (pan, knife, table, stove, safe, lettuce) are preserved as open-group labels (object_label::*), with no deeper semantic resolution possible from the BrainCode vocabulary.
  - Color attribute "black table" is identified but not encoded in any operation parameter (walk, place, face have no color parameter).
  - Spatial constraints "next to lettuce", "closest one", "back left burner", and "above the lettuce" are semantic refinements on object selection and placement that exceed the available operation signatures.
- Missing constructs:
  - No spatial relation "in" or "inside" exists in the glossary (place(destination=pan) represents containment implicitly).
  - No operation parameter for selection constraints like "closest to" or relative positioning like "above".
  - Color attributes cannot be encoded in walk/face/place operations (color parameter exists only for pick_up).
- Unresolved ambiguities:
  - t2:s2 "walk forward then turn left to the black table": destination inferred from context; color "black" is not a walk parameter.
  - t2:s4 "knife next to the lettuce that is closest": spatial proximity and selection rank not encoded in pick_up parameters.
  - t2:s8 "put the knife in the pan on the back left burner": "in" containment and burner location not explicitly encoded (pan serves as implicit container).
  - t2:s14 "put the pan on the table on the left side above the lettuce": location set to lettuce with relation="left_of"; "above" constraint not representable with available spatial relations.
- Check: `rag check` will confirm whether all symbols are glossary-valid.
