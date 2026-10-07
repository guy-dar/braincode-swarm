```braincode
TERM  lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM lexical_label(value=color_label::white) -> lexical_label_3 : TERM
TERM subject(kind="Dave", qualifier=lexical_label_2) -> subject_2 : TERM
TERM subject(kind="Erin", qualifier=lexical_label_3) -> subject_3 : TERM
TERM subject(kind="Fiona", qualifier=lexical_label_2) -> subject_4 : TERM
TERM subject(kind="Gary", qualifier=lexical_label_3) -> subject_5 : TERM
TERM requirement(property="furry", value=TRUE) -> requirement_2 : TERM
TERM requirement(property="color", value=lexical_label_2) -> requirement_3 : TERM
TERM requirement(property="kind", value=TRUE) -> requirement_4 : TERM
TERM requirement(property="smart", value=TRUE) -> requirement_5 : TERM
TERM requirement(property="quiet", value=TRUE) -> requirement_6 : TERM
TERM conjunction(items=[requirement_3, requirement_5]) -> conjunction_2 : TERM
TERM conditional(condition=conjunction_2, consequence=requirement_6) -> conditional_2 : TERM
TERM subject(kind="Erin", qualifier=requirement_5) -> subject_6 : TERM
TERM subject(kind="Erin", qualifier=requirement_6) -> subject_7 : TERM
TERM conditional(condition=subject_6, consequence=subject_7) -> conditional_3 : TERM
TERM conjunction(items=[requirement_4, requirement_5]) -> conjunction_3 : TERM
TERM conditional(condition=conjunction_3, consequence=requirement_2) -> conditional_4 : TERM
TERM requirement(property="furry", value=TRUE) -> requirement_7 : TERM
TERM conditional(condition=requirement_7, consequence=requirement_4) -> conditional_5 : TERM
TERM conjunction(items=[requirement_4, requirement_7
```
