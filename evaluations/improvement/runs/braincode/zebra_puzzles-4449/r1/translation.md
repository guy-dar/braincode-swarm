```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelPillow
TASK ObjectLabelPillow {
  ACTION pick_up(target=object_label::pillow, quantity=6) -> object_label_pillow_refs : LIST[REF[STRING]]
  FOR EACH item IN object_label_pillow_refs {
    ACTION place(target=item, destination=object_label::armchair, relation=on)
  }
}
```