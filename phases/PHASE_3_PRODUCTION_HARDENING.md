# Phase 3 — Production Hardening

## Goal
Prove the vertical slice remains correct under failure, restart, cancellation, stale-state and spend incidents.

## Failure-injection matrix
- process restart during provider polling;
- timeout before/after upstream task identity is known;
- duplicate callback/event delivery;
- provider outage/rate limit;
- user cancel before submit and after submit;
- spend cap reached mid-run;
- rejected parent shot blocks dependent child;
- accepted-version revert marks only affected dependents stale;
- external keyframe invalid/needs correction;
- voice provider failure while visual remains accepted;
- final export/transcode failure without regenerating source video.

## Exit gate
No failure path can silently duplicate a billable attempt, corrupt canon/version state, release a blocked dependent shot, or replace accepted media with fake fallback. Recovery is observable/actionable and durable.
