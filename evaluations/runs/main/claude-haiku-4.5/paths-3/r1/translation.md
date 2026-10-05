Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="write", object="story") -> write_story : TERM
    TERM subject(kind="Inception", qualifier="film") -> inception_source : TERM
    TERM aesthetic(period="medieval", style="fantasy") -> medieval_fantasy : TERM
    UTTER propose(target=write_story, topic=inception_source, constraints=[medieval_fantasy])
  }

  TURN t2 SPEAKER=AGENT {
    TERM character(name="Johnathon Wyrd") -> johnathon : TERM
    TERM character(name="Lady Elyria") -> elyria : TERM
    TERM character(name="Lord Amandus") -> amandus : TERM
    TERM character(name="Prince Emory") -> emory : TERM
    TERM character(name="Elara") -> elara : TERM
    TERM character(name="Silas") -> silas : TERM
    TERM character(name="Caelum") -> caelum : TERM
    
    TERM subject(kind="Dreamcrafter", location="Aetheroth") -> dreamcrafter_kind : TERM
    TERM activity(verb="extract", object="secrets", location="dreams") -> extraction : TERM
    TERM activity(verb="plant", object="ideas", location="minds") -> inception_activity : TERM
    
    CLAIM has_goal(subject=johnathon, goal=activity(verb="resurrect", object="Lady Elyria")) BY role_agent STATUS observed SOURCE "t2:s5-s7" -> johnathon_goal : CLAIM
    
    TERM activity(verb="hire", actor="Lord Amandus", object=johnathon, purpose=inception_activity) -> hiring : TERM
    TERM activity(verb="abandon", object="claim_to_throne", actor="Prince Emory") -> target_activity : TERM
    CLAIM has_goal(subject=amandus, goal=target_activity) BY role_agent STATUS observed SOURCE "t2:s8-s9" -> amandus_goal : CLAIM
    
    TERM activity(verb="navigate", actor="Elara", location="dreams") -> elara_role : TERM
    TERM activity(verb="protect", actor="Silas", instrument="illusions") -> silas_role : TERM
    TERM activity(verb="steal", actor="Caelum", object="memories") -> caelum_role : TERM
    
    TERM temporal_context(activity=activity(verb="infiltrate", location="dreams"), period="while_facing_defenses") -> infiltration_context : TERM
    CLAIM has_goal(subject=johnathon, goal=activity(verb="complete", object="inception", purpose=activity(verb="save", object="Aetheroth"))) BY role_agent STATUS observed SOURCE "t2:s14-s16" -> final_goal : CLAIM
    
    CLAIM provides(actor=role_agent, subject=art_story) BY role_agent STATUS observed SOURCE "t2:s1-s17" -> story_provided : CLAIM
  }

  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(verb="rewrite", object="story") -> rewrite_story : TERM
    TERM subject(kind="Half-Life 2", qualifier="video_game") -> hl2_source : TERM
    UTTER propose(target=rewrite_story, topic=hl2_source)
  }

  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM character(name="Gordon Freeman") -> gordon : TERM
    TERM character(name="Alyx Vance") -> alyx : TERM
    TERM character(name="Isaac Kleiner") -> kleiner : TERM
    TERM character(name="Wallace Breen") -> breen : TERM
    TERM character(name="Barney Calhoun") -> barney : TERM
    TERM character(name="Dog") -> dog_char : TERM
    TERM character(name="Judith Mossman") -> mossman : TERM
    
    TERM subject(kind="Dreamhacker", location="City_17") -> dreamhacker_kind : TERM
    TERM subject(kind="Combine", qualifier="enemy") -> combine_subject : TERM
    
    CLAIM has_goal(subject=gordon, goal=activity(verb="understand", object="truth_about_Alyx")) BY role_agent STATUS observed SOURCE "t4:s5-s7" -> gordon_goal : CLAIM
    
    CLAIM has_goal(subject=kleiner, goal=activity(verb="extract", object="classified_information", purpose=activity(verb="defeat", object="Combine"))) BY role_agent STATUS observed SOURCE "t4:s8-s9" -> kleiner_goal : CLAIM
    
    TERM activity(verb="help", actor="Barney Calhoun", purpose=activity(verb="navigate", location="dreams")) -> barney_role : TERM
    TERM activity(verb="provide_protection", actor="Dog", location="dreamworld") -> dog_role : TERM
    TERM activity(verb="extract", actor="Judith Mossman", object="memories") -> judith_role : TERM
    
    TERM temporal_context(activity=activity(verb="infiltrate", location="dreams"), period="while_facing_defenses") -> hl2_infiltration : TERM
    
    CLAIM opposes(actor=gordon, subject=combine_subject) BY role_agent STATUS observed SOURCE "t4:s15-t4:s17" -> opposes_combine : CLAIM
    CLAIM enables(condition=activity(verb="complete", object="inception"), outcome=activity(verb="secure", object="humanity_future")) BY role_agent STATUS observed SOURCE "t4:s15-t4:s17" -> inception_enables : CLAIM
    
    CLAIM provides(actor=role_agent, subject=art_story) BY role_agent STATUS observed SOURCE "t4:s1-s17" -> hl2_story_provided : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity(verb="write"), propose | covered |
| n2 | constraint | aesthetic(period="medieval", style="fantasy") | covered |
| n3 | speech_act | provides, propose | covered |
| n4 | object | subject(kind="Dreamcrafter", location="Aetheroth"), activity(verb="extract"), activity(verb="plant") | covered |
| n5 | object | character(name="Johnathon Wyrd"), character(name="Lady Elyria"), has_goal | covered |
| n6 | action | activity(verb="hire"), has_goal(subject=amandus) | covered |
| n7 | object | character(name="Elara"), character(name="Silas"), character(name="Caelum") | covered |
| n8 | action | temporal_context(activity=infiltrate) | covered |
| n9 | action | has_goal(subject=johnathon, goal=complete_inception) | covered |
| n10 | action | activity(verb="rewrite"), propose | covered |
| n11 | constraint | subject(kind="Half-Life 2", qualifier="video_game") | covered |
| n12 | speech_act | provides, propose | covered |
| n13 | object | subject(kind="Dreamhacker", location="City_17"), opposes(actor=gordon, subject=Combine) | covered |
| n14 | object | character(name="Gordon Freeman"), character(name="Alyx Vance"), has_goal | covered |
| n15 | action | has_goal(subject=kleiner), activity(verb="plant") | covered |
| n16 | object | character(name="Barney Calhoun"), character(name="Dog"), character(name="Judith Mossman") | covered |
| n17 | action | temporal_context(activity=infiltrate), has_goal(object="truth_about_Alyx") | covered |
| n18 | action | opposes, enables, has_goal(goal=secure_humanity_future) | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1, t2:s1–s17, t3:s1, t4:s1–s17 is represented through TERMs describing characters, activities, and goals; CLAIMs capturing the plot propositions; and UTTER/provides statements recording the agent's responses.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: run `node /kit/rag.mjs check --translation /output/translation.md` to verify
```

Now let me run the check:
<function_calls>
<invoke name="bash">
<parameter name="command">cd /output && node /kit/rag.mjs check --translation /output/translation.md 2>&1