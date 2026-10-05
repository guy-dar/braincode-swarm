Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=genre_label::documentary) -> lexical_label_2 : TERM
    TERM subject(kind="The Social Dilemma", qualifier=lexical_label_2) -> subject_2 : TERM
    TERM requirement(property="format", value="group_discussion") -> requirement_2 : TERM
    TERM requirement(property="definitive_answer", value=FALSE) -> requirement_3 : TERM
    UTTER ask(target=subject_2, constraints=[requirement_2, requirement_3])
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    CLAIM focus_of(concept=personal_values, subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> focus_of_2 : CLAIM
    TERM activity(object=art_social_post, verb="use") -> activity_2 : TERM
    TERM activity(object=potential_harms, verb="mitigate") -> activity_3 : TERM
    CLAIM leads_to(cause=activity_2, effect=activity_3) BY role_agent STATUS asserted SOURCE "t2:s1" -> leads_to_2 : CLAIM
    TERM property_question(property="balance", subject=activity_2) -> property_question_2 : TERM
    UTTER respond(target=property_question_2, constraints=[t1.requirement_2, t1.requirement_3])
    TERM activity(actor="individuals", instrument=art_social_post, object=potential_harms, verb="cooperate") -> activity_4 : TERM
    TERM obligation(activity=activity_4, actor=role_adults) -> obligation_2 : TERM
    CLAIM statement(fact=obligation_2) BY role_agent STATUS asserted SOURCE "t2:s4" -> statement_2 : CLAIM
    CLAIM involves(target=activity_4, subject=statement_2) BY role_agent STATUS asserted SOURCE "t2:s4" -> involves_2 : CLAIM
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM property_question(property="theme", subject=t1.subject_2) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM activity(object=potential_harms, verb="detriment") -> activity_5 : TERM
    CLAIM causes(cause=activity_5, effect=leads_to_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> causes_2 : CLAIM
    CLAIM focus_of(concept=potential_harms, subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> focus_of_3 : CLAIM
    TERM activity(actor="tech_companies", object="user_attention", verb="manipulate") -> activity_6 : TERM
    CLAIM enables(condition=activity_6, outcome=focus_of_3) BY role_agent STATUS asserted SOURCE "t4:s2" -> enables_2 : CLAIM
    CLAIM distracts_from(distraction="profit", focus="user_behavior") BY role_agent STATUS asserted SOURCE "t4:s2" -> distracts_from_2 : CLAIM
    TERM self_protection(actor=role_user, domain="privacy") -> self_protection_2 : TERM
    CLAIM focus_of(concept="privacy", subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t4:s3" -> focus_of_4 : CLAIM
    CLAIM unaware(person=role_user, topic="misinformation") BY role_agent STATUS asserted SOURCE "t4:s3" -> unaware_2 : CLAIM
    CLAIM provides(actor=role_colleague, subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t4:s4" -> provides_2 : CLAIM
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM subject(kind="Misinformation and Its Correction: Continued Influence and Successful Debiasing", qualifier="research_paper") -> subject_3 : TERM
    UTTER ask(target=subject_3, constraints=[t1.requirement_2, t1.requirement_3])
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    TERM activity(object="misinformation", verb="correct") -> activity_7 : TERM
    CLAIM focus_of(concept="correction_challenges", subject=t5.subject_3) BY role_agent STATUS asserted SOURCE "t6:s1" -> focus_of_5 : CLAIM
    CLAIM stereotype(target=role_user, trait=beliefs) BY role_agent STATUS asserted SOURCE "t6:s2" -> stereotype_2 : CLAIM
    TERM property_question(property="mitigate_impact", subject=t5.subject_3) -> property_question_4 : TERM
    UTTER propose(target=property_question_4)
    CLAIM role(role_type="individual", subject=role_user) BY role_agent STATUS asserted SOURCE "t6:s3" -> role_2 : CLAIM
    CLAIM controversial(subject=t5.subject_3) BY role_agent STATUS asserted SOURCE "t6:s3" -> controversial_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, subject | covered |
| n2 | action | property_question, ask | covered |
| n3 | object | genre_label::documentary, lexical_label, subject | label-preserved |
| n4 | constraint | requirement | covered |
| n5 | constraint | requirement | covered |
| n6 | claim | focus_of, personal_values, leads_to | covered |
| n7 | speech_act | respond, property_question | covered |
| n8 | object | activity, potential_harms, property_question | covered |
| n9 | action | activity, obligation, statement, involves | covered |
| n10 | speech_act | ask, property_question | covered |
| n11 | claim | focus_of, causes, potential_harms, genre_label::documentary | label-preserved |
| n12 | claim | activity, enables, distracts_from | covered |
| n13 | claim | focus_of, self_protection, unaware | covered |
| n14 | claim | provides, role_colleague | covered |
| n15 | speech_act | ask, subject | covered |
| n16 | object | subject | covered |
| n17 | constraint | requirement | covered |
| n18 | claim | focus_of, activity | covered |
| n19 | speech_act | propose, property_question, stereotype, beliefs | covered |
| n20 | object | role, controversial | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t6:s3 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "documentary" → genre_label::documentary (label only; no sense resolved); t4:s1 "documentary" → genre_label::documentary (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
