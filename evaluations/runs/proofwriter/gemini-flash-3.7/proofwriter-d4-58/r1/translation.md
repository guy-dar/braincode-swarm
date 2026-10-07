Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # Theory
    # t1:s2 The bear needs the tiger.
    TERM activity(actor="bear", object=animal_label::tiger, verb="needs") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM

    # t1:s3 The cat eats the squirrel.
    TERM activity(actor="cat", object=animal_label::squirrel, verb="eats") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM

    # t1:s4 The cat is not green.
    TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
    TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
    TERM subject(kind="cat", qualifier=requirement_2) -> subject_2 : TERM
    TERM negation(target=subject_2) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM

    # t1:s5 The cat is not round.
    TERM requirement(property="shape", value=shape_round) -> requirement_3 : TERM
    TERM subject(kind="cat", qualifier=requirement_3) -> subject_3 : TERM
    TERM negation(target=subject_3) -> negation_3 : TERM
    CLAIM statement(fact=negation_3) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM

    # t1:s6 The cat likes the squirrel.
    TERM activity(actor="cat", object=animal_label::squirrel, verb="likes") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM

    # t1:s7 The cat needs the bear.
    TERM activity(actor="cat", object=animal_label::bear, verb="needs") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM

    # t1:s8 The squirrel eats the bear.
    TERM activity(actor="squirrel", object=animal_label::bear, verb="eats") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM

    # t1:s9 The squirrel does not eat the cat.
    TERM activity(actor="squirrel", object=animal_label::cat, verb="eats") -> activity_7 : TERM
    TERM negation(target=activity_7) -> negation_4 : TERM
    CLAIM statement(fact=negation_4) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM

    # t1:s10 The squirrel does not eat the tiger.
    TERM activity(actor="squirrel", object=animal_label::tiger, verb="eats") -> activity_8 : TERM
    TERM negation(target=activity_8) -> negation_5 : TERM
    CLAIM statement(fact=negation_5) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM

    # t1:s11 The squirrel is cold.
    TERM requirement(property="temperature", value=state_cold) -> requirement_4 : TERM
    TERM subject(kind="squirrel", qualifier=requirement_4) -> subject_4 : TERM
    CLAIM statement(fact=subject_4) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM

    # t1:s12 The squirrel likes the bear.
    TERM activity(actor="squirrel", object=animal_label::bear, verb="likes") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM

    # t1:s13 The squirrel likes the cat.
    TERM activity(actor="squirrel", object=animal_label::cat, verb="likes") -> activity_10 : TERM
    CLAIM statement(fact=activity_10) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM

    # t1:s14 The squirrel needs the cat.
    TERM activity(actor="squirrel", object=animal_label::cat, verb="needs") -> activity_11 : TERM
    CLAIM statement(fact=activity_11) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM

    # t1:s15 The tiger is not green.
    TERM requirement(property="color", value=lexical_label_2) -> requirement_5 : TERM
    TERM subject(kind="tiger", qualifier=requirement_5) -> subject_5 : TERM
    TERM negation(target=subject_5) -> negation_6 : TERM
    CLAIM statement(fact=negation_6) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM

    # t1:s16 The tiger does not like the cat.
    TERM activity(actor="tiger", object=animal_label::cat, verb="likes") -> activity_12 : TERM
    TERM negation(target=activity_12) -> negation_7 : TERM
    CLAIM statement(fact=negation_7) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM

    # t1:s17 The tiger needs the cat.
    TERM activity(actor="tiger", object=animal_label::cat, verb="needs") -> activity_13 : TERM
    CLAIM statement(fact=activity_13) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM

    # t1:s18 If something is round then it likes the tiger.
    TERM requirement(property="shape", value=shape_round) -> requirement_6 : TERM
    TERM subject(kind="something", qualifier=requirement_6) -> subject_6 : TERM
    TERM activity(actor="something", object=animal_label::tiger, verb="likes") -> activity_14 : TERM
    TERM conditional(condition=subject_6, consequence=activity_14) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM

    # t1:s19 If something needs the squirrel then it does not like the cat.
    TERM activity(actor="something", object=animal_label::squirrel, verb="needs") -> activity_15 : TERM
    TERM activity(actor="something", object=animal_label::cat, verb="likes") -> activity_16 : TERM
    TERM negation(target=activity_16) -> negation_8 : TERM
    TERM conditional(condition=activity_15, consequence=negation_8) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_19 : CLAIM

    # t1:s20 If something is cold and it likes the tiger then the tiger is round.
    TERM requirement(property="temperature", value=state_cold) -> requirement_7 : TERM
    TERM subject(kind="something", qualifier=requirement_7) -> subject_7 : TERM
    TERM activity(actor="something", object=animal_label::tiger, verb="likes") -> activity_17 : TERM
    TERM conjunction(items=[subject_7, activity_17]) -> conjunction_2 : TERM
    TERM requirement(property="shape", value=shape_round) -> requirement_8 : TERM
    TERM subject(kind="tiger", qualifier=requirement_8) -> subject_8 : TERM
    TERM conditional(condition=conjunction_2, consequence=subject_8) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_20 : CLAIM

    # t1:s21 If something eats the bear then the bear likes the tiger.
    TERM activity(actor="something", object=animal_label::bear, verb="eats") -> activity_18 : TERM
    TERM activity(actor="bear", object=animal_label::tiger, verb="likes") -> activity_19 : TERM
    TERM conditional(condition=activity_18, consequence=activity_19) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_21 : CLAIM

    # t1:s22 If something eats the cat then the cat does not like the tiger.
    TERM activity(actor="something", object=animal_label::cat, verb="eats") -> activity_20 : TERM
    TERM activity(actor="cat", object=animal_label::tiger, verb="likes") -> activity_21 : TERM
    TERM negation(target=activity_21) -> negation_9 : TERM
    TERM conditional(condition=activity_20, consequence=negation_9) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_22 : CLAIM

    # t1:s23 If the squirrel likes the cat then the cat eats the squirrel.
    TERM conditional(condition=activity_10, consequence=activity_3) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_23 : CLAIM

    # t1:s24 If something needs the squirrel then the squirrel likes the cat.
    TERM conditional(condition=activity_15, consequence=activity_10) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s24" -> statement_24 : CLAIM

    # t1:s25 If something likes the tiger then it is cold.
    TERM conditional(condition=activity_17, consequence=subject_7) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s25" -> statement_25 : CLAIM

    # t1:s26 If something eats the cat then the cat eats the bear.
    TERM activity(actor="cat", object=animal_label::bear, verb="eats") -> activity_22 : TERM
    TERM conditional(condition=activity_20, consequence=activity_22) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s26" -> statement_26 : CLAIM

    # t1:s27 Question: Based only on the theory, is the following statement True, False, or Unknown?
    # t1:s28 The tiger does not like the tiger.
    TERM activity(actor="tiger", object=animal_label::tiger, verb="likes") -> activity_23 : TERM
    TERM negation(target=activity_23) -> negation_10 : TERM
    UTTER ask(target=negation_10)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | statement, role_user | covered |
