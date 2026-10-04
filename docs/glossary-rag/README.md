# Compact glossary and future RAG design

Status: format experiment and implementation design, not a working RAG service. No language meanings, approvals, or existing kit files are changed.

## 1. What was compressed and verified

`glossary-compact.txt` is a full-content model-facing view of the current `../glossary-migrated.md`. Tables become tab-separated rows with one header per table. Markdown table delimiters, padding and separator rows disappear. All cell text, ordering, headings, prose, qualifications, original status labels and code examples are retained. Tabs separate fields; line breaks separate records. Read each row under its most recent table header and section context.

Measured result: 57,859 to 54,055 UTF-8 bytes, a **6.57% reduction**. All 384 table data rows, including 252 source-inventory occurrences, are preserved. The 328 index keys include documentation/structural keys and are not a count of approved symbols. See `compression-report.json` for hashes and checks. `build_compact.py` regenerates and verifies the view.

This is modest compression: most source text conveys actual meaning. Token savings have NOT been measured; a tokenizer for the eventual translator model and a comprehension comparison are required. Smaller files are not automatically cheaper prompts. No definitions were shortened or aliases/caveats removed to manufacture a larger saving. The source is a draft, and formatting does not approve its vocabulary.

Do not minify prose, invent cryptic field abbreviations or replace readable text with compressed binary/base64. Storage compression saves disk/network bytes, not model context after decompression. Normalizing repeated category rules can reduce storage; the model still needs those rules when using member entries.

## 2. Recommended storage and authority

Use **typed JSON records, exported as JSONL** (one full record per line), with a JSON Schema. Use Markdown for the collaboratively edited/rendered glossary and compact plain text for model replies. JSONL is an exchange/indexing format; it is not a concurrently writable shared file.

Integrate with the redesign's single host writer and SQLite event store:

1. Preserve source Markdown and immutable approved releases.
2. Commit agent decisions as validated events and entry versions through the writer.
3. Produce the live Markdown and normalized records from the same committed revision; never permit unrelated edits to two competing definition sources.
4. Export immutable `items.jsonl`, `rules.jsonl`, `examples.jsonl` and `manifest.json` for indexing. The manifest identifies release, source hashes, schema/adapter version and index generation.
5. Build exact-name, lexical and vector indexes as replaceable derivatives. Embeddings and similarity scores are not definitions or evidence of approval.

Initial normalization must be reviewed and lossless at the content level. Preserve unparsed source blocks instead of dropping text or guessing typed semantics. Every source table cell/prose block must map to an item, rule, example or document-level note. Keep coverage mappings and hashes. If completeness of an item's rules/dependencies is unknown, label it unresolved and retrieve its entire source section plus ancestor contracts. Do not claim a complete semantic graph merely because extraction ran successfully.

## 3. General RAG item shape

`glossary-item.template.json` supplies the general shape. Its placeholders are documentation, not indexable language entries. Keep descriptive field names in storage. A record represents one stable entry at one version, not a random token-window chunk.

| Field group | Requirement |
|---|---|
| Identity | Stable ID, exact case-sensitive symbol, entry version, category and kind |
| Authority | Release membership, approval state, original migration status, documentation versions |
| Meaning | Definition, signature, constraints, expansion and contrasts; retain source wording |
| Shared context | Explicit global/category/spec rule IDs, inherited constraints and exceptions |
| Relations | Required dependencies separate from optional related entries and contrasts |
| Evidence | Examples/counterexamples, source spans and content hashes |
| Change history | New symbol versus modification, target version/hash, proposal/decision IDs |
| Search aids | Contextual aliases, multilingual hints, domains and search text; clearly non-authoritative |

Rules and examples are separate typed records with stable ID/version, approval state, complete text, scope and source references. A required rule reference is always resolved with the item; it is not an optional follow-up that a weak model must remember to request. Shared rules appear once per response bundle, with explicit applies-to IDs. Undefined/unreviewed structured fields stay null with extraction status, not invented values; null means unknown/not extracted, never "no constraint". Empty lists mean checked and none found only when extraction is marked reviewed.

Do not conflate `Retained`/`Adapted` migration labels with approval. Keep `needs_approval`, `editor_approved` and `approved` as distinct states from the redesign. Only entry versions present in the pinned approved release may be used as accepted vocabulary. A separate pending search supports suggestion deduplication. Existing-symbol amendments have their own pending candidate version and expected target hash; the accepted version is unchanged until publication.

### Search documents versus returned definitions

Build search text from the exact symbol, aliases, meaning, signature, restrictions, examples, contrasts and short source-derived category context. An index may have several search documents for a complex entry (meaning/example/contrast); each points back to the same item version. Search hits hydrate the complete canonical record and required context. Never return a free-standing chunk that contains a symbol but omits its restrictive paragraph.

