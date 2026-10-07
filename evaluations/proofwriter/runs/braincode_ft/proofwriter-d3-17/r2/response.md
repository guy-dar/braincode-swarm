```braincode
TERM  activity(verb="chase", actor="bear", object=animal_label::dog) -> chase_dog : TERM
TERM negation(target=chase_dog) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
