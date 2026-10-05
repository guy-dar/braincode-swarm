Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM described_object(kind=object_label::ottoman) -> described_object_2 : TERM   # PROPOSED: S2
    TERM located(ground=described_object_2, relation=on) -> located_2 : TERM   # PROPOSED: S1
    TERM activity(destination=located_2, object=object_label::keys, verb="place") -> activity_2 : TERM   # PROPOSED: S3
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM activity(direction="left", verb="turn") -> activity_3 : TERM   # PROPOSED: S3
    TERM described_object(kind=object_label::wall) -> described_object_3 : TERM   # PROPOSED: S2
    TERM described_object(kind=object_label::couch) -> described_object_4 : TERM   # PROPOSED: S2
    TERM located(ground=described_object_3, relation=on) -> located_3 : TERM   # PROPOSED: S1
    TERM located(ground=described_object_4, relation=other_side_of) -> located_4 : TERM   # PROPOSED: S1
    TERM described_object(color=color_label::black, constraints=[located_3, located_4], kind=object_label::endtable) -> described_object_5 : TERM   # PROPOSED: S2
    TERM activity(destination=described_object_5, verb="go") -> activity_4 : TERM   # PROPOSED: S3
    UTTER propose(target=activity_3)
    UTTER propose(target=activity_4)
    TERM described_object(color=color_label::white, kind=object_label::vase) -> described_object_6 : TERM   # PROPOSED: S2
    TERM located(ground=described_object_6, relation=behind) -> located_5 : TERM   # PROPOSED: S1
    TERM located(ground=described_object_5, relation=on) -> located_6 : TERM   # PROPOSED: S1
    TERM described_object(constraints=[located_5, located_6], kind=object_label::keys) -> described_object_7 : TERM   # PROPOSED: S2
    TERM activity(object=described_object_7, verb="pick_up") -> activity_5 : TERM
    UTTER propose(target=activity_5)
    TERM activity(direction="around", verb="turn") -> activity_6 : TERM   # PROPOSED: S3
    TERM described_object(kind=object_label::livingroom) -> described_object_8 : TERM   # PROPOSED: S2
    TERM described_object(color=color_label::purple, kind=object_label::ottoman) -> described_object_9 : TERM   # PROPOSED: S2
    TERM activity(destination=described_object_9, verb="go", via=described_object_8) -> activity_7 : TERM   # PROPOSED: S3
    UTTER propose(target=activity_6)
    UTTER propose(target=activity_7)
    TERM located(ground=described_object_9, relation=on) -> located_7 : TERM   # PROPOSED: S1
    TERM described_object(constraints=[located_7], kind=object_label::phone) -> described_object_10 : TERM   # PROPOSED: S2
    TERM located(ground=described_object_10, relation=left_of) -> located_8 : TERM   # PROPOSED: S1
    TERM activity(destination=located_8, object=object_label::keys, verb="place") -> activity_8 : TERM   # PROPOSED: S3
    UTTER propose(target=activity_8)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, ask | covered |
| n2 | object | object_label::keys | label-preserved |
| n3 | object | described_object (PROPOSED: S2), object_label::ottoman | proposed |
| n4 | action | activity (direction PROPOSED: S3), propose | proposed |
| n5 | action | activity (destination PROPOSED: S3) | proposed |
| n6 | constraint | described_object color (PROPOSED: S2) | proposed |
| n7 | object | object_label::endtable | label-preserved |
| n8 | constraint | located (PROPOSED: S1) | proposed |
| n9 | constraint | located relation=other_side_of (PROPOSED: S1) | proposed |
| n10 | object | object_label::couch | label-preserved |
| n11 | action | activity, propose | covered |
| n12 | object | object_label::keys | label-preserved |
| n13 | constraint | located relation=behind (PROPOSED: S1) | proposed |
| n14 | constraint | described_object color (PROPOSED: S2) | proposed |
| n15 | object | object_label::vase | label-preserved |
| n16 | constraint | located relation=on (PROPOSED: S1) | proposed |
| n17 | action | activity direction (PROPOSED: S3) | proposed |
| n18 | action | activity via (PROPOSED: S3) | proposed |
| n19 | object | object_label::livingroom | label-preserved |
| n20 | constraint | described_object color (PROPOSED: S2) | proposed |
| n21 | object | object_label::ottoman | label-preserved |
| n22 | action | activity, propose | proposed |
| n23 | object | object_label::keys | label-preserved |
| n24 | constraint | located relation=left_of (PROPOSED: S1) | proposed |
| n25 | object | object_label::phone | label-preserved |
| n26 | constraint | located relation=on (PROPOSED: S1) | proposed |

## Why the translation failed

- n8/n9/n13/n16/n24/n26 (spatial constraints on described objects): search "on the wall", "across from", "behind the vase" → only spatial-relation STRING values (`on`, `behind`, `left_of`), usable solely as `place.relation`; `location_spec` is geographic. No constructor relates a figure to a ground. Proposed S1.
- n6/n14/n20 and object descriptions (black end table, white vase): `color_label` is accepted only in pick_up.color/search_web.color; no constructor describes an object with colour and constraints. Proposed S2.
- n4/n5/n17/n18 (turn left, go to X, turn around, go through Y to Z): `turn`/`walk` are operations, not TERMs; `activity` has no direction, destination or path role, and `walk.destination` cannot take a described object. Proposed S3.
- n22: the second placement needs a relative placement (left of phone, phone on ottoman) not expressible; same S1/S3.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 and t2:s2–t2:s8 represented; t2:s1, s3, s5, s7 are step numbers (not-applicable, no content).
- Opaque-text spans: none
- Label-preserved spans: keys, ottoman, endtable, couch, vase, living_room, phone, wall as object_label (label only)
- Missing constructs: S1 located; S2 described_object; S3 activity roles
- Unresolved ambiguities: "across from the couch" mapped to other_side_of (could be opposite-facing); "left side of" taken as left_of; agent's instructions treated as proposed (not performed) actions in TRACE; "end table" kept as one label.
- Check: not run clean; proposed symbols unknown by design
