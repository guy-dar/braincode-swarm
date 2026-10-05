Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Request
TASK Request {
  ACTION walk(destination=object_label::bed, relation=in_front_of)
  ACTION pick_up(target=object_label::book, color=color_label::blue, source=object_label::bed) -> book_ref : REF[STRING]
  ACTION turn(direction="right")
  ACTION walk(destination=object_label::nightstand)
  TERM lexical_label(value=object_label::lamp) -> lexical_label_2 : TERM
  ACTION turn_on(target=lexical_label_2)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | walk, pick_up, turn, turn_on | covered |
| n2 | action | pick_up, turn_on | covered |
| n3 | object | object_label::book | label-preserved |
| n4 | object | object_label::lamp | label-preserved |
| n5 | temporal | walk, pick_up, turn, turn_on | covered |
| n6 | action | walk | covered |
| n7 | object | object_label::bed | label-preserved |
| n8 | constraint | in_front_of | covered |
| n9 | action | pick_up | covered |
| n10 | object | object_label::book | label-preserved |
| n11 | constraint | color_label::blue | label-preserved |
| n12 | constraint | object_label::bed | covered |
| n13 | constraint | pick_up | covered |
| n14 | action | turn | covered |
| n15 | action | walk | covered |
| n16 | object | object_label::nightstand | label-preserved |
| n17 | action | turn_on | covered |
| n18 | object | object_label::lamp | label-preserved |
| n19 | constraint | walk, object_label::nightstand | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s8 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "book" → object_label::book, t1:s1 "lamp" → object_label::lamp, t2:s2 "bed" → object_label::bed, t2:s4 "book" → object_label::book, t2:s4 "blue" → color_label::blue, t2:s4 "bed" → object_label::bed, t2:s6 "night stand" → object_label::nightstand, t2:s8 "lamp" → object_label::lamp, t2:s8 "night stand" → object_label::nightstand
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
