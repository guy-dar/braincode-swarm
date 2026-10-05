Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object=food_label::potato, verb="place") -> activity_2 : TERM
    CLAIM request(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM sequence(items=[activity_2]) -> sequence_2 : TERM
    UTTER respond(target=sequence_2)
    ACTION walk(destination=object_label::microwave)
    ACTION face(target=object_label::microwave)
    ACTION pick_up(target=food_label::potato, source=object_label::microwave) -> potato_ref : REF[STRING]
    ACTION remove(target=potato_ref)
    ACTION walk(destination=object_label::sink)
    ACTION face(target=object_label::sink)
    ACTION rinse(target=potato_ref, destination=object_label::sink) -> potato_ref_2 : REF[STRING]
    ACTION remove(target=potato_ref_2)
    ACTION walk(destination=object_label::fridge)
    ACTION face(target=object_label::fridge)
    ACTION place(target=potato_ref_2, destination=object_label::fridge, relation=in)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, role_user | covered |
| n2 | action | place, in, activity | covered |
| n3 | object | food_label::potato | label-preserved |
| n4 | constraint | rinse | covered |
| n5 | object | object_label::fridge | label-preserved |
| n6 | temporal | sequence, respond | covered |
| n7 | action | walk, face | covered |
| n8 | object | object_label::microwave | label-preserved |
| n9 | action | remove | covered |
| n10 | object | food_label::potato | label-preserved |
| n11 | object | object_label::microwave | label-preserved |
| n12 | action | walk, face | covered |
| n13 | object | object_label::sink | label-preserved |
| n14 | action | rinse | covered |
| n15 | action | remove | covered |
| n16 | object | food_label::potato | label-preserved |
| n17 | object | object_label::sink | label-preserved |
| n18 | action | walk, face | covered |
| n19 | object | object_label::fridge | label-preserved |
| n20 | action | place, in | covered |
| n21 | object | food_label::potato | label-preserved |
| n22 | object | object_label::fridge | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: t1:s1–t2:s12
- Opaque-text spans: none
- Label-preserved spans: food_label::potato (t1:s1, t2:s4, t2:s8, t2:s12), object_label::fridge (t1:s1, t2:s10, t2:s12), object_label::microwave (t2:s2, t2:s4), object_label::sink (t2:s6, t2:s8)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: passed
