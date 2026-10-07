Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM attribute_claim(property="size", subject="bear", value=size_large) BY user STATUS asserted SOURCE "t1:s2" -> attribute_claim_2 : CLAIM
    TERM activity(actor="bear", object=animal_label::cat, verb="see") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY user STATUS asserted SOURCE "t1:s3" -> statement_2 : CLAIM
    TERM activity(actor="cat", object=animal_label::cow, verb="chase") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY user STATUS asserted SOURCE "t1:s4" -> statement_3 : CLAIM
    TERM activity(actor="cat", object=animal_label::bear, verb="like") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY user STATUS asserted SOURCE "t1:s5" -> statement_4 : CLAIM
    TERM activity(actor="cow", object=animal_label::cat, verb="like") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY user STATUS asserted SOURCE "t1:s6" -> statement_5 : CLAIM
    TERM activity(actor="cow", object=animal_label::bear, verb="see") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY user STATUS asserted SOURCE "t1:s7" -> statement_6 : CLAIM
    TERM activity(actor="dog", object=animal_label::cow, verb="see") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY user STATUS asserted SOURCE "t1:s8" -> statement_7 : CLAIM
    TERM activity(actor="cat", object=animal_label::bear, verb="like") -> activity_8 : TERM
    TERM activity(actor="cat", object=animal_label::dog, verb="chase") -> activity_9 : TERM
    TERM conjunction(items=[activity_8, activity_9]) -> conjunction_2 : TERM
    TERM activity(actor="dog", object=animal_label::cat, verb="like") -> activity_10 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_10) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY user STATUS asserted SOURCE "t1:s9" -> statement_8 : CLAIM
    TERM activity(actor="someone", object=animal_label::cat, verb="like") -> activity_11 : TERM
    TERM activity(actor="cat", object=animal_label::bear, verb="see") -> activity_12 : TERM
    TERM conditional(condition=activity_11, consequence=activity_12) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY user STATUS asserted SOURCE "t1:s10" -> statement_9 : CLAIM
    TERM activity(actor="someone", object=animal_label::bear, verb="see") -> activity_13 : TERM
    TERM activity(actor="they", object=animal_label::dog, verb="chase") -> activity_14 : TERM
    TERM conditional(condition=activity_13, consequence=activity_14) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY user STATUS asserted SOURCE "t1:s11" -> statement_10 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    TERM subject(kind="cat", qualifier=lexical_label_2) -> subject_2 : TERM
    TERM activity(actor="cat", object=animal_label::bear, verb="like") -> activity_15 : TERM
    TERM conditional(condition=subject_2, consequence=activity_15) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY user STATUS asserted SOURCE "t1:s12" -> statement_11 : CLAIM
    TERM activity(actor="someone", object=animal_label::bear, verb="chase") -> activity_16 : TERM
    TERM activity(actor="bear", object=animal_label::dog, verb="see") -> activity_17 : TERM
    TERM conditional(condition=activity_16, consequence=activity_17) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY user STATUS asserted SOURCE "t1:s13" -> statement_12 : CLAIM
    TERM activity(actor="someone", object=animal_label::cat, verb="like") -> activity_18 : TERM
    TERM activity(actor="they", object=animal_label::cow, verb="chase") -> activity_19 : TERM
    TERM conditional(condition=activity_18, consequence=activity_19) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY user STATUS asserted SOURCE "t1:s14" -> statement_13 : CLAIM
    TERM activity(actor="someone", object=animal_label::cow, verb="chase") -> activity_20 : TERM
    TERM activity(actor="cow", object=animal_label::dog, verb="chase") -> activity_21 : TERM
    TERM conjunction(items=[activity_20, activity_21]) -> conjunction_3 : TERM
    TERM subject(kind="they", qualifier=lexical_label_2) -> subject_3 : TERM
    TERM conditional(condition=conjunction_3, consequence=subject_3) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY user STATUS asserted SOURCE "t1:s15" -> statement_14 : CLAIM
    TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
    TERM subject(kind="cow", qualifier=lexical_label_3) -> subject_4 : TERM
    TERM activity(actor="cow", object=animal_label::cat, verb="chase") -> activity_22 : TERM
    TERM conditional(condition=subject_4, consequence=activity_22) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY user STATUS asserted SOURCE "t1:s16" -> statement_15 : CLAIM
    TERM activity(actor="someone", object=animal_label::dog, verb="like") -> activity_23 : TERM
    TERM activity(actor="they", object=animal_label::bear, verb="see") -> activity_24 : TERM
    TERM conjunction(items=[activity_23, activity_24]) -> conjunction_4 : TERM
    TERM subject(kind="bear", qualifier="young") -> subject_5 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_5) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY user STATUS asserted SOURCE "t1:s17" -> statement_16 : CLAIM
    TERM activity(actor="dog", object=animal_label::cat, verb="like") -> activity_25 : TERM
    UTTER ask(target=activity_25)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, subject, conjunction, activity | covered |
| n2 | object | animal_label::bear | label-preserved |
| n3 | constraint | size_large | covered |
| n4 | claim | attribute_claim, statement | covered |
| n5 | object | animal_label::cat | label-preserved |
| n6 | action | activity | covered |
| n7 | claim | statement, activity | covered |
| n8 | object | animal_label::cow | label-preserved |
| n9 | action | activity | covered |
| n10 | claim | statement, activity | covered |
| n11 | action | activity | covered |
| n12 | claim | statement, activity | covered |
| n13 | claim | statement, activity | covered |
| n14 | claim | statement, activity | covered |
| n15 | object | animal_label::dog | label-preserved |
| n16 | claim | statement, activity | covered |
| n17 | claim | conditional, conjunction, statement | covered |
| n18 | claim | conditional, statement | covered |
| n19 | claim | conditional, statement | covered |
| n20 | constraint | color_label::red | label-preserved |
| n21 | claim | conditional, statement | covered |
| n22 | claim | conditional, statement | covered |
| n23 | claim | conditional, statement | covered |
| n24 | claim | conditional, conjunction, statement | covered |
| n25 | constraint | color_label::green | label-preserved |
| n26 | claim | conditional, statement | covered |
| n27 | constraint | subject | covered |
| n28 | claim | conditional, conjunction, statement | covered |
| n29 | speech_act | ask | covered |
| n30 | constraint | ask | covered |
| n31 | constraint | ask | covered |
| n32 | claim | activity, statement | covered |

## Translation report

- Input kind: prompt
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s19 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bear" -> animal_label::bear; t1:s3 "cat" -> animal_label::cat; t1:s4 "cow" -> animal_label::cow; t1:s8 "dog" -> animal_label::dog; t1:s12 "red" -> color_label::red; t1:s16 "green" -> color_label::green
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
