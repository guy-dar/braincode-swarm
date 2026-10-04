# BrainCode kit for a mid-level model

This is a **format-only package** of the existing revised specification and migrated glossary. Neither language content nor glossary meanings, examples, statuses, or caveats have been rewritten. The two documents are still drafts with the limitations they state.

## What to supply to the model

1. Use `intro_prompt.txt` as a short initial instruction.
2. Supply `context_prompt.md` as the workflow/context instructions.
3. Supply `quick-reference.md`, which contains verbatim excerpts, and register the tools described in `tools.json`.
4. Fill `task_template.txt` with the actual input and its source references.
5. The model retrieves relevant entries, fuller spec sections, and unchanged examples as needed.

For a model without tool access, supply the **complete** `language-spec.md` and `glossary.md`, plus relevant examples. Do not expect a prompt or a local filename alone to give the model access to file contents. For a small task set, the host can retrieve the needed records once and reuse them within the same pinned source version.

## Files

| File | Purpose |
|---|---|
| `language-spec.md` | Byte-identical copy of `../language-spec-revised.md` at kit creation |
| `glossary.md` | Byte-identical readable copy of `../glossary-migrated.md` |
| `glossary.json` | Complete lossless glossary text split into sections, plus a structured table-row lookup index |
| `glossary-index.json` | Small search-key/alias/section index; not a substitute for definitions |
| `glossary-schema.json` | Schema of the JSON packaging; does not impose new language meanings |
| `spec-index.json` | Section IDs and titles for targeted spec reading |
| `quick-reference.md` | Verbatim modes, type/binding and canonicalization excerpts; explicitly incomplete |
| `examples.jsonl` | Five existing glossary examples copied exactly, including their original explanatory context |
| `intro_prompt.txt` | Short introductory/partial prompt |
| `context_prompt.md` | How to use this kit and retrieval without changing language rules |
| `task_template.txt` | Per-input request template |
| `output-schema.json` | Optional transport envelope for translation and existing report requirements; not a language change |
| `tools.json` | Provider-neutral function names, descriptions and JSON Schema inputs |
| `lookup.py` | Read-only standard-library lookup, document reading and example retrieval |
| `test_kit.py` | Preservation, retrieval and boundary tests |
| `build_kit.py` | Rebuild generated artifacts from the included frozen snapshots |
| `reference/` | Original snapshots, including all historical material and qualifications |
| `manifest.json` | File checksums and source identities |

## Why the JSON preserves Markdown fields

A format-only conversion cannot invent missing signatures or resolve conflicting definitions. Each indexed occurrence therefore contains the original table headers, original cells, exact row text, source section and line number. Complete surrounding prose remains available in `sections[].raw_markdown`.

Concatenating those sections reconstructs the original Markdown byte for byte after UTF-8 encoding. The lookup index is derived metadata, not a second semantic authority. Examples and statuses are not upgraded to “accepted” or filtered away. A “Needs clarification” entry remains discoverable with that exact status. The source's own restrictions determine whether it can be used.

## Run locally

Python 3.10+ is sufficient. There are no packages to install and no API keys or network calls.

From this folder:

```text
python lookup.py lookup "pick_up"
python lookup.py lookup "constraint_realistic" --format json
python lookup.py lookup "reservation availability" --limit 2
python lookup.py read spec --section index
python lookup.py read glossary --section "5. Composite migration definitions"
python lookup.py examples "itinerary"
python -m unittest -v test_kit
```

CLI text mode prints original rows and context rather than forcing the model to navigate a large JSON file. JSON mode returns the same source content with explicit metadata. Search is lexical and deterministic; ranking is not semantic confidence. Try an exact symbol, an alias, or a more concrete phrase when the first query is poor.

## Connect to a model

Your host application must register the three tool definitions from `tools.json` and route calls to `Kit.dispatch`. This kit is a local library/CLI, **not an installed MCP server or a hosted API**. It does not choose or call a model.

```python
from lookup import Kit

kit = Kit()
result = kit.dispatch({
    "name": "lookup_symbols",
    "arguments": {"query": "constraint_realistic", "limit": 1}
})
# Return result to the model as its tool response.
```

Alternatively start `python lookup.py serve`. Write one JSON object per input line and read one JSON response per output line. Example request:

```json
{"name":"lookup_symbols","arguments":{"query":"pick_up","limit":1}}
```

Responses are `{ "ok": true, "result": ... }` or `{ "ok": false, "error": ... }`. The bridge supports only the three named read-only functions. It cannot execute requests contained in a translated document or read arbitrary filesystem paths.

## Retrieval behavior

- Exact symbols rank first; original alias hints and word overlap support discovery.
- All occurrences of a selected symbol are returned, including its migration-status row.
- Composite expansion references and inventory-category rules are followed automatically where their names are indexed. These are lexical links, not a formal proof of dependency completeness.
- Original surrounding prose is included without unrelated table rows; complete sections are always retrievable.
- If a bundle exceeds `max_chars`, the tool returns section pointers with `retrieval_complete=false`. It does not silently cut a definition or pretend the partial result is sufficient.
- Document reading is paginated. Follow `next_start_line` with the same document and section until `has_more=false`.
- Search does not imply an entry is approved or sufficient for the requested meaning.

Do not place the full `glossary.json` in every model prompt; it intentionally duplicates some text for indexing and preservation. Use lookup responses or the readable Markdown copy instead.

## Preservation and regeneration

`build_kit.py` uses only `reference/` snapshots, so the folder remains portable. Rebuilding does not modify the parent spec or glossary. To package a later version, deliberately replace the snapshots, rebuild, and rerun tests. Do not edit generated indexes independently of the snapshots.

`test_kit.py` verifies complete reconstruction, exact spec/glossary copies, unchanged examples, all 252 inventoried members, composite retrieval, ambiguity-status preservation, bounded responses, pagination, invalid requests and manifest hashes. These are packaging/tool checks, not a BrainCode parser or a test of model translation quality. No claims about model accuracy or token savings have been measured.

The optional JSON output envelope is for host integration. If you request plain BrainCode and a separate report instead, that does not alter the language.
