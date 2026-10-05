### S1 | type: add | dimension: constructor | symbol: deprecation_notice
- Needs: n1 (t1:s1)
- Searches tried: "deprecation warning details" → only generic `warning` relation; no constructor for full-text deprecation details
- Typed parameters: source_module: STRING, target_module: STRING, version: NUMBER
- Interpretation: Structured representation of a deprecation notice with the original and replacement modules and the version where deprecation takes effect.
- Example: `TERM deprecation_notice(source_module="collections", target_module="collections.abc", version=3.8) -> deprecation_notice_2 : TERM`
- Proposed record: {"symbol":"deprecation_notice","kind":"constructor","signature":"TERM deprecation_notice(source_module: STRING, target_module: STRING, version: NUMBER) -> TERM","definition":"Structured representation of a deprecation notice specifying the original module, its replacement, and the version where deprecation applies.","not":"A claim of system failure or exception (use warning for that)","aliases":["deprecation_detail","deprecation_warning"]}

### S2 | type: add | dimension: constructor | symbol: code_location
- Needs: n21 (t1:s23)
- Searches tried: "file path and line number" → no existing constructor; file locations encoded only in RECORD arguments
- Typed parameters: path: STRING, line: NUMBER
- Interpretation: Identifies a source code location by file path and line number; asserts nothing beyond location.
- Example: `TERM code_location(path="foo/bar.py", line=42) -> code_location_2 : TERM`
- Proposed record: {"symbol":"code_location","kind":"constructor","signature":"TERM code_location(path: STRING, line: NUMBER) -> TERM","definition":"Represents a precise location in source code by file path and line number.","not":"An executable operation or assertion; use RECORD for events","aliases":["source_location","file_line"]}
