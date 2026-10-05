Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # The user issues a command to put a pan with a knife on a table.
    TERM command_request(pan=object_label::pan, contains=object_label::knife, destination=object_label::table) -> command_request_2 : TERM   # PROPOSED: S1
    UTTER command(target=command_request_2)   # PROPOSED: S1
  }
  TURN t2 SPEAKER=AGENT {
    # Step 1: walk forward to the black table
    ACTION walk_forward()   # PROPOSED: S2
    ACTION turn(direction="left")
    ACTION face(target=object_label::table)
    # Step 2: pick up the knife next to the closest lettuce
    TERM select_object(reference=object_label::lettuce, target_class=object_label::knife, relation=next_to) -> knife_target : TERM   # PROPOSED: S3
    ACTION pick_up(target=knife_target)   # PROPOSED: S4
    # Step 3: turn around and go to the stove top on the left
    ACTION turn(direction="around")
    TERM select_object(reference=object_label::stove, target_class="top", relation=on) -> stove_top : TERM   # PROPOSED: S3
    ACTION walk(target=stove_top)
    # Step 4: put the knife into the pan on the back left burner
    TERM select_object(reference=stove_top, target_class=object_label::pan, relation=on) -> pan_on_burner : TERM   # PROPOSED: S3
    ACTION place(target=knife_target, destination=pan_on_burner, relation=on)
    # Step 5: take the pan from the stove top
    ACTION pick_up(target=pan_on_burner)
    # Step 6: turn left, walk to the safe, then face the black table
    ACTION turn(direction="left")
    ACTION walk(target=object_label::safe)
    ACTION turn(direction="left")
    ACTION face(target=object_label::table)
    # Step 7: put the pan on the table on its left side above the lettuce
    TERM select_object(reference=object_label::table, target_class="left_side", relation=on) -> left_side : TERM   # PROPOSED: S3
    TERM select_object(reference=left_side, target_class=object_label::lettuce, relation=above) -> lettuce_zone : TERM   # PROPOSED: S3
    ACTION place(target=pan_on_burner, destination=lettuce_zone, relation=on)
  }
}
```

## Needs coverage

| need | kind       | expressed by                                                                                         | status          |
|------|------------|------------------------------------------------------------------------------------------------------|-----------------|
| n1   | speech_act | UTTER command                                                                                        | proposed        |
| n2   | action     | ACTION walk_forward()                                                                                | proposed        |
| n3   | object     | object_label::pan                                                                                    | covered         |
| n4   | object     | object_label::knife                                                                                  | covered         |
| n5   | object     | object_label::table                                                                                  | covered         |
| n6   | constraint | contains=object_label::knife in TERM command_request                                                | proposed        |
| n7   | action     | ACTION turn(direction="left")                                                                      | covered         |
| n8   | temporal   | temporal sequencing implicit in steps                                                                | not-applicable  |
| n9   | action     | ACTION turn(direction="left") + ACTION face(target=…)                                              | covered         |
| n10  | object     | object_label::table                                                                                  | covered         |
| n11  | constraint | color_label::black (table color)                                                                     | unresolved      |
| n12  | action     | ACTION pick_up(target=knife_target)                                                                  | covered         |
| n13  | object     | object_label::knife                                                                                  | covered         |
| n14  | object     | object_label::lettuce                                                                                | covered         |
| n15  | constraint | relation=next_to in TERM select_object                                                               | proposed        |
| n16  | constraint | rank_distance ("closest")                                                                          | unresolved      |
| n17  | action     | ACTION turn(direction="around")                                                                    | covered         |
| n18  | action     | ACTION walk(target=stove_top)                                                                        | covered         |
| n19  | object     | object_label::stove                                                                                  | covered         |
| n20  | constraint | relation=on + implied "left" in select_object                                                      | proposed        |
| n21  | action     | ACTION place(target=knife_target, destination=pan_on_burner)                                         | covered         |
| n22  | object     | object_label::knife                                                                                  | covered         |
| n23  | object     | object_label::pan                                                                                    | covered         |
| n24  | object     | object_label::stove                                                                                  | covered         |
| n25  | constraint | specificity "back left"                                                                            | unresolved      |
| n26  | action     | ACTION pick_up(target=pan_on_burner)                                                                 | covered         |
| n27  | object     | object_label::pan                                                                                    | covered         |
| n28  | object     | object_label::stove                                                                                  | covered         |
| n29  | action     | ACTION turn(direction="left")                                                                      | covered         |
| n30  | action     | ACTION walk(target=object_label::safe)                                                               | covered         |
| n31  | object     | object_label::safe                                                                                   | covered         |
| n32  | action     | ACTION turn(direction="left") + ACTION face(target=object_label::table)                            | covered         |
| n33  | object     | object_label::table                                                                                  | covered         |
| n34  | action     | ACTION place(target=pan_on_burner, destination=lettuce_zone)                                         | covered         |
| n35  | object     | object_label::pan                                                                                    | covered         |
| n36  | object     | object_label::table                                                                                  | covered         |
| n37  | object     | object_label::lettuce                                                                                | covered         |
| n38  | constraint | specificity "left side"                                                                            | unresolved      |
| n39  | constraint | relation=above in TERM select_object                                                                 | proposed        |

## Why the translation failed

- n1 “command” UTTER speech act does not exist in glossary.
- n2 “walk forward” needs a zero-argument operation walk_forward(), not present.
- n11 No way to specify color_label::black as a parameter to face/place/walk.
- n16 No constructor or operation accepts ranking qualifiers ("closest") for selection.
- n25 No support for specifying "back left" burner location.
- n38 No way to express "left side" specificity in spatial selection.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all spans t1:s1–t2:s14 structured, qualifiers unformalized
- Opaque-text spans: none
- Missing constructs: S1 command, S2 walk_forward, S3 select_object constructor, S4 pick_up TERM target
- Unresolved ambiguities: interpretation of "closest" vs. adjacency; distinction between back-left and left-side
- Check: 7 unresolved needs, 4 proposed symbols
