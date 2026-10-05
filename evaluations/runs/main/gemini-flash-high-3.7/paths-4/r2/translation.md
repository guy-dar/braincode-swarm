Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="visiting_researcher", location=country::DE, qualifier="Hagen University") -> subject_2 : TERM
    CLAIM role(role_type="visiting_researcher", subject=subject_2) BY "user" STATUS asserted SOURCE "t1:s1" -> role_2 : CLAIM
    TERM time_point(date="August") -> time_point_2 : TERM
    CLAIM attribute_claim(property="valid_until", subject="visa", value=time_point_2) BY "user" STATUS asserted SOURCE "t1:s1" -> attribute_claim_2 : CLAIM
    TERM activity(actor="Hagen University", location=country::DE, verb="extend_stay") -> activity_2 : TERM
    CLAIM provides(actor="Hagen University", subject=activity_2) BY "user" STATUS asserted SOURCE "t1:s2" -> provides_2 : CLAIM
    TERM activity(object="visa_extension", verb="apply") -> activity_3 : TERM
    CLAIM has_goal(goal=activity_3, subject="user") BY "user" STATUS asserted SOURCE "t1:s2" -> has_goal_2 : CLAIM
    TERM subject(kind="stay", location=country::IR, time="August") -> subject_3 : TERM
    CLAIM exists_in(location=country::IR, subject="user") BY "user" STATUS asserted SOURCE "t1:s3" -> exists_in_2 : CLAIM
    TERM location_spec(city="Tehran") -> location_spec_2 : TERM
    TERM activity(location=country::IR, object="German_Embassy", verb="obtain_visa_extension") -> activity_4 : TERM
    TERM property_question(property="feasibility", subject=activity_4) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="immigration_policy_updates", qualifier="latest") -> subject_4 : TERM
    CLAIM possesses(item=subject_4, subject="AI_model", value=FALSE) BY "agent" STATUS asserted SOURCE "t2:s1" -> possesses_2 : CLAIM
    TERM activity(location=country::IR, object="German_Embassy", verb="contact") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY "agent" STATUS asserted SOURCE "t2:s2" -> recommended_2 : CLAIM
    UTTER propose(target=activity_5)
    TERM activity(object="visa_extension", verb="apply_early") -> activity_6 : TERM
    CLAIM recommended(target=activity_6) BY "agent" STATUS asserted SOURCE "t2:s3" -> recommended_3 : CLAIM
    TERM subject(kind="transition", qualifier="smooth") -> subject_5 : TERM
    CLAIM enables(condition=activity_6, outcome=subject_5) BY "agent" STATUS inferred SOURCE "t2:s3" -> enables_2 : CLAIM
    LINK supports(conclusion=recommended_3, premise=enables_2) SOURCE "t2:s3"
    TERM well_wishes(recipient="user", sentiment="good_luck") -> well_wishes_2 : TERM
    UTTER respond(target=well_wishes_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(object="text", verb="edit") -> activity_7 : TERM
    UTTER propose(target=activity_7)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM subject(kind="draft", qualifier="edited_email") -> subject_6 : TERM
    CLAIM provides(actor="agent", subject=subject_6) BY "agent" STATUS asserted SOURCE "t4:s1" -> provides_3 : CLAIM
    UTTER respond(target=subject_6)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM activity(object="text", verb="rewrite") -> activity_8 : TERM
    UTTER propose(target=activity_8)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    TERM subject(kind="draft", qualifier="rewritten_version_1") -> subject_7 : TERM
    CLAIM provides(actor="agent", subject=subject_7) BY "agent" STATUS asserted SOURCE "t6:s1" -> provides_4 : CLAIM
    UTTER respond(target=subject_7)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM activity(object="text", verb="rewrite") -> activity_9 : TERM
    UTTER propose(target=activity_9)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM subject(kind="draft", qualifier="rewritten_version_2") -> subject_8 : TERM
    CLAIM provides(actor="agent", subject=subject_8) BY "agent" STATUS asserted SOURCE "t8:s1" -> provides_5 : CLAIM
    UTTER respond(target=subject_8)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity | covered |
| n2 | claim | role, subject, country::DE | covered |
| n3 | object | country::DE | covered |
| n4 | claim | attribute_claim, time_point | covered |
| n5 | temporal | time_point | covered |
| n6 | claim | provides, activity | covered |
| n7 | action | activity, has_goal | covered |
| n8 | claim | exists_in, country::IR | covered |
| n9 | object | country::IR | covered |
| n10 | speech_act | ask, property_question, activity | covered |
| n11 | object | location_spec, country::IR | covered |
| n12 | negation | possesses | covered |
| n13 | speech_act | propose, recommended, activity | covered |
| n14 | speech_act | recommended, activity | covered |
| n15 | reasoning | supports, enables | covered |
| n16 | speech_act | well_wishes, respond | covered |
| n17 | action | activity, propose | covered |
| n18 | speech_act | provides, respond, subject | covered |
| n19 | action | activity, propose | covered |
| n20 | speech_act | provides, respond, subject | covered |
| n21 | action | activity, propose | covered |
| n22 | speech_act | provides, respond, subject | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s4 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
