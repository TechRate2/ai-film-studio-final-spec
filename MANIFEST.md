# Canonical Manifest — V4.3.1

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
- normative JSON schemas: **43**
- golden scenarios: **28**
- traceability requirements: **88**
- phase gate docs: **7**

Git commit/tree identity is the immutable version anchor. No other repository is required to interpret this canonical spec. When adding/removing canonical contracts, update MANIFEST + SPEC_VERSION + CI in the same change.

## Machine-readable count mirror
```text
SPEC_DOC_COUNT=47
TASK_COUNT=43
SCHEMA_COUNT=43
GOLDEN_SCENARIO_COUNT=28
TRACEABILITY_REQUIREMENT_COUNT=88
PHASE_COUNT=7
```

`governance/contract_index.json` maps task reads, dependencies, requirements and invariant comparisons. `schemas/common.schema.json` is the 43rd schema and contains shared values. `governance/validate_spec.py` validates offline; `governance/test_validate_spec.py` proves negative mutations are rejected. `evals/contract_fixtures.json` contains specification fixtures only. Audit report/inventory/issue matrix are evidence, not parallel product contracts. Total repository file count is inventoried in the audit, not a permanently frozen product constraint.
