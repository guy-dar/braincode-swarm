### S1 | type: add | dimension: vocabulary-member | symbol: create_file
- Needs: n14 (t1:s15)
- Searches tried: "create file" → no matching operation in glossary; widen "file creation operation" → none found
- Signature: ACTION create_file(target: STRING) -> REF[STRING]
- Definition: Create a new file at the specified path and return its reference identity.
- Not: Does not write file contents or modify existing files; only creates an empty file reference.
- Aliases: ["make_file", "touch_file", "new_file"]
- Example: `ACTION create_file(target="test.py") -> test_py_ref : REF[STRING]`
- Proposed record: {"symbol":"create_file","kind":"operation","signature":"(target: STRING) -> REF[STRING]","definition":"Create a new file at the specified path and return its reference identity.","not":"Does not write file contents or modify existing files.","aliases":["make_file","touch_file","new_file"]}

### S2 | type: add | dimension: constructor | symbol: code_location
- Needs: n21 (t1:s23)
- Searches tried: "code location file line" → no TERM constructor; widen "location in source file" → none found
- Typed parameters: file: STRING, line: NUMBER
- Interpretation: Constructs a term representing a location within a source code file by filename and line number.
- Example: `TERM code_location(file="module.py", line=42) -> code_location_2 : TERM`
- Proposed record: {"symbol":"code_location","kind":"constructor","signature":"TERM code_location(file: STRING, line: NUMBER) -> TERM","definition":"Constructs a term representing a location in a source code file by filename and line number.","not":"An executable operation or plain file path string.","aliases":["source_location","file_location"]}

### S3 | type: add | dimension: vocabulary-member | symbol: not_observed
- Needs: n22 (t1:s24)
- Searches tried: "not observed" → no claim relation; widen "negative observation claim" → none
- Signature: CLAIM not_observed(target: CLAIM)
- Definition: Asserts that the specified event or observation did not occur or could not be observed by the source.
- Not: An assertion that a claim is false; does not prove the negation of the claim's content.
- Aliases: ["absent","unobserved"]
- Example: `CLAIM not_observed(target=some_event_claim) BY user STATUS observed SOURCE "loc" -> not_obs : CLAIM`
- Proposed record: {"symbol":"not_observed","kind":"claim_relation","signature":"CLAIM not_observed(target: CLAIM)","definition":"Asserts that the specified event or observation was not observed or could not be confirmed by the source.","not":"A negation of claim truth; only a statement of missing observation.","aliases":["absent","unobserved"]}