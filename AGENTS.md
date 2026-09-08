# AGENTS.md — Mandatory Contract for Coding Agents

This repository is the canonical product/build contract. Read this before touching implementation code.

## Authority
1. `spec/00_SPEC_LOCK.md`
2. canonical `/spec`
3. normative `/schemas`
4. accepted ADRs
5. active task packet
6. implementation code
7. comments/ad-hoc suggestions

If implementation and canonical spec conflict, report the conflict; do not silently redefine the product.

## Mandatory task bootstrap
1. Identify exactly one active `TASK-___`.
2. Read `SPEC_LOCK` and `governance/AI_CODING_PROTOCOL.md`.
3. Read the task packet and only its linked specs/schemas/playbooks.
4. Inspect actual repository files/symbols/tests/runtime.
5. Produce current-reality vs required-behavior map before edits.
6. Implement the smallest complete vertical capability.

## Forbidden
- niche-specific hard-coded pipelines as product architecture;
- multiple competing Director brains;
- provider quirks inside Generalist Director reasoning;
- treating chat history as Project Canon;
- full-series/full-spec context dumps by default;
- mandatory keyframes/storyboards for every shot;
- dependent paid shots generated concurrently before parent acceptance;
- silent capability downgrade;
- automatic new paid media generation after quality rejection;
- blind resubmission after uncertain provider timeout;
- overwriting accepted/historical shot versions;
- broad downstream regeneration when selective staleness is sufficient;
- production fake/mock output fallback;
- marking tasks complete without acceptance evidence.

## Required boundaries
- ModelProfile ≠ ProviderProfile.
- UniversalVideoSpec sits before model-specific compiler.
- Provider adapter owns transport, not creative logic.
- PaidAttemptGuard owns spend/approval/idempotency/reconciliation.
- Project Canon owns long-form/series truth.
- Continuity Baton carries accepted observed output state.
- Contextual revisions create new versions and use Continuity Sandwich when neighboring accepted shots exist.

## Engineering quality
Use typed contracts, explicit state transitions, migrations, structured errors, provenance, observability, cancellation/resume and tests. UI/backend capability is developed vertically where user interaction exists.

## Completion
Run applicable typecheck/lint/unit/integration/contract/golden tests. Update traceability with exact implementation/test refs. Use `PARTIAL`/`BLOCKED` instead of claiming success when evidence is missing.

## Architecture change
Follow `governance/CANONICAL_CHANGE_POLICY.md`. Class C canonical changes require explicit owner approval before implementation.
