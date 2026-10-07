```braincode
TERM  activity(verb="chase", actor="mouse", object=animal_label::lion) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
