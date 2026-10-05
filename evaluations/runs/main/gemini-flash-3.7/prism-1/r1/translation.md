Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="work", location=country::JP) -> subject_2 : TERM
    TERM subject(kind="personal_activities", location=country::JP) -> subject_3 : TERM
    TERM conjunction(items=[subject_2, subject_3]) -> conjunction_2 : TERM
    TERM subject(kind="problem", qualifier=conjunction_2) -> subject_4 : TERM
    UTTER ask(target=subject_4)
  }
  TURN t2 SPEAKER=AGENT {
    TERM duration(amount=1, unit=unit_hour) -> duration_2 : TERM
    TERM activity(location=country::JP, verb="work") -> activity_2 : TERM
    TERM subject(kind="flexible_working_arrangements", location=country::JP) -> subject_5 : TERM
    TERM subject(kind="shorter_working_hours", location=country::JP) -> subject_6 : TERM
    CLAIM ongoing(target=subject_5) BY agent STATUS asserted SOURCE "t2:s1" -> ongoing_2 : CLAIM
    CLAIM occurred_recently(target=ongoing_2) BY agent STATUS asserted SOURCE "t2:s1" -> occurred_recently_2 : CLAIM
    TERM subject(kind="morale_and_balance") -> subject_7 : TERM
    CLAIM enables(condition=subject_5, outcome=subject_7) BY agent STATUS asserted SOURCE "t2:s1" -> enables_2 : CLAIM
    TERM subject(kind="productivity_and_growth") -> subject_8 : TERM
    CLAIM enables(condition=subject_5, outcome=subject_8) BY agent STATUS inferred SOURCE "t2:s2" -> enables_3 : CLAIM
    CLAIM user_practice(activity=activity_2) BY agent STATUS asserted SOURCE "t2:s3" -> user_practice_2 : CLAIM
    LINK supports(conclusion=user_practice_2, premise=enables_2) SOURCE "t2:s3"
    TERM subject(kind="issues", location=country::JP) -> subject_9 : TERM
    CLAIM ongoing(target=subject_9) BY agent STATUS asserted SOURCE "t2:s4" -> ongoing_3 : CLAIM
    LINK supports(conclusion=ongoing_3, premise=user_practice_2) SOURCE "t2:s5"
    UTTER respond(target=ongoing_3)
  }
  TURN t3 SPEAKER=USER {
    TERM measure(amount=2, unit=unit_day) -> measure_2 : TERM
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM requirement(property="multiple_jobs", value=at_least_2) -> requirement_2 : TERM
    TERM subject(kind="multiple_jobs", location=country::JP, qualifier=requirement_2) -> subject_10 : TERM
    UTTER ask(target=subject_10)
  }
  TURN t4 SPEAKER=AGENT {
    TERM activity(location=country::JP, verb="multiple_part_time_jobs") -> activity_3 : TERM
    CLAIM user_practice(activity=activity_3) BY agent STATUS asserted SOURCE "t4:s1" -> user_practice_3 : CLAIM
    UTTER confirm(target=user_practice_3)
    TERM subject(kind="balance_income_and_schedule") -> subject_11 : TERM
    CLAIM enables(condition=activity_3, outcome=subject_11) BY agent STATUS asserted SOURCE "t4:s2" -> enables_4 : CLAIM
    TERM subject(kind="lack_of_free_time_and_stress") -> subject_12 : TERM
    CLAIM leads_to(cause=activity_3, effect=subject_12) BY agent STATUS asserted SOURCE "t4:s2" -> leads_to_2 : CLAIM
    TERM subject(kind="hobbies_and_work_life_balance", location=country::JP) -> subject_13 : TERM
    CLAIM important(target=subject_13) BY agent STATUS asserted SOURCE "t4:s3" -> important_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, conjunction, subject | covered |
| n2 | object | country::JP | covered |
| n3 | object | activity, duration, unit_hour | covered |
| n4 | object | subject | covered |
| n5 | temporal | occurred_recently | covered |
| n6 | claim | ongoing | covered |
| n7 | claim | enables | covered |
| n8 | claim | enables | covered |
| n9 | claim | user_practice | covered |
| n10 | reasoning | supports | covered |
| n11 | claim | ongoing, subject | covered |
| n12 | object | country::JP | covered |
| n13 | speech_act | ask, subject | covered |
| n14 | object | subject | covered |
| n15 | constraint | at_least, measure, requirement, unit_day | covered |
| n16 | speech_act | confirm | covered |
| n17 | object | country::JP | covered |
| n18 | claim | enables | covered |
| n19 | claim | leads_to | covered |
| n20 | claim | important | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s6 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
