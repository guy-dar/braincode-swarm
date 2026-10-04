/**
 * Context limits for loop agents (loaded with `-e`, see entrypoint.sh). Both
 * parts are off unless their env var is set, so agents that need large tool
 * results or their whole history (the migration agents) are unaffected.
 *
 * PI_TOOL_RESULT_MAX_CHARS: cap on what one tool call puts into the
 *   conversation. Every later model call re-sends it, and translators used to
 *   pull whole glossary categories this way (grep for a kind column, `cat
 *   /needs.json`, a `node -e` filter over glossary.md, chained `rag widen`):
 *   28-51k characters each, re-sent on every turn after. The output is cut at
 *   a line boundary and the agent is told how much was dropped and how to
 *   narrow the lookup.
 *
 * PI_COMPACT_AT (estimated tokens): before a model call whose context is over
 *   this, the older turns are replaced by a summary. The first message (the
 *   task, with the spec, retrieval context and formats attached) stays
 *   verbatim, with the summary appended to it; the latest
 *   PI_KEEP_RECENT_TOKENS of turns stay as they are. This runs in the
 *   `context` hook, which only changes what is sent: the session file keeps
 *   the full history. The summary is reused on every later call (so the
 *   prompt prefix stays cacheable) until the context grows past the threshold
 *   again, when the summary is extended. When the first message alone is
 *   large, the threshold rises to its size + PI_COMPACT_HEADROOM (30000).
 *   (Pi's own auto-compaction never triggers in --print mode within one
 *   prompt, and its summary would also summarize the spec away.)
 *
 * PI_CONTEXT_LOG: a JSON-lines file; one line per compaction, with the
 *   summary call's token usage, so the host can count its cost.
 */
import * as fs from "node:fs";

type Part = { type: string; text?: string; thinking?: string; name?: string; arguments?: unknown };
type Msg = { role?: string; content?: string | Part[]; timestamp?: number };

const MAX_CHARS = Number(process.env.PI_TOOL_RESULT_MAX_CHARS || 0);
const COMPACT_AT = Number(process.env.PI_COMPACT_AT || 0);
const KEEP_RECENT = Number(process.env.PI_KEEP_RECENT_TOKENS || 12000);
const COMPACT_HEADROOM = Number(process.env.PI_COMPACT_HEADROOM || 30000);
const LOG = process.env.PI_CONTEXT_LOG || "";
const TOOL_RESULT_IN_SUMMARY = 1500;

function log(entry: Record<string, unknown>) {
  if (!LOG) return;
  try {
    fs.appendFileSync(LOG, JSON.stringify({ at: new Date().toISOString(), ...entry }) + "\n");
  } catch { /* logging only */ }
}

function partsOf(m: Msg): Part[] {
  return typeof m.content === "string" ? [{ type: "text", text: m.content }] : (m.content || []);
}

function textOf(m: Msg): string {
  return partsOf(m).filter((p) => p.type === "text").map((p) => p.text || "").join("\n");
}

/** Rough token estimate (characters / 4), the same order as pi's own. */
function tokens(messages: Msg[]): number {
  let chars = 0;
  for (const m of messages) {
    for (const p of partsOf(m)) {
      chars += (p.text || p.thinking || "").length;
      if (p.type === "toolCall") chars += JSON.stringify(p.arguments || {}).length;
    }
  }
  return Math.ceil(chars / 4);
}

/** Context size of a call: the provider's own count from the last reply in
 * this view (input + cached tokens + its output), plus an estimate for what
 * came after it. chars/4 alone ran 15-20% low on translator conversations, so
 * a 70k threshold only fired at ~83k real tokens. */
function contextTokens(full: Msg[], view: Msg[], since: number): number {
  // only replies made after the last compaction measured the context as it is now sent
  for (let i = full.length - 1; i >= since; i--) {
    const u = (full[i] as any).usage;
    if (full[i].role === "assistant" && u && (u.input || u.cacheRead)) {
      return (u.input || 0) + (u.cacheRead || 0) + (u.output || 0) + tokens(full.slice(i + 1));
    }
  }
  return tokens(view);
}

function serialize(messages: Msg[]): string {
  const out: string[] = [];
  for (const m of messages) {
    if (m.role === "user") out.push(`[Instruction]: ${textOf(m)}`);
    else if (m.role === "assistant") {
      for (const p of partsOf(m)) {
        if (p.type === "text" && p.text) out.push(`[Agent]: ${p.text}`);
        else if (p.type === "toolCall") out.push(`[Agent ran ${p.name}]: ${JSON.stringify(p.arguments)}`);
      }
    } else if (m.role === "toolResult") {
      const t = textOf(m);
      out.push(`[Result]: ${t.length > TOOL_RESULT_IN_SUMMARY
        ? t.slice(0, TOOL_RESULT_IN_SUMMARY) + ` …[${t.length - TOOL_RESULT_IN_SUMMARY} more characters]` : t}`);
    }
  }
  return out.join("\n");
}

const SUMMARY_PROMPT = `You are compacting the working history of an agent that translates one item into BrainCode. The agent keeps its original instructions and attachments verbatim and its latest turns unchanged; your summary replaces only the turns below (and the earlier summary, if one is given). Keep everything it needs to continue without redoing work, and nothing else:

- Which steps of its instructions are already done (so they are not repeated), and which remain.
- Glossary symbols it looked up and found usable, and for which need: exact symbol names and signatures.
- Lookups that found nothing (so they aren't repeated), and needs still unresolved.
- Decisions about the translation and why; problems a check reported and whether they were fixed.
- Files written under /output (path and state) and the current translation draft, verbatim if it is in these turns.
- Suggestions it plans to make.
- The next steps.

Be concise: lists, exact names, no narration.`;

