```braincode
TERM  activity(verb="see", actor="tiger", object=animal_label::mouse) -> see_mouse : TERM
TERM negation(target=see_mouse) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
