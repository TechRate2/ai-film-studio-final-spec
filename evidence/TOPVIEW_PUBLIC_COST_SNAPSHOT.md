# TopView Public Cost Snapshot — Evidence Only

This is a **snapshot from public code inspected during design**, not a guaranteed current product price and not a cash conversion.

Previously inspected public estimator logic included examples such as:
- Seedance 2.0 Mini: 480p 0.32 credits/s, 720p 0.64 credits/s.
- Some image models charged per generated image/resolution.
- Public code did not establish a reliable universal USD/VND value per credit in the inspected source.

Architecture consequence only:
- video generation is usually the dominant media cost;
- LLM/research/image planning can be economically worthwhile if it prevents one unnecessary video regeneration;
- UI must use live provider profile values at runtime rather than hard-coded snapshot values.

Never use this file as runtime pricing truth.
