```braincode
TERM  activity(verb="like", actor="lion", object=animal_label::dog) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=TERM negation(target=q)) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
