```braincode
TERM  lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
TERM  subject(kind="Anne") -> subject_2 : TERM
TERM  attribute_claim(property="color", subject=subject_2, value=lexical_label_2) -> attribute_claim_2 : TERM
TERM  subject(kind="Dave") -> subject_3 : TERM
TERM  attribute_claim(property="color", subject=subject_3, value=lexical_label_2) -> attribute_claim_3 : TERM
TERM  subject(kind="Fiona") -> subject_4 : TERM
TERM  attribute_claim(property="color", subject=subject_4, value=lexical_label_2) -> attribute_claim_4 : TERM
TERM  subject(kind="Gary") -> subject_5 : TERM
TERM  attribute_claim(property="color", subject=subject_5, value=lexical_label_2) -> attribute_claim_5 : TERM
TERM  requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
TERM  requirement(property="size", value=size_large) -> requirement_3 : TERM
TERM  conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
TERM  requirement(property="furry", value=TRUE) -> requirement_4 : TERM
TERM  conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_2 : TERM
TERM  requirement(property="smart", value=TRUE) -> requirement_5 : TERM
TERM  requirement(property="state", value=state_cold) -> requirement_6 : TERM
TERM  conjunction(items=[requirement_5, requirement_6]) -> conjunction_3 : TERM
TERM  conditional(condition=conjunction_3, consequence=requirement_3) -> conditional_3 : TERM
TERM  requirement(property="shape", value=shape_round) -> requirement_7 : TERM
TERM  conjunction(items=[requirement_
```