Optional generated synonym/translation hints are stored separately, labeled as search aids and versioned/reviewed. They cannot overwrite definitions. Index original Hebrew queries with a tested multilingual representation, and optionally add an English paraphrase; do not discard the original. Hard category/domain filters are avoided unless certain, because cross-domain vocabulary may be essential.

## 4. Translator-facing tools

Expose a small host API. The translator requests meaning; the host handles fusion, expansion, versions and output limits.

```text
retrieve_glossary(release_id, needs[], context_refs[], budget_tokens, cursor?)
get_glossary_items(release_id, item_ids[], include_required_context=true)
browse_glossary_category(release_id, category_id, cursor?)
search_pending_suggestions(working_revision, needs[], target_entry_ids[])
```

A need contains `{need_id, source_turn_ids, source_spans, meaning, role, polarity, temporal_scope, alternatives, known_symbols}`. Roles include operation, entity, constraint, relation, speech-act and evidence-status. Optional fields are null when unknown. Evidence spans refer to immutable supplied conversation text; generated paraphrases remain retrieval aids.

The response contains release/index hashes, entry IDs/versions, definitions, required rules, source references, per-need matches, matched-by explanations, alternatives, missing dependencies, unresolved needs, pagination and `bundle_complete`. `bundle_complete` means the selected definitions and their required context were returned, NOT that all relevant language has been found. Never report semantic completeness from similarity scores. Return `index_ready=false` rather than silently searching an outdated release. Caches include release/index version, query, filter and rendering version.

Use a compact readable rendering for models:

```text
ENTRY <stable-id>@<version> | <symbol> | <kind> | <approval/release>
Meaning: <complete definition>
Form: <complete signature/expansion>
Constraints: <complete local restrictions>
Rules: <IDs of shared rules included below>
Contrast: <relevant neighboring meanings and counterexamples>
Source: <references>
```

Do not put embeddings, audit logs or repeated field metadata into every prompt. Keep provenance accessible and show enough status/version data to prevent confusion. Drop optional hits before required rules; if the minimum complete bundle exceeds budget, return an explicit budget failure/continuation and process smaller need groups. Never trim the end of a definition to fit.

## 5. Algorithm: conversation to relevant glossary bundles

### A. Pin language and preserve conversation structure

Pin an approved release and matching complete index generation. Supply core grammar, scope, REQUEST/TRACE rules, reference binding, correction rules and status distinctions independently of search. Preserve the original conversation, speaker, turn IDs and task-versus-trajectory mode. Split long inputs along turns, preserving overlapping context and explicit references to earlier turns. A summary supplements original spans; it never replaces them.

### B. Build a source-linked needs ledger

Before translation, extract needs per turn: actions and objects, properties, quantities/units, negations, modality, conditions, temporal order, identity/coreference, speech acts, corrections, evidence/provenance and whether actions are requested or observed. Inspect every source turn and preserve ambiguous interpretations. Merge duplicate search needs for efficiency while retaining every source reference.

Do not use one embedding of the whole conversation as the only query. A dominant topic can hide a short but essential constraint. Resolve "it", "those", and corrections using their linked context for query construction, without overwriting earlier turns or inventing a referent.

### C. Retrieve candidates per need

For every need, run in parallel:

1. Exact ID/symbol lookup for explicitly known symbols; preserve case-sensitive identity.
2. Lexical/BM25 search over names, contextual aliases, definitions, restrictions and examples.
3. Semantic search over the same grounded content, using original text plus a concise contextual paraphrase where useful.

Union candidates and deduplicate by item ID/version. Fuse lexical and semantic ranks using reciprocal rank fusion, for example `sum(1 / (60 + rank))`; exact requested identities are retained regardless of fusion. This is a pilot parameter, not a relevance probability. Start experiments with 20 lexical and 20 semantic candidates per need, not one global top-3. Batch requests and cache repeated needs. Tune counts using measured recall, latency and model-token budgets.

### D. Rerank and resolve compatibility

Rerank candidates against the need AND its source context. Check meaning, negation, requested versus recorded action, types/arguments, constraints and temporal scope. Retain distinguishable alternatives for ambiguous needs rather than blindly selecting one. Reranking can use a dedicated ranker or a bounded model judgment; evaluate whether it helps before making it mandatory. A similarity match is not permission to use an incompatible symbol.

Preserve at least one candidate route for every need that had results; global top-K must not crowd out minor turns or constraints. Category restrictions are generally soft ranking hints, not filters. For a need that appears unsupported, search allowed compositions too, not only a hypothetical single primitive.

### E. Expand the required context

