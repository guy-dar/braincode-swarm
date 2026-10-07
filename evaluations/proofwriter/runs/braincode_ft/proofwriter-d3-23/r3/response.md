```braincode
TERM  subject(kind="theory") -> subject_2 : TERM
TERM  subject(kind="Anne", qualifier=role_user) -> subject_3 : TERM
TERM  subject(kind="Bob", qualifier=role_user) -> subject_4 : TERM
TERM  subject(kind="Gary", qualifier=role_user) -> subject_5 : TERM
TERM  subject(kind="Harry", qualifier=role_user) -> subject_6 : TERM
TERM  subject(kind="young") -> subject_7 : TERM
TERM  subject(kind="color", qualifier=color_label::red) -> subject_8 : TERM
TERM  requirement(property="young", value=TRUE) -> requirement_2 : TERM
TERM  requirement(property="color", value=color_label::red) -> requirement_3 : TERM
TERM  requirement(property="smart", value=TRUE) -> requirement_4 : TERM
TERM  requirement(property="kind", value=TRUE) -> requirement_5 : TERM
TERM  requirement(property="rough", value=TRUE) -> requirement_6 : TERM
TERM  requirement(property="thermal_state", value=state_cold) -> requirement_7 : TERM
TERM  requirement(property="color", value=color_label::blue) -> requirement_8 : TERM
TERM  conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
TERM  conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_2 : TERM
TERM  conjunction(items=[requirement_6, requirement_7]) -> conjunction_3 : TERM
TERM  conditional(condition=conjunction_3, consequence=requirement_5) -> conditional_3 : TERM
TERM  conjunction(items=[requirement_4, requirement_5]) -> conjunction_4 : TERM
TERM  conditional(condition=conjunction_4, consequence=requirement_2) -> conditional_4 : TERM
TERM  conjunction(items=[requirement_6, requirement_8
```
