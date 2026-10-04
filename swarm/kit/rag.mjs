#!/usr/bin/env node
// Glossary RAG client for models running inside harness containers.
// Zero dependencies (Node >= 18 for fetch). Talks to the host's RAG server
// (swarm/rag/server.py) at $RAG_URL, else http://host.docker.internal:$RAG_PORT.
//
//   node /kit/rag.mjs retrieve [--file /trajectory.txt]   steps 1-4: needs + candidates + records
//   node /kit/rag.mjs search "<need 1>" ["<need 2>" ...] [--kind constraint]   one call, several needs
//   node /kit/rag.mjs widen  "<need text>" [--kind ...]      step 6: broad search for an unresolved need
//   node /kit/rag.mjs entry  <symbol> [<symbol> ...]        compact records + their rules and dependencies;
//                                                            a value group also lists its slots, and
//                                                            `entry currency::ZAR` says whether that key is valid
//   node /kit/rag.mjs check  --translation /output/translation.md [--needs /needs.json]   step 5
//   node /kit/rag.mjs needs  [--file ...]                   step 1 only
//   node /kit/rag.mjs health
//
// Output is the rendered text a model reads; add --json for raw JSON.
import { readFileSync } from "node:fs";

const argv = process.argv.slice(2);
const command = argv[0];
const flags = {};
const positional = [];
for (let i = 1; i < argv.length; i++) {
  if (argv[i].startsWith("--")) {
    const key = argv[i].slice(2);
    const next = argv[i + 1];
    if (next === undefined || next.startsWith("--")) flags[key] = true;
    else { flags[key] = next; i++; }
  } else positional.push(argv[i]);
}

const base = (process.env.RAG_URL || `http://host.docker.internal:${process.env.RAG_PORT || "8765"}`).replace(/\/$/, "");
const asText = !flags.json;

async function call(method, path, body, nullOn404 = false) {
  const options = { method, headers: { "Content-Type": "application/json" } };
  if (body !== undefined) options.body = JSON.stringify({ ...body, format: asText ? "text" : undefined });
  let res;
  for (let attempt = 1; ; attempt++) {
    try { res = await fetch(base + path, options); break; }
    catch (err) {
      if (attempt >= 4) {
        console.error(`rag: cannot reach ${base} (${err.message}). Fall back to grepping /reference/glossary.md.`);
        process.exit(2);
      }
      await new Promise((r) => setTimeout(r, 1500 * attempt));
    }
  }
  const text = await res.text();
  if (nullOn404 && res.status === 404) return null;
  if (!res.ok) { console.error(`rag: ${path} -> HTTP ${res.status}: ${text.slice(0, 400)}`); process.exit(1); }
  return text;
}

function readFlagFile(name, fallback) {
  const path = flags[name] || fallback;
  try { return readFileSync(path, "utf8"); }
  catch { console.error(`rag: cannot read ${path}`); process.exit(1); }
}

function loadNeeds() {
  const raw = JSON.parse(readFlagFile("needs", "/needs.json"));
  return Array.isArray(raw) ? raw : raw.needs || [];
}

// /trajectory.txt is the numbered view ("t1:s2 [USER] ..."); the server
// numbers raw content itself, so retrieve/needs read the raw item instead.
function itemContent() {
  return readFlagFile("file", "/item_raw.txt");
}

const query = positional.join(" ");
let out;
switch (command) {
  case "health": out = await call("GET", "/health"); break;
  case "needs": out = await call("POST", "/needs", { content: itemContent() }); break;
  case "retrieve": out = await call("POST", "/retrieve", { content: itemContent() }); break;
  case "search":
    // Each quoted argument is its own query: look up several needs in one call.
    if (!positional.length) { console.error('usage: rag search "<need 1>" ["<need 2>" ...] [--kind K] [--context C]'); process.exit(1); }
    // `text` too, for a server that predates multi-query search (it ignores `queries`).
    out = await call("POST", "/search", { queries: positional, text: positional.join(" "), kind: flags.kind || "", context: flags.context || "", k: Number(flags.k || 15), keep: Number(flags.keep || 8) });
    break;
  case "widen":
    if (!query) { console.error('usage: rag widen "<need text>" [--kind K]'); process.exit(1); }
    out = await call("POST", "/widen", { text: query, kind: flags.kind || "", context: flags.context || "" });
    break;
  case "entry":
    if (!positional.length) { console.error("usage: rag entry <symbol> [<symbol> ...]"); process.exit(1); }
    out = await call("POST", "/entries", { keys: positional }, true);
    if (out === null) {  // server predates /entries: one lookup per symbol
      const parts = [];
      for (const key of positional) parts.push(await call("GET", "/entry/" + encodeURIComponent(key)));
      out = parts.join("\n");
    }
    break;
  case "check":
    out = await call("POST", "/check", { translation: readFlagFile("translation", "/output/translation.md"), needs: loadNeeds() });
    break;
  default:
    console.error("usage: rag <retrieve|search|widen|entry|check|needs|health> ... (see header of /kit/rag.mjs)");
    process.exit(1);
}
process.stdout.write(out.endsWith("\n") ? out : out + "\n");
