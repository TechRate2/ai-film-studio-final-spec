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


## Executable handoff and evidence currency
`governance/IMPLEMENTATION_HANDOFF.md` defines the implementation-root instruction bridge, pinned spec adoption, baseline environment decisions, task receipts and resume protocol. Root agent instructions must actually load; a spec directory's mere presence is not sufficient. TASK-002 verifies discovery and CI wiring. This is implementation governance, not authorization to execute application tasks during a specification audit.

Checkpoint commits may preserve PARTIAL/BLOCKED work and tests with explicit known failures; they are not acceptance or release. COMPLETE requires every criterion in the task packet (including prose acceptance requirements), prerequisite task/phase receipts and exact code/test evidence for the candidate implementation tree. Evidence must name its spec revision, implementation revision, environment, command/result and artifact/log. A changed relevant implementation invalidates prior proof; rerun affected checks before promotion. Never mark a skipped, unrun, fixture-only or unexplained failing real gate as passed. CI success on the spec alone proves no application behavior.

Do not weaken acceptance assertions, remove failing scenarios, disable checks or relabel critical requirements merely to pass. Legitimate test correction requires a stated erroneous expectation, canonical authority and review of the replacement's equivalent coverage. Independent review must inspect the actual diff and evidence; self-review is recorded honestly and is not described as another reviewer. Missing an explicitly required review blocks the corresponding gate. Instructions do not supersede platform access controls or authorize spending.
