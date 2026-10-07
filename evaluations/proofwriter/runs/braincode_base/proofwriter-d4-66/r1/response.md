```braincode
TERM  quiet_and_cold := (requirement(property="quiet", value=TRUE) AND requirement(property="cold", value=TRUE)) -> quiet_and_cold : TERM
CLAIM statement(fact=quiet_and_cold) BY role_agent STATUS inferred SOURCE "theory" -> q : CLAIM

True (the statement holds):
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
