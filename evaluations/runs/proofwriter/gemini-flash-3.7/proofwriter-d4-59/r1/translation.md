Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=animal_label::baldeagle) -> lexical_label_2 : TERM
    TERM lexical_label(value=animal_label::dog) -> lexical_label_3 : TERM
    TERM lexical_label(value=animal_label::tiger) -> lexical_label_4 : TERM
    TERM lexical_label(value=animal_label::lion) -> lexical_label_5 : TERM
    TERM lexical_label(value=color_label::red) -> lexical_label_6 : TERM
    TERM lexical_label(value=color_label::blue) -> lexical_label_7 : TERM

    TERM subject(kind="bald_eagle", qualifier="kind") -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY role_user STATUS asserted SOURCE "t1:s2" -> statement_2 : CLAIM

    TERM subject(kind="bald_eagle", qualifier="red") -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_3 : CLAIM

    TERM activity(actor="bald_eagle", object=animal_label::dog, verb="need") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_4 : CLAIM

    TERM activity(actor="bald_eagle", object=animal_label::tiger, verb="visit") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_5 : CLAIM

    TERM subject(kind="dog", qualifier=size_large) -> subject_4 : TERM
    CLAIM statement(fact=subject_4) BY role_user STATUS asserted SOURCE "t1:s6" -> statement_6 : CLAIM

    TERM activity(actor="dog", object=animal_label::lion, verb="like") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_user STATUS asserted SOURCE "t1:s7" -> statement_7 : CLAIM

    TERM activity(actor="dog", object=animal_label::tiger, verb="like") -> activity_5 : TERM
    CLAIM statement(fact=activity_5) BY role_user STATUS asserted SOURCE "t1:s8" -> statement_8 : CLAIM

    TERM activity(actor="dog", object=animal_label::lion, verb="need") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_user STATUS asserted SOURCE "t1:s9" -> statement_9 : CLAIM

    TERM activity(actor="dog", object=animal_label::tiger, verb="need") -> activity_7 : TERM
    CLAIM statement(fact=activity_7) BY role_user STATUS asserted SOURCE "t1:s10" -> statement_10 : CLAIM

    TERM activity(actor="dog", object=animal_label::baldeagle, verb="visit") -> activity_8 : TERM
    CLAIM statement(fact=activity_8) BY role_user STATUS asserted SOURCE "t1:s11" -> statement_11 : CLAIM

    TERM subject(kind="lion", qualifier="red") -> subject_5 : TERM
    CLAIM statement(fact=subject_5) BY role_user STATUS asserted SOURCE "t1:s12" -> statement_12 : CLAIM

    TERM activity(actor="lion", object=animal_label::baldeagle, verb="like") -> activity_9 : TERM
    CLAIM statement(fact=activity_9) BY role_user STATUS asserted SOURCE "t1:s13" -> statement_13 : CLAIM

    TERM subject(kind="tiger", qualifier=size_large) -> subject_6 : TERM
    CLAIM statement(fact=subject_6) BY role_user STATUS asserted SOURCE "t1:s14" -> statement_14 : CLAIM

    TERM subject(kind="tiger", qualifier="kind") -> subject_7 : TERM
    CLAIM statement(fact=subject_7) BY role_user STATUS asserted SOURCE "t1:s15" -> statement_15 : CLAIM

    TERM activity(actor="something", object=animal_label::lion, verb="need") -> activity_10 : TERM
    TERM subject(kind="something", qualifier="blue") -> subject_8 : TERM
    TERM conditional(condition=activity_10, consequence=subject_8) -> conditional_2 : TERM
    CLAIM statement(fact=conditional_2) BY role_user STATUS asserted SOURCE "t1:s16" -> statement_16 : CLAIM

    TERM activity(actor="something", object=animal_label::tiger, verb="like") -> activity_11 : TERM
    TERM activity(actor="tiger", object=animal_label::lion, verb="need") -> activity_12 : TERM
    TERM conditional(condition=activity_11, consequence=activity_12) -> conditional_3 : TERM
    CLAIM statement(fact=conditional_3) BY role_user STATUS asserted SOURCE "t1:s17" -> statement_17 : CLAIM

    TERM activity(actor="something", object=animal_label::baldeagle, verb="like") -> activity_13 : TERM
    TERM activity(actor="bald_eagle", object=animal_label::lion, verb="need") -> activity_14 : TERM
    TERM conditional(condition=activity_13, consequence=activity_14) -> conditional_4 : TERM
    CLAIM statement(fact=conditional_4) BY role_user STATUS asserted SOURCE "t1:s18" -> statement_18 : CLAIM

    TERM subject(kind="something", qualifier="red") -> subject_9 : TERM
    TERM subject(kind="something", qualifier=size_large) -> subject_10 : TERM
    TERM conjunction(items=[subject_9, subject_10]) -> conjunction_2 : TERM
    TERM activity(actor="something", object=animal_label::lion, verb="visit") -> activity_15 : TERM
    TERM conditional(condition=conjunction_2, consequence=activity_15) -> conditional_5 : TERM
    CLAIM statement(fact=conditional_5) BY role_user STATUS asserted SOURCE "t1:s19" -> statement_19 : CLAIM

    TERM activity(actor="something", object=animal_label::dog, verb="visit") -> activity_16 : TERM
    TERM subject(kind="something", qualifier="kind") -> subject_11 : TERM
    TERM conjunction(items=[activity_16, subject_11]) -> conjunction_3 : TERM
    TERM activity(actor="something", object=animal_label::tiger, verb="like") -> activity_17 : TERM
    TERM conditional(condition=conjunction_3, consequence=activity_17) -> conditional_6 : TERM
    CLAIM statement(fact=conditional_6) BY role_user STATUS asserted SOURCE "t1:s20" -> statement_20 : CLAIM

    TERM activity(actor="something", object=animal_label::tiger, verb="like") -> activity_18 : TERM
    TERM subject(kind="something", qualifier=size_large) -> subject_12 : TERM
    TERM conditional(condition=activity_18, consequence=subject_12) -> conditional_7 : TERM
    CLAIM statement(fact=conditional_7) BY role_user STATUS asserted SOURCE "t1:s21" -> statement_21 : CLAIM

    TERM activity(actor="something", object=animal_label::lion, verb="need") -> activity_19 : TERM
    TERM activity(actor="something", object=animal_label::tiger, verb="visit") -> activity_20 : TERM
    TERM conjunction(items=[activity_19, activity_20]) -> conjunction_4 : TERM
    TERM subject(kind="tiger", qualifier="red") -> subject_13 : TERM
    TERM conditional(condition=conjunction_4, consequence=subject_13) -> conditional_8 : TERM
    CLAIM statement(fact=conditional_8) BY role_user STATUS asserted SOURCE "t1:s22" -> statement_22 : CLAIM

    TERM activity(actor="something", object=animal_label::lion, verb="visit") -> activity_21 : TERM
    TERM activity(actor="something", object=animal_label::dog, verb="visit") -> activity_22 : TERM
    TERM conditional(condition=activity_21, consequence=activity_22) -> conditional_9 : TERM
    CLAIM statement(fact=conditional_9) BY role_user STATUS asserted SOURCE "t1:s23" -> statement_23 : CLAIM

    TERM activity(actor="something", object=animal_label::baldeagle, verb="like") -> activity_23 : TERM
    TERM subject(kind="something", qualifier=state_cold) -> subject_14 : TERM
    TERM conditional(condition=activity_23, consequence=subject_14) -> conditional_10 : TERM
    CLAIM statement(fact=conditional_10) BY role_user STATUS asserted SOURCE "t1:s24" -> statement_24 : CLAIM

    TERM constraint_single_choice() -> constraint_single_choice_2 : TERM
    TERM activity(actor="lion", object=animal_label::dog, verb="visit") -> activity_24 : TERM
    CLAIM statement(fact=activity_24) BY role_user STATUS asserted SOURCE "t1:s26" -> statement_25 : CLAIM
    UTTER ask(target=statement_25, constraints=[constraint_single_choice_2])
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, subject, conjunction | covered |
| n2 | object | animal_label::baldeagle | label-preserved |
| n3 | claim | statement, subject | covered |
| n4 | object | animal_label::baldeagle | label-preserved |
| n5 | constraint | color_label::red | label-preserved |
| n6 | claim | statement, subject | covered |
| n7 | object | animal_label::baldeagle | label-preserved |
| n8 | object | animal_label::dog | label-preserved |
| n9 | claim | activity, statement | covered |
| n10 | object | animal_label::baldeagle | label-preserved |
| n11 | object | animal_label::tiger | label-preserved |
| n12 | claim | activity, statement | covered |
| n13 | object | animal_label::dog | label-preserved |
| n14 | claim | size_large, statement, subject | covered |
| n15 | object | animal_label::dog | label-preserved |
| n16 | object | animal_label::lion | label-preserved |
| n17 | claim | activity, statement | covered |
| n18 | object | animal_label::dog | label-preserved |
| n19 | object | animal_label::tiger | label-preserved |
| n20 | claim | activity, statement | covered |
| n21 | object | animal_label::dog | label-preserved |
| n22 | object | animal_label::lion | label-preserved |
| n23 | claim | activity, statement | covered |
| n24 | object | animal_label::dog | label-preserved |
| n25 | object | animal_label::tiger | label-preserved |
| n26 | claim | activity, statement | covered |
| n27 | object | animal_label::dog | label-preserved |
| n28 | object | animal_label::baldeagle | label-preserved |
| n29 | claim | activity, statement | covered |
| n30 | object | animal_label::lion | label-preserved |
| n31 | constraint | color_label::red | label-preserved |
| n32 | claim | statement, subject | covered |
| n33 | object | animal_label::lion | label-preserved |
| n34 | object | animal_label::baldeagle | label-preserved |
| n35 | claim | activity, statement | covered |
| n36 | object | animal_label::tiger | label-preserved |
| n37 | claim | size_large, statement, subject | covered |
| n38 | object | animal_label::tiger | label-preserved |
| n39 | claim | statement, subject | covered |
| n40 | object | animal_label::lion | label-preserved |
| n41 | constraint | color_label::blue | label-preserved |
| n42 | reasoning | conditional, statement, subject | covered |
| n43 | object | animal_label::tiger | label-preserved |
| n44 | object | animal_label::lion | label-preserved |
| n45 | reasoning | activity, conditional, statement | covered |
| n46 | object | animal_label::baldeagle | label-preserved |
| n47 | object | animal_label::lion | label-preserved |
| n48 | reasoning | activity, conditional, statement | covered |
| n49 | constraint | color_label::red | label-preserved |
| n50 | object | animal_label::lion | label-preserved |
| n51 | reasoning | conditional, conjunction, size_large, statement | covered |
| n52 | object | animal_label::dog | label-preserved |
| n53 | object | animal_label::tiger | label-preserved |
| n54 | reasoning | activity, conditional, conjunction, statement | covered |
| n55 | object | animal_label::tiger | label-preserved |
| n56 | reasoning | conditional, size_large, statement | covered |
| n57 | object | animal_label::lion | label-preserved |
| n58 | object | animal_label::tiger | label-preserved |
| n59 | constraint | color_label::red | label-preserved |
| n60 | reasoning | activity, conditional, conjunction, statement | covered |
| n61 | object | animal_label::lion | label-preserved |
| n62 | object | animal_label::dog | label-preserved |
| n63 | reasoning | activity, conditional, statement | covered |
| n64 | object | animal_label::baldeagle | label-preserved |
| n65 | reasoning | conditional, state_cold, statement | covered |
| n66 | speech_act | ask, statement | covered |
| n67 | constraint | statement | covered |
| n68 | constraint | constraint_single_choice | covered |
| n69 | object | animal_label::lion | label-preserved |
| n70 | object | animal_label::dog | label-preserved |
| n71 | claim | activity, statement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1-t1:s26 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "bald eagle" -> animal_label::baldeagle; t1:s3 "bald eagle" -> animal_label::baldeagle, "red" -> color_label::red; t1:s4 "bald eagle" -> animal_label::baldeagle, "dog" -> animal_label::dog; t1:s5 "bald eagle" -> animal_label::baldeagle, "tiger" -> animal_label::tiger; t1:s6 "dog" -> animal_label::dog; t1:s7 "dog" -> animal_label::dog, "lion" -> animal_label::lion; t1:s8 "dog" -> animal_label::dog, "tiger" -> animal_label::tiger; t1:s9 "dog" -> animal_label::dog, "lion" -> animal_label::lion; t1:s10 "dog" -> animal_label::dog, "tiger" -> animal_label::tiger; t1:s11 "dog" -> animal_label::dog, "bald eagle" -> animal_label::baldeagle; t1:s12 "lion" -> animal_label::lion, "red" -> color_label::red; t1:s13 "lion" -> animal_label::lion, "bald eagle" -> animal_label::baldeagle; t1:s14 "tiger" -> animal_label::tiger; t1:s15 "tiger" -> animal_label::tiger; t1:s16 "lion" -> animal_label::lion, "blue" -> color_label::blue; t1:s17 "tiger" -> animal_label::tiger, "lion" -> animal_label::lion; t1:s18 "bald eagle" -> animal_label::baldeagle, "lion" -> animal_label::lion; t1:s19 "red" -> color_label::red, "lion" -> animal_label::lion; t1:s20 "dog" -> animal_label::dog, "tiger" -> animal_label::tiger; t1:s21 "tiger" -> animal_label::tiger; t1:s22 "lion" -> animal_label::lion, "tiger" -> animal_label::tiger, "red" -> color_label::red; t1:s23 "lion" -> animal_label::lion, "dog" -> animal_label::dog; t1:s24 "bald eagle" -> animal_label::baldeagle; t1:s26 "lion" -> animal_label::lion, "dog" -> animal_label::dog
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
