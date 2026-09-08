# TASK-013 — Creative Strategy, Retention and Style/Grammar

## Goal
Produce provider-neutral CreativeStrategy informed by audience, evidence, StyleDNA and only relevant grammar layers.

## Read first
- `spec/05_CREATIVE_STORY_RETENTION.md`
- `spec/39_STYLE_DNA_AND_GRAMMAR_LAYERS.md`
- `schemas/creative_strategy.schema.json`
- `schemas/style_dna.schema.json`
- `schemas/user_taste_profile.schema.json`

## Acceptance criteria
- different niches/platforms produce materially different mechanisms without niche-hardcoded pipeline branches;
- StyleDNA extracts transferable mechanisms and do-not-copy elements;
- Genre/Platform/Brand/UserTaste layers have explicit conflict precedence;
- retention does not force fast cuts universally;
- Creative Critic runs before paid media;
- critic/replan loop is bounded and exposes stop reason;
- user hard constraints/canon/product truth outrank style/taste heuristics;
- decision provenance available for major trade-offs.

## Binding execution and verification packet

Dependencies: TASK-012. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/05_CREATIVE_STORY_RETENTION.md`
- `spec/39_STYLE_DNA_AND_GRAMMAR_LAYERS.md`
- `schemas/creative_strategy.schema.json`
- `schemas/style_dna.schema.json`
- `schemas/user_taste_profile.schema.json`

Requirements: R-002, R-042, R-043, R-078.
Golden coverage: GS01, GS02, GS03, GS04, GS25.

- [ ] Produce an audience promise, beat question/change/payoff and camera/audio/performance rationale; compare at least restrained drama, factual explanation and product proof.
- [ ] Conflicting style/taste cannot override locks, canon, facts or brand hard rules; critic stop counts persist and generic positive scores cannot replace evidence.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
