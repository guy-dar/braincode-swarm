# visualizer

Browse a swarm `output/` directory: pick the folder, click a trajectory subfolder,
click a file to view it. `.bc` files get syntax highlighting; `.md`/`.json`/logs
render as plain text (JSON pretty-printed).

No build step, no dependencies, no server. Open `index.html` in a browser and click
"Choose output folder…" (`<input webkitdirectory>` — reads the folder locally via
the browser's own file APIs, nothing leaves your machine).

Works with any task's output — groups files by parent subfolder and lists whatever's
there, no fixed filename list assumed.

## Highlighting

Recognizes only:

- `<|...|>` turn tags
- strings, comments (`#`), numbers
- Python keywords (`import`, `from`, `def`, `if`, `for`, ...)
- function-call shape (an identifier immediately followed by `(`)

No BrainCode construct or package names are hardcoded — see `../swarm/DESIGN_DOC.md`
for the current vocabulary state.
