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
    TERM activity(actor=role_user, purpose=subject_2, verb="plan") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    UTTER offer(target=greeting_3)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
    TERM property_question(property="travelers", subject=role_user) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    TERM property_question(property="origin", subject="trip") -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
    TERM property_question(property="destination", subject="trip") -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
    TERM property_question(property="budget", subject="trip") -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
    TERM property_question(property="vibe", subject="trip") -> property_question_6 : TERM
    UTTER ask(target=property_question_6)
    TERM property_question(property="duration", subject="trip") -> property_question_7 : TERM
    UTTER ask(target=property_question_7)
    TERM property_question(property="constraints", subject="trip") -> property_question_8 : TERM
    UTTER ask(target=property_question_8)
  }
  TURN t3 SPEAKER=USER {
    TERM group_size(count=2, group="couple") -> group_size_2 : TERM
    TERM activity(actor=role_user, location=country::IE, verb="reside") -> activity_3 : TERM
    TERM activity(actor=role_user, location=country::IT, verb="travel") -> activity_4 : TERM
    TERM requirement(property="budget", value="flexible") -> requirement_2 : TERM
    TERM requirement(property="destination_style", value="off_the_beaten_track") -> requirement_3 : TERM
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    CLAIM user_preference(constraints=group_size_2) BY role_user STATUS asserted SOURCE "t3:s1" -> user_preference_2 : CLAIM
    CLAIM user_preference(constraints=activity_4) BY role_user STATUS asserted SOURCE "t3:s2" -> user_preference_3 : CLAIM
    CLAIM user_preference(constraints=requirement_2) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_4 : CLAIM
    CLAIM user_preference(constraints=requirement_3) BY role_user STATUS asserted SOURCE "t3:s3" -> user_preference_5 : CLAIM
    CLAIM user_preference(constraints=duration_2) BY role_user STATUS asserted SOURCE "t3:s4" -> user_preference_6 : CLAIM
    UTTER inform(target=user_preference_2)
    UTTER inform(target=user_preference_3)
    UTTER inform(target=user_preference_4)
    UTTER inform(target=user_preference_5)
    UTTER inform(target=user_preference_6)
  }
  TURN t4 SPEAKER=AGENT {
    TERM location_spec(area="Abruzzo") -> location_spec_2 : TERM
    TERM location_spec(area="Maremma", state="Tuscany") -> location_spec_3 : TERM
    TERM location_spec(area="Basilicata") -> location_spec_4 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier="Option 1: Abruzzo") -> subject_3 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier="Option 2: Maremma") -> subject_4 : TERM
    TERM subject(kind=art_itinerary, location=country::IT, qualifier="Option 3: Basilicata and Puglia") -> subject_5 : TERM
    UTTER propose(target=subject_3)
    UTTER propose(target=subject_4)
    UTTER propose(target=subject_5)
    CLAIM recommended(target=subject_3) BY role_agent STATUS asserted SOURCE "t4:s52" -> recommended_2 : CLAIM
    UTTER inform(target=recommended_2)
    TERM property_question(property="preferred_option", subject="itinerary") -> property_question_9 : TERM
    UTTER ask(target=property_question_9)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, offer | covered |
| n2 | action | activity, art_itinerary, role_user, ask | covered |
| n3 | temporal | subject, unit_week | covered |
| n4 | speech_act | greeting, role_user, offer_help, offer | covered |
| n5 | action | property_question, role_user, ask | covered |
| n6 | action | property_question, ask | covered |
| n7 | action | property_question, ask | covered |
| n8 | action | property_question, ask | covered |
| n9 | action | property_question, ask | covered |
| n10 | action | property_question, ask | covered |
| n11 | action | property_question, ask | covered |
| n12 | object | group_size, role_user, user_preference, inform | covered |
| n13 | object | country::IE, activity | covered |
| n14 | object | country::IT, activity, user_preference, inform | covered |
| n15 | constraint | requirement, user_preference, inform | covered |
| n16 | constraint | requirement, user_preference, inform | covered |
| n17 | temporal | duration, unit_week, user_preference, inform | covered |
| n18 | action | propose, art_itinerary, country::IT, subject | covered |
| n19 | object | location_spec, subject, art_itinerary, propose | covered |
| n20 | object | location_spec, subject, art_itinerary, propose | covered |
| n21 | object | location_spec, subject, art_itinerary, propose | covered |
| n22 | claim | recommended, role_agent, inform, subject | covered |
| n23 | action | property_question, ask | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every turn t1:s1–t4:s55 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
