# Format: reconstruction (`/output/reconstruction.md`)

The reconstructed item in the dataset's raw form, and nothing else: no heading, no commentary, no code fence.

- **A single request** (`MODE REQUEST` without turns): the request text, as the user would have typed it.
- **A conversation** (turns): every turn starts with its marker on the same line, in order:

```
<|user|>first user message
<|assistant|>the assistant's reply, including any numbered steps it gave
<|user|>the next user message
```

Use `<|user|>` for `SPEAKER=USER` and `<|assistant|>` for `SPEAKER=AGENT`. Keep each turn's content in the order the code gives it.
