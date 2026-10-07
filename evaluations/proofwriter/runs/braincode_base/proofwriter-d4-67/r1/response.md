```braincode
TERM  subject(kind="Charlie", qualifier="young") -> young_charlie : TERM
TERM negation(target=young_charlie) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
