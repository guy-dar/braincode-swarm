```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION determine_truth(target=Delbert, Sima, Crista) -> result : LIST[STRING]
  ACTION ask(target=result, format=LIST[STRING], audience=USER) -> answer : LIST[STRING]
  ACTION format_answer(target=answer, value=STRING) -> formatted_answer : STRING
}
```