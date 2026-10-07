```braincode
TERM  character(name="Bob") -> bob_char : TERM
TERM  character(name="Charlie") -> charlie_char : TERM
TERM  character(name="Dave") -> dave_char : TERM
TERM  character(name="Erin") -> erin_char : TERM
TERM  character_trait(property="color", value=color_label::red) -> color_red : TERM
TERM  character_trait(property="age", value="young") -> age_young : TERM
TERM  character_trait(property="thermal_state", value=state_cold) -> cold_state : TERM
TERM  character_trait(property="shape", value=shape_round) -> round_shape : TERM
TERM  character_trait(property="texture", value="rough") -> rough_texture : TERM
TERM  character_trait(property="temperament", value="kind") -> kind_temperament : TERM
TERM  conjunction(items=[color_red, age_young]) -> young_rough : TERM
TERM  conjunction(items=[cold_state, rough_texture]) -> cold_rough : TERM
TERM  conjunction(items=[color_red, kind_temperament]) -> red_kind : TERM
TERM  conjunction(items=[cold_state, rough_texture]) -> cold_rough_2 : TERM
TERM  conjunction(items=[color_red, cold_state]) -> red_cold : TERM
TERM  conjunction(items=[rough_texture, kind_temperament]) -> rough_kind : TERM
TERM  conjunction(items=[round_shape, kind_temperament]) -> round_kind : TERM
TERM  conjunction(items=[cold_state, age_young]) -> cold_young : TERM
TERM  conjunction(items=[rough_texture, kind_temperament]) -> rough_kind_2 : TERM
TERM  property_question(property="age", subject=charlie_char) -> charlie_age_q : TERM
TERM  attribute_claim(property="age", subject=charlie_char, value="young") -> charlie_age_claim : CLAIM
UTTER ask(target=charlie
```
