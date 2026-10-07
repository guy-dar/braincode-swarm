```braincode
TERM  character_trait(property="nice", value="true") -> nice : TERM
TERM character_trait(property="furry", value="true") -> furry : TERM
TERM character_trait(property="big", value="true") -> big : TERM
TERM conjunction(items=[nice, furry]) -> nice_furry : TERM
TERM conditional(condition=nice_furry, consequence=big) -> nice_furry_big : TERM
TERM character_trait(property="green", value="true") -> green : TERM
TERM character_trait(property="red", value="true") -> red : TERM
TERM conjunction(items=[green, nice]) -> green_nice : TERM
TERM conditional(condition=green_nice, consequence=red) -> green_nice_red : TERM
TERM character_trait(property="young", value="true") -> young : TERM
TERM conditional(condition=nice, consequence=furry) -> nice_furry_2 : TERM
TERM conjunction(items=[nice, young]) -> nice_young : TERM
TERM conditional(condition=nice_young, consequence=green) -> nice_young_green : TERM
TERM conjunction(items=[furry, nice]) -> furry_nice : TERM
TERM conditional(condition=furry_nice, consequence=big) -> furry_nice_big : TERM
TERM character_trait(property="kind", value="true") -> kind : TERM
TERM negation(target=kind) -> not_kind : TERM
TERM conjunction(items=[red, nice]) -> red_nice : TERM
TERM conditional(condition=red_nice, consequence=not_kind) -> red_nice_not_kind : TERM
TERM character_trait(property="young", value="true") -> young_2 : TERM
TERM conditional(condition=nice, consequence=young_2) -> nice_young_2 : TERM
TERM conjunction(items=[nice, young_2]) -> nice_young_3 : TERM
TERM conditional(condition=nice_young_3, consequence=green) -> nice_young_3
```
