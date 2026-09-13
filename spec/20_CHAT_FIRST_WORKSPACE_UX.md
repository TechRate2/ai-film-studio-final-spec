# Chat-First Workspace UX

## Default screen
One primary conversation/input surface with text request, attachments, progress, previews, cost summary and create/continue action. Do not expose dozens of required mode selectors.

## Global UI localization
The application UI must support Vietnamese and English globally from the same workspace. `ui_locale` is separate from project/script/dialogue/subtitle language. Changing UI from Vietnamese to English must not mutate story canon, voices, prompts or output language.

User-facing generated explanations/progress should follow UI locale when practical; creative output follows explicit project/content language.

## Progressive disclosure
Advanced “Cost & Production” may expose keyframe strategy (Smart Auto / External / User refs), quality (Economy / Balanced / Maximum), paid revision policy (Never automatic / Ask me), spend cap, research Auto and provider override (advanced).

## Artifact/shot cards
Preview, duration, cost, QA summary, accepted version, natural-language `Sửa shot này...`, Create New Version / Accept and version history.

## Intent-driven editing
User intent such as “nữ chính áo đỏ”, “camera chậm hơn”, “đổi sang tiếng Trung”, “giữ hình, chỉ sửa giọng” is translated into affected artifacts by backend.

## External keyframe card
Shows why keyframe is needed, copy prompt, required refs, upload result and validation result.

## Long-form navigation
Keep chat primary with lightweight Project → Episode → Scene/Shot previews. Do not turn default UI into a complex NLE.

## Accessibility/state
Loading, blocked, waiting-user, failed-partial, stale and completed states must be understandable in both supported UI locales without exposing raw provider logs as the main UX.

## Separate Translate Video entry after core completion
`spec/47_SOURCE_VIDEO_LOCALIZATION.md` defines an independent minimal workspace: upload → detected source language → target → Subtitles/Dubbing checkboxes → estimate → Process. Show a preview and editable sentence list with progressive voice, subtitle style and speed controls. AI check & align shows safe fixes, unresolved findings and Undo; it never hides a paid regeneration. Ordinary dubbing does not modify mouth shapes. Main Studio chat/Create stays primary and unchanged. Both surfaces have vi/en UI independently of output language.

## Visible Studio language and voice controls
Keep the composer primary. Show a compact 'Thoại / Speech language' control with Chinese (Mandarin, default), English, Vietnamese and verified other choices; a no-speech request displays 'Không thoại / No speech'. Do not use multiple language checkboxes that can accidentally select incompatible project defaults. Expose 'Phụ đề / Subtitles: Off or selected language' independently. The initial subtitle setting is Off. Chinese is a visible product preset for unspecified new speech, not silently inferred from model nationality; explicit request/series language follows spec/09.

Selecting Vietnamese displays 'Giọng riêng / Controlled voice', a short relevant voice list or upload option and the voice cost. Additional 'Khớp môi / Lip sync' starts unchecked; show its extra cost/capability when selected. If off with visible speaking faces, show 'Lồng tiếng thường không thay đổi khẩu hình / Ordinary dubbing does not change mouth shapes' and obtain explicit mismatch acknowledgment if this plan is to proceed. Never label unsynchronized dubbing as synchronized. An explicit lip-match constraint must be resolved, not waived by the default unchecked box. Hide irrelevant sync controls for narration/no speech; do not create narration just to avoid a difficult character scene.

Before Create, summarize resolved spoken and subtitle language, native/controlled voice, optional sync and complete estimate in the same workspace. A Chinese preset is therefore reviewable without an extra compulsory approval dialog per shot. Conflicting explicit chat/UI selections use one focused resolution; request prose/UI locale never silently changes speech. Preserve controls on reload and bind the server command to that version. Show capability blocks with viable, priced choices rather than letting unavailable options spend.

After an accepted Studio master, 'Dịch / Thêm phụ đề / Translate / Add subtitles' explicitly opens a linked LOCALIZATION draft with the exact source artifact/version. It does not run translation, TTS or lip sync; target and mode/cost approval remain separate under spec/47. Hide/disable this action with an explanation until that extension is released. Do not duplicate its workflow inside the Studio language selector.
