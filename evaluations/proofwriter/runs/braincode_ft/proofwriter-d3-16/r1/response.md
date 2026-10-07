```braincode
TERM  lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM  subject(kind="rabbit", qualifier=lexical_label_2) -> subject_2 : TERM
TERM  negation(target=subject_2) -> q : TERM
TERM  negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
