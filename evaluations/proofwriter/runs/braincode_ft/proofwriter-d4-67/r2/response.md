```braincode
TERM  lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM subject(kind="Bob", qualifier=lexical_label_2) -> subject_3 : TERM
CLAIM statement(fact=subject_3) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
TERM subject(kind="Bob", qualifier="kind") -> subject_4 : TERM
CLAIM statement(fact=subject_4) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
TERM subject(kind="Charlie", qualifier="nice") -> subject_5 : TERM
CLAIM statement(fact=subject_5) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
TERM subject(kind="Erin", qualifier="kind") -> subject_6 : TERM
CLAIM statement(fact=subject_6) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
TERM lexical_label(value=color_label::white) -> lexical_label_3 : TERM
TERM subject(kind="Erin", qualifier=lexical_label_3) -> subject_8 : TERM
CLAIM statement(fact=subject_8) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
TERM subject(kind="Gary", qualifier="young") -> subject_9 : TERM
CLAIM statement(fact=subject_9) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
TERM subject(kind="thing", qualifier="young") -> subject_10 : TERM
TERM subject(kind="thing", qualifier=lexical_label_3) -> subject_11 : TERM
TERM conditional(condition=subject_10, consequence=subject_11) -> conditional_2 : TERM
CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
```
