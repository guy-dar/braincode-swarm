Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_1 : TERM
    CLAIM request(target=offer_help()) BY role_user STATUS asserted SOURCE "t1:s2" -> request_1 : CLAIM
    TERM art_plan() -> art_plan_1 : TERM
    TERM sequence(items=[include(item="organization_methods"), include(item="story_writing")]) -> sequence_1 : TERM
    CLAIM request(target=sequence_1) BY role_user STATUS asserted SOURCE "t1:s3" -> request_2 : CLAIM
    TERM subject(kind="fanfiction") -> fanfiction_subject : TERM
    CLAIM enables(condition=art_plan_1, outcome="author_vision") BY role_user STATUS asserted SOURCE "t1:s5" -> enables_1 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greeting_2 : TERM
    UTTER acknowledge(target=request_1)
    TERM document_section(title="Story Bible", items=[include(item="summary"), include(item="themes"), include(item="tone"), include(item="audience"), include(item="length")]) -> story_bible : TERM
    TERM document_section(title="Character Profiles", items=[include(item=character(name="protagonist")), include(item="canon_reinterpretation"), include(item="traits"), include(item="motivations"), include(item="arc"), include(item="relationships")]) -> char_profiles : TERM
    TERM document_section(title="Worldbuilding", items=[include(item="universe_setting"), include(item="locations"), include(item="timeline"), include(item="canon_divergences"), include(item="rules")]) -> worldbuilding : TERM
    TERM sequence(items=[include(item="macro_structure"), include(item="character_arcs"), include(item="chapter_plan")]) -> narrative_structure : TERM
    TERM document_section(title="Narrative Structure", items=[narrative_structure]) -> narrative_doc : TERM
    TERM performance_tracking(target="plot_tracking") -> plot_tracking : TERM
    TERM document_section(title="Plot Tracking", items=[include(item="main_plot"), include(item="subplots"), include(item="unresolved_threads")]) -> plot_tracking_doc : TERM
    TERM activity(verb="organize", object="fanfiction", instrument=platform_label::notion) -> notion_use : TERM
    TERM activity(verb="organize", object="fanfiction", instrument=platform_label::obsidian) -> obsidian_use : TERM
    TERM activity(verb="write", object="chapters", instrument=platform_label::google_docs) -> gdocs_use : TERM
    TERM activity(verb="track_progress", object="fanfiction", instrument=platform_label::trello) -> trello_use : TERM
    TERM activity(verb="write", object="fanfiction", instrument=platform_label::scrivener) -> scrivener_use : TERM
    TERM document_section(title="Tools", items=[notion_use, obsidian_use, gdocs_use, trello_use, scrivener_use]) -> tools_section : TERM
    TERM obligation(actor="writer", activity=activity(verb="review", object="chapter_plan")) -> pre_write_routine : TERM
    TERM obligation(actor="writer", activity=activity(verb="write", object="chapter")) -> write_routine : TERM
    TERM obligation(actor="writer", activity=activity(verb="update_tracking", object="plot_tracking")) -> post_write_routine : TERM
    TERM sequence(items=[pre_write_routine, write_routine, post_write_routine]) -> writing_routine : TERM
    TERM document_section(title="Writing Routine", items=[writing_routine]) -> routine_section : TERM
    TERM sequence(items=[story_bible, char_profiles, worldbuilding, narrative_doc, plot_tracking_doc, tools_section, routine_section]) -> comprehensive_guide : TERM
    UTTER propose(target=comprehensive_guide)
    TERM subject(kind="fandom", qualifier="user_project") -> fandom_subject : TERM
    UTTER ask(target=fandom_subject, topic="initial_ideas")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER acknowledge(target=greeting_2)
    CLAIM designed_to_be(subject=art_plan_1, quality="helpful_for_organization") BY role_user STATUS asserted SOURCE "t3:s2" -> designed_claim : CLAIM
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM activity(verb="plan", object="story") -> planning_activity : TERM
    TERM activity(verb="write", object="story") -> writing_activity : TERM
    UTTER propose(target=include(item="do_not_over_plan"))
    TERM interpersonal_stance(actor="character", stance="flexible") -> flexibility_stance : TERM
    UTTER propose(target=flexibility_stance)
    CLAIM works_best(style="balanced", count=1, purpose="creative_satisfaction") BY role_agent STATUS asserted SOURCE "t4:s9" -> works_best_1 : CLAIM
    UTTER offer(target=sequence(items=[include(item="character_sheets"), include(item="chapter_outlines"), include(item="scene_unblocking"), include(item="proofreading")]))
    CLAIM ongoing(target=offer_help()) BY role_agent STATUS asserted SOURCE "t4:s12" -> ongoing_1 : CLAIM
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM activity(verb="help_with_writers_block", actor=role_agent) -> writers_block_help : TERM
    UTTER ask(target=writers_block_help)
    CLAIM request(target="ideas_to_connect_story_points") BY role_user STATUS asserted SOURCE "t5:s2" -> request_3 : CLAIM
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    UTTER acknowledge(target=request_3)
    TERM sequence(items=[include(item="narrative_pathways"), include(item="transitional_scenes"), include(item="character_psychology")]) -> unblock_tools : TERM
    UTTER propose(target=unblock_tools)
    TERM subject(kind="story_status") -> status_subject : TERM
    UTTER ask(target=status_subject)
    TERM subject(kind="intended_progression") -> progression_subject : TERM
    UTTER ask(target=progression_subject)
    TERM subject(kind="specific_obstacle") -> obstacle_subject : TERM
    UTTER ask(target=obstacle_subject)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    UTTER acknowledge(target=ongoing_1)
    CLAIM ongoing(target=request_1) BY role_user STATUS asserted SOURCE "t7:s2" -> ongoing_2 : CLAIM
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM well_wishes(recipient=role_user, sentiment="good_luck_with_fanfiction") -> wishes_1 : TERM
    UTTER offer(target=wishes_1)
    CLAIM ongoing(target=offer_help()) BY role_agent STATUS asserted SOURCE "t8:s2" -> ongoing_3 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting | covered |
