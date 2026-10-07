```braincode
TERM  activity(verb="visit", actor="dog", object=animal_label::mouse) -> visit_mouse : TERM
CLAIM statement(fact=visit_mouse) BY role_agent STATUS inferred SOURCE "theory" -> q : CLAIM

CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
