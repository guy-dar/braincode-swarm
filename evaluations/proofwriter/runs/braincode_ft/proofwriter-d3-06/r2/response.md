```braincode
TERM  lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
TERM  subject(kind="person", qualifier="Anne") -> subject_2 : TERM
TERM  attribute_claim(property="color", subject=subject_2, value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
TERM  subject(kind="person", qualifier="Anne") -> subject_3 : TERM
TERM  attribute_claim(property="smart", subject=subject_3, value=TRUE) BY role_user STATUS asserted SOURCE "t1:s3" -> attribute_claim_3 : CLAIM
TERM  subject(kind="person", qualifier="Dave") -> subject_4 : TERM
TERM  attribute_claim(property="size", subject=subject_4, value=size_large) BY role_user STATUS asserted SOURCE "t1:s4" -> attribute_claim_4 : CLAIM
TERM  subject(kind="person", qualifier="Dave") -> subject_5 : TERM
TERM  attribute_claim(property="color", subject=subject_5, value=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s5" -> attribute_claim_5 : CLAIM
TERM  subject(kind="person", qualifier="Dave") -> subject_6 : TERM
TERM  attribute_claim(property="state", subject=subject_6, value=state_cold) BY role_user STATUS asserted SOURCE "t1:s6" -> attribute_claim_6 : CLAIM
TERM  subject(kind="person", qualifier="Dave") -> subject_7 : TERM
TERM  attribute_claim(property="furry", subject=subject_7, value=TRUE) BY role_user STATUS asserted SOURCE "t1:s7" -> attribute_claim_7 : CLAIM
TERM  subject(kind="person", qualifier="Dave") -> subject_8 : TERM
TERM  attribute_claim(property="nice", subject=subject_8, value=TRUE) BY role_user
```
