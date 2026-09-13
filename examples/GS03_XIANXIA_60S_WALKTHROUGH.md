# GS03 Walkthrough — 60s Xianxia Episode 1

## User input
> Tập 1 phim tiên hiệp 60 giây. Lâm Uyên tỉnh dậy giữa môn phái bị hủy diệt, Tô Nghi xuất hiện, cuối tập sư phụ Huyền Tôn lộ diện và nói chính Lâm Uyên đã mở phong ấn. Điện ảnh Trung Hoa, thoại tiếng Việt, cliffhanger mạnh.

Refs may include three characters, sword, sect hall, camera-motion video and voice.

## 1. Scope
If user signals continuing episodes/recurring cast, `scope=SERIES`, `content_mode=DRAMA`, current episode 1.

## 2. Reference Intelligence
- Lâm Uyên → CHARACTER_IDENTITY/HARD_LOCK
- Tô Nghi → CHARACTER_IDENTITY/HARD_LOCK
- Huyền Tôn → CHARACTER_IDENTITY/HARD_LOCK
- sword → PROP_IDENTITY/HARD_LOCK
- sect hall → LOCATION
- sample video → CAMERA_REFERENCE/MOTION_ONLY; explicitly do not copy story/characters/location
- voice sample → VOICE_REFERENCE

## 3. Canon
Store world/faction/power-system, the hidden truth that Lâm Uyên is tied to the seal, and separate audience/character knowledge states.

## 4. Episode arc (illustrative beat windows, not generation boundaries)
0–15 catastrophe hook  
15–30 missing seal/mystery  
30–45 attack + master reveal  
45–60 truth accusation/cliffhanger

## 5. Blocking example for final segment
Huyền Tôn first looks at Lâm Uyên's sword, not his face. Lâm Uyên takes half a step forward. Huyền Tôn raises his eyes only before the reveal. Pause. Camera slowly pushes into Lâm Uyên reaction. Red seal appears beneath torn collar.

## 6. Illustrative prompt intent excerpt
This is desired creative intent, not a verified callable provider request or evidence of native Vietnamese dialogue support. Apply `spec/09_DIALOGUE_VOICE_LOCALIZATION.md`, `spec/14_UNIVERSAL_VIDEO_SPEC.md` and exact-route EffectiveCapability before compilation/submission. If native Vietnamese is UNKNOWN or insufficient, propose a qualified controlled-voice route with its complete incremental cost and any visible-mouth constraints. Never silently replace the requested dialogue language. Continuation wording must match the actual endpoint operation and parameters.

```text
Continue directly from the accepted previous segment.
No fighting now. The scene becomes still.

Stage 1: Huyền Tôn looks at the Azure Sword rather than Lâm Uyên's face. Lâm Uyên steps forward half a pace. Huyền Tôn pauses and studies Lâm Uyên, leaving the approved speech window clear.

Stage 2: Huyền Tôn raises his eyes as the accusation lands. Lâm Uyên does not answer. Camera slowly pushes toward his reaction. A faint red ancient seal becomes visible beneath the torn collar.

End state: extreme close-up of the glowing seal reflected in Lâm Uyên's eye.
Video prompt audio ownership: no intelligible native speech. Controlled voice is compiled separately. No native subtitles. Keep faces, outfits, injuries, sword and night lighting unchanged.
```

Approved controlled-voice lines (separate voice compiler input): “Con vẫn chưa hiểu sao?” and “Cửu U Phong Ấn... chính con đã mở.” Under studio-audio-v1, this explicit Vietnamese request stays Vietnamese and uses controlled voice. If the intended visible dialogue requires mouth match, the user selects a qualified costed sync route; otherwise an explicitly acknowledged ordinary-dub limitation is required. Do not silently change this scene into off-screen narration.

## 7. Episode commit
After final acceptance, commit: master alive, seal missing, accusation heard but not necessarily believed, outfit/injury state, sword ownership, destroyed hall and cliffhanger. Episode 2 retrieves this canon rather than re-reading entire chat history.
