```braincode
TERM  activity(verb="like", actor="bald_eagle", object=animal_label::lion) -> like_bald_eagle_lion : TERM
TERM negation(target=like_bald_eagle_lion) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
