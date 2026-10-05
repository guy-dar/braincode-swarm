```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION visualize(target=svg_path) -> svg_path_ref : REF[STRING]
  ACTION search_web(target=svg_path_ref, constraints=LIST[TERM]) -> list_of_shapes : LIST[TERM]
  ACTION pick_up(target=list_of_shapes, quantity=10, source=task_description) -> selected_shapes : LIST[TERM]
  ACTION sort(target=selected_shapes, order=rank_direction) -> sorted_shapes : LIST[TERM]
  ACTION select_option(target=sorted_shapes, value=option_A) -> final_answer : TERM
  ACTION send_email(target=final_answer) -> email_sent : EVENT
}
```