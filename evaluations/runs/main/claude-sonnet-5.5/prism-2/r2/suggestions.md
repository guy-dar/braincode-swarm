### S1 | type: add | dimension: constructor | symbol: requires
- Needs: n3 (t2:s1), n4 (t2:s1), n5 (t2:s1)
- Searches tried: "need lawn mower gloves eyewear" → requirement (value can't take object_label), obligation (deontic duty); no prerequisite relation
- Typed parameters: activity: TERM, requirement: TERM
- Interpretation: claim relation: performing the activity needs the required item/activity; asserts nothing by itself.
- Example: `CLAIM requires(activity=activity_3, requirement=activity_4) BY role_agent STATUS asserted SOURCE "t2:s1" -> requires_2 : CLAIM`
- Proposed record: `{"symbol": "requires", "kind": "claim_relation", "signature": "CLAIM requires(activity: TERM, requirement: TERM)", "definition": "The activity needs the described item or prerequisite activity.", "not": "an obligation on an actor (obligation)", "aliases": ["need", "needs"]}`

### S2 | type: add | dimension: constructor | symbol: precedes
- Needs: n6 (t2:s3), n12 (t2:s9)
- Searches tried: "first prepare before mowing", "after mowing trim edges" → prep_time, daytime, unit_day, supports; nothing temporal-ordering
- Typed parameters: first: TERM, then: TERM
- Interpretation: claim relation: the first activity is to occur before the second; not causation or support.
- Example: `CLAIM precedes(first=activity_7, then=activity_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> precedes_2 : CLAIM`
- Proposed record: `{"symbol": "precedes", "kind": "claim_relation", "signature": "CLAIM precedes(first: TERM, then: TERM)", "definition": "The first described activity occurs before the second.", "not": "support or causation (supports)", "aliases": ["before", "after", "first"]}`

### S3 | type: add | dimension: constructor | symbol: alternative
- Needs: n13 (t2:s9)
- Searches tried: "string trimmer or edger", "either or choice" → conjunction (all apply), exclude; no disjunction
- Typed parameters: items: LIST[TERM]
- Interpretation: any one of the described items may be used; describes only.
- Example: `TERM alternative(items=[activity_11, activity_12]) -> alternative_2 : TERM`
- Proposed record: `{"symbol": "alternative", "kind": "constructor", "signature": "TERM alternative(items: LIST[TERM]) -> TERM", "definition": "A set of options of which any one satisfies it.", "not": "conjunction (all apply)", "aliases": ["or", "either"]}`

### S4 | type: add | dimension: constructor | symbol: suitable_for
- Needs: n19 (t4:s1), n20 (t4:s2, t4:s3)
- Searches tried: "cutting grass with scissors inefficient for large lawns", "useful for small patches" → enables, recommended, important, works_best; none expresses (un)suitability of an activity for a context
- Typed parameters: activity: TERM, context: TERM, quality: STRING, suitable: BOOL
- Interpretation: claim relation: the activity is (suitable TRUE) or is not (FALSE) suitable for the context regarding the named quality.
- Example: `CLAIM suitable_for(activity=activity_15, context=subject_12, quality="practical_and_efficient", suitable=FALSE) BY role_agent STATUS asserted SOURCE "t4:s1" -> suitable_for_3 : CLAIM`
- Proposed record: `{"symbol": "suitable_for", "kind": "claim_relation", "signature": "CLAIM suitable_for(activity: TERM, context: TERM, quality: STRING, suitable: BOOL)", "definition": "The activity does or does not have the named quality in the given context.", "not": "a recommendation (recommended)", "aliases": ["useful for", "practical for"]}`
