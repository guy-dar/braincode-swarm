```braincode
TERM  activity(verb="like", actor="tiger", object=animal_label::tiger) -> like_tiger : TERM
TERM negation(target=like_tiger) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
