# Canonical Manifest — V4.2

Required roots:
- `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `SPEC_VERSION`
- `spec/00_SPEC_LOCK.md` through `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md`
- `schemas/` — normative structured contracts
- `profiles/`, `skills/`, `knowledge/filmcraft/`
- `phases/PHASE_0...PHASE_6`
- `governance/`
- `tasks/00_IMPLEMENTATION_ORDER.md`
- exactly 43 numbered `tasks/TASK_001...TASK_043` plus non-numbered provider/probe templates
- `evals/GOLDEN_SCENARIOS.md`, `evals/BENCHMARK_RUBRIC.md`
- `traceability/REQUIREMENTS_TRACEABILITY.csv`
- `evidence/`, `examples/`, `prompts/`
- `.github/workflows/spec-governance.yml`

Current canonical counts:
- canonical spec docs: **47** (`00`–`46`)
- numbered implementation task packets: **43**
- normative JSON schemas: **42**
- golden scenarios: **25**
- traceability requirements: **78**
- phase gate docs: **7**

Git commit/tree identity is the immutable version anchor. No other repository is required to interpret this canonical spec. When adding/removing canonical contracts, update MANIFEST + SPEC_VERSION + CI in the same change.
