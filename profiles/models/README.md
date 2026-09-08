# Model Profiles

Profiles are versioned evidence about model behavior, not marketing catalogs and not product-law defaults.

Statuses:
- `MEASURED`: evidence exists for stated scope;
- `PARTIAL`: some capability known, important behavior unknown;
- `UNVERIFIED`: do not route as if confirmed.

Provider exposure is stored separately. A new model version gets its own profile/probes; do not mutate an old profile into a different model identity.

All bundled profiles are currently non-routable evidence/template records. Values in an UNKNOWN claim are reported hypotheses, not runtime capability. Reading third-party measurements does not satisfy MEASURED promotion. Populate exact version and provider scope, inspectable samples and current price/entitlement before enabling a route. Family profiles never route directly. All model/image/voice YAML validates against schemas/model_profile.schema.json; provider YAML against schemas/provider_profile.schema.json. last_verified_at records verification of a stated source/claim, not a blanket warranty of provider availability. Empty failure lists mean no recorded samples, not no failures.
