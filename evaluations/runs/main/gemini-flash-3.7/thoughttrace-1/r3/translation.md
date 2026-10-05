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
    CLAIM request(target=art_plan) BY role_user STATUS asserted SOURCE "t1:s2" -> request_2 : CLAIM
    TERM temporal_context(activity="writing") -> temporal_context_2 : TERM
    TERM lexical_label(value=genre_label::fanfiction) -> lexical_label_2 : TERM
    CLAIM enables(condition=art_plan, outcome=art_story) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    UTTER acknowledge(target=greeting_3)
    CLAIM provides(actor=role_agent, subject=art_structured_report) BY role_agent STATUS asserted SOURCE "t2:s3" -> provides_2 : CLAIM
    TERM audience_targeting(criteria=["general_audience"]) -> audience_targeting_2 : TERM
    TERM document_section(items=[audience_targeting_2], title="Story Bible") -> document_section_2 : TERM
    TERM character(name="character_profile") -> character_2 : TERM
    TERM character_trait(property="personality", value="canon_reinterpretation") -> character_trait_2 : TERM
    CLAIM role(role_type="narrative_role", subject=character_2) BY role_agent STATUS asserted SOURCE "t2:s19" -> role_2 : CLAIM
    TERM document_section(items=[character_2, character_trait_2], title="Character Profiles") -> document_section_3 : TERM
    TERM location_spec(area="worldbuilding") -> location_spec_2 : TERM
    TERM time_horizon(horizon="timeline") -> time_horizon_2 : TERM
    TERM config_setting(option="divergence", section="canon", value="alternate_universe") -> config_setting_2 : TERM
    TERM document_section(items=[config_setting_2, location_spec_2, time_horizon_2], title="Worldbuilding") -> document_section_4 : TERM
    TERM sequence(items=[art_story]) -> sequence_2 : TERM
    TERM document_section(items=[sequence_2], title="Narrative Structure") -> document_section_5 : TERM
    TERM performance_tracking(target=art_story) -> performance_tracking_2 : TERM
    TERM document_section(items=[performance_tracking_2], title="Plot Tracking") -> document_section_6 : TERM
    TERM subject(kind="tool", qualifier=platform_label::notion) -> subject_2 : TERM
    TERM subject(kind="tool", qualifier=platform_label::obsidian) -> subject_3 : TERM
    TERM subject(kind="tool", qualifier=platform_label::google_docs) -> subject_4 : TERM
    TERM subject(kind="tool", qualifier=platform_label::trello) -> subject_5 : TERM
    TERM subject(kind="tool", qualifier=platform_label::scrivener) -> subject_6 : TERM
    TERM decision(activity=sequence_2) -> decision_2 : TERM
    TERM document_section(items=[decision_2], title="Writing Routine") -> document_section_7 : TERM
    TERM subject(kind="fandom") -> subject_7 : TERM
    UTTER ask(target=subject_7)
  }
  TURN t3 SPEAKER=USER {
    UTTER acknowledge(target=t2.provides_2)
    CLAIM recommended(target=t2.provides_2) BY role_user STATUS asserted SOURCE "t3:s2" -> recommended_2 : CLAIM
    UTTER express_interest(target=t2.provides_2)
  }
  TURN t4 SPEAKER=AGENT {
    TERM decision(activity=art_plan) -> decision_3 : TERM
    CLAIM recommended(target=decision_3) BY role_agent STATUS asserted SOURCE "t4:s4" -> recommended_3 : CLAIM
    UTTER inform(target=recommended_3)
    CLAIM ongoing(target=art_character_profile) BY role_agent STATUS asserted SOURCE "t4:s12" -> ongoing_2 : CLAIM
    UTTER offer(target=ongoing_2)
  }
  TURN t5 SPEAKER=USER {
    TERM offer_help() -> offer_help_2 : TERM
    UTTER ask(target=offer_help_2)
    TERM sequence(items=[art_story]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
  }
  TURN t6 SPEAKER=AGENT {
    UTTER confirm(target=t5.offer_help_2)
    TERM dialogue(style="narrative") -> dialogue_2 : TERM
    TERM character_trait(property="psychology", value="character_arc") -> character_trait_3 : TERM
    TERM sequence(items=[dialogue_2, character_trait_3]) -> sequence_4 : TERM
    UTTER propose(target=sequence_4)
    CLAIM provides(actor=role_user, subject=art_story) BY role_agent STATUS asserted SOURCE "t6:s19" -> provides_3 : CLAIM
    UTTER inform(target=provides_3)
  }
  TURN t7 SPEAKER=USER {
    UTTER acknowledge(target=t6.provides_3)
    CLAIM ongoing(target=art_story) BY role_user STATUS asserted SOURCE "t7:s2" -> ongoing_3 : CLAIM
    UTTER inform(target=ongoing_3)
  }
  TURN t8 SPEAKER=AGENT {
    TERM time_horizon(horizon="future") -> time_horizon_3 : TERM
    TERM well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_2 : TERM
    UTTER acknowledge(target=time_horizon_3)
    UTTER acknowledge(target=well_wishes_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, acknowledge, role_agent | covered |
| n2 | action | request, art_plan, role_user | covered |
| n3 | action | temporal_context | covered |
| n4 | object | art_plan, art_story | covered |
| n5 | object | lexical_label, genre_label::fanfiction | label-preserved |
| n6 | claim | enables, art_plan, art_story, role_user | covered |
| n7 | speech_act | greeting, acknowledge, role_user | covered |
| n8 | action | provides, art_structured_report, role_agent | covered |
| n9 | action | audience_targeting, document_section | covered |
| n10 | action | character, character_trait, role, document_section | covered |
| n11 | action | location_spec, time_horizon, config_setting, document_section | covered |
| n12 | action | sequence, document_section, art_story | covered |
| n13 | action | performance_tracking, document_section, art_story | covered |
| n14 | object | subject, platform_label::notion | label-preserved |
| n15 | object | subject, platform_label::obsidian | label-preserved |
| n16 | object | subject, platform_label::google_docs | label-preserved |
| n17 | object | subject, platform_label::trello | label-preserved |
| n18 | object | subject, platform_label::scrivener | label-preserved |
| n19 | action | decision, sequence, document_section | covered |
| n20 | speech_act | subject, ask | covered |
| n21 | speech_act | acknowledge, recommended, express_interest, role_user | covered |
| n22 | action | decision, recommended, art_plan, role_agent, inform | covered |
| n23 | speech_act | ongoing, art_character_profile, role_agent, offer | covered |
| n24 | speech_act | offer_help, ask | covered |
| n25 | action | sequence, art_story, propose | covered |
| n26 | speech_act | confirm | covered |
| n27 | action | dialogue, character_trait, sequence, propose | covered |
| n28 | action | provides, role_user, art_story, role_agent, inform | covered |
| n29 | speech_act | acknowledge, ongoing, art_story, role_user, inform | covered |
| n30 | speech_act | time_horizon, well_wishes, role_user, acknowledge | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s12 is represented.
- Opaque-text spans: none
- Label-preserved spans: t1:s4 "fanfiction" → genre_label::fanfiction (open group); t2:s61 "Notion" → platform_label::notion; t2:s61 "Obsidian" → platform_label::obsidian; t2:s62 "Google Docs" → platform_label::google_docs; t2:s63 "Trello" → platform_label::trello; t2:s64 "Scrivener" → platform_label::scrivener.
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
