```braincode
MODE REQUEST
ENTRYPOINT Conversation
TASK Translate {
  ACTION translate(target="the eagle's snake") -> result : TERM
  ACTION search_web(target="the eagle's snake") -> results : LIST[TERM]
  ACTION generate(target="the eagle's snake", language="Vai") -> result : TERM
  ACTION pick_up(target="the eagle's snake") -> result : REF[STRING]
  ACTION place(target="the eagle's snake", destination="Vai") -> result : REF[STRING]
  ACTION rinse(target="the eagle's snake") -> result : REF[STRING]
}
```