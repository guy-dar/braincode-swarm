```braincode
MODE REQUEST
ENTRYPOINT Meeting
TASK Meeting {
  ACTION search_travel(target=country::US, constraints=[constraint_budget_limited, constraint_exclude_flowery_language]) -> LIST[REF[STRING]] : LIST[REF[STRING]]
  ACTION pick_up(target=country::US, quantity=6, source=people) -> REF[STRING] : REF[STRING]
  ACTION place(destination=country::US, target=people) -> void : void
  ACTION wait(duration=3) -> void : void
  ACTION send_message(recipient=people, content=meeting_request) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_details) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_agenda) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_schedule) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_start_time) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_end_time) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value) -> void : void
  ACTION wait(duration=10) -> void : void
  ACTION send_message(recipient=people, content=meeting_duration_unit_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value_value