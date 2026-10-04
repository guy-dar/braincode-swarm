// Allowlist guard for grep and find inside the harness (see guard-search.sh).
// Agents may only search the paths mounted for them; anything else (the root,
// system dirs, the home dir) is refused with the list of allowed paths. The
// arguments are parsed, so a pattern such as `grep -v "/proc"` is never
// mistaken for a path. Relative paths resolve against the working directory.
import { spawnSync } from "node:child_process";
import { resolve } from "node:path";

const [, , tool, real, ...args] = process.argv;

const ALLOWED = [
  "/reference", "/kit", "/doc_formats", "/attach", "/output", "/tmp", "/workspace",
  "/trajectory.txt", "/item_raw.txt", "/rag_context.md", "/needs.json",
  // migration agents
  "/suggestions", "/translations", "/merged", "/previous",
];
const allowed = (p) => {
  const abs = resolve(process.cwd(), p);
  return ALLOWED.some((root) => abs === root || abs.startsWith(root + "/"));
};

// grep: options that consume the next argument as their value.
const GREP_VALUE_OPTS = new Set(["-e", "-f", "-A", "-B", "-C", "-m", "-d", "-D", "--regexp", "--file",
  "--after-context", "--before-context", "--context", "--max-count", "--include", "--exclude",
  "--exclude-dir", "--label", "--color", "--colour"]);

function grepPaths(argv) {
  const positional = [];
  let patternGiven = false;
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--") { positional.push(...argv.slice(i + 1)); break; }
    if (a.startsWith("--")) {
      const name = a.split("=")[0];
      if (name === "--regexp" || name === "--file") patternGiven = true;
      if (!a.includes("=") && GREP_VALUE_OPTS.has(name)) i++;
      continue;
    }
    if (a.startsWith("-") && a.length > 1) {
      // short options, possibly combined (-rn); a value option may carry its value inline (-A3)
      const letters = a.slice(1);
      for (let j = 0; j < letters.length; j++) {
        const opt = "-" + letters[j];
        if (opt === "-e" || opt === "-f") patternGiven = true;
        if (GREP_VALUE_OPTS.has(opt)) { if (j === letters.length - 1) i++; break; }
      }
      continue;
    }
    positional.push(a);
  }
  return patternGiven ? positional : positional.slice(1);   // first positional is the pattern
}

function findPaths(argv) {
  const paths = [];
  for (const a of argv) {
    if (a.startsWith("-") || a === "(" || a === "!" || a === ")") break;   // expression starts
    paths.push(a);
  }
  return paths;
}

const paths = tool === "find" ? findPaths(args) : grepPaths(args);
const bad = paths.filter((p) => !allowed(p));
if (bad.length) {
  process.stderr.write(
    `${tool}: not allowed to search ${bad.join(", ")} — only the mounted paths can be searched: ` +
    `${ALLOWED.join(", ")}. For glossary symbols use: node /kit/rag.mjs search "<meaning>" or grep /reference/glossary.md\n`);
  process.exit(2);
}
const res = spawnSync(real, args, { stdio: "inherit" });
process.exit(res.status === null ? 1 : res.status);
