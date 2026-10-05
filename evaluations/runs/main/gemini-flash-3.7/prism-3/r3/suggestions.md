### S1 | type: add | dimension: constructor | symbol: identity_credential
- Needs: n3 (t1:s1)
- Searches tried: "social security numbers or unique identification" → dom_sgi, resource_sink, driver_license; widen "social security numbers or unique identification" --kind object → keys, foreigners; no general official/government identity credential constructor.
- Typed parameters: kind: STRING, issuer?: STRING / TERM
- Interpretation: Constructs a descriptive term for an official identity credential or government-issued identifier (e.g. 'ssn', 'national_id', 'passport'); describes, asserts nothing.
- Example: `TERM identity_credential(issuer="government", kind="ssn") -> identity_credential_2 : TERM`
- Proposed record: {"symbol": "identity_credential", "kind": "constructor", "signature": "TERM identity_credential(kind: STRING, issuer?: STRING / TERM) -> TERM", "definition": "Constructs a descriptive term for an official identity credential, identifier, or government-issued document. Describes the credential without asserting its possession or validity.", "not": "driver_license (specifically a motor vehicle license entity) or identity (a claim relation asserting persona names)", "aliases": ["government_id", "national_id", "ssn", "identification_number"]}

### S2 | type: add | dimension: constructor | symbol: account_verification
- Needs: n13 (t4:s4), n14 (t4:s5)
- Searches tried: "require email address verification before account creation or posting" → send_email (external email sending action), format_email (layout format); widen → address_form, open_page; no constructor for account-level identity or email verification policies.
- Typed parameters: method: STRING, stage?: STRING
- Interpretation: Constructs a descriptive term for an account verification requirement or mechanism (e.g. method='email', stage='account_creation'); describes, asserts nothing.
- Example: `TERM account_verification(method="email", stage="account_creation") -> account_verification_2 : TERM`
- Proposed record: {"symbol": "account_verification", "kind": "constructor", "signature": "TERM account_verification(method: STRING, stage?: STRING) -> TERM", "definition": "Constructs a descriptive term for an identity verification procedure required for account registration or platform access. Describes the verification mechanism without executing it.", "not": "send_email (an external action sending email messages) or validates_parameter (a code-level parameter inspection claim)", "aliases": ["email_verification", "verify_account", "account_validation"]}

### S3 | type: add | dimension: constructor | symbol: multi_factor_authentication
- Needs: n17 (t4:s10)
- Searches tried: "implement two-factor authentication requiring secondary confirmation codes" → run_tests, reconcile_code, modify_code; widen → check_reservation_availability, validates_parameter; no constructor for multi-factor authentication or secondary confirmation codes.
- Typed parameters: factor_type: STRING, secondary?: BOOL
- Interpretation: Constructs a descriptive term for a multi-factor or two-factor authentication requirement; describes, asserts nothing.
- Example: `TERM multi_factor_authentication(factor_type="sms_code", secondary=TRUE) -> multi_factor_authentication_2 : TERM`
- Proposed record: {"symbol": "multi_factor_authentication", "kind": "constructor", "signature": "TERM multi_factor_authentication(factor_type: STRING, secondary?: BOOL) -> TERM", "definition": "Constructs a descriptive term representing multi-factor or secondary authentication requirements for security access. Describes the security protocol without asserting its completion.", "not": "run_tests (an executable testing operation) or keys (a physical key entity)", "aliases": ["two_factor_authentication", "2fa", "mfa", "secondary_verification"]}
