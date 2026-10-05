### S1 | type: add | dimension: constructor | symbol: reconcile
- Needs: n1 (t1:s1), n2 (t1:s1), n7 (t2:s2)
- Searches tried: "reconcile accounts receivable" → reconcile_code (code entities only); no financial reconciliation
- Typed parameters: entities: LIST[TERM], objective?: STRING / TERM
- Interpretation: describes making the listed records/accounts agree with a reference source; asserts nothing.
- Example: `TERM reconcile(entities=[subject_2, subject_3]) -> reconcile_2 : TERM`
- Proposed record: `{"symbol": "reconcile", "kind": "constructor", "signature": "TERM reconcile(entities: LIST[TERM], objective?: STRING / TERM) -> TERM", "definition": "Describes reconciling the listed entities (e.g. accounts) so they agree with a reference source.", "not": "reconcile_code (code behavior standardization)", "aliases": ["reconcile accounts"]}`

### S2 | type: add | dimension: constructor | symbol: meaning_question
- Needs: n4 (t1:s2)
- Searches tried: "what does X mean" → ask (needs TERM target), subject; no property/meaning question constructor
- Typed parameters: subject: TERM, context?: TERM
- Interpretation: asks for the meaning of the subject in the context; presupposes no answer.
- Example: `TERM meaning_question(context=subject_5, subject=subject_4) -> meaning_question_2 : TERM`
- Proposed record: `{"symbol": "meaning_question", "kind": "constructor", "signature": "TERM meaning_question(subject: TERM, context?: TERM) -> TERM", "definition": "Question target asking what the subject means in the context.", "not": "an answer or definition claim", "aliases": ["what does it mean"]}`

### S3 | type: add | dimension: constructor | symbol: recurrence
- Needs: n25 (t4:s23), n3 (t1:s1)
- Searches tried: "schedule report recurring intervals" → time_point, duration, temporal_context (no repetition)
- Typed parameters: activity: TERM, every: NUMBER, unit: STRING
- Interpretation: the activity repeats each interval of the stated length; describes only.
- Example: `TERM recurrence(activity=activity_3, every=1, unit=unit_day) -> recurrence_2 : TERM`
- Proposed record: `{"symbol": "recurrence", "kind": "constructor", "signature": "TERM recurrence(activity: TERM, every: NUMBER, unit: STRING) -> TERM", "definition": "The activity repeats at intervals of every units.", "not": "a single time_point or one duration", "aliases": ["at regular intervals"]}`
