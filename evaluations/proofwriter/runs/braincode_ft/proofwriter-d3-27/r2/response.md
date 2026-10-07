```braincode
TERM  character(name="Charlie") -> charlie : TERM
TERM property_question(property="age", subject=charlie) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
