# Measured glossary reduction and migration boundaries

Base: glossary revision 14, 687 total records (685 live, 2 deprecated). Revised candidate: **661 records (659 live, 2 deprecated)**. The original reference files remain the historical authority and have not been edited.

## Exact changes

- Remove 34 standalone leaf-value records from the active candidate.
- Remove the currency-value category rule, now empty and without dependents.
- Add seven groups, one lexical_label constructor and one common rule.
- Net reduction: **26 records, 3.8%**. No removed value is kept as a deprecated row in the active candidate.
- Update precise consumer signatures, dependencies, glossary examples and canonical spellings. No implicit STRING/ATOM conversion or blanket acceptance in STRING fields is introduced.

| Replacement group | Removed value rows | Replacement storage |
|---|---:|---|
| animal_label | 4 | No member entries; examples only |
| color_label | 9 | No member entries; examples only |
| country | 7 | 7 pinned member definitions retained |
| currency | 6 | 6 pinned member definitions retained |
| food_label | 4 | No member entries; examples only |
| genre_label | 1 | No member entries; examples only |
| object_label | 3 | No member entries; examples only |

The removed nominal values are pillow, sofa, armchair; tomato, popcorn, potato, egg; cat, donkey, fish, tuna; genre_comedy; and nine color_* values other than color_pink. These **21 open-group values have no member records**. The candidate contains only ten illustrative open-group example spellings across the five groups, plus sparse key aliases. A fresh unlisted key such as color_label::ochre is admissible under the same rules; the migration map is not consulted.

The registered migrations cover six currencies and seven countries (Japan, Argentina, Mexico, Germany, Poland, China and United States). Their 13 published definitions remain inside group records. This consolidates top-level entries but does not eliminate semantic knowledge. No complete external country/currency standard is claimed.

The full removed-ID/replacement mapping is in migration-map.json, outside active vocabulary. It contains no duplicate definition inventory for open labels. Translators of new documents do not load this migration audit as a whitelist.

## Retained exceptions and why

| Entry/family | Reason retained |
|---|---|
| phone | Published sense and contextual aliases must not be replaced by guessed phone/cellphone/smartphone equivalence. |
| watch | Timepiece sense differs from an action or other uses of the same word. |
| material_memory_foam | A defined compound and material distinction; no automatic decomposition or one-word synonym is assumed. |
| color_pink | Existing recognition hints include distinct shade phrases. Retained for explicit review rather than silently collapsing those shades. |
| size_queen | Bedding size system is distinct from general sizes; numerical dimensions cannot be inferred. |
| dog | Existing aliases include canine, pup and puppy; distinctions need review before consolidating them. |
| resource_sink / resource_heater / resource_chiller | Abstract resource roles, not just named physical objects. |
| unit_percent and other semantic units | Numeric interpretation must stay defined. |
| role_adults | Participant role and contextual interpretation cannot become an unexplained name. |
| relationships, actions, constraints | Formal meaning-bearing vocabulary; open groups cannot replace it. |

The remaining 122 entity-name entries are not all claimed to be irreducible. This is a reviewed first reduction, not a maximal purge. Later glossary revisions can consolidate more families after resolving their aliases and consumer roles. The group-first policy prevents automatically adding another member row for each new nominal value.

## Semantic and type migration

Open-group migration preserves the nominal descriptor and source-supported domain role. It does not certify all English implications of the old gloss. A use that relied on further properties, ambiguous synonymy, or STRING comparisons must be retranslated with explicit semantics or flagged; it must not be blindly substituted. Food and animal groups are distinct: animal_label::tuna does not automatically denote a prepared food item. Each domain is supplied by the source, not inferred from the key.

The migrated pillow example now acquires object_label::pillow from object_label::sofa and places the REF on object_label::armchair. Identity still comes from acquisition. The source/destination signatures explicitly admit the relevant group. Other TERM consumers can receive a lexical_label term where their semantic role allows it; no universal atom cast is introduced.

## Size accounting

| File | Original bytes | Previous suggestion | Current bytes | vs original |
|---|---:|---:|---:|---:|
| language-spec.md | 37,701 | 51,352 | 40,529 | +7.5% |
| language-spec.compact.md | 34,197 | 46,948 | 39,273 | +14.8% |
| glossary.md | 139,055 | 144,612 | 132,426 | -4.8% |
| glossary.jsonl | 260,970 | 261,078 | 249,938 | -4.2% |

| Required input pair | Original bytes | Current bytes | Change |
|---|---:|---:|---:|
| full readable | 176,756 | 172,955 | -2.2% |
| compact readable | 173,252 | 171,699 | -0.9% |
| full machine | 298,671 | 290,467 | -2.7% |
| compact machine | 295,167 | 289,211 | -2.0% |

These are actual UTF-8 bytes, including registered member definitions. Use one complete glossary view and one spec variant. Historical notes and offline migration audits supply no extra admission rules and are not required input for fresh translation. The new grammar still adds specification text, but every combined spec/glossary pair is smaller than the original. This is byte reduction, not an estimated token or quality improvement.

Compaction uses shared group defaults, derives consumers from signatures, renders registries as tables, and removes duplicate explanations from shared glossary rules. No additional value definitions were removed to improve these size figures. Migration limitations above remain unchanged.

## Adoption

Implement group-aware grammar, types, schema validation, retrieval and atomic migrations once. Thereafter, ordinary group additions and refinements are glossary-only changes. Freeze each batch's glossary revision. Preserve the original release for historical documents; retry affected translations against this candidate rather than silently reinterpreting them. Measure reconstruction, ambiguity, label-only coverage and cross-translator convergence alongside record counts and total bytes.
