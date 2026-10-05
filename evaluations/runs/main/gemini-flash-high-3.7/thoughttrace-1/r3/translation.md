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
    TERM activity(actor=role_agent, verb="assist_planning") -> activity_2 : TERM
    CLAIM request(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> request_2 : CLAIM
    TERM temporal_context(activity="writing_story") -> temporal_context_2 : TERM
    TERM activity(actor=role_user, purpose=temporal_context_2, verb="stay_organized") -> activity_3 : TERM
    TERM subject(kind="story_planning", qualifier="organization_framework") -> subject_2 : TERM
    TERM lexical_label(value=genre_label::fanfiction) -> lexical_label_2 : TERM
    CLAIM role(role_type="fanfiction", subject=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s4" -> role_2 : CLAIM
    CLAIM enables(condition=activity_3, outcome=subject_2) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_2 : CLAIM
    UTTER ask(target=request_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    UTTER respond(target=greeting_3)
    TERM audience_targeting(criteria=["demographics"]) -> audience_targeting_2 : TERM
    TERM document_section(items=[audience_targeting_2], title="story_bible") -> document_section_2 : TERM
    TERM character(name="character_profile") -> character_2 : TERM
    TERM character_trait(property="personality_and_motivation", value="arc_and_traits") -> character_trait_2 : TERM
    CLAIM role(role_type="canon_or_original", subject=character_2) BY role_agent STATUS asserted SOURCE "t2:s17" -> role_3 : CLAIM
    TERM document_section(items=[character_2, character_trait_2], title="character_profiles") -> document_section_3 : TERM
    TERM location_spec(area="main_locations") -> location_spec_2 : TERM
    TERM time_horizon(horizon="timeline_setting") -> time_horizon_2 : TERM
    TERM document_section(items=[location_spec_2, time_horizon_2], title="worldbuilding_and_setting") -> document_section_4 : TERM
    TERM sequence(items=[document_section_2, document_section_3, document_section_4]) -> sequence_2 : TERM
    TERM document_section(items=[sequence_2], title="narrative_structure_three_levels") -> document_section_5 : TERM
    TERM performance_tracking(target=art_story) -> performance_tracking_2 : TERM
    TERM document_section(items=[performance_tracking_2], title="plot_tracking") -> document_section_6 : TERM
    CLAIM provides(actor=platform_label::notion, subject=platform_label::obsidian) BY role_agent STATUS asserted SOURCE "t2:s61" -> provides_2 : CLAIM
    CLAIM provides(actor=platform_label::google_docs, subject="drafting_chapters") BY role_agent STATUS asserted SOURCE "t2:s62" -> provides_3 : CLAIM
    CLAIM provides(actor=platform_label::trello, subject="progress_tracking") BY role_agent STATUS asserted SOURCE "t2:s63" -> provides_4 : CLAIM
    CLAIM provides(actor=platform_label::scrivener, subject="all_in_one_writing") BY role_agent STATUS asserted SOURCE "t2:s64" -> provides_5 : CLAIM
    TERM activity(verb="pre_writing_review") -> activity_4 : TERM
    TERM activity(verb="writing_notes") -> activity_5 : TERM
    TERM activity(verb="post_writing_update") -> activity_6 : TERM
    TERM sequence(items=[activity_4, activity_5, activity_6]) -> sequence_3 : TERM
    TERM document_section(items=[sequence_3], title="writing_routine") -> document_section_7 : TERM
    TERM subject(kind="fandom_and_ideas", qualifier="custom_templates") -> subject_3 : TERM
    UTTER ask(target=subject_3)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM subject(kind="appreciation_and_gratitude") -> subject_4 : TERM
    UTTER acknowledge(target=subject_4)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM decision(activity=t1.activity_3) -> decision_2 : TERM
    CLAIM recommended(target=decision_2) BY role_agent STATUS asserted SOURCE "t4:s5" -> recommended_2 : CLAIM
    CLAIM works_best(count=1, purpose="balance_planning_and_writing", style="flexible") BY role_agent STATUS asserted SOURCE "t4:s8" -> works_best_2 : CLAIM
    CLAIM ongoing(target=art_plan) BY role_agent STATUS asserted SOURCE "t4:s12" -> ongoing_2 : CLAIM
    TERM subject(kind="ongoing_writing_support", qualifier="character_and_chapter_outlines") -> subject_5 : TERM
    UTTER offer(target=subject_5)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM offer_help() -> offer_help_2 : TERM
    TERM subject(kind="resolve_writers_block", qualifier="during_writing") -> subject_6 : TERM
    UTTER ask(target=subject_6)
    TERM activity(actor=role_agent, purpose=art_story, verb="generate_continuation_ideas") -> activity_7 : TERM
    CLAIM request(target=activity_7) BY role_user STATUS asserted SOURCE "t5:s2" -> request_3 : CLAIM
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    CLAIM designed_to_be(quality="unblock_writing", subject=role_agent) BY role_agent STATUS asserted SOURCE "t6:s1" -> designed_to_be_2 : CLAIM
    UTTER confirm(target=designed_to_be_2)
    TERM dialogue(style="character_dialogue") -> dialogue_2 : TERM
    TERM aesthetic(period="contemporary", style="narrative_pathways") -> aesthetic_2 : TERM
    TERM subject(kind="unblocking_solutions", qualifier="transitional_scenes") -> subject_7 : TERM
    UTTER propose(target=subject_7)
    TERM obligation(activity=t5.activity_7, actor=role_user) -> obligation_2 : TERM
    CLAIM provides(actor=role_user, subject="story_status_and_obstacle") BY role_agent STATUS asserted SOURCE "t6:s19" -> provides_6 : CLAIM
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM subject(kind="gratitude_and_future_return") -> subject_8 : TERM
    UTTER acknowledge(target=subject_8)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM time_horizon(horizon="future_assistance") -> time_horizon_3 : TERM
    TERM well_wishes(recipient=role_user, sentiment="good_luck_with_fanfiction") -> well_wishes_2 : TERM
    UTTER propose(target=well_wishes_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, acknowledge | covered |
| n2 | action | activity, request, role_agent, role_user | covered |
| n3 | action | temporal_context, activity, role_user | covered |
| n4 | object | subject | covered |
| n5 | object | lexical_label, genre_label::fanfiction | label-preserved |
| n6 | claim | enables, role_user | covered |
| n7 | speech_act | greeting, role_user, respond | covered |
| n8 | action | document_section, sequence | covered |
| n9 | action | document_section, audience_targeting | covered |
| n10 | action | character, character_trait, role, document_section, role_agent | covered |
| n11 | action | location_spec, time_horizon, document_section | covered |
| n12 | action | sequence, document_section | covered |
| n13 | action | performance_tracking, art_story, document_section | covered |
| n14 | object | provides, platform_label::notion | label-preserved |
| n15 | object | provides, platform_label::obsidian | label-preserved |
| n16 | object | provides, platform_label::google_docs | label-preserved |
| n17 | object | provides, platform_label::trello | label-preserved |
| n18 | object | provides, platform_label::scrivener | label-preserved |
| n19 | action | activity, sequence, document_section | covered |
| n20 | speech_act | subject, ask | covered |
| n21 | speech_act | subject, acknowledge | covered |
| n22 | action | decision, recommended, works_best, role_agent | covered |
| n23 | speech_act | ongoing, art_plan, subject, offer, role_agent | covered |
| n24 | speech_act | offer_help, subject, ask | covered |
| n25 | action | activity, art_story, request, role_agent, role_user | covered |
| n26 | speech_act | designed_to_be, role_agent, confirm | covered |
| n27 | action | dialogue, aesthetic, subject, propose | covered |
| n28 | action | obligation, provides, role_user, role_agent | covered |
| n29 | speech_act | subject, acknowledge | covered |
| n30 | speech_act | time_horizon, well_wishes, role_user, propose | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s12 is represented
- Opaque-text spans: none
- Label-preserved spans:
  - t1:s4 "fanfiction" → genre_label::fanfiction
  - t2:s61 "Notion" → platform_label::notion
  - t2:s61 "Obsidian" → platform_label::obsidian
  - t2:s62 "Google Docs" → platform_label::google_docs
  - t2:s63 "Trello" → platform_label::trello
  - t2:s64 "Scrivener" → platform_label::scrivener
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
