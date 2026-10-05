```braincode
MODE REQUEST
ENTRYPOINT Meeting
TASK Meeting {
  ACTION search_travel(target="meeting", constraints=[
    requirement(property="time", value="9:00"),
    requirement(property="time", value="17:00"),
    requirement(property="day", value="Monday"),
    requirement(property="day", value="Tuesday"),
    requirement(property="day", value="Wednesday"),
    requirement(property="day", value="Thursday"),
    requirement(property="day", value="Friday")
  ],
  location="local")
  -> meeting_options : LIST[REF[STRING]]

  ACTION search_travel(target="meeting", constraints=[
    requirement(property="time", value="9:00"),
    requirement(property="time", value="17:00"),
    requirement(property="day", value="Monday"),
    requirement(property="duration", value="1 hour"),
    requirement(property="duration", value="at most 1 hour")
  ],
  location="local")
  -> short_meetings : LIST[REF[STRING]]

  ACTION search_travel(target="meeting", constraints=[
    requirement(property="time", value="17:00"),
    requirement(property="time", value="18:00"),
    requirement(property="day", value="Wednesday")
  ],
  location="local")
  -> lunch_break : LIST[REF[STRING]]

  ACTION search_travel(target="meeting", constraints=[
    requirement(property="duration", value="10 minutes"),
    requirement(property="duration", value="at most 10 minutes")
  ],
  location="local")
  -> flexible_attendee : LIST[REF[STRING]]

  ACTION calculate(duration=60, unit="minutes")
  -> longest_meeting_duration : NUMBER

  ACTION calculate(duration=60, unit="minutes")
  -> possible_meetings_count : NUMBER

  ACTION generate(target="meeting", constraints=[
    requirement(property="time", value="9:00"),
    requirement(property="time", value="17:00"),
    requirement(property="day", value="Monday"),
    requirement(property="day", value="Tuesday"),
    requirement(property="day", value="Wednesday"),
    requirement(property="day", value="Thursday"),
    requirement(property="day", value="Friday")
  ],
  constraints=[
    requirement(property="duration", value=longest_meeting_duration),
    requirement(property="duration", value=possible_meetings_count)
  ],
  topic="meeting")
  -> meeting : STRING

  RETURN meeting
}
```