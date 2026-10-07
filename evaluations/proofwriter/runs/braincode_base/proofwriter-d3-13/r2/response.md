```braincode
TERM  character_trait(property="young", value="Fiona") -> young_Fiona : TERM
TERM negation(target=young_Fiona) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
