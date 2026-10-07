```braincode
TERM  subject(kind="Charlie", qualifier="young") -> charlie_young : TERM
TERM negation(target=charlie_young) -> neg_charlie : TERM
CLAIM statement(fact=neg_charlie) BY role_user STATUS asked SOURCE "t1:s18" -> ask_charlie : CLAIM
```