| n2 | claim | statement, activity | label-preserved |
| n3 | object | animal_label::bear | label-preserved |
| n4 | object | animal_label::tiger | label-preserved |
| n5 | action | activity | covered |
| n6 | claim | statement, activity | label-preserved |
| n7 | object | animal_label::cat | label-preserved |
| n8 | object | animal_label::squirrel | label-preserved |
| n9 | action | activity | covered |
| n10 | claim | statement, negation, subject | label-preserved |
| n11 | object | animal_label::cat | label-preserved |
| n12 | constraint | color_label::green, requirement | covered |
| n13 | negation | negation, color_label::green | covered |
| n14 | claim | statement, negation, subject | covered |
| n15 | object | animal_label::cat | label-preserved |
| n16 | constraint | shape_round | covered |
| n17 | negation | shape_round, negation | covered |
| n18 | claim | statement, activity | label-preserved |
| n19 | object | animal_label::cat | label-preserved |
| n20 | object | animal_label::squirrel | label-preserved |
| n21 | action | activity | covered |
| n22 | claim | statement, activity | label-preserved |
| n23 | object | animal_label::cat | label-preserved |
| n24 | object | animal_label::bear | label-preserved |
| n25 | action | activity | covered |
| n26 | claim | statement, activity | covered |
| n27 | object | animal_label::squirrel | label-preserved |
| n28 | object | animal_label::bear | label-preserved |
| n29 | action | activity | covered |
| n30 | claim | statement, negation, activity | covered |
| n31 | object | animal_label::squirrel | label-preserved |
| n32 | object | animal_label::cat | label-preserved |
| n33 | action | activity | covered |
| n34 | negation | negation | covered |
| n35 | claim | statement, negation, activity | covered |
| n36 | object | animal_label::squirrel | label-preserved |
| n37 | object | animal_label::tiger | label-preserved |
| n38 | action | activity | covered |
| n39 | negation | negation | covered |
| n40 | claim | statement, subject, state_cold | covered |
| n41 | object | animal_label::squirrel | label-preserved |
| n42 | constraint | state_cold, requirement | covered |
| n43 | claim | statement, activity | label-preserved |
| n44 | object | animal_label::squirrel | label-preserved |
| n45 | object | animal_label::bear | label-preserved |
| n46 | action | activity | covered |
| n47 | claim | statement, activity | label-preserved |
| n48 | object | animal_label::squirrel | label-preserved |
| n49 | object | animal_label::cat | label-preserved |
| n50 | action | activity | covered |
| n51 | claim | statement, activity | label-preserved |
| n52 | object | animal_label::squirrel | label-preserved |
| n53 | object | animal_label::cat | label-preserved |
| n54 | action | activity | covered |
| n55 | claim | statement, negation, subject | label-preserved |
| n56 | object | animal_label::tiger | label-preserved |
| n57 | constraint | color_label::green, requirement | covered |
| n58 | negation | negation, color_label::green | covered |
| n59 | claim | statement, negation, activity | covered |
| n60 | object | animal_label::tiger | label-preserved |
| n61 | object | animal_label::cat | label-preserved |
| n62 | action | activity | covered |
| n63 | negation | negation | covered |
| n64 | claim | statement, activity | label-preserved |
| n65 | object | animal_label::tiger | label-preserved |
| n66 | object | animal_label::cat | label-preserved |
| n67 | action | activity | covered |
| n68 | reasoning | conditional, shape_round | covered |
| n69 | constraint | shape_round | covered |
| n70 | action | activity | covered |
| n71 | object | animal_label::tiger | label-preserved |
| n72 | reasoning | conditional, negation | covered |
| n73 | action | activity | covered |
| n74 | object | animal_label::squirrel | label-preserved |
| n75 | action | activity | covered |
| n76 | object | animal_label::cat | label-preserved |
| n77 | negation | negation | covered |
| n78 | reasoning | conditional, conjunction, state_cold, shape_round | covered |
| n79 | constraint | state_cold, requirement | covered |
| n80 | action | activity | covered |
| n81 | object | animal_label::tiger | label-preserved |
| n82 | constraint | shape_round | covered |
| n83 | reasoning | conditional | label-preserved |
| n84 | action | activity | covered |
| n85 | object | animal_label::bear | label-preserved |
| n86 | action | activity | covered |
| n87 | object | animal_label::tiger | label-preserved |
| n88 | reasoning | conditional, negation | covered |
| n89 | action | activity | covered |
| n90 | object | animal_label::cat | label-preserved |
| n91 | action | activity | covered |
| n92 | object | animal_label::tiger | label-preserved |
| n93 | negation | negation | covered |
| n94 | reasoning | conditional | label-preserved |
| n95 | object | animal_label::squirrel | label-preserved |
| n96 | action | activity | covered |
| n97 | object | animal_label::cat | label-preserved |
| n98 | action | activity | covered |
| n99 | reasoning | conditional | label-preserved |
| n100 | action | activity | covered |
| n101 | object | animal_label::squirrel | label-preserved |
| n102 | action | activity | covered |
| n103 | object | animal_label::cat | label-preserved |
| n104 | reasoning | conditional, state_cold | covered |
| n105 | action | activity | covered |
| n106 | object | animal_label::tiger | label-preserved |
| n107 | constraint | state_cold, requirement | covered |
| n108 | reasoning | conditional | label-preserved |
| n109 | action | activity | covered |
| n110 | object | animal_label::cat | label-preserved |
| n111 | object | animal_label::bear | label-preserved |
| n112 | speech_act | ask, statement, negation, conditional | covered |
| n113 | constraint | subject, requirement, conjunction | covered |
| n114 | constraint | subject, requirement | covered |
| n115 | claim | negation, activity | covered |
| n116 | object | animal_label::tiger | label-preserved |
| n117 | action | activity | covered |
| n118 | negation | negation | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t1:s28 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2-s28 "bear" → animal_label::bear, "tiger" → animal_label::tiger, "cat" → animal_label::cat, "squirrel" → animal_label::squirrel, "green" → color_label::green (open-group labels only)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
