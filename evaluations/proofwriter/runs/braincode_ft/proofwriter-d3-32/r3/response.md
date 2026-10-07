```braincode
TERM  subject(kind="Harry", qualifier=requirement(property="color", value=color_label::green)) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
