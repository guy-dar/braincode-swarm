```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION determine_truth(target=Delbert, Crista, Sima) -> truth_result : TERM
  ACTION format_answer(target=truth_result, format=LIST[STRING]) -> answer : LIST[STRING]
  ACTION assert_format(format=answer, type=STRING) -> format_result : TERM
  ACTION return_answer(target=format_result) -> final_answer : TERM
}
```