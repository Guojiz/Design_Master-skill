# External backends and upstream adapters

Use external tools behind the same intermediate contract. Never make a project unrecoverable without one vendor.

## Claude Design

Claude Design is closed-source. Use it when the user already has access and its visual canvas, direct editing or export path materially helps.

Official Claude Code connection:

```bash
claude mcp add --scope user --transport http claude-design https://api.anthropic.com/v1/design/mcp
```

Then authenticate with `/design-login`. Use `/design-sync` for an existing design system when available.

Handoff into Claude Design:

- brief and audience;
- selected reference URLs and supplied screenshots;
- `design-system.md` and `tokens.json`;
- content, brand assets and factual constraints;
- requested output and quality gates.

Handoff out:

- standalone HTML or ZIP source when available;
- PDF / PPTX / Canva only when requested;
- design-system changes and unresolved assumptions;
- source assets and license notes.

Do not claim that Claude Design accepts arbitrary installable Skills. Treat design-system sync, MCP and Claude Code handoff as its extension surface.

## Open Design

Open Design is an Apache-2.0 local-first optional backend. Do not vendor its monorepo.

After the user installs Open Design, connect a supported agent with:

```bash
od mcp install codex
```

Use `od mcp install <agent> --print` to preview changes when appropriate.

Send the same design-system and artifact metadata used by the local workflow. Prefer Open Design for:

- preview and iterative studio editing;
- file-backed HTML / CSS artifacts;
- design-system reuse;
- plugins, functional Skills and rendering templates;
- HTML, PDF, PPTX, ZIP, Markdown or MP4 handoff.

Keep canonical project source in user-controlled files. Treat Open Design's bundled templates as independently licensed resources.

## Six upstream Skill adapters

| Upstream | Call when | Boundary |
|---|---|---|
| frontend-slides | Creating or converting an HTML deck; needing style previews or PPT extraction | Prefer its external Skill / template pack; do not load its full library into every task |
| huashu-design | Need multi-artifact routing, real visual directions, editable PPTX or motion-video pipeline | Use modules independently; do not force three directions for exact implementation work |
| guizang-ppt-skill | User explicitly wants its magazine or Swiss system and accepts AGPL external dependency | Do not copy its current source into Design Master |
| html-ppt-skill | Need the static deck runtime, themes, layouts or presenter mode | Use selected assets with MIT attribution or call external Skill |
| taste-skill | Need visual critique, anti-template review or design-intensity dials | Use as QA; do not let it override factual or product requirements |
| ui-ux-pro-max-skill | Need local search over style, palette, typography, charts, UX or stack rules | Invoke CLI / Python query; record Skill and CLI versions separately |

## Adapter result

Normalize every external result to:

```json
{
  "backend": "open-design",
  "backendVersion": "0.15.1",
  "inputs": ["design-system.md", "tokens.json", "artifact.json"],
  "outputs": ["src/index.html", "qa-report.json"],
  "licenses": ["Apache-2.0"],
  "assumptions": [],
  "warnings": []
}
```

If the backend cannot provide source, label the output as an export rather than a complete project.
