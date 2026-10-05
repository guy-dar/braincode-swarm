Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="dealing_with_toxic_family") -> interpersonal_stance_2 : TERM
    UTTER ask(target=interpersonal_stance_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM self_protection(actor=role_user, domain="boundaries", strategy="setting_boundaries") -> self_protection_2 : TERM
    UTTER propose(target=self_protection_2)
    TERM negation(target=self_protection_2) -> negation_2 : TERM
    CLAIM attitude(target=negation_2, holder=role_user, type="intolerance") BY role_agent STATUS asserted SOURCE "t2:s3" -> attitude_2 : CLAIM
    CLAIM varies_with(target=attitude_2, condition="continues_to_cause_problems") BY role_agent STATUS asserted SOURCE "t2:s3" -> varies_with_2 : CLAIM
    TERM self_protection(actor=role_user, domain="self_esteem", strategy=personal_values) -> self_protection_3 : TERM
    UTTER propose(target=self_protection_3)
    CLAIM argues_for(subject=role_user, value=personal_values) BY role_agent STATUS asserted SOURCE "t2:s6" -> argues_for_2 : CLAIM
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="express_point_of_view_strongly") -> interpersonal_stance_3 : TERM
    UTTER propose(target=interpersonal_stance_3)
    TERM self_protection(actor=role_user, domain="healthy_boundaries", strategy=role_mother) -> self_protection_4 : TERM
    UTTER propose(target=self_protection_4)
    TERM exclude(item="defensiveness") -> exclude_2 : TERM
    UTTER propose(target=exclude_2)
    TERM exclude(item="taking_criticisms_personally") -> exclude_3 : TERM
    UTTER propose(target=exclude_3)
    UTTER respond(target=role_mother)
    CLAIM attitude(target=role_user, holder=role_mother, type="anger") BY role_agent STATUS asserted SOURCE "t2:s10" -> attitude_3 : CLAIM
    CLAIM recommended(target=role_support_team) BY role_agent STATUS asserted SOURCE "t2:s12" -> recommended_2 : CLAIM
    CLAIM trained_for(activity=self_protection_2, subject=role_support_team) BY role_agent STATUS asserted SOURCE "t2:s13" -> trained_for_2 : CLAIM
    CLAIM enables(condition=trained_for_2, outcome=self_protection_4) BY role_agent STATUS asserted SOURCE "t2:s13" -> enables_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="force_choice_between_user_and_family") -> interpersonal_stance_4 : TERM
    UTTER ask(target=interpersonal_stance_4)
  }
  TURN t4 SPEAKER=AGENT {
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="force_hand") -> interpersonal_stance_5 : TERM
    CLAIM recommended(target=interpersonal_stance_5) BY role_agent STATUS asserted SOURCE "t4:s2" -> recommended_3 : CLAIM
    CLAIM opposes(actor=role_agent, subject=interpersonal_stance_5) BY role_agent STATUS asserted SOURCE "t4:s2" -> opposes_2 : CLAIM
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="strong_positive_relationship") -> interpersonal_stance_6 : TERM
    CLAIM focus_of(concept="positive_relationship", subject=interpersonal_stance_6) BY role_agent STATUS asserted SOURCE "t4:s4" -> focus_of_2 : CLAIM
    CLAIM attitude(target=role_friend, holder=role_user, type="supportive_and_encouraging") BY role_agent STATUS asserted SOURCE "t4:s5" -> attitude_4 : CLAIM
    TERM dialogue(style="open") -> dialogue_2 : TERM
    UTTER propose(target=dialogue_2)
    UTTER ask(target=interpersonal_stance_6)
    UTTER inform(target=attitude_4)
    CLAIM varies_with(target=interpersonal_stance_6, condition="partner_unwilling_to_make_changes") BY role_agent STATUS asserted SOURCE "t4:s10" -> varies_with_3 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | object | role_mother | covered |
| n3 | object | role_mother | covered |
| n4 | action | self_protection | covered |
| n5 | speech_act | attitude | covered |
| n6 | action | varies_with | covered |
| n7 | negation | negation | covered |
| n8 | action | personal_values, self_protection | covered |
| n9 | action | argues_for, interpersonal_stance | covered |
| n10 | action | self_protection | covered |
| n11 | negation | exclude | covered |
| n12 | negation | exclude | covered |
| n13 | action | respond | covered |
| n14 | claim | attitude | covered |
| n15 | action | recommended | covered |
| n16 | object | role_support_team | covered |
| n17 | claim | enables | covered |
| n18 | speech_act | ask | covered |
| n19 | object | role_friend | covered |
| n20 | object | role_mother | covered |
| n21 | claim | recommended | covered |
| n22 | action | focus_of, interpersonal_stance | covered |
| n23 | action | attitude | covered |
| n24 | action | dialogue | covered |
| n25 | speech_act | ask | covered |
| n26 | action | varies_with | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s10 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
