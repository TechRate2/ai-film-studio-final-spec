# GS04 Walkthrough — 120s Saturn Sci‑Fi Film

## User input
> Làm phim ngắn 2 phút về một phi hành gia lần đầu tiến sát Sao Thổ. Chân thật như phim điện ảnh, cô độc nhưng hùng vĩ, có biến cố nhỏ cuối phim, thoại tiếng Việt.

Optional user refs: character, spacecraft, cockpit, camera reference, voice reference.

## 1. Scope/Content
`scope=LONG_SINGLE`, `content_mode=VISUAL_FILM` (drama is a retrieved grammar), `duration=120s`, `language=vi-VN`, `continuity=HIGH`, `research=factual + cinematography + model`.

## 2. Research
Create Fact Pack for Saturn visual/scientific anchors and Evidence Pack for cinematic scale/space-camera grammar/model prompting. Research must be distilled before creative writing.

## 3. Creative concept
Act 1: first approach.  
Act 2: awe becomes unease.  
Act 3: ring-debris navigation fault.  
Act 4: recovery + unexplained signal under rings.

## 4. Project state
Character: Commander Minh.  
Ship: Odyssey-7.  
Location: Saturn orbit.  
Voice: Vietnamese male, calm/restrained.  
Persistent locks: face, suit, ship design, cockpit architecture, lighting direction.

## 5. Example segment plan for Seedance 2.0 profile
Hypothetical timing sketch only: if an exact verified route permits a 15-second maximum, the following eight equal windows still require complexity/editorial justification. They are not a measured plan or a template for division; actual segments may have unequal lengths, shared generations or existing media. No current provider limit is asserted here.

1. 0–15 Hook/scale reveal
2. 15–30 cockpit arrival
3. 30–45 ring-plane awe
4. 45–60 anomaly discovery
5. 60–75 danger onset
6. 75–90 one readable evasive maneuver
7. 90–105 quiet recovery
8. 105–120 unknown signal cliffhanger

Dependency chain is sequential because visual/story state carries across the film.

## 6. Segment 1 UniversalVideoSpec excerpt
```text
GOAL: reveal overwhelming scale of Saturn.
SUBJECT: Odyssey-7; Commander Minh only faintly visible through canopy.
INITIAL: deep black space; Saturn partly outside frame.
PRIMARY CHANGE: ship advances while Saturn grows dominant.
END STATE: Saturn fills background; ship remains tiny foreground.
CAMERA: slow approach; no fast orbit/random rotation.
AUDIO: mechanical hum, quiet suit breathing.
DIALOGUE: “Tôi đã chờ khoảnh khắc này mười bảy năm.”
CONTINUITY OUT: ship intact; commander inside; approach vector and light direction stable.
```

## 7. Example Seedance 2.0 compiled prompt excerpt
```text
@image1 defines the exact Odyssey-7 spacecraft design.
@image2 defines Commander Minh's identity and flight suit.
Do not use the backgrounds from either reference.

Photoreal cinematic deep-space approach to Saturn, realistic scale, restrained lighting, physically plausible spacecraft reflections, deep black space, no colorful fantasy nebula.

Stage 1: Odyssey-7 is extremely small against Saturn's distant limb. It moves slowly forward. End state: Saturn dominates the background while Odyssey-7 remains small in foreground.
Stage 2: camera gently closes distance; rings reflect softly across canopy. End state: ship stays low-center with Saturn immense behind it.

Camera: very slow forward tracking, stable framing, no fast orbit, no aggressive zoom.
Audio: subtle spacecraft hum and quiet breathing.
Commander Minh says naturally in Vietnamese: “Tôi đã chờ khoảnh khắc này mười bảy năm.”
No subtitles. No text overlays.
```

## 8. After Segment 1
Run QA. If accepted, persist Continuity Baton: ship heading, commander position/suit, lighting, Saturn orientation, audio state, accepted last frame/video.

Segment 2 cannot start until Segment 1 is accepted because it depends on the accepted visual state.

## 9. Cost optimization
Selective keyframes only. Existing refs/previous accepted frame take priority. A mixed-media route may reduce fully generated seconds if it preserves intended quality. No quality failure triggers automatic paid regeneration.
