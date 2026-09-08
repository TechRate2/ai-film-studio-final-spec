# Independent Reviewer Prompt

Review implementation against canonical specs, not implementer intent.

Search specifically for: SPEC_LOCK violations, niche hardcoding, provider leakage, model/provider conflation, dependent-shot parallelism, hidden paid retry/duplicate billing risk, missing upstream reconciliation, context dumps instead of scoped retrieval, broken canon/knowledge logic, reference leakage, mandatory keyframes, shot-version overwrite, revision ignoring incoming/outgoing continuity, stale propagation bugs, UI/backend mismatch, missing cost preview/spend cap, mock/demo production fallback, race/idempotency issues and missing tests.

Output findings by severity with exact spec references and concrete remediation.
