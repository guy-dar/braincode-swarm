```braincode
TERM  subject(kind="Charlie", qualifier="young") -> young_charlie : TERM
TERM negation(target=young_charlie) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
