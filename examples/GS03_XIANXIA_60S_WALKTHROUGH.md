# GS03 Walkthrough — 60s Xianxia Episode 1

## User input
> Tập 1 phim tiên hiệp 60 giây. Lâm Uyên tỉnh dậy giữa môn phái bị hủy diệt, Tô Nghi xuất hiện, cuối tập sư phụ Huyền Tôn lộ diện và nói chính Lâm Uyên đã mở phong ấn. Điện ảnh Trung Hoa, thoại tiếng Việt, cliffhanger mạnh.

Refs may include three characters, sword, sect hall, camera-motion video and voice.

## 1. Scope
If user signals continuing episodes/recurring cast, `scope=SERIES`, `content_mode=DRAMA`, current episode 1.

## 2. Reference Intelligence
- Lâm Uyên → CHARACTER_IDENTITY/HARD
- Tô Nghi → CHARACTER_IDENTITY/HARD
- Huyền Tôn → CHARACTER_IDENTITY/HARD
- sword → PROP_IDENTITY/HARD
- sect hall → LOCATION
- sample video → CAMERA/MOTION_ONLY; explicitly do not copy story/characters/location
- voice sample → VOICE_REFERENCE

## 3. Canon
Store world/faction/power-system, the hidden truth that Lâm Uyên is tied to the seal, and separate audience/character knowledge states.

## 4. Episode arc
0–15 catastrophe hook  
15–30 missing seal/mystery  
30–45 attack + master reveal  
45–60 truth accusation/cliffhanger

## 5. Blocking example for final segment
Huyền Tôn first looks at Lâm Uyên's sword, not his face. Lâm Uyên takes half a step forward. Huyền Tôn raises his eyes only before the reveal. Pause. Camera slowly pushes into Lâm Uyên reaction. Red seal appears beneath torn collar.

## 6. Compiled prompt excerpt
```text
Continue directly from the accepted previous segment.
No fighting now. The scene becomes still.

Stage 1: Huyền Tôn looks at the Azure Sword rather than Lâm Uyên's face. Lâm Uyên steps forward half a pace. Huyền Tôn asks softly in Vietnamese: “Con vẫn chưa hiểu sao?” Pause.

Stage 2: Huyền Tôn raises his eyes and says: “Cửu U Phong Ấn... chính con đã mở.” Lâm Uyên does not answer. Camera slowly pushes toward his reaction. A faint red ancient seal becomes visible beneath the torn collar.

End state: extreme close-up of the glowing seal reflected in Lâm Uyên's eye.
No subtitles. No additional dialogue. Keep faces, outfits, injuries, sword and night lighting unchanged.
```

## 7. Episode commit
After final acceptance, commit: master alive, seal missing, accusation heard but not necessarily believed, outfit/injury state, sword ownership, destroyed hall and cliffhanger. Episode 2 retrieves this canon rather than re-reading entire chat history.
