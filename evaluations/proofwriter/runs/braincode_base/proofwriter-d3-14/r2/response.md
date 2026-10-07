```braincode
TERM  character_trait(property="temperament", value="rough") -> rough_trait : TERM
TERM subject(kind="Charlie", qualifier=rough_trait) -> charlie_rough : TERM
TERM negation(target=charlie_rough) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