Fetch exact full entries and transitively resolve required dependencies, spec/category rules and expansions with visited-ID cycle handling. Include relevant contrast neighbors and scoped examples where they disambiguate use. Distinguish required edges from optional relatedness; do not recursively walk every similarity neighbor. Reject or mark missing/unapproved dependencies. If extraction is unresolved, fall back to full source sections and their inherited rules. The host must enforce this expansion; it should not depend on a weak model choosing extra tool calls.

### F. Translate and audit both directions

Construct a ledger from each source need to selected entry IDs, rules, expression and source turn. Translate using pinned approved entries. Then check (1) each used symbol has the correct exact definition and all mandatory restrictions and (2) each source meaning is represented, explicitly approximate, ambiguous or omitted. An identifier lookup alone checks vocabulary validity, not fidelity. Source-led auditing catches information omitted before any symbol was chosen.

### G. Widen before proposing additions

For unresolved needs, reformulate around the missing distinction, search synonyms and contrasts, widen categories, increase candidate breadth, then browse relevant categories. Search pending suggestions separately to reuse a proposal ID or suggest an amendment to an existing symbol. A pending match is never silently treated as approved vocabulary. Never infer "language has no expression" from a failed vector search.

Permit two widening passes initially, then report `retrieval_unresolved` if the source/meaning still cannot be assessed; do not call this proven absence. A glossary-addition proposal records the searches, entries and compositions considered. The stronger ordering agent uses full governing documentation to decide whether it is a true gap or a lookup failure. The budget is a stopping rule, not a completeness certificate.

### Example decomposition (illustrative; not new language definitions)

Conversation: "Find a hotel in Kyoto under 150 USD per night." Then: "Actually Osaka, and don't book anything; just show three options."

Search separately for accommodation search, location values, price/currency and per-night scope, correction of the earlier location, negated authorization to book, presentation and quantity. Preserve the first turn and its revision relationship. Do not retrieve only "Osaka hotel" or confuse searching with booking. If per-night pricing or the correction relationship cannot be represented with the supplied spec/glossary, expose the exact gap rather than dropping it. No symbol spelling is assumed by this example.

## 6. Index growth and simultaneous edits

Ordering agents approve new symbols and amendments through the existing writer. Index immutable entry versions incrementally, invalidate cached dependencies when shared rules change, and retain historical release membership. Separate the pending workspace index from approved release indexes. Build and verify a complete index manifest before advertising a release as RAG-ready; switch the release/index pair atomically. Existing jobs retain their pinned pair.

A deletion/redirect in a working proposal must not delete historical indexed versions. Exact getters resolve using the pinned release. Candidate evaluation uses an explicitly labeled candidate index, never an unlabeled mixture of pending and approved entries.

## 7. Evidence required before depending on RAG

Use the full-context compact glossary as the initial comparison baseline. Prepare reviewed conversations with required entries, valid alternative compositions, required rules and explicit source meanings. Include Hebrew/English paraphrases, rare terms, short constraints inside long turns, corrections, negation, ambiguous aliases, similar operations, multi-turn references and unapproved entries. Gold labels may allow several valid bundles, not just one spelling.

Measure required-entry/rule recall, dependency closure, per-need coverage, exact release/status accuracy, irrelevant-context burden, source-fidelity errors, token cost and latency. Compare full context, lexical only, semantic only, hybrid, and hybrid with expansion/reranking. A source-audit omission or wrong approval state matters even if average retrieval recall is high. Report confidence/variation across cases and translators; agree adoption thresholds before testing. No guarantee of "all relevant items" is available from top-K search alone.

Current work verifies format preservation only. No embeddings, tokenizer benchmark, relevance benchmark, model comprehension test, RAG backend or live tool integration was run.

## 8. Implementation sequence for Claude

1. Add a reviewed normalization adapter, item/rule/example schemas and source-to-record coverage checks. Preserve source blocks and status semantics. Validate schema and references.
2. Integrate deterministic exports with the glossary writer; serve exact versioned entries plus inherited context.
3. Add lexical and vector indexes behind one replaceable search interface; implement per-need hybrid retrieval, bundle expansion, explicit budget handling and trace logs.
4. Add the translator needs ledger, source audit, controlled widening and pending-suggestion lookup.
5. Benchmark against full context and only then enable RAG-dependent translation. Until then, retain the full-context default from the swarm plan.

## References for retrieval mechanisms

Rank fusion combines ranked result lists without treating incompatible scores as the same scale: [Elastic RRF documentation](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion). Lexical plus semantic retrieval, source context attached to chunks and reranking are supported retrieval patterns: [Anthropic contextual retrieval](https://www.anthropic.com/engineering/contextual-retrieval). These motivate candidate mechanisms; their reported results do not establish recall on BrainCode. The per-need ledger, required-rule expansion and adoption tests above are project-specific design recommendations.
