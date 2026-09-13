# visualizer

Browse a swarm `output/` directory: pick the folder, click a trajectory subfolder,
click a file to view it. `.bc`, `.md` and `.json` files get syntax highlighting;
logs and anything else render as plain text. The header above each file has a
`copy` button that puts its raw contents on the clipboard.

No build step, no dependencies, no server. Open `index.html` in a browser and click
"Choose output folder…" — the folder is read locally via the browser's own file
APIs, nothing leaves your machine.

Works with any task's output — groups files by parent subfolder and lists whatever's
there, no fixed filename list assumed.

If the picked folder holds trajectories directly, that's what you see. If it
holds namespace subfolders instead (`output/<namespace>/<trajectory>/` — what
every run now writes under, one namespace per `SWARM_EXPERIMENT` tag so two
runs never shadow each other), a **namespace** selector appears in the header;
pick one to browse its trajectories. The two shapes are told apart
automatically — nothing to configure.

## Live updating

The folder is re-read on a timer (5s by default, configurable in the header, or
off), so a running batch shows up on its own — no re-picking to see new results.
Newly appeared trajectories are briefly highlighted, and if the file you're looking
at is rewritten it reloads in place, keeping your scroll position. Only actual
changes trigger a re-render, so open sections and scroll position survive a refresh.

Sorted newest first by default, so results land at the top while a batch runs;
switch to name ordering in the header.

This needs the File System Access API (`showDirectoryPicker`), i.e. a Chromium
browser. Elsewhere it falls back to a one-off `<input webkitdirectory>` snapshot —
everything still works, but you have to re-pick the folder to pick up changes, and
the header says so.

## Highlighting

Deliberately structural rather than vocabulary-aware. For `.bc` it recognizes only:

- `<|...|>` turn tags
- strings, comments (`#`), numbers
- Python keywords (`import`, `from`, `def`, `if`, `for`, ...)
- function-call shape (an identifier immediately followed by `(`)

No BrainCode construct or package names are hardcoded — see `../swarm/reference/DESIGN_DOC.md`
for the current vocabulary state.

Markdown is highlighted **as source**, not rendered: `decisions.md` and
`uncertainties.md` are read as evidence of what a translation actually wrote, and
rendering would quietly hide malformed markup instead of showing it. A fenced block
tagged ```` ```bc ```` gets its body highlighted as BrainCode, since those files
often quote it.

JSON is pretty-printed, then keys, strings, numbers and literals are coloured
separately. Invalid JSON is shown verbatim rather than erroring.
