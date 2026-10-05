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
    TERM activity(actor=role_agent, verb="advise") -> activity_2 : TERM
    UTTER ask(target=activity_2, recipient=role_agent)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER apologize(target=t1.comfortable_2, tone=tone_empathetic)
    TERM subject(kind="management", qualifier=role_manager) -> subject_3 : TERM
    TERM subject(kind="coworkers", qualifier=role_colleague) -> subject_4 : TERM
    TERM subject(kind="alignment", qualifier=personal_values) -> subject_5 : TERM
    TERM conjunction(items=[subject_3, subject_4, subject_5]) -> conjunction_2 : TERM
    CLAIM causes(cause=conjunction_2, effect=t1.comfortable_2) BY role_agent STATUS hypothesized SOURCE "t2:s10" -> causes_2 : CLAIM
    TERM activity(actor=role_user, purpose=conjunction_2, verb="identify_root_cause") -> activity_3 : TERM
    UTTER propose(target=activity_3)
    TERM activity(actor=role_user, verb="assess_fixability") -> activity_4 : TERM
    TERM decision(activity=activity_4) -> decision_2 : TERM
    UTTER propose(target=decision_2)
    TERM activity(actor=role_user, object=role_manager, verb="discuss_boundaries") -> activity_5 : TERM
    TERM activity(actor=role_user, verb="request_new_project") -> activity_6 : TERM
    TERM conjunction(items=[activity_5, activity_6]) -> conjunction_3 : TERM
    UTTER propose(target=conjunction_3)
    TERM subject(kind="toxic_culture", qualifier=role_manager) -> subject_6 : TERM
    TERM activity(actor=role_user, verb="plan_exit") -> activity_7 : TERM
    CLAIM leads_to(cause=subject_6, effect=activity_7) BY role_agent STATUS inferred SOURCE "t2:s25" -> leads_to_2 : CLAIM
    TERM self_protection(actor=role_user, domain="mental_health", strategy="emotional_detachment") -> self_protection_2 : TERM
    UTTER propose(target=self_protection_2)
    TERM activity(actor=role_user, verb="perform_required_duties") -> activity_8 : TERM
    TERM obligation(activity=activity_8, actor=role_user) -> obligation_2 : TERM
    UTTER propose(target=obligation_2)
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="seek_support") -> interpersonal_stance_2 : TERM
    UTTER propose(target=interpersonal_stance_2)
    TERM activity(actor=role_user, verb="create_exit_strategy") -> activity_9 : TERM
    UTTER propose(target=activity_9)
    TERM activity(actor=role_user, verb="quit_without_plan") -> activity_10 : TERM
    TERM negation(target=activity_10) -> negation_2 : TERM
    UTTER propose(target=negation_2)
    TERM activity(actor=role_user, verb="update_resume") -> activity_11 : TERM
    UTTER propose(target=activity_11)
    TERM subject(kind="job_preferences") -> subject_7 : TERM
    TERM activity(actor=role_user, object=subject_7, verb="define_preferences") -> activity_12 : TERM
    UTTER propose(target=activity_12)
    TERM duration(amount=60, unit=unit_minute) -> duration_2 : TERM
    TERM activity(actor=role_user, purpose=duration_2, verb="search_job") -> activity_13 : TERM
    UTTER propose(target=activity_13)
    TERM activity(actor=role_user, verb="build_emergency_fund") -> activity_14 : TERM
    UTTER propose(target=activity_14)
    TERM activity(actor=role_user, verb="apply_jobs") -> activity_15 : TERM
    UTTER propose(target=activity_15)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | comfortable, subject, role_user | covered |
| n2 | speech_act | ask, activity, role_agent | covered |
| n3 | speech_act | apologize, tone_empathetic | covered |
| n4 | action | activity, propose | covered |
| n5 | object | subject, conjunction, role_manager, role_colleague, personal_values, causes | covered |
| n6 | action | activity, decision, propose | covered |
| n7 | action | activity, conjunction, role_manager, propose | covered |
| n8 | claim | subject, role_manager, activity, leads_to | covered |
| n9 | action | self_protection, role_user, propose | covered |
| n10 | action | activity, obligation, role_user, propose | covered |
| n11 | action | interpersonal_stance, role_user, role_friend, propose | covered |
| n12 | action | activity, role_user, propose | covered |
| n13 | negation | activity, negation, propose | covered |
| n14 | action | activity, role_user, propose | covered |
| n15 | action | subject, activity, role_user, propose | covered |
| n16 | action | duration, unit_minute, activity, role_user, propose | covered |
| n17 | action | activity, role_user, propose | covered |
| n18 | action | activity, role_user, propose | covered |
| n19 | speech_act | offer_help, offer | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s52 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
