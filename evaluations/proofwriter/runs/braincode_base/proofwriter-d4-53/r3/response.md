```braincode
TERM  activity(verb="chase", actor="tiger", object=animal_label::lion) -> chase_lion : TERM
TERM negation(target=chase_lion) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
