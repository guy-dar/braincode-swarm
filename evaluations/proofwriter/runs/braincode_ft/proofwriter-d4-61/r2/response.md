```braincode
TERM  lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM subject(kind="Dave", qualifier=state_cold) -> subject_2 : TERM
TERM subject(kind="Dave", qualifier="kind") -> subject_3 : TERM
TERM conditional(condition=subject_2, consequence=subject_3) -> conditional_2 : TERM
TERM subject(kind="thing", qualifier="quiet") -> subject_4 : TERM
TERM conjunction(items=[subject_2, subject_4]) -> conjunction_2 : TERM
TERM conditional(condition=conjunction_2, consequence=subject_3) -> conditional_3 : TERM
TERM subject(kind="thing", qualifier="young") -> subject_5 : TERM
TERM conjunction(items=[subject_2, subject_5]) -> conjunction_3 : TERM
TERM conditional(condition=conjunction_3, consequence=subject_5) -> conditional_4 : TERM
TERM subject(kind="Harry", qualifier="kind") -> subject_6 : TERM
TERM negation(target=subject_6) -> negation_2 : TERM
TERM conjunction(items=[subject_2, subject_5]) -> conjunction_4 : TERM
TERM subject(kind="Dave", qualifier=state_cold) -> subject_7 : TERM
TERM subject(kind="Dave", qualifier="kind") -> subject_8 : TERM
TERM conditional(condition=subject_7, consequence=subject_8) -> conditional_5 : TERM
CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_2 : CLAIM
CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_3 : CLAIM
CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_4 : CLAIM
CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE
```
