Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Textbook
TASK Textbook {
  ACTION walk(destination=bed, relation=in_front_of)
  ACTION pick_up(target=textbook, color=color_label::blue, source=bed) -> textbook_ref : REF[STRING]
  ACTION turn(direction="right")
  ACTION walk(destination=night_stand)
  ACTION turn_on(target=lamp)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | TASK | covered |
| n2 | action | textbook | covered |
| n3 | object | textbook | covered |
| n4 | object | lamp | covered |
| n5 | temporal | TASK | covered |
| n6 | action | walk, bed | covered |
| n7 | object | bed | covered |
| n8 | constraint | in_front_of | covered |
| n9 | action | pick_up | covered |
| n10 | object | textbook | covered |
| n11 | constraint | color_label::blue | label-preserved |
| n12 | constraint | bed | covered |
| n13 | constraint | textbook | covered |
| n14 | action | turn | covered |
| n15 | action | walk, night_stand | covered |
| n16 | object | night_stand | covered |
| n17 | action | turn_on, lamp | covered |
| n18 | object | lamp | covered |
| n19 | constraint | night_stand | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s8 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s4 "blue" -> color_label::blue (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unknown symbols
