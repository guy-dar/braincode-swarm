```braincode
TERM  character_trait(property="furry", value="furry") -> character_trait_2 : TERM
TERM character_trait(property="rough", value="rough") -> character_trait_3 : TERM
TERM character_trait(property="cold", value="cold") -> character_trait_4 : TERM
TERM character_trait(property="quiet", value="quiet") -> character_trait_5 : TERM
TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
TERM test_condition(condition=lexical_label_2, expected=TRUE) -> test_condition_2 : TERM
TERM test_condition(condition=lexical_label_3, expected=TRUE) -> test_condition_3 : TERM
TERM conjunction(items=[test_condition_2, test_condition_3]) -> conjunction_2 : TERM
TERM subject(kind="round") -> subject_2 : TERM
TERM subject(kind="quiet") -> subject_3 : TERM
TERM subject(kind="rough") -> subject_4 : TERM
TERM subject(kind="furry") -> subject_5 : TERM
TERM subject(kind="quiet", qualifier="Fiona") -> subject_6 : TERM
TERM subject(kind="rough", qualifier="Fiona") -> subject_7 : TERM
TERM subject(kind="furry", qualifier="Fiona") -> subject_8 : TERM
TERM subject(kind="green") -> subject_9 : TERM
TERM subject(kind="blue") -> subject_10 : TERM
TERM subject(kind="quiet", qualifier="Fiona") -> subject_11 : TERM
TERM conjunction(items=[subject_7, subject_11]) -> conjunction_3 : TERM
TERM subject(kind="rough", qualifier="Fiona") -> subject_12 : TERM
TERM subject(kind="green") -> subject_13 : TERM
TERM subject(kind="blue") -> subject_14 : TERM
TERM subject(kind
```
