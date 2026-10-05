Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="place", object=object_label::pan, instrument=object_label::knife, location=object_label::table) -> place_pan_knife_2 : TERM
    UTTER propose(target=place_pan_knife_2)
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION walk(destination=object_label::table) STATUS succeeded SOURCE "t2:s2" -> walk_event : EVENT
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s2" -> turn_event : EVENT
    LINK then(previous=walk_event, next=turn_event) SOURCE "t2:s2"
    RECORD ACTION face(target=object_label::table) STATUS succeeded SOURCE "t2:s2" -> face_event : EVENT
    LINK then(previous=turn_event, next=face_event) SOURCE "t2:s2"
    RECORD ACTION pick_up(target=object_label::knife, source=object_label::lettuce) STATUS succeeded SOURCE "t2:s4" -> pick_up_event : EVENT
    LINK then(previous=face_event, next=pick_up_event) SOURCE "t2:s4"
    RECORD ACTION turn(direction="around") STATUS succeeded SOURCE "t2:s6" -> turn_around_event : EVENT
    LINK then(previous=pick_up_event, next=turn_around_event) SOURCE "t2:s6"
    RECORD ACTION walk(destination=object_label::stove, relation=left_of) STATUS succeeded SOURCE "t2:s6" -> walk_2_event : EVENT
    LINK then(previous=turn_around_event, next=walk_2_event) SOURCE "t2:s6"
    RECORD ACTION place(target=object_label::knife, destination=object_label::pan) STATUS succeeded SOURCE "t2:s8" -> place_event : EVENT
    LINK then(previous=walk_2_event, next=place_event) SOURCE "t2:s8"
    RECORD ACTION pick_up(target=object_label::pan, source=object_label::stove) STATUS succeeded SOURCE "t2:s10" -> pick_up_2_event : EVENT
    LINK then(previous=place_event, next=pick_up_2_event) SOURCE "t2:s10"
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s12" -> turn_left_event : EVENT
    LINK then(previous=pick_up_2_event, next=turn_left_event) SOURCE "t2:s12"
    RECORD ACTION walk(destination=object_label::safe) STATUS succeeded SOURCE "t2:s12" -> walk_3_event : EVENT
    LINK then(previous=turn_left_event, next=walk_3_event) SOURCE "t2:s12"
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s12" -> turn_left_2_event : EVENT
    LINK then(previous=walk_3_event, next=turn_left_2_event) SOURCE "t2:s12"
    RECORD ACTION place(target=object_label::pan, destination=object_label::table) STATUS succeeded SOURCE "t2:s14" -> place_2_event : EVENT
    LINK then(previous=turn_left_2_event, next=place_2_event) SOURCE "t2:s14"
  }
}
```

## Needs coverage

| need | kind | expressed by | status         |
|------|------|--------------|----------------|
| n1   | speech_act | propose           | covered        |
| n2   | action     | TERM activity     | covered        |
| n3   | object     | object_label::pan | covered        |
| n4   | object     | object_label::knife | covered      |
| n5   | object     | object_label::table | covered      |
| n6   | constraint | instrument slot     | covered    |
| n7   | action     | walk               | covered        |
| n8   | temporal   | then               | covered        |
| n9   | action     | turn, face        | covered        |
| n10  | object     | object_label::table | covered      |
| n11  | constraint | black color       | not-applicable |
| n12  | action     | pick_up           | covered        |
| n13  | object     | object_label::knife | covered      |
| n14  | object     | object_label::lettuce | covered    |
| n15  | constraint | source slot       | covered        |
| n16  | constraint | closest one       | not-applicable |
| n17  | action     | turn              | covered        |
| n18  | action     | walk              | covered        |
| n19  | object     | object_label::stove | covered      |
| n20  | constraint | relation=left_of  | covered        |
| n21  | action     | place             | covered        |
| n22  | object     | object_label::knife | covered      |
| n23  | object     | object_label::pan | covered        |
| n24  | object     | object_label::stove | covered      |
| n25  | constraint | back left burner  | not-applicable |
| n26  | action     | pick_up           | covered        |
| n27  | object     | object_label::pan | covered        |
| n28  | object     | object_label::stove | covered      |
| n29  | action     | turn              | covered        |
| n30  | action     | walk              | covered        |
| n31  | object     | object_label::safe | covered      |
| n32  | action     | turn, face        | covered        |
| n33  | object     | object_label::table | covered      |
| n34  | action     | place             | covered        |
| n35  | object     | object_label::pan | covered        |
| n36  | object     | object_label::table | covered      |
| n37  | object     | object_label::lettuce | covered    |
| n38  | constraint | left side         | not-applicable |
| n39  | constraint | above lettuce     | not-applicable |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: all utterances and agent operations from t1:s1 through t2:s14 are represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none (selection constraints in TRACE mode are not represented)
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
