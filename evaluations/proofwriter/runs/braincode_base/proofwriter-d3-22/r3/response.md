```braincode
TERM  activity(verb="chase", actor="squirrel", object=animal_label::cow) -> chase_squirrel_cow : TERM
TERM negation(target=chase_squirrel_cow) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
