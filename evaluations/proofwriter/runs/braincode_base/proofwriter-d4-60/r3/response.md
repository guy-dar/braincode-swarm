```braincode
TERM  character_trait(property="size", value="big") -> trait_big : TERM
TERM negation(target=trait_big) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
