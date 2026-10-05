```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION send_message(recipient=role_agent, content="Determine if Fidel, Gwenn, and Sal tell the truth.") -> message_ref : REF[STRING]
  ACTION generate(target=art_short_text, format=format_plain_text, tone=tone_neutral) -> short_text : STRING
  ACTION send_message(recipient=role_agent, content=short_text)
}
```