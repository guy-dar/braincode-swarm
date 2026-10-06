"""LanguageState: the loop's view of the living spec, glossary, backlog, and changelog under
docs/, plus the seed task pool. Every read/write to those files goes through here so the
orchestrator and roles never touch the filesystem directly.
"""
from __future__ import annotations

import json
import os
import random
import re
from dataclasses import dataclass
from datetime import date

_VERSION_RANK = {"MAJOR": 3, "MINOR": 2, "PATCH": 1}
_SPEC_PLACEHOLDER_RE = re.compile(r"\n?\*\(No constructs accepted yet\..*?\)\*\n?", re.DOTALL)
_GLOSSARY_PLACEHOLDER_RE = re.compile(r"\n?\*\(Empty — no constructs accepted yet\.\)\*\n?")
# Vocabulary categories (descriptive lexicon: actions, objects, attribute values, literal forms)
# live in their own section at the end of glossary.md, headed `### \`name\` (vocabulary)` so they
# never collide with a construct entry of the same name.
VOCAB_HEADING = "## Vocabulary"
_VOCAB_INTRO = (
    f"\n\n{VOCAB_HEADING}\n\n"
    "The descriptive lexicon: every category of symbol an expression may use besides the "
    "constructs above (actions, objects, roles, attributes and their allowed values, literal "
    "forms). Closed categories list every member; open categories list representative members "
    "plus the rule that defines membership.\n"
)
_VOCAB_SUFFIX = " (vocabulary)"


@dataclass
class Task:
    id: str
    nl: str
    domain: str
    split: str  # "dev" | "heldout"
    source: str = ""


