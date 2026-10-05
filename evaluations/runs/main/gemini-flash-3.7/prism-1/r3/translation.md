Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="work_hours", location=country::JP) -> subject_2 : TERM
    TERM activity(location=country::JP, verb="personal_activities") -> activity_2 : TERM
    TERM conjunction(items=[subject_2, activity_2]) -> conjunction_2 : TERM
    TERM subject(kind="problem", location=country::JP, qualifier=conjunction_2) -> subject_3 : TERM
    UTTER ask(target=subject_3)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM activity(location=country::JP, verb="adopt_flexible_working") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_agent STATUS reported SOURCE "t2:s1" -> statement_2 : CLAIM
    CLAIM occurred_recently(target=statement_2) BY role_agent STATUS reported SOURCE "t2:s1" -> occurred_recently_2 : CLAIM
    TERM subject(kind="employee_morale_and_balance") -> subject_4 : TERM
    CLAIM enables(condition=activity_3, outcome=subject_4) BY role_agent STATUS reported SOURCE "t2:s1" -> enables_2 : CLAIM
    TERM subject(kind="productivity_and_growth") -> subject_5 : TERM
    CLAIM enables(condition=activity_3, outcome=subject_5) BY role_agent STATUS reported SOURCE "t2:s2" -> enables_3 : CLAIM
    TERM duration(amount=8, unit=unit_hour) -> duration_2 : TERM
    TERM activity(location=country::JP, purpose=duration_2, verb="work_longer_hours") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_agent STATUS reported SOURCE "t2:s3" -> statement_3 : CLAIM
    TERM subject(kind="high_workload") -> subject_6 : TERM
    CLAIM causes(cause=subject_6, effect=statement_3) BY role_agent STATUS reported SOURCE "t2:s3" -> causes_2 : CLAIM
    LINK supports(conclusion=statement_3, premise=causes_2) SOURCE "t2:s3"
    TERM subject(kind="workplace_issues", location=country::JP) -> subject_7 : TERM
    CLAIM leads_to(cause=activity_3, effect=subject_7) BY role_agent STATUS reported SOURCE "t2:s4" -> leads_to_2 : CLAIM
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM measure(amount=2, unit=unit_day) -> measure_2 : TERM
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM subject(kind="jobs", location=country::JP, qualifier=at_least_2) -> subject_8 : TERM
    TERM activity(location=country::JP, object=subject_8, verb="hold_jobs") -> activity_5 : TERM
    UTTER ask(target=activity_5)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM activity(location=country::JP, verb="multiple_part_time_jobs") -> activity_6 : TERM
    CLAIM statement(fact=activity_6) BY role_agent STATUS reported SOURCE "t4:s1" -> statement_4 : CLAIM
    UTTER confirm(target=statement_4)
    TERM subject(kind="income_and_schedule_balance") -> subject_9 : TERM
    CLAIM enables(condition=activity_6, outcome=subject_9) BY role_agent STATUS reported SOURCE "t4:s2" -> enables_4 : CLAIM
    TERM subject(kind="lack_of_free_time_and_stress") -> subject_10 : TERM
    CLAIM leads_to(cause=activity_6, effect=subject_10) BY role_agent STATUS reported SOURCE "t4:s2" -> leads_to_3 : CLAIM
    TERM activity(location=country::JP, verb="prioritize_leisure_and_hobbies") -> activity_7 : TERM
    CLAIM user_practice(activity=activity_7) BY role_agent STATUS reported SOURCE "t4:s3" -> user_practice_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, subject, conjunction | covered |
| n2 | object | country::JP | covered |
| n3 | object | unit_hour, subject | covered |
| n4 | object | activity | covered |
| n5 | temporal | occurred_recently | covered |
| n6 | claim | statement, activity | covered |
| n7 | claim | enables, subject | covered |
| n8 | claim | enables, subject | covered |
| n9 | claim | statement, activity, duration, unit_hour | covered |
| n10 | reasoning | causes, supports | covered |
| n11 | claim | leads_to, subject | covered |
| n12 | object | country::JP | covered |
| n13 | speech_act | ask, activity | covered |
| n14 | object | subject | covered |
| n15 | constraint | at_least, measure | covered |
| n16 | speech_act | confirm, statement | covered |
| n17 | object | country::JP | covered |
| n18 | claim | enables, subject | covered |
| n19 | claim | leads_to, subject | covered |
| n20 | claim | user_practice, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s6 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
