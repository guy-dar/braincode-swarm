Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greet_a : TERM
    UTTER acknowledge(target=greet_a)
    TERM subject(kind="fanfiction") -> fic : TERM
    TERM activity(verb="write_story", actor=role_user, object=fic) -> write_act : TERM
    TERM temporal_context(activity=write_act) -> while_writing : TERM
    TERM subject(kind="methods_for_staying_organized") -> org_methods : TERM
    TERM activity(verb="plan_and_categorize_best_methods", actor=role_agent, object=org_methods, purpose=while_writing) -> plan_act : TERM
    CLAIM request(target=plan_act) BY role_user STATUS asserted SOURCE "t1:s3" -> request_plan : CLAIM
    UTTER ask(target=plan_act)
    TERM activity(verb="realize_vision", actor=role_user) -> vision_act : TERM
    CLAIM enables(condition=plan_act, outcome=vision_act) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_vision : CLAIM
    UTTER inform(target=enables_vision)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greet_u : TERM
    UTTER acknowledge(target=greet_u)
    UTTER acknowledge(target=t1.request_plan)
    TERM include(item="global_summary") -> inc_summary : TERM
    TERM include(item="main_themes") -> inc_themes : TERM
    TERM include(item="tone_and_mood") -> inc_tone : TERM
    TERM include(item="target_audience") -> inc_audience : TERM
    TERM include(item="estimated_length") -> inc_length : TERM
    TERM document_section(title="story_bible", items=[inc_summary, inc_themes, inc_tone, inc_audience, inc_length]) -> sec_bible : TERM
    TERM include(item="name_or_nickname") -> inc_name : TERM
    TERM include(item="role_in_story") -> inc_role : TERM
    TERM include(item="canon_reinterpretation") -> inc_reinterp : TERM
    TERM include(item="personality_traits") -> inc_traits : TERM
    TERM include(item="motivations_and_goals") -> inc_motiv : TERM
    TERM include(item="planned_narrative_arc") -> inc_arc : TERM
    TERM include(item="relations_with_other_characters") -> inc_rel : TERM
    TERM document_section(title="character_sheets", items=[inc_name, inc_role, inc_reinterp, inc_traits, inc_motiv, inc_arc, inc_rel]) -> sec_chars : TERM
    TERM include(item="universe_of_origin_canon_faithful_or_divergent") -> inc_universe : TERM
    TERM include(item="main_locations") -> inc_places : TERM
    TERM include(item="era_and_timeline") -> inc_timeline : TERM
    TERM include(item="canon_divergence_points") -> inc_diverge : TERM
    TERM include(item="universe_specific_rules") -> inc_rules : TERM
    TERM document_section(title="worldbuilding_and_setting", items=[inc_universe, inc_places, inc_timeline, inc_diverge, inc_rules]) -> sec_world : TERM
    TERM include(item="macro_acts_and_major_parts") -> inc_macro : TERM
    TERM include(item="meso_character_arcs") -> inc_meso : TERM
    TERM include(item="micro_chapter_by_chapter_outline") -> inc_micro : TERM
    TERM include(item="chapter_narrative_goal") -> inc_ch_goal : TERM
    TERM include(item="chapter_planned_scenes") -> inc_ch_scenes : TERM
    TERM include(item="chapter_characters_present") -> inc_ch_chars : TERM
    TERM include(item="chapter_plot_progress") -> inc_ch_plot : TERM
    TERM include(item="chapter_cliffhanger_hook") -> inc_ch_hook : TERM
    TERM sequence(items=[inc_macro, inc_meso, inc_micro]) -> three_levels : TERM
    TERM document_section(title="narrative_structure", items=[three_levels, inc_ch_goal, inc_ch_scenes, inc_ch_chars, inc_ch_plot, inc_ch_hook]) -> sec_struct : TERM
    TERM include(item="main_plot") -> inc_main_plot : TERM
    TERM include(item="subplots_romance_mystery_secondary_conflict") -> inc_subplots : TERM
    TERM include(item="tracking_table_of_active_plots_per_chapter") -> inc_track : TERM
    TERM include(item="unresolved_narrative_threads") -> inc_unresolved : TERM
    TERM document_section(title="plot_tracking", items=[inc_main_plot, inc_subplots, inc_track, inc_unresolved]) -> sec_plots : TERM
    TERM activity(verb="store_story_bible_and_character_sheets", instrument=platform_label::notion) -> tool_notion_bible : TERM
    TERM activity(verb="store_story_bible_and_character_sheets", instrument=platform_label::obsidian) -> tool_obsidian_bible : TERM
    TERM activity(verb="draft_chapters", instrument=platform_label::google_docs) -> tool_gdocs : TERM
    TERM activity(verb="track_progress", instrument=platform_label::trello) -> tool_trello : TERM
    TERM activity(verb="track_progress", instrument=platform_label::notion) -> tool_notion_track : TERM
    TERM activity(verb="all_in_one_writing", instrument=platform_label::scrivener) -> tool_scriv : TERM
    TERM include(item="paper_notebook_for_quick_notes_and_inspiration") -> inc_notebook : TERM
    TERM document_section(title="practical_tools", items=[tool_notion_bible, tool_obsidian_bible, tool_gdocs, tool_trello, tool_notion_track, tool_scriv, inc_notebook]) -> sec_tools : TERM
    TERM include(item="reread_chapter_sheet") -> pre_write : TERM
    TERM include(item="note_inconsistencies_to_fix") -> during_write : TERM
    TERM include(item="update_plot_tracking") -> post_write : TERM
    TERM sequence(items=[pre_write, during_write, post_write]) -> routine_seq : TERM
    TERM document_section(title="writing_routine", items=[routine_seq]) -> sec_routine : TERM
    TERM sequence(items=[sec_bible, sec_chars, sec_world, sec_struct, sec_plots, sec_tools, sec_routine]) -> guide_seq : TERM
    TERM document_section(title="fanfiction_organization_guide", items=[guide_seq]) -> guide_doc : TERM
    UTTER respond(target=guide_doc)
    TERM subject(kind="fandom_of_the_fanfiction_and_initial_ideas") -> fandom_info : TERM
    UTTER ask(target=fandom_info)
    TERM activity(verb="create_customized_templates", actor=role_agent, object=fic) -> templates_act : TERM
    UTTER offer(target=templates_act)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(verb="thank", actor=role_user, object=role_agent) -> thank_a : TERM
    UTTER acknowledge(target=thank_a)
    TERM activity(verb="use_ideas_well", actor=role_user) -> use_ideas : TERM
    CLAIM enables(condition=t2.guide_doc, outcome=use_ideas) BY role_user STATUS asserted SOURCE "t3:s2" -> enables_help : CLAIM
    UTTER inform(target=enables_help)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM activity(verb="avoid_over_planning_write_eventually", actor=role_user) -> adv_balance : TERM
    CLAIM recommended(target=adv_balance) BY role_agent STATUS asserted SOURCE "t4:s5" -> rec_balance : CLAIM
    UTTER inform(target=rec_balance)
    TERM activity(verb="keep_loose_ideas_section", actor=role_user) -> adv_ideas : TERM
    CLAIM recommended(target=adv_ideas) BY role_agent STATUS asserted SOURCE "t4:s7" -> rec_ideas : CLAIM
    UTTER inform(target=rec_ideas)
    TERM activity(verb="be_flexible", actor=role_user) -> adv_flex : TERM
    CLAIM recommended(target=adv_flex) BY role_agent STATUS asserted SOURCE "t4:s8" -> rec_flex : CLAIM
    UTTER inform(target=rec_flex)
    TERM activity(verb="proceed_at_own_pace", actor=role_user) -> adv_pace : TERM
    CLAIM recommended(target=adv_pace) BY role_agent STATUS asserted SOURCE "t4:s9" -> rec_pace : CLAIM
    UTTER inform(target=rec_pace)
    TERM include(item="build_character_sheets") -> sup_chars : TERM
    TERM include(item="develop_chapter_outline") -> sup_outline : TERM
    TERM include(item="unblock_difficult_scene") -> sup_unblock : TERM
    TERM include(item="proofread_and_improve_passage") -> sup_proof : TERM
    TERM include(item="find_right_tone_for_scene") -> sup_tone : TERM
    TERM conjunction(items=[sup_chars, sup_outline, sup_unblock, sup_proof, sup_tone]) -> support_items : TERM
    TERM activity(verb="support_later", actor=role_agent, object=support_items) -> support_act : TERM
    UTTER offer(target=support_act)
    TERM well_wishes(recipient=role_user, sentiment="good_writing") -> wish_t4 : TERM
    UTTER respond(target=wish_t4)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM activity(verb="resolve_writer_block", actor=role_agent, object=fic) -> resolve_act : TERM
    TERM temporal_context(activity=resolve_act) -> if_blocked : TERM
    TERM activity(verb="give_ideas_to_continue_planned_story", actor=role_agent, purpose=if_blocked) -> ideas_act : TERM
    UTTER ask(target=ideas_act)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    CLAIM request(target=t5.ideas_act) BY role_agent STATUS asserted SOURCE "t6:s1" -> can_help : CLAIM
    UTTER confirm(target=can_help)
    TERM include(item="several_narrative_paths_linking_point_a_to_b") -> hp_paths : TERM
    TERM include(item="natural_transition_scenes") -> hp_trans : TERM
    TERM include(item="internal_logic_of_characters") -> hp_logic : TERM
    TERM include(item="character_psychology_analysis") -> hp_psych : TERM
    TERM include(item="coherent_dialogues_or_reactions") -> hp_dial : TERM
    TERM include(item="unblocking_character_arc") -> hp_carc : TERM
    TERM include(item="creative_prompts") -> hp_prompts : TERM
    TERM include(item="plot_twists") -> hp_twists : TERM
    TERM include(item="subplots_to_enrich_story") -> hp_subs : TERM
    TERM conjunction(items=[hp_paths, hp_trans, hp_logic, hp_psych, hp_dial, hp_carc, hp_prompts, hp_twists, hp_subs]) -> help_items : TERM
    TERM activity(verb="help_unblock_writing", actor=role_agent, object=help_items) -> help_act : TERM
    UTTER propose(target=help_act)
    TERM include(item="current_story_status") -> need_status : TERM
    TERM include(item="planned_continuation") -> need_plan : TERM
    TERM include(item="precise_obstacle") -> need_block : TERM
    TERM conjunction(items=[need_status, need_plan, need_block]) -> need_items : TERM
    TERM activity(verb="provide_information", actor=role_user, object=need_items) -> provide_act : TERM
    UTTER ask(target=provide_act)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM activity(verb="thank", actor=role_user, object=role_agent) -> thank_b : TERM
    UTTER acknowledge(target=thank_b)
    TERM activity(verb="return_to_agent_if_help_needed_again", actor=role_user) -> return_act : TERM
    CLAIM request(target=return_act) BY role_user STATUS asserted SOURCE "t7:s2" -> return_intent : CLAIM
    UTTER inform(target=return_intent)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM activity(verb="welcome_return_any_time", actor=role_agent) -> welcome_act : TERM
    UTTER offer(target=welcome_act)
    TERM well_wishes(recipient=role_user, sentiment="good_luck_with_fanfiction_and_enjoyable_writing") -> wish_t8 : TERM
    UTTER respond(target=wish_t8)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | - | greeting, acknowledge, role_agent | covered |
