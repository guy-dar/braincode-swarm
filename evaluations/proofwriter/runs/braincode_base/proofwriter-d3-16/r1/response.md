```braincode
TERM  activity(verb="need", actor="rabbit", object=animal_label::red) -> need_red : TERM
TERM  negation(target=need_red) -> q : TERM
TERM  negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
