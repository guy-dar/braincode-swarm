```braincode
TERM  subject(kind="Anne", qualifier="nice") -> anne_nice : TERM
TERM negation(target=anne_nice) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
