```braincode
TERM  lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
TERM activity(verb="kind", actor="bald_eagle") -> activity_2 : TERM
CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
TERM activity(verb="need", actor="bald_eagle", object=animal_label::bear) -> activity_3 : TERM
CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
TERM activity(verb="kind", actor="bear") -> activity_4 : TERM
CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
TERM activity(verb="need", actor="lion", object=animal_label::bear) -> activity_5 : TERM
CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
TERM activity(verb="kind", actor="lion") -> activity_6 : TERM
CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
TERM activity(verb="need", actor="squirrel", object=animal_label::eagle) -> activity_7 : TERM
CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
TERM activity(verb="visit", actor="squirrel", object=animal_label::lion) -> activity_8 : TERM
CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
TERM activity(verb="is", actor="someone", object=lexical_label_2) -> activity_9 : TERM
```
