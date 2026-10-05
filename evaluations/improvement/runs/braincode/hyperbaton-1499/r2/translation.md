```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION search_web(target="correct_adjective_order", criteria=[
    "correct_adjective_order",
    "sentence",
    "adjective",
    "noun",
    "adjective",
    "noun",
    "adjective",
    "noun",
    "adjective",
    "noun"
  ])
  -> search_results : LIST[REF[STRING]]
  ACTION sort(
    target=search_results,
    rank_direction="asc",
    rank_field="correct_adjective_order"
  )
  -> sorted_results : LIST[REF[STRING]]
  ACTION extract(
    target=sorted_results,
    limit=1
  )
  -> final_answer : STRING
  RETURN final_answer
}
```