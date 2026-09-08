# Canonical Change Policy

## Classes
**A — Implementation detail:** no product behavior change; engineer may decide locally.  
**B — Contract-affecting:** API/schema/job-state change preserving canonical behavior; ADR + review required.  
**C — Canonical behavior:** changes SPEC_LOCK, user workflow, continuity, retry/cost, memory, provider separation or model semantics; explicit owner approval required before implementation.

## Required process for B/C
1. describe current constraint and concrete problem;
2. cite affected canonical docs/schemas/tasks/golden scenarios;
3. propose alternatives and trade-offs;
4. create ADR;
5. obtain required approval;
6. update spec/schema/traceability/tests before or with implementation;
7. never leave code and spec intentionally divergent.

Silently editing a canonical document to match already-written code is prohibited.
