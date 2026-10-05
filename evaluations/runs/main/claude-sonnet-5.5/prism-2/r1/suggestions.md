### S1 | type: add | dimension: constructor | symbol: precedes
- Needs: n6 (t2:s3), n12 (t2:s9)
- Searches tried: "first prepare before mowing", "after mowing trim edges" → prep_time (duration estimate), no ordering relation
- Typed parameters: earlier: TERM, later: TERM
- Interpretation: claim relation; the earlier activity is to be done before the later one. Not causation or support.
- Example: `CLAIM precedes(earlier=conjunction_3, later=activity_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> precedes_2 : CLAIM`
- Proposed record: `{"symbol": "precedes", "kind": "claim_relation", "signature": "CLAIM precedes(earlier: TERM, later: TERM)", "definition": "The earlier described activity is to occur before the later one.", "not": "causation, support or mere textual adjacency", "aliases": ["before", "first", "after"]}`

### S2 | type: add | dimension: constructor | symbol: fraction
- Needs: n9 (t2:s5)
- Searches tried: "no more than a third" → at_most, measure (needs unit), no fraction unit
- Typed parameters: numerator: NUMBER, denominator: NUMBER, of: STRING / TERM
- Interpretation: the stated fraction of the named quantity; usable in at_most/at_least; denominator nonzero.
- Example: `TERM fraction(denominator=3, numerator=1, of="grass_height_per_mowing") -> fraction_2 : TERM`
- Proposed record: `{"symbol": "fraction", "kind": "constructor", "signature": "TERM fraction(numerator: NUMBER, denominator: NUMBER, of: STRING / TERM) -> TERM", "definition": "A proportion of the named quantity; asserts nothing.", "not": "a percentage or absolute measure", "aliases": ["a third", "half of"]}`

### S3 | type: add | dimension: constructor | symbol: alternatives
- Needs: n13 (t2:s9)
- Searches tried: "string trimmer or edger" → conjunction only (all apply), no disjunction
- Typed parameters: items: LIST[TERM]
- Interpretation: any one of the described items suffices/is acceptable; describes, asserts nothing.
- Example: `TERM alternatives(items=[activity_10, activity_11]) -> alternatives_2 : TERM`
- Proposed record: `{"symbol": "alternatives", "kind": "constructor", "signature": "TERM alternatives(items: LIST[TERM]) -> TERM", "definition": "Any one of the described components may be chosen.", "not": "conjunction or exclusive choice", "aliases": ["or", "either"]}`

### S4 | type: add | dimension: constructor | symbol: feasibility
- Needs: n19 (t4:s1)
- Searches tried: "possible but inefficient for large lawns" → enables, recommended, important; none express possibility with efficiency in a context
- Typed parameters: activity: TERM, context?: TERM, possible: BOOL, efficient?: BOOL
- Interpretation: claim that the activity is (not) possible and (not) efficient in the context.
- Example: `CLAIM feasibility(activity=activity_15, context=subject_3, efficient=FALSE, possible=TRUE) BY role_agent STATUS asserted SOURCE "t4:s1" -> feasibility_2 : CLAIM`
- Proposed record: `{"symbol": "feasibility", "kind": "claim_relation", "signature": "CLAIM feasibility(activity: TERM, context?: TERM, possible: BOOL, efficient?: BOOL)", "definition": "Whether the activity can be done and whether it is efficient in the context.", "not": "a recommendation", "aliases": ["practical", "workable"]}`
