```braincode
TERM  activity(actor="cat", object=animal_label::mouse, verb="eat") -> eat_mouse : TERM
TERM negation(target=eat_mouse) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
