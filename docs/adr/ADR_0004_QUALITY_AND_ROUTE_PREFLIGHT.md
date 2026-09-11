# ADR 0004 — Quality acceptance and route preflight

Status: ACCEPTED FOR SPECIFICATION. Version 4.4.2. Date 2026-09-11. Class B hardening under the owner's final audit authorization; existing product behavior is preserved.

## Problem and authority
Under spec/19 and TASK-034, critical QA failures cannot release accepted media. However, QAReport currently admits ACCEPTABLE with MAJOR/FATAL severity or a required FAIL/UNKNOWN check. ProductionStrategy also admits negative cost. Spec/14 requires faithful compilation, but does not explicitly test disagreements between prompt-implied operation and endpoint mode. Existing cheapest-sufficient routing needs total-route comparisons rather than isolated video prices.

## Decision
Enforce the QA contradiction veto in the existing schema; enforce nonnegative known route cost. Require policy-owned QA check completeness in the domain layer, explicit prompt/mode/parameter conformance, and complete-route cost comparison. Strengthen TASK-019/027/034 and GS03/10/14, preserving their requirement mappings. Refresh dated market/provider evidence without promoting measured capability or enabling any route.

## Alternatives and trade-offs
Schema-only validation cannot prove policy completeness or media quality; domain acceptance and empirical calibration remain required. Prose-only fixes leave incompatible objects admissible. A new judging agent, provider router or ranking schema duplicates existing responsibilities. Blanket auto-rejection of optional UNKNOWN checks would overconstrain harmless uncertainty. Therefore the veto targets severe results and required FAIL/UNKNOWN checks, while noncritical imperfections retain review policy.

## Consequences and verification
Previously contradictory QA objects must be rejected at write/acceptance boundaries; retain historical evidence and route it to review, never rewrite it as passed. No application data exists here and no migration is executed. Positive/negative fixtures and mutation tests prove contract enforcement; runtime tests must prove missing policy checks cannot be omitted or downgraded. No model-specific parameter is added to Director inputs. Paid retry remains OFF, candidate default remains one, and no application task is completed by this change.
