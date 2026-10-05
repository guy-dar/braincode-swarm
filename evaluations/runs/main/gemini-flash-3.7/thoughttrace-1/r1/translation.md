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
    TERM offer_help() -> offer_help_2 : TERM
    CLAIM request(target=offer_help_2) BY role_user STATUS asserted SOURCE "t1:s2" -> request_2 : CLAIM
    UTTER ask(target=offer_help_2)
    TERM activity(object=art_story, verb="write") -> activity_2 : TERM
    TERM temporal_context(activity=activity_2) -> temporal_context_2 : TERM
    TERM activity(object=art_plan, purpose=temporal_context_2, verb="organize") -> activity_3 : TERM
    TERM lexical_label(value=genre_label::fanfiction) -> lexical_label_2 : TERM
    TERM subject(kind="story", qualifier=lexical_label_2) -> subject_2 : TERM
    CLAIM enables(condition=activity_3, outcome=subject_2) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
    TERM subject(kind="guide", qualifier=t1.lexical_label_2) -> subject_2 : TERM
    CLAIM request(target=subject_2) BY role_agent STATUS asserted SOURCE "t2:s3" -> request_2 : CLAIM
    UTTER propose(target=subject_2)
    TERM audience_targeting(criteria=[format_plain_text]) -> audience_targeting_2 : TERM
    TERM document_section(items=[audience_targeting_2], title="story_bible") -> document_section_2 : TERM
    TERM character(name="profile") -> character_2 : TERM
    TERM character_trait(property="role", value="character_arc") -> character_trait_2 : TERM
    TERM document_section(items=[character_2, character_trait_2], title="character_profiles") -> document_section_3 : TERM
    TERM location_spec(area="setting") -> location_spec_2 : TERM
    TERM time_horizon(horizon="timeline") -> time_horizon_2 : TERM
    TERM document_section(items=[location_spec_2, time_horizon_2], title="worldbuilding") -> document_section_4 : TERM
    TERM sequence(items=[character_2]) -> sequence_2 : TERM
    TERM document_section(items=[sequence_2], title="narrative_structure") -> document_section_5 : TERM
    TERM performance_tracking(target=art_story) -> performance_tracking_2 : TERM
    TERM document_section(items=[performance_tracking_2], title="plot_tracking") -> document_section_6 : TERM
    CLAIM provides(actor=platform_label::notion, subject=platform_label::obsidian) BY role_agent STATUS reported SOURCE "t2:s61" -> provides_2 : CLAIM
    CLAIM provides(actor=platform_label::google_docs, subject=platform_label::trello) BY role_agent STATUS reported SOURCE "t2:s62" -> provides_3 : CLAIM
    CLAIM provides(actor=platform_label::scrivener, subject=platform_label::notion) BY role_agent STATUS reported SOURCE "t2:s64" -> provides_4 : CLAIM
    TERM activity(object=art_story, verb="pre_writing") -> activity_2 : TERM
    TERM sequence(items=[activity_2]) -> sequence_3 : TERM
    TERM document_section(items=[sequence_3], title="writing_routine") -> document_section_7 : TERM
    TERM subject(kind="fandom", qualifier=art_story) -> subject_3 : TERM
    UTTER ask(target=subject_3)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER acknowledge(target=t2.subject_2)
    UTTER express_interest(target=art_plan)
    CLAIM enables(condition=t2.subject_2, outcome=art_story) BY role_user STATUS asserted SOURCE "t3:s3" -> enables_2 : CLAIM
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM recommended(target=art_plan) BY role_agent STATUS asserted SOURCE "t4:s5" -> recommended_2 : CLAIM
    CLAIM works_best(count=1, purpose="writing", style=style_narrative) BY role_agent STATUS asserted SOURCE "t4:s8" -> works_best_2 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    CLAIM ongoing(target=offer_help_2) BY role_agent STATUS asserted SOURCE "t4:s12" -> ongoing_2 : CLAIM
    UTTER offer(target=offer_help_2)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM subject(kind="writers_block", qualifier=art_story) -> subject_2 : TERM
    UTTER ask(target=subject_2)
    TERM sequence(items=[subject_2]) -> sequence_2 : TERM
    CLAIM request(target=sequence_2) BY role_user STATUS asserted SOURCE "t5:s2" -> request_2 : CLAIM
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    CLAIM designed_to_be(quality="assistance", subject=role_agent) BY role_agent STATUS asserted SOURCE "t6:s1" -> designed_to_be_2 : CLAIM
    UTTER confirm(target=designed_to_be_2)
    TERM dialogue(style="character_psychology") -> dialogue_2 : TERM
    TERM character_trait(property="psychology", value="motivation") -> character_trait_2 : TERM
    TERM sequence(items=[dialogue_2, character_trait_2]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM activity(actor="user", object=art_story, verb="provide_status") -> activity_2 : TERM
    TERM obligation(activity=activity_2, actor=role_user) -> obligation_2 : TERM
    CLAIM provides(actor=role_user, subject=activity_2) BY role_agent STATUS asserted SOURCE "t6:s19" -> provides_2 : CLAIM
    UTTER propose(target=obligation_2)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM time_horizon(horizon="future_assistance") -> time_horizon_2 : TERM
    UTTER express_interest(target=time_horizon_2)
    UTTER acknowledge(target=t6.designed_to_be_2)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_2 : TERM
    TERM time_horizon(horizon="future_session") -> time_horizon_2 : TERM
    UTTER propose(target=well_wishes_2)
    UTTER express_interest(target=time_horizon_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, acknowledge | covered |
| n2 | action | offer_help, request, ask | covered |
| n3 | action | activity, art_story, temporal_context, art_plan | covered |
| n4 | object | art_plan, art_story | covered |
| n5 | object | genre_label::fanfiction, lexical_label | label-preserved |
| n6 | claim | enables, role_user | covered |
| n7 | speech_act | greeting, role_user, acknowledge | covered |
| n8 | action | subject, lexical_label, request, propose | covered |
| n9 | action | audience_targeting, format_plain_text, document_section | covered |
| n10 | action | character, character_trait, document_section | covered |
| n11 | action | location_spec, time_horizon, document_section | covered |
| n12 | action | sequence, character, document_section | covered |
| n13 | action | performance_tracking, art_story, document_section | covered |
| n14 | object | platform_label::notion | label-preserved |
| n15 | object | platform_label::obsidian | label-preserved |
| n16 | object | platform_label::google_docs | label-preserved |
| n17 | object | platform_label::trello | label-preserved |
| n18 | object | platform_label::scrivener | label-preserved |
| n19 | action | activity, art_story, sequence, document_section | covered |
| n20 | speech_act | subject, art_story, ask | covered |
| n21 | speech_act | acknowledge, express_interest, art_plan, enables, role_user, art_story | covered |
| n22 | action | recommended, art_plan, works_best, style_narrative | covered |
| n23 | speech_act | offer_help, ongoing, offer | covered |
| n24 | speech_act | subject, art_story, ask | covered |
| n25 | action | sequence, request, role_user | covered |
| n26 | speech_act | designed_to_be, role_agent, confirm | covered |
| n27 | action | dialogue, character_trait, sequence, propose | covered |
| n28 | action | activity, art_story, obligation, role_user, provides, propose | covered |
| n29 | speech_act | time_horizon, express_interest, acknowledge | covered |
| n30 | speech_act | well_wishes, role_user, time_horizon, propose, express_interest | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s12 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s4 "fanfiction" → genre_label::fanfiction; t2:s61 "Notion" → platform_label::notion; t2:s61 "Obsidian" → platform_label::obsidian; t2:s62 "Google Docs" → platform_label::google_docs; t2:s63 "Trello" → platform_label::trello; t2:s64 "Scrivener" → platform_label::scrivener
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
