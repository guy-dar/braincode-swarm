```braincode
TERM  lexical_label(value=color_label::red) -> lexical_label_2 : TERM
TERM  subject(kind="Anne") -> subject_2 : TERM
TERM  attribute_claim(property="color", subject=subject_2, value=lexical_label_2) -> attribute_claim_2 : CLAIM
TERM  subject(kind="Anne") -> subject_3 : TERM
TERM  attribute_claim(property="rough", subject=subject_3, value=TRUE) -> attribute_claim_3 : CLAIM
TERM  subject(kind="Bob") -> subject_4 : TERM
TERM  attribute_claim(property="young", subject=subject_4, value=TRUE) -> attribute_claim_4 : CLAIM
TERM  subject(kind="Dave") -> subject_5 : TERM
TERM  has_state(state=state_cold, subject=subject_5) -> has_state_2 : CLAIM
TERM  subject(kind="Dave") -> subject_6 : TERM
TERM  attribute_claim(property="kind", subject=subject_6, value=TRUE) -> attribute_claim_5 : CLAIM
TERM  subject(kind="Fiona") -> subject_7 : TERM
TERM  attribute_claim(property="size", subject=subject_7, value=size_large) -> attribute_claim_6 : CLAIM
TERM  subject(kind="Fiona") -> subject_8 : TERM
TERM  attribute_claim(property="young", subject=subject_8, value=TRUE) -> attribute_claim_7 : CLAIM
TERM  character_trait(property="cold", value="true") -> character_trait_2 : TERM
TERM  character_trait(property="young", value="true") -> character_trait_3 : TERM
TERM  character_trait(property="furry", value="true") -> character_trait_4 : TERM
TERM  conjunction(items=[character_trait_2, character_trait_3]) -> conjunction_2 : TERM
TERM  conditional(condition=conjunction_2, consequence=character_trait_4) ->
```