| n2 | action | request, offer_help | covered |
| n3 | action | sequence, include | covered |
| n4 | object | art_plan, document_section | covered |
| n5 | object | subject, fanfiction_subject | label-preserved |
| n6 | claim | enables | covered |
| n7 | speech_act | greeting, acknowledge, offer | covered |
| n8 | action | propose, document_section | covered |
| n9 | action | document_section, include, story_bible | covered |
| n10 | action | character, document_section, char_profiles | covered |
| n11 | action | document_section, activity, worldbuilding | covered |
| n12 | action | sequence, narrative_structure, narrative_doc | covered |
| n13 | action | performance_tracking, plot_tracking_doc | covered |
| n14 | object | activity, platform_label::notion | covered |
| n15 | object | activity, platform_label::obsidian | covered |
| n16 | object | platform_label::google_docs | label-preserved |
| n17 | object | platform_label::trello | label-preserved |
| n18 | object | activity, platform_label::scrivener | covered |
| n19 | action | obligation, sequence, writing_routine | covered |
| n20 | speech_act | ask | covered |
| n21 | speech_act | acknowledge | covered |
| n22 | action | propose, works_best | covered |
| n23 | speech_act | offer, ongoing | covered |
| n24 | speech_act | ask | covered |
| n25 | action | activity, unblock_tools | covered |
| n26 | speech_act | acknowledge | covered |
| n27 | action | sequence, include, unblock_tools | covered |
| n28 | action | ask | covered |
| n29 | speech_act | acknowledge, ongoing | covered |
| n30 | speech_act | well_wishes, offer | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: Every turn t1–t8 and sentence t1:s1–t8:s12 is represented with semantic content preserved
- Opaque-text spans: none
- Label-preserved spans: n16 (Google Docs as platform_label only), n17 (Trello as platform_label only)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: All 30 needs covered; all glossary symbols used are documented in the retrieval

