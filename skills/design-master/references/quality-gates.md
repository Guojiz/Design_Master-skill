# Unified quality gates

Run blockers before warnings. Record results in `qa-report.json` with evidence such as viewport, selector, screenshot or test command.

## Contents

- [Universal blockers](#universal-blockers)
- [Taste and anti-template checks](#taste-and-anti-template-checks)
- [UX and accessibility checks](#ux-and-accessibility-checks)
- [Responsive page checks](#responsive-page-checks)
- [Deck checks](#deck-checks)
- [Data and ECharts checks](#data-and-echarts-checks)
- [Motion and GSAP checks](#motion-and-gsap-checks)
- [3D checks](#3d-checks)
- [Editor checks](#editor-checks)
- [Severity and report format](#severity-and-report-format)

## Universal blockers

- The artifact renders without uncaught console errors or missing required assets.
- Content facts, metrics, logos and product screenshots are user-provided or source-backed.
- Text/background contrast, visible focus, keyboard path and semantic landmarks are usable.
- No horizontal overflow occurs at required page viewports.
- Motion honors reduced-motion; 3D has a static or non-WebGL fallback.
- Every third-party dependency has a reason, version and license classification.
- The output follows the accepted design system; exceptions are documented.
- Exported artifacts reopen successfully and contain no editor chrome or debug state.

## Taste and anti-template checks

- The first viewport contains the primary message and a meaningful next action without accidental clipping.
- Typography has a deliberate display/body hierarchy; body text has readable line length and line height.
- Spacing follows a scale. Near-equal arbitrary gaps do not create visual noise.
- Repeated cards are justified by repeated content. Vary composition when the story changes.
- Eyebrows, pills, gradients, glass panels and giant rounded cards are not used as default decoration.
- Images are relevant, art-directed and correctly cropped; generic stock or fabricated UI is absent.
- Motion has a named purpose. If removing it changes nothing, remove it.
- The design contains at least one content-specific visual decision and does not look like a generic template with swapped text.

## UX and accessibility checks

- Interactive controls use the correct native element or equivalent semantics.
- Touch targets are large enough for the supported platform and not crowded.
- Hover-only information has a focus / touch path.
- Forms expose labels, instructions, errors and recovery.
- Loading, empty, error, disabled and success states exist where the flow needs them.
- Focus order matches visual and reading order.
- Zoom and text resizing do not hide essential content.
- Color is not the only carrier of state.
- Autoplaying media can be paused and does not unexpectedly produce audio.

## Responsive page checks

Test at least 320×800, 768×1024 and 1440×900 unless the brief sets other targets.

- Navigation has an operable narrow-screen state.
- Headings wrap without orphaned single words when practical.
- Images reserve space and do not crop essential subjects.
- Grid content becomes a meaningful reading order, not just fewer columns.
- Sticky or fixed elements do not cover content or controls.
- Viewport units account for mobile browser chrome where full-height sections are required.

## Deck checks

- Every slide stays inside the safe area at 1920×1080 logical size.
- Stage scaling preserves aspect ratio and does not reflow individual elements.
- Keyboard, pointer / touch and direct page selection work.
- Presenter notes and controls are absent from audience and print modes.
- Body text remains legible from a projected / small viewport.
- Each slide has one dominant idea; overflow is solved by editing or splitting, not shrinking everything.
- PDF / print output preserves backgrounds, page breaks and correct slide count.

## Data and ECharts checks

- Chart type matches the analytical question.
- Source, time range, units, timezone and freshness are visible.
- Axis baselines and scales do not exaggerate change.
- Ranking / sorting behavior is stable and explained.
- Tooltips are supplemental; the essential conclusion is visible without hovering.
- Color palette works for common color-vision deficiencies and state colors retain their semantic role.
- Critical data has an accessible text or table alternative.
- No demo or fabricated numbers remain.

## Motion and GSAP checks

- Each animation has a trigger, purpose, duration, easing, interrupt behavior and reduced-motion result.
- Hidden initial states do not strand content if JavaScript fails.
- ScrollTrigger instances, observers and timelines are cleaned up.
- Layout thrashing is absent; transforms and opacity are preferred.
- Scroll is not hijacked and keyboard navigation remains predictable.
- Split text is reverted and accessible text remains available.

## 3D checks

- 3D is central to the message or interaction, not ornamental cost.
- Scene loading has progress or an immediate poster.
- Page content and CTA remain usable when the scene fails.
- DPR, texture sizes, geometry and postprocessing respect the stated budget.
- Rendering pauses when hidden / offscreen and resources are disposed on teardown.
- Pointer, touch and keyboard behavior are defined where interaction is required.
- Spline and Three.js are not both active without an approved reason and measured budget.

## Editor checks

- Edit/play toggle does not cause layout drift.
- Text, image, token, duplicate and delete commands each undo and redo.
- Drag behavior respects page grid or deck canvas constraints.
- Editor overlay is keyboard operable and has visible focus.
- Export strips editor-only elements, attributes, storage and listeners.
- Reopened export preserves original responsive layout and animation.

## Severity and report format

Use `blocker`, `warning` and `pass`:

```json
{
  "artifact": "dist/index.html",
  "testedAt": "YYYY-MM-DDTHH:mm:ssZ",
  "checks": [
    {
      "id": "responsive.no-horizontal-overflow",
      "severity": "blocker",
      "status": "pass",
      "evidence": "320x800 and 768x1024 Playwright screenshots"
    }
  ],
  "knownLimitations": []
}
```

Do not hand off with an unresolved blocker. Warnings may remain only when the tradeoff is explicit and the core task is still usable.
