Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Textbook
TASK Textbook {
  TERM inscribed_text(target=textbook, text="Probabilistic Robotics") -> inscribed_text_2 : TERM   # PROPOSED: S1
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
| n1 | speech_act | lamp, textbook | covered |
| n2 | action | textbook | covered |
| n3 | object | textbook | covered |
| n4 | object | lamp | covered |
| n5 | temporal | in_front_of | covered |
| n6 | action | walk | covered |
| n7 | object | bed | covered |
| n8 | constraint | in_front_of | covered |
| n9 | action | pick_up | covered |
| n10 | object | textbook | covered |
| n11 | constraint | color_label::blue | label-preserved |
| n12 | constraint | bed | covered |
| n13 | constraint | inscribed_text (PROPOSED: S1) | proposed |
| n14 | action | turn | covered |
| n15 | action | walk | covered |
| n16 | object | night_stand | covered |
| n17 | action | turn_on | covered |
| n18 | object | lamp | covered |
| n19 | constraint | night_stand | covered |

## Why the translation failed

- n13 "Titled 'Probabilistic Robotics'": search "title", "book title", "says", "titled", "inscribed" → only document_section (for document sections), art_short_text (artifact type); widen "the book that says Probabilistic Robotics" → no constructor exists to represent title or inscribed text on a physical object/publication. Proposed S1 (inscribed_text).

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: every segment t1:s1–t2:s8 is represented; t2:s4 book title requires proposed constructor inscribed_text
- Opaque-text spans: none
- Label-preserved spans: t2:s4 "blue" → color_label::blue (label only; no sense resolved)
- Missing constructs: S1 inscribed_text constructor
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unknown symbols other than proposed S1
