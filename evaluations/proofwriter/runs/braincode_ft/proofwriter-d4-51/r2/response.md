```braincode
TERM  subject(kind="Harry", qualifier=requirement(property="color", value=color_label::red)) -> subject_harry : TERM
TERM negation(target=subject_harry) -> negation_subject_harry : TERM
CLAIM statement(fact=negation_subject_harry) BY role_agent STATUS hypothesized SOURCE "theory" -> verdict : CLAIM
```
