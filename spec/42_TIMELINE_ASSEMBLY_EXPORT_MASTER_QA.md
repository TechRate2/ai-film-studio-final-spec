# Composition Timeline, Assembly and Final Master QA

## CompositionTimeline
Final editing is a deterministic artifact, not an opaque FFmpeg command. Persist:
- ordered video/image segments and accepted source versions;
- trims, speed/hold instructions and transitions;
- dialogue/ADR/narration tracks;
- ambience/SFX/music tracks and fades/ducking;
- subtitles/captions and language variant;
- graphics/text overlays where required;
- aspect/resolution/frame-rate/export target;
- edit decisions and compiler/export version.

## Assembly
FFmpeg/Remotion/media tools execute the timeline. Re-running the same accepted timeline should reproduce the same logical master absent nondeterministic codec details.

## FinalMaster QA
Before `COMPLETE`, verify where applicable:
- expected duration/aspect/resolution/frame rate/codec/container;
- no missing/duplicated shot ranges;
- no unintended black/frozen/corrupt frames;
- A/V synchronization and dialogue continuity;
- no missing/duplicated audio regions;
- loudness/peak policy appropriate to target;
- subtitle timing, legibility and safe-area bounds;
- language/voice/pronunciation variant matches requested output;
- output references only CURRENT/accepted artifacts;
- export checksum/provenance stored.

Deterministic post fixes may run automatically when they incur no new paid generative-media attempt and do not change creative intent. Any new paid media generation follows SpendAuthorization/repair policy.

## Deterministic time and track semantics
CompositionTimeline is immutable per version. All positions/ranges are integer ticks at positive ticks_per_second; FPS is a rational numerator/denominator. Intervals are half-open [start,end). Conversion to frame/sample positions uses a pinned compiler rounding policy. Each media clip pins artifact/version, source in/out, timeline start/duration, positive rational playback rate and optional hold. Holds explicitly freeze one source frame; no accidental freeze is accepted. Audio clips identify dialogue/ADR/narration/ambience/foley/SFX/music, gain, fades, language/speaker where applicable and an explicit ducking sidechain/envelope. J/L cuts use independent audio placement. Graphics/subtitles have timed cues, normalized safe-area bounds, style/font asset pins and language. Transitions name both clip IDs and overlap duration; handles must exist and overlap is intentional.
Validate unique clip IDs, positive ranges, source bounds, playback mapping, intended gaps/overlaps, ordered tracks/z-order, fade/duck bounds, fonts, aspect, resolution, frame rate, codecs, sample rate and channel layout before export. Missing media, stale/unaccepted source versions or unpinned dependencies block; never substitute an unrelated current version. Export pins a source manifest, timeline hash, compiler/exporter version and output checksum. Repeated execution must have equivalent logical frame/audio/cue placement; bit identity is required only if the codec/toolchain contract guarantees it.

## QA completion policy
FinalMaster QA records every applicable check, threshold/policy version, evidence and PASS/WARN/FAIL/UNKNOWN. Required integrity checks cannot be absent or UNKNOWN at completion; planned black/silence/holds are compared to their declared ranges rather than flagged indiscriminately. Validate actual output metadata, A/V sync, clipping/loudness, missing/duplicated regions, subtitle safe area and timing, language and pronunciation. Thresholds are explicit export/profile policy, not fabricated universal platform rules. Deterministic repair creates a new derivative/timeline/master version and reruns affected checks; it never rewrites accepted source bytes or spends new generation credits. Recheck current source pins atomically when publishing COMPLETE; edits during export stale the master.

Source in/out ticks use the timeline timebase after deterministic conversion from the probed media timebase. A clip playback span maps (source_out-source_in)/speed plus hold to duration_ticks within the declared rounding tolerance. Intentional gaps must name the relevant track/range; absent audio tracks mean a deliberately silent master only when the accepted audio intent and export policy agree.
