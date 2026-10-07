```braincode
TERM  lexical_label(value=color_label::red) -> lexical_label_2 : TERM
TERM subject(kind="person", qualifier=lexical_label_2) -> subject_2 : TERM
TERM subject(kind="person", qualifier="quiet") -> subject_3 : TERM
TERM conjunction(items=[subject_2, subject_3]) -> conjunction_2 : TERM
TERM conditional(condition=conjunction_2, consequence=subject_2) -> conditional_2 : TERM
TERM property_question(property="truth_value", subject=conditional_2) -> property_question_2 : TERM
TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
UTTER ask(target=property_question_2, constraints=[constraint_single_choice_2])
```
