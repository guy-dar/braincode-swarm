```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION extract(target=LIST[REF[STRING]], limit=35) -> null_values : LIST[REF[STRING]]
  ACTION pick_up(target=null_values, quantity=18) -> table_data : REF[STRING]
  ACTION place(destination=table_data, relation="table") -> table : REF[STRING]
  ACTION sort(target=table, rank_direction="asc", rank_field="coding_minutes") -> sorted_table : LIST[REF[STRING]]
  ACTION wait(duration=2) -> void
  ACTION calculate(inputs=sorted_table, operation="sum", result=0) -> sum_coding_minutes : TERM
  ACTION calculate(inputs=sorted_table, operation="sum", result=0) -> sum_study_minutes : TERM
  ACTION between(target=sum_coding_minutes, value=sum_study_minutes, criterion="coding_minutes") -> difference : TERM
  ACTION at_most(target=difference, measure=2) -> rounded_difference : TERM
  ACTION condition(condition=rounded_difference, expected=0) -> condition_satisfied : CLAIM
  ACTION test_condition(condition=condition_satisfied, expected=TRUE) -> test_result : CLAIM
  ACTION raises_exception(target=test_result, exception_type="RuntimeError", message="Condition cannot be determined") -> exception : CLAIM
  ACTION outcome(event=exception, value="0") -> outcome : CLAIM
  RETURN outcome
}
```