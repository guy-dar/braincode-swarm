```braincode
TERM  not_rough_bob : TERM
TERM negation(target=rough_bob) -> not_rough_bob : TERM
CLAIM statement(fact=not_rough_bob) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=rough_bob) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
