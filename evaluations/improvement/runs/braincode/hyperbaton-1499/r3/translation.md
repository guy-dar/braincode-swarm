```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION pick_up(target=task::sentences, quantity=20, source=task::task) -> sentences_refs : LIST[REF[STRING]]
  FOR EACH item IN sentences_refs {
    ACTION place(target=item, destination=task::options, relation=contains)
  }
  ACTION sort(target=task::options, rank_direction=ascending, rank_field=adjective_order) -> options_sorted : LIST[REF[STRING]]
  ACTION pick_up(target=task::options_sorted, quantity=1) -> options_sorted_ref : REF[STRING]
  ACTION place(target=options_sorted_ref, destination=task::final_answer, relation=concatenate)
}
```