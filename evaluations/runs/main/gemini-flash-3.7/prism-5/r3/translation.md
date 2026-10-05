Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM self_protection(actor=role_user, domain="boundaries", strategy="coping") -> self_protection_2 : TERM
    UTTER ask(target=self_protection_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM self_protection(actor=role_user, domain="boundaries", strategy="limit_contact") -> self_protection_2 : TERM
    UTTER propose(target=self_protection_2)
    CLAIM recommended(target=self_protection_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> recommended_2 : CLAIM
    TERM negation(target=self_protection_2) -> negation_2 : TERM
    CLAIM attitude(target=negation_2, holder=role_user, type="intolerance") BY role_agent STATUS asserted SOURCE "t2:s3" -> attitude_2 : CLAIM
    CLAIM varies_with(target=self_protection_2, condition="continued_behavior") BY role_agent STATUS asserted SOURCE "t2:s3" -> varies_with_2 : CLAIM
    TERM self_protection(actor=role_user, domain="self_esteem") -> self_protection_3 : TERM
    UTTER propose(target=self_protection_3)
    CLAIM argues_for(subject=role_user, value=personal_values) BY role_agent STATUS asserted SOURCE "t2:s6" -> argues_for_2 : CLAIM
    TERM self_protection(actor=role_user, domain="boundaries_mother") -> self_protection_4 : TERM
    UTTER propose(target=self_protection_4)
    UTTER respond(target=self_protection_4)
    CLAIM attitude(target=self_protection_4, holder=role_mother, type="anger") BY role_agent STATUS asserted SOURCE "t2:s10" -> attitude_3 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    CLAIM recommended(target=offer_help_2) BY role_agent STATUS asserted SOURCE "t2:s12" -> recommended_3 : CLAIM
    CLAIM enables(condition=offer_help_2, outcome=self_protection_4) BY role_agent STATUS asserted SOURCE "t2:s13" -> enables_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="ultimatum") -> interpersonal_stance_2 : TERM
    UTTER ask(target=interpersonal_stance_2)
  }
  TURN t4 SPEAKER=AGENT {
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="ultimatum") -> interpersonal_stance_2 : TERM
    TERM negation(target=interpersonal_stance_2) -> negation_2 : TERM
    CLAIM recommended(target=negation_2) BY role_agent STATUS asserted SOURCE "t4:s2" -> recommended_2 : CLAIM
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="supportive") -> interpersonal_stance_3 : TERM
    UTTER propose(target=interpersonal_stance_3)
    TERM dialogue(style="open") -> dialogue_2 : TERM
    UTTER propose(target=dialogue_2)
    UTTER ask(target=dialogue_2)
    CLAIM varies_with(target=interpersonal_stance_3, condition="unwillingness") BY role_agent STATUS asserted SOURCE "t4:s10" -> varies_with_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, self_protection | covered |
| n2 | object | self_protection | covered |
| n3 | object | role_mother, self_protection | covered |
| n4 | action | self_protection, propose | covered |
| n5 | speech_act | attitude, propose | covered |
| n6 | action | varies_with, self_protection | covered |
| n7 | negation | negation, attitude | covered |
| n8 | action | self_protection, personal_values | covered |
| n9 | action | argues_for, personal_values | covered |
| n10 | action | self_protection, propose | covered |
| n11 | negation | self_protection | covered |
| n12 | negation | negation, self_protection | covered |
| n13 | action | respond, self_protection | covered |
| n14 | claim | attitude, role_mother | covered |
| n15 | action | offer_help, recommended | covered |
| n16 | object | offer_help | covered |
| n17 | claim | enables, offer_help | covered |
| n18 | speech_act | ask, interpersonal_stance | covered |
| n19 | object | role_friend | covered |
| n20 | object | interpersonal_stance | covered |
| n21 | claim | recommended, negation | covered |
| n22 | action | interpersonal_stance, propose | covered |
| n23 | action | interpersonal_stance | covered |
| n24 | action | dialogue, propose | covered |
| n25 | speech_act | ask, dialogue | covered |
| n26 | action | varies_with, interpersonal_stance | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s10 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
