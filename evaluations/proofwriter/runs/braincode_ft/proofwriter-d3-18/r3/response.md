```braincode
TERM  subject(kind="person", qualifier="nice") -> subject_nice : TERM
TERM  subject(kind="person", qualifier="quiet") -> subject_quiet : TERM
TERM  negation(target=subject_quiet) -> negation_quiet : TERM
TERM  conditional(condition=subject_nice, consequence=negation_quiet) -> conditional_nice_not_quiet : TERM
TERM  subject(kind="person", qualifier="round") -> subject_round : TERM
TERM  subject(kind="person", qualifier="quiet") -> subject_round_quiet : TERM
TERM  conditional(condition=subject_round, consequence=subject_round_quiet) -> conditional_round_quiet : TERM
TERM  subject(kind="person", qualifier="nice") -> subject_anne_nice : TERM
TERM  subject(kind="person", qualifier="white") -> subject_anne_white : TERM
TERM  negation(target=subject_anne_white) -> negation_anne_white : TERM
TERM  subject(kind="person", qualifier="young") -> subject_anne_young : TERM
TERM  subject(kind="person", qualifier="round") -> subject_erin_round : TERM
TERM  subject(kind="person", qualifier="blue") -> subject_fiona_blue : TERM
TERM  subject(kind="person", qualifier="young") -> subject_gary_young : TERM
TERM  subject(kind="person", qualifier="nice") -> subject_nice_person : TERM
TERM  subject(kind="person", qualifier="quiet") -> subject_quiet_person : TERM
TERM  negation(target=subject_quiet_person) -> negation_quiet_person : TERM
TERM  conditional(condition=subject_nice_person, consequence=negation_quiet_person) -> conditional_nice_not_quiet : TERM
TERM  subject(kind="person", qualifier="round") -> subject_round_person : TERM
TERM  subject(kind="person", qualifier="quiet") -> subject_round_quiet : TERM
TERM  conditional
```
