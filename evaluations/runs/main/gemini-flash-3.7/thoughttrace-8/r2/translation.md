Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="job") -> subject_2 : TERM
    CLAIM comfortable(person=subject_2, value=FALSE) BY role_user STATUS asserted SOURCE "t1:s1" -> comfortable_2 : CLAIM
    TERM activity(actor=role_user, verb="seek_advice") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER apologize(target=t1.comfortable_2, tone=tone_empathetic)
    TERM activity(actor=role_user, verb="identify_root_cause") -> activity_3 : TERM
    TERM decision(activity=activity_3) -> decision_2 : TERM
    CLAIM recommended(target=decision_2) BY role_agent STATUS asserted SOURCE "t2:s7" -> recommended_2 : CLAIM
    TERM subject(kind="workplace_cause", qualifier=personal_values) -> subject_3 : TERM
    CLAIM causes(cause=subject_3, effect=t1.comfortable_2) BY role_agent STATUS hypothesized SOURCE "t2:s10" -> causes_2 : CLAIM
    TERM activity(actor=role_user, verb="assess_fixability") -> activity_4 : TERM
    TERM decision(activity=activity_4) -> decision_3 : TERM
    CLAIM recommended(target=decision_3) BY role_agent STATUS asserted SOURCE "t2:s21" -> recommended_3 : CLAIM
    TERM activity(actor=role_user, object=role_manager, verb="discuss_boundaries") -> activity_5 : TERM
    CLAIM request(target=activity_5) BY role_user STATUS hypothesized SOURCE "t2:s22" -> request_2 : CLAIM
    TERM subject(kind="toxic_culture", qualifier=role_manager) -> subject_4 : TERM
    TERM activity(actor=role_user, verb="plan_exit") -> activity_6 : TERM
    CLAIM leads_to(cause=subject_4, effect=activity_6) BY role_agent STATUS inferred SOURCE "t2:s25" -> leads_to_2 : CLAIM
    TERM self_protection(actor=role_user, domain="mental_health") -> self_protection_2 : TERM
    CLAIM attitude(target=self_protection_2, holder=role_user, type="detachment") BY role_agent STATUS recommended SOURCE "t2:s29" -> attitude_2 : CLAIM
    TERM activity(actor=role_user, verb="job_duties") -> activity_7 : TERM
    TERM obligation(activity=activity_7, actor=role_user) -> obligation_2 : TERM
    CLAIM constrained_by(activity=activity_7, constraint=obligation_2) BY role_agent STATUS recommended SOURCE "t2:s31" -> constrained_by_2 : CLAIM
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="seek_support") -> interpersonal_stance_2 : TERM
    CLAIM recommended(target=interpersonal_stance_2) BY role_agent STATUS asserted SOURCE "t2:s32" -> recommended_4 : CLAIM
    TERM activity(actor=role_user, verb="formulate_exit_strategy") -> activity_8 : TERM
    UTTER propose(target=activity_8)
    TERM activity(actor=role_user, verb="quit_job") -> activity_9 : TERM
    TERM negation(target=activity_9) -> negation_2 : TERM
    CLAIM recommended(target=negation_2) BY role_agent STATUS asserted SOURCE "t2:s36" -> recommended_5 : CLAIM
    TERM activity(actor=role_user, object=platform_label::linkedin, verb="update_profile") -> activity_10 : TERM
    CLAIM role(role_type="accomplishments", subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s38" -> role_2 : CLAIM
    TERM subject(kind="next_job") -> subject_5 : TERM
    CLAIM has_goal(goal=subject_5, subject=role_user) BY role_agent STATUS recommended SOURCE "t2:s39" -> has_goal_2 : CLAIM
    CLAIM user_preference(constraints=subject_5) BY role_user STATUS hypothesized SOURCE "t2:s40" -> user_preference_2 : CLAIM
    TERM activity(actor=role_user, verb="search_jobs") -> activity_11 : TERM
    CLAIM user_practice(activity=activity_11) BY role_user STATUS hypothesized SOURCE "t2:s41" -> user_practice_2 : CLAIM
    TERM constraint_budget_limited() -> constraint_budget_limited_2 : TERM
    TERM time_horizon(horizon="future") -> time_horizon_2 : TERM
    CLAIM recommended(target=constraint_budget_limited_2) BY role_agent STATUS asserted SOURCE "t2:s42" -> recommended_6 : CLAIM
    TERM activity(actor=role_user, verb="apply_for_jobs") -> activity_12 : TERM
    UTTER propose(target=activity_12)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | comfortable | covered |
| n2 | speech_act | ask | covered |
| n3 | speech_act | apologize, tone_empathetic | covered |
| n4 | action | activity, decision, recommended | covered |
| n5 | object | causes, personal_values, role_manager | covered |
| n6 | action | activity, decision, recommended | covered |
| n7 | action | activity, role_manager, request | covered |
| n8 | claim | leads_to, role_manager | covered |
| n9 | action | self_protection, attitude | covered |
| n10 | action | obligation, constrained_by | covered |
| n11 | action | interpersonal_stance, role_friend, recommended | covered |
| n12 | action | activity, propose | covered |
| n13 | negation | negation, recommended | covered |
| n14 | action | activity, platform_label::linkedin, role | covered |
| n15 | action | has_goal, user_preference | covered |
| n16 | action | activity, user_practice | covered |
| n17 | action | constraint_budget_limited, time_horizon, recommended | covered |
| n18 | action | activity, propose | covered |
| n19 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s52 is represented across the conversational steps.
- Opaque-text spans: none
- Label-preserved spans: t2:s37 "LinkedIn" → platform_label::linkedin
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
