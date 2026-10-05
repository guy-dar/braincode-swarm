### S1 | type: add | dimension: vocabulary-member | symbol: inefficient
- Needs: n19 (t4:s1)
- Searches tried: "scissors are inefficient" → only `inefficient` alias on `negation`, not a claim relation; widen "inefficient method" → no claim relations
- Meaning: Asserts that the described method is inefficient in context
- Category: claim_relation
- Contextual aliases: ["inefficient method", "not efficient"]
- Example: `CLAIM inefficient(subject=cut_with_scissors) -> inefficient_cut : CLAIM`
- Contrast: Not a claim of impossibility or failure; asserts low performance rather than inability
- Proposed record: {"symbol":"inefficient","kind":"claim_relation","signature":"CLAIM inefficient(subject: TERM) -> CLAIM","definition":"Asserts that the described method is inefficient in the given context.","not":"a claim that the method cannot work","aliases":["inefficient"]}