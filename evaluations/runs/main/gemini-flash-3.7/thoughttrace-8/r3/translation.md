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
    TERM activity(verb="advise") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    UTTER apologize(target=t1.comfortable_2, tone=tone_empathetic)
    TERM subject(kind="job_discomfort") -> subject_2 : TERM
    TERM activity(actor="user", purpose=subject_2, verb="identify_root_cause") -> activity_2 : TERM
    UTTER propose(target=activity_2)
    TERM subject(kind="culture") -> subject_3 : TERM
    TERM subject(kind="manager", qualifier="micromanaging") -> subject_4 : TERM
    TERM subject(kind="coworkers") -> subject_5 : TERM
    TERM subject(kind="workload") -> subject_6 : TERM
    TERM subject(kind="compensation") -> subject_7 : TERM
    TERM subject(kind="values_mismatch", qualifier=personal_values) -> subject_8 : TERM
    TERM conjunction(items=[subject_3, subject_4, subject_5, subject_6, subject_7, subject_8]) -> conjunction_2 : TERM
    CLAIM causes(cause=conjunction_2, effect=t1.comfortable_2) BY role_agent STATUS hypothesized SOURCE "t2:s10" -> causes_2 : CLAIM
    TERM activity(verb="assess_fixable") -> activity_3 : TERM
    TERM decision(activity=activity_3) -> decision_2 : TERM
    UTTER propose(target=decision_2)
    TERM subject(kind="boundaries", qualifier="workload") -> subject_9 : TERM
    TERM activity(actor="user", object=subject_9, verb="discuss_with_manager") -> activity_4 : TERM
    UTTER propose(target=activity_4)
    TERM subject(kind="toxic_culture") -> subject_10 : TERM
    TERM subject(kind="exit_plan") -> subject_11 : TERM
    CLAIM leads_to(cause=subject_10, effect=subject_11) BY role_agent STATUS inferred SOURCE "t2:s25" -> leads_to_2 : CLAIM
    TERM self_protection(actor=role_user, domain="mental_health") -> self_protection_2 : TERM
    UTTER propose(target=self_protection_2)
    TERM activity(verb="perform_required_duties") -> activity_5 : TERM
    TERM obligation(activity=activity_5, actor=role_user) -> obligation_2 : TERM
    UTTER propose(target=obligation_2)
    TERM subject(kind="friends") -> subject_12 : TERM
    TERM subject(kind="family") -> subject_13 : TERM
    TERM subject(kind="therapist") -> subject_14 : TERM
    TERM conjunction(items=[subject_12, subject_13, subject_14]) -> conjunction_3 : TERM
    TERM interpersonal_stance(actor=role_user, stance="seek_support", target=conjunction_3) -> interpersonal_stance_2 : TERM
    UTTER propose(target=interpersonal_stance_2)
    TERM activity(verb="formulate_exit_strategy") -> activity_6 : TERM
    UTTER propose(target=activity_6)
    TERM activity(verb="quit_without_plan") -> activity_7 : TERM
    TERM negation(target=activity_7) -> negation_2 : TERM
    UTTER propose(target=negation_2)
    TERM subject(kind="resume") -> subject_15 : TERM
    TERM subject(kind="linkedin_profile") -> subject_16 : TERM
    TERM conjunction(items=[subject_15, subject_16]) -> conjunction_4 : TERM
    TERM activity(object=conjunction_4, verb="update") -> activity_8 : TERM
    UTTER propose(target=activity_8)
    TERM subject(kind="next_job_preferences") -> subject_17 : TERM
    CLAIM has_goal(goal=subject_17, subject="user") BY role_agent STATUS asserted SOURCE "t2:s39" -> has_goal_2 : CLAIM
    TERM activity(verb="search_job") -> activity_9 : TERM
    CLAIM user_practice(activity=activity_9) BY role_agent STATUS asserted SOURCE "t2:s41" -> user_practice_2 : CLAIM
    TERM activity(verb="build_emergency_fund") -> activity_10 : TERM
    UTTER propose(target=activity_10)
    TERM activity(verb="apply_other_jobs") -> activity_11 : TERM
    UTTER propose(target=activity_11)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | comfortable, role_user, subject | covered |
| n2 | speech_act | ask, activity | covered |
| n3 | speech_act | apologize, tone_empathetic | covered |
| n4 | action | propose, activity, subject | covered |
| n5 | object | causes, conjunction, subject, personal_values | covered |
| n6 | action | propose, decision, activity | covered |
| n7 | action | propose, activity, subject | covered |
| n8 | claim | leads_to, role_agent, subject | covered |
| n9 | action | propose, self_protection, role_user | covered |
| n10 | action | propose, obligation, role_user, activity | covered |
| n11 | action | propose, interpersonal_stance, role_user, conjunction, subject | covered |
| n12 | action | propose, activity | covered |
| n13 | negation | propose, negation, activity | covered |
| n14 | action | propose, activity, conjunction, subject | covered |
| n15 | action | has_goal, role_agent, subject | covered |
| n16 | action | user_practice, role_agent, activity | covered |
| n17 | action | propose, activity | covered |
| n18 | action | propose, activity | covered |
| n19 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s52 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
