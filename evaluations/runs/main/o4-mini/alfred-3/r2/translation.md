Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # User issues a command to place a pan containing a knife on a table
    TERM activity(verb="place", object=object_label::pan, instrument=object_label::knife, location=object_label::table) -> activity_2 : TERM  # PROPOSED: S1
    UTTER propose(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    # 1. Walk forward then turn left to the black table
    RECORD ACTION walk(destination=object_label::table) STATUS succeeded SOURCE "t2:s2" -> walk_event : EVENT
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s2" -> turn_event : EVENT
    LINK then(previous=walk_event, next=turn_event) SOURCE "t2:s2"

    # 2. Pick up the knife next to the lettuce that is closest
    RECORD ACTION pick_up(target=TERM entity_reference(kind=object_label::knife, relation=spatial_relation::next_to, reference=object_label::lettuce, rank=1) -> knife_ref_term : TERM) STATUS succeeded SOURCE "t2:s4" -> pick_up_event : EVENT  # PROPOSED: S2
    LINK then(previous=turn_event, next=pick_up_event) SOURCE "t2:s4"

    # 3. Turn around, go to the stove top on the left
    RECORD ACTION turn(direction="around") STATUS succeeded SOURCE "t2:s6" -> turn_around_event : EVENT
    RECORD ACTION walk(destination=TERM entity_reference(kind=object_label::stove, relation=spatial_relation::on, reference=object_label::stove, rank=1)) STATUS succeeded SOURCE "t2:s6" -> walk_stove_event : EVENT  # PROPOSED: S2
    LINK then(previous=pick_up_event, next=turn_around_event) SOURCE "t2:s6"
    LINK then(previous=turn_around_event, next=walk_stove_event) SOURCE "t2:s6"

    # 4. Put the knife in the pan on the back left burner
    RECORD ACTION place(target=TERM entity_reference(kind=object_label::knife, relation=spatial_relation::in, reference=object_label::pan) -> knife_in_pan_term : TERM, destination=TERM entity_reference(kind=object_label::stove, relation=spatial_relation::other_side_of, reference=object_label::pan, position="back_left")) STATUS succeeded SOURCE "t2:s8" -> place_event : EVENT  # PROPOSED: S2
    LINK then(previous=walk_stove_event, next=place_event) SOURCE "t2:s8"

    # 5. Take the pan from the stove top
    RECORD ACTION pick_up(target=TERM entity_reference(kind=object_label::pan, relation=spatial_relation::on, reference=object_label::stove, rank=1) -> pan_ref_term : TERM) STATUS succeeded SOURCE "t2:s10" -> pick_up_pan_event : EVENT
    LINK then(previous=place_event, next=pick_up_pan_event) SOURCE "t2:s10"

    # 6. Turn left, walk towards the safe, turn to the left to face the black table
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s12" -> turn_left_event : EVENT
    RECORD ACTION walk(destination=object_label::safe) STATUS succeeded SOURCE "t2:s12" -> walk_safe_event : EVENT
    RECORD ACTION turn(direction="left") STATUS succeeded SOURCE "t2:s12" -> turn_to_table_event : EVENT
    LINK then(previous=pick_up_pan_event, next=turn_left_event) SOURCE "t2:s12"
    LINK then(previous=turn_left_event, next=walk_safe_event) SOURCE "t2:s12"
    LINK then(previous=walk_safe_event, next=turn_to_table_event) SOURCE "t2:s12"

    # 7. Put the pan on the table on the left side above the lettuce
    RECORD ACTION place(target=pan_ref_term, destination=TERM entity_reference(kind=object_label::table, relation=spatial_relation::left_of, reference=object_label::lettuce), location="above") STATUS succeeded SOURCE "t2:s14" -> final_place_event : EVENT  # PROPOSED: S2
    LINK then(previous=turn_to_table_event, next=final_place_event) SOURCE "t2:s14"
  }
}
```

## Needs coverage

| need | kind       | expressed by                                                           | status          |
|------|------------|------------------------------------------------------------------------|-----------------|
| n1   | speech_act | UTTER propose(target=activity)                                          | covered         |
| n2   | action     | activity(verb="place")                                                | covered         |
| n3   | object     | object_label::pan, object_label::knife                                  | covered         |
| n4   | constraint | instrument=object_label::knife                                          | covered         |
| n5   | object     | object_label::table                                                     | covered         |
| n6   | action     | RECORD ACTION place                                                    | covered         |
| n7   | action     | RECORD ACTION walk                                                     | covered         |
| n8   | temporal   | LINK then                                                             | covered         |
| n9   | action     | RECORD ACTION turn                                                     | covered         |
| n10  | object     | object_label::table                                                     | covered         |
| n11  | constraint | color_label::black                                                       | proposed        |
| n12  | action     | RECORD ACTION pick_up                                                  | covered         |
| n13  | object     | object_label::knife                                                     | covered         |
| n14  | object     | object_label::lettuce                                                  | covered         |
| n15  | constraint | entity_reference(relation=spatial_relation::next_to, reference=lettuce) | proposed        |
| n16  | constraint | rank=1                                                                  | proposed        |
| n17  | action     | RECORD ACTION turn(direction="around")                               | covered         |
| n18  | action     | RECORD ACTION walk(destination=object_label::stove)                    | covered         |
| n19  | object     | object_label::stove                                                     | covered         |
| n20  | constraint | spatial_relation::left_of                                              | covered         |
| n21  | action     | RECORD ACTION place                                                    | covered         |
| n22  | object     | object_label::knife                                                     | covered         |
| n23  | object     | object_label::pan                                                      | covered         |
| n24  | object     | object_label::stove                                                    | covered         |
| n25  | constraint | position="back_left"                                                  | proposed        |
| n26  | action     | RECORD ACTION pick_up                                                  | covered         |
| n27  | object     | object_label::pan                                                      | covered         |
| n28  | object     | object_label::stove                                                    | covered         |
| n29  | action     | RECORD ACTION turn                                                     | covered         |
| n30  | action     | RECORD ACTION walk(destination=object_label::safe)                     | covered         |
| n31  | object     | object_label::safe                                                     | covered         |
| n32  | action     | RECORD ACTION turn                                                     | covered         |
| n33  | object     | object_label::table                                                     | covered         |
| n34  | action     | RECORD ACTION place                                                    | covered         |
| n35  | object     | object_label::pan                                                      | covered         |
| n36  | object     | object_label::table                                                     | covered         |
| n37  | object     | object_label::lettuce                                                  | covered         |
| n38  | constraint | spatial_relation::left_of                                              | covered         |
| n39  | constraint | location="above"                                                      | proposed        |

## Why the translation failed

- The user’s requirement for the table’s color (n11) has no existing way to express a color constraint on a target; it needs a constructor like `requirement(property="color", value=color_label::black)` or a claim relation.
- Spatial qualifiers (n15, n16, n25, n39) require a generalized constructor (`entity_reference`) to specify relation, reference object, ranking, and position; none exists.

## Translation report

- Input kind: prompt | conversation
- Coverage status: partial
- Source-span coverage: all user and agent turns represented except color and detailed spatial qualifiers
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1 activity.location extension; S2 entity_reference constructor; S3 requirement constructor or claim relation for color constraint
- Unresolved ambiguities: none
- Check: `rag check` reported unresolved needs n11, n15, n16, n25, n39 and 1 unknown symbol (entity_reference)
