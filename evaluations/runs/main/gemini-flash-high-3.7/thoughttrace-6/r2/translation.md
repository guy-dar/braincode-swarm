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
    TERM activity(object=art_itinerary, purpose=subject_2, verb="plan") -> activity_2 : TERM
    UTTER ask(target=activity_2)
    CLAIM request(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greeting_2 : TERM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
    TERM property_question(property="travel_party", subject=t1.subject_2) -> property_question_2 : TERM
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
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM group_size(count=2, group="couple") -> group_size_2 : TERM
    TERM subject(kind="origin", location=country::IE) -> subject_2 : TERM
    TERM subject(kind="destination", location=country::IT) -> subject_3 : TERM
    TERM requirement(property="budget", value="flexible") -> requirement_2 : TERM
    TERM requirement(property="destination_style", value="off_the_beaten_track") -> requirement_3 : TERM
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    CLAIM user_preference(constraints=requirement_2) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_2 : CLAIM
    CLAIM user_preference(constraints=requirement_3) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_3 : CLAIM
    UTTER respond(target=group_size_2)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM subject(kind=art_itinerary, location=country::IT, qualifier="Abruzzo") -> subject_2 : TERM
    TERM location_spec(area="Abruzzo") -> location_spec_2 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier="Maremma") -> subject_3 : TERM
    TERM location_spec(area="Maremma") -> location_spec_3 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier="Basilicata_Puglia") -> subject_4 : TERM
    TERM location_spec(area="Basilicata") -> location_spec_4 : TERM
    UTTER propose(target=subject_2)
    UTTER propose(target=subject_3)
    UTTER propose(target=subject_4)
    CLAIM recommended(target=subject_2) BY role_agent STATUS inferred SOURCE "t4:s52" -> recommended_2 : CLAIM
    TERM property_question(property="preferred_option", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, offer, role_agent | covered |
| n2 | action | activity, art_itinerary, ask, request | covered |
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
| n15 | constraint | requirement, user_preference | covered |
| n16 | constraint | requirement, user_preference | covered |
| n17 | temporal | duration, unit_week | covered |
| n18 | action | art_itinerary, propose, subject | covered |
| n19 | object | art_itinerary, location_spec, subject | covered |
| n20 | object | art_itinerary, location_spec, subject | covered |
| n21 | object | art_itinerary, location_spec, subject | covered |
| n22 | claim | recommended, role_agent | covered |
| n23 | action | property_question, ask | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s55 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
