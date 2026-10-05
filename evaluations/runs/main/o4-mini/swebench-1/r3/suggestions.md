### S1 | type: add | dimension: constructor | symbol: code_revision
- Needs: n16 (t2:s2)
- Searches tried: `search "revision" --kind constructor` → no candidate; widen "code revision term" → nothing
- Typed parameters: description: STRING
- Interpretation: A structured term representing a description of a code modification revision.
- Example: `TERM code_revision(description="add seq_length assignment for inputs_embeds branch") -> code_revision_1 : TERM`
- Proposed record: {"symbol":"code_revision","kind":"constructor","signature":"TERM code_revision(description: STRING) -> TERM","definition":"A description of a code modification revision as a structured term.","not":"a specific code diff or AST node representation","aliases":[]}