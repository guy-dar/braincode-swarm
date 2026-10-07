```braincode
TERM  lexical_label(value=color_label::white) -> lexical_label_white : TERM
TERM  lexical_label(value=color_label::blue) -> lexical_label_blue : TERM
TERM  subject(kind="Anne", qualifier="nice") -> subject_anne_nice : TERM
TERM  negation(target=subject_anne_nice) -> negation_anne_nice : TERM
CLAIM statement(fact=negation_anne_nice) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_anne_not_nice : CLAIM
TERM  subject(kind="Anne", qualifier=shape_round) -> subject_anne_round : TERM
CLAIM statement(fact=subject_anne_round) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_anne_round : CLAIM
TERM  subject(kind="Anne", qualifier=lexical_label_white) -> subject_anne_white : TERM
TERM  negation(target=subject_anne_white) -> negation_anne_white : TERM
CLAIM statement(fact=negation_anne_white) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_anne_not_white : CLAIM
TERM  subject(kind="Anne", qualifier="young") -> subject_anne_young : TERM
CLAIM statement(fact=subject_anne_young) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_anne_young : CLAIM
TERM  subject(kind="Erin", qualifier=shape_round) -> subject_erin_round : TERM
CLAIM statement(fact=subject_erin_round) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_erin_round : CLAIM
TERM  subject(kind="Fiona", qualifier=lexical_label_blue) -> subject_fiona_blue : TERM
CLAIM statement(fact=subject_fiona_blue) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_fiona_blue : CLAIM
TERM  subject(kind="Gary", qualifier="young") -> subject_g
```
