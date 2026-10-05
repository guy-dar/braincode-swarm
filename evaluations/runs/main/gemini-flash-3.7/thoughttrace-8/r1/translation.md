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
    TERM decision(activity=activity_2) -> decision_2 : TERM
    UTTER ask(target=decision_2)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER apologize(target=t1.comfortable_2, tone=tone_empathetic)
    TERM activity(actor=role_user, verb="identify_root_cause") -> activity_3 : TERM
    UTTER propose(target=activity_3)
    TERM subject(kind="workplace_culture") -> subject_3 : TERM
    TERM subject(kind="boss", qualifier=role_manager) -> subject_4 : TERM
    TERM subject(kind="coworkers", qualifier=role_colleague) -> subject_5 : TERM
    TERM subject(kind="workload") -> subject_6 : TERM
    TERM subject(kind="compensation") -> subject_7 : TERM
    TERM subject(kind="values_mismatch", qualifier=personal_values) -> subject_8 : TERM
    TERM conjunction(items=[subject_3, subject_4, subject_5, subject_6, subject_7, subject_8]) -> conjunction_2 : TERM
    CLAIM causes(cause=conjunction_2, effect=t1.comfortable_2) BY role_agent STATUS hypothesized SOURCE "t2:s10" -> causes_2 : CLAIM
    TERM activity(actor=role_user, verb="assess_fixability") -> activity_4 : TERM
    TERM decision(activity=activity_4) -> decision_3 : TERM
    UTTER propose(target=decision_3)
    TERM activity(actor=role_user, object=role_manager, verb="discuss_workload") -> activity_5 : TERM
    TERM activity(actor=role_user, verb="request_new_project") -> activity_6 : TERM
    TERM conjunction(items=[activity_5, activity_6]) -> conjunction_3 : TERM
    UTTER propose(target=conjunction_3)
    TERM subject(kind="toxic_culture", qualifier=role_manager) -> subject_9 : TERM
    TERM activity(actor=role_user, verb="plan_exit") -> activity_7 : TERM
    CLAIM leads_to(cause=subject_9, effect=activity_7) BY role_agent STATUS inferred SOURCE "t2:s24" -> leads_to_2 : CLAIM
    TERM self_protection(actor=role_user, domain="work", strategy="emotional_detachment") -> self_protection_2 : TERM
    UTTER propose(target=self_protection_2)
    TERM activity(actor=role_user, verb="perform_required_duties") -> activity_8 : TERM
    TERM obligation(activity=activity_8, actor=role_user) -> obligation_2 : TERM
    UTTER propose(target=obligation_2)
    TERM activity(actor=role_user, object=role_friend, verb="seek_support") -> activity_9 : TERM
    UTTER propose(target=activity_9)
    TERM activity(actor=role_user, verb="create_exit_strategy") -> activity_10 : TERM
    UTTER propose(target=activity_10)
    TERM activity(actor=role_user, verb="quit_without_plan") -> activity_11 : TERM
    TERM negation(target=activity_11) -> negation_2 : TERM
    UTTER propose(target=negation_2)
    TERM activity(actor=role_user, verb="update_resume_and_profile") -> activity_12 : TERM
    UTTER propose(target=activity_12)
    TERM activity(actor=role_user, verb="define_next_job_preferences") -> activity_13 : TERM
    CLAIM has_goal(goal=activity_13, subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s39" -> has_goal_2 : CLAIM
    TERM activity(actor=role_user, verb="search_jobs_and_network") -> activity_14 : TERM
    UTTER propose(target=activity_14)
    TERM activity(actor=role_user, verb="build_emergency_fund") -> activity_15 : TERM
    UTTER propose(target=activity_15)
    TERM activity(actor=role_user, verb="apply_for_jobs") -> activity_16 : TERM
    UTTER propose(target=activity_16)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | comfortable, subject, role_user | covered |
| n2 | speech_act | ask, decision, activity | covered |
| n3 | speech_act | apologize, tone_empathetic | covered |
| n4 | action | activity, propose | covered |
| n5 | object | causes, conjunction, subject, role_manager, role_colleague, personal_values | covered |
| n6 | action | decision, activity, propose | covered |
| n7 | action | activity, conjunction, propose, role_manager, role_user | covered |
| n8 | claim | leads_to, subject, activity, role_manager, role_user | covered |
| n9 | action | self_protection, propose, role_user | covered |
| n10 | action | obligation, activity, propose, role_user | covered |
| n11 | action | activity, propose, role_friend, role_user | covered |
| n12 | action | activity, propose, role_user | covered |
| n13 | negation | negation, activity, propose, role_user | covered |
| n14 | action | activity, propose, role_user | covered |
| n15 | action | has_goal, activity, role_user | covered |
| n16 | action | activity, propose, role_user | covered |
| n17 | action | activity, propose, role_user | covered |
| n18 | action | activity, propose, role_user | covered |
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
