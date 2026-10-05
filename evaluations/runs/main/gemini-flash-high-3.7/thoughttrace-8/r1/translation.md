Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="job") -> subject_2 : TERM
    TERM subject(kind="user", qualifier=subject_2) -> subject_3 : TERM
    CLAIM comfortable(person=subject_3, value=FALSE) BY role_user STATUS asserted SOURCE "t1:s1" -> comfortable_2 : CLAIM
    TERM activity(actor=role_user, verb="seek_advice") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER apologize(target=t1.comfortable_2, tone=tone_empathetic)
    TERM activity(actor=role_user, object=t1.subject_2, verb="identify_root_cause") -> activity_3 : TERM
    CLAIM recommended(target=activity_3) BY role_agent STATUS asserted SOURCE "t2:s7" -> recommended_2 : CLAIM
    UTTER propose(target=activity_3)
    TERM subject(kind="workplace_culture") -> subject_4 : TERM
    TERM subject(kind="manager", qualifier=role_manager) -> subject_5 : TERM
    TERM subject(kind="coworkers", qualifier=role_colleague) -> subject_6 : TERM
    TERM subject(kind="workload") -> subject_7 : TERM
    TERM subject(kind="compensation") -> subject_8 : TERM
    TERM subject(kind="values_mismatch", qualifier=personal_values) -> subject_9 : TERM
    TERM conjunction(items=[subject_4, subject_5, subject_6, subject_7, subject_8, subject_9]) -> conjunction_2 : TERM
    CLAIM causes(cause=conjunction_2, effect=t1.comfortable_2) BY role_agent STATUS hypothesized SOURCE "t2:s10" -> causes_2 : CLAIM
    TERM activity(actor=role_user, verb="assess_fixability") -> activity_4 : TERM
    TERM decision(activity=activity_4) -> decision_2 : TERM
    CLAIM recommended(target=decision_2) BY role_agent STATUS asserted SOURCE "t2:s20" -> recommended_3 : CLAIM
    TERM activity(actor=role_user, object=role_manager, verb="discuss_boundaries") -> activity_5 : TERM
    TERM activity(actor=role_user, object=role_manager, verb="request_new_projects") -> activity_6 : TERM
    TERM conjunction(items=[activity_5, activity_6]) -> conjunction_3 : TERM
    CLAIM recommended(target=conjunction_3) BY role_agent STATUS asserted SOURCE "t2:s22" -> recommended_4 : CLAIM
    TERM subject(kind="toxic_culture", qualifier=role_manager) -> subject_10 : TERM
    TERM activity(actor=role_user, verb="plan_exit") -> activity_7 : TERM
    CLAIM leads_to(cause=subject_10, effect=activity_7) BY role_agent STATUS inferred SOURCE "t2:s24" -> leads_to_2 : CLAIM
    TERM self_protection(actor=role_user, domain="mental_health", strategy="emotional_detachment") -> self_protection_2 : TERM
    CLAIM recommended(target=self_protection_2) BY role_agent STATUS asserted SOURCE "t2:s27" -> recommended_5 : CLAIM
    TERM activity(actor=role_user, verb="perform_required_duties") -> activity_8 : TERM
    TERM obligation(activity=activity_8, actor=role_user) -> obligation_2 : TERM
    CLAIM recommended(target=obligation_2) BY role_agent STATUS asserted SOURCE "t2:s31" -> recommended_6 : CLAIM
    TERM activity(actor=role_user, object=role_friend, verb="seek_support") -> activity_9 : TERM
    CLAIM recommended(target=activity_9) BY role_agent STATUS asserted SOURCE "t2:s32" -> recommended_7 : CLAIM
    TERM activity(actor=role_user, verb="create_exit_strategy") -> activity_10 : TERM
    CLAIM recommended(target=activity_10) BY role_agent STATUS asserted SOURCE "t2:s35" -> recommended_8 : CLAIM
    TERM activity(actor=role_user, verb="quit_without_plan") -> activity_11 : TERM
    TERM negation(target=activity_11) -> negation_2 : TERM
    CLAIM recommended(target=negation_2) BY role_agent STATUS asserted SOURCE "t2:s36" -> recommended_9 : CLAIM
    TERM activity(actor=role_user, instrument=platform_label::linkedin, verb="update_resume") -> activity_12 : TERM
    CLAIM recommended(target=activity_12) BY role_agent STATUS asserted SOURCE "t2:s37" -> recommended_10 : CLAIM
    TERM subject(kind="next_job") -> subject_11 : TERM
    TERM activity(actor=role_user, object=subject_11, verb="define_preferences") -> activity_13 : TERM
    CLAIM has_goal(goal=activity_13, subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s39" -> has_goal_2 : CLAIM
    TERM duration(amount=60, unit=unit_minute) -> duration_2 : TERM
    TERM activity(actor=role_user, purpose=duration_2, verb="job_hunt_daily") -> activity_14 : TERM
    CLAIM user_practice(activity=activity_14) BY role_agent STATUS asserted SOURCE "t2:s41" -> user_practice_2 : CLAIM
    TERM activity(actor=role_user, verb="build_emergency_fund") -> activity_15 : TERM
    CLAIM recommended(target=activity_15) BY role_agent STATUS asserted SOURCE "t2:s42" -> recommended_11 : CLAIM
    TERM activity(actor=role_user, verb="apply_for_jobs") -> activity_16 : TERM
    CLAIM recommended(target=activity_16) BY role_agent STATUS asserted SOURCE "t2:s46" -> recommended_12 : CLAIM
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
| n3 | speech_act | apologize, tone_empathetic | covered |
| n4 | action | activity, recommended, propose, role_user | covered |
| n5 | object | subject, conjunction, causes, role_manager, role_colleague, personal_values | covered |
| n6 | action | activity, decision, recommended, role_user | covered |
| n7 | action | activity, role_manager, conjunction, recommended, role_user | covered |
| n8 | claim | subject, role_manager, activity, leads_to, role_user | covered |
| n9 | action | self_protection, recommended, role_user | covered |
| n10 | action | activity, obligation, recommended, role_user | covered |
| n11 | action | activity, role_friend, recommended, role_user | covered |
| n12 | action | activity, recommended, role_user | covered |
| n13 | negation | activity, negation, recommended, role_user | covered |
| n14 | action | activity, platform_label::linkedin, recommended, role_user | covered |
| n15 | action | subject, activity, has_goal, role_user | covered |
| n16 | action | duration, unit_minute, activity, user_practice, role_user | covered |
| n17 | action | activity, recommended, role_user | covered |
| n18 | action | activity, recommended, role_user | covered |
| n19 | speech_act | offer_help, offer | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s52 is represented in structured terms and claims
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
