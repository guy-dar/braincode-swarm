```braincode
TERM  subject(kind="Anne", qualifier="nice") -> subject_2 : TERM
TERM  negation(target=subject_2) -> q : TERM
TERM  subject(kind="Anne", qualifier="nice") -> subject_3 : TERM
TERM  negation(target=subject_3) -> not_q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
