# Traceability

`REQUIREMENTS_TRACEABILITY.csv` is a living implementation ledger. A requirement becomes `IMPLEMENTED` only when implementation refs and test refs are populated. `PARTIAL` is preferred over false completion.

The schemas column names applicable normative contracts; common value schemas may be reached transitively. The critical column makes release gating explicit. A task's Binding execution and verification packet lists exact requirements, Golden coverage, reads and conservative dependencies; governance/contract_index.json mirrors these for validation. Specification fixture success is not implementation evidence. Keep status NOT_STARTED until application/report implementation evidence actually exists; schema edits do not implement a feature.

release_gate is CORE or LOCALIZATION. IDs are pinned by governance/contract_index.json; CORE is R-001–R-088 and GS01–GS28, LOCALIZATION is R-089–R-096 and GS29–GS33. The latter is a subsequent Phase 7 capability, not a core release prerequisite. Shared regressions remain blocking. Keep both gate statuses NOT_STARTED until implementation evidence exists.
