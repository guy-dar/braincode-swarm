```braincode
TERM  activity(verb="see", actor="tiger", object=animal_label::cow) -> see_cow : TERM
TERM  negation(target=see_cow) -> q : TERM
TERM  negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
