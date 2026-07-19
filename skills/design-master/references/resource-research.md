# Reference research protocol

Use `resource-index.json` as a routing index, not as permission to scrape every site.

If the user only wants inspiration, bookmarks, or navigation, return a curated categorized link list with a short purpose for each source and stop there. Artifact generation is not required.

## Select sources

1. Classify the project and audience.
2. Query `projectTypes` and `specialties` in `resource-index.json`.
3. Select 3–5 sources with complementary roles: one structural, one visual-language, one typography or product-flow source as needed.
4. Treat entries with `aliasOf` as the same source. Do not count Godly and Recent Design twice.
5. Prefer primary project pages over aggregator reposts and record the original creator.

Example query:

```bash
jq '.resources[] | select(.projectTypes | index("dashboard")) | {name, url, specialties}' references/resource-index.json
```

## Collect cases

Collect 3–8 cases. For each case record:

```json
{
  "url": "https://example.com/project",
  "sourceId": "siteinspire",
  "title": "Project title",
  "creator": "Known creator or unknown",
  "observedAt": "YYYY-MM-DD",
  "projectFit": ["brand-site", "typography"],
  "observableFacts": [
    "Twelve-column desktop grid",
    "Display serif used only for editorial headlines"
  ],
  "inferences": [
    "The high contrast likely prioritizes editorial authority"
  ],
  "doNotCopy": ["logo", "copy", "hero photograph"],
  "rights": "linked-reference-only"
}
```

Separate facts from inference. Do not infer exact CSS values from a compressed screenshot when they cannot be measured.

## Synthesize

Do not average every reference into a bland hybrid. Produce:

- common rules supported by multiple cases;
- deliberate differences and which one fits the brief;
- design tokens and measurable layout rules;
- component, chart, motion and responsive rules;
- patterns to avoid because they depend on another brand or content type.

## Rights and access

- Respect login, robots, rate limits and terms. Do not bypass access controls.
- Store URLs, necessary metadata and original analysis; do not bulk-cache copyrighted images, videos, copy or source code.
- Treat Pinterest, Huaban, Muzli and navigation sites as discovery layers; follow through to the original creator when possible.
- Treat Dribbble concepts as visual references, not proof of a complete usable product flow.
- Cite live sources in the final design rationale.
