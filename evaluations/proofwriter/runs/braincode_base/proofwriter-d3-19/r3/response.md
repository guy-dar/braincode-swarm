```braincode
TERM  activity(verb="like", actor="lion", object=animal_label::lion) -> like_lion : TERM
TERM negation(target=like_lion) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
