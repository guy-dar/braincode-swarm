```braincode
TERM  activity(verb="chase", actor="squirrel", object=animal_label::cow) -> chase_cow : TERM
TERM negation(target=chase_cow) -> q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
