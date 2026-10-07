```braincode
TERM  subject(kind="person", qualifier=shape_round) -> subject_4 : TERM
TERM negation(target=subject_4) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
