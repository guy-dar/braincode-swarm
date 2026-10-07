```braincode
TERM  character_trait(property="temperament", value="rough") -> rough_character : TERM
TERM  subject(kind="Charlie", qualifier=rough_character) -> charlie_subject : TERM
TERM  negation(target=charlie_subject) -> neg_charlie : TERM
CLAIM statement(fact=neg_charlie) BY role_user STATUS hypothesized SOURCE "t1:s19" -> neg_charlie_claim : CLAIM
TERM  test_condition(condition="truth_value", expected=TRUE) -> test_condition_2 : TERM
TERM  conjunction(items=[neg_charlie_claim, test_condition_2]) -> conjunction_2 : TERM
UTTER ask(target=conjunction_2)
```
