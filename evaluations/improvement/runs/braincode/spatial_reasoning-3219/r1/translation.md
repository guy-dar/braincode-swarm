```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION search_web(target="cousin_of_hat") -> search_result : TERM
  ACTION pick_up(target=search_result) -> target_ref : REF[STRING]
  ACTION format_structured_report(target_ref, format="object_name") -> report : STRING
  RETURN report : STRING
}
```