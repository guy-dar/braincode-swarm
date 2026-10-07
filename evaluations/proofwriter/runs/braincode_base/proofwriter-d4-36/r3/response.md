```braincode
TERM  activity(actor="bear", object=animal_label::cat, verb="see") -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
