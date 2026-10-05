# Suggestions from translator paths-1-r3

### S1 | type: add | dimension: vocabulary-member | symbol: tone_flirty

- Needs: n4 (t1:s1)
- Searches tried:
  - `search "flirty tone"` → tone_silly, tone_casual, tone_polite (none capture flirtatiousness)
  - `widen "flirty tone"` → same candidates
  - `search "romantic tone"` → no results
  - `search "seductive tone"` → no results
  - `widen "playful romantic register"` → no results

- Meaning: A conversational register conveying romantic or sexual interest, playfulness, and attraction in interpersonal communication.

- Category: tone-value (STRING communication register, parallel to tone_silly, tone_casual, tone_polite)

- Definition: Conveys flirtatiousness, romantic interest, or playful attraction in conversational tone.

- Contextual aliases: flirty, flirtatious, romantic, seductive

- Positive example: A dating app message with a pickup line delivered in a tone_flirty tone

- Negative example (contrast with tone_silly): tone_silly is lighthearted humor without romantic intent; tone_flirty combines playfulness with romantic/sexual interest signals

- Used in: UTTER propose(tone=tone_flirty), UTTER inform(tone=tone_flirty), GENERATE(tone=tone_flirty)

- Proposed record:
```json
{
  "symbol": "tone_flirty",
  "kind": "value",
  "category": "tone-value",
  "signature": "STRING (tone constraint)",
  "definition": "Conveys flirtatiousness, romantic interest, or playful attraction in conversational tone.",
  "not": "tone_silly (which is lighthearted humor without romantic signaling); does not assert attraction as fact, only as conversational register",
  "aliases": ["flirty", "flirtatious"],
  "status": "Accepted"
}
```

