```braincode
TERM  lexical_label(value=color_label::white) -> lexical_label_white : TERM
TERM  lexical_label(value=color_label::blue) -> lexical_label_blue : TERM
TERM  subject(kind="Anne", qualifier="nice") -> subject_anne_nice : TERM
TERM  negation(target=subject_anne_nice) -> negation_anne_nice : TERM
TERM  subject(kind="Anne", qualifier=shape_round) -> subject_anne_round : TERM
TERM  subject(kind="Anne", qualifier=lexical_label_white) -> subject_anne_white : TERM
TERM  negation(target=subject_anne_white) -> negation_anne_white : TERM
TERM  subject(kind="Anne", qualifier="young") -> subject_anne_young : TERM
TERM  subject(kind="Erin", qualifier=shape_round) -> subject_erin_round : TERM
TERM  subject(kind="Fiona", qualifier=lexical_label_blue) -> subject_fiona_blue : TERM
TERM  subject(kind="Gary", qualifier="young") -> subject_gary_young : TERM
TERM  subject(kind="person", qualifier="nice") -> subject_nice_person : TERM
TERM  subject(kind="person", qualifier="quiet") -> subject_quiet_person : TERM
TERM  negation(target=subject_quiet_person) -> negation_quiet_person : TERM
TERM  conditional(condition=subject_nice_person, consequence=negation_quiet_person) -> conditional_nice_not_quiet : TERM
TERM  subject(kind="person", qualifier=shape_round) -> subject_round_person : TERM
TERM  conditional(condition=subject_round_person, consequence=subject_quiet_person) -> conditional_round_quiet : TERM
TERM  conditional(condition=subject_anne_nice, consequence=subject_anne_white) -> conditional_anne_nice_white : TERM
TERM  subject(kind="person", qualifier=lexical_label_blue) -> subject_blue_person : TERM
TERM  conditional(condition=
```
