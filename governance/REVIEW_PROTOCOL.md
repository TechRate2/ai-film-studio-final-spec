# Independent Review Protocol

The reviewer evaluates implementation against canonical requirements, not against the implementer's explanation.

Search explicitly for:
- SPEC_LOCK violations;
- niche hardcoding or duplicate creative brains;
- provider leakage into Director;
- ModelProfile/ProviderProfile conflation;
- dependent-shot concurrency bugs;
- missing scoped canon retrieval;
- reference-role leakage;
- forced storyboard/keyframe generation;
- shot-version overwrite or broad downstream regeneration;
- missing Continuity Sandwich on revisions;
- silent paid retries / duplicate billing risk;
- missing cost preview/spend cap;
- artifact stale-propagation errors;
- UI/backend mismatch;
- fake/mock production paths;
- race/idempotency/cancellation gaps;
- tests that assert mocks rather than required behavior.

Classify findings: CRITICAL / HIGH / MEDIUM / LOW. CRITICAL canonical mismatch blocks task completion.
