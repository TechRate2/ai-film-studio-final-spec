# TASK-042 — Security Backup Observability

## Goal
Harden production secrets/access, backups/restores, audit, metrics and spend incident controls.

## Read first
- `spec/23_SECURITY_PRIVACY_PROVENANCE.md`
- `spec/35_DEPLOYMENT_OPERATIONS.md`

## Acceptance criteria
- provider credentials encrypted/protected and absent from logs;
- project/media authorization enforced;
- structured paid-attempt audit trail;
- backup **and restore** tested;
- job/provider/cost observability correlated by IDs;
- ability to pause/disable paid provider route/spend;
- no private media leaked through public-by-default storage.
