Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="theory") -> subject_2 : TERM
    UTTER inform(target=subject_2)
    TERM activity(actor="cat", object=animal_label::mouse, verb="eat") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="cat", object=animal_label::squirrel, verb="eat") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    CLAIM has_attribute(attribute="rough", subject="cat") BY role_user STATUS asserted SOURCE "t1:s4" -> has_attribute_2 : CLAIM
    TERM activity(actor="cat", object=animal_label::lion, verb="see") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_4 : CLAIM
    TERM activity(actor="cat", object=animal_label::mouse, verb="see") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_5 : CLAIM
    TERM activity(actor="cat", object=animal_label::squirrel, verb="see") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_6 : CLAIM
    TERM activity(actor="lion", object=animal_label::cat, verb="see") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_7 : CLAIM
    TERM activity(actor="lion", object=animal_label::squirrel, verb="see") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_8 : CLAIM
    CLAIM attribute_claim(property="shape", subject="mouse", value=shape_round) BY role_user STATUS asserted SOURCE "t1:s10" -> attribute_claim_2 : CLAIM
    TERM activity(actor="mouse", object=animal_label::squirrel, verb="see") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_9 : CLAIM
    TERM activity(actor="squirrel", object=animal_label::lion, verb="like") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_10 : CLAIM
    TERM activity(actor="someone", verb="be_cold") -> activity_11 : TERM
    TERM activity(actor="someone", verb="be_kind") -> activity_12 : TERM
    TERM conditional(condition=activity_11, consequence=activity_12) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_11 : CLAIM
    TERM activity(actor="someone", object=animal_label::cat, verb="eat") -> activity_13 : TERM
    TERM conditional(condition=activity_13, consequence=activity_2) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_12 : CLAIM
    TERM activity(actor="someone", object=animal_label::mouse, verb="eat") -> activity_14 : TERM
    TERM conditional(condition=activity_14, consequence=activity_11) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_13 : CLAIM
    TERM activity(actor="someone", object=animal_label::squirrel, verb="eat") -> activity_15 : TERM
    TERM activity(actor="squirrel", verb="be_nice") -> activity_16 : TERM
    TERM conjunction(items=[activity_15, activity_16]) -> conjunction_2 : TERM
    TERM activity(actor="someone", object=animal_label::squirrel, verb="see") -> activity_17 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_17) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_14 : CLAIM
    TERM conditional(condition=activity_15, consequence=activity_11) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_15 : CLAIM
    TERM activity(actor="someone", object=animal_label::cat, verb="like") -> activity_18 : TERM
    TERM conditional(condition=activity_17, consequence=activity_18) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_16 : CLAIM
    TERM activity(actor="someone", object=animal_label::lion, verb="like") -> activity_19 : TERM
    TERM activity(actor="lion", object=animal_label::cat, verb="like") -> activity_20 : TERM
    TERM conjunction(items=[activity_19, activity_20]) -> conjunction_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_17) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_17 : CLAIM
    TERM activity(actor="someone", object=animal_label::mouse, verb="see") -> activity_21 : TERM
    TERM conjunction(items=[activity_21, activity_18]) -> conjunction_4 : TERM
    TERM activity(actor="someone", verb="be_nice") -> activity_22 : TERM
    TERM conditional(condition=conjunction_4, consequence=activity_22) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_18 : CLAIM
    TERM conjunction(items=[activity_17, activity_22]) -> conjunction_5 : TERM
    TERM activity(actor="squirrel", object=animal_label::mouse, verb="eat") -> activity_23 : TERM
    TERM conditional(condition=conjunction_5, consequence=activity_23) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_19 : CLAIM
    CLAIM statement(fact=activity_23) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_20 : CLAIM
    TERM requirement(property="grounded_in_theory", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="allowed_responses", value="True, False, or Unknown") -> requirement_3 : TERM
    UTTER ask(target=activity_23, constraints=[requirement_2, requirement_3])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | inform, subject | covered |
| n2 | object | animal_label::cat | label-preserved |
| n3 | object | animal_label::mouse | label-preserved |
| n4 | claim | activity, statement | covered |
| n5 | object | animal_label::squirrel | label-preserved |
| n6 | claim | activity, statement | covered |
| n7 | claim | has_attribute | covered |
| n8 | object | animal_label::lion | label-preserved |
| n9 | claim | activity, statement | covered |
| n10 | claim | activity, statement | covered |
| n11 | claim | activity, statement | covered |
| n12 | claim | activity, statement | covered |
| n13 | claim | activity, statement | covered |
| n14 | claim | attribute_claim, shape_round | covered |
| n15 | claim | activity, statement | covered |
| n16 | claim | activity, statement | covered |
| n17 | reasoning | activity, conditional, statement | covered |
| n18 | reasoning | activity, conditional, statement | covered |
| n19 | reasoning | activity, conditional, statement | covered |
| n20 | reasoning | activity, conditional, conjunction, statement | covered |
| n21 | reasoning | activity, conditional, statement | covered |
| n22 | reasoning | activity, conditional, statement | covered |
| n23 | reasoning | activity, conditional, conjunction, statement | covered |
| n24 | reasoning | activity, conditional, conjunction, statement | covered |
| n25 | reasoning | activity, conditional, conjunction, statement | covered |
| n26 | speech_act | ask | covered |
| n27 | constraint | requirement | covered |
| n28 | constraint | requirement | covered |
| n29 | claim | activity, statement | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s23 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "cat" → animal_label::cat; t1:s2 "mouse" → animal_label::mouse; t1:s3 "squirrel" → animal_label::squirrel; t1:s5 "lion" → animal_label::lion
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
