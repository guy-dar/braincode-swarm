```braincode
TERM  activity(verb="like", actor="rabbit", object=animal_label::squirrel) -> like_squirrel : TERM
TERM negation(target=like_squirrel) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
