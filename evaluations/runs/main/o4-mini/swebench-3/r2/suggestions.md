### S1 | type: add | dimension: vocabulary-member | symbol: create_file
- Needs: n14 (t1:s15)
- Searches tried: "Create file test.py" → no matching operation; widen "create file operation" → nothing
- signature: create_file(target: STRING) -> REF[STRING]
- definition: An external action that creates a new file at the specified path and returns its file reference.
- not: opening or reading an existing file (use open_file)
- aliases: make_file
- Proposed record: {"symbol":"create_file","kind":"operation","signature":"(target: STRING) -> REF[STRING]","definition":"An external action that creates a new file at the specified path and returns its file reference.","not":"opening or reading an existing file","aliases":["make_file"]}

### S2 | type: add | dimension: vocabulary-member | symbol: execute_cli
- Needs: n17 (t1:s19)
- Searches tried: "Run pytest test.py" → run_tests (runs tests only); widen "execute shell command" → nothing
- signature: execute_cli(command: STRING, args: LIST[STRING]) -> EVENT
- definition: An external action that executes the given command-line executable with arguments, recording an EVENT.
- not: a pure TERM description (use cli_command)
- aliases: run_cli, shell_execute
- Proposed record: {"symbol":"execute_cli","kind":"operation","signature":"(command: STRING, args: LIST[STRING]) -> EVENT","definition":"An external action that executes the given command-line executable with arguments, recording an EVENT.","not":"a pure description without execution","aliases":["run_cli","shell_execute"]}

### S3 | type: add | dimension: vocabulary-member | symbol: deprecation_notice
- Needs: n1 (t1:s1)
- Searches tried: "deprecation warning" → warning relation only accepts STRING; widen "encode deprecation notice" → nothing
- signature: deprecation_notice(module: STRING / ATOM[platform_label], replacement: STRING, version: STRING) -> TERM
- definition: A structured description of a module import deprecation, specifying the old and new import paths and the version when it will stop working.
- not: an external action or assertion; it is a descriptive TERM
- aliases: deprecation_warning
- Proposed record: {"symbol":"deprecation_notice","kind":"constructor","signature":"TERM deprecation_notice(module: STRING / ATOM[platform_label], replacement: STRING, version: STRING) -> TERM","definition":"A structured description of a module import deprecation, specifying the old and new import paths and the version when it will stop working.","not":"an external action or assertion","aliases":["deprecation_warning"]}

### S4 | type: refine | dimension: refine-entry | target: v19/claim_relation/warning
- Needs: n1 (t1:s1), n20 (t1:s21)
- Searches tried: warning relation signature → message: STRING only
- Before: "warning(message: STRING, target?: TERM)"
- After: "warning(message: STRING / TERM, target?: TERM)"
- Justification: To allow structured TERM messages such as deprecation_notice; preserves existing use of STRING messages too.
- Affected uses: all existing uses of warning relation
- Compatibility: backward compatible with STRING messages
- Proposed record: {"signature":"(message: STRING / TERM, target?: TERM)","kind":"claim_relation","status":"Accepted"}

### S5 | type: add | dimension: vocabulary-member | symbol: originates_from
- Needs: n21 (t1:s23)
- Searches tried: "originates from file" → no claim; widen "warning source location claim" → nothing
- signature: originates_from(event: EVENT, file: STRING, line: NUMBER) -> CLAIM
- definition: Asserts that the given event originated from the specified file path and line number.
- not: a temporal occurrence (use occurred_recently)
- aliases: source_location
- Proposed record: {"symbol":"originates_from","kind":"claim_relation","signature":"(event: EVENT, file: STRING, line: NUMBER)","definition":"Asserts that the given event originated from the specified file path and line number.","not":"a temporal or causal relation","aliases":["source_location"]}

### S6 | type: add | dimension: vocabulary-member | symbol: cannot_reproduce
- Needs: n22 (t1:s24)
- Searches tried: "couldn't reproduce" → exclude (requires item), decline, raises_exception; widen "reproduction failure claim" → nothing
- signature: cannot_reproduce(target: TERM) -> CLAIM
- definition: Asserts that the described action or event could not be reproduced when attempted.
- not: an observed error (use raises_exception)
- aliases: reproduction_failed
- Proposed record: {"symbol":"cannot_reproduce","kind":"claim_relation","signature":"(target: TERM)","definition":"Asserts that the described action or event could not be reproduced when attempted.","not":"an observed runtime exception","aliases":["reproduction_failed"]}

### S7 | type: add | dimension: vocabulary-member | symbol: catches_warning
- Needs: n23 (t1:s24)
- Searches tried: "catches warning" → supports, rejects, none; widen "capture warning relation" → nothing
- signature: catches_warning(event: EVENT, warning: CLAIM) -> CLAIM
- definition: Asserts that the specified event handler caught the given warning.
- not: logical inference of support (use supports)
- aliases: warning_caught
- Proposed record: {"symbol":"catches_warning","kind":"claim_relation","signature":"(event: EVENT, warning: CLAIM)","definition":"Asserts that the specified event handler caught the given warning.","not":"a general support or causation link","aliases":["warning_caught"]}