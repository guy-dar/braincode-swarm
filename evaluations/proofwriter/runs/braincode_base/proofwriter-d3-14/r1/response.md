```braincode
TERM  character_trait(property="temperament", value="rough") -> rough_charlie : TERM
TERM negation(target=rough_charlie) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
