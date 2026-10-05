### S1 | type: add | dimension: member-family | symbol: tone_funny
- Needs: n3 (t1:s1), n4 (t1:s1), n5 (t1:s1)
- Searches tried: "funny tone", "flirty tone", "intellectual tone" → tone_silly (playful; not humorous/flirty/intellectual), tone_casual, tone_polite; no match
- Shared category rules: tone-value STRING register
- Members: tone_funny (humorous register), tone_flirty (playfully romantic/teasing register), tone_intellectual (register showing reasoning, wit about ideas)
- Exceptions: none
- Proposed record: `{"symbol": "tone_flirty", "kind": "value", "category": "tone-value", "definition": "Playfully romantic or teasing register.", "not": "tone_silly (merely playful)", "aliases": ["flirtatious"]}`

### S2 | type: add | dimension: constructor | symbol: reassure
- Needs: n12 (t2:s3), n17 (t4:s4), n22 (t6:s5-s7)
- Searches tried: "reassure late reply worth the wait", "forgive", "flatter" → acknowledge, apologize, confirm, inform (none express reassurance or forgiveness)
- Typed parameters: target: CLAIM / TERM
- Interpretation: speech act reassuring/forgiving the recipient about the target; asserts nothing beyond the act.
- Example: `UTTER reassure(target=activity_3)`
- Proposed record: `{"symbol": "reassure", "kind": "speech_act", "signature": "UTTER reassure(target: CLAIM / TERM)", "definition": "Speech act reassuring the recipient regarding the target.", "not": "acknowledge (mere awareness)", "aliases": ["forgive"]}`

### S3 | type: refine | dimension: refine-entry | target: activity
- Needs: n23 (t6:s8-s9), n18 (t4:s6)
- Searches tried: entry activity, restaurant → restaurant is an entity-name STRING value, not accepted by activity.object/location slots; speakeasy has no entry
- Before: object accepts STRING / TERM / ATOM[object_label|food_label|animal_label]; location STRING / ATOM[country]
- After: location also accepts entity-name descriptors (e.g. restaurant) via STRING descriptor category
- Justification: venues are needed for dining proposals
- Affected uses: none
- Compatibility: additive
- Proposed record: `{"signature": "TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / TERM / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM"}`
