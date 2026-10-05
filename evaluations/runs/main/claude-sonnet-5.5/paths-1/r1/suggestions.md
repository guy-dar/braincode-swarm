### S1 | type: add | dimension: constructor | symbol: persona
- Needs: n2 (t1:s1)
- Searches tried: "adopt a playboy persona" → role_user, character (fictional character descriptor), identity (claim of a name), char_female; widen found nothing for a persona the responder is to adopt
- Typed parameters: name: STRING / TERM, traits?: LIST[TERM]
- Interpretation: describes a persona or role the agent is requested to speak as; asserts nothing about the agent's real identity.
- Example: `TERM persona(name="playboy") -> persona_2 : TERM`
- Proposed record: `{"symbol": "persona", "kind": "constructor", "signature": "TERM persona(name: STRING / TERM, traits?: LIST[TERM]) -> TERM", "definition": "A role or persona that a speaker is to adopt in generated output; describes, asserts nothing.", "not": "identity (a claim of name) or character (a fictional character descriptor)", "aliases": ["act like", "play the role of"]}`

### S2 | type: add | dimension: member-family | symbol: tone_flirty
- Needs: n4 (t1:s1), n5 (t1:s1)
- Searches tried: "flirty tone", "intellectual tone" → tone_silly, tone_casual, tone_polite, tone_empathetic, style_academic; none fit
- Shared category rules: tone-value, STRING register
- Members: tone_flirty (playfully romantic or teasing register); tone_intellectual (register showing thoughtful, knowledge-referencing wit)
- Exceptions: none
- Proposed record: `{"symbol": "tone_flirty", "kind": "value", "category": "tone-value", "definition": "Playfully romantic or teasing register.", "not": "tone_polite or tone_casual", "aliases": ["flirtatious", "flirty"]}`
