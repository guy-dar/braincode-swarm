```braincode
TERM  subject(kind="Bob", qualifier=size_large) -> bob_large : TERM
TERM negation(target=bob_large) -> neg_bob_large : TERM
TERM property_question(property="truth_value", subject=neg_bob_large) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
