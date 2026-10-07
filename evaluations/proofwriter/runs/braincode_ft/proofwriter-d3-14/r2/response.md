```braincode
TERM  character_trait(property="temperament", value="rough") -> rough_charlie : TERM
TERM subject(kind="Charlie", qualifier=rough_charlie) -> charlie_rough : TERM
TERM negation(target=charlie_rough) -> neg_charlie_rough : TERM
CLAIM statement(fact=neg_charlie_rough) BY role_user STATUS hypothesized SOURCE "t1:s19" -> q : CLAIM
```
