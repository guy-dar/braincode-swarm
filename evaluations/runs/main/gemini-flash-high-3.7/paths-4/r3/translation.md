Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM requirement(property="format", value=format_plain_text) -> requirement_2 : TERM
    TERM substitute(original="draft_text", replacement="edited_text") -> substitute_2 : TERM
    UTTER propose(target=substitute_2)
    TERM subject(kind="visiting_researcher", location=country::DE, qualifier="Hagen University") -> subject_2 : TERM
    CLAIM role(role_type="visiting_researcher", subject=role_user) BY role_user STATUS asserted SOURCE "t1:s1" -> role_2 : CLAIM
    TERM time_point(date="August", time="end") -> time_point_2 : TERM
    CLAIM allowed_to_enter(condition="visa_valid_until_end_of_August", location=country::DE, subject=role_user) BY role_user STATUS asserted SOURCE "t1:s1" -> allowed_to_enter_2 : CLAIM
    TERM activity(actor="Hagen University", object="stay", verb="extend") -> activity_2 : TERM
    CLAIM ongoing(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> ongoing_2 : CLAIM
    TERM activity(actor="role_user", object="visa_extension", verb="apply") -> activity_3 : TERM
    CLAIM has_goal(goal=activity_3, subject=role_user) BY role_user STATUS asserted SOURCE "t1:s2" -> has_goal_2 : CLAIM
    TERM subject(kind="stay", location=country::IR, time="until_end_of_August") -> subject_3 : TERM
    CLAIM has_state(state="current_and_probable_stay", subject=subject_3) BY role_user STATUS asserted SOURCE "t1:s3" -> has_state_2 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_4 : TERM
    TERM activity(actor="role_user", location=country::IR, object="visa_extension", purpose=subject_4, verb="extend_visa") -> activity_4 : TERM
    UTTER ask(target=activity_4)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="immigration_policy_updates") -> subject_5 : TERM
    TERM negation(target=subject_5) -> negation_2 : TERM
    CLAIM possesses(item=subject_5, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t2:s1" -> possesses_2 : CLAIM
    TERM subject(kind="visa_extension_details", location=country::IR, qualifier=locale_de) -> subject_6 : TERM
    TERM activity(actor="role_user", object="German_Embassy_in_Tehran", purpose=subject_6, verb="contact") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY role_agent STATUS inferred SOURCE "t2:s2" -> recommended_2 : CLAIM
    LINK contrast(first=possesses_2, second=recommended_2) SOURCE "t2:s2"
    UTTER inform(target=recommended_2)
    TERM activity(actor="role_user", object="visa_extension", time="well_before_expiration", verb="apply") -> activity_6 : TERM
    CLAIM recommended(target=activity_6) BY role_agent STATUS inferred SOURCE "t2:s3" -> recommended_3 : CLAIM
    TERM subject(kind="smooth_transition_and_avoid_legal_implications") -> subject_7 : TERM
    CLAIM enables(condition=recommended_3, outcome=subject_7) BY role_agent STATUS inferred SOURCE "t2:s3" -> enables_2 : CLAIM
    LINK supports(conclusion=recommended_3, premise=enables_2) SOURCE "t2:s3"
    UTTER inform(target=recommended_3)
    TERM well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_2 : TERM
    UTTER express_interest(target=well_wishes_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM requirement(property="format", value=format_plain_text) -> requirement_3 : TERM
    TERM substitute(original="draft_text", replacement="edited_text") -> substitute_3 : TERM
    UTTER propose(target=substitute_3)
    CLAIM role(role_type="visiting_researcher", subject=role_user) BY role_user STATUS asserted SOURCE "t3:s1" -> role_3 : CLAIM
    CLAIM allowed_to_enter(condition="visa_valid_until_end_of_August", location=country::DE, subject=role_user) BY role_user STATUS asserted SOURCE "t3:s1" -> allowed_to_enter_3 : CLAIM
    TERM activity(actor="Hagen University", object="stay", verb="extend") -> activity_7 : TERM
    CLAIM ongoing(target=activity_7) BY role_user STATUS asserted SOURCE "t3:s2" -> ongoing_3 : CLAIM
    TERM activity(actor="role_user", object="visa_extension", verb="apply") -> activity_8 : TERM
    CLAIM has_goal(goal=activity_8, subject=role_user) BY role_user STATUS asserted SOURCE "t3:s2" -> has_goal_3 : CLAIM
    TERM subject(kind="stay", location=country::IR, time="until_end_of_August") -> subject_8 : TERM
    CLAIM has_state(state="current_and_probable_stay", subject=subject_8) BY role_user STATUS asserted SOURCE "t3:s3" -> has_state_3 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_9 : TERM
    TERM activity(actor="role_user", location=country::IR, object="visa_extension", purpose=subject_9, verb="extend_visa") -> activity_9 : TERM
    UTTER ask(target=activity_9)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM role(role_type="visiting_researcher", subject=role_user) BY role_agent STATUS reported SOURCE "t4:s1" -> role_4 : CLAIM
    CLAIM allowed_to_enter(condition="visa_expires_end_of_August", location=country::DE, subject=role_user) BY role_agent STATUS reported SOURCE "t4:s1" -> allowed_to_enter_4 : CLAIM
    TERM activity(actor="Hagen University", object="stay", verb="extend") -> activity_10 : TERM
    CLAIM ongoing(target=activity_10) BY role_agent STATUS reported SOURCE "t4:s2" -> ongoing_4 : CLAIM
    TERM activity(actor="role_user", object="visa_extension", verb="apply") -> activity_11 : TERM
    CLAIM has_goal(goal=activity_11, subject=role_user) BY role_agent STATUS reported SOURCE "t4:s2" -> has_goal_4 : CLAIM
    TERM subject(kind="stay", location=country::IR, time="until_end_of_August") -> subject_10 : TERM
    CLAIM has_state(state="residing_in_Iran", subject=subject_10) BY role_agent STATUS reported SOURCE "t4:s3" -> has_state_4 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_11 : TERM
    TERM activity(actor="role_user", location=country::IR, object="visa_extension", purpose=subject_11, verb="extend_visa") -> activity_12 : TERM
    CLAIM statement(fact=activity_12) BY role_agent STATUS reported SOURCE "t4:s4" -> statement_2 : CLAIM
    UTTER respond(target=statement_2)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM requirement(property="format", value=format_plain_text) -> requirement_4 : TERM
    TERM substitute(original="draft_text", replacement="rewritten_text") -> substitute_4 : TERM
    UTTER propose(target=substitute_4)
    CLAIM role(role_type="visiting_researcher", subject=role_user) BY role_user STATUS asserted SOURCE "t5:s1" -> role_5 : CLAIM
    CLAIM allowed_to_enter(condition="visa_valid_until_end_of_August", location=country::DE, subject=role_user) BY role_user STATUS asserted SOURCE "t5:s1" -> allowed_to_enter_5 : CLAIM
    TERM activity(actor="Hagen University", object="stay", verb="extend") -> activity_13 : TERM
    CLAIM ongoing(target=activity_13) BY role_user STATUS asserted SOURCE "t5:s2" -> ongoing_5 : CLAIM
    TERM activity(actor="role_user", object="visa_extension", verb="apply") -> activity_14 : TERM
    CLAIM has_goal(goal=activity_14, subject=role_user) BY role_user STATUS asserted SOURCE "t5:s2" -> has_goal_5 : CLAIM
    TERM subject(kind="stay", location=country::IR, time="until_end_of_August") -> subject_12 : TERM
    CLAIM has_state(state="current_and_probable_stay", subject=subject_12) BY role_user STATUS asserted SOURCE "t5:s3" -> has_state_5 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_13 : TERM
    TERM activity(actor="role_user", location=country::IR, object="visa_extension", purpose=subject_13, verb="extend_visa") -> activity_15 : TERM
    UTTER ask(target=activity_15)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    CLAIM role(role_type="visiting_scholar", subject=role_user) BY role_agent STATUS reported SOURCE "t6:s1" -> role_6 : CLAIM
    CLAIM allowed_to_enter(condition="visa_expires_end_of_August", location=country::DE, subject=role_user) BY role_agent STATUS reported SOURCE "t6:s1" -> allowed_to_enter_6 : CLAIM
    TERM activity(actor="Hagen University", object="stay", verb="grant_extension") -> activity_16 : TERM
    CLAIM ongoing(target=activity_16) BY role_agent STATUS reported SOURCE "t6:s2" -> ongoing_6 : CLAIM
    TERM activity(actor="role_user", object="visa_extension", verb="apply") -> activity_17 : TERM
    CLAIM has_goal(goal=activity_17, subject=role_user) BY role_agent STATUS reported SOURCE "t6:s2" -> has_goal_6 : CLAIM
    TERM subject(kind="stay", location=country::IR, time="until_end_of_August") -> subject_14 : TERM
    CLAIM has_state(state="residing_in_Iran", subject=subject_14) BY role_agent STATUS reported SOURCE "t6:s3" -> has_state_6 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_15 : TERM
    TERM activity(actor="role_user", location=country::IR, object="visa_renewal", purpose=subject_15, verb="renew_visa") -> activity_18 : TERM
    CLAIM statement(fact=activity_18) BY role_agent STATUS reported SOURCE "t6:s3" -> statement_3 : CLAIM
    UTTER respond(target=statement_3)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM requirement(property="format", value=format_plain_text) -> requirement_5 : TERM
    TERM substitute(original="draft_text", replacement="rewritten_text") -> substitute_5 : TERM
    UTTER propose(target=substitute_5)
    CLAIM role(role_type="visiting_scholar", subject=role_user) BY role_user STATUS asserted SOURCE "t7:s1" -> role_7 : CLAIM
    CLAIM allowed_to_enter(condition="visa_valid_until_end_of_August", location=country::DE, subject=role_user) BY role_user STATUS asserted SOURCE "t7:s1" -> allowed_to_enter_7 : CLAIM
    TERM activity(actor="Hagen University", object="stay", verb="extend") -> activity_19 : TERM
    CLAIM ongoing(target=activity_19) BY role_user STATUS asserted SOURCE "t7:s2" -> ongoing_7 : CLAIM
    TERM activity(actor="role_user", object="visa_extension", verb="apply") -> activity_20 : TERM
    CLAIM has_goal(goal=activity_20, subject=role_user) BY role_user STATUS asserted SOURCE "t7:s2" -> has_goal_7 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_16 : TERM
    TERM activity(actor="role_user", location=country::IR, object="visa_extension", purpose=subject_16, verb="extend_visa") -> activity_21 : TERM
    UTTER ask(target=activity_21)
    TERM subject(kind="stay", location=country::IR, time="until_end_of_August") -> subject_17 : TERM
    CLAIM has_state(state="current_and_probable_stay", subject=subject_17) BY role_user STATUS asserted SOURCE "t7:s3" -> has_state_7 : CLAIM
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    CLAIM role(role_type="visiting_scholar", subject=role_user) BY role_agent STATUS reported SOURCE "t8:s1" -> role_8 : CLAIM
    CLAIM allowed_to_enter(condition="visa_expires_end_of_August", location=country::DE, subject=role_user) BY role_agent STATUS reported SOURCE "t8:s1" -> allowed_to_enter_8 : CLAIM
    TERM activity(actor="Hagen University", object="studies_extension", verb="grant_extension") -> activity_22 : TERM
    CLAIM provides(actor="Hagen University", subject="extension") BY role_agent STATUS reported SOURCE "t8:s2" -> provides_2 : CLAIM
    TERM activity(actor="role_user", object="visa_renewal", verb="apply") -> activity_23 : TERM
    CLAIM has_goal(goal=activity_23, subject=role_user) BY role_agent STATUS reported SOURCE "t8:s2" -> has_goal_8 : CLAIM
    TERM subject(kind="stay", location=country::IR, time="until_end_of_August") -> subject_18 : TERM
    CLAIM has_state(state="located_in_Iran", subject=subject_18) BY role_agent STATUS reported SOURCE "t8:s3" -> has_state_8 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_19 : TERM
    TERM activity(actor="role_user", location=country::IR, object="visa_extension", purpose=subject_19, verb="extend_visa") -> activity_24 : TERM
    CLAIM statement(fact=activity_24) BY role_agent STATUS reported SOURCE "t8:s4" -> statement_4 : CLAIM
    UTTER respond(target=statement_4)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | format_plain_text, substitute, propose | covered |
| n2 | claim | role, country::DE, locale_de, ongoing | covered |
| n3 | object | country::DE | covered |
| n4 | claim | allowed_to_enter, time_point, ongoing, has_state | covered |
| n5 | temporal | time_point | covered |
| n6 | claim | ongoing, activity | covered |
| n7 | action | has_goal, activity, allowed_to_enter | covered |
| n8 | claim | has_state, subject, country::IR, ongoing | covered |
| n9 | object | country::IR | covered |
| n10 | speech_act | ask, activity, locale_de | covered |
| n11 | object | locale_de, subject, country::IR | covered |
| n12 | negation | possesses, negation, country::IR | covered |
| n13 | speech_act | recommended, inform, propose, locale_de | covered |
| n14 | speech_act | recommended, inform, ask | covered |
| n15 | reasoning | enables, supports, ongoing | covered |
| n16 | speech_act | well_wishes, express_interest, ask | covered |
| n17 | action | format_plain_text, substitute, propose | covered |
| n18 | speech_act | respond, statement, ask | covered |
| n19 | action | format_plain_text, substitute, propose | covered |
| n20 | speech_act | respond, statement, provides, ask | covered |
| n21 | action | format_plain_text, substitute, propose | covered |
| n22 | speech_act | respond, statement, provides, locale_de | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s4 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: rag check reported 22 of 22 needs covered, 0 unknown symbols
