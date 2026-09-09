# Phase 6 — Commercial Beta Release

## Goal
Release only when canonical behavior, paid safety, user data/rights and operational recovery are demonstrably correct.

## Exit gate
- all 28 CORE golden scenarios (GS01–GS28) pass at required deterministic/real-provider levels;
- critical CORE traceability requirements (R-001–R-088) have implementation + test refs;
- real Seedance end-to-end benchmark dates/providers documented;
- no unresolved critical SPEC_LOCK violation;
- backup restore and project/media deletion tested;
- provider callback/auth/security controls tested where used;
- identity/voice consent and source-rights handling represented;
- global/provider/user/project spend controls and paid queue kill switch tested;
- known model/provider limitations are explicit;
- no fake/demo production fallback.

Subsequent LOCALIZATION requirements R-089–R-096 / GS29–GS33 do not participate in this core gate. TASK-044 starts only after this gate passes. Shared-core regressions found later still block the affected release.
