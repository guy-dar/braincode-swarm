```braincode
TERM  subject(kind="Harry", qualifier=requirement_3) -> subject_3 : TERM
TERM  subject(kind="Harry", qualifier=requirement_4) -> subject_4 : TERM
TERM  subject(kind="Harry", qualifier=requirement_8) -> subject_5 : TERM
TERM  conjunction(items=[subject_3, subject_4, subject_5]) -> conjunction_2 : TERM
TERM  subject(kind="Harry", qualifier=conjunction_2) -> subject_6 : TERM
TERM  subject(kind="Harry", qualifier=requirement_6) -> subject_7 : TERM
TERM  subject(kind="Harry", qualifier=requirement_7) -> subject_8 : TERM
TERM  conjunction(items=[subject_7, subject_8]) -> conjunction_3 : TERM
TERM  subject(kind="Harry", qualifier=conjunction_3) -> subject_9 : TERM
TERM  subject(kind="Harry", qualifier=requirement_9) -> subject_10 : TERM
TERM  conjunction(items=[subject_6, subject_9, subject_10]) -> conjunction_4 : TERM
TERM  subject(kind="Harry", qualifier=conjunction_4) -> subject_11 : TERM
TERM  negation(target=subject_11) -> negation_2 : TERM
CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s18" -> q : CLAIM
```
