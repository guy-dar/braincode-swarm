```braincode
TERM  activity(verb="eat", actor="mouse", object=animal_label::squirrel) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
