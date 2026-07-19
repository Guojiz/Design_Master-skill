# Delivery contracts

## Contents

- [Shared project state](#shared-project-state)
- [Design-system contract](#design-system-contract)
- [Responsive page](#responsive-page)
- [HTML deck](#html-deck)
- [Dashboard](#dashboard)
- [Motion artifact](#motion-artifact)
- [3D artifact](#3d-artifact)
- [Editor contract](#editor-contract)
- [Handoff contract](#handoff-contract)

## Shared project state

Keep generated work portable across Claude Design, Open Design and a local coding Agent:

```text
project/
├── research/
│   └── refs.json
├── design-system.md
├── tokens.json
├── artifact.json
├── src/
├── public/
└── qa-report.json
```

Use the repository's `assets/schemas/artifact-request.schema.json` before choosing engines. Generated projects may use a framework-specific structure, but the five metadata files should retain the same semantics.

## Design-system contract

`design-system.md` is the human-readable contract. Include:

1. Intent, audience, brand traits and prohibited traits.
2. Source references and evidence.
3. Color roles and contrast expectations.
4. Typography roles, type scale, line height, line length and language coverage.
5. Spacing scale, container sizes, grid, breakpoints and vertical rhythm.
6. Image ratios, crop behavior, lighting, treatment and fallback.
7. Component anatomy, variants, states and interaction.
8. Chart palette, chart selection, labels, tooltips and data integrity.
9. Motion purpose, duration bands, easing, orchestration and reduced-motion behavior.
10. Surface, icon, accessibility and performance rules.

`tokens.json` is the machine-readable contract. Prefer semantic tokens over component literals:

```json
{
  "color": {
    "bg": { "canvas": "#FFFFFF", "surface": "#F6F7F9" },
    "text": { "primary": "#101114", "muted": "#5D6470" },
    "accent": { "primary": "#5B5BD6", "onPrimary": "#FFFFFF" },
    "state": { "success": "#137A50", "warning": "#9A5B00", "danger": "#B42318" }
  },
  "type": {
    "family": { "display": "system-ui", "body": "system-ui", "mono": "ui-monospace" },
    "size": { "body": "1rem", "h3": "1.5rem", "h2": "2.25rem", "h1": "clamp(2.75rem, 7vw, 6rem)" },
    "lineHeight": { "body": 1.6, "heading": 1.05 }
  },
  "space": { "1": "0.25rem", "2": "0.5rem", "3": "0.75rem", "4": "1rem", "6": "1.5rem", "8": "2rem", "12": "3rem", "16": "4rem" },
  "radius": { "sm": "0.5rem", "md": "1rem", "lg": "1.5rem" },
  "motion": { "fast": 0.16, "base": 0.32, "slow": 0.7, "ease": "power2.out" },
  "chart": { "categorical": ["#5B5BD6", "#2A9D8F", "#E9C46A", "#E76F51"] },
  "performance": { "maxDpr": 2, "threeDTextureBudgetMb": 24 }
}
```

Replace sample values with evidence-backed project values. Check contrast after replacement.

## Responsive page

Use content-driven document flow.

- Use semantic landmarks and one meaningful `h1`.
- Use grid / flex for layout; absolute positioning is limited to controlled visual layers.
- Define mobile-first behavior and at least one narrow and one wide verification viewport.
- Keep readable body line length, usually 45–80 characters depending on language and typeface.
- Prevent horizontal overflow at 320 CSS px unless the product explicitly requires a canvas.
- Define hover, focus, active, disabled, loading, error and empty states where relevant.
- Lazy-load noncritical media and reserve dimensions to avoid layout shift.
- Do not inherit the deck's 1920×1080 stage.

## HTML deck

Use a fixed logical stage with uniform scale:

- Logical size: 1920×1080 unless the brief defines another aspect ratio.
- Scale the entire stage to fit the viewport; do not independently reflow slide content.
- Support keyboard, click / touch navigation, page number and direct slide selection.
- Keep titles, body and key visuals inside a shared safe area.
- Expose presenter notes in a separate presenter mode, not on the audience canvas.
- Preserve a print / PDF mode without navigation chrome.
- Test every slide at full size and at a small projected viewport.
- Use progressive disclosure for large template libraries: index → preview → selected template detail.

Recommended slide types:

| Purpose | Required behavior |
|---|---|
| Cover | One clear promise, minimal metadata, strong art direction |
| Agenda / section | Orient the audience and change rhythm |
| Feature | One claim, evidence, product visual or mechanism |
| Data | One question per chart, source and annotation |
| Case | Context, intervention, result; no unsupported metrics |
| Summary | Reconnect to the opening promise and next action |

## Dashboard

Design around decisions rather than chart count.

- Name the user decision and update frequency for every view.
- Put status and comparison context next to KPI values.
- Match chart type to analytical question; use tables for exact lookup.
- Include data source, time range, timezone and last refresh.
- Use a consistent categorical palette; reserve state colors for state.
- Keep axes, labels and units visible unless redundant by construction.
- Support loading, empty, stale, partial and error states.
- Make legends and tooltips keyboard-accessible when the library permits.
- Provide a text or table alternative for critical chart information.
- Do not animate rankings or live data unless the transition helps track change.

## Motion artifact

Create a motion map before writing a timeline:

| Field | Meaning |
|---|---|
| Trigger | load, scroll, click, state change or timeline time |
| Purpose | hierarchy, continuity, feedback or narrative |
| Target | exact elements or component state |
| Duration | token or explicit seconds |
| Easing | design-system easing |
| Interrupt | what happens on rapid input or route change |
| Reduced motion | instant state, fade or static poster |

Use one master timeline per scene / section and named labels for meaningful states. Kill observers and timelines on teardown. Do not animate layout properties when transforms or opacity can express the same change.

## 3D artifact

Choose one 3D path:

- **Spline** when the user provides a Spline scene and needs quick product presentation or authored spatial interaction.
- **Three.js** when custom shaders, particles, camera choreography, generated geometry or low-level control are essential.

Before implementation, define:

- central user value of 3D;
- asset owner and license;
- desktop and mobile GPU budget;
- texture and model size budget;
- input model: pointer, touch, keyboard and device motion;
- loading, failure, reduced-motion and no-WebGL fallback;
- whether interaction is discoverable and reversible.

Pause rendering when offscreen or when the document is hidden. Cap device pixel ratio. Dispose GPU resources on teardown. Keep core content outside the canvas so it remains accessible.

## Editor contract

Separate model, rendering and editor UI:

```text
serializable document model → artifact renderer
              ↑                     ↓
         command history ← editor overlay
```

Required commands:

- `editText(nodeId, value)`
- `replaceImage(nodeId, asset, crop)`
- `setToken(path, value)`
- `moveNode(nodeId, constrainedPosition)`
- `duplicatePage(pageId)`
- `deleteNode(nodeId)`
- `undo()` / `redo()`
- `exportHtml()`

Rules:

- Store stable node IDs outside visible copy.
- Serialize each mutation as a reversible command.
- Do not inject toolbar elements into animation target nodes.
- Constrain drag behavior by artifact type: free positioning for deck / canvas, grid reordering for responsive page.
- Strip all editor-only DOM, attributes, event handlers and storage state during export.

## Handoff contract

Deliver these together:

- source files and start / build command;
- `design-system.md` and `tokens.json`;
- reference provenance and licenses;
- dependency list with purpose and version;
- QA report with viewports and fallbacks tested;
- export files requested by the user;
- known limitations and the smallest next step.

Do not declare completion from source generation alone. Render, interact with and reopen the exported artifact.
