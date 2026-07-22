#!/usr/bin/env python3
"""Generate a design asset with Genblaze and persist it to Backblaze B2."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path


def build_plan(prompt: str, model: str, bucket: str) -> dict[str, object]:
    return {
        "pipeline": "design-master-generated-asset",
        "provider": "genblaze-openai",
        "model": model,
        "modality": "image",
        "storage": "Backblaze B2 via genblaze-s3",
        "bucket": bucket or "<B2_BUCKET>",
        "key_strategy": "hierarchical",
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "prompt": prompt,
    }


def required_env() -> dict[str, str]:
    names = ("OPENAI_API_KEY", "B2_KEY_ID", "B2_APP_KEY", "B2_BUCKET")
    values = {name: os.environ.get(name, "") for name in names}
    missing = [name for name, value in values.items() if not value]
    if missing:
        raise RuntimeError("Missing required environment variables: " + ", ".join(missing))
    return values


def run(prompt: str, model: str, output_dir: Path) -> dict[str, object]:
    values = required_env()
    from genblaze_core import KeyStrategy, Modality, ObjectStorageSink, Pipeline
    from genblaze_openai import DalleProvider
    from genblaze_s3 import S3StorageBackend

    storage = ObjectStorageSink(
        S3StorageBackend.for_backblaze(
            values["B2_BUCKET"],
            key_id=values["B2_KEY_ID"],
            app_key=values["B2_APP_KEY"],
        ),
        prefix="design-master",
        key_strategy=KeyStrategy.HIERARCHICAL,
    )
    result = (
        Pipeline("design-master-generated-asset")
        .step(
            DalleProvider(api_key=values["OPENAI_API_KEY"], output_dir=output_dir),
            model=model,
            prompt=prompt,
            modality=Modality.IMAGE,
            metadata={"created_by": "Design Master", "purpose": "design asset"},
        )
        .run(sink=storage)
    )
    asset = result.run.steps[0].assets[0]
    return {
        "status": "generated-and-stored",
        "url": asset.url,
        "sha256": asset.sha256,
        "run_id": str(result.run.id),
        "bucket": values["B2_BUCKET"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Reference-derived prompt for the design asset")
    parser.add_argument("--model", default="dall-e-3")
    parser.add_argument("--output-dir", default="output/genblaze")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    plan = build_plan(args.prompt, args.model, os.environ.get("B2_BUCKET", ""))
    if args.dry_run:
        print(json.dumps(plan, indent=2))
        return 0
    receipt = run(args.prompt, args.model, Path(args.output_dir))
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

