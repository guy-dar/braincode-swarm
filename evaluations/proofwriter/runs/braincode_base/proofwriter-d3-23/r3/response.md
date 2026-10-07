```braincode
TERM  attribute_claim(property="smart", subject="Gary", value=FALSE) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
