```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION sort(target=LIST[REF[STRING]], rank_direction="dir_asc", rank_field="alphabetical_order") -> sorted_words : LIST[REF[STRING]]
  ACTION place(destination=sorted_words, separator=",") -> result : REF[STRING]
  ACTION generate(target=result, format="csv") -> artifact : TERM
  CLAIM artifact BY system STATUS asserted SOURCE "glossary" -> artifact : TERM
  ACTION action(action=artifact, result=artifact) -> artifact : TERM
  CLAIM artifact BY system STATUS asserted SOURCE "glossary" -> artifact : TERM
}
```