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
    TERM activity(actor=role_user, purpose=subject_2, verb="plan") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    UTTER offer(target=greeting_3)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
    TERM property_question(property="travelers", subject=t1.subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    TERM property_question(property="origin", subject=t1.subject_2) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
    TERM property_question(property="destination", subject=t1.subject_2) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
    TERM property_question(property="budget", subject=t1.subject_2) -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
    TERM property_question(property="vibe", subject=t1.subject_2) -> property_question_6 : TERM
    UTTER ask(target=property_question_6)
    TERM property_question(property="duration", subject=t1.subject_2) -> property_question_7 : TERM
    UTTER ask(target=property_question_7)
    TERM property_question(property="constraints", subject=t1.subject_2) -> property_question_8 : TERM
    UTTER ask(target=property_question_8)
  }
  TURN t3 SPEAKER=USER {
    TERM group_size(count=2, group=role_adults) -> group_size_2 : TERM
    CLAIM user_preference(constraints=group_size_2) BY role_user STATUS asserted SOURCE "t3:s1" -> user_preference_2 : CLAIM
    TERM subject(kind="origin", location=country::IE) -> subject_3 : TERM
    CLAIM user_preference(constraints=subject_3) BY role_user STATUS asserted SOURCE "t3:s2" -> user_preference_3 : CLAIM
    TERM subject(kind="destination", location=country::IT) -> subject_4 : TERM
    CLAIM user_preference(constraints=subject_4) BY role_user STATUS asserted SOURCE "t3:s2" -> user_preference_4 : CLAIM
    TERM requirement(property="budget_flexible", value=TRUE) -> requirement_2 : TERM
    CLAIM user_preference(constraints=requirement_2) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_5 : CLAIM
    TERM location_spec(area="off_the_beaten_track") -> location_spec_2 : TERM
    CLAIM user_preference(constraints=location_spec_2) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_6 : CLAIM
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    CLAIM user_preference(constraints=duration_2) BY role_user STATUS asserted SOURCE "t3:s4" -> user_preference_7 : CLAIM
  }
  TURN t4 SPEAKER=AGENT {
    TERM subject(kind=art_itinerary, location=country::IT, qualifier="hidden_gems") -> subject_5 : TERM
    UTTER propose(target=subject_5)
    TERM location_spec(area="Abruzzo") -> location_spec_3 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_3) -> subject_6 : TERM
    UTTER propose(target=subject_6)
    TERM location_spec(area="Maremma", state="Tuscany") -> location_spec_4 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_4) -> subject_7 : TERM
    UTTER propose(target=subject_7)
    TERM location_spec(area="Basilicata_and_Puglia") -> location_spec_5 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_5) -> subject_8 : TERM
    UTTER propose(target=subject_8)
    CLAIM recommended(target=subject_6) BY role_agent STATUS inferred SOURCE "t4:s52" -> recommended_2 : CLAIM
    UTTER inform(target=recommended_2)
    TERM property_question(property="preferred_option", subject=subject_5) -> property_question_9 : TERM
    UTTER ask(target=property_question_9)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, offer | covered |
| n2 | action | activity, ask | covered |
| n3 | temporal | subject | covered |
| n4 | speech_act | greeting, role_user, offer_help, offer | covered |
| n5 | action | property_question, ask | covered |
| n6 | action | property_question, ask | covered |
| n7 | action | property_question, ask | covered |
| n8 | action | property_question, ask | covered |
| n9 | action | property_question, ask | covered |
| n10 | action | property_question, ask | covered |
| n11 | action | property_question, ask | covered |
| n12 | object | group_size, role_adults, user_preference | covered |
| n13 | object | subject, country::IE, user_preference | covered |
| n14 | object | subject, country::IT, user_preference | covered |
| n15 | constraint | requirement, user_preference | covered |
| n16 | constraint | location_spec, user_preference | covered |
| n17 | temporal | duration, unit_week, user_preference | covered |
| n18 | action | art_itinerary, subject, country::IT, propose | covered |
| n19 | object | art_itinerary, location_spec, subject, country::IT, propose | covered |
| n20 | object | art_itinerary, location_spec, subject, country::IT, propose | covered |
| n21 | object | art_itinerary, location_spec, subject, country::IT, propose | covered |
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
