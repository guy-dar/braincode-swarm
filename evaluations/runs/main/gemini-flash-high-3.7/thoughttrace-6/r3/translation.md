Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
    TERM subject(kind="holiday", time="summer") -> subject_2 : TERM
    TERM activity(actor=role_agent, object=subject_2, verb="plan") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM greeting(recipient=role_user) -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
    TERM property_question(property="travelers", subject="holiday") -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    TERM property_question(property="origin", subject="holiday") -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
    TERM property_question(property="destination", subject="holiday") -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
    TERM property_question(property="budget", subject="holiday") -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
    TERM property_question(property="vibe", subject="holiday") -> property_question_6 : TERM
    UTTER ask(target=property_question_6)
    TERM property_question(property="duration", subject="holiday") -> property_question_7 : TERM
    UTTER ask(target=property_question_7)
    TERM property_question(property="constraints", subject="holiday") -> property_question_8 : TERM
    UTTER ask(target=property_question_8)
  }
  TURN t3 SPEAKER=USER {
    TERM group_size(count=2, group="couple") -> group_size_2 : TERM
    CLAIM statement(fact=group_size_2) BY role_user STATUS asserted SOURCE "t3:s1" -> statement_2 : CLAIM
    UTTER inform(target=statement_2)
    TERM activity(actor=role_user, location=country::IE, verb="live") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_user STATUS asserted SOURCE "t3:s2" -> statement_3 : CLAIM
    UTTER inform(target=statement_3)
    TERM activity(actor=role_user, location=country::IT, verb="travel") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_user STATUS asserted SOURCE "t3:s2" -> statement_4 : CLAIM
    UTTER inform(target=statement_4)
    TERM requirement(property="budget", value="flexible") -> requirement_2 : TERM
    CLAIM user_preference(constraints=requirement_2) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_2 : CLAIM
    UTTER inform(target=user_preference_2)
    TERM requirement(property="style", value="off_the_beaten_track") -> requirement_3 : TERM
    CLAIM user_preference(constraints=requirement_3) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_3 : CLAIM
    UTTER inform(target=user_preference_3)
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    CLAIM statement(fact=duration_2) BY role_user STATUS asserted SOURCE "t3:s4" -> statement_5 : CLAIM
    UTTER inform(target=statement_5)
  }
  TURN t4 SPEAKER=AGENT {
    TERM location_spec(area="Abruzzo") -> location_spec_2 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_2) -> subject_2 : TERM
    UTTER propose(target=subject_2)
    TERM location_spec(area="Maremma", state="Tuscany") -> location_spec_3 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_3) -> subject_3 : TERM
    UTTER propose(target=subject_3)
    TERM location_spec(area="Basilicata and inland Puglia") -> location_spec_4 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_4) -> subject_4 : TERM
    UTTER propose(target=subject_4)
    CLAIM recommended(target=subject_2) BY role_agent STATUS asserted SOURCE "t4:s52" -> recommended_2 : CLAIM
    UTTER inform(target=recommended_2)
    TERM property_question(property="preference", subject="itinerary_option") -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, acknowledge, role_agent | covered |
| n2 | action | activity, ask | covered |
| n3 | temporal | subject | covered |
| n4 | speech_act | greeting, offer_help, offer, acknowledge, role_user | covered |
| n5 | action | property_question, ask | covered |
| n6 | action | property_question, ask | covered |
| n7 | action | property_question, ask | covered |
| n8 | action | property_question, ask | covered |
| n9 | action | property_question, ask | covered |
| n10 | action | property_question, ask | covered |
| n11 | action | property_question, ask | covered |
| n12 | object | group_size, statement, inform, role_user | covered |
| n13 | object | country::IE, activity, statement, inform, role_user | covered |
| n14 | object | country::IT, activity, statement, inform, role_user | covered |
| n15 | constraint | requirement, user_preference, inform, role_user | covered |
| n16 | constraint | requirement, user_preference, inform, role_user | covered |
| n17 | temporal | duration, unit_week, statement, inform, role_user | covered |
| n18 | action | propose, subject, art_itinerary, country::IT | covered |
| n19 | object | location_spec, subject, art_itinerary, country::IT | covered |
| n20 | object | location_spec, subject, art_itinerary, country::IT | covered |
| n21 | object | location_spec, subject, art_itinerary, country::IT | covered |
| n22 | claim | recommended, role_agent, inform | covered |
| n23 | action | property_question, ask | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s55 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
