---
name: design-master
description: Resource-first AI design orchestration for researching references, extracting executable design systems, and creating or improving responsive websites, product pages, HTML presentations, dashboards, infographics, motion pages, and selective 3D experiences. Use when Codex must analyze a URL, screenshot, image, design file, HTML or brand assets; choose design inspiration sources; generate a consistent page or deck; conditionally use ECharts, GSAP, Spline or Three.js; add lightweight editing; or audit visual quality, UX, accessibility, responsiveness and performance.
---

# Design Master

Treat reference research and design-system extraction as prerequisites, not decoration added after implementation.

## Core workflow

1. Classify the deliverable as `page`, `deck`, `dashboard`, `motion`, or `3d`.
2. Inspect supplied URLs, screenshots, HTML, brand assets, copy and data. Do not invent facts, logos, product UI or metrics.
3. If the request is open-ended, select 3–5 relevant sources from `references/resource-index.json`, collect 3–8 cases, and record URLs plus observable facts. Do not bulk-copy protected assets.
4. Extract an executable design system before generating: colors, typography, spacing, grid, imagery, components, charts, motion, responsive behavior and constraints. Use `references/prompt-pipeline.md` and `references/delivery-contracts.md`.
5. For an open-ended new design, show three materially different visual directions as real previews. Skip this gate when the user provides a locked design system, an exact implementation target, or explicitly requests direct execution.
6. Generate with the selected contract. Use `references/engine-recipes.md` to include only justified engines.
7. Run every blocking quality gate in `references/quality-gates.md`. Fix blockers before presenting the artifact.
8. Deliver source, design-system files, reference provenance, QA result and export instructions together.

Ask at most one critical question at a time. Make reversible assumptions for noncritical gaps and state them early.

## Load only what the task needs

- Read `references/prompt-pipeline.md` when analyzing a reference, generating a design, packaging a reusable system, or adding an editor.
- Read `references/resource-research.md` and query `references/resource-index.json` when external inspiration or trend research is required.
- Read `references/delivery-contracts.md` before creating a page, deck, dashboard, motion or 3D artifact.
- Read `references/engine-recipes.md` only for engines selected by the router.
- Read `references/quality-gates.md` before review and delivery.
- Read `references/external-backends.md` only when Claude Design, Open Design or an upstream Skill is available.
- Read `../../docs/RESOURCE_RESEARCH.md` and `../../docs/UPSTREAMS.lock.json` only when auditing or upgrading upstream resources.

## Engine decision

When the request is ambiguous or more than one rich-media engine appears plausible, create an artifact request JSON conforming to `assets/schemas/artifact-request.schema.json`, then run:

```bash
python3 scripts/plan_artifact.py request.json --pretty
```

Follow the result. Never enable ECharts without structured data, GSAP for purely decorative motion, Spline without a user-provided scene/export, or Three.js when a simpler 2D or Spline solution is sufficient. Do not enable Spline and Three.js together by default.

## Non-negotiable delivery rules

- Keep responsive pages content-driven; never force them into a 16:9 deck canvas.
- Keep decks on a fixed logical stage and scale them uniformly.
- Make data visualization truthful, legible and accessible; include table or text alternatives when needed.
- Honor `prefers-reduced-motion` and supply a static fallback for motion and 3D.
- Keep editor controls in an isolated overlay that disappears from playback and export.
- Preserve source attribution and license boundaries. Never copy AGPL or unlicensed upstream code into this MIT plugin.
