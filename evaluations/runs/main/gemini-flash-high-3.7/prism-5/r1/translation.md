Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="cope_with_mother_in_law") -> interpersonal_stance_2 : TERM
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="cope_with_narcissistic_mother") -> interpersonal_stance_3 : TERM
    TERM self_protection(actor=role_user, domain="toxic_family", strategy=interpersonal_stance_2) -> self_protection_2 : TERM
    UTTER ask(target=self_protection_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="set_boundaries") -> interpersonal_stance_4 : TERM
    TERM self_protection(actor=role_user, domain="boundaries_mother_in_law", strategy=interpersonal_stance_4) -> self_protection_3 : TERM
    CLAIM recommended(target=interpersonal_stance_4) BY role_agent STATUS inferred SOURCE "t2:s2" -> recommended_2 : CLAIM
    UTTER propose(target=interpersonal_stance_4)
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="negative_behavior") -> interpersonal_stance_5 : TERM
    TERM negation(target=interpersonal_stance_5) -> negation_2 : TERM
    CLAIM attitude(target=negation_2, holder=role_user, type="intolerance") BY role_agent STATUS reported SOURCE "t2:s3" -> attitude_2 : CLAIM
    UTTER inform(target=attitude_2)
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="limit_contact") -> interpersonal_stance_6 : TERM
    TERM obligation(activity=interpersonal_stance_6, actor=role_user) -> obligation_2 : TERM
    CLAIM varies_with(target=obligation_2, condition="continues_negative_behavior") BY role_agent STATUS inferred SOURCE "t2:s3" -> varies_with_2 : CLAIM
    UTTER propose(target=obligation_2)
    TERM self_protection(actor=role_user, domain="self_esteem", strategy=personal_values) -> self_protection_4 : TERM
    CLAIM recommended(target=self_protection_4) BY role_agent STATUS inferred SOURCE "t2:s5" -> recommended_3 : CLAIM
    UTTER propose(target=self_protection_4)
    CLAIM argues_for(subject=role_user, value=personal_values) BY role_agent STATUS inferred SOURCE "t2:s6" -> argues_for_2 : CLAIM
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="express_point_of_view_strongly") -> interpersonal_stance_7 : TERM
    UTTER propose(target=interpersonal_stance_7)
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="healthy_boundaries") -> interpersonal_stance_8 : TERM
    TERM self_protection(actor=role_user, domain="boundaries_mother", strategy=interpersonal_stance_8) -> self_protection_5 : TERM
    UTTER propose(target=self_protection_5)
    TERM self_protection(actor=role_user, domain="defensiveness") -> self_protection_6 : TERM
    TERM negation(target=self_protection_6) -> negation_3 : TERM
    UTTER propose(target=negation_3)
    TERM activity(actor="user", object=role_mother, verb="take_criticisms_personally") -> activity_2 : TERM
    TERM negation(target=activity_2) -> negation_4 : TERM
    UTTER propose(target=negation_4)
    TERM dialogue(style="calm") -> dialogue_2 : TERM
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="respond_calmly") -> interpersonal_stance_9 : TERM
    UTTER respond(target=interpersonal_stance_9)
    CLAIM attitude(target=role_user, holder=role_mother, type="anger") BY role_mother STATUS asserted SOURCE "t2:s10" -> attitude_3 : CLAIM
    TERM activity(actor="user", object=role_support_team, verb="seek_professional_help") -> activity_3 : TERM
    CLAIM recommended(target=activity_3) BY role_agent STATUS inferred SOURCE "t2:s12" -> recommended_4 : CLAIM
    UTTER propose(target=activity_3)
    CLAIM enables(condition=activity_3, outcome=t1.self_protection_2) BY role_agent STATUS inferred SOURCE "t2:s13" -> enables_2 : CLAIM
    UTTER inform(target=enables_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="force_choice_family") -> interpersonal_stance_10 : TERM
    UTTER ask(target=interpersonal_stance_10)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM recommended(target=t3.interpersonal_stance_10) BY role_agent STATUS inferred SOURCE "t4:s2" -> recommended_5 : CLAIM
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="positive_relationship") -> interpersonal_stance_11 : TERM
    CLAIM focus_of(concept="positive_relationship", subject=interpersonal_stance_11) BY role_agent STATUS inferred SOURCE "t4:s4" -> focus_of_2 : CLAIM
    CLAIM important(target=interpersonal_stance_11) BY role_agent STATUS inferred SOURCE "t4:s4" -> important_2 : CLAIM
    UTTER propose(target=interpersonal_stance_11)
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="supportive_and_encouraging") -> interpersonal_stance_12 : TERM
    UTTER propose(target=interpersonal_stance_12)
    TERM dialogue(style="open_conversation") -> dialogue_3 : TERM
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="discuss_family_impact") -> interpersonal_stance_13 : TERM
    UTTER propose(target=interpersonal_stance_13)
    TERM property_question(property="input_on_handling_family", subject=role_friend) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="reevaluate_relationship") -> interpersonal_stance_14 : TERM
    CLAIM varies_with(target=interpersonal_stance_14, condition="partner_unwilling_to_change") BY role_agent STATUS inferred SOURCE "t4:s10" -> varies_with_3 : CLAIM
    UTTER propose(target=interpersonal_stance_14)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, role_mother, personal_values, respond, propose, role_support_team | covered |
| n2 | object | role_mother | covered |
| n3 | object | role_mother, personal_values | covered |
| n4 | action | role_mother, self_protection, obligation | covered |
| n5 | speech_act | role_mother, inform, propose, attitude, interpersonal_stance, respond | covered |
| n6 | action | propose, obligation, attitude, varies_with | covered |
| n7 | negation | negation, interpersonal_stance, attitude | covered |
| n8 | action | personal_values, self_protection, attitude, role_user | covered |
| n9 | action | propose, self_protection, interpersonal_stance, attitude, personal_values, argues_for, focus_of | covered |
| n10 | action | role_mother, self_protection, obligation, enables, propose | covered |
| n11 | negation | self_protection, argues_for, inform, negation | covered |
| n12 | negation | negation, self_protection, attitude | covered |
| n13 | action | role_mother, respond, propose, ask, obligation | covered |
| n14 | claim | role_mother, attitude, varies_with, personal_values, enables, recommended | covered |
| n15 | action | propose, role_support_team, recommended, argues_for, ask, obligation | covered |
| n16 | object | role_support_team, role_mother, role_agent, role_user, role_friend | covered |
| n17 | claim | enables, role_mother, role_support_team, recommended | covered |
| n18 | speech_act | ask, varies_with, role_user, role_mother, inform, personal_values, role_friend, respond | covered |
| n19 | object | interpersonal_stance, role_friend | covered |
| n20 | object | role_mother, personal_values | covered |
| n21 | claim | recommended, enables, varies_with, propose, attitude, interpersonal_stance, ask | covered |
| n22 | action | interpersonal_stance, attitude, important, propose, focus_of, role_support_team, obligation, argues_for | covered |
| n23 | action | attitude, interpersonal_stance, recommended, argues_for, enables, propose, obligation | covered |
| n24 | action | interpersonal_stance, attitude, property_question, important, dialogue, propose, recommended | covered |
| n25 | speech_act | ask, propose, personal_values, interpersonal_stance, attitude, respond | covered |
| n26 | action | interpersonal_stance, attitude, varies_with, propose, enables, recommended | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s10 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
