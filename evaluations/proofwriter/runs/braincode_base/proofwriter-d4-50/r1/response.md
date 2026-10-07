```braincode
TERM  attribute_claim(property="color", subject="Bob", value=color_label::red) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
