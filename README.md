# AI Film Studio — Final Canonical Build Spec V4.1

**Status:** CANONICAL BUILD CONTRACT  
**Repository role:** source of truth for Codex, Claude and human engineers  
**Product:** AI Creative Director + Autonomous Video Production Studio

This repository is deliberately **spec-first**. It is not application code. Its job is to prevent AI coding agents from drifting, simplifying, hard-coding providers, skipping continuity/cost rules, or inventing a different product during long vibe-coding sessions.

## Product promise
A user gives one natural-language request plus any mix of images, videos, audio, documents, scripts and references. One visible **Generalist Director** understands the goal, detects short/long/series scope, researches where evidence matters, builds story/canon/character/continuity state, directs performance/camera/audio/editing, chooses the cheapest production strategy that meets quality, compiles model-specific prompts, runs replaceable providers, reviews results, supports user-directed shot revision, assembles final media and preserves project state for future episodes.

The user should not need to understand model prompt syntax, keyframe theory, continuity graphs or provider quirks.

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

Lower levels may never silently contradict higher levels.

## Repository map
- `/spec` — canonical behavior and implementation contracts (`00`–`38`)
- `/schemas` — normative structured data contracts
- `/profiles` — evidence-backed model/provider knowledge; never product law
- `/skills` — dynamically retrieved creative/production skills
- `/knowledge/filmcraft` — directing/story/edit/audio knowledge
- `/phases` — phase gates; no phase skipping without satisfying exit criteria
- `/tasks` — 43 vertical implementation packets
- `/evals` — 15 golden scenarios + benchmark rubric
- `/traceability` — requirement → task → implementation → test ledger
- `/evidence` — public evidence, confidence and freshness boundaries
- `/examples` — end-to-end walkthroughs
- `/prompts` — Codex/Claude implementer/reviewer/audit bootstraps
- `/governance` — strict vibe-coding protocol and canonical change policy
- `/.github` — PR/issue templates + spec governance CI

## Non-negotiable system rules
- one visible Generalist Director;
- no niche-hardcoded architecture;
- short/long/series share one brain with adaptive depth;
- evidence-first research when material;
- Project Canon, not chat history, is story truth;
- scoped context retrieval;
- explicit reference roles/locks/lifetimes;
- selective keyframes, including external/user-generated keyframes;
- dependent shots sequential, independent branches may parallelize;
- previous accepted real output carries continuity forward;
- ModelProfile and ProviderProfile are different concepts;
- provider-specific prompt behavior belongs in compilers/profiles;
- no automatic paid media regeneration after quality failure;
- user revisions create new versions and preserve originals;
- middle-shot revision uses Continuity Sandwich;
- artifacts use CURRENT/STALE/MISSING/BLOCKED;
- cost estimated before paid calls; spend caps enforced;
- duplicate paid submission prevented/reconciled;
- production paths have real adapters, never fake/demo fallback.

## How to develop with Codex/Claude
Never say “build the whole project.” Execute one task packet at a time:

`REALITY → PLAN → IMPLEMENT VERTICALLY → TEST → GOLDEN SCENARIO → SPEC REVIEW → TRACEABILITY → COMMIT`

Use a second model as independent reviewer where practical. The reviewer audits against canonical specs, not the implementer's intent.

## First implementation action
Before modifying an existing codebase, run `TASK-001_REPOSITORY_REALITY_AUDIT.md`. No broad refactor or production coding is allowed before the reality report identifies what actually exists.

## Definition of done
A capability is complete only when applicable persistence, domain logic, API, UI, error handling, provenance, cost behavior, tests, golden scenarios and traceability all pass. See `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`.
