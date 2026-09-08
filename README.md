# AI Film Studio — Final Canonical Build Spec V4.2

**Status:** CANONICAL CANDIDATE under completeness audit  
**Repository role:** source of truth for Codex, Claude and human engineers  
**Product:** AI Creative Director + Autonomous Video Production Studio

This repository is deliberately **spec-first**. It is not application code. Its job is to stop long vibe-coding sessions from drifting, simplifying continuity/cost rules, hard-coding providers, over-generating media or quietly turning the product into a generic text-to-video wrapper.

## Product promise
A user gives one natural-language request plus any mix of images, videos, audio, documents, scripts and references. One visible **Generalist Director** understands the goal, detects short/long/series scope, researches only where evidence is worth the cost, builds creative/story/character/canon/continuity state, directs performance/camera/audio/editing, chooses the cheapest production strategy that meets quality, compiles model-specific prompts, runs replaceable providers, reviews results, supports user-directed shot revision and external/internal keyframes, assembles final media and preserves project state for future episodes.

The user should not need to understand model prompt syntax, keyframe theory, continuity graphs, provider quirks or retry mechanics. The global workspace supports **Vietnamese and English UI independently from the project's content/output language**.

## Mandatory reading order for coding agents
1. `AGENTS.md`
2. `spec/00_SPEC_LOCK.md`
3. `governance/AI_CODING_PROTOCOL.md`
4. assigned `tasks/TASK_...md`
5. only canonical specs/schemas referenced by that task
6. actual implementation repository reality

Do **not** read every document into every task context. Retrieval must be scoped.

## Authority order
`SPEC_LOCK` → canonical spec → normative schema → accepted ADR → task packet → implementation → comments/ad-hoc suggestions.

## Canonical map
- `/spec` — **47** canonical contracts (`00`–`46`)
- `/schemas` — **42** normative structured contracts
- `/profiles` — evidence-backed model/provider/image/voice knowledge; never product law
- `/skills` + `/knowledge/filmcraft` — retrieved creative/directing knowledge, not hard-coded pipelines
- `/phases` — **7** binding phase gates
- `/tasks` — **43** numbered vertical implementation packets + provider/probe templates
- `/evals` — **25** Golden Scenarios + benchmark rubric
- `/traceability` — **78** requirements mapped to implementation/test evidence
- `/evidence` — public evidence, verification status and completeness audit
- `/examples`, `/prompts`, `/governance`, `/.github` — walkthroughs, coding-agent bootstraps and enforcement

## Non-negotiable highlights
One Director behind provider-neutral ports; no niche-hardcoded architecture; evidence-first research with ROI/stop/freshness; Project Canon + scoped ActiveContextPack; StyleDNA/grammar/taste as lower-priority layers; validated refs/locks/lifetimes; all five selective keyframe sources; dependent shots sequential; canonical identity separate from observed continuity; UniversalVideoSpec → model compiler → provider adapter; EffectiveCapability rather than marketing claims; SpendAuthorization for planned first attempts; no automatic new paid generation after quality output; ambiguous submit reconciliation; contextual shot versioning/Continuity Sandwich; deterministic non-paid repair; CURRENT/STALE/MISSING/BLOCKED dependency semantics; real controlled voice route; CompositionTimeline + FinalMaster QA; VN/EN UI locale separate from output language; bounded Director/research/critic loops; rights/consent/deletion/backup/restore/spend incident controls; no production fake fallback.

## Critical execution-order correction
Task numbers are stable IDs, not naive numeric order. Before the first billable Seedance test, **TASK-032 Durable Jobs and TASK-033 SpendAuthorization/PaidAttemptGuard must pass**. TASK-024 full Smart Auto acceptance executes after TASK-028 ImageProvider port exists. See `tasks/00_IMPLEMENTATION_ORDER.md`.

## Development loop
`REALITY → GAP MAP → PLAN → IMPLEMENT VERTICALLY → TEST → GOLDEN → SPEC REVIEW → TRACEABILITY → COMMIT`.

Before modifying an existing codebase, run `TASK-001_REPOSITORY_REALITY_AUDIT.md`.

## Remaining intentional unknowns
Exact current behavior/pricing/exposure of Seedance 2.5 and future Wan/Vidu/Kling/Veo/image/voice providers is empirical. `UNKNOWN/PARTIAL` remains explicit until current docs/provider probes/benchmarks establish evidence.

See `evidence/COMPLETENESS_AUDIT_V4_2.md` and `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`.
