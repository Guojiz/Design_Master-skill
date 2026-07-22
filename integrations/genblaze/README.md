# Genblaze + Backblaze B2 experiment

This optional Design Master integration turns a reference-derived asset prompt
into an image-generation pipeline. Genblaze runs the provider, uploads the
generated asset to Backblaze B2, and writes provenance alongside the output.

It is intentionally separate from Design Master's deterministic engine planner.
The planner decides whether generated imagery is justified; this integration
only runs when an image is actually required.

## Install

```bash
python -m pip install -r integrations/genblaze/requirements.txt
```

## Preview without credentials

```bash
python integrations/genblaze/generate_design_asset.py \
  "Editorial hero image for an accessible climate-data dashboard" --dry-run
```

## Generate and store

Set `OPENAI_API_KEY`, `B2_KEY_ID`, `B2_APP_KEY`, and `B2_BUCKET`, then run the
same command without `--dry-run`. The JSON receipt contains the permanent asset
URL, SHA-256 digest, run ID, and bucket name. Never commit credentials.

## Verification status

- Official Genblaze packages install and import successfully.
- The dry-run path is executable and does not require credentials.
- A live generation and B2 upload is not yet claimed. Complete one run and save
  its receipt plus a redacted B2 object screenshot before a Devpost submission.

