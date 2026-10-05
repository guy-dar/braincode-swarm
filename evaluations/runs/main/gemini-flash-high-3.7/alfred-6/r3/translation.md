Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(instrument=object_label::lamp, object=textbook, verb="read") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    ACTION walk(destination=object_label::bed, relation=in_front_of)
    ACTION pick_up(target=object_label::book, color=color_label::blue, source=object_label::bed) -> object_label_book_ref : REF[STRING]
    ACTION turn(direction="right")
    ACTION walk(destination=night_stand)
    TERM lexical_label(value=object_label::lamp) -> lexical_label_2 : TERM
    ACTION turn_on(target=lexical_label_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, textbook | covered |
| n2 | action | textbook | covered |
| n3 | object | textbook | covered |
| n4 | object | object_label::lamp | label-preserved |
| n5 | temporal | in_front_of | covered |
| n6 | action | walk | covered |
| n7 | object | object_label::bed | label-preserved |
| n8 | constraint | in_front_of | covered |
| n9 | action | pick_up | covered |
| n10 | object | object_label::book | label-preserved |
| n11 | constraint | color_label::blue | label-preserved |
| n12 | constraint | pick_up | covered |
| n13 | constraint | pick_up | covered |
| n14 | action | turn | covered |
| n15 | action | walk | covered |
| n16 | object | night_stand | covered |
| n17 | action | turn_on | covered |
| n18 | object | object_label::lamp | label-preserved |
| n19 | constraint | night_stand | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s8 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "lamp" -> object_label::lamp; t2:s2 "bed" -> object_label::bed; t2:s4 "book" -> object_label::book; t2:s4 "blue" -> color_label::blue; t2:s8 "lamp" -> object_label::lamp
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
