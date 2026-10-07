```braincode
TERM  character(name="Fiona") -> character_fiona : TERM
TERM  subject(kind="Fiona", qualifier="round") -> subject_fiona_round : TERM
TERM  negation(target=subject_fiona_round) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
