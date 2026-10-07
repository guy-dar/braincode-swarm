```braincode
TERM  activity(verb="need", actor="something", object=animal_label::rabbit) -> needs_rabbit : TERM
TERM negation(target=needs_rabbit) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