class LanguageState:
    def __init__(self, docs_dir: str, seed_tasks_path: str, sources_path: str | None = None, random_seed: int = 42):
        self.docs_dir = docs_dir
        self.spec_path = os.path.join(docs_dir, "language-spec.md")
        self.glossary_path = os.path.join(docs_dir, "glossary.md")
        self.backlog_path = os.path.join(docs_dir, "backlog.md")
        self.changelog_path = os.path.join(docs_dir, "changelog.md")
        self.sources_path = sources_path

        self._rng = random.Random(random_seed)
        self.tasks_by_split: dict[str, list[Task]] = {"dev": [], "heldout": []}
        self._load_seed_tasks(seed_tasks_path)

        self.constructs: dict[str, dict] = {}  # in-memory mirror of accepted constructs this run, by name
        self.version = self._read_version()

    # ---------------------------------------------------------------- tasks
    def _load_seed_tasks(self, seed_tasks_path: str) -> None:
        with open(seed_tasks_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for split, key in (("dev", "dev_domains"), ("heldout", "heldout_domains")):
            for domain, items in data.get(key, {}).items():
                for item in items:
                    self.tasks_by_split[split].append(
                        Task(id=item["id"], nl=item["nl"], domain=domain, split=split, source=item.get("source", ""))
                    )

    def sample_task(self, split: str = "dev") -> Task:
        pool = self.tasks_by_split[split]
        if not pool:
            raise RuntimeError(f"No tasks available in split={split!r}; check seed_tasks.json")
        return self._rng.choice(pool)

    # -------------------------------------------------------------- version
    def _read_version(self) -> str:
        content = self._read(self.spec_path)
        m = re.search(r"\*\*Version:\*\*\s*(\d+\.\d+\.\d+)", content)
        return m.group(1) if m else "0.1.0"

    def bump_version(self, change_type: str) -> str:
        major, minor, patch = (int(x) for x in self.version.split("."))
        change_type = (change_type or "").upper()
        if change_type == "MAJOR":
            major, minor, patch = major + 1, 0, 0
        elif change_type == "MINOR":
            minor, patch = minor + 1, 0
        else:  # PATCH or unrecognized -> treat as patch, never silently no-op a real change
            patch += 1
        self.version = f"{major}.{minor}.{patch}"
        self._replace_in_file(self.spec_path, r"\*\*Version:\*\*\s*\d+\.\d+\.\d+", f"**Version:** {self.version}")
        return self.version

    def bump_version_for(self, change_types: list[str]) -> str:
        """One bump per accepted sprint, by the strongest change type in the set."""
        strongest = max((str(c or "").upper() for c in change_types), key=lambda c: _VERSION_RANK.get(c, 1), default="PATCH")
        return self.bump_version(strongest)

    # ---------------------------------------------------------------- io
    @staticmethod
    def _read(path: str) -> str:
        if not os.path.exists(path):
            return ""
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def _write(path: str, content: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    @classmethod
    def _replace_in_file(cls, path: str, pattern: str, replacement: str) -> None:
        content = cls._read(path)
        content = re.sub(pattern, replacement, content, count=1)
        cls._write(path, content)

    @staticmethod
    def _section_re(name: str, suffix: str = "") -> re.Pattern:
        return re.compile(rf"\n### `{re.escape(name)}`{re.escape(suffix)}\n.*?(?=\n### |\n## |\Z)", re.DOTALL)

    @classmethod
    def _upsert_section(cls, content: str, name: str, section: str, placeholder_re: re.Pattern | None,
                        suffix: str = "", before: str | None = None) -> str:
        """Replace the `### \\`name\\`` section (up to the next ### / ## heading or EOF) if it
        exists, else strip the empty-file placeholder and append — just before the `before`
        heading when that heading is present (so constructs stay ahead of the Vocabulary section)."""
        pattern = cls._section_re(name, suffix)
        if pattern.search(content):
            return pattern.sub(lambda _m: section, content, count=1)
        if placeholder_re is not None:
            content = placeholder_re.sub("\n", content, count=1)
        idx = content.find(f"\n{before}\n") if before else -1
        if idx != -1:
            return content[:idx].rstrip("\n") + "\n" + section + content[idx:]
        return content.rstrip("\n") + "\n" + section

    # ------------------------------------------------------------ mutators
    def upsert_construct_in_spec(self, construct: dict) -> None:
        name = construct["construct_name"]
        section = (
            f"\n### `{name}`\n\n"
            f"**Grammar:** `{construct['grammar']}`\n\n"
            f"**Semantics:** {construct['semantics']}\n\n"
            f"**Example:**\n"
            f"- NL: \"{construct['worked_example']['nl']}\"\n"
            f"- BrainCode: `{construct['worked_example']['braincode']}`\n\n"
            f"*Introduced/last revised: sprint {construct['sprint']}, version {self.version}*\n"
        )
        self._write(self.spec_path, self._upsert_section(self._read(self.spec_path), name, section, _SPEC_PLACEHOLDER_RE))
        self.constructs[name] = construct

    def upsert_glossary_entry(self, construct: dict) -> None:
        name = construct["construct_name"]
        entry = (
            f"\n### `{name}`\n\n"
            f"**Gloss:** {construct['glossary_gloss']}\n\n"
            f"**Example:**\n"
            f"- NL: \"{construct['worked_example']['nl']}\"\n"
            f"- BrainCode: `{construct['worked_example']['braincode']}`\n\n"
            f"**Introduced/last revised:** sprint {construct['sprint']}, see `changelog.md#sprint-{construct['sprint']}`\n"
        )
        self._write(self.glossary_path, self._upsert_section(
            self._read(self.glossary_path), name, entry, _GLOSSARY_PLACEHOLDER_RE, before=VOCAB_HEADING,
        ))

    def upsert_vocabulary_entry(self, entry: dict) -> None:
        """A `kind: "vocabulary"` change: one category of the descriptive lexicon, written under
        the glossary's Vocabulary section (created on first use). Never touches the spec."""
        name = entry["construct_name"]
        members = entry.get("members") or []
        member_lines = "\n".join(
            f"- `{m.get('symbol', '?')}` — {m.get('gloss', '')}"
            + (f" (natural-language synonyms: {', '.join(m['nl_synonyms'])})" if m.get("nl_synonyms") else "")
            for m in members if isinstance(m, dict)
        ) or "- (none listed — see membership rule)"
        closed = entry.get("closed", True)
        section = (
            f"\n### `{name}`{_VOCAB_SUFFIX}\n\n"
            f"**Gloss:** {entry['glossary_gloss']}\n\n"
            f"**Category:** {'closed — the members below are exhaustive' if closed else 'open — the members below are representative'}\n\n"
            f"**Members:**\n{member_lines}\n\n"
            + (f"**Membership rule:** {entry['membership_rule']}\n\n" if entry.get("membership_rule") else "")
            + f"**Example:**\n"
            f"- NL: \"{entry['worked_example']['nl']}\"\n"
            f"- BrainCode: `{entry['worked_example']['braincode']}`\n\n"
            f"**Introduced/last revised:** sprint {entry['sprint']}, see `changelog.md#sprint-{entry['sprint']}`\n"
        )
        content = self._read(self.glossary_path)
        if f"\n{VOCAB_HEADING}\n" not in content:
            content = content.rstrip("\n") + _VOCAB_INTRO
        self._write(self.glossary_path, self._upsert_section(content, name, section, None, suffix=_VOCAB_SUFFIX))

    def remove_vocabulary_entry(self, name: str) -> bool:
        content = self._read(self.glossary_path)
        new_content, n = self._section_re(name, _VOCAB_SUFFIX).subn("", content, count=1)
        if n:
            self._write(self.glossary_path, new_content)
        return bool(n)

    def vocabulary_section(self) -> str:
        """The glossary's Vocabulary section (heading to EOF), or "" if it doesn't exist yet."""
        content = self._read(self.glossary_path)
        idx = content.find(f"\n{VOCAB_HEADING}\n")
        return content[idx + 1:] if idx != -1 else ""

    def vocabulary_names(self) -> set[str]:
        return set(re.findall(rf"^### `([^`]+)`{re.escape(_VOCAB_SUFFIX)}$", self._read(self.glossary_path), re.MULTILINE))

    def remove_construct(self, name: str) -> bool:
        """Delete the `### <name>` section from both the spec and the glossary (op: remove).
        Returns True if the spec had it."""
        pattern = self._section_re(name)
        found = False
        for path in (self.spec_path, self.glossary_path):
            content = self._read(path)
            new_content, n = pattern.subn("", content, count=1)
            if n:
                self._write(path, new_content)
                found = found or path == self.spec_path
        self.constructs.pop(name, None)
        return found

    def append_changelog_entry(self, entry_md: str) -> None:
        with open(self.changelog_path, "a", encoding="utf-8") as f:
            f.write(entry_md)

    def update_last_cost(self, true_cost_usd: float) -> None:
        """Patch the most recently appended changelog entry's 'Cost this sprint' line with the
        true total. The Documenter writes a preliminary figure that excludes its own LLM call
        (that call's cost isn't known until after it returns), so the orchestrator calls this
        right after each Documenter write — one entry per attempt, patched immediately."""
        content = self._read(self.changelog_path)
        idx = content.rfind("- **Cost this sprint:**")
        if idx == -1:
            return
        line_end = content.find("\n", idx)
        if line_end == -1:
            line_end = len(content)
        content = content[:idx] + f"- **Cost this sprint:** ${true_cost_usd:.4f}" + content[line_end:]
        self._write(self.changelog_path, content)

    def append_backlog_row(self, row_md: str) -> None:
        with open(self.backlog_path, "a", encoding="utf-8") as f:
            f.write(row_md)

    def glossary_terms(self) -> set[str]:
        """Construct entries only — vocabulary categories are vocabulary_names()."""
        return set(re.findall(r"^### `([^`]+)`$", self._read(self.glossary_path), re.MULTILINE))

    def spec_construct_names(self) -> set[str]:
        return set(re.findall(r"^### `([^`]+)`", self._read(self.spec_path), re.MULTILINE))

    def last_sprint_number(self) -> int:
        """Highest sprint number already on record — changelog `## Sprint N` headers, a baseline
        import's `Continues from sprint: N` marker, and the spec's per-construct `sprint N,
        version` stamps — so a resumed or baseline-imported run continues numbering instead of
        restarting at Sprint 1."""
        changelog = self._read(self.changelog_path)
        numbers = [int(n) for n in re.findall(r"^## Sprint (\d+)", changelog, re.MULTILINE)]
        numbers += [int(n) for n in re.findall(r"\*\*Continues from sprint:\*\*\s*(\d+)", changelog)]
        numbers += [int(n) for n in re.findall(r"sprint (\d+), version", self._read(self.spec_path), re.IGNORECASE)]
        return max(numbers, default=0)

    # ------------------------------------------------------------ bootstrap
    def is_bootstrapped(self) -> bool:
        """True once Sprint 0 has written a basis into language-spec.md. Determined from the file
        itself (not in-memory state) so re-running against an existing docs/ skips Sprint 0."""
        content = self._read(self.spec_path)
        return bool(re.search(r"^### `", content, re.MULTILINE)) or "**Status:** bootstrapped" in content

    def set_foundations(self, overview_text: str) -> None:
        """Sprint 0: replace the placeholder '## Foundations' body with the Shaper's overview."""
        content = re.sub(
            r"(## Foundations\n\n)\*\(To be filled in.*?\)\*",
            lambda m: m.group(1) + overview_text,
            self._read(self.spec_path),
            count=1,
            flags=re.DOTALL,
        )
        self._write(self.spec_path, content)

    def replace_foundations(self, overview_text: str) -> None:
        """Later sprints: overwrite the whole '## Foundations' body (placeholder already gone)."""
        content = re.sub(
            r"(## Foundations\n\n).*?(?=\n## )",
            lambda m: m.group(1) + overview_text.rstrip("\n") + "\n",
            self._read(self.spec_path),
            count=1,
            flags=re.DOTALL,
        )
        self._write(self.spec_path, content)

    # -------------------------------------------------------------- sources
    def append_discovered_source(self, entry: dict) -> None:
        """Log a source the Searcher found in internet mode back into sources/previous_work.md,
        under a running, auto-appended section. No-op if sources_path wasn't configured."""
        if not self.sources_path or not os.path.exists(self.sources_path):
            return
        heading = "## Sources found during sprints (auto-logged)"
        content = self._read(self.sources_path)
        if heading not in content:
            content = content.rstrip() + f"\n\n{heading}\n\nEntries the Searcher found via live search (internet mode) and judged durable enough to keep. Not hand-curated — review periodically.\n"
        content = content.replace("\n*(Empty at seed.)*\n", "\n")
        name = entry.get("name", "untitled")
        link = entry.get("link", "")
        relevance = entry.get("relevance", "")
        content = content.rstrip() + f"\n- **{name}** — {link} — {relevance}\n"
        self._write(self.sources_path, content)

    @staticmethod
    def today() -> str:
        return date.today().isoformat()
