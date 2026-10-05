### S1 | type: add | dimension: member-family | symbol: tone_flirty
- Needs: n3 (t1:s1), n4 (t1:s1), n5 (t1:s1)
- Searches tried: "funny tone", "flirty tone", "intellectual tone" → tone_silly, tone_casual, tone_polite, style_academic; none matches
- Shared category rules: tone-value STRING register
- Members: tone_funny (humorous register), tone_flirty (playfully romantic register), tone_intellectual (erudite, idea-focused register)
- Exceptions: none
- Proposed record: `{"symbol": "tone_flirty", "kind": "value", "category": "tone-value", "definition": "Playfully romantic or teasing register.", "not": "tone_silly", "aliases": ["flirtatious"]}`

### S2 | type: add | dimension: constructor | symbol: persona
- Needs: n2 (t1:s1)
- Searches tried: "adopt a playboy persona" → role_agent, character, char_female; none expresses adopting a persona
- Typed parameters: label: STRING / TERM
- Interpretation: requires the responder to speak as the described persona; asserts nothing about reality.
- Example: `TERM persona(label="playboy") -> persona_2 : TERM`
- Proposed record: `{"symbol": "persona", "kind": "constructor", "signature": "TERM persona(label: STRING / TERM) -> TERM", "definition": "A persona the speaker is to adopt; describes, asserts nothing.", "not": "character (fictional character description)", "aliases": ["act like"]}`
