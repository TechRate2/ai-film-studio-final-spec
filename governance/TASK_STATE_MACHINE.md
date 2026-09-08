# Canonical Task State Machine

`NOT_STARTED → REALITY_AUDITED → PLANNED → IMPLEMENTING → VERIFYING → REVIEW → COMPLETE`

Optional: `BLOCKED`, `PARTIAL`.

A task may not enter COMPLETE without acceptance evidence and traceability refs. `BLOCKED` must name the concrete missing external dependency/decision. `PARTIAL` is preferred when some acceptance criteria are unverified.

Do not have multiple coding agents concurrently modify overlapping canonical/domain surfaces without explicit branch ownership and merge order.
