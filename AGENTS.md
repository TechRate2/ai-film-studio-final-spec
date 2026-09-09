# AGENTS.md — Mandatory Contract for Codex / Claude / Coding Agents

This repository is the canonical product/build contract. Read this before touching implementation code.

## Authority
1. `spec/00_SPEC_LOCK.md`
2. canonical `/spec`
3. normative `/schemas`
4. accepted ADRs
5. active numbered task packet
6. implementation code
7. comments/ad-hoc suggestions

If implementation and canonical spec conflict, report the conflict; do not silently redefine the product.

## Specification audit versus application implementation
When assigned a canonical specification audit/hardening mission, audit and repair this repository's contracts, knowledge, tasks, schemas and governance. Numbered TASK-001 through TASK-046 are future implementation packets to audit, not tasks to execute merely because the owner says to continue the specification mission. Absence of application code is expected here and does not block specification audit completion. Use a findings/coverage matrix and preserve implementation statuses until real implementation evidence exists. Do not request an implementation repository or begin application work unless the owner changes the task scope to building the product.

## Mandatory task bootstrap for application work
1. Identify exactly one active numbered `TASK-___`.
2. Read `SPEC_LOCK` and `governance/AI_CODING_PROTOCOL.md`.
3. Read the task packet and only its linked canonical docs/schemas/playbooks.
4. Inspect actual implementation files/symbols/tests/runtime.
5. Produce current-reality vs required-behavior gap map before edits.
6. Check prerequisites in `tasks/00_IMPLEMENTATION_ORDER.md`; task number alone does not imply execution permission.
7. Implement the smallest complete vertical capability.

## Forbidden
- niche-specific hard-coded pipelines as product architecture;
- multiple competing Director brains;
- concrete vendor SDK/transport inside Generalist Director reasoning;
- treating chat history as Project Canon;
- full-series/full-spec context dumps by default;
- mandatory keyframes/storyboards for every shot;
- dependent paid shots generated before parent acceptance;
- silent capability downgrade or assuming UNKNOWN capability;
- automatic new paid media generation after quality result/rejection;
- blind resubmission after uncertain provider timeout;
- hidden multi-candidate generation beyond authorization;
- overwriting accepted/historical shot versions;
- broad downstream regeneration when selective staleness is sufficient;
- bypassing rights/consent/provider-policy checks by switching provider;
- production fake/mock output fallback;
- marking tasks complete without acceptance evidence.

## Required boundaries
- Director depends on provider-neutral LLM/tool ports from its first implementation.
- ModelProfile ≠ ProviderProfile; runtime reasons from EffectiveCapability.
- UniversalVideoSpec sits before model-specific compiler.
- Provider adapter owns transport, not creative logic.
- SpendAuthorization + PaidAttemptGuard own cost/approval/idempotency/reconciliation.
- Project Canon owns long-form/series truth; ActiveContextPack scopes retrieval.
- Continuity Baton carries accepted observed output state; canonical refs remain identity truth.
- Contextual revisions create new versions and use Continuity Sandwich when neighboring accepted shots exist.
- CompositionTimeline is source of deterministic final assembly; FinalMaster requires QA.

## Paid safety prerequisite
No real billable image/video/voice/lip-sync/generative-repair/probe submission may occur until `TASK-032` and `TASK-033` pass. Confirmed recovery of the same upstream task is not a new generation; a new post-output paid attempt is user-directed.

## Engineering quality
Use typed contracts, explicit state transitions, migrations, structured errors, provenance, observability, authorization, cancellation/resume and tests. Develop UI/backend vertically where user interaction exists.

## Completion
Run applicable typecheck/lint/unit/integration/contract/golden tests. Update traceability with exact implementation/test refs. Use `PARTIAL`/`BLOCKED` instead of claiming success when evidence is missing. Critical release requirements cannot remain PARTIAL.

## Architecture change
Follow `governance/CANONICAL_CHANGE_POLICY.md`. Future Class C canonical changes require explicit owner approval before implementation.
