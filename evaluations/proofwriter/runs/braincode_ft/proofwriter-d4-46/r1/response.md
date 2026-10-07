```braincode
TERM  character(name="Gary") -> character_2 : TERM
TERM character_trait(property="smart", value="Gary") -> character_trait_2 : TERM
TERM character_trait(property="cold", value="Gary") -> character_trait_3 : TERM
TERM conjunction(items=[character_trait_2, character_trait_3]) -> conjunction_2 : TERM
TERM conditional(condition=conjunction_2, consequence=character_trait_2) -> conditional_2 : TERM
CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_2 : CLAIM
TERM character_trait(property="cold", value="Gary") -> character_trait_4 : TERM
UTTER ask(target=character_trait_4)
```
