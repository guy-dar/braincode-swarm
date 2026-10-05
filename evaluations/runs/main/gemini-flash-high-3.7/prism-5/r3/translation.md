Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="mother_in_law", qualifier="toxic") -> subject_2 : TERM
    TERM subject(kind="mother", qualifier="narcissistic") -> subject_3 : TERM
    TERM property_question(property="dealing_with", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM self_protection(actor=role_user, domain="boundaries", strategy=role_mother) -> self_protection_2 : TERM
    UTTER propose(target=self_protection_2)
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="intolerant") -> interpersonal_stance_2 : TERM
    TERM negation(target=interpersonal_stance_2) -> negation_2 : TERM
    TERM activity(actor=role_user, object=role_mother, purpose=negation_2, verb="communicate") -> activity_2 : TERM
    UTTER propose(target=activity_2)
    TERM activity(actor=role_user, object=role_mother, verb="limit_contact") -> activity_3 : TERM
    CLAIM varies_with(target=activity_3, condition="negative_behavior_continues") BY role_agent STATUS asserted SOURCE "t2:s3" -> varies_with_2 : CLAIM
    TERM self_protection(actor=role_user, domain="personal_values") -> self_protection_3 : TERM
    UTTER propose(target=self_protection_3)
    CLAIM argues_for(subject=role_user, value=personal_values) BY role_agent STATUS asserted SOURCE "t2:s6" -> argues_for_2 : CLAIM
    TERM self_protection(actor=role_user, domain="healthy_boundaries", strategy=role_mother) -> self_protection_4 : TERM
    UTTER propose(target=self_protection_4)
    TERM exclude(item="defensiveness") -> exclude_2 : TERM
    TERM negation(target=exclude_2) -> negation_3 : TERM
    UTTER propose(target=negation_3)
    TERM exclude(item="criticisms") -> exclude_3 : TERM
    UTTER propose(target=exclude_3)
    TERM activity(actor=role_user, object=role_mother, verb="respond") -> activity_4 : TERM
    UTTER respond(target=activity_4)
    CLAIM attitude(target=role_mother, holder=role_mother, type="anger") BY role_agent STATUS asserted SOURCE "t2:s10" -> attitude_2 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER propose(target=offer_help_2)
    CLAIM trained_for(activity=activity_4, subject=role_support_team) BY role_agent STATUS asserted SOURCE "t2:s13" -> trained_for_2 : CLAIM
    CLAIM enables(condition=trained_for_2, outcome=activity_4) BY role_agent STATUS asserted SOURCE "t2:s13" -> enables_2 : CLAIM
    CLAIM ongoing(target=subject_2) BY role_agent STATUS asserted SOURCE "t2:s13" -> ongoing_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="ultimatum") -> interpersonal_stance_3 : TERM
    TERM property_question(property="force_choice", subject=interpersonal_stance_3) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM activity(actor=role_user, object=role_friend, verb="force_hand") -> activity_5 : TERM
    TERM negation(target=activity_5) -> negation_4 : TERM
    CLAIM recommended(target=negation_4) BY role_agent STATUS asserted SOURCE "t4:s2" -> recommended_2 : CLAIM
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="positive_relationship") -> interpersonal_stance_4 : TERM
    CLAIM important(target=interpersonal_stance_4) BY role_agent STATUS asserted SOURCE "t4:s4" -> important_2 : CLAIM
    UTTER propose(target=interpersonal_stance_4)
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="supportive") -> interpersonal_stance_5 : TERM
    UTTER propose(target=interpersonal_stance_5)
    TERM dialogue(style="open") -> dialogue_2 : TERM
    TERM activity(actor=role_user, object=role_friend, purpose=dialogue_2, verb="converse") -> activity_6 : TERM
    UTTER propose(target=activity_6)
    TERM property_question(property="input", subject=role_friend) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
    TERM decision(activity=activity_6) -> decision_2 : TERM
    CLAIM varies_with(target=decision_2, condition="unwilling_to_change") BY role_agent STATUS asserted SOURCE "t4:s10" -> varies_with_3 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | object | subject | covered |
| n3 | object | subject | covered |
| n4 | action | self_protection, propose, role_mother | covered |
| n5 | speech_act | propose, activity, role_mother | covered |
| n6 | action | varies_with, activity, role_mother | covered |
| n7 | negation | negation, interpersonal_stance | covered |
| n8 | action | self_protection, role_user | covered |
| n9 | action | argues_for, personal_values | covered |
| n10 | action | self_protection, propose, role_mother | covered |
| n11 | negation | exclude, negation, propose | covered |
| n12 | negation | exclude, propose | covered |
| n13 | action | respond, activity, role_mother | covered |
| n14 | claim | attitude, role_mother | covered |
| n15 | action | offer_help, propose | covered |
| n16 | object | role_support_team | covered |
| n17 | claim | trained_for, enables, ongoing | covered |
| n18 | speech_act | ask, property_question | covered |
| n19 | object | role_friend | covered |
| n20 | object | interpersonal_stance | covered |
| n21 | claim | recommended, negation, activity | covered |
| n22 | action | interpersonal_stance, important, propose | covered |
| n23 | action | interpersonal_stance, propose | covered |
| n24 | action | dialogue, activity, propose | covered |
| n25 | speech_act | ask, property_question | covered |
| n26 | action | decision, varies_with | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s10 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
