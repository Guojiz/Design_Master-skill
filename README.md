# Design Master

[English](README.md) | [简体中文](README.zh-CN.md)

Design Master is a resource-first AI design orchestration plugin. It researches relevant references and extracts an executable design system before generating responsive pages, HTML presentations, dashboards, motion experiences, or selective 3D. It then applies a unified review across visual quality, UX, accessibility, responsiveness, and performance.

Version `0.1.0` establishes the foundation. It is not a template generator that forces animation and 3D into every page.

## Implemented

- Source, version, dependency, and license audits for the six required open-source Skills
- Integration boundaries for Claude Design, Open Design, and four frontend engines
- A queryable index of international and Chinese design resources
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

- “Research three highly relevant references, then build a design system and landing page for my AI product.”
- “Turn this content into a 12-slide HTML launch deck, using real charts on the data slides.”
- “Analyze this URL and screenshot, produce a design specification, then redesign the page with it.”
- “Audit this HTML for generic AI styling, hierarchy, responsiveness, accessibility, and motion.”

Run the deterministic engine planner:

```bash
python3 skills/design-master/scripts/plan_artifact.py request.json --pretty
```

See the [resource research report](docs/RESOURCE_RESEARCH.md) for the complete audit.

## Principles

- Reuse proven resources without disguising license-incompatible code as original work.
- Establish the reference-derived design system before implementation.
- Do not add animation, charts, or 3D unless the content justifies them.
- Do not invent data to create a false sense of sophistication.
- Keep editing and playback isolated so exported artifacts remain clean.

## License

Original content in this repository is licensed under MIT. Third-party projects and runtimes retain their respective licenses; see [THIRD_PARTY.md](THIRD_PARTY.md).
