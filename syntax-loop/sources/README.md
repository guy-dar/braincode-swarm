# sources/

Inspiration material for syntax creation — precedent work, methodological references, and
vocabulary-inspiration notes. This is the folder the **Searcher** role (Gemini) reads from and
writes to during each sprint, including Sprint 0.

- [`previous_work.md`](previous_work.md) — Sprint-0 baseline inspiration (Python, HTML, English,
  formal-language-theory references), precedent papers/talks (ReAct, Parsel, Automatic Textbook
  Formalization, agent-swarm economics, ontology talk), benchmark suites used for Coverage
  testing, and the raw "vocabulary inspiration" list from the team's meeting notes.

This folder is about *why a construct looks the way it does* — precedent and grounding. Actual
example tasks the Shaper translates into syntax live in `../datasets/` (real-world trajectories)
and `../braincode_loop/seed_tasks.json` (small curated pool for fast, cheap sprints). The living
language definition itself lives in `../docs/`.

## Folder vs. internet (70/30)

Every Searcher call — Sprint 0's basis-grounding and every steady-state sprint's task-grounding
— randomly picks one of two modes (`config.yaml -> roles.searcher.folder_probability`, default
70% folder / 30% internet):

- **folder** — ground only in what's already in `previous_work.md`.
- **internet** — search live via Gemini's native Google Search grounding
  (`braincode_loop/llm/gemini_client.py`). Anything durable it finds gets logged into
  `previous_work.md`'s auto-logged section, so future folder-mode sprints benefit from it too —
  the two modes feed each other over a run rather than being isolated.

Keep this folder growing: every sprint's Searcher step should either cite an existing entry or
add a new one with a one-line relevance note. A source with no relevance note is not useful to
future readers — don't add link-only rows.
