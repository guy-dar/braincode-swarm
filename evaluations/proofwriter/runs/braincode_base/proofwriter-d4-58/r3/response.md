```braincode
TERM  activity(verb="like", actor="tiger", object=animal_label::tiger) -> like_tiger : TERM
TERM negation(target=like_tiger) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
