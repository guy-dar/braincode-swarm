Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="user", object="text", verb="edit") -> activity_2 : TERM
    TERM obligation(activity=activity_2, actor="user") -> obligation_2 : TERM
    TERM activity(actor="user", location=country::DE, verb="research") -> activity_3 : TERM
    CLAIM ongoing(target=activity_3) BY "user" STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    TERM time_point(date="end_of_August") -> time_point_2 : TERM
    TERM duration(amount=1, unit=unit_year) -> duration_2 : TERM
    TERM subject(kind="visa", location=country::DE, time="end_of_August") -> subject_2 : TERM
    CLAIM has_state(state="valid", subject=subject_2) BY "user" STATUS asserted SOURCE "t1:s1" -> has_state_2 : CLAIM
    TERM activity(actor="university", object="stay", verb="extend") -> activity_4 : TERM
    CLAIM ongoing(target=activity_4) BY "user" STATUS asserted SOURCE "t1:s2" -> ongoing_3 : CLAIM
    TERM activity(actor="user", object="visa_extension", verb="apply") -> activity_5 : TERM
    CLAIM allowed_to_enter(condition="visa_extension", location="Germany", subject="user") BY "user" STATUS asserted SOURCE "t1:s2" -> allowed_to_enter_2 : CLAIM
    TERM activity(actor="user", location=country::IR, time="end_of_August", verb="stay") -> activity_6 : TERM
    CLAIM ongoing(target=activity_6) BY "user" STATUS asserted SOURCE "t1:s3" -> ongoing_4 : CLAIM
    TERM location_spec(city="Tehran") -> location_spec_2 : TERM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_3 : TERM
    TERM property_question(property="can_extend_visa", subject=subject_3) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="policy", qualifier="immigration") -> subject_4 : TERM
    TERM negation(target=subject_4) -> negation_2 : TERM
    CLAIM has_state(state="unknown", subject=negation_2) BY "agent" STATUS asserted SOURCE "t2:s1" -> has_state_3 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_5 : TERM
    TERM activity(actor="user", object=subject_5, verb="contact") -> activity_7 : TERM
    CLAIM recommended(target=activity_7) BY "agent" STATUS asserted SOURCE "t2:s2" -> recommended_2 : CLAIM
    TERM activity(actor="user", object="visa_extension", verb="apply_early") -> activity_8 : TERM
    CLAIM recommended(target=activity_8) BY "agent" STATUS asserted SOURCE "t2:s3" -> recommended_3 : CLAIM
    TERM subject(kind="transition", qualifier="smooth") -> subject_6 : TERM
    CLAIM has_state(state="legal", subject=subject_6) BY "agent" STATUS inferred SOURCE "t2:s3" -> has_state_4 : CLAIM
    LINK supports(conclusion=recommended_3, premise=has_state_4) SOURCE "t2:s3"
    TERM well_wishes(recipient="user", sentiment="good_luck") -> well_wishes_2 : TERM
    UTTER inform(target=recommended_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(actor="user", object="text", verb="edit") -> activity_9 : TERM
    TERM obligation(activity=activity_9, actor="user") -> obligation_3 : TERM
    UTTER propose(target=obligation_3)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM subject(kind="draft", qualifier="edited_email") -> subject_7 : TERM
    CLAIM statement(fact=subject_7) BY "agent" STATUS asserted SOURCE "t4:s1" -> statement_2 : CLAIM
    UTTER respond(target=statement_2)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM substitute(original="text", replacement="rewritten_text") -> substitute_2 : TERM
    UTTER propose(target=substitute_2)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    TERM subject(kind="draft", qualifier="rewritten_email") -> subject_8 : TERM
    CLAIM statement(fact=subject_8) BY "agent" STATUS asserted SOURCE "t6:s1" -> statement_3 : CLAIM
    UTTER respond(target=statement_3)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM substitute(original="text", replacement="rewritten_text_2") -> substitute_3 : TERM
    UTTER propose(target=substitute_3)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM subject(kind="draft", qualifier="rewritten_email_2") -> subject_9 : TERM
    CLAIM statement(fact=subject_9) BY "agent" STATUS asserted SOURCE "t8:s1" -> statement_4 : CLAIM
    UTTER respond(target=statement_4)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | obligation, activity | covered |
| n2 | claim | ongoing, activity | covered |
| n3 | object | country::DE | covered |
| n4 | claim | has_state, subject | covered |
| n5 | temporal | time_point, duration, unit_year | covered |
| n6 | claim | ongoing, activity | covered |
| n7 | action | allowed_to_enter, activity | covered |
| n8 | claim | ongoing, activity | covered |
| n9 | object | country::IR | covered |
| n10 | speech_act | ask, property_question | covered |
| n11 | object | locale_de, location_spec, subject | covered |
| n12 | negation | negation, has_state | covered |
| n13 | speech_act | recommended, activity | covered |
| n14 | speech_act | recommended, activity | covered |
| n15 | reasoning | supports, has_state | covered |
| n16 | speech_act | well_wishes | covered |
| n17 | action | obligation, propose, activity | covered |
| n18 | speech_act | respond, statement | covered |
| n19 | action | propose, substitute | covered |
| n20 | speech_act | respond, statement | covered |
| n21 | action | propose, substitute | covered |
| n22 | speech_act | respond, statement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s4 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
