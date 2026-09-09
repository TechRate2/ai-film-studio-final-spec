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
