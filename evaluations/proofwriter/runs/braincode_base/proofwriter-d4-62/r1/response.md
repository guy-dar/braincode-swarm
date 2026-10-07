```braincode
TERM  activity(verb="is_kind", actor="mouse") -> is_kind_mouse : TERM
TERM negation(target=is_kind_mouse) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
