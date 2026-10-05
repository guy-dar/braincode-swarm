### S1 | type: add | dimension: constructor | symbol: depicts
- Needs: n4 (t2:s3), n5 (t2:s5), n6 (t2:s8), n9 (t2:s16), n13 (t4:s3), n18 (t4:s16)
- Searches tried: "story adaptation of a work into a setting", "character role in story" → art_story (artifact class), style_narrative (style), `provides`, `inform` (need CLAIM); no relation linking an artifact to its narrative content
- Typed parameters: event: EVENT, content: TERM
- Interpretation: the generated artifact recorded by the event narrates the described content (event TERM, sequence, character); it asserts nothing about the narrated events being real.
- Example: `CLAIM depicts(content=sequence_2, event=art_story_event) BY role_agent STATUS asserted SOURCE "t2:s3" -> depicts_2 : CLAIM`
- Proposed record: `{"symbol": "depicts", "kind": "claim_relation", "signature": "CLAIM depicts(event: EVENT, content: TERM)", "definition": "The artifact produced in the recorded generation event narrates or portrays the described content; the content is fictional description, not asserted fact.", "not": "occurred or provides", "aliases": ["narrates", "portrays"]}`

### S2 | type: refine | dimension: refine-entry | target: art_story
- Needs: n3 (t2:s1), n12 (t4:s1)
- Searches tried: entry art_story → GENERATE target only; rule_recording_signatures has no generation profile for it
- Before: art_story is a GENERATE.target artifact class only
- After: art_story is also an accepted generation-profile identifier for RECORD GENERATE (no attributes required; optional topic/constraints TERMs)
- Justification: spec §11 requires an accepted profile identifier to record a completed generation in TRACE
- Affected uses: none
- Compatibility: additive
- Proposed record: `{"definition": "Narrative story; also an accepted RECORD GENERATE profile identifier.", "signature": "RECORD GENERATE art_story(topic?: STRING / TERM, constraints?: LIST[TERM]) -> EVENT"}`
