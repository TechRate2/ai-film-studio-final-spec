# ADR 0003 — Reproducible coding-agent handoff

Status: ACCEPTED FOR SPECIFICATION. Version 4.4.1. Date 2026-09-10. Class B clarification under the owner's final specification-hardening request. Product behavior and paid policy are unchanged.

## Problem
Root instruction discovery is not guaranteed when the canonical repository is embedded under a directory. A generic commit-only-after-acceptance rule conflicts with durable partial checkpoints. Existing reports need explicit environment, revision and complete-criterion proof to survive context resets without stale or fabricated completion.

## Decision and alternatives
Use one handoff guide linked by existing entrypoints, strengthen spec/26, TASK-002 and Phase 0, and machine-check mandatory bootstrap readings. Permit marked partial checkpoint commits while retaining acceptance gates. Reject copying all docs into every startup instruction (context waste), flattening the entire spec into generated summaries (authority drift), or creating a new orchestration service (unnecessary). Test existing templates rather than adding a second task vocabulary.

## Consequences and verification
The implementation repository must install root bridges, pin one canonical revision, supply stack-specific run/test commands, retain evidence and follow the existing task graph. No universal stack, model or deployment is imposed. Current schema/task/Golden counts remain unchanged. GS26 covers missing bridges, stale proof and partial-checkpoint recovery. New negative governance mutations prove required-read omissions are rejected. This specification change does not execute any application task, auto-approve external access or certify provider behavior.
