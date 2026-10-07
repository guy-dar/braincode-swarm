```braincode
TERM  attribute_claim(property="color", subject="lion", value=lexical_label_2) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict_negation : CLAIM
```