const SUMMARY_HEAD = "\n\n---\n## Your work so far (compacted)\n\nThe conversation got long, so your older turns were replaced by this summary. Your instructions and attachments above are unchanged, and your latest turns follow as they were. Don't redo steps the summary lists as done.\n\n";

export default function (pi: any) {
  if (MAX_CHARS > 0) {
    pi.on("tool_result", async (event: any) => {
      const parts: Part[] = event.content || [];
      const total = parts.reduce((n, p) => n + (p.type === "text" ? (p.text || "").length : 0), 0);
      if (total <= MAX_CHARS) return;
      let budget = MAX_CHARS;
      const content: Part[] = [];
      for (const p of parts) {
        if (p.type !== "text") { content.push(p); continue; }
        if (budget <= 0) continue;
        const t = p.text || "";
        let keep = t.length <= budget ? t : t.slice(0, budget);
        if (keep.length < t.length) {
          const nl = keep.lastIndexOf("\n");
          if (nl > budget / 2) keep = keep.slice(0, nl);
        }
        budget -= keep.length;
        content.push({ type: "text", text: keep });
      }
      content.push({
        type: "text",
        text: `\n[output truncated: showed ${MAX_CHARS.toLocaleString()} of ${total.toLocaleString()} characters. ` +
          "Don't list whole categories or files: look up the specific symbols you need " +
          "(node /kit/rag.mjs entry a b c, or node /kit/rag.mjs search \"<need>\", or grep -E for exact names).]",
      });
      log({ event: "truncated", tool: event.toolName, chars: total });
      return { content };
    });
  }

  if (COMPACT_AT > 0) {
    // The summary covers messages[1 .. cut) of the full history; the history
    // only grows within one run, so the indices stay valid.
    let summary = "";
    let cut = 1;
    let measuredFrom = 0;   // replies from this index on were made with the current view

    const view = (messages: Msg[]): Msg[] => {
      if (!summary) return messages;
      const first = messages[0];
      return [{ ...first, content: [...partsOf(first), { type: "text", text: SUMMARY_HEAD + summary }] },
              ...messages.slice(cut)];
    };

    pi.on("context", async (event: any, ctx: any) => {
      const messages: Msg[] = event.messages || [];
      if (messages.length < 3 || messages[0].role !== "user") return;
      let current = view(messages);
      const before = contextTokens(messages, current, measuredFrom);
      // The first message stays verbatim, so when it alone is near or over the
      // threshold (a very long item: one was 83k tokens) compacting at
      // COMPACT_AT would fold a sliver every few turns, and each fold changes
      // the first message, which voids the prompt cache for the whole 80k+.
      // Leave room for COMPACT_HEADROOM tokens of work above it instead.
      const threshold = Math.max(COMPACT_AT, tokens([messages[0]]) + COMPACT_HEADROOM);
      if (before <= threshold) return summary ? { messages: current } : undefined;

      // New cut: keep the latest KEEP_RECENT tokens, starting at an assistant
      // message (a tool result must stay with the call that produced it).
      let newCut = -1;
      let acc = 0;
      for (let i = messages.length - 1; i > cut; i--) {
        acc += tokens([messages[i]]);
        if (acc >= KEEP_RECENT) {
          for (let j = i; j < messages.length; j++) {
            if (messages[j].role === "assistant") { newCut = j; break; }
          }
          break;
        }
      }
      if (newCut <= cut) return summary ? { messages: current } : undefined;   // nothing old enough to fold

      const chunk = messages.slice(cut, newCut);
      let text = "";
      let usage: any = undefined;
      try {
        const response = await ctx.modelRegistry.complete(ctx.model, {
          messages: [{
            role: "user",
            content: [{
              type: "text",
              text: `${SUMMARY_PROMPT}\n\n${summary ? `<earlier-summary>\n${summary}\n</earlier-summary>\n\n` : ""}` +
                `<turns>\n${serialize(chunk)}\n</turns>`,
            }],
            timestamp: Date.now(),
          }],
        }, { maxTokens: 6000, signal: event.signal ?? ctx.signal });
        text = (response.content || []).filter((c: Part) => c.type === "text").map((c: Part) => c.text).join("\n").trim();
        usage = response.usage;
      } catch (e) {
        log({ event: "summary_failed", error: e instanceof Error ? e.message : String(e) });
      }
      if (!text) {
        // no model summary: keep a list of the actions taken, so lookups aren't repeated blindly
        text = (summary ? summary + "\n" : "") + chunk.flatMap((m) => m.role !== "assistant" ? [] : partsOf(m)
          .filter((p) => p.type === "toolCall")
          .map((p) => `- ran ${p.name}: ${JSON.stringify(p.arguments).slice(0, 300)}`)).join("\n");
      }
      summary = text;
      cut = newCut;
      measuredFrom = messages.length;
      current = view(messages);
      log({ event: "compacted", tokens_before: before, tokens_after: tokens(current), messages_folded: chunk.length,
            summary_chars: summary.length, usage });
      return { messages: current };
    });
  }
}
