Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_u1 : TERM
    UTTER acknowledge(target=greeting_u1)
    TERM subject(kind="fanfiction") -> subject_fanfic : TERM
    TERM activity(object=subject_fanfic, actor=role_user, verb="write") -> activity_write : TERM
    TERM activity(actor=role_user, object=activity_write, verb="stay_organized") -> activity_org : TERM
    TERM temporal_context(activity=activity_org, period="during_story_writing") -> ctx_org : TERM
    TERM activity(actor=role_agent, object=ctx_org, verb="help_plan_and_categorize_best_methods") -> activity_help : TERM
    CLAIM request(target=activity_help) BY role_user STATUS asserted SOURCE "t1:s3" -> request_help : CLAIM
    UTTER inform(target=request_help)
    TERM activity(actor=role_user, verb="realize_own_vision") -> activity_vision : TERM
    CLAIM enables(condition=activity_org, outcome=activity_vision) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_vision : CLAIM
    UTTER inform(target=enables_vision)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greeting_a2 : TERM
    UTTER acknowledge(target=greeting_a2)
    TERM include(item="global_summary") -> inc_summary : TERM
    TERM include(item="main_themes") -> inc_themes : TERM
    TERM include(item="tone_and_atmosphere") -> inc_tone : TERM
    TERM include(item="target_audience") -> inc_audience : TERM
    TERM include(item="estimated_length") -> inc_length : TERM
    TERM document_section(items=[inc_summary, inc_themes, inc_tone, inc_audience, inc_length], title="story_bible") -> sec_bible : TERM
    TERM include(item="name_or_nickname") -> inc_name : TERM
    TERM include(item="role_in_story") -> inc_role : TERM
    TERM include(item="reinterpretation_relative_to_canon") -> inc_reinterp : TERM
    TERM include(item="personality_traits") -> inc_traits : TERM
    TERM include(item="motivations_and_goals") -> inc_motiv : TERM
    TERM include(item="planned_narrative_arc") -> inc_arc : TERM
    TERM include(item="relationships_with_other_characters") -> inc_rel : TERM
    TERM document_section(items=[inc_name, inc_role, inc_reinterp, inc_traits, inc_motiv, inc_arc, inc_rel], title="character_sheets") -> sec_chars : TERM
    TERM include(item="universe_of_origin_faithful_or_divergent") -> inc_universe : TERM
    TERM include(item="main_locations") -> inc_loc : TERM
    TERM include(item="era_and_timeline") -> inc_timeline : TERM
    TERM include(item="points_of_divergence_from_canon") -> inc_diverge : TERM
    TERM include(item="universe_specific_rules") -> inc_rules : TERM
    TERM document_section(items=[inc_universe, inc_loc, inc_timeline, inc_diverge, inc_rules], title="worldbuilding_and_setting") -> sec_world : TERM
    TERM include(item="macro_level_acts_and_major_parts") -> inc_macro : TERM
    TERM include(item="meso_level_narrative_arcs_per_character") -> inc_meso : TERM
    TERM include(item="micro_level_chapter_by_chapter_plan") -> inc_micro : TERM
    TERM include(item="per_chapter_narrative_objective") -> inc_ch_obj : TERM
    TERM include(item="per_chapter_planned_scenes") -> inc_ch_scenes : TERM
    TERM include(item="per_chapter_characters_present") -> inc_ch_chars : TERM
    TERM include(item="per_chapter_plot_progress") -> inc_ch_plot : TERM
    TERM include(item="per_chapter_cliffhanger_or_hook") -> inc_ch_hook : TERM
    TERM document_section(items=[inc_macro, inc_meso, inc_micro, inc_ch_obj, inc_ch_scenes, inc_ch_chars, inc_ch_plot, inc_ch_hook], title="narrative_structure") -> sec_struct : TERM
    TERM include(item="main_plot") -> inc_main_plot : TERM
    TERM include(item="subplots_romance_mystery_secondary_conflict") -> inc_subplots : TERM
    TERM include(item="tracking_table_of_active_plots_per_chapter") -> inc_table : TERM
    TERM include(item="unresolved_narrative_threads") -> inc_threads : TERM
    TERM document_section(items=[inc_main_plot, inc_subplots, inc_table, inc_threads], title="plot_tracking") -> sec_plots : TERM
    TERM activity(instrument=platform_label::notion, verb="hold_story_bible_and_character_sheets") -> act_notion_bible : TERM
    TERM activity(instrument=platform_label::obsidian, verb="hold_story_bible_and_character_sheets") -> act_obsidian_bible : TERM
    TERM activity(instrument=platform_label::google_docs, verb="draft_chapters") -> act_gdocs : TERM
    TERM activity(instrument=platform_label::trello, verb="track_progress") -> act_trello : TERM
    TERM activity(instrument=platform_label::notion, verb="track_progress") -> act_notion_track : TERM
    TERM activity(instrument=platform_label::scrivener, verb="all_in_one_writing") -> act_scrivener : TERM
    TERM activity(instrument=object_label::notebook, verb="quick_notes_and_inspiration") -> act_notebook : TERM
    TERM conjunction(items=[act_notion_bible, act_obsidian_bible, act_gdocs, act_trello, act_notion_track, act_scrivener, act_notebook]) -> conj_tools : TERM
    TERM document_section(items=[conj_tools], title="practical_tools") -> sec_tools : TERM
    TERM activity(object="chapter_sheet", verb="reread") -> act_pre : TERM
    TERM activity(object="inconsistencies_to_fix", verb="note") -> act_during : TERM
    TERM activity(object="plot_tracking", verb="update") -> act_post : TERM
    TERM sequence(items=[act_pre, act_during, act_post]) -> seq_routine : TERM
    TERM document_section(items=[seq_routine], title="writing_routine_before_during_after") -> sec_routine : TERM
    TERM sequence(items=[sec_bible, sec_chars, sec_world, sec_struct, sec_plots, sec_tools, sec_routine]) -> seq_guide : TERM
    UTTER propose(target=seq_guide)
    TERM activity(actor=role_agent, object="personalized_templates", verb="create") -> act_templates : TERM
    UTTER offer(target=act_templates)
    TERM activity(actor=role_user, object="fandom_and_initial_ideas", verb="specify") -> act_specify : TERM
    UTTER ask(target=act_specify)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(actor=role_user, object="agent_guide", verb="thank_and_appreciate") -> act_thanks : TERM
    UTTER acknowledge(target=act_thanks)
    TERM activity(actor=role_user, object="own_ideas", verb="use_well") -> act_use_ideas : TERM
    CLAIM enables(condition=act_thanks, outcome=act_use_ideas) BY role_user STATUS asserted SOURCE "t3:s3" -> enables_ideas : CLAIM
    UTTER inform(target=enables_ideas)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM activity(actor=role_agent, object="user_being_helped", verb="be_glad") -> act_glad : TERM
    UTTER acknowledge(target=act_glad)
    TERM activity(object="user_ideas_into_structure_without_losing_creativity", verb="transform") -> act_transform : TERM
    CLAIM designed_to_be(subject=seq_guide, quality="transforming_ideas_into_structure_preserving_creativity") BY role_agent STATUS asserted SOURCE "t4:s2" -> designed_transform : CLAIM
    UTTER inform(target=designed_transform)
    TERM activity(object="planning_over_writing", verb="avoid_getting_lost") -> act_lost : TERM
    TERM activity(object="idea_dump_section", verb="keep") -> act_dump : TERM
    TERM activity(object="planning", verb="be_flexible") -> act_flex : TERM
    TERM activity(object="own_pace", verb="advance_at") -> act_pace : TERM
    CLAIM recommended(target=act_lost) BY role_agent STATUS asserted SOURCE "t4:s5" -> rec_lost : CLAIM
    CLAIM recommended(target=act_dump) BY role_agent STATUS asserted SOURCE "t4:s7" -> rec_dump : CLAIM
    CLAIM recommended(target=act_flex) BY role_agent STATUS asserted SOURCE "t4:s8" -> rec_flex : CLAIM
    CLAIM recommended(target=act_pace) BY role_agent STATUS asserted SOURCE "t4:s9" -> rec_pace : CLAIM
    UTTER inform(target=rec_lost)
    UTTER inform(target=rec_dump)
    UTTER inform(target=rec_flex)
    UTTER inform(target=rec_pace)
    TERM activity(actor=role_agent, object="character_sheets", verb="help_build") -> act_h1 : TERM
    TERM activity(actor=role_agent, object="chapter_outline", verb="help_develop") -> act_h2 : TERM
    TERM activity(actor=role_agent, object="difficult_scene", verb="help_unblock") -> act_h3 : TERM
    TERM activity(actor=role_agent, object="passage", verb="help_proofread_and_improve") -> act_h4 : TERM
    TERM activity(actor=role_agent, object="scene_tone", verb="help_find") -> act_h5 : TERM
    TERM conjunction(items=[act_h1, act_h2, act_h3, act_h4, act_h5]) -> conj_help : TERM
    UTTER offer(target=conj_help)
    TERM well_wishes(recipient=role_user, sentiment="good_writing_and_eagerness_to_see_creation") -> wishes_t4 : TERM
    UTTER inform(target=wishes_t4)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM activity(actor=role_agent, object="writing_block", verb="help_resolve") -> act_block : TERM
    TERM activity(actor=role_agent, object="ideas_to_continue_planned_story", verb="give") -> act_ideas : TERM
    TERM subject(kind="writers_block", qualifier=act_block) -> subj_block : TERM
    UTTER ask(target=act_block)
    UTTER ask(target=act_ideas)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    TERM activity(actor=role_agent, object="writing_block", verb="help_resolve") -> act_can_help : TERM
    CLAIM request(target=act_can_help) BY role_agent STATUS asserted SOURCE "t6:s1" -> can_help : CLAIM
    UTTER confirm(target=can_help)
    TERM activity(actor=role_agent, object="multiple_narrative_paths_between_point_a_and_b", verb="propose") -> p1 : TERM
    TERM activity(actor=role_agent, object="natural_transition_scenes", verb="suggest") -> p2 : TERM
    TERM activity(actor=role_agent, object="internal_logic_of_characters", verb="help_find") -> p3 : TERM
    TERM activity(actor=role_agent, object="character_psychology_and_likely_reactions", verb="analyze") -> p4 : TERM
    TERM activity(actor=role_agent, object="coherent_character_dialogues_or_reactions", verb="propose") -> p5 : TERM
    TERM activity(actor=role_agent, object="character_narrative_arc", verb="help_unblock") -> p6 : TERM
    TERM activity(actor=role_agent, object="creative_prompts", verb="provide") -> p7 : TERM
    TERM activity(actor=role_agent, object="plot_twists", verb="propose") -> p8 : TERM
    TERM activity(actor=role_agent, object="subplots_to_enrich_story", verb="suggest") -> p9 : TERM
    TERM conjunction(items=[p1, p2, p3, p4, p5, p6, p7, p8, p9]) -> conj_ways : TERM
    UTTER propose(target=conj_ways)
    TERM activity(actor=role_user, object="current_story_status", verb="tell") -> q1 : TERM
    TERM activity(actor=role_user, object="planned_continuation", verb="tell") -> q2 : TERM
    TERM activity(actor=role_user, object="precise_obstacle", verb="tell") -> q3 : TERM
    TERM conjunction(items=[q1, q2, q3]) -> conj_asks : TERM
    UTTER ask(target=conj_asks)
    TERM activity(actor=role_user, object="context", verb="give_more") -> act_ctx : TERM
    CLAIM enables(condition=act_ctx, outcome=conj_ways) BY role_agent STATUS asserted SOURCE "t6:s24" -> enables_precise : CLAIM
    UTTER inform(target=enables_precise)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM activity(actor=role_user, object="agent", verb="thank") -> act_thanks_7 : TERM
    UTTER acknowledge(target=act_thanks_7)
    TERM activity(actor=role_user, object="agent_for_help_if_needed_again", verb="return_to") -> act_return : TERM
    UTTER inform(target=act_return)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM activity(actor=role_agent, object="user_return_any_time", verb="welcome") -> act_welcome : TERM
    UTTER acknowledge(target=act_welcome)
    TERM well_wishes(recipient=role_user, sentiment="good_luck_with_fanfiction_and_enjoyable_writing") -> wishes_t8 : TERM
    UTTER inform(target=wishes_t8)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, acknowledge | covered |
