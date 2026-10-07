```braincode
TERM  attribute_claim(property="color", subject="Bob", value=color_label::red) -> color_red : TERM
TERM  attribute_claim(property="young", subject="Bob", value=TRUE) -> young_true : TERM
TERM  conjunction(items=[color_red, young_true]) -> conjunction_red_young : TERM
TERM  negation(target=conjunction_red_young) -> q : TERM
TERM  negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
