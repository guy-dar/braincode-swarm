### S1 | type: add | dimension: vocabulary-member | symbol: national_id
- Needs: n3 (t1:s1)
- Searches tried: "social security numbers or unique identification" -> driver_license, credit_card, keys, dom_sgi; widen "social security number" -> driver_license, credit_card; entry driver_license -> motor vehicle credential
- Meaning: An official government-issued identification number or identity credential such as a social security number or national ID card.
- Category: entity-name
- Contextual aliases: ssn, social security number, national id, national ID, unique identification, government identifier
- Example: `TERM requirement(property="credential_type", value=national_id) -> requirement_id : TERM`
- Contrast: driver_license (specifically an authorization to operate motor vehicles) or credit_card (a financial payment card)
- Proposed record: {"symbol": "national_id", "kind": "value", "category": "entity-name", "definition": "An official government-issued unique identification number or national identity credential such as a social security number or national ID card.", "not": "driver_license (specifically an authorization to operate motor vehicles) or credit_card (a payment card)", "aliases": ["ssn", "social security number", "national identity", "national ID", "unique identification", "government identifier"]}

### S2 | type: add | dimension: constructor | symbol: verification_requirement
- Needs: n13 (t4:s4), n14 (t4:s5), n17 (t4:s10)
- Searches tried: "require email address verification", "two-factor authentication", "secondary confirmation codes"; widen "email address verification" -> send_email, format_email, address_form, validates_parameter; widen "two factor authentication" -> run_tests, check_reservation_availability, confirm, acknowledge
- Typed parameters: channel: STRING / TERM, stage?: STRING / TERM
- Interpretation: Constructs a descriptive account or identity verification requirement specifying the verification channel (such as email or two-factor code) and stage; describes a policy requirement, asserts nothing.
- Example: `TERM verification_requirement(channel="email_address", stage="pre_registration") -> verification_email : TERM`
- Proposed record: {"symbol": "verification_requirement", "kind": "constructor", "signature": "TERM verification_requirement(channel: STRING / TERM, stage?: STRING / TERM) -> TERM", "definition": "Constructs a descriptive representation of an account or identity verification requirement specifying the verification channel and stage.", "not": "validates_parameter (inspecting code parameter signatures) or send_email (an executed messaging action)", "aliases": ["verify_identity", "email_verification", "two_factor_auth", "2fa_requirement", "account_verification"]}
