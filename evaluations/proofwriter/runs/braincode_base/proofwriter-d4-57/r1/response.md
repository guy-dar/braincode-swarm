```braincode
TERM  activity(actor="mouse", object=animal_label::tiger, verb="see") -> see_mouse_tiger : TERM
TERM negation(target=see_mouse_tiger) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
