```braincode
TERM  character_trait(property="young", value="Fiona") -> young_Fiona : TERM
TERM negation(target=young_Fiona) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
