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
    TERM subject(kind=art_itinerary, time="summer") -> subject_2 : TERM
    TERM activity(object=subject_2, verb="plan") -> activity_2 : TERM
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
    TERM group_size(count=2, group="couple") -> group_size_2 : TERM
    TERM subject(kind="origin", location=country::IE) -> subject_3 : TERM
    TERM subject(kind="destination", location=country::IT) -> subject_4 : TERM
    TERM requirement(property="budget", value="flexible") -> requirement_2 : TERM
    TERM requirement(property="off_the_beaten_track", value=TRUE) -> requirement_3 : TERM
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    CLAIM user_preference(constraints=group_size_2) BY role_user STATUS asserted SOURCE "t3:s1" -> user_preference_2 : CLAIM
    CLAIM user_preference(constraints=subject_3) BY role_user STATUS asserted SOURCE "t3:s2" -> user_preference_3 : CLAIM
    CLAIM user_preference(constraints=subject_4) BY role_user STATUS asserted SOURCE "t3:s2" -> user_preference_4 : CLAIM
    CLAIM user_preference(constraints=requirement_2) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_5 : CLAIM
    CLAIM user_preference(constraints=requirement_3) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_6 : CLAIM
    CLAIM user_preference(constraints=duration_2) BY role_user STATUS asserted SOURCE "t3:s4" -> user_preference_7 : CLAIM
  }
  TURN t4 SPEAKER=AGENT {
    TERM location_spec(state="Abruzzo") -> location_spec_2 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_2) -> subject_5 : TERM
    TERM location_spec(area="Maremma", state="Tuscany") -> location_spec_3 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_3) -> subject_6 : TERM
    TERM location_spec(area="Basilicata and inland Puglia") -> location_spec_4 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier=location_spec_4) -> subject_7 : TERM
    UTTER propose(target=subject_5)
    UTTER propose(target=subject_6)
    UTTER propose(target=subject_7)
    CLAIM recommended(target=subject_5) BY role_agent STATUS asserted SOURCE "t4:s52" -> recommended_2 : CLAIM
    TERM property_question(property="preferred_option", subject=t1.subject_2) -> property_question_9 : TERM
    UTTER ask(target=property_question_9)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, offer, role_agent | covered |
| n2 | action | activity, art_itinerary, ask | covered |
| n3 | temporal | subject | covered |
| n4 | speech_act | greeting, offer_help, offer, role_user | covered |
| n5 | action | property_question, ask | covered |
| n6 | action | property_question, ask | covered |
| n7 | action | property_question, ask | covered |
| n8 | action | property_question, ask | covered |
| n9 | action | property_question, ask | covered |
| n10 | action | property_question, ask | covered |
| n11 | action | property_question, ask | covered |
| n12 | object | group_size | covered |
| n13 | object | country::IE, subject | covered |
| n14 | object | country::IT, subject | covered |
| n15 | constraint | requirement | covered |
| n16 | constraint | requirement | covered |
| n17 | temporal | duration, unit_week | covered |
| n18 | action | propose, art_itinerary | covered |
| n19 | object | art_itinerary, country::IT, location_spec, subject | covered |
| n20 | object | art_itinerary, country::IT, location_spec, subject | covered |
| n21 | object | art_itinerary, country::IT, location_spec, subject | covered |
| n22 | claim | recommended, role_agent | covered |
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
