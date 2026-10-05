Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM code_entity(kind="fixer", name="imports2", project=platform_label::imports2) -> code_entity_2 : TERM
    TERM cli_command(args=[code_entity_2], executable="2to3") -> cli_command_2 : TERM
    UTTER propose(target=cli_command_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM code_entity(file="tools/py3tool.py", kind="script", name="py3tool") -> code_entity_3 : TERM
    TERM chg_modify_code(target=platform_label::imports2, file="tools/py3tool.py", revision=t1.code_entity_2) -> chg_modify_code_2 : TERM
    TERM sequence(items=[chg_modify_code_2]) -> sequence_2 : TERM
    UTTER respond(target=sequence_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | propose | covered |
| n2 | action | cli_command | covered |
| n3 | object | platform_label | covered |
| n4 | object | platform_label::imports2 | label-preserved |
| n5 | temporal | sequence | covered |
| n6 | speech_act | respond | covered |
| n7 | action | chg_modify_code | covered |
| n8 | object | code_entity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s2 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "imports2" → platform_label::imports2 (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
