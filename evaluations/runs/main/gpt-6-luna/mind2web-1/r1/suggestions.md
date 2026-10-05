### S1 | type: add | dimension: vocabulary-member | symbol: role_senior
- Needs: n9 (t1:s1–t1:s2)
- Searches tried: `widen "senior passenger traveler role" --kind object` → role_adults, role_daughter, role_son, and other unrelated roles; `search "flight passenger senior role group"` → role_adults, role_daughter, role_son, etc. No senior-passenger role was found. `constraint_17_plus` is not a passenger role and must not be used to infer an age threshold.
- Meaning: A senior passenger participant group/role in a travel party; this identifies the group requested without assigning a numeric age threshold.
- Category: recipient-value
- Contextual aliases: senior passenger, senior traveler
- Example: `TERM group_size(count=1, group=role_senior) -> group_size_2 : TERM`
- Contrast: Not `role_adults`; not an assertion that a particular passenger is a particular age, and not a 17+ content/rating constraint.
- Proposed record: {"symbol": "role_senior", "kind": "value", "category": "recipient-value", "definition": "A senior passenger participant role in a travel party; it identifies a senior-traveler group without specifying a numeric age threshold.", "not": "A generic adult passenger, a specific person's identity, or a numeric age/rating threshold such as 17+.", "aliases": ["senior passenger", "senior traveler"]}