| n2 | - | request, ask, activity | covered |
| n3 | - | activity, temporal_context, subject | covered |
| n4 | - | document_section, sequence | covered |
| n5 | - | subject | covered |
| n6 | - | enables, inform | covered |
| n7 | - | greeting, acknowledge | covered |
| n8 | - | document_section, sequence, respond | covered |
| n9 | - | document_section, include | covered |
| n10 | - | document_section | covered |
| n11 | - | document_section | covered |
| n12 | - | document_section, sequence, include | covered |
| n13 | - | document_section, include | covered |
| n14 | - | activity, platform_label::notion | label-preserved |
| n15 | - | platform_label::obsidian | label-preserved |
| n16 | - | platform_label::google_docs | label-preserved |
| n17 | - | platform_label::trello | label-preserved |
| n18 | - | platform_label::scrivener | label-preserved |
| n19 | - | sequence, include | covered |
| n20 | - | ask, offer, subject | covered |
| n21 | - | acknowledge, enables, inform | covered |
| n22 | - | recommended, inform | covered |
| n23 | - | offer, conjunction, include | covered |
| n24 | - | ask, temporal_context | covered |
| n25 | - | activity, ask | covered |
| n26 | - | confirm, request | covered |
| n27 | - | propose, conjunction, include | covered |
| n28 | - | ask, activity, conjunction | covered |
| n29 | - | acknowledge, request, inform | covered |
| n30 | - | offer, well_wishes, respond | covered |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: turns t1–t8 represented; emoji, separators, markdown decoration omitted; t4:s2, t6:s2–s3, t6:s24, t8:s3–s7 (encouragement, return-topic list) only generally encoded.
- Opaque-text spans: none (include(item="...") snake_case labels are a weak fallback for list items)
- Label-preserved spans: t2:s61–s64 Notion, Obsidian, Google Docs, Trello, Scrivener → platform_label (label only)
- Missing constructs: no greeting/thanks speech act (acknowledge/respond used); fanfiction has no accepted slot for genre_label (subject kind string used)
- Unresolved ambiguities: greetings via acknowledge; thanks encoded as activity(verb="thank"); Notion appears twice in tool table
- Check: rag check reported 0 unknown symbols; n15-n17 label-preserved; n4,n5,n10,n11 flagged declared-only by heuristic
