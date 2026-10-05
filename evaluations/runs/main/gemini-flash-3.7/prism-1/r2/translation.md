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
    TERM property_question(property="issue", subject=conjunction_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM duration(amount=1, unit=unit_hour) -> duration_2 : TERM
    TERM activity(location=country::JP, purpose=duration_2, verb="flexible_work") -> activity_3 : TERM
    CLAIM user_practice(activity=activity_3) BY role_agent STATUS reported SOURCE "t2:s1" -> user_practice_2 : CLAIM
    CLAIM occurred_recently(target=user_practice_2) BY role_agent STATUS reported SOURCE "t2:s1" -> occurred_recently_2 : CLAIM
    TERM activity(verb="improve_morale") -> activity_4 : TERM
    CLAIM enables(condition=activity_3, outcome=activity_4) BY role_agent STATUS reported SOURCE "t2:s1" -> enables_2 : CLAIM
    TERM activity(verb="improve_productivity") -> activity_5 : TERM
    CLAIM enables(condition=activity_3, outcome=activity_5) BY role_agent STATUS reported SOURCE "t2:s2" -> enables_3 : CLAIM
    TERM activity(location=country::JP, verb="overtime_work") -> activity_6 : TERM
    CLAIM user_practice(activity=activity_6) BY role_agent STATUS reported SOURCE "t2:s3" -> user_practice_3 : CLAIM
    LINK supports(conclusion=user_practice_3, premise=enables_2) SOURCE "t2:s3"
    TERM subject(kind="issue", location=country::JP) -> subject_2 : TERM
    CLAIM leads_to(cause=activity_3, effect=subject_2) BY role_agent STATUS reported SOURCE "t2:s4" -> leads_to_2 : CLAIM
    CLAIM user_practice(activity=activity_6) BY role_agent STATUS reported SOURCE "t2:s5" -> user_practice_4 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM measure(amount=2, unit=unit_hour) -> measure_2 : TERM
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM requirement(property="job_count", value=at_least_2) -> requirement_2 : TERM
    TERM activity(actor="japanese_people", location=country::JP, purpose=requirement_2, verb="multiple_jobs") -> activity_7 : TERM
    TERM property_question(property="prevalence", subject=activity_7) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM activity(location=country::JP, verb="part_time_job") -> activity_8 : TERM
    CLAIM user_practice(activity=activity_8) BY role_agent STATUS reported SOURCE "t4:s1" -> user_practice_5 : CLAIM
    UTTER confirm(target=user_practice_5)
    TERM activity(verb="balance_income_and_schedule") -> activity_9 : TERM
    CLAIM enables(condition=activity_8, outcome=activity_9) BY role_agent STATUS reported SOURCE "t4:s2" -> enables_4 : CLAIM
    TERM subject(kind="stress") -> subject_3 : TERM
    CLAIM leads_to(cause=activity_8, effect=subject_3) BY role_agent STATUS reported SOURCE "t4:s2" -> leads_to_3 : CLAIM
    TERM activity(location=country::JP, verb="hobbies_and_work_life_balance") -> activity_10 : TERM
    CLAIM user_practice(activity=activity_10) BY role_agent STATUS reported SOURCE "t4:s3" -> user_practice_6 : CLAIM
    CLAIM user_practice(activity=activity_8) BY role_agent STATUS reported SOURCE "t4:s4" -> user_practice_7 : CLAIM
    CLAIM leads_to(cause=activity_8, effect=subject_3) BY role_agent STATUS reported SOURCE "t4:s5" -> leads_to_4 : CLAIM
    CLAIM user_practice(activity=activity_10) BY role_agent STATUS reported SOURCE "t4:s6" -> user_practice_8 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, conjunction | covered |
| n2 | object | country::JP | covered |
| n3 | object | topic_school_work_routine | covered |
| n4 | object | activity | covered |
| n5 | temporal | occurred_recently | covered |
| n6 | claim | user_practice, activity, country::JP, duration, unit_hour | covered |
| n7 | claim | enables, activity | covered |
| n8 | claim | enables, activity | covered |
| n9 | claim | user_practice, activity, country::JP | covered |
| n10 | reasoning | supports | covered |
| n11 | claim | leads_to, subject, country::JP | covered |
| n12 | object | country::JP | covered |
| n13 | speech_act | ask, property_question, activity, country::JP | covered |
| n14 | object | activity | covered |
| n15 | constraint | requirement, at_least, measure, unit_hour | covered |
| n16 | speech_act | confirm, user_practice, activity, country::JP | covered |
| n17 | object | country::JP | covered |
| n18 | claim | enables, activity | covered |
| n19 | claim | leads_to, activity, subject | covered |
| n20 | claim | user_practice, activity, country::JP | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s6 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
