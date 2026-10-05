Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_2 : TERM
    UTTER offer(target=greeting_2)
    TERM subject(kind="holiday", time="summer") -> subject_2 : TERM
    TERM activity(actor=role_agent, object=subject_2, verb="plan") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=greeting_3)
    UTTER offer(target=offer_help_2)
    TERM property_question(property="travelers", subject=role_user) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    TERM property_question(property="origin_location", subject=role_user) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
    TERM property_question(property="destination", subject=role_user) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
    TERM property_question(property="budget_range", subject=role_user) -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
    TERM property_question(property="vibe", subject=role_user) -> property_question_6 : TERM
    UTTER ask(target=property_question_6)
    TERM property_question(property="duration", subject=role_user) -> property_question_7 : TERM
    UTTER ask(target=property_question_7)
    TERM property_question(property="constraints", subject=role_user) -> property_question_8 : TERM
    UTTER ask(target=property_question_8)
  }
  TURN t3 SPEAKER=USER {
    TERM group_size(count=2, group=role_adults) -> group_size_2 : TERM
    CLAIM statement(fact=group_size_2) BY role_user STATUS asserted SOURCE "t3:s1" -> statement_2 : CLAIM
    UTTER inform(target=statement_2)
    TERM subject(kind="origin", location=country::IE) -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY role_user STATUS asserted SOURCE "t3:s2" -> statement_3 : CLAIM
    UTTER inform(target=statement_3)
    TERM subject(kind="destination", location=country::IT) -> subject_4 : TERM
    CLAIM statement(fact=subject_4) BY role_user STATUS asserted SOURCE "t3:s2" -> statement_4 : CLAIM
    UTTER inform(target=statement_4)
    TERM requirement(property="budget", value="flexible") -> requirement_2 : TERM
    CLAIM user_preference(constraints=requirement_2) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_2 : CLAIM
    UTTER inform(target=user_preference_2)
    TERM requirement(property="destinations", value="off_the_beaten_track") -> requirement_3 : TERM
    CLAIM user_preference(constraints=requirement_3) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_3 : CLAIM
    UTTER inform(target=user_preference_3)
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    TERM requirement(property="duration", value=duration_2) -> requirement_4 : TERM
    CLAIM user_preference(constraints=requirement_4) BY role_user STATUS asserted SOURCE "t3:s4" -> user_preference_4 : CLAIM
    UTTER inform(target=user_preference_4)
  }
  TURN t4 SPEAKER=AGENT {
    TERM subject(kind=art_itinerary, location=country::IT, qualifier="hidden_gems") -> subject_5 : TERM
    UTTER propose(target=subject_5)
    TERM location_spec(area="Abruzzo") -> location_spec_2 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_2) -> subject_6 : TERM
    TERM location_spec(area="Maremma", state="Tuscany") -> location_spec_3 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_3) -> subject_7 : TERM
    TERM location_spec(area="Basilicata", state="Puglia") -> location_spec_4 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_4) -> subject_8 : TERM
    CLAIM recommended(target=subject_6) BY role_agent STATUS inferred SOURCE "t4:s52" -> recommended_2 : CLAIM
    UTTER inform(target=recommended_2)
    TERM property_question(property="preferred_option", subject=role_user) -> property_question_9 : TERM
    UTTER ask(target=property_question_9)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, offer, role_agent | covered |
| n2 | action | activity, art_itinerary, ask, propose | covered |
| n3 | temporal | subject, unit_week | covered |
| n4 | speech_act | greeting, offer, offer_help, role_user | covered |
| n5 | action | ask, property_question, role_adults, role_user | covered |
| n6 | action | ask, location_spec, property_question, role_user | covered |
| n7 | action | ask, property_question, role_user, user_preference | covered |
| n8 | action | ask, property_question, role_user | covered |
| n9 | action | ask, property_question, role_user | covered |
| n10 | action | ask, duration, property_question, role_user, unit_week | covered |
| n11 | action | ask, property_question, requirement, role_user, user_preference | covered |
| n12 | object | group_size, role_adults | covered |
| n13 | object | country::IE, subject | covered |
| n14 | object | country::IT, subject | covered |
| n15 | constraint | requirement, user_preference | covered |
| n16 | constraint | art_itinerary, location_spec, requirement, user_preference | covered |
| n17 | temporal | duration, requirement, unit_week, user_preference | covered |
| n18 | action | art_itinerary, country::IT, location_spec, propose, subject | covered |
| n19 | object | art_itinerary, country::IT, location_spec, subject | covered |
| n20 | object | art_itinerary, country::IT, location_spec, subject | covered |
| n21 | object | art_itinerary, country::IT, location_spec, subject | covered |
| n22 | claim | recommended, role_agent | covered |
| n23 | action | ask, property_question, role_user, user_preference | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s55 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
