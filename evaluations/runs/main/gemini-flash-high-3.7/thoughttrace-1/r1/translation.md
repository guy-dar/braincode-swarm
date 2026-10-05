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
    TERM temporal_context(activity=art_story) -> temporal_context_2 : TERM
    TERM activity(actor=role_user, purpose=temporal_context_2, verb="organize") -> activity_2 : TERM
    TERM subject(kind="story_planning", qualifier=art_plan) -> subject_2 : TERM
    TERM lexical_label(value=genre_label::fanfiction) -> lexical_label_2 : TERM
    CLAIM enables(condition=activity_2, outcome=subject_2) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_2 : CLAIM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
    TERM lexical_label(value=genre_label::fanfiction) -> lexical_label_2 : TERM
    TERM document_section(items=[lexical_label_2], title="Guide d'Organisation pour ta Fanfiction") -> document_section_2 : TERM
    TERM audience_targeting(criteria=["general_readers"]) -> audience_targeting_2 : TERM
    TERM document_section(items=[audience_targeting_2], title="Story Bible") -> document_section_3 : TERM
    TERM character(name="character_profile") -> character_2 : TERM
    TERM character_trait(property="personality", value="traits") -> character_trait_2 : TERM
    TERM interpersonal_stance(actor=role_user, stance="character_relations") -> interpersonal_stance_2 : TERM
    TERM document_section(items=[character_2, character_trait_2, interpersonal_stance_2], title="Character Profiles") -> document_section_4 : TERM
    TERM location_spec(area="main_locations") -> location_spec_2 : TERM
    TERM time_horizon(horizon="timeline") -> time_horizon_2 : TERM
    TERM document_section(items=[location_spec_2, time_horizon_2], title="Worldbuilding") -> document_section_5 : TERM
    TERM sequence(items=[document_section_3, document_section_4, document_section_5]) -> sequence_2 : TERM
    TERM document_section(items=[sequence_2], title="Narrative Structure") -> document_section_6 : TERM
    TERM performance_tracking(target="plot_threads") -> performance_tracking_2 : TERM
    TERM document_section(items=[performance_tracking_2], title="Plot Tracking") -> document_section_7 : TERM
    TERM subject(kind="tool", qualifier=platform_label::notion) -> subject_3 : TERM
    TERM subject(kind="tool", qualifier=platform_label::obsidian) -> subject_4 : TERM
    TERM subject(kind="tool", qualifier=platform_label::google_docs) -> subject_5 : TERM
    TERM subject(kind="tool", qualifier=platform_label::trello) -> subject_6 : TERM
    TERM subject(kind="tool", qualifier=platform_label::scrivener) -> subject_7 : TERM
    TERM sequence(items=[document_section_6, document_section_7]) -> sequence_3 : TERM
    TERM document_section(items=[sequence_3], title="Writing Routine") -> document_section_8 : TERM
    TERM subject(kind="fandom_templates", qualifier=lexical_label_2) -> subject_8 : TERM
    UTTER ask(target=subject_8)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER acknowledge(target=t2.document_section_2)
    CLAIM enables(condition=t2.document_section_2, outcome=t1.subject_2) BY role_user STATUS asserted SOURCE "t3:s3" -> enables_3 : CLAIM
    UTTER express_interest(target=t1.subject_2)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM decision(activity=t1.activity_2) -> decision_2 : TERM
    CLAIM recommended(target=decision_2) BY role_agent STATUS asserted SOURCE "t4:s5" -> recommended_2 : CLAIM
    UTTER propose(target=decision_2)
    TERM activity(actor=role_agent, verb="support") -> activity_3 : TERM
    CLAIM ongoing(target=activity_3) BY role_agent STATUS asserted SOURCE "t4:s12" -> ongoing_2 : CLAIM
    UTTER offer(target=activity_3)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM offer_help() -> offer_help_3 : TERM
    UTTER ask(target=offer_help_3)
    TERM activity(actor=role_agent, purpose=art_story, verb="generate_ideas") -> activity_4 : TERM
    UTTER ask(target=activity_4)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    CLAIM provides(actor=role_agent, subject=role_user) BY role_agent STATUS asserted SOURCE "t6:s1" -> provides_2 : CLAIM
    UTTER confirm(target=provides_2)
    TERM dialogue(style="coherent") -> dialogue_2 : TERM
    TERM character(name="character_psychology") -> character_3 : TERM
    TERM activity(actor=role_agent, object=dialogue_2, purpose=art_story, verb="propose_pathways") -> activity_5 : TERM
    UTTER propose(target=activity_5)
    CLAIM provides(actor=role_user, subject=role_agent) BY role_agent STATUS asserted SOURCE "t6:s20" -> provides_3 : CLAIM
    UTTER ask(target=activity_5)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM time_horizon(horizon="future") -> time_horizon_3 : TERM
    TERM activity(actor=role_user, purpose=time_horizon_3, verb="return_for_help") -> activity_6 : TERM
    UTTER acknowledge(target=t6.provides_2)
    UTTER express_interest(target=activity_6)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_2 : TERM
    UTTER acknowledge(target=well_wishes_2)
    TERM lexical_label(value=genre_label::fanfiction) -> lexical_label_2 : TERM
    TERM subject(kind="story_creation", qualifier=lexical_label_2) -> subject_9 : TERM
    UTTER express_interest(target=subject_9)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, acknowledge | covered |
