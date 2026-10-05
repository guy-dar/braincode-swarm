### S1 | type: add | dimension: member-family | symbol: tone_funny
- Needs: n3 (t1:s1), n4 (t1:s1), n5 (t1:s1)
- Searches tried: "funny tone", "flirty tone", "intellectual tone" → tone_silly (playful/lighthearted, not humor-intent), tone_casual, tone_polite, style_academic (style, not register); none flirty or intellectual
- Shared category rules: tone-value STRING registers
- Members: tone_funny (humorous register); tone_flirty (playfully romantic/teasing register); tone_intellectual (register showing erudition and abstract reasoning)
- Exceptions: none
- Proposed record: `{"symbol": "tone_flirty", "kind": "value", "category": "tone-value", "definition": "Playfully romantic, teasing register; also add tone_funny and tone_intellectual.", "not": "tone_silly (lighthearted without romantic intent)", "aliases": ["flirtatious"]}`

### S2 | type: add | dimension: constructor | symbol: persona
- Needs: n2 (t1:s1)
- Searches tried: "adopt a playboy persona" → role_user, role_agent, char_female, character_trait; widen → nothing for a persona the speaker should act as
- Typed parameters: name: STRING / TERM
- Interpretation: a described persona the agent is asked to adopt in its responses; describes, asserts nothing about the agent's identity.
- Example: `TERM persona(name="playboy") -> persona_2 : TERM`
- Proposed record: `{"symbol": "persona", "kind": "constructor", "signature": "TERM persona(name: STRING / TERM) -> TERM", "definition": "A persona or role-play character to be adopted in speech; asserts nothing.", "not": "identity (a name claim) or character (a fictional character description)", "aliases": ["act like"]}`
