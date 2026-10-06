# BrainCode Language Specification

**Version:** 0.1.0
**Status:** not yet bootstrapped — Sprint 0 will run automatically on the next invocation against this empty spec.

## Purpose

BrainCode is a formal syntax for expressing human agent-requests and agentic reasoning
(task decomposition) that is:

- **Expressive** — captures what natural language captures (negation, quantifiers, conditionals,
  temporal ordering, causal chains, multi-step dependency) without redundancy.
- **Broad-coverage** — generalizes to domains not seen during its own development.
- **Deterministic** — independent translators (different models, or repeated runs) converge on
  the same or equivalent expression for the same task.
- **Interpretable** — recoverable to plain-language intent by a human or LLM reader, given only
  the expression and this documentation.
- **Style-independent** — does not encode the linguistic idiosyncrasies of whichever model wrote
  it (e.g. "email my mom" vs. "email my professor" should differ in *content* the syntax
  captures — recipient, register — not in incidental phrasing).

This document is the frozen reference during any evaluation. Do not hand-edit it outside of a
sprint — use the orchestrator so `docs/changelog.md` and `docs/glossary.md` stay in sync.

## Foundations

*(To be filled in by Sprint 0 — the Searcher gathers structural notes on the inspiration
languages configured in `config.yaml -> run.bootstrap.inspiration_languages`, then the Shaper
proposes the initial basis.)*

## Constructs

*(No constructs accepted yet. Each accepted change appends or rewrites one section here: name,
grammar, semantics, one worked example, and a pointer to its `glossary.md` entry and the
sprint/changelog entry that introduced or last revised it.)*
