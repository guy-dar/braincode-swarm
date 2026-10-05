### S1 | type: add | dimension: lexical-group | symbol: employment_field_label
- Needs: n3 (t1:s1).
- Searches tried: widen "IT jobs" and "employment field label information technology"; search "information technology employment vacancies" and "occupational field sector label" → rank_field, lexical_label, platform_label and unrelated roles; rank_field is a sorting field and platform_label denotes software systems rather than fields of employment.
- Domain: Source-supplied employment-field labels; opaque occupational or professional domain designations, with no inferred skills, qualifications, taxonomy or abbreviation expansion.
- Admission: open_label.
- Key form: lower_word.
- Key aliases: {}.
- Consuming signatures: S2 `TERM job_postings(field?: ATOM[employment_field_label]) -> TERM`.
- Illustrative values: employment_field_label::it, employment_field_label::engineering, employment_field_label::healthcare.
- Positive example: `TERM job_postings(field=employment_field_label::it) -> job_postings_2 : TERM` describes listings in the source-labeled IT field.
- Negative example: employment_field_label::it does not imply a named software platform, a required clearance or knowledge of specific programming languages.
- Overlap analysis: object_label denotes object kinds, platform_label named software systems, and genre_label genres; none supplies an employment-field domain role.
- Signature refinements: No existing signature is widened; accept this group atomically with the new exact consumer signature in S2. It is not an admitted parameter elsewhere.
- Compatibility: Additive; existing groups and signatures remain unchanged. Preserve label-covered spans separately from resolved semantics; no it/informationtechnology alias is proposed.
- Proposed record: {"symbol":"employment_field_label","kind":"lexical_group","definition":"A source-supplied employment-field label; denotes the labeled occupational or professional domain without inferred taxonomy, skills, qualifications or abbreviation expansion.","group":{"examples":["employment_field_label::it","employment_field_label::engineering","employment_field_label::healthcare"]}}

### S2 | type: add | dimension: constructor | symbol: job_postings
- Needs: n3 (t1:s1).
- Searches tried: widen "IT jobs"; search "job postings constructor" and "information technology employment vacancies" → include, conjunction, decision, roles and tone_professional; none describes employment listings. subject requires an unaccepted job-kind descriptor and cannot supply this interpretation solely from an arbitrary STRING.
- Typed parameters: field?: ATOM[employment_field_label].
- Interpretation: A description of advertised employment opportunities, optionally restricted to a source-labeled employment field; no assertion of availability, suitability, qualifications, count or search completion.
- Example: `TERM job_postings(field=employment_field_label::it) -> job_postings_2 : TERM`.
- Proposed record: {"symbol":"job_postings","kind":"constructor","signature":"TERM job_postings(field?: ATOM[employment_field_label]) -> TERM","definition":"Describes advertised employment opportunities, optionally qualified by the supplied employment-field label. It does not assert availability, suitability, qualification requirements, a result count or a completed search.","not":"A particular employment contract, an application submission or a claim that a job was found.","aliases":[]}

### S3 | type: add | dimension: constructor | symbol: certificate_filter
- Needs: n5 (t1:s1).
- Searches tried: widen "Filter by Security clearance certificate"; search "security clearance certificate requirement" and "certificate filter credential" → requirement, driver_license, vehicle_allowance and reservation-state filters; they do not define selection by a named certificate category.
- Typed parameters: name: STRING, the exact source-supplied certificate/filter-option name, not a sentence or unnamed credential description.
- Interpretation: A catalog-selection constraint matching the named certificate option in the catalog's certificate facet. It neither specifies whether postings require or accept that credential beyond the source's filter semantics nor asserts anyone holds it; issuer, jurisdiction and level remain unspecified unless separately represented.
- Example: `TERM certificate_filter(name="Security clearance") -> certificate_filter_2 : TERM` preserves the explicitly named option under Certificates.
- Proposed record: {"symbol":"certificate_filter","kind":"constructor","signature":"TERM certificate_filter(name: STRING) -> TERM","definition":"A selection constraint matching the exact named option in a catalog's certificate facet; name is the source-supplied option or certificate name. It does not assert credential possession or infer issuer, jurisdiction, level or whether the catalog's matching rule means required versus accepted credentials.","not":"A claim of authorization to enter a facility, or a claim that a person is certified.","aliases":[]}

### S4 | type: add | dimension: constructor | symbol: catalog_query
- Needs: n2 (t1:s1), n4 (t1:s1); supplies the structured target for n1.
- Searches tried: widen "Browse or search job listings", "Filter job search results" and "catalog query action description with filtering criteria"; search "catalog query description criteria" and "activity search filter verb" → search_web, select_filter, apply_filters and activity; executable operations cannot be used as pure request targets in TRACE, and activity lacks a defined query/filter profile and scoped criteria list.
- Typed parameters: target: TERM, criteria?: LIST[TERM].
- Interpretation: Non-executing description of browsing/searching a catalog for entries of the described target kind, restricting the selected entries to satisfy each supplied selection criterion. Omitted criteria leave filtering unspecified; no ranking, results or particular UI procedure is implied.
- Example: `TERM catalog_query(target=job_postings_2, criteria=[certificate_filter_2]) -> catalog_query_2 : TERM`, used as the target of `CLAIM request` rather than RECORD.
- Proposed record: {"symbol":"catalog_query","kind":"constructor","signature":"TERM catalog_query(target: TERM, criteria?: LIST[TERM]) -> TERM","definition":"Describes browsing/searching a catalog for entries of the target kind, restricting selected entries by every supplied criterion; criteria must be selection-constraint terms. This constructs a non-executing action description and does not assert returned results, completed filtering, ranking or a particular UI procedure.","not":"The executable search_web operation, an observed search event or a claim that matching entries exist.","aliases":[]}
