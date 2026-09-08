# AI Film Studio — Final Canonical Build Spec V4.2

**Status:** CANONICAL CANDIDATE under completeness audit  
**Repository role:** source of truth for Codex, Claude and human engineers  
**Product:** AI Creative Director + Autonomous Video Production Studio

This repository is deliberately **spec-first**. It is not application code. Its job is to stop long vibe-coding sessions from drifting, simplifying continuity/cost rules, hard-coding providers, over-generating media or quietly turning the product into a generic text-to-video wrapper.

## Product promise
A user gives one natural-language request plus any mix of images, videos, audio, documents, scripts and references. One visible **Generalist Director** understands the goal, detects short/long/series scope, researches only where evidence is worth the cost, builds creative/story/character/canon/continuity state, directs performance/camera/audio/editing, chooses the cheapest production strategy that meets quality, compiles model-specific prompts, runs replaceable providers, reviews results, supports user-directed shot revision and external/internal keyframes, assembles final media and preserves project state for future episodes.

The user should not need to understand model prompt syntax, keyframe theory, continuity graphs, provider quirks or retry mechanics.

## Mandatory reading order for coding agents
1. `AGENTS.md`
2. `spec/00_SPEC_LOCK.md`
3. `governance/AI_CODING_PROTOCOL.md`
4. assigned numbered `tasks/TASK_...md`
5. only canonical specs/schemas referenced by that task
6. actual implementation repository reality

Do **not** read every document into every task context. Retrieval must be scoped.

## Authority order
`SPEC_LOCK` → canonical spec → normative schema → accepted ADR → task packet → implementation → comments/ad-hoc suggestions.

Lower levels may never silently contradict higher levels.

## Canonical map
- `/spec` — **47** canonical behavior/implementation contracts (`00`–`46`)
- `/schemas` — **42** normative structured contracts
- `/profiles` — evidence-backed model/provider/image/voice knowledge; never product law
- `/skills` — dynamically retrieved creative/platform/production skills
- `/knowledge/filmcraft` — directing/story/edit/audio knowledge
- `/phases` — **7** binding phase gates
- `/tasks` — **43** numbered vertical implementation packets + non-numbered provider/probe templates
- `/evals` — **25** Golden Scenarios + benchmark rubric
- `/traceability` — **75** requirements mapped to implementation/test evidence
- `/evidence` — public evidence, verification status and completeness audit
- `/examples` — end-to-end walkthroughs
- `/prompts` — Codex/Claude implementer/reviewer/audit bootstraps
- `/governance` — vibe-coding protocol, change policy and completeness checklist
- `/.github` — PR/issue templates + exact-count/schema-parse governance CI

## Non-negotiable behavior highlights
- one visible Generalist Director behind provider-neutral ports;
- no niche-hardcoded architecture;
- short/long/series share one brain with adaptive depth;
- evidence-first research with ROI/stop/freshness;
- Project Canon, not chat history, is story truth;
- scoped ActiveContextPack;
- StyleDNA/genre/platform/brand/taste are grammar layers, not pipelines;
- validated reference ingestion + explicit roles/locks/lifetimes;
- selective keyframes with AUTO_INTERNAL / EXTERNAL_ASSISTED / USER_SUPPLIED / PREVIOUS_ACCEPTED_FRAME / NONE;
- dependent shots sequential, independent branches may parallelize;
- accepted real output carries continuity while canonical refs remain identity truth;
- ModelProfile ≠ ProviderProfile; route through EffectiveCapability;
- UniversalVideoSpec → model compiler → provider adapter;
- user-approved SpendAuthorization covers planned first attempts so no per-shot confirmation spam;
- **no automatic new paid media generation after a quality result/rejection**;
- ambiguous submit reconciles before resubmit;
- shot revision creates a new version and uses Continuity Sandwich;
- deterministic non-paid repair is separate from paid regeneration;
- artifacts use CURRENT/STALE/MISSING/BLOCKED;
- CompositionTimeline + FinalMaster QA make export reproducible;
- rights/consent/source provenance, deletion, backup/restore and spend incident controls are production concerns;
- production paths have real adapters, never fake/demo fallback.

## Critical execution-order correction
Task numbers are stable IDs, not naive numeric execution. Before the first real billable Seedance task, **TASK-032 Durable Jobs and TASK-033 SpendAuthorization/PaidAttemptGuard must already pass**. See `tasks/00_IMPLEMENTATION_ORDER.md`.

## How to develop with Codex/Claude
Never say “build the whole project.” Execute one task packet at a time:

`REALITY → GAP MAP → PLAN → IMPLEMENT VERTICALLY → TEST → GOLDEN → SPEC REVIEW → TRACEABILITY → COMMIT`

Use a second model as independent reviewer where practical. Reviewer audits canonical behavior, not the implementer's intent.

## First implementation action
Before modifying an existing codebase, run `TASK-001_REPOSITORY_REALITY_AUDIT.md`. No broad refactor or production coding is allowed before the reality report identifies what actually exists.

## Remaining intentional unknowns
Exact current behavior/pricing/exposure of Seedance 2.5 and future Wan/Vidu/Kling/Veo/image/voice providers is not paper architecture. `UNKNOWN/PARTIAL` remains explicit until current docs/provider probes/benchmarks establish evidence.

## Definition of done
A capability is complete only when applicable persistence, domain logic, API, UI, error handling, provenance, cost behavior, tests, Golden Scenarios and traceability all pass. See `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`.
