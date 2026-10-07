```braincode
TERM  character_trait(property="kind", value="true") -> character_trait_2 : TERM
TERM  character_trait(property="size", value="big") -> character_trait_3 : TERM
TERM  conjunction(items=[character_trait_2, character_trait_3]) -> conjunction_2 : TERM
TERM  character_trait(property="furry", value="true") -> character_trait_4 : TERM
TERM  conditional(condition=conjunction_2, consequence=character_trait_4) -> conditional_2 : TERM
TERM  character_trait(property="young", value="true") -> character_trait_5 : TERM
TERM  character_trait(property="rough", value="true") -> character_trait_6 : TERM
TERM  conjunction(items=[character_trait_5, character_trait_6]) -> conjunction_3 : TERM
TERM  character_trait(property="color", value=color_label::red) -> character_trait_7 : TERM
TERM  conditional(condition=conjunction_3, consequence=character_trait_7) -> conditional_3 : TERM
TERM  character_trait(property="cold", value="true") -> character_trait_8 : TERM
TERM  character_trait(property="young", value="true") -> character_trait_9 : TERM
TERM  conjunction(items=[character_trait_8, character_trait_9]) -> conjunction_4 : TERM
TERM  character_trait(property="kind", value="true") -> character_trait_10 : TERM
TERM  conjunction(items=[conjunction_4, character_trait_10]) -> conjunction_5 : TERM
TERM  character_trait(property="furry", value="true") -> character_trait_11 : TERM
TERM  conditional(condition=conjunction_5, consequence=character_trait_11) -> conditional_4 : TERM
TERM  character_trait(property="big", value="true") -> character_trait_12 : TERM
TERM  conjunction(items=[character_trait_9, character_trait_
```
