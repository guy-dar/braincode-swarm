```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION pick_up(target=mug) -> mug_ref : REF[STRING]
  ACTION rinse(target=mug_ref, destination=sink) -> mug_ref_2 : REF[STRING]
  ACTION place(target=mug_ref_2, destination=coffee_maker)
}
```