```braincode
TERM  subject(kind="Bob", qualifier=color_label::green) -> bob_green : TERM
TERM subject(kind="Bob", qualifier="kind") -> bob_kind : TERM
TERM subject(kind="Charlie", qualifier="nice") -> charlie_nice : TERM
TERM subject(kind="Erin", qualifier="kind") -> erin_kind : TERM
TERM subject(kind="Erin", qualifier=color_label::white) -> erin_white : TERM
TERM subject(kind="Gary", qualifier="young") -> gary_young : TERM
TERM subject(kind="thing", qualifier="young") -> young_thing : TERM
TERM subject(kind="thing", qualifier=color_label::white) -> white_thing : TERM
TERM conditional(condition=young_thing, consequence=white_thing) -> young_cond : TERM
TERM conditional(condition=white_thing, consequence=young_thing) -> white_cond : TERM
TERM subject(kind="thing", qualifier="nice") -> nice_thing : TERM
TERM subject(kind="thing", qualifier=color_label::green) -> green_thing : TERM
TERM conjunction(items=[nice_thing, green_thing]) -> nice_green : TERM
TERM subject(kind="thing", qualifier="kind") -> kind_thing : TERM
TERM conditional(condition=nice_green, consequence=kind_thing) -> nice_cond : TERM
TERM subject(kind="thing", qualifier="furry") -> furry_thing : TERM
TERM conditional(condition=young_thing, consequence=furry_thing) -> young_furry : TERM
TERM conditional(condition=kind_thing, consequence=nice_thing) -> kind_nice : TERM
TERM conjunction(items=[kind_thing, nice_thing]) -> kind_nice_conj : TERM
TERM conditional(condition=kind_nice_conj, consequence=young_thing) -> kind_nice_cond : TERM
TERM subject(kind="thing", qualifier="cold") -> cold_thing : TERM
TERM conjunction(items=[cold
```
