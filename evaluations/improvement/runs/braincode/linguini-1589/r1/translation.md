```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION translate(target="the eagle's snake") -> translation : TERM
  ACTION generate(target="translation") -> artifact : TERM
}
```