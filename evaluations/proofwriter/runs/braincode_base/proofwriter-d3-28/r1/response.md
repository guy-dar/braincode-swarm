```braincode
TERM  activity(actor="mouse", object=animal_label::lion, verb="visit") -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=negation(target=q)) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
