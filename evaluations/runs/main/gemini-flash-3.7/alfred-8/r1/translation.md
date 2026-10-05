Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    ACTION pick_up(target=object_label::book, quantity=2, source=desk) -> object_label_book_refs : LIST[REF[STRING]]
    FOR EACH item IN object_label_book_refs {
      ACTION place(target=item, destination=bed)
    }
  }
  TURN t2 SPEAKER=AGENT {
    ACTION turn(direction="around")
    ACTION walk(destination=object_label::room)
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    ACTION walk(destination=trash_can, relation=in_front_of)
    ACTION turn(direction="right")
    ACTION walk(destination=desk)
    ACTION pick_up(target=object_label::book, source=mug) -> book_ref : REF[STRING]
    ACTION turn(direction="right")
    ACTION walk(destination=bed)
    ACTION place(target=book_ref, destination=bed, location=object_label::computer, relation=in_front_of)
    ACTION turn(direction="around")
    ACTION walk(destination=desk)
    ACTION pick_up(target=object_label::book, source=lamp) -> book_ref_2 : REF[STRING]
    ACTION turn(direction="right")
    ACTION walk(destination=bed)
    ACTION place(target=book_ref_2, destination=bed, location=object_label::bear, relation=other_side_of)
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
| n5 | object | desk | covered |
| n6 | object | bed | covered |
| n7 | action | turn | covered |
| n8 | action | walk | covered |
| n9 | object | object_label::room | label-preserved |
| n10 | action | turn | covered |
| n11 | constraint | trash_can, in_front_of | covered |
| n12 | constraint | color_label::green, lexical_label | label-preserved |
| n13 | object | trash_can | covered |
| n14 | action | walk, desk | covered |
| n15 | object | desk | covered |
| n16 | action | pick_up | covered |
| n17 | object | object_label::book | label-preserved |
| n18 | constraint | in_front_of, mug | covered |
| n19 | object | mug | covered |
| n20 | action | turn | covered |
| n21 | action | walk, bed | covered |
| n22 | object | bed | covered |
| n23 | action | place, bed | covered |
| n24 | object | object_label::book | label-preserved |
| n25 | object | bed | covered |
| n26 | constraint | in_front_of | covered |
| n27 | object | object_label::computer | label-preserved |
| n28 | action | turn | covered |
| n29 | action | walk, desk | covered |
| n30 | object | desk | covered |
| n31 | action | pick_up | covered |
| n32 | object | object_label::book | label-preserved |
| n33 | constraint | in_front_of, lamp, other_side_of | covered |
| n34 | object | lamp | covered |
| n35 | action | turn | covered |
| n36 | action | walk, bed | covered |
| n37 | object | bed | covered |
| n38 | action | place, bed | covered |
| n39 | object | object_label::book | label-preserved |
| n40 | object | bed | covered |
| n41 | constraint | other_side_of | covered |
| n42 | object | object_label::bear | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1 through t2:s16 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "books" -> object_label::book; t2:s2 "room" -> object_label::room; t2:s2 "green" -> color_label::green; t2:s4 "book" -> object_label::book; t2:s8 "book" -> object_label::book; t2:s8 "computer" -> object_label::computer; t2:s12 "book" -> object_label::book; t2:s16 "book" -> object_label::book; t2:s16 "stuffed bear" -> object_label::bear
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
