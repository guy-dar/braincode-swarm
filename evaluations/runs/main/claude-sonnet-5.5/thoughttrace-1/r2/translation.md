Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_2 : TERM
    UTTER respond(recipient=role_agent, target=greeting_2)
    TERM activity(actor=role_agent, verb="assist_with_planning_task") -> activity_2 : TERM
    CLAIM request(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s2" -> request_2 : CLAIM
    UTTER ask(recipient=role_agent, target=activity_2)
    TERM activity(actor=role_user, object="story", verb="write") -> activity_3 : TERM
    TERM temporal_context(activity=activity_3) -> temporal_context_2 : TERM
    TERM subject(kind="best_methods_to_stay_organized", qualifier=temporal_context_2) -> subject_2 : TERM
    TERM activity(actor=role_agent, object=subject_2, verb="categorize") -> activity_4 : TERM
    UTTER ask(recipient=role_agent, target=activity_4)
    TERM subject(kind="story_planning_and_organization_framework") -> subject_3 : TERM
    TERM subject(kind="fanfiction") -> subject_4 : TERM
    TERM activity(actor=role_user, object=subject_4, verb="write") -> activity_5 : TERM
    CLAIM request(target=activity_5) BY role_user STATUS asserted SOURCE "t1:s4" -> request_3 : CLAIM
    TERM activity(actor=role_user, object=subject_3, verb="be_organized") -> activity_6 : TERM
    TERM activity(actor=role_user, verb="realize_own_vision") -> activity_7 : TERM
    CLAIM enables(condition=activity_6, outcome=activity_7) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    UTTER respond(recipient=role_user, target=greeting_3)
    CLAIM request(target=activity_2) BY role_agent STATUS reported SOURCE "t2:s3" -> request_4 : CLAIM
    UTTER confirm(recipient=role_user, target=request_4)
    TERM subject(kind="global_summary") -> s_summary : TERM
    TERM subject(kind="main_themes") -> s_themes : TERM
    TERM subject(kind="tone_and_atmosphere") -> s_tone : TERM
    TERM subject(kind="target_audience") -> s_audience : TERM
    TERM subject(kind="estimated_length") -> s_length : TERM
    TERM document_section(items=[s_summary, s_themes, s_tone, s_audience, s_length], title="story_bible") -> sec_bible : TERM
    TERM subject(kind="name_or_nickname") -> s_name : TERM
    TERM subject(kind="role_in_story") -> s_role : TERM
    TERM subject(kind="reinterpretation_relative_to_canon") -> s_reinterp : TERM
    TERM subject(kind="personality_traits") -> s_traits : TERM
    TERM subject(kind="motivations_and_goals") -> s_motiv : TERM
    TERM subject(kind="planned_narrative_arc") -> s_arc : TERM
    TERM subject(kind="relations_with_other_characters") -> s_rel : TERM
    TERM document_section(items=[s_name, s_role, s_reinterp, s_traits, s_motiv, s_arc, s_rel], title="character_sheets") -> sec_chars : TERM
    TERM subject(kind="original_universe_canon_or_divergent") -> s_universe : TERM
    TERM subject(kind="main_locations") -> s_places : TERM
    TERM subject(kind="era_and_timeline") -> s_timeline : TERM
    TERM subject(kind="divergence_points_from_canon") -> s_diverge : TERM
    TERM subject(kind="universe_specific_rules") -> s_rules : TERM
    TERM document_section(items=[s_universe, s_places, s_timeline, s_diverge, s_rules], title="worldbuilding_and_setting") -> sec_world : TERM
    TERM subject(kind="macro_acts_or_major_parts") -> s_macro : TERM
    TERM subject(kind="meso_narrative_arcs_per_character") -> s_meso : TERM
    TERM subject(kind="micro_chapter_by_chapter_outline") -> s_micro : TERM
    TERM sequence(items=[s_macro, s_meso, s_micro]) -> sequence_2 : TERM
    TERM subject(kind="chapter_narrative_goal") -> c_goal : TERM
    TERM subject(kind="planned_scenes") -> c_scenes : TERM
    TERM subject(kind="characters_present") -> c_chars : TERM
    TERM subject(kind="plot_progress") -> c_plot : TERM
    TERM subject(kind="cliffhanger_or_hook") -> c_hook : TERM
    TERM document_section(items=[sequence_2, c_goal, c_scenes, c_chars, c_plot, c_hook], title="narrative_structure") -> sec_struct : TERM
    TERM subject(kind="main_plot") -> p_main : TERM
    TERM subject(kind="subplots") -> p_sub : TERM
    TERM subject(kind="active_plots_per_chapter_tracking_table") -> p_table : TERM
    TERM subject(kind="unresolved_narrative_threads") -> p_open : TERM
    TERM performance_tracking(target=p_main) -> track_main : TERM
    TERM document_section(items=[track_main, p_sub, p_table, p_open], title="plot_tracking") -> sec_plots : TERM
    TERM activity(instrument=platform_label::notion, verb="store_complete_bible_and_sheets") -> tool_1 : TERM
    TERM activity(instrument=platform_label::obsidian, verb="store_complete_bible_and_sheets") -> tool_2 : TERM
    TERM activity(instrument=platform_label::google_docs, verb="draft_chapters") -> tool_3 : TERM
    TERM activity(instrument=platform_label::trello, verb="track_progress") -> tool_4 : TERM
    TERM activity(instrument=platform_label::notion, verb="track_progress") -> tool_5 : TERM
    TERM activity(instrument=platform_label::scrivener, verb="all_in_one_writing") -> tool_6 : TERM
    TERM activity(instrument=object_label::notebook, verb="quick_notes_and_inspiration") -> tool_7 : TERM
    TERM document_section(items=[tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7], title="practical_tools") -> sec_tools : TERM
    TERM activity(verb="reread_chapter_sheet") -> r_pre : TERM
    TERM activity(verb="note_inconsistencies_to_fix") -> r_during : TERM
    TERM activity(verb="update_plot_tracking") -> r_post : TERM
    TERM sequence(items=[r_pre, r_during, r_post]) -> sequence_3 : TERM
    TERM document_section(items=[sequence_3], title="writing_routine") -> sec_routine : TERM
    TERM sequence(items=[sec_bible, sec_chars, sec_world, sec_struct, sec_plots, sec_tools, sec_routine]) -> sequence_4 : TERM
    UTTER propose(recipient=role_user, target=sequence_4)
    TERM activity(actor=role_agent, object="personalized_templates", verb="create") -> activity_8 : TERM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(recipient=role_user, target=offer_help_2)
    TERM subject(kind="fandom_and_initial_ideas") -> subject_5 : TERM
    TERM activity(actor=role_user, object=subject_5, verb="provide", purpose=activity_8) -> activity_9 : TERM
    UTTER ask(recipient=role_user, target=activity_9)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(actor=role_user, object="guide", verb="thank_and_appreciate") -> activity_10 : TERM
    UTTER acknowledge(recipient=role_agent, target=activity_10)
    CLAIM enables(condition=sequence_4, outcome=activity_7) BY role_user STATUS asserted SOURCE "t3:s3" -> enables_3 : CLAIM
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM activity(actor=role_agent, verb="advise_on_planning_vs_writing_flexibility_and_pace") -> activity_11 : TERM
    UTTER propose(recipient=role_user, target=activity_11)
    TERM offer_help() -> offer_help_3 : TERM
    UTTER offer(recipient=role_user, target=offer_help_3)
    TERM character(name="character_sheets") -> character_2 : TERM
    TERM subject(kind="chapter_outline_development") -> subject_6 : TERM
    TERM subject(kind="unblocking_difficult_scene") -> subject_7 : TERM
    TERM subject(kind="proofreading_and_improving_passage") -> subject_8 : TERM
    TERM subject(kind="finding_right_tone_for_scene") -> subject_9 : TERM
    TERM conjunction(items=[character_2, subject_6, subject_7, subject_8, subject_9]) -> conjunction_2 : TERM
    CLAIM ongoing(target=conjunction_2) BY role_agent STATUS asserted SOURCE "t4:s12" -> ongoing_2 : CLAIM
    TERM well_wishes(recipient=role_user) -> well_wishes_2 : TERM
    UTTER acknowledge(recipient=role_user, target=well_wishes_2)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM subject(kind="writer_block_during_writing") -> subject_10 : TERM
    TERM activity(actor=role_agent, object=subject_10, verb="help_resolve") -> activity_12 : TERM
    UTTER ask(recipient=role_agent, target=activity_12)
    TERM activity(actor=role_agent, object="ideas_to_continue_planned_story", verb="generate") -> activity_13 : TERM
    UTTER ask(recipient=role_agent, target=activity_13)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    CLAIM request(target=activity_12) BY role_agent STATUS reported SOURCE "t6:s1" -> request_5 : CLAIM
    UTTER confirm(recipient=role_user, target=request_5)
    TERM subject(kind="narrative_pathways_from_point_a_to_b") -> h_1 : TERM
    TERM subject(kind="natural_transition_scenes") -> h_2 : TERM
    TERM subject(kind="characters_internal_logic") -> h_3 : TERM
    TERM subject(kind="character_psychology_analysis") -> h_4 : TERM
    TERM dialogue(style="coherent_with_character") -> dialogue_2 : TERM
    TERM subject(kind="unblocking_character_arc") -> h_5 : TERM
    TERM subject(kind="creative_prompts") -> h_6 : TERM
    TERM subject(kind="plot_twists") -> h_7 : TERM
    TERM subject(kind="subplots_to_enrich_story") -> h_8 : TERM
    TERM conjunction(items=[h_1, h_2, h_3, h_4, dialogue_2, h_5, h_6, h_7, h_8]) -> conjunction_3 : TERM
    UTTER propose(recipient=role_user, target=conjunction_3)
    TERM subject(kind="current_story_status") -> n_1 : TERM
    TERM subject(kind="planned_continuation") -> n_2 : TERM
    TERM subject(kind="specific_obstacle") -> n_3 : TERM
    TERM conjunction(items=[n_1, n_2, n_3]) -> conjunction_4 : TERM
    TERM activity(actor=role_user, object=conjunction_4, verb="provide") -> activity_14 : TERM
    UTTER ask(recipient=role_user, target=activity_14)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM activity(actor=role_user, object="help", verb="thank_for") -> activity_15 : TERM
    UTTER acknowledge(recipient=role_agent, target=activity_15)
    TERM activity(actor=role_user, verb="return_to_agent_if_help_needed_again") -> activity_16 : TERM
    UTTER inform(recipient=role_agent, target=enables_2)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM activity(actor=role_user, verb="return_at_any_time") -> activity_17 : TERM
    UTTER acknowledge(recipient=role_user, target=activity_17)
    TERM well_wishes(recipient=role_user, sentiment="good_luck_with_fanfiction") -> well_wishes_3 : TERM
    UTTER acknowledge(recipient=role_user, target=well_wishes_3)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, respond | covered |
| n2 | action | activity, request, ask | covered |
| n3 | action | activity, subject, temporal_context, ask | covered |
| n4 | object | subject | covered |
| n5 | object | subject | covered |
| n6 | claim | enables | covered |
| n7 | speech_act | greeting, respond, request, confirm | covered |
| n8 | action | sequence, document_section, propose | covered |
| n9 | action | document_section, subject | covered |
| n10 | action | document_section, subject | covered |
| n11 | action | document_section, subject | covered |
| n12 | action | sequence, document_section | covered |
| n13 | action | performance_tracking, document_section | covered |
| n14 | object | activity, platform_label::notion | label-preserved |
| n15 | object | activity, platform_label::obsidian | label-preserved |
| n16 | object | activity, platform_label::google_docs | label-preserved |
| n17 | object | activity, platform_label::trello | label-preserved |
| n18 | object | activity, platform_label::scrivener | label-preserved |
| n19 | action | sequence, activity | covered |
| n20 | speech_act | ask, activity, offer_help | covered |
| n21 | speech_act | acknowledge, activity | covered |
| n22 | action | propose, activity | covered |
| n23 | speech_act | offer, offer_help, conjunction, ongoing, character | covered |
| n24 | speech_act | ask, activity | covered |
| n25 | action | ask, activity | covered |
| n26 | speech_act | confirm, request | covered |
| n27 | action | propose, conjunction, dialogue | covered |
| n28 | action | ask, activity, conjunction | covered |
| n29 | speech_act | acknowledge, activity | covered |
| n30 | speech_act | well_wishes, acknowledge | covered |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all turns t1–t8 represented in condensed structured form; markdown decoration, emoji and separators omitted; t4:s2 and t6:s2–s3 (encouragement) and t8:s3–s7 (list of return topics) only partly represented.
- Opaque-text spans: none (descriptive strings are snake_case kind labels in subject/activity, not content fallback)
- Label-preserved spans: t2:s61–s64 Notion, Obsidian, Google Docs, Trello, Scrivener → platform_label (label only); fanfiction has no accepting group slot, written as subject(kind="fanfiction")
- Missing constructs: none blocking; verbs/kinds are free STRING descriptors
- Unresolved ambiguities: t7:s2 intention to return encoded as activity_16 term (unused in an utterance); t1:s5 "cela" interpreted as the organization framework
- Check: `rag check` reported 0 unknown symbols; n4 and n11 flagged only as heuristic non-matches (covered by subject/document_section terms); n14–n18 are label-preserved platform_label values
