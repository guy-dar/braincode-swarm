### S1 | type: add | dimension: constructor | symbol: inability
- Needs: n1 (t1:s1)
- Searches tried: "failing to complete a game" → failure (system hypothesis) wrong; widen → no matching entry
- Typed parameters: activity: TERM
- Interpretation: expresses an inability to perform the described activity; asserts nothing
- Example: `TERM inability(activity=activity(verb="complete", actor="user", object="game")) -> inability_2 : TERM`
- Proposed record: {"symbol":"inability","kind":"constructor","signature":"TERM inability(activity: TERM) -> TERM","definition":"Expresses an inability to perform the described activity; asserts nothing.","not":"a system failure (use failure)","aliases":["unable to","cannot"]}

### S2 | type: add | dimension: constructor | symbol: help_request
- Needs: n2 (t1:s1), n5 (t1:s1)
- Searches tried: "request help" → offer_help() (generic) misses the underlying activity; widen → nothing
- Typed parameters: activity: TERM
- Interpretation: represents a request for assistance in performing the described activity; asserts nothing
- Example: `TERM help_request(activity=inability_2) -> help_request_2 : TERM`
- Proposed record: {"symbol":"help_request","kind":"constructor","signature":"TERM help_request(activity: TERM) -> TERM","definition":"Represents a request for assistance in performing the described activity; asserts nothing.","not":"assumes the activity occurred","aliases":["ask for help","request assistance"]}