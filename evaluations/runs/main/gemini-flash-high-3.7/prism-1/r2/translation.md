Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM duration(amount=1, unit=unit_hour) -> duration_2 : TERM
    TERM subject(kind="work", location=country::JP, qualifier=duration_2) -> subject_2 : TERM
    TERM activity(location=country::JP, verb="leisure") -> activity_2 : TERM
    TERM conjunction(items=[subject_2, activity_2]) -> conjunction_2 : TERM
    TERM property_question(property="issue", subject=conjunction_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="flexible_work", location=country::JP) -> subject_2 : TERM
    TERM subject(kind="work_life_balance") -> subject_3 : TERM
    CLAIM enables(condition=subject_2, outcome=subject_3) BY role_agent STATUS asserted SOURCE "t2:s1" -> enables_2 : CLAIM
    CLAIM occurred_recently(target=enables_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> occurred_recently_2 : CLAIM
    TERM subject(kind="productivity") -> subject_4 : TERM
    CLAIM enables(condition=subject_2, outcome=subject_4) BY role_agent STATUS reported SOURCE "t2:s2" -> enables_3 : CLAIM
    TERM duration(amount=8, unit=unit_hour) -> duration_2 : TERM
    TERM activity(location=country::JP, purpose=duration_2, verb="work") -> activity_2 : TERM
    CLAIM user_practice(activity=activity_2) BY role_agent STATUS hypothesized SOURCE "t2:s3" -> user_practice_2 : CLAIM
    LINK contrast(first=enables_2, second=user_practice_2) SOURCE "t2:s3"
    TERM subject(kind="issue", location=country::JP) -> subject_5 : TERM
    CLAIM leads_to(cause=subject_2, effect=subject_5) BY role_agent STATUS asserted SOURCE "t2:s4" -> leads_to_2 : CLAIM
    LINK contrast(first=enables_3, second=user_practice_2) SOURCE "t2:s5"
  }
  TURN t3 SPEAKER=USER {
    TERM measure(amount=2, unit=unit_item) -> measure_2 : TERM
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM requirement(property="jobs", value=at_least_2) -> requirement_2 : TERM
    TERM activity(location=country::JP, purpose=requirement_2, verb="work") -> activity_2 : TERM
    TERM property_question(property="frequency", subject=activity_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t4 SPEAKER=AGENT {
    TERM activity(location=country::JP, verb="part_time_work") -> activity_2 : TERM
    CLAIM user_practice(activity=activity_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> user_practice_2 : CLAIM
    UTTER confirm(target=user_practice_2)
    TERM subject(kind="income_balance") -> subject_2 : TERM
    CLAIM enables(condition=activity_2, outcome=subject_2) BY role_agent STATUS asserted SOURCE "t4:s2" -> enables_2 : CLAIM
    TERM subject(kind="stress") -> subject_3 : TERM
    CLAIM leads_to(cause=activity_2, effect=subject_3) BY role_agent STATUS asserted SOURCE "t4:s2" -> leads_to_2 : CLAIM
    TERM subject(kind="free_time_priority", location=country::JP) -> subject_4 : TERM
    CLAIM important(target=subject_4) BY role_agent STATUS asserted SOURCE "t4:s3" -> important_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question | covered |
| n2 | object | country::JP | covered |
| n3 | object | duration, unit_hour | covered |
| n4 | object | activity | covered |
| n5 | temporal | occurred_recently | covered |
| n6 | claim | enables | covered |
| n7 | claim | enables | covered |
| n8 | claim | enables | covered |
| n9 | claim | duration, unit_hour, user_practice | covered |
| n10 | reasoning | contrast | covered |
| n11 | claim | leads_to | covered |
| n12 | object | country::JP | covered |
| n13 | speech_act | ask, property_question | covered |
| n14 | object | activity | covered |
| n15 | constraint | at_least, measure, requirement | covered |
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
