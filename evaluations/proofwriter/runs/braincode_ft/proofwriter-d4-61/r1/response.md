```braincode
TERM  lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM subject(kind="Dave", qualifier=lexical_label_2) -> subject_2 : TERM
TERM subject(kind="Dave", qualifier="quiet") -> subject_3 : TERM
TERM subject(kind="Dave", qualifier="young") -> subject_4 : TERM
TERM lexical_label(value=color_label::blue) -> lexical_label_3 : TERM
TERM subject(kind="Erin", qualifier=lexical_label_3) -> subject_5 : TERM
TERM subject(kind="Erin", qualifier="white") -> subject_6 : TERM
TERM subject(kind="Gary", qualifier="quiet") -> subject_7 : TERM
TERM subject(kind="Harry", qualifier=lexical_label_3) -> subject_8 : TERM
TERM subject(kind="cold") -> subject_9 : TERM
TERM subject(kind="green") -> subject_10 : TERM
TERM conjunction(items=[subject_9, subject_10]) -> conjunction_2 : TERM
TERM subject(kind="thing", qualifier="kind") -> subject_11 : TERM
TERM conditional(condition=conjunction_2, consequence=subject_11) -> conditional_2 : TERM
TERM subject(kind="quiet") -> subject_12 : TERM
TERM conditional(condition=subject_12, consequence=subject_11) -> conditional_3 : TERM
TERM subject(kind="cold") -> subject_13 : TERM
TERM conditional(condition=subject_13, consequence=subject_12) -> conditional_4 : TERM
TERM conjunction(items=[subject_12, conditional_4]) -> conjunction_3 : TERM
TERM subject(kind="thing", qualifier="white") -> subject_14 : TERM
TERM conditional(condition=conjunction_3, consequence=subject_14) -> conditional_5 : TERM
TERM subject(kind="cold") -> subject_15 : TERM
```