| n2 | action | offer_help, request, role_user, ask | covered |
| n3 | action | temporal_context, art_story, activity, role_user, ask | covered |
| n4 | object | subject, art_plan | covered |
| n5 | object | genre_label::fanfiction, lexical_label | label-preserved |
| n6 | claim | enables, role_user | covered |
| n7 | speech_act | greeting, role_user, acknowledge | covered |
| n8 | action | document_section, lexical_label, genre_label::fanfiction | covered |
| n9 | action | audience_targeting, document_section | covered |
| n10 | action | character, character_trait, interpersonal_stance, document_section | covered |
| n11 | action | location_spec, time_horizon, document_section | covered |
| n12 | action | sequence, document_section | covered |
| n13 | action | performance_tracking, document_section | covered |
| n14 | object | platform_label::notion, subject | label-preserved |
| n15 | object | platform_label::obsidian, subject | label-preserved |
| n16 | object | platform_label::google_docs, subject | label-preserved |
| n17 | object | platform_label::trello, subject | label-preserved |
| n18 | object | platform_label::scrivener, subject | label-preserved |
| n19 | action | sequence, document_section | covered |
| n20 | speech_act | subject, lexical_label, genre_label::fanfiction, ask | covered |
| n21 | speech_act | acknowledge, enables, role_user, express_interest | covered |
| n22 | action | decision, recommended, role_agent, propose | covered |
| n23 | speech_act | activity, role_agent, ongoing, offer | covered |
| n24 | speech_act | offer_help, ask | covered |
| n25 | action | activity, role_agent, art_story, ask | covered |
| n26 | speech_act | provides, role_agent, role_user, confirm | covered |
| n27 | action | dialogue, character, activity, role_agent, art_story, propose | covered |
| n28 | action | provides, role_user, role_agent, ask | covered |
| n29 | speech_act | time_horizon, activity, role_user, acknowledge, express_interest | covered |
| n30 | speech_act | well_wishes, role_user, acknowledge, lexical_label, genre_label::fanfiction, subject, express_interest | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s12 is represented.
- Opaque-text spans: none
- Label-preserved spans: t1:s4 "fanfiction" → genre_label::fanfiction; t2:s61 "Notion" → platform_label::notion; t2:s61 "Obsidian" → platform_label::obsidian; t2:s62 "Google Docs" → platform_label::google_docs; t2:s63 "Trello" → platform_label::trello; t2:s64 "Scrivener" → platform_label::scrivener
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
