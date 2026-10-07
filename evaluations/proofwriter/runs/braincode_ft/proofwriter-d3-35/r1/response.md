```braincode
TERM  subject(kind="Bob") -> bob : TERM
TERM property_question(property="quiet", subject=bob) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
