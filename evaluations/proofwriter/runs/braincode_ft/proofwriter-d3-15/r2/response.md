```braincode
TERM  character_trait(property="furry", value="true") -> character_trait_2 : TERM
TERM  negation(target=character_trait_2) -> negation_2 : TERM
TERM  subject(kind="Bob", qualifier=negation_2) -> subject_2 : TERM
TERM  requirement(property="basis", value="theory") -> requirement_2 : TERM
TERM  constraint_single_choice() -> constraint_single_choice_2 : TERM
CLAIM statement(fact=subject_2) BY role_agent STATUS hypothesized SOURCE "t1:s18" -> candidate : CLAIM
```
