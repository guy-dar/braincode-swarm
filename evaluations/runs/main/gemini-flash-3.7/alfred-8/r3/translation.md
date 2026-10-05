Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    ACTION pick_up(target=object_label::book, quantity=2, source=desk) -> book_refs : LIST[REF[STRING]]
    FOR EACH item IN book_refs {
      ACTION place(target=item, destination=bed, relation=on)
    }
  }
  TURN t2 SPEAKER=AGENT {
    ACTION turn(direction="around")
    ACTION walk(destination=object_label::room)
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    ACTION turn(direction="right")
    ACTION walk(destination=trash_can, relation=in_front_of)
    ACTION walk(destination=desk)
    TERM lexical_label(value=object_label::book) -> lexical_label_3 : TERM
    TERM lexical_label(value=object_label::mug) -> lexical_label_4 : TERM
    TERM spatial_constraint(object=lexical_label_3, reference=lexical_label_4, relation=right_of) -> spatial_constraint_2 : TERM
    ACTION pick_up(target=object_label::book, source=desk) -> book_ref : REF[STRING]
    ACTION turn(direction="right")
    ACTION walk(destination=bed)
    ACTION place(target=book_ref, destination=bed, location=laptop, relation=in_front_of)
    ACTION turn(direction="around")
    ACTION walk(destination=desk)
    TERM lexical_label(value=object_label::lamp) -> lexical_label_5 : TERM
    TERM spatial_constraint(object=lexical_label_3, reference=lexical_label_5, relation=right_of) -> spatial_constraint_3 : TERM
    ACTION pick_up(target=object_label::book, source=desk) -> book_ref_2 : REF[STRING]
    ACTION turn(direction="right")
    ACTION walk(destination=bed)
    ACTION place(target=book_ref_2, destination=bed, location=object_label::bear, relation=other_side_of)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ACTION walk, ACTION place | covered |
| n2 | action | ACTION pick_up, ACTION place, ACTION walk | covered |
| n3 | object | object_label::book | label-preserved |
| n4 | constraint | quantity=2 | covered |
| n5 | object | desk | covered |
| n6 | object | bed | covered |
| n7 | action | ACTION turn(direction="around") | covered |
| n8 | action | ACTION walk(destination=object_label::room) | covered |
| n9 | object | object_label::room | label-preserved |
| n10 | action | ACTION turn(direction="right") | covered |
| n11 | constraint | relation=in_front_of, trash_can | covered |
| n12 | constraint | color_label::green | label-preserved |
| n13 | object | trash_can | covered |
| n14 | action | ACTION walk(destination=desk) | covered |
| n15 | object | desk | covered |
| n16 | action | ACTION pick_up | covered |
| n17 | object | object_label::book | label-preserved |
| n18 | constraint | spatial_constraint, right_of, mug | covered |
| n19 | object | object_label::mug | label-preserved |
| n20 | action | ACTION turn(direction="right") | covered |
| n21 | action | ACTION walk(destination=bed) | covered |
| n22 | object | bed | covered |
| n23 | action | ACTION place | covered |
| n24 | object | object_label::book | label-preserved |
| n25 | object | bed | covered |
| n26 | constraint | relation=in_front_of, location=laptop | covered |
| n27 | object | laptop | covered |
| n28 | action | ACTION turn(direction="around") | covered |
| n29 | action | ACTION walk(destination=desk) | covered |
| n30 | object | desk | covered |
| n31 | action | ACTION pick_up | covered |
| n32 | object | object_label::book | label-preserved |
| n33 | constraint | spatial_constraint, right_of, lamp | covered |
| n34 | object | lamp | covered |
| n35 | action | ACTION turn(direction="right") | covered |
| n36 | action | ACTION walk(destination=bed) | covered |
| n37 | object | bed | covered |
| n38 | action | ACTION place | covered |
| n39 | object | object_label::book | label-preserved |
| n40 | object | bed | covered |
| n41 | constraint | relation=other_side_of, location=object_label::bear | covered |
| n42 | object | object_label::bear | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s16 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "book" → object_label::book; t2:s2 "room" → object_label::room; t2:s2 "green" → color_label::green; t2:s4 "book" → object_label::book; t2:s4 "coffee mug" → object_label::mug; t2:s8 "book" → object_label::book; t2:s12 "book" → object_label::book; t2:s16 "book" → object_label::book; t2:s16 "stuffed bear" → object_label::bear
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
