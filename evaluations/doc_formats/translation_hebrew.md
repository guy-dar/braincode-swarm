# Format: Hebrew translation (`/output/translation.md`)

The translated item in Hebrew, and nothing else: no heading, no commentary, no code fence around the whole text.

- **A single request** (no turn markers): the request text in Hebrew.
- **A conversation** (turn markers): every turn starts with its marker on the same line, in the original order:

```
<|user|>ההודעה הראשונה של המשתמש
<|assistant|>תשובת העוזר, כולל כל צעד ממוספר שנתן
<|user|>ההודעה הבאה של המשתמש
```

Keep each marker exactly as `<|user|>` or `<|assistant|>`. Code, paths, URLs, identifiers, UI labels and names stay in their original script.
