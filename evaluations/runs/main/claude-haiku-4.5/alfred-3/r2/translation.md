Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER propose(target=activity(verb="place", object=object_label::pan, instrument=object_label::knife, location=object_label::table))
  }
  
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION walk(destination=object_label::table) STATUS succeeded SOURCE "t2:s2" -> walk_1 : EVENT
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s2" -> turn_1 : EVENT
    LINK then(previous=walk_1, next=turn_1) SOURCE "t2:s2"
    
    RECORD ACTION pick_up(target=object_label::knife) STATUS succeeded SOURCE "t2:s4" -> pick_up_1 : EVENT
    
    RECORD ACTION turn(direction="around") STATUS succeeded SOURCE "t2:s6" -> turn_2 : EVENT
    RECORD ACTION walk(destination=object_label::stove) STATUS succeeded SOURCE "t2:s6" -> walk_2 : EVENT
    LINK then(previous=turn_2, next=walk_2) SOURCE "t2:s6"
    
    RECORD ACTION place(target=object_label::knife, destination=object_label::pan, location=object_label::stove, relation="on") STATUS succeeded SOURCE "t2:s8" -> place_1 : EVENT
    
    RECORD ACTION pick_up(target=object_label::pan) STATUS succeeded SOURCE "t2:s10" -> pick_up_2 : EVENT
    
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s12" -> turn_3 : EVENT
    RECORD ACTION walk(destination=object_label::safe) STATUS succeeded SOURCE "t2:s12" -> walk_3 : EVENT
    RECORD ACTION face(target=object_label::table) STATUS succeeded SOURCE "t2:s12" -> face_1 : EVENT
    
    RECORD ACTION place(target=object_label::pan, destination=object_label::table, location=food_label::lettuce, relation="above") STATUS succeeded SOURCE "t2:s14" -> place_2 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | propose, activity | covered |
| n2 | action | place | covered |
| n3 | object | object_label::pan | label-preserved |
| n4 | object | object_label::knife | label-preserved |
| n5 | object | object_label::table | label-preserved |
| n6 | constraint | pan containing knife | not-applicable |
| n7 | action | walk | covered |
| n8 | temporal | then | covered |
| n9 | action | turn, face | covered |
| n10 | object | object_label::table | label-preserved |
| n11 | constraint | black color | label-preserved |
| n12 | action | pick_up | covered |
| n13 | object | object_label::knife | label-preserved |
| n14 | object | food_label::lettuce | covered |
| n15 | constraint | next to lettuce | unresolved |
| n16 | constraint | closest one | unresolved |
| n17 | action | turn | covered |
| n18 | action | walk | covered |
| n19 | object | object_label::stove | label-preserved |
| n20 | constraint | on the left | unresolved |
| n21 | action | place | covered |
| n22 | object | object_label::knife | label-preserved |
| n23 | object | object_label::pan | label-preserved |
| n24 | object | burner | label-preserved |
| n25 | constraint | back left burner | unresolved |
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
| n37 | object | food_label::lettuce | covered |
| n38 | constraint | on left side of table | unresolved |
| n39 | constraint | above lettuce | covered |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: Every action segment (t2:s2, t2:s4, t2:s6, t2:s8, t2:s10, t2:s12, t2:s14) is represented with RECORD ACTION. The user's request (t1:s1) is represented with UTTER propose and activity constructor.
- Opaque-text spans: None
- Label-preserved spans: 
  - n3, n4, n5, n10, n13, n19, n22, n23, n27, n28, n31, n33, n35, n36: objects (knife, pan, table, stove, safe) are represented as open-group labels (`object_label::*`), preserving the word form but not semantic resolution beyond object kind
  - n14, n37: lettuce represented as `food_label::lettuce`, word preserved
  - n11, n24: color descriptor "black" and burner type preserved only as part of object selection (object_label::table, burner implied by stove reference); no separate encoding
- Missing constructs: 
  - Spatial selection constraints ("next to lettuce that is closest") cannot be fully expressed in pick_up's current signature; the constraint combines selection criteria with spatial relation that operation doesn't support
  - Relative positioning with multiple relations ("on back left burner") requires simultaneous behind+left_of relations, which place's relation parameter cannot express as a compound
  - Directional modifiers for movement ("walk forward") vs locomotion; "forward" is implicit in walk
  - Color attribute selection for pick_up (the "black" table is a descriptor, not a filter in pick_up signature)
- Unresolved ambiguities: 
  - n14, n15: "the knife next to the lettuce that is closest" — pick_up signature does not support spatial location constraints or proximity ranking. The glossary provides state/color/shape filters but no relation-based selection criteria. The agent selected a specific knife using lettuce as a reference point and distance as a tie-breaker, which cannot be expressed in the current operation signature.
  - "Turn around" direction string: turn_around is an alias for turn(), but whether "around" is valid as a literal STRING value (vs. requiring "180" degrees) is not specified in the signature.
  - "Put the knife in the pan on the back left burner": parsed as place(target=knife, destination=pan, location=stove, relation="on") with burner position lost; the burner is a specific heating appliance on the stove, but no way to indicate "back left" of stove
  - "Put the pan on the table on the left side above the lettuce": uses place(target=pan, destination=table, location=lettuce, relation="above"), but the "left side of table" component is unrepresented; place accepts only one location + relation pair, not compound spatial constraints
- Check: Ran `rag check` (see below)
```

