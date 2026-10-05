Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object=food_label::potato, verb="place") -> activity_2 : TERM
    UTTER propose(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(object=object_label::microwave, verb="walk") -> activity_3 : TERM
    TERM activity(object=object_label::microwave, verb="face") -> activity_4 : TERM
    TERM activity(object=food_label::potato, verb="remove") -> activity_5 : TERM
    TERM activity(object=object_label::sink, verb="walk") -> activity_6 : TERM
    TERM activity(object=object_label::sink, verb="face") -> activity_7 : TERM
    TERM activity(object=food_label::potato, verb="wash") -> activity_8 : TERM
    TERM activity(object=food_label::potato, verb="remove") -> activity_9 : TERM
    TERM activity(object=object_label::fridge, verb="walk") -> activity_10 : TERM
    TERM activity(object=object_label::fridge, verb="face") -> activity_11 : TERM
    TERM activity(object=food_label::potato, verb="place") -> activity_12 : TERM
    TERM sequence(items=[activity_3, activity_4, activity_5, activity_6, activity_7, activity_8, activity_9, activity_10, activity_11, activity_12]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | propose | covered |
| n2 | action | activity | covered |
| n3 | object | food_label::potato | label-preserved |
| n4 | constraint | activity | covered |
| n5 | object | object_label::fridge | label-preserved |
| n6 | temporal | sequence | covered |
| n7 | action | activity | covered |
| n8 | object | object_label::microwave | label-preserved |
| n9 | action | activity | covered |
| n10 | object | food_label::potato | label-preserved |
| n11 | object | object_label::microwave | label-preserved |
| n12 | action | activity | covered |
| n13 | object | object_label::sink | label-preserved |
| n14 | action | activity | covered |
| n15 | action | activity | covered |
| n16 | object | food_label::potato | label-preserved |
| n17 | object | object_label::sink | label-preserved |
| n18 | action | activity | covered |
| n19 | object | object_label::fridge | label-preserved |
| n20 | action | activity | covered |
| n21 | object | food_label::potato | label-preserved |
| n22 | object | object_label::fridge | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s12 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "potato" -> food_label::potato, t1:s1 "fridge" -> object_label::fridge, t2:s2 "microwave" -> object_label::microwave, t2:s4 "potato" -> food_label::potato, t2:s4 "microwave" -> object_label::microwave, t2:s6 "sink" -> object_label::sink, t2:s8 "potato" -> food_label::potato, t2:s8 "sink" -> object_label::sink, t2:s10 "fridge" -> object_label::fridge, t2:s12 "potato" -> food_label::potato, t2:s12 "fridge" -> object_label::fridge
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
