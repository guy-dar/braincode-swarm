```braincode
TERM  activity(verb="see", actor="bear", object=animal_label::cat) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
```
