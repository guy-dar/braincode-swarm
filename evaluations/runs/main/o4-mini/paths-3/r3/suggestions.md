### S1 | type: add | dimension: constructor | symbol: plot_request
- Needs: n1 (t1:s1)
- Searches tried:
  • "plot of Inception medieval" → no candidate
  • widen "plot request" → nothing
- Typed parameters: movie: STRING, setting: STRING
- Interpretation: a request to generate a narrative plot for the named movie in the specified setting; does not itself perform generation
- Example:
  TERM plot_request(movie="Inception", setting="medieval") -> plot_request_2 : TERM
- Proposed record:
  {"symbol":"plot_request","kind":"constructor","signature":"TERM plot_request(movie: STRING, setting: STRING) -> TERM","definition":"A request to produce a narrative plot for the specified movie set in the given style or period.","not":"An actual generation or assertion that the plot exists; it just represents the request","aliases":["story_request","plot_request"]}

### S2 | type: add | dimension: constructor | symbol: narrative_text
- Needs: n2–n9, n13–n18
- Searches tried:
  • "narrative text term" → nothing
  • widen "free-form story term" → nothing
- Typed parameters: content: STRING
- Interpretation: wraps a block of free-form narrative text as a structured term for utterance; asserts nothing
- Example:
  TERM narrative_text(content="In a faraway land…") -> narrative_text_2 : TERM
- Proposed record:
  {"symbol":"narrative_text","kind":"constructor","signature":"TERM narrative_text(content: STRING) -> TERM","definition":"Encapsulates free-form narrative or plot text as a structured term for recording speech acts.","not":"A claim or executable action; it merely holds text","aliases":["story_text","narrative"]}

### S3 | type: add | dimension: constructor | symbol: adaptation_request
- Needs: n10 (t3:s1), n11 (t3:s1)
- Searches tried:
  • "rewrite Inception HL2 request" → nothing
  • widen "adaptation request" → nothing
- Typed parameters: original: STRING, setting: STRING
- Interpretation: a request to adapt the named narrative into the specified setting or universe
- Example:
  TERM adaptation_request(original="Dreamcrafter", setting="Half-Life 2") -> adaptation_request_2 : TERM
- Proposed record:
  {"symbol":"adaptation_request","kind":"constructor","signature":"TERM adaptation_request(original: STRING, setting: STRING) -> TERM","definition":"Represents a request to adapt an existing narrative or title into a new setting or context.","not":"An actual transformation or content generation; only the request","aliases":["story_adaptation_request"]}