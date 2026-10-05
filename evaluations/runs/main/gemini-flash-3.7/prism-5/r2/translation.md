Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM self_protection(actor=role_user, domain="boundaries", strategy=role_mother) -> self_protection_2 : TERM
    UTTER ask(target=self_protection_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM self_protection(actor=role_user, domain="boundaries", strategy=role_mother) -> self_protection_3 : TERM
    CLAIM recommended(target=self_protection_3) BY role_agent STATUS asserted SOURCE "t2:s2" -> recommended_2 : CLAIM
    UTTER propose(target=self_protection_3)
    CLAIM opposes(actor=role_user, subject=role_mother) BY role_user STATUS asserted SOURCE "t2:s3" -> opposes_2 : CLAIM
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="limit_contact") -> interpersonal_stance_2 : TERM
    CLAIM varies_with(target=interpersonal_stance_2, condition=role_mother) BY role_agent STATUS asserted SOURCE "t2:s3" -> varies_with_2 : CLAIM
    UTTER inform(target=opposes_2)
    TERM self_protection(actor=role_user, domain="self_esteem", strategy=personal_values) -> self_protection_4 : TERM
    UTTER propose(target=self_protection_4)
    CLAIM argues_for(subject=role_user, value=personal_values) BY role_user STATUS asserted SOURCE "t2:s6" -> argues_for_2 : CLAIM
    UTTER propose(target=argues_for_2)
    TERM self_protection(actor=role_user, domain="healthy_boundaries", strategy=role_mother) -> self_protection_5 : TERM
    UTTER propose(target=self_protection_5)
    TERM exclude(item="defensiveness") -> exclude_2 : TERM
    TERM negation(target=exclude_2) -> negation_2 : TERM
    UTTER propose(target=negation_2)
    UTTER respond(target=role_mother)
    CLAIM attitude(target=role_user, holder=role_mother, type="anger") BY role_agent STATUS asserted SOURCE "t2:s10" -> attitude_2 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    CLAIM recommended(target=offer_help_2) BY role_agent STATUS asserted SOURCE "t2:s12" -> recommended_3 : CLAIM
    CLAIM trained_for(activity=offer_help_2, subject=role_support_team) BY role_agent STATUS asserted SOURCE "t2:s13" -> trained_for_2 : CLAIM
    CLAIM enables(condition=trained_for_2, outcome=self_protection_5) BY role_agent STATUS asserted SOURCE "t2:s13" -> enables_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="ultimatum") -> interpersonal_stance_3 : TERM
    UTTER ask(target=interpersonal_stance_3)
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM recommended(target=t3.interpersonal_stance_3) BY role_agent STATUS assumed SOURCE "t4:s2" -> recommended_4 : CLAIM
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="positive") -> interpersonal_stance_4 : TERM
    CLAIM focus_of(concept="positive_relationship", subject=interpersonal_stance_4) BY role_agent STATUS asserted SOURCE "t4:s4" -> focus_of_2 : CLAIM
    CLAIM important(target=interpersonal_stance_4) BY role_agent STATUS asserted SOURCE "t4:s4" -> important_2 : CLAIM
    CLAIM attitude(target=interpersonal_stance_4, holder=role_user, type="supportive") BY role_agent STATUS asserted SOURCE "t4:s5" -> attitude_3 : CLAIM
    TERM dialogue(style="open") -> dialogue_2 : TERM
    UTTER propose(target=dialogue_2)
    TERM property_question(property="input", subject=role_friend) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    CLAIM varies_with(target=interpersonal_stance_4, condition=role_friend) BY role_agent STATUS asserted SOURCE "t4:s10" -> varies_with_3 : CLAIM
    CLAIM leads_to(cause=interpersonal_stance_4, effect=dialogue_2) BY role_agent STATUS asserted SOURCE "t4:s10" -> leads_to_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, self_protection, role_mother | covered |
| n2 | object | role_mother | covered |
| n3 | object | role_mother, personal_values | covered |
| n4 | action | self_protection, recommended, propose, role_mother | covered |
| n5 | speech_act | inform, opposes, role_mother | covered |
| n6 | action | interpersonal_stance, varies_with, role_mother | covered |
| n7 | negation | opposes, negation, exclude | covered |
| n8 | action | self_protection, personal_values, propose | covered |
| n9 | action | argues_for, personal_values, propose | covered |
| n10 | action | self_protection, role_mother, propose | covered |
| n11 | negation | exclude, negation, propose | covered |
| n12 | negation | exclude, negation, propose | covered |
| n13 | action | respond, role_mother | covered |
| n14 | claim | attitude, role_mother | covered |
| n15 | action | offer_help, recommended | covered |
| n16 | object | role_support_team, trained_for | covered |
| n17 | claim | trained_for, enables, self_protection, role_support_team | covered |
| n18 | speech_act | ask, interpersonal_stance, role_friend | covered |
| n19 | object | role_friend | covered |
| n20 | object | role_mother | covered |
| n21 | claim | recommended, interpersonal_stance | covered |
| n22 | action | interpersonal_stance, focus_of, important, role_friend | covered |
| n23 | action | attitude, interpersonal_stance | covered |
| n24 | action | dialogue, propose | covered |
| n25 | speech_act | ask, property_question, role_friend | covered |
| n26 | action | varies_with, leads_to, interpersonal_stance | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s10 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
