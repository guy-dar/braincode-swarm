Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM cli_command(args=["imports2"], executable="2to3") -> cli_command_2 : TERM
    UTTER ask(target=cli_command_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(object="tools/py3tool.py", verb="modify") -> activity_2 : TERM
    TERM sequence(items=[activity_2]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | action | cli_command | covered |
| n3 | object | cli_command.executable | covered |
| n4 | object | cli_command.args | covered |
| n5 | temporal | sequence | covered |
| n6 | speech_act | propose | covered |
| n7 | action | activity | covered |
| n8 | object | activity.object | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s2 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
