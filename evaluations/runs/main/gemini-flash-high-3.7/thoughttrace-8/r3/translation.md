Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="user") -> subject_2 : TERM
    CLAIM comfortable(person=subject_2, value=FALSE) BY role_user STATUS asserted SOURCE "t1:s1" -> comfortable_2 : CLAIM
    TERM activity(actor=role_user, verb="seek_advice") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER apologize(target=t1.comfortable_2)
    TERM activity(actor=role_user, verb="identify_root_cause") -> activity_3 : TERM
    UTTER propose(target=activity_3)
    TERM subject(kind="workplace_culture", qualifier=personal_values) -> subject_3 : TERM
    CLAIM causes(cause=subject_3, effect=t1.comfortable_2) BY role_agent STATUS hypothesized SOURCE "t2:s10" -> causes_2 : CLAIM
    TERM activity(actor=role_user, verb="assess_fixable") -> activity_4 : TERM
    TERM decision(activity=activity_4) -> decision_2 : TERM
    UTTER propose(target=decision_2)
    TERM activity(actor=role_user, object=role_manager, verb="discuss_boundaries") -> activity_5 : TERM
    UTTER propose(target=activity_5)
    TERM subject(kind="toxic_leadership") -> subject_4 : TERM
    TERM activity(actor=role_user, verb="plan_exit") -> activity_6 : TERM
    CLAIM leads_to(cause=subject_4, effect=activity_6) BY role_agent STATUS inferred SOURCE "t2:s25" -> leads_to_2 : CLAIM
    TERM self_protection(actor=role_user, domain="mental_health") -> self_protection_2 : TERM
    UTTER propose(target=self_protection_2)
    TERM activity(actor=role_user, verb="job_duties") -> activity_7 : TERM
    TERM obligation(activity=activity_7, actor=role_user) -> obligation_2 : TERM
    UTTER propose(target=obligation_2)
    TERM activity(actor=role_user, object=role_friend, verb="seek_support") -> activity_8 : TERM
    UTTER propose(target=activity_8)
    TERM activity(actor=role_user, verb="create_exit_strategy") -> activity_9 : TERM
    UTTER propose(target=activity_9)
    TERM activity(actor=role_user, verb="quit_without_plan") -> activity_10 : TERM
    TERM negation(target=activity_10) -> negation_2 : TERM
    UTTER propose(target=negation_2)
    TERM activity(actor=role_user, instrument=platform_label::linkedin, verb="update_materials") -> activity_11 : TERM
    UTTER propose(target=activity_11)
    TERM requirement(property="next_job_preference", value=TRUE) -> requirement_2 : TERM
    CLAIM user_preference(constraints=requirement_2) BY role_user STATUS assumed SOURCE "t2:s39" -> user_preference_2 : CLAIM
    TERM activity(actor=role_user, verb="search_jobs") -> activity_12 : TERM
    CLAIM user_practice(activity=activity_12) BY role_agent STATUS asserted SOURCE "t2:s41" -> user_practice_2 : CLAIM
    UTTER propose(target=activity_12)
    TERM activity(actor=role_user, verb="build_emergency_fund") -> activity_13 : TERM
    UTTER propose(target=activity_13)
    TERM activity(actor=role_user, verb="apply_elsewhere") -> activity_14 : TERM
    UTTER propose(target=activity_14)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | comfortable, subject, role_user | covered |
| n2 | speech_act | ask, activity, role_user | covered |
| n3 | speech_act | apologize | covered |
| n4 | action | activity, propose, role_user | covered |
| n5 | object | subject, causes, personal_values, role_agent | covered |
| n6 | action | decision, activity, propose, role_user | covered |
| n7 | action | activity, role_manager, propose, role_user | covered |
| n8 | claim | subject, activity, leads_to, role_agent, role_user | covered |
| n9 | action | self_protection, propose, role_user | covered |
| n10 | action | obligation, activity, propose, role_user | covered |
| n11 | action | activity, role_friend, propose, role_user | covered |
| n12 | action | activity, propose, role_user | covered |
| n13 | negation | negation, activity, propose, role_user | covered |
| n14 | action | activity, platform_label::linkedin, propose, role_user | covered |
| n15 | action | user_preference, requirement, role_user | covered |
| n16 | action | activity, user_practice, propose, role_agent, role_user | covered |
| n17 | action | activity, propose, role_user | covered |
| n18 | action | activity, propose, role_user | covered |
| n19 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s52 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s37 "LinkedIn" → platform_label::linkedin (label only; platform name)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
