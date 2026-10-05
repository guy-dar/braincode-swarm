# Suggestions from translator swebench-4-r3

- Translator ID: swebench-4-r3
- Batch: 4
- Dataset: swebench
- Item ID: ipython-2529
- Glossary version: 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6)
- Translation: translations/failed/swebench/swebench-4-r3.md

### S1 | type: add | dimension: constructor | symbol: network_connection
- Needs: n3 (t1:s1)
- Searches tried: "remote connections" -> remote_control (a physical TV remote), laptop, caddy; widen "remote connections" --kind object -> remote_control, laptop, resource_chiller; search "connection" -> no relevant constructors
- Typed parameters: target?: STRING / TERM / ATOM[platform_label], protocol?: STRING, remote?: BOOL
- Interpretation: Constructs a structured descriptor representing a network or inter-process communication connection.
- Example: `TERM network_connection(remote=TRUE, target=platform_label::ipython) -> network_connection_2 : TERM`
- Proposed record: {"symbol": "network_connection", "kind": "constructor", "signature": "TERM network_connection(target?: STRING / TERM / ATOM[platform_label], protocol?: STRING, remote?: BOOL) -> TERM", "definition": "Constructs a structured descriptor representing a network or inter-process communication connection.", "not": "remote_control (a physical remote control device) or executed connection action", "aliases": ["remote_connection", "socket_connection", "ipc_connection"]}

### S2 | type: add | dimension: constructor | symbol: cli_flag
- Needs: n7 (t1:s4), n11 (t1:s8)
- Searches tried: "flag '--ip=0'" -> indicator, extract, tone_neutral; "flag '--exiting'" -> indicator, constraint_exclude_liberation_theme; widen "flag" --kind constraint -> indicator, measure
- Typed parameters: flag: STRING, value?: STRING / NUMBER / BOOL
- Interpretation: Constructs a structured specification of a command-line flag or argument option passed to an executable.
- Example: `TERM cli_flag(flag="--ip", value="0") -> cli_flag_2 : TERM`
- Proposed record: {"symbol": "cli_flag", "kind": "constructor", "signature": "TERM cli_flag(flag: STRING, value?: STRING / NUMBER / BOOL) -> TERM", "definition": "Constructs a structured representation of a command-line flag or argument option.", "not": "config_setting (an INI/config file setting) or indicator (a warning sign)", "aliases": ["command_flag", "cli_option", "command_argument"]}
