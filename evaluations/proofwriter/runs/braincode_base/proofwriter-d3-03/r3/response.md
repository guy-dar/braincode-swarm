```braincode
TERM  activity(actor="bear", object=animal_label::eagle, verb="need") -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=TERM negation(target=q)) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
