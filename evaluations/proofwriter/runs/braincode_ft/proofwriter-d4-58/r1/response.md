```braincode
TERM  activity(verb="like", actor="tiger", object="tiger") -> like_tiger : TERM
TERM negation(target=like_tiger) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
```
