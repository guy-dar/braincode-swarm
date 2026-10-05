Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Lettuce
TASK Lettuce {
  ACTION pick_up(target=food_label::lettuce, source=object_label::counter) -> lettuce_ref : REF[STRING]
  ACTION slice(target=lettuce_ref) -> lettuce_slice_ref : REF[STRING]
  ACTION chill(target=lettuce_slice_ref, destination=object_label::fridge) -> chilled_ref : REF[STRING]  # PROPOSED: S1
  ACTION remove(target=chilled_ref, source=object_label::fridge)
  ACTION place(target=lettuce_slice_ref, destination=object_label::counter, relation=right_of)
}
```

## Needs coverage

| need | kind   | expressed by                                   | status    |
|------|--------|-------------------------------------------------|-----------|
| n1   | action | chill                                          | proposed  |
| n2   | object | food_label::lettuce                            | covered   |
| n3   | action | place                                          | covered   |
| n4   | object | object_label::counter                          | covered   |
| n5   | action | —                                               | not-applicable |
| n6   | object | —                                               | not-applicable |
| n7   | action | —                                               | not-applicable |
| n8   | object | —                                               | not-applicable |
| n9   | action | —                                               | not-applicable |
| n10  | object | food_label::lettuce                            | covered   |
| n11  | action | slice                                          | covered   |
| n12  | action | —                                               | not-applicable |
| n13  | action | —                                               | not-applicable |
| n14  | action | —                                               | not-applicable |
| n15  | action | —                                               | not-applicable |
| n16  | action | —                                               | not-applicable |
| n17  | object | object_label::fridge                           | covered   |
| n18  | action | remove, place                                  | covered   |
| n19  | action | —                                               | not-applicable |
| n20  | action | place                                          | covered   |

## Why the translation failed

- n1 “cool a lettuce slice” (t1:s1): no existing operation encodes cooling or chilling. Searched “cool lettuce slice” → no matching operation; widened “chill” → none found.

## Translation report

- Input kind: prompt
- Coverage status: partial
- Source-span coverage: t1:s1 (“cool a lettuce slice” → proposed chill; “place it on the counter” → place); navigation steps omitted as not requested.
- Opaque-text spans: none
- Missing constructs: S1 chill operation
- Unresolved ambiguities: none
- Check: `rag check` reported 1 unresolved need (n1) and 1 unknown symbol (chill)