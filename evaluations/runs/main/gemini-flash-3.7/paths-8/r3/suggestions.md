### S1 | type: add | dimension: vocabulary-member | symbol: praise
- Needs: n6 (t2:s1), n7 (t2:s2), n11 (t4:s1), n15 (t6:s1), n16 (t6:s2)
- Searches tried: "praise" → greeting, well_wishes, acknowledge, important; "commend" → recommended; widen "praise Arun's ongoing support" → role_support_team, supports, ongoing, confirm, inform, acknowledge
- Meaning: Speech act expressing praise, commendation, or compliment for a person, contribution, quality, or achievement.
- Category: operation-vocabulary
- Contextual aliases: commend, compliment, laud, applaud
- Example: `UTTER praise(recipient="Arun", target=ongoing_2)`
- Contrast: acknowledge (which acknowledges receipt without evaluative praise) or confirm (which confirms factual truth)
- Proposed record: {"symbol": "praise", "kind": "speech_act", "signature": "UTTER praise(target?: CLAIM / TERM, recipient?: STRING / TERM)", "definition": "Speech act expressing praise, commendation, or compliment for a person, contribution, quality, or achievement.", "not": "acknowledge (which acknowledges receipt without evaluative praise) or confirm (which confirms factual truth)", "aliases": ["commend", "compliment", "laud", "applaud"]}

### S2 | type: add | dimension: vocabulary-member | symbol: thank
- Needs: n8 (t2:s3), n12 (t4:s2), n13 (t4:s3), n17 (t6:s3), n18 (t6:s4)
- Searches tried: "thank" → acknowledge, greeting, well_wishes; "gratitude" → well_wishes, acknowledge; "appreciation" → acknowledge, well_wishes; widen "express gratitude" → offer, offer_help, acknowledge, apologize
- Meaning: Speech act expressing thanks, gratitude, or appreciation to an addressee for assistance, efforts, or contributions.
- Category: operation-vocabulary
- Contextual aliases: express gratitude, express appreciation, thanks, grateful
- Example: `UTTER thank(recipient="Arun", target=activity_2)`
- Contrast: apologize (which expresses regret) or well_wishes (which conveys parting encouragement/wishes)
- Proposed record: {"symbol": "thank", "kind": "speech_act", "signature": "UTTER thank(target?: CLAIM / TERM, recipient?: STRING / TERM)", "definition": "Speech act expressing thanks, gratitude, or appreciation to an addressee for assistance, efforts, or contributions.", "not": "apologize (which expresses regret) or well_wishes (which conveys parting encouragement/wishes)", "aliases": ["express gratitude", "express appreciation", "thanks", "grateful"]}

### S3 | type: add | dimension: constructor | symbol: compliment
- Needs: n1 (t1:s1), n2 (t1:s1), n9 (t3:s1), n14 (t5:s1)
- Searches tried: "compliment" → acknowledge, well_wishes, greeting; widen "write a compliment" → well_wishes, greeting, acknowledge, propose
- Typed parameters: recipient?: STRING / TERM, topic?: STRING / TERM, qualities?: LIST[TERM]
- Interpretation: Constructs a descriptive term representing a compliment or praise statement directed at a recipient, optionally specifying topic and praised qualities.
- Example: `TERM compliment(qualities=[conjunction_2], recipient="Arun") -> compliment_2 : TERM`
- Proposed record: {"symbol": "compliment", "kind": "constructor", "signature": "TERM compliment(recipient?: STRING / TERM, topic?: STRING / TERM, qualities?: LIST[TERM]) -> TERM", "definition": "Constructs a descriptive term representing a compliment or praise directed at a recipient, optionally specifying topic and praised qualities.", "not": "an executed speech act (use UTTER praise) or salutation (use greeting)", "aliases": ["praise_message", "compliment_text", "words_of_praise"]}