| n2 | action | request, activity | covered |
| n3 | action | activity, temporal_context, request | covered |
| n4 | object | activity, temporal_context | covered |
| n5 | object | subject | covered |
| n6 | claim | enables | covered |
| n7 | speech_act | greeting, acknowledge | covered |
| n8 | action | document_section, sequence, propose | covered |
| n9 | action | document_section, include | covered |
| n10 | action | document_section, include | covered |
| n11 | action | document_section, include | covered |
| n12 | action | document_section, include | covered |
| n13 | action | document_section, include | covered |
| n14 | object | platform_label::notion | label-preserved |
| n15 | object | platform_label::obsidian | label-preserved |
| n16 | object | platform_label::google_docs | label-preserved |
| n17 | object | platform_label::trello | label-preserved |
| n18 | object | platform_label::scrivener | label-preserved |
| n19 | action | sequence, activity | covered |
| n20 | speech_act | ask, offer, activity | covered |
| n21 | speech_act | acknowledge, activity, enables | covered |
| n22 | action | recommended, inform | covered |
| n23 | speech_act | offer, conjunction | covered |
| n24 | speech_act | ask, activity | covered |
| n25 | action | ask, activity | covered |
| n26 | speech_act | confirm, request | covered |
| n27 | action | propose, conjunction, activity | covered |
| n28 | action | ask, conjunction, activity | covered |
| n29 | speech_act | acknowledge, inform, activity | covered |
| n30 | speech_act | well_wishes, acknowledge | covered |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all turns t1–t8 represented; emoji, separators, closing decorations omitted as non-semantic; t8:s3–s7 (list of return occasions) summarized only by "welcome return any time".
- Opaque-text spans: none
- Label-preserved spans: t2:s61–s64 Notion, Obsidian, Google Docs, Trello, Scrivener → platform_label (label only); "Carnet papier" → object_label::notebook
- Missing constructs: no greeting/thank speech act (acknowledge used as nearest); no genre slot accepting genre_label::fanfiction (used subject(kind="fanfiction")); activity verbs and objects are STRING descriptors, not governed vocabulary.
- Unresolved ambiguities: t1:s4 "fanfiction" is a story type/genre; t3 thanks encoded via activity(verb="thank_and_appreciate").
- Check: see host check
