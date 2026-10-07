```braincode
TERM  subject(kind="Harry", qualifier=role_user) -> subject_harry : TERM
TERM negation(target=subject_harry) -> negation_harry : TERM
CLAIM statement(fact=negation_harry) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
