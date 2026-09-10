# Canonical Manifest — V4.4.1

Required roots:
- `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `SPEC_VERSION`
- `spec/00_SPEC_LOCK.md` through `spec/47_SOURCE_VIDEO_LOCALIZATION.md`
- `schemas/` — normative structured contracts
- `profiles/`, `skills/`, `knowledge/filmcraft/`
- `phases/PHASE_0...PHASE_7`
- `governance/`
- `tasks/00_IMPLEMENTATION_ORDER.md`
- exactly 46 numbered `tasks/TASK_001...TASK_046` plus non-numbered provider/probe templates
- `evals/GOLDEN_SCENARIOS.md`, `evals/BENCHMARK_RUBRIC.md`
- `traceability/REQUIREMENTS_TRACEABILITY.csv`
- `evidence/`, `examples/`, `prompts/`
- `.github/workflows/spec-governance.yml`

Current canonical counts:
- canonical spec docs: **48** (`00`–`47`)
- numbered implementation task packets: **46**
- normative JSON schemas: **45**
- golden scenarios: **33**
- traceability requirements: **96**
- phase gate docs: **8**

Git commit/tree identity is the immutable version anchor. No other repository is required to interpret this canonical spec. When adding/removing canonical contracts, update MANIFEST + SPEC_VERSION + CI in the same change.

## Machine-readable count mirror
```text
SPEC_DOC_COUNT=48
TASK_COUNT=46
SCHEMA_COUNT=45
GOLDEN_SCENARIO_COUNT=33
TRACEABILITY_REQUIREMENT_COUNT=96
PHASE_COUNT=8
```

`governance/contract_index.json` maps task reads, dependencies, requirements and invariant comparisons. `schemas/common.schema.json` contains shared values. `governance/validate_spec.py` validates offline; `governance/test_validate_spec.py` proves negative mutations are rejected. `evals/contract_fixtures.json` contains specification fixtures only. Audit report/inventory/issue matrix are evidence, not parallel product contracts. Total repository file count is inventoried in the audit, not a permanently frozen product constraint.
