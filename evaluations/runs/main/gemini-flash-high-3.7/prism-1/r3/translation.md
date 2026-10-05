Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM topic_school_work_routine() -> topic_school_work_routine_2 : TERM
    TERM activity(location=country::JP, verb="leisure") -> activity_2 : TERM
    TERM conjunction(items=[topic_school_work_routine_2, activity_2]) -> conjunction_2 : TERM
    UTTER ask(target=conjunction_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM duration(amount=6, unit=unit_hour) -> duration_2 : TERM
    TERM activity(location=country::JP, verb="flexible_work") -> activity_3 : TERM
    CLAIM ongoing(target=activity_3) BY role_agent STATUS reported SOURCE "t2:s1" -> ongoing_2 : CLAIM
    CLAIM occurred_recently(target=ongoing_2) BY role_agent STATUS reported SOURCE "t2:s1" -> occurred_recently_2 : CLAIM
    TERM subject(kind="morale_and_balance") -> subject_2 : TERM
    CLAIM enables(condition=activity_3, outcome=subject_2) BY role_agent STATUS reported SOURCE "t2:s1" -> enables_2 : CLAIM
    TERM subject(kind="productivity_and_growth") -> subject_3 : TERM
    CLAIM enables(condition=activity_3, outcome=subject_3) BY role_agent STATUS reported SOURCE "t2:s2" -> enables_3 : CLAIM
    TERM duration(amount=10, unit=unit_hour) -> duration_3 : TERM
    TERM activity(location=country::JP, verb="overtime_work") -> activity_4 : TERM
    CLAIM user_practice(activity=activity_4) BY role_agent STATUS reported SOURCE "t2:s3" -> user_practice_2 : CLAIM
    LINK contrast(first=enables_2, second=user_practice_2) SOURCE "t2:s3"
    TERM subject(kind="issues", location=country::JP) -> subject_4 : TERM
    CLAIM leads_to(cause=activity_3, effect=subject_4) BY role_agent STATUS reported SOURCE "t2:s4" -> leads_to_2 : CLAIM
    LINK supports(conclusion=user_practice_2, premise=leads_to_2) SOURCE "t2:s5"
    UTTER inform(target=enables_2)
  }
  TURN t3 SPEAKER=USER {
    TERM measure(amount=2, unit="job") -> measure_2 : TERM
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM subject(kind="multiple_jobs", location=country::JP, qualifier=at_least_2) -> subject_5 : TERM
    UTTER ask(target=subject_5)
  }
  TURN t4 SPEAKER=AGENT {
    TERM activity(location=country::JP, verb="part_time_jobs") -> activity_5 : TERM
    CLAIM user_practice(activity=activity_5) BY role_agent STATUS reported SOURCE "t4:s1" -> user_practice_3 : CLAIM
    UTTER confirm(target=user_practice_3)
    TERM subject(kind="balance_income_and_schedule") -> subject_6 : TERM
    CLAIM enables(condition=activity_5, outcome=subject_6) BY role_agent STATUS reported SOURCE "t4:s2" -> enables_4 : CLAIM
    TERM subject(kind="stress_and_time_deficit") -> subject_7 : TERM
    CLAIM leads_to(cause=activity_5, effect=subject_7) BY role_agent STATUS reported SOURCE "t4:s2" -> leads_to_3 : CLAIM
    LINK contrast(first=enables_4, second=leads_to_3) SOURCE "t4:s2"
    TERM activity(location=country::JP, verb="hobbies_and_leisure") -> activity_6 : TERM
    CLAIM user_practice(activity=activity_6) BY role_agent STATUS reported SOURCE "t4:s3" -> user_practice_4 : CLAIM
    LINK contrast(first=leads_to_3, second=user_practice_4) SOURCE "t4:s3"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | object | country::JP | covered |
| n3 | object | topic_school_work_routine, unit_hour | covered |
| n4 | object | activity, user_practice | covered |
| n5 | temporal | occurred_recently, duration | covered |
| n6 | claim | ongoing, unit_hour | covered |
| n7 | claim | enables | covered |
| n8 | claim | enables | covered |
| n9 | claim | user_practice, unit_hour | covered |
| n10 | reasoning | supports | covered |
| n11 | claim | leads_to | covered |
| n12 | object | country::JP | covered |
| n13 | speech_act | ask | covered |
| n14 | object | subject, unit_hour | covered |
| n15 | constraint | at_least | covered |
| n16 | speech_act | confirm | covered |
| n17 | object | country::JP | covered |
| n18 | claim | enables | covered |
| n19 | claim | leads_to | covered |
| n20 | claim | user_practice | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s6 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
