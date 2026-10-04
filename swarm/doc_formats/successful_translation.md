# Format: successful translation

**Final location:** `translations/successful/<dataset>/<translator_id>.md`, where `<translator_id>` is `<batch_id>-<tnum_inside_batch>`, e.g. `7-23`.

The file has two parts:

1. **Header and original data item.** The host writes this, so the translator never re-copies the item.
2. **Translation body.** The translator writes this as `/output/translation.md`. It starts with `Status: success`.

---

## Part 1 — written by the host (shown for reference)

````markdown
# Translation 7-23 — success

- Translator ID: 7-23
- Batch: 7
- Dataset: alfred
- Item ID: alfred-trial_T20190909_004531_402154#2
- Glossary version: 19.0.0-draft.1+g3 (sha 1a2b3c4d5e6f)
- Model: vertex-proxy/gemini-3.5-flash
- Translated at: 2026-10-04T12:00:00Z
- Needs: 9 (decomposition: llm)

## Original data item

```text
t1:s1 [USER] Put the sponge in the pan and put the pan in the sink.

t2:s1 [AGENT] 1. Walk to the white bin to the right of the fridge.
...
```
````

## Part 2 — written by the translator: `/output/translation.md`

All of these sections are required, in this order. Do not add the header or the original item; the host adds them.

````markdown
Status: success
Mode: REQUEST

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Pan
TASK Pan {
  ACTION pick_up(target=sponge, source=bin) -> sponge_ref : REF[STRING]
  ...
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | pick_up, place | covered |
| n2 | object | sponge | covered |
| n3 | constraint | relation=in | covered |
| n4 | object | object_label::pan | label-preserved |

## Translation report

- Input kind: prompt | conversation
- Coverage status: complete | partial
- Source-span coverage: every segment t1:s1–t2:s7 is represented except …
- Opaque-text spans: none | t3:s2 — reason (content="…" fallback)
- Label-preserved spans: none | t1:s1 "pan" → object_label::pan (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none | t1:s1 — "it" could refer to the pan or the sponge; chose …
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
````

### Rules

- **Status line.** The first line is exactly `Status: success`. The second is `Mode: REQUEST` or `Mode: TRACE` and must match the document's `MODE`.
- **BrainCode block.** There is exactly one fenced `braincode` block. It is a complete document under `/reference/language-spec.md` (one `MODE`, one `ENTRYPOINT`) that uses only glossary symbols, group values (`group::key`, spec §3.1), local handles and literals.
- **Needs coverage.** There is one row per need from `/needs.json`, using its `n<k>` id. `expressed by` names the glossary symbols or constructs used. `status` is `covered`, `opaque`, `not-applicable` or `label-preserved` (expressed only by an open-group label such as `object_label::pan`), and `not-applicable` must be justified in the report. Label-preserved needs are also listed under "Label-preserved spans".
- **Success means** every need is covered or justified, and `rag check` reports no symbols missing from the glossary. If any need could only be expressed with a symbol that doesn't exist, the result is a failed translation (see `failed_translation.md`), not a success with an invented symbol.
- **Translation report.** Its fields are those required by spec §13, "Required external translation report".
