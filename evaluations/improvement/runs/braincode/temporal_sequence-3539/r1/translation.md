```braincode
MODE REQUEST
ENTRYPOINT Meeting
TASK Meeting {
  ACTION schedule_meeting(target=meeting, participants=[Isabella, Sarah, Ava, Charlotte, Sophia]) -> meeting_ref : REF[STRING]
  ACTION generate_meeting_schedule(target=meeting_ref, participants=[Isabella, Sarah, Ava, Charlotte, Sophia]) -> schedule : STRING
  ACTION compute_meeting_length(target=schedule) -> meeting_length : NUMBER
  ACTION compute_meeting_options(target=schedule) -> meeting_options : NUMBER
  GENERATE(target=meeting_length, constraints=[meeting_options], format=comma_separated) -> result : STRING
  RETURN result
}
```