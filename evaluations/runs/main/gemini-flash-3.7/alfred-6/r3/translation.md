Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(instrument=object_label::lamp, object=object_label::book, verb="read") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    ACTION walk(destination=object_label::bed, relation=in_front_of)
    TERM requirement(property="title", value="Probabilistic Robotics") -> requirement_2 : TERM
    ACTION pick_up(target=object_label::book, color=color_label::blue, source=object_label::bed) -> book_ref : REF[STRING]
    ACTION turn(direction=right_of)
    ACTION walk(destination=object_label::nightstand)
    TERM lexical_label(value=object_label::lamp) -> lexical_label_2 : TERM
    ACTION turn_on(target=lexical_label_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, activity | covered |
| n2 | action | activity | covered |
| n3 | object | object_label::book | label-preserved |
| n4 | object | object_label::lamp | label-preserved |
| n5 | temporal | walk, pick_up, turn, turn_on | covered |
| n6 | action | walk | covered |
| n7 | object | object_label::bed | label-preserved |
| n8 | constraint | in_front_of | covered |
| n9 | action | pick_up | covered |
| n10 | object | object_label::book | label-preserved |
| n11 | constraint | color_label::blue | label-preserved |
| n12 | constraint | source | covered |
| n13 | constraint | requirement | covered |
| n14 | action | turn, right_of | covered |
| n15 | action | walk | covered |
| n16 | object | object_label::nightstand | label-preserved |
| n17 | action | turn_on | covered |
| n18 | object | object_label::lamp | label-preserved |
| n19 | constraint | lexical_label | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s8 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "book" → object_label::book (label only; no sense resolved); t1:s1 "lamp" → object_label::lamp (label only; no sense resolved); t2:s2 "bed" → object_label::bed (label only; no sense resolved); t2:s4 "book" → object_label::book (label only; no sense resolved); t2:s4 "blue" → color_label::blue (label only; no sense resolved); t2:s6 "night stand" → object_label::nightstand (label only; no sense resolved); t2:s8 "lamp" → object_label::lamp (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
