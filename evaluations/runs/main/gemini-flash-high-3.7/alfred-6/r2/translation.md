Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Textbook
TASK Textbook {
  ACTION walk(destination=bed, relation=in_front_of)
  ACTION pick_up(target=textbook, color=color_label::blue, source=bed, title="Probabilistic Robotics") -> textbook_ref : REF[STRING]   # REFINED: S1
  ACTION turn(direction="right")
  ACTION walk(destination=night_stand)
  ACTION turn_on(target=lamp)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | Textbook | covered |
| n2 | action | Textbook | covered |
| n3 | object | textbook | covered |
| n4 | object | lamp | covered |
| n5 | temporal | walk, pick_up, turn, walk, turn_on | covered |
| n6 | action | walk | covered |
| n7 | object | bed | covered |
| n8 | constraint | in_front_of | covered |
| n9 | action | pick_up | covered |
| n10 | object | textbook | covered |
| n11 | constraint | color_label::blue | label-preserved |
| n12 | constraint | bed | covered |
| n13 | constraint | pick_up.title (REFINED: S1) | proposed |
| n14 | action | turn | covered |
| n15 | action | walk | covered |
| n16 | object | night_stand | covered |
| n17 | action | turn_on | covered |
| n18 | object | lamp | covered |
| n19 | constraint | night_stand | covered |

## Why the translation failed

- n13 "Titled 'Probabilistic Robotics'": search "title", "book title", "the book that says Probabilistic Robotics", "text on object" -> textbook (entity), document_section (report section), art_short_text (text artifact); widen "book title" --kind constraint -> no attribute or parameter in pick_up or general constraint for object title/inscription. Proposed S1 to refine pick_up with title parameter.

## Translation report

- Input kind: prompt
- Coverage status: partial
- Source-span coverage: every segment t1:s1–t2:s8 is represented except the book title constraint in t2:s4 which requires S1
- Opaque-text spans: none
- Label-preserved spans: t2:s4 "blue" -> color_label::blue
- Missing constructs: S1 refine pick_up to accept title?: STRING
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs (1 proposed: n13) and 0 unknown symbols
