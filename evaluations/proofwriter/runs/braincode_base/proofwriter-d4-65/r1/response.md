```braincode
TERM  attribute_claim(property="shape", subject="Bob", value=shape_round) -> shape_round_claim : TERM
TERM  attribute_claim(property="quiet", subject="Bob", value=TRUE) -> quiet_claim : TERM
CLAIM statement(fact=shape_round_claim) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
