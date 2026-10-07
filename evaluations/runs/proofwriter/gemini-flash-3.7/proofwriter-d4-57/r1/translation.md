Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="bald_eagle", object=animal_label::tiger, verb="eat") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::tiger, verb="need") -> activity_3 : TERM
    TERM negation(target=activity_3) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM
    TERM activity(actor="bald_eagle", object=animal_label::cow, verb="see") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM
    TERM activity(actor="cow", object=animal_label::eagle, verb="eat") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM
    TERM requirement(property="nice", value=TRUE) -> requirement_2 : TERM
    TERM subject(kind="cow", qualifier=requirement_2) -> subject_2 : TERM
    TERM negation(target=subject_2) -> negation_3 : TERM
    CLAIM statement(fact=negation_3) BY user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM
    TERM activity(actor="mouse", object=animal_label::eagle, verb="need") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM
    TERM activity(actor="tiger", object=animal_label::cow, verb="eat") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM
    TERM requirement(property="rough", value=TRUE) -> requirement_3 : TERM
    TERM subject(kind="tiger", qualifier=requirement_3) -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM
    TERM requirement(property="young", value=TRUE) -> requirement_4 : TERM
    TERM subject(kind="tiger", qualifier=requirement_4) -> subject_4 : TERM
    TERM negation(target=subject_4) -> negation_4 : TERM
    CLAIM statement(fact=negation_4) BY user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM
    TERM activity(actor="tiger", object=animal_label::eagle, verb="see") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM
    TERM activity(actor="tiger", object=animal_label::cow, verb="need") -> activity_9 : TERM
    TERM conjunction(items=[activity_9, activity_7]) -> conjunction_2 : TERM
    TERM negation(target=activity_5) -> negation_5 : TERM
    TERM conditional(condition=conjunction_2, consequence=negation_5) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM
    TERM activity(object=animal_label::tiger, verb="see") -> activity_10 : TERM
    TERM activity(object=animal_label::mouse, verb="eat") -> activity_11 : TERM
    TERM conditional(condition=activity_10, consequence=activity_11) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM
    TERM requirement(property="rough", value=TRUE) -> requirement_5 : TERM
    TERM conditional(condition=requirement_2, consequence=requirement_5) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM
    TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
    TERM requirement(property="young", value=TRUE) -> requirement_6 : TERM
    TERM negation(target=requirement_6) -> negation_6 : TERM
    TERM conditional(condition=lexical_label_2, consequence=negation_6) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM
    TERM activity(object=animal_label::mouse, verb="need") -> activity_12 : TERM
    TERM activity(actor="mouse", object=animal_label::eagle, verb="need") -> activity_13 : TERM
    TERM negation(target=activity_13) -> negation_7 : TERM
    TERM conditional(condition=activity_12, consequence=negation_7) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM
    TERM activity(actor="mouse", object=animal_label::cow, verb="need") -> activity_14 : TERM
    TERM activity(actor="cow", object=animal_label::tiger, verb="need") -> activity_15 : TERM
    TERM conjunction(items=[activity_14, activity_15]) -> conjunction_3 : TERM
    TERM activity(actor="cow", object=animal_label::mouse, verb="see") -> activity_16 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_16) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM
    TERM activity(actor="mouse", object=animal_label::cow, verb="see") -> activity_17 : TERM
    TERM conditional(condition=activity_11, consequence=activity_17) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM
    TERM activity(object=animal_label::eagle, verb="eat") -> activity_18 : TERM
    TERM subject(kind="bald_eagle", qualifier=requirement_2) -> subject_5 : TERM
    TERM conditional(condition=activity_18, consequence=subject_5) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY user STATUS asserted SOURCE "t1:s19" -> statement_19 : CLAIM
    TERM activity(object=animal_label::cow, verb="see") -> activity_19 : TERM
    TERM activity(object=animal_label::tiger, verb="see") -> activity_20 : TERM
    TERM conditional(condition=activity_19, consequence=activity_20) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY user STATUS asserted SOURCE "t1:s20" -> statement_20 : CLAIM
    TERM requirement(property="evidence_basis", value="provided_theory") -> requirement_7 : TERM
    TERM requirement(property="allowed_choices", value="true_false_unknown") -> requirement_8 : TERM
    TERM activity(actor="mouse", object=animal_label::tiger, verb="see") -> activity_21 : TERM
    TERM negation(target=activity_21) -> negation_8 : TERM
    CLAIM statement(fact=negation_8) BY user STATUS asserted SOURCE "t1:s22" -> statement_21 : CLAIM
    UTTER ask(target=statement_21, constraints=[requirement_7, requirement_8])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, statement | covered |
| n2 | object | animal_label::eagle | label-preserved |
| n3 | object | animal_label::tiger | label-preserved |
| n4 | claim | activity, statement | covered |
| n5 | claim | activity, negation, statement | covered |
| n6 | negation | negation | covered |
| n7 | object | animal_label::cow | label-preserved |
| n8 | claim | activity, statement | covered |
| n9 | claim | activity, statement | covered |
| n10 | claim | requirement, subject, negation, statement | covered |
| n11 | negation | negation | covered |
| n12 | object | animal_label::mouse | label-preserved |
| n13 | claim | activity, statement | covered |
| n14 | claim | activity, statement | covered |
| n15 | claim | requirement, subject, statement | covered |
| n16 | claim | requirement, subject, negation, statement | covered |
| n17 | negation | negation | covered |
| n18 | claim | activity, statement | covered |
| n19 | reasoning | activity, conjunction, negation, conditional, statement | covered |
| n20 | negation | negation | covered |
| n21 | reasoning | activity, conditional, statement | covered |
| n22 | reasoning | requirement, conditional, statement | covered |
| n23 | constraint | color_label::red | label-preserved |
| n24 | reasoning | lexical_label, requirement, negation, conditional, statement | covered |
| n25 | negation | negation | covered |
| n26 | reasoning | activity, negation, conditional, statement | covered |
| n27 | negation | negation | covered |
| n28 | reasoning | activity, conjunction, activity, conditional, statement | covered |
| n29 | reasoning | activity, conditional, statement | covered |
| n30 | reasoning | activity, subject, requirement, conditional, statement | covered |
| n31 | reasoning | activity, conditional, statement | covered |
| n32 | speech_act | ask | covered |
| n33 | constraint | requirement | covered |
| n34 | constraint | requirement | covered |
| n35 | claim | activity, negation, statement | covered |
| n36 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s22 is fully represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" → animal_label::eagle; t1:s2 "tiger" → animal_label::tiger; t1:s4 "cow" → animal_label::cow; t1:s7 "mouse" → animal_label::mouse; t1:s15 "red" → color_label::red
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` validated syntax, types, and glossary symbol usage
