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
