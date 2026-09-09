# Model Benchmark Rubric

## Unit and scope
A sample is one pre-authorized candidate with exact model/version/provider/endpoint/account/region, input/spec/ref hashes, profile/compiler versions, settings, duration, upstream ID, raw output, cost and timestamp. Record failed/billed and rejected outputs; do not report only selected successes. Planned candidate_count defaults to one. New comparisons require explicit sample/cost authorization. No paid tests run in ordinary CI.

## Scenario coverage
Human realism, product fidelity, two-character dialogue, action causality, fantasy/VFX, camera function, multi-event long segment, identity/reference isolation, first/end state, continuation and native/controlled audio. Compare routes under matching purpose and constraints; do not extrapolate one scene to all genres.

## Anchored assessment
For each applicable dimension (prompt/semantic adherence, identity/product, performance/motion, camera/geography, continuity/end state, audio/language/pronunciation and timing): 0 = unusable or wrong requirement; 1 = major violation; 2 = usable only with material repair; 3 = meets declared acceptance with minor flaws; 4 = exceeds the declared target without violating constraints. Use NOT_APPLICABLE separately from UNKNOWN. Record evaluator identity/version, observable evidence/ranges and disagreements. Hard lock, rights, corrupt-media or material continuity failures veto acceptance regardless of mean score. An aesthetic average never overrides product truth.

Acceptance criteria are fixed before viewing samples. Human review is required for subjective/performance claims until evaluator calibration supports the exact scope. Do not equate model self-rating with empirical acceptance. Report accepted count/total, confidence interval method, sample count and uncertainty; a single sample is anecdotal and cannot establish a reliability ceiling. Controlled comparisons vary one material factor where practical; record confounders and dataset/reference differences otherwise.

## Economics
Persist all research/LLM/image/video/voice/compute costs separately. Generation cost_per_accepted_second = total billed generation cost including failed/rejected candidates divided by unique accepted usable source seconds for the evaluated scope. Zero/unknown accepted seconds yields null and an explicit reason, not zero cost. Do not count repeated timeline reuse twice. Report end-to-end project cost separately including non-generation costs. Record latency, queue time and failed task rate independently. Expected acceptance/cost uses scope-matched measurements only; unknown stays null.

## Promotion
Promote a claim only with exact route/version scope, inspected evidence, sample ledger and declared uncertainty. Keep conflicting samples, known failures and re-probe triggers. No fixed sample count proves every model behavior; justified sample design and precision are part of review. Provider/account changes invalidate applicable exposure and pricing while preserving historical evidence.


## Source-video localization extension (Phase 7)
Evaluate separately from generated-video acceptance. Record cost_per_accepted_localized_minute with source/target duration basis, total attempted/rejected spend, ASR/translation/separation/TTS/compute/storage breakdown and end-to-end latency. Imported minutes cannot improve generated cost_per_accepted_second.

For each exposed direction, voice and provider route, pin versions/entitlement/date, source rights, representative sample IDs and reviewer proficiency. Include clean/noisy speech, mixed language, silence, accented speech, names/numbers/negation, two-speaker turns, overlap, music-under-dialogue and long-form timing. Translation fidelity, speaker attribution, natural delivery and background preservation require source/target-competent human review, not merely back-translation or the same LLM grading itself. Do not call intelligible but emotionally flat speech performance-preserving.

Measure source transcription error separately from translation error; alignment boundary error separately from voice quality. Predeclare launch-specific quality thresholds, sample coverage and review procedure before selecting passing samples; report sample count and distribution, not one headline success rate. A severe factual/negation error, wrong speaker, rights violation, forbidden submission or unexplained missing range is release-blocking for the affected route. Subtitle reading density, line breaks, diacritics/script shaping, safe area, dubbing pace, clipping/loudness and source preservation use the versioned policy in spec/47. Numeric policy values must be justified on target viewing contexts before release, not invented as universal constants here.

Report unresolved difficult material honestly. No claim of perfect lip synchronization: this extension never changes mouths. Missing credentials/budget or human-language review leaves empirical proof BLOCKED. Tests use licensed fixtures; no paid calls in default CI.
