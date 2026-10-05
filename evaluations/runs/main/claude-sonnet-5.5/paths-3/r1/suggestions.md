### S1 | type: add | dimension: constructor | symbol: adaptation
- Needs: n3 (t2:s1), n11 (t3:s1), n12 (t4:s1)
- Searches tried: "adaptation of a story into another setting" → aesthetic (style/period only), substitute (entity replacement), art_story (artifact class); entry adaptation → none
- Typed parameters: source: STRING / TERM, setting: STRING / TERM, title?: STRING
- Interpretation: a described work derived from the source work, relocated to the setting; asserts nothing.
- Example: `TERM adaptation(setting="medieval fantasy", source="Inception", title="Dreamcrafter") -> adaptation_2 : TERM`
- Proposed record: `{"symbol": "adaptation", "kind": "constructor", "signature": "TERM adaptation(source: STRING / TERM, setting: STRING / TERM, title?: STRING) -> TERM", "definition": "A described work derived from the source work and transposed into the setting, optionally titled; asserts nothing.", "not": "substitute (replacing an entity)", "aliases": ["adaptation", "retelling"]}`

### S2 | type: add | dimension: constructor | symbol: depicts
- Needs: n3–n9, n12–n18 (t2, t4)
- Searches tried: "story contains events and characters" → provides, activity, sequence; widen → nothing relating an artifact to content
- Typed parameters: artifact: TERM, content: TERM
- Interpretation: CLAIM that the described artifact contains/narrates the content (fictional content, not real events).
- Example: `CLAIM depicts(artifact=adaptation_2, content=activity_3) BY role_agent STATUS asserted SOURCE "t2:s5" -> depicts_3 : CLAIM`
- Proposed record: `{"symbol": "depicts", "kind": "claim_relation", "signature": "CLAIM depicts(artifact: TERM, content: TERM)", "definition": "The artifact narrates or portrays the content; says nothing about the content being real.", "not": "provides (supplying an item/service)", "aliases": ["portrays", "narrates"]}`
