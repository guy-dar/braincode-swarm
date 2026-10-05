### S1 | type: add | dimension: constructor | symbol: job_search
- Needs: n2 (t1:s1), n3 (t1:s1)
- Searches tried: widen “Browse or search job listings in a user request represented in TRACE, without claiming search was executed” → `search_web` and related search operations; search “job posting employment vacancy occupational category information technology jobs” → `search_web`; `search_web` is an executable Action and cannot represent unexecuted requested work in TRACE. Existing `activity` can describe an action but does not give the request a stable job-search structure.
- Typed parameters: domain: STRING
- Interpretation: A TERM describing a request to search job listings in the specified domain; it does not execute a search or assert that listings were found. The domain preserves the supplied search phrase.
- Example: `TERM job_search(domain="IT jobs") -> job_search_2 : TERM`
- Contrast: Not a completed web search (use `search_web` in REQUEST or RECORD an observed operation in TRACE).
- Proposed record: {"symbol":"job_search","kind":"constructor","signature":"TERM job_search(domain: STRING) -> TERM","definition":"Describes a request to search job listings in the specified domain. It does not execute a search or assert that listings were found.","not":"a completed web search operation","aliases":[]}

### S2 | type: add | dimension: constructor | symbol: job_posting_filter
- Needs: n4 (t1:s1), n5 (t1:s1)
- Searches tried: widen “Filter job search results in the user's requested behavior, not as a falsely recorded completed operation” → `select_filter`, `apply_filters`, `search_web`; widen “A requested Security clearance certificate filter criterion for job postings” → `select_filter`, `requirement`, `driver_license`; `select_filter`/`apply_filters` are operations, and `requirement` alone does not define filtering job postings by the named credential. The driver-license entry is a different credential.
- Typed parameters: criterion: STRING
- Interpretation: A TERM describing a request to filter job postings according to the named criterion; it does not execute the filtering or claim any posting satisfies it. The criterion retains the source-supplied credential label without inferring credential properties.
- Example: `TERM job_posting_filter(criterion="Security clearance certificate") -> job_posting_filter_2 : TERM`
- Contrast: Not a claim that a job posting requires or possesses the credential, and not an observed completed filter action.
- Proposed record: {"symbol":"job_posting_filter","kind":"constructor","signature":"TERM job_posting_filter(criterion: STRING) -> TERM","definition":"Describes a request to filter job postings according to the named criterion. It does not execute the filtering or claim any posting satisfies it.","not":"a claim that a posting requires or possesses the credential, or a completed filter operation","aliases":[]}
