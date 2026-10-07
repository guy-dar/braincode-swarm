```braincode
TERM  activity(verb="chase", actor="bald eagle", object=animal_label::lion) -> chase_lion : TERM
TERM negation(target=chase_lion) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
