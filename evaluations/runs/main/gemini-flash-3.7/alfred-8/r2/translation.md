Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    ACTION pick_up(target=object_label::book, quantity=2, source=object_label::desk) -> book_refs : LIST[REF[STRING]]
    FOR EACH item IN book_refs {
      ACTION place(target=item, destination=object_label::bed, relation=on)
    }
  }
  TURN t2 SPEAKER=AGENT {
    ACTION turn(direction="around")
    ACTION walk(destination=object_label::room)
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    TERM lexical_label(value=object_label::trashcan) -> lexical_label_3 : TERM
    TERM spatial_constraint(object=lexical_label_2, reference=lexical_label_3, relation=in_front_of) -> spatial_constraint_2 : TERM
    ACTION turn(direction="right")
    ACTION walk(destination=object_label::desk)
    TERM lexical_label(value=object_label::mug) -> lexical_label_4 : TERM
    TERM lexical_label(value=object_label::book) -> lexical_label_5 : TERM
    TERM spatial_constraint(object=lexical_label_5, reference=lexical_label_4, relation=right_of) -> spatial_constraint_3 : TERM
    ACTION pick_up(target=object_label::book, source=object_label::desk) -> book_ref : REF[STRING]
    ACTION turn(direction="right")
    ACTION walk(destination=object_label::bed)
    ACTION place(target=book_ref, destination=object_label::bed, location=object_label::computer, relation=in_front_of)
    ACTION turn(direction="around")
    ACTION walk(destination=object_label::desk)
    TERM lexical_label(value=object_label::lamp) -> lexical_label_6 : TERM
    TERM spatial_constraint(object=lexical_label_5, reference=lexical_label_6, relation=right_of) -> spatial_constraint_4 : TERM
    ACTION pick_up(target=object_label::book, source=object_label::desk) -> book_ref_2 : REF[STRING]
    ACTION turn(direction="right")
    ACTION walk(destination=object_label::bed)
    ACTION place(target=book_ref_2, destination=object_label::bed, location=object_label::bear, relation=other_side_of)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | pick_up, place | covered |
| n2 | action | pick_up, place | covered |
| n3 | object | object_label::book | label-preserved |
| n4 | constraint | quantity | covered |
| n5 | object | object_label::desk | label-preserved |
| n6 | object | object_label::bed | label-preserved |
| n7 | action | turn | covered |
| n8 | action | walk | covered |
| n9 | object | object_label::room | label-preserved |
| n10 | action | turn | covered |
| n11 | constraint | spatial_constraint | covered |
| n12 | constraint | color_label::green | label-preserved |
| n13 | object | object_label::trashcan | label-preserved |
| n14 | action | walk | covered |
| n15 | object | object_label::desk | label-preserved |
| n16 | action | pick_up | covered |
| n17 | object | object_label::book | label-preserved |
| n18 | constraint | right_of, spatial_constraint | covered |
| n19 | object | object_label::mug | label-preserved |
| n20 | action | turn | covered |
| n21 | action | walk | covered |
| n22 | object | object_label::bed | label-preserved |
| n23 | action | place | covered |
| n24 | object | object_label::book | label-preserved |
| n25 | object | object_label::bed | label-preserved |
| n26 | constraint | in_front_of | covered |
| n27 | object | object_label::computer | label-preserved |
| n28 | action | turn | covered |
| n29 | action | walk | covered |
| n30 | object | object_label::desk | label-preserved |
| n31 | action | pick_up | covered |
| n32 | object | object_label::book | label-preserved |
| n33 | constraint | right_of, spatial_constraint | covered |
| n34 | object | object_label::lamp | label-preserved |
| n35 | action | turn | covered |
| n36 | action | walk | covered |
| n37 | object | object_label::bed | label-preserved |
| n38 | action | place | covered |
| n39 | object | object_label::book | label-preserved |
| n40 | object | object_label::bed | label-preserved |
| n41 | constraint | other_side_of | covered |
| n42 | object | object_label::bear | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s16 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "book" -> object_label::book; t1:s1 "desk" -> object_label::desk; t1:s1 "bed" -> object_label::bed; t2:s2 "room" -> object_label::room; t2:s2 "green" -> color_label::green; t2:s2 "garbage can" -> object_label::trashcan; t2:s2 "desk" -> object_label::desk; t2:s4 "book" -> object_label::book; t2:s4 "coffee mug" -> object_label::mug; t2:s6 "bed" -> object_label::bed; t2:s8 "book" -> object_label::book; t2:s8 "bed" -> object_label::bed; t2:s8 "computer" -> object_label::computer; t2:s10 "desk" -> object_label::desk; t2:s12 "book" -> object_label::book; t2:s12 "lamp" -> object_label::lamp; t2:s14 "bed" -> object_label::bed; t2:s16 "book" -> object_label::book; t2:s16 "bed" -> object_label::bed; t2:s16 "stuffed bear" -> object_label::bear
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
