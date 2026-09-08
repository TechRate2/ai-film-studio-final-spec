# ADR-0001 — Enforce the existing canonical product contract

Status: Accepted for specification hardening under the owner's explicit final-audit mission.
Date: 2026-09-08
Class: B — cross-module contract clarification preserving SPEC_LOCK.

## Context and authority
Base main commit: cf61168bfa8ce8303963f14fd9b45377d8690bfb. All 242 tracked files were read before edits. The pre-edit issue matrix identified conflicting durable job states, missing paid-authorization links/certainty, untyped provenance/timeline/creative contracts, insufficient task/evaluation coverage and unsupported MEASURED scope. Authority is spec/00_SPEC_LOCK.md, then canonical specs, schemas and task packets. The highest-level lock is unchanged.

## Decision
Maintain one canonical tree and stable TASK-001 through TASK-043 IDs. Advance SPEC_VERSION to 4.3 for stricter wire contracts. Resolve job vocabulary from spec/29, payment certainty from spec/44, and invariant enums from their canonical specs. Use one shared schema of value records; no additional runtime services or Director agents. Define atomic authorization/reservation/reconciliation, version-pinned continuity/revision and deterministic assembly semantics. Strengthen existing skill cards/filmcraft knowledge and lower-authority examples without introducing hardcoded genre pipelines. Preserve empirical uncertainty and prohibit routing unverified bundled profiles.

Make task prerequisites, reading, requirement/schema/Golden links and dangerous enum comparisons machine-checkable. Add offline validation and negative fixtures/mutations; application behavior remains the implementation team's test obligation. Move billable keyframes after TASK-032/TASK-033 and preflight QA before real video smoke. This enforces the existing paid-media invariant for every modality rather than weakening it to video only.

## Alternatives and trade-offs
Keeping permissive objects would minimize diff but permit incompatible implementations and false safety claims. Adding independent services/schemas for every conceptual subcomponent would inflate architecture without improving these boundaries. Changing SPEC_LOCK to match old schema/task shortcuts would violate the product. Chosen approach keeps existing documents and uses typed shared records, at the cost of larger schema diffs and explicit migration work for any preexisting consumer.

## Migration and adoption
This repository contains specification, not an implemented production database. Do not assume consumers are absent: TASK-001 inspects the actual implementation repository. Consumers of 4.2 must map old job states into the one canonical family with documented evidence, backfill authorization/provenance only from real records, and quarantine ambiguous paid attempts as UNKNOWN. Missing facts must not be invented to satisfy schema validation. Migrate persisted artifacts with preserved original snapshots; do not relabel an old incomplete provenance record as fully verified. Revalidate templates/profile YAML and compiler boundaries before enabling spend.

## Review and approval scope
The owner explicitly authorized the exhaustive audit and minimal corrections preserving existing product behavior. This ADR records that authorization; it does not claim a separate external architecture review, owner approval of application deployment, live provider qualification or a successful commercial release. No Class C change to SPEC_LOCK was necessary. Findings, exact changed paths, task coverage and verification are in evidence/FINAL_AUDIT_REPORT.md and evidence/AUDIT_ISSUE_MATRIX.csv. Future behavior changes still follow governance/CANONICAL_CHANGE_POLICY.md.
