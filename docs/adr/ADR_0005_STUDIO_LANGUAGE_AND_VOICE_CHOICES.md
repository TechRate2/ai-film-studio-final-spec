# ADR 0005 — Explicit Studio language and voice choices

Status: ACCEPTED FOR SPECIFICATION. Date: 2026-09-13. Contract version: 4.5.0. Class C product-default change explicitly requested by the owner in the current session; no application implementation or paid probe is authorized by this ADR.

## Current behavior and problem
Spec/09 separates UI, script, dialogue and subtitle languages and offers per-shot audio routing, but leaves new Studio defaults and UI/chat conflict resolution underspecified. The owner now requests a visible Chinese dialogue default independent of Vietnamese prompt text, English choice, controlled Vietnamese voice and optional user-selected lip sync, plus a later original-video translation workflow. Without a shared persisted choice, UI, compiler and cost planning can disagree or buy unwanted voice/sync operations.

## Decision
For new STUDIO speech with no explicit or inherited output language, propose visible zh-CN (Mandarin Chinese); do not add speech to a silent request. Explicit language instructions beat a product default. Conflicting explicit chat/UI/script locks need resolution before paid work. Preserve existing/series language; never apply new defaults to historical projects. Subtitle default is Off. The initial Vietnamese policy uses controlled voice (new TTS or valid imported speech), with additional lip-sync off until explicitly selected. Selecting Vietnamese shows the controlled-voice plan and cost; it never silently authorizes synthesis. Optional lip sync does not waive an explicit mouth-match requirement: an incompatible plan is blocked until changed or knowingly accepted as ordinary unsynchronized dubbing.

One typed studio_audio record in ProjectIntent carries the confirmed preference snapshot. No new service or Director. Per-line language variants and provider-neutral UV audio plans derive from it. Exact API/model/account capability and complete cost remain pre-spend gates. Chinese/English preference is not a measured capability declaration; future native-Vietnamese policy may be adopted explicitly after evidence, never by silently changing old projects.

## Alternatives and trade-offs
Matching interface/request language automatically conflicts with the owner's desired Chinese preset. Hard-forcing Chinese over explicit English/Vietnamese violates user intent. Always adding TTS/lip-sync wastes money. A permanent per-niche routing table prevents creative generalization. Chosen approach uses visible editable defaults, deterministic precedence, a constrained launch policy and context-driven cinematography. It adds a small audio preference record and more preflight tests, not a second workflow engine.

## Affected contracts and migration
Specs 09, 10, 14, 20, 30, 31, 45, 46; ProjectIntent schema; tasks 005/017/018/027/037/041 and integration qualification/handoff; GS03/11/13/17; existing traceability IDs and fixtures; existing filmcraft cards; README, manifest and SPEC_VERSION. Existing records without studio_audio remain readable but require evidence-based resolution before a new paid Studio plan. Do not backfill Chinese, invent consent, rewrite original scripts or invalidate historical accepted media merely because the policy changed. LOCALIZATION remains governed by spec/47 and has no video/image/lip-sync access. A user explicitly opens that workspace with a pinned accepted master; no automatic translation charges.

## Verification and evidence limits
Test record shape plus precedence, authorization, compiler language ownership, stale-version rejection and no-forbidden-call behavior. Domain tests own cross-record semantics; fixtures alone cannot prove language quality. Current public Topview skills and ByteDance examples inform bounded workflow/creative lessons, not a claim to have replicated a private agent or measured Seedance performance. Existing release gates and all NOT_STARTED implementation states remain binding.
