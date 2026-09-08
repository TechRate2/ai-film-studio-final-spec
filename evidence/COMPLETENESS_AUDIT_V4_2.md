# V4.2 Completeness Audit

Date: 2026-09-08
Repository: `TechRate2/ai-film-studio-final-spec`

## Audit purpose
Check whether the canonical repo contains enough product law, data contracts, task gates and acceptance scenarios for Codex/Claude to implement the discussed AI Creative Director without silently simplifying important logic.

## Material gaps found in V4.1 and resolved in V4.2
1. Manifest schema count drift (manifest said 16 while repo already had 22) → exact count/CI enforcement.
2. PRODUCT_DEMO missing from canonical Content Mode → added and schema-enforced.
3. StyleDNA / Genre-Platform-Brand-Taste grammar layers not formalized → canonical spec + schema.
4. ResearchROIController / CreativeEvidenceGraph not formalized → spec + schemas + task acceptance.
5. ActiveContextPack lacked normative schema → added.
6. Character Knowledge schema lacked `wants`/`fears` → fixed.
7. GenerationPlan lacked sequential/parallel groups and ref overrides → fixed.
8. Asset ingestion/dedup/corrupt/external provenance under-specified → canonical ingestion spec/schema.
9. Smart Auto internal keyframe not forced by implementation task → Task 024 now covers all source routes and real ImageProvider port.
10. Controlled real VoiceProvider path not forced → Task 037 requirement.
11. CompositionTimeline/FinalMaster QA lacked normative contract → added.
12. SpendAuthorization semantics ambiguous → planned first attempts may run under user-approved cap; post-output paid retries remain user-directed.
13. Multi-candidate generation not bounded → default 1; >1 must be explicitly planned/costed.
14. Provider paid-state/fallback certainty under-specified → exact semantics added.
15. EffectiveCapability intersection not explicit enough → canonical contract/schema.
16. Paid Seedance task order unsafe → Durable Jobs + PaidAttemptGuard are now hard prerequisites to Task 030.
17. Rights/consent/deletion/webhook security too thin → expanded safety/rights/operations contract.
18. Traceability/golden coverage too coarse → 75 requirements + 25 golden scenarios.

## Remaining intentional unknowns
These are not architecture gaps and must be learned from current provider docs/probes/benchmarks:
- Seedance 2.5 exact provider/API behavior and prompt bias;
- current Wan/Vidu/Kling/Veo provider exposure/cost/reliability;
- exact best image/voice provider behavior/pricing;
- empirical audience/viral performance by niche/platform;
- production scaling numbers after beta load.

Because live web verification was unavailable during this audit, all time-sensitive non-Seedance model placeholders remain PARTIAL/UNVERIFIED. The architecture intentionally treats UNKNOWN as valid and requires Phase-5 probes rather than guessing.

## Freeze recommendation
After CI/structural checks pass, V4.2 is sufficient to start/continue implementation. Further paper architecture should occur only when a real benchmark, provider limitation, legal/policy requirement or beta outcome reveals a concrete gap.
