Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM self_protection(actor=role_user, domain="toxic_family", strategy=role_mother) -> self_protection_2 : TERM
    UTTER ask(target=self_protection_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM self_protection(actor=role_user, domain="boundaries_mother_in_law", strategy=role_mother) -> self_protection_3 : TERM
    CLAIM recommended(target=self_protection_3) BY role_agent STATUS inferred SOURCE "t2:s2" -> recommended_2 : CLAIM
    TERM negation(target=self_protection_3) -> negation_2 : TERM
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="intolerance_negative_behavior") -> interpersonal_stance_2 : TERM
    UTTER propose(target=interpersonal_stance_2)
    TERM activity(actor="user", object=role_mother, verb="limit_contact") -> activity_2 : TERM
    CLAIM varies_with(target=activity_2, condition="negative_behavior_continues") BY role_agent STATUS inferred SOURCE "t2:s3" -> varies_with_2 : CLAIM
    TERM self_protection(actor=role_user, domain="self_esteem", strategy=personal_values) -> self_protection_4 : TERM
    UTTER propose(target=self_protection_4)
    TERM interpersonal_stance(target=role_mother, actor=role_user, stance="express_point_of_view") -> interpersonal_stance_3 : TERM
    UTTER propose(target=interpersonal_stance_3)
    TERM self_protection(actor=role_user, domain="healthy_boundaries", strategy=role_mother) -> self_protection_5 : TERM
    UTTER propose(target=self_protection_5)
    TERM exclude(item="defensiveness") -> exclude_2 : TERM
    UTTER propose(target=exclude_2)
    TERM exclude(item="personalizing_criticisms") -> exclude_3 : TERM
    UTTER propose(target=exclude_3)
    TERM dialogue(style=tone_polite) -> dialogue_2 : TERM
    UTTER respond(target=dialogue_2)
    CLAIM attitude(target=role_user, holder=role_mother, type="anger_not_about_user") BY role_agent STATUS inferred SOURCE "t2:s10" -> attitude_2 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    CLAIM recommended(target=offer_help_2) BY role_agent STATUS inferred SOURCE "t2:s12" -> recommended_3 : CLAIM
    CLAIM trained_for(activity=offer_help_2, subject=role_support_team) BY role_agent STATUS inferred SOURCE "t2:s13" -> trained_for_2 : CLAIM
    CLAIM enables(condition=trained_for_2, outcome=self_protection_2) BY role_agent STATUS inferred SOURCE "t2:s13" -> enables_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM interpersonal_stance(target=role_adults, actor=role_user, stance="force_choice") -> interpersonal_stance_4 : TERM
    UTTER ask(target=interpersonal_stance_4)
  }
  TURN t4 SPEAKER=AGENT {
    TERM interpersonal_stance(target=role_adults, actor=role_user, stance="ultimatum") -> interpersonal_stance_5 : TERM
    CLAIM recommended(target=interpersonal_stance_5) BY role_agent STATUS inferred SOURCE "t4:s2" -> recommended_4 : CLAIM
    TERM interpersonal_stance(target=role_adults, actor=role_user, stance="strong_positive_relationship") -> interpersonal_stance_6 : TERM
    CLAIM focus_of(concept="positive_relationship", subject=interpersonal_stance_6) BY role_agent STATUS inferred SOURCE "t4:s4" -> focus_of_2 : CLAIM
    TERM interpersonal_stance(target=role_adults, actor=role_user, stance="supportive_and_encouraging") -> interpersonal_stance_7 : TERM
    UTTER propose(target=interpersonal_stance_7)
    TERM dialogue(style="open_conversation") -> dialogue_3 : TERM
    CLAIM important(target=dialogue_3) BY role_agent STATUS inferred SOURCE "t4:s7" -> important_2 : CLAIM
    TERM property_question(property="input_on_handling_family", subject=role_adults) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    TERM interpersonal_stance(target=role_adults, actor=role_user, stance="reevaluate_relationship") -> interpersonal_stance_8 : TERM
    CLAIM varies_with(target=interpersonal_stance_8, condition="unwilling_or_unable_to_make_changes") BY role_agent STATUS inferred SOURCE "t4:s10" -> varies_with_3 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, self_protection | covered |
| n2 | object | role_mother | covered |
| n3 | object | role_mother | covered |
| n4 | action | self_protection, role_mother | covered |
| n5 | speech_act | propose, interpersonal_stance, role_mother | covered |
| n6 | action | activity, varies_with, role_mother | covered |
| n7 | negation | negation | covered |
| n8 | action | self_protection, personal_values, propose | covered |
| n9 | action | interpersonal_stance, propose, role_mother | covered |
| n10 | action | self_protection, role_mother, propose | covered |
| n11 | negation | exclude, propose | covered |
| n12 | negation | exclude, propose | covered |
| n13 | action | dialogue, tone_polite, respond | covered |
| n14 | claim | attitude, role_mother, role_user | covered |
| n15 | action | offer_help, recommended | covered |
| n16 | object | role_support_team | covered |
| n17 | claim | enables, trained_for, role_support_team | covered |
| n18 | speech_act | ask, interpersonal_stance | covered |
| n19 | object | role_adults | covered |
| n20 | object | role_adults | covered |
| n21 | claim | recommended, interpersonal_stance | covered |
| n22 | action | focus_of, interpersonal_stance | covered |
| n23 | action | interpersonal_stance, propose | covered |
| n24 | action | dialogue, important | covered |
| n25 | speech_act | ask, property_question, role_adults | covered |
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
