### S1 | type: add | dimension: constructor | symbol: network_connection
- Needs: n3 (t1:s1)
- Searches tried: "network connection", "remote", "socket" → remote_control (a physical remote control), laptop, behind; widen "remote connections" → no network socket or process connection constructor
- Typed parameters: mode?: STRING, processes?: NUMBER, target?: STRING / TERM
- Interpretation: Constructs a descriptive representation of a network or inter-process connection.
- Example: `TERM network_connection(mode="remote", processes=2) -> network_connection_2 : TERM`
- Proposed record: {"symbol": "network_connection", "kind": "constructor", "signature": "TERM network_connection(mode?: STRING, processes?: NUMBER, target?: STRING / TERM) -> TERM", "definition": "Constructs a descriptive representation of a network or inter-process connection.", "not": "an active network socket or executed connection attempt", "aliases": ["remote_connection", "socket_connection", "process_connection"]}

### S2 | type: add | dimension: constructor | symbol: hang
- Needs: n12 (t1:s10)
- Searches tried: "stall hang freeze unresponsive" → shower, warning, wait, close; widen "stall hang freeze" → no claim relation for stalling or hanging processes/connections
- Typed parameters: target: TERM / STRING
- Interpretation: Asserts that a target process, command, or connection stalls, hangs, or becomes unresponsive.
- Example: `CLAIM hang(target=cli_command_3) BY role_user STATUS observed SOURCE "t1:s10" -> hang_2 : CLAIM`
- Proposed record: {"symbol": "hang", "kind": "claim_relation", "signature": "CLAIM hang(target: TERM / STRING)", "definition": "Asserts that a target process, command, or connection stalls, hangs, or becomes unresponsive.", "not": "a graceful exit or successful termination", "aliases": ["stall", "freeze", "unresponsive", "deadlock"]}

### S3 | type: refine | dimension: refine-entry | target: v19/operation-vocabulary/modify_code
- Needs: n18 (t2:s2), n20 (t2:s4), n22 (t2:s6)
- Searches tried: modify_code, chg_modify_code → both require mandatory revision: TERM
- Before: (target: STRING / ATOM[platform_label], file: STRING, revision: TERM, method?: STRING) -> void
- After: (target: STRING / ATOM[platform_label], file: STRING, revision?: TERM, method?: STRING) -> void
- Justification: When modifying code by specifying target files without an explicit structured AST revision, revision should be optional.
- Affected uses: None in existing codebase (optional argument is backwards-compatible).
- Compatibility: Fully backwards compatible.
- Proposed record: {"signature": "(target: STRING / ATOM[platform_label], file: STRING, revision?: TERM, method?: STRING) -> void"}
