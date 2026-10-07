```braincode
TERM  lexical_label(value=color_label::red) -> lexical_label_2 : TERM
TERM subject(kind="person", qualifier="big") -> subject_3 : TERM
TERM subject(kind="person", qualifier="smart") -> subject_4 : TERM
TERM conjunction(items=[subject_3, subject_4]) -> conjunction_2 : TERM
TERM subject(kind="person", qualifier="rough") -> subject_5 : TERM
TERM conditional(condition=conjunction_2, consequence=subject_5) -> conditional_2 : TERM
TERM subject(kind="person", qualifier="young") -> subject_6 : TERM
TERM conjunction(items=[subject_6, subject_5]) -> conjunction_3 : TERM
TERM conditional(condition=conjunction_3, consequence=subject_3) -> conditional_3 : TERM
TERM subject(kind="person", qualifier="cold") -> subject_7 : TERM
TERM conditional(condition=subject_7, consequence=subject_4) -> conditional_4 : TERM
TERM subject(kind="person", qualifier="cold") -> subject_8 : TERM
TERM conjunction(items=[subject_8, subject_4]) -> conjunction_4 : TERM
TERM conditional(condition=conjunction_4, consequence=subject_6) -> conditional_5 : TERM
TERM subject(kind="person", qualifier="cold") -> subject_9 : TERM
TERM conjunction(items=[subject_9, subject_5]) -> conjunction_5 : TERM
TERM conditional(condition=conjunction_5, consequence=subject_7) -> conditional_6 : TERM
TERM subject(kind="person", qualifier="cold") -> subject_10 : TERM
TERM conjunction(items=[subject_10, subject_4]) -> conjunction_6 : TERM
TERM conditional(condition=conjunction_6, consequence=subject_6) -> conditional_7 : TERM
TERM subject(kind="person", qualifier="cold") -> subject_11 : TERM
TERM conjunction
```
