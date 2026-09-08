# Implementation Governance

## Authority order
1. `spec/00_SPEC_LOCK.md`
2. canonical spec documents
3. normative JSON schemas
4. accepted ADRs
5. assigned task packet
6. implementation code
7. comments/ad-hoc suggestions

Lower layers may not silently contradict higher layers.

## Vertical capability rule
A capability is implemented through the complete path required by user behavior: persisted state → domain service → orchestration/job → API/event → UI/review surface → tests/provenance/observability. Avoid broad layers that leave users unable to exercise the feature.

## Repository reality rule
Before every task, inspect actual files, schemas, dependencies, tests and runtime. A spec describes desired behavior, not existing code. Never fabricate implementation status.

## Minimal-change rule
Preserve working architecture where compatible with canon. Refactor only when correctness or the assigned task requires it. Avoid speculative services, agents, flags and abstractions.

## ADR boundary
Implementation details may be chosen locally. Contract-affecting changes require ADR + review. Canonical behavior changes require explicit owner approval.

## Definition of implementation evidence
Task reports include exact files/symbols/migrations/API routes/tests and golden-scenario results. “Implemented” without inspectable evidence is invalid.

## Cross-agent workflow
Recommended: one model implements, another independently reviews. The second model receives the task/spec and diff, not only the first model's summary.
