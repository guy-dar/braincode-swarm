### S1 | type: add | dimension: constructor | symbol: connection
- Needs: n3 (t1:s1)
- Searches tried: "remote connections" -> remote_control (a physical remote control device, wrong entity type); widen "remote connections" -> dom_ddp, dom_ovr, laptop; none represent network or inter-process communication connections
- Typed parameters: kind: STRING, protocol?: STRING, target?: STRING / TERM / ATOM[platform_label]
- Interpretation: Constructs a descriptive representation of a network or inter-process communication connection specification; describes, asserts nothing.
- Example: `TERM connection(kind="remote", protocol="two_process") -> connection_2 : TERM`
- Proposed record: {"symbol": "connection", "kind": "constructor", "signature": "TERM connection(kind: STRING, protocol?: STRING, target?: STRING / TERM / ATOM[platform_label]) -> TERM", "definition": "Constructs a descriptive representation of a network, socket, or inter-process communication connection specification.", "not": "remote_control (a physical remote control handset)", "aliases": ["remote connection", "network connection", "process connection"]}

### S2 | type: add | dimension: vocabulary-member | symbol: functions_properly
- Needs: n14 (t1:s11)
- Searches tried: "works properly" -> menu_works (menu evaluation), works_best (event format recommendation); widen "Everything works properly when --ip is not specified" -> menu_works, validates_parameter; neither represents software or system operational correctness
- Meaning: Asserts that the designated software system, feature, or component executes and functions properly without error.
- Category: claim_relation
- Contextual aliases: works, operates correctly, functions as expected, works properly
- Example: `CLAIM functions_properly(system=platform_label::ipython) BY role_user STATUS asserted SOURCE "t1:s11" -> functions_properly_2 : CLAIM`
- Contrast: failure (asserts a system malfunction or failure)
- Proposed record: {"symbol": "functions_properly", "kind": "claim_relation", "signature": "CLAIM functions_properly(system: STRING / ATOM[platform_label], condition?: TERM)", "definition": "Asserts that the indicated software system, component, or workflow functions correctly without errors under specified conditions.", "not": "failure (which asserts a system failure or defect)", "aliases": ["works", "functions properly", "operates correctly"]}
