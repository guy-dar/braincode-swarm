```braincode
TERM  subject(kind="quiet_and_cold") -> subject_2 : TERM
TERM requirement(property="quiet_and_cold", value=subject_2) -> requirement_2 : TERM
TERM requirement(property="rely_on_theory", value=TRUE) -> requirement_3 : TERM
TERM conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
TERM negation(target=conjunction_2) -> negation_2 : TERM
TERM requirement(property="rely_only_on_theory", value=TRUE) -> requirement_4 : TERM
TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
TERM requirement(property="statement_in_question", value=negation_2) -> requirement_5 : TERM
TERM requirement(property="rely_only_on_theory", value=TRUE) -> requirement_6 : TERM
TERM requirement(property="statement_in_question", value=requirement_5) -> requirement_7 : TERM
TERM requirement(property="statement_in_question", value=requirement_6) -> requirement_8 : TERM
TERM requirement(property="statement_in_question", value=requirement_7) -> requirement_9 : TERM
TERM requirement(property="statement_in_question", value=requirement_8) -> requirement_10 : TERM
TERM requirement(property="statement_in_question", value=requirement_9) -> requirement_11 : TERM
TERM requirement(property="statement_in_question", value=requirement_10) -> requirement_12 : TERM
TERM requirement(property="statement_in_question", value=requirement_11) -> requirement_13 : TERM
TERM requirement(property="statement_in_question", value=requirement_12) -> requirement_14 : TERM
TERM requirement(property="statement_in_question", value=requirement_13) -> requirement_15 : TERM
TERM requirement(property="statement_in_question", value=requirement_14) -> requirement_16 : TERM
TERM requirement
```
