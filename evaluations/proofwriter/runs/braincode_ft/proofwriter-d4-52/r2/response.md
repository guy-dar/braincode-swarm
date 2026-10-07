```braincode
TERM  character(name="Fiona") -> char_fiona : TERM
TERM  subject(kind="Fiona", qualifier="round") -> subj_fiona_round : TERM
TERM  negation(target=subj_fiona_round) -> neg_fiona_round : TERM
CLAIM statement(fact=neg_fiona_round) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
