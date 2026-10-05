Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Knife
TASK Knife {
  ACTION turn(direction="left")
  ACTION walk(destination=object_label::sink)
  ACTION face(target=object_label::sink)

  ACTION pick_up(target=object_label::knife, source=object_label::sink) -> knife_ref : REF[STRING]

  ACTION turn(direction="around")
  ACTION walk(destination=food_label::lettuce)
  ACTION face(target=food_label::lettuce)

  # PROPOSED: S1  (need a constructor to describe the lettuce on the counter)
  TERM object_at_location(object=food_label::lettuce, location=object_label::counter) -> lettuce_on_counter : TERM
  ACTION slice(target=lettuce_on_counter) -> lettuce_slice_ref : REF[STRING]

  ACTION turn(direction="around")
  ACTION walk(destination=object_label::counter)
  ACTION face(target=object_label::counter)

  ACTION place(target=knife_ref, destination=object_label::counter)

  ACTION turn(direction="around")
  ACTION walk(destination=food_label::lettuce)
  ACTION face(target=food_label::lettuce)

  ACTION pick_up(target=food_label::lettuce, state=state_sliced, source=object_label::counter) -> lettuce_slice_ref_2 : REF[STRING]

  ACTION turn(direction="around")
  ACTION walk(destination=object_label::fridge)
  ACTION face(target=object_label::fridge)

  ACTION chill(target=lettuce_slice_ref_2, destination=object_label::fridge) -> lettuce_slice_ref_3 : REF[STRING]
  ACTION remove(target=lettuce_slice_ref_3, source=object_label::fridge)

  ACTION place(target=lettuce_slice_ref_3, destination=object_label::counter, relation=right_of)
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | chill | covered |
| n2 | object | food_label::lettuce, state_sliced | covered |
| n3 | action | place | covered |
| n4 | object | object_label::counter | covered |
| n5 | action | turn, walk, face | covered |
| n6 | object | object_label::sink | covered |
| n7 | action | pick_up | covered |
| n8 | object | object_label::knife | covered |
| n9 | action | turn, walk, face | covered |
| n10 | object | food_label::lettuce | covered |
| n11 | action | slice (via object_at_location) | proposed |
| n12 | action | turn, walk | covered |
| n13 | action | place | covered |
| n14 | action | turn, walk, face | covered |
| n15 | action | pick_up | covered |
| n16 | action | turn, walk, face | covered |
| n17 | object | object_label::fridge | covered |
| n18 | action | chill, remove | covered |
| n19 | action | turn, walk, face | covered |
| n20 | action | place | covered |

## Why the translation failed

- n11 "cut the lettuce on the counter into slices": no existing TERM constructor describes an object at a location for use with `slice(target: TERM)`. `slice` requires a REF or TERM; `food_label::lettuce` and `object_label::lettuce` are ATOMs, not TERM. No suitable constructor like `object_at_location` exists. See suggestion S1.

## Translation report

- Input kind: prompt
- Coverage status: partial
- Source-span coverage: every segment t1:s1–t2:s24 is represented, except t2:s8 requires the proposed constructor S1
- Opaque-text spans: none
- Missing constructs: S1 object_at_location constructor
- Unresolved ambiguities: none
- Check: `rag check` reported 1 unresolved need (n11), 1 unknown symbol (object_at_location)