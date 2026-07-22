# Design Master

[English](README.md) | [简体中文](README.zh-CN.md)

Design Master is a resource-first AI designer plugin. It researches relevant references and extracts an executable design system before generating responsive pages, HTML presentations, dashboards, motion experiences, or selective 3D. It then applies a unified review across visual quality, UX, accessibility, responsiveness, and performance.

The user only needs to provide the goal, content, images, and data. Design Master automatically selects reference sources, derives the design system, chooses justified engines, generates the artifact, and runs quality checks. Users do not need to request each step separately.

Version `0.1.0` establishes the foundation. It is not a template generator that forces animation and 3D into every page.

## Implemented

- Source, version, dependency, and license audits for the six required open-source Skills
- Integration boundaries for Claude Design, Open Design, and four frontend engines
- A queryable index of international and Chinese design resources
- A human-readable design-resource guide that also works as a bookmark collection
- A prompt pipeline covering reference research, design DNA, generation, Skill packaging, and editing
- Unified routing for pages, decks, dashboards, motion, and 3D
- Conditional integration recipes for ECharts, GSAP, Spline, and Three.js
- Quality gates covering design taste, UI/UX, accessibility, responsiveness, and performance
- An executable engine planner and JSON Schemas

## Structure

```text
.codex-plugin/plugin.json       Codex plugin manifest
skills/design-master/           Main Skill, references, schemas, and scripts
docs/RESOURCE_RESEARCH.md       Resource research report
docs/UPSTREAMS.lock.json        Pinned upstream versions and licenses
THIRD_PARTY.md                  Third-party integration and redistribution boundaries
```

## Usage

After installing it as a Codex plugin, try prompts such as:

- “Build a landing page for my AI product.”
- “Turn this content into a 12-slide launch presentation with real charts.”
- “Redesign this page using the supplied URL and screenshot as references.”
- “Review and improve this existing website.”

The research, design-system extraction, engine selection, and quality review happen automatically when required.

Run the deterministic engine planner:

```bash
python3 skills/design-master/scripts/plan_artifact.py request.json --pretty
```

See the [resource research report](docs/RESOURCE_RESEARCH.md) for the complete audit.

## Optional generated-asset pipeline

The experimental [`integrations/genblaze/`](integrations/genblaze/) path uses the
official Genblaze SDK to generate justified design imagery and persist assets
and provenance in Backblaze B2. It includes an executable dry-run; live provider
and storage verification remains required before this is described as deployed.

## Design resource guide

The resource library can also be used independently as a categorized bookmark and discovery guide:

- [Design Resource Guide](docs/DESIGN_RESOURCES.md)
- [设计资源导览](docs/DESIGN_RESOURCES.zh-CN.md)

## Principles

- Reuse proven resources without disguising license-incompatible code as original work.
- Establish the reference-derived design system before implementation.
- Do not add animation, charts, or 3D unless the content justifies them.
- Do not invent data to create a false sense of sophistication.
- Keep editing and playback isolated so exported artifacts remain clean.

## License

Original content in this repository is licensed under MIT. Third-party projects and runtimes retain their respective licenses; see [THIRD_PARTY.md](THIRD_PARTY.md).
