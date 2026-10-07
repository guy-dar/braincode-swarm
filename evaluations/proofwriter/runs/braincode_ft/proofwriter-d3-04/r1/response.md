```braincode
TERM  character_trait(property="color", value=color_label::blue) -> character_trait_2 : TERM
TERM subject(kind="Bob", qualifier=character_trait_2) -> subject_2 : TERM
TERM test_condition(condition="can_be_white", expected=TRUE) -> test_condition_2 : TERM
UTTER ask(target=subject_2, constraints=[test_condition_2])
```
