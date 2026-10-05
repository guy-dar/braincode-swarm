Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_2 : TERM
    UTTER express_interest(target=greeting_2)
    TERM offer_help() -> offer_help_2 : TERM
    CLAIM request(target=offer_help_2) BY role_user STATUS asserted SOURCE "t1:s2" -> request_2 : CLAIM
    TERM temporal_context(activity=art_story) -> temporal_context_2 : TERM
    TERM activity(purpose=temporal_context_2, verb="plan") -> activity_2 : TERM
    TERM lexical_label(value=genre_label::fanfiction) -> lexical_label_2 : TERM
    CLAIM created_by(creator=role_user, subject=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s4" -> created_by_2 : CLAIM
    CLAIM enables(condition=art_plan, outcome=temporal_context_2) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    UTTER acknowledge(target=greeting_3)
    UTTER propose(target=art_structured_report)
    TERM audience_targeting(criteria=["general"]) -> audience_targeting_2 : TERM
    TERM document_section(items=[audience_targeting_2], title="story_bible") -> document_section_2 : TERM
    TERM character(name="protagonist") -> character_2 : TERM
    TERM character_trait(property="role", value="canon_reinterpretation") -> character_trait_2 : TERM
    TERM document_section(items=[character_2, character_trait_2], title="character_profiles") -> document_section_3 : TERM
    TERM location_spec(area="setting") -> location_spec_2 : TERM
    TERM time_horizon(horizon="timeline") -> time_horizon_2 : TERM
    TERM document_section(items=[location_spec_2, time_horizon_2], title="worldbuilding") -> document_section_4 : TERM
    TERM sequence(items=[document_section_2, document_section_3]) -> sequence_2 : TERM
    TERM document_section(items=[sequence_2], title="narrative_structure") -> document_section_5 : TERM
    TERM performance_tracking(target=art_story) -> performance_tracking_2 : TERM
    TERM document_section(items=[performance_tracking_2], title="plot_tracking") -> document_section_6 : TERM
    CLAIM provides(actor=platform_label::notion, subject=art_structured_report) BY role_agent STATUS asserted SOURCE "t2:s61" -> provides_2 : CLAIM
    CLAIM provides(actor=platform_label::obsidian, subject=art_structured_report) BY role_agent STATUS asserted SOURCE "t2:s61" -> provides_3 : CLAIM
    CLAIM provides(actor=platform_label::google_docs, subject=art_story) BY role_agent STATUS asserted SOURCE "t2:s62" -> provides_4 : CLAIM
    CLAIM provides(actor=platform_label::trello, subject=performance_tracking_2) BY role_agent STATUS asserted SOURCE "t2:s63" -> provides_5 : CLAIM
    CLAIM provides(actor=platform_label::scrivener, subject=art_story) BY role_agent STATUS asserted SOURCE "t2:s64" -> provides_6 : CLAIM
    TERM decision(activity=t1.activity_2) -> decision_2 : TERM
    UTTER ask(target=t1.lexical_label_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER acknowledge(target=t2.provides_2)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM recommended(target=t2.decision_2) BY role_agent STATUS asserted SOURCE "t4:s5" -> recommended_2 : CLAIM
    CLAIM ongoing(target=t2.character_2) BY role_agent STATUS asserted SOURCE "t4:s12" -> ongoing_2 : CLAIM
    UTTER offer(target=ongoing_2)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    UTTER ask(target=t1.offer_help_2)
    TERM time_point(date="future") -> time_point_2 : TERM
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    CLAIM designed_to_be(quality="supportive", subject=role_agent) BY role_agent STATUS asserted SOURCE "t6:s1" -> designed_to_be_2 : CLAIM
    UTTER confirm(target=designed_to_be_2)
    TERM dialogue(style="narrative") -> dialogue_2 : TERM
    UTTER propose(target=dialogue_2)
    TERM obligation(activity=t1.activity_2, actor=role_user) -> obligation_2 : TERM
    UTTER propose(target=obligation_2)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    UTTER acknowledge(target=role_agent)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_2 : TERM
    UTTER express_interest(target=well_wishes_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, express_interest, role_agent | covered |
| n2 | action | offer_help, request | covered |
| n3 | action | temporal_context, art_story | covered |
| n4 | object | activity, art_plan | covered |
| n5 | object | genre_label::fanfiction, lexical_label, created_by | label-preserved |
| n6 | claim | enables, art_plan | covered |
| n7 | speech_act | greeting, acknowledge, role_user | covered |
| n8 | action | propose, art_structured_report | covered |
| n9 | action | audience_targeting, document_section | covered |
| n10 | action | character, character_trait, document_section | covered |
| n11 | action | location_spec, time_horizon, document_section | covered |
| n12 | action | sequence, document_section | covered |
| n13 | action | performance_tracking, document_section, art_story | covered |
| n14 | object | platform_label::notion, provides | label-preserved |
| n15 | object | platform_label::obsidian, provides | label-preserved |
| n16 | object | platform_label::google_docs, provides | label-preserved |
| n17 | object | platform_label::trello, provides | label-preserved |
| n18 | object | platform_label::scrivener, provides | label-preserved |
| n19 | action | decision | covered |
| n20 | speech_act | ask | covered |
| n21 | speech_act | acknowledge | covered |
| n22 | action | recommended | covered |
| n23 | speech_act | ongoing, offer | covered |
| n24 | speech_act | ask | covered |
| n25 | action | time_point | covered |
| n26 | speech_act | designed_to_be, confirm | covered |
| n27 | action | dialogue, propose | covered |
| n28 | action | obligation, propose | covered |
| n29 | speech_act | acknowledge, role_agent | covered |
| n30 | speech_act | well_wishes, express_interest, role_user | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s12 is represented.
- Opaque-text spans: none
- Label-preserved spans: t1:s4 "fanfiction" → genre_label::fanfiction; t2:s61 "Notion" → platform_label::notion; t2:s61 "Obsidian" → platform_label::obsidian; t2:s62 "Google Docs" → platform_label::google_docs; t2:s63 "Trello" → platform_label::trello; t2:s64 "Scrivener" → platform_label::scrivener
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
