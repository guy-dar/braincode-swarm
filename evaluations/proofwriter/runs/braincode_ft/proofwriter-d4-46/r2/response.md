```braincode
TERM  character(name="Gary") -> character_2 : TERM
TERM character_trait(property="smart", value="Gary") -> character_trait_2 : TERM
TERM character_trait(property="cold", value="Gary") -> character_trait_3 : TERM
TERM character_trait(property="nice", value="Gary") -> character_trait_4 : TERM
TERM conjunction(items=[character_trait_2, character_trait_3]) -> conjunction_5 : TERM
TERM conditional(condition=conjunction_5, consequence=character_trait_4) -> conditional_7 : TERM
TERM character_trait(property="cold", value="Gary") -> character_trait_5 : TERM
TERM conjunction(items=[character_trait_2, character_trait_5]) -> conjunction_6 : TERM
TERM conditional(condition=conjunction_6, consequence=character_trait_2) -> conditional_8 : TERM
TERM character_trait(property="cold", value="Gary") -> character_trait_6 : TERM
CLAIM statement(fact=character_trait_6) BY role_user STATUS hypothesized SOURCE "t1:s20" -> character_trait_6_hypothesis : CLAIM
```
