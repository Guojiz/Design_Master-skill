#!/usr/bin/env python3
"""Create a deterministic optional-engine plan for a Design Master artifact."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ARTIFACT_TYPES = {"page", "deck", "dashboard", "motion", "3d"}
DATA_SHAPES = {"none", "category", "timeseries", "composition", "ranking", "relationship"}
MOTION_PURPOSES = {"none", "hierarchy", "state", "story", "decorative"}
THREE_D_MODES = {"none", "spline", "custom"}
CHARTABLE_SHAPES = DATA_SHAPES - {"none"}
JUSTIFIED_MOTION = {"hierarchy", "state", "story"}


class InputError(ValueError):
    """Raised when the artifact request does not match the supported contract."""


def _object(payload: dict[str, Any], key: str) -> dict[str, Any]:
    value = payload.get(key, {})
    if not isinstance(value, dict):
        raise InputError(f"{key} must be an object")
    return value


def _boolean(payload: dict[str, Any], key: str, default: bool = False) -> bool:
    value = payload.get(key, default)
    if not isinstance(value, bool):
        raise InputError(f"{key} must be a boolean")
    return value


def _enum(payload: dict[str, Any], key: str, allowed: set[str], default: str) -> str:
    value = payload.get(key, default)
    if not isinstance(value, str) or value not in allowed:
        choices = ", ".join(sorted(allowed))
        raise InputError(f"{key} must be one of: {choices}")
    return value


def _decision(enabled: bool, reason: str) -> dict[str, Any]:
    return {"enabled": enabled, "reason": reason}


def validate_request(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise InputError("request must be a JSON object")

    allowed_top_level = {"artifactType", "structuredData", "motion", "threeD", "performance"}
    unknown = sorted(set(payload) - allowed_top_level)
    if unknown:
        raise InputError(f"unsupported top-level fields: {', '.join(unknown)}")

    artifact_type = payload.get("artifactType")
    if not isinstance(artifact_type, str) or artifact_type not in ARTIFACT_TYPES:
        choices = ", ".join(sorted(ARTIFACT_TYPES))
        raise InputError(f"artifactType must be one of: {choices}")

    data = _object(payload, "structuredData")
    motion = _object(payload, "motion")
    three_d = _object(payload, "threeD")
    performance = _object(payload, "performance")

    _reject_unknown(data, {"present", "shape"}, "structuredData")
    _reject_unknown(motion, {"purpose"}, "motion")
    _reject_unknown(three_d, {"mode", "central", "sceneProvided"}, "threeD")
    _reject_unknown(performance, {"mobilePriority", "reducedMotionFallback"}, "performance")

    return {
        "artifactType": artifact_type,
        "structuredData": {
            "present": _boolean(data, "present"),
            "shape": _enum(data, "shape", DATA_SHAPES, "none"),
        },
        "motion": {
            "purpose": _enum(motion, "purpose", MOTION_PURPOSES, "none"),
        },
        "threeD": {
            "mode": _enum(three_d, "mode", THREE_D_MODES, "none"),
            "central": _boolean(three_d, "central"),
            "sceneProvided": _boolean(three_d, "sceneProvided"),
        },
        "performance": {
            "mobilePriority": _boolean(performance, "mobilePriority"),
            "reducedMotionFallback": _boolean(performance, "reducedMotionFallback"),
        },
    }


def _reject_unknown(payload: dict[str, Any], allowed: set[str], label: str) -> None:
    unknown = sorted(set(payload) - allowed)
    if unknown:
        raise InputError(f"unsupported {label} fields: {', '.join(unknown)}")


def build_plan(raw_request: Any) -> dict[str, Any]:
    request = validate_request(raw_request)
    artifact_type = request["artifactType"]
    data = request["structuredData"]
    motion = request["motion"]
    three_d = request["threeD"]
    performance = request["performance"]

    blockers: list[str] = []
    warnings: list[str] = []
    fallbacks: list[str] = []

    chartable = data["present"] and data["shape"] in CHARTABLE_SHAPES
    if chartable:
        echarts = _decision(True, f"Structured {data['shape']} data has a chartable question.")
        fallbacks.append("Provide a text summary or accessible data table for critical chart content.")
    else:
        echarts = _decision(False, "No structured chartable data was declared; avoid decorative or fabricated charts.")

    if data["present"] != (data["shape"] != "none"):
        blockers.append("structuredData.present and structuredData.shape disagree.")
    if artifact_type == "dashboard" and not chartable:
        blockers.append("A dashboard needs real structured data or an explicit schema placeholder before final generation.")

    if motion["purpose"] in JUSTIFIED_MOTION:
        gsap = _decision(True, f"Motion is justified by {motion['purpose']}.")
        fallbacks.append("Provide a prefers-reduced-motion branch that exposes the final semantic state.")
    elif motion["purpose"] == "decorative":
        gsap = _decision(False, "Decorative motion alone does not justify a GSAP dependency.")
        warnings.append("Replace decorative motion with static hierarchy or a small CSS transition if useful.")
    else:
        gsap = _decision(False, "No hierarchy, state or story purpose was declared for motion.")

    if artifact_type == "motion" and motion["purpose"] not in JUSTIFIED_MOTION:
        blockers.append("A motion artifact needs a hierarchy, state or story purpose before choosing a timeline.")

    spline = _decision(False, "No user-provided central Spline scene was declared.")
    three = _decision(False, "No central custom 3D requirement was declared.")

    if three_d["mode"] != "none" and not three_d["central"]:
        warnings.append("3D was requested but is not central; prefer a 2D image or video fallback.")
    elif three_d["mode"] == "spline":
        if not three_d["sceneProvided"]:
            blockers.append("Spline requires a user-provided scene URL, viewer export or .splinecode asset.")
        else:
            spline = _decision(True, "A user-provided Spline scene is central to the artifact.")
            fallbacks.append("Keep an informative poster visible until Spline loads and restore it on failure.")
    elif three_d["mode"] == "custom":
        three = _decision(True, "Custom low-level 3D is central, so Three.js is appropriate.")
        fallbacks.append("Provide a static poster or core HTML experience for reduced motion and WebGL failure.")

    if artifact_type == "3d" and three_d["mode"] == "none":
        blockers.append("A 3d artifact must choose spline or custom mode and define why 3D is central.")

    rich_motion_enabled = gsap["enabled"] or spline["enabled"] or three["enabled"]
    if rich_motion_enabled and not performance["reducedMotionFallback"]:
        warnings.append("Implement and test the required reduced-motion or static fallback before delivery.")

    if performance["mobilePriority"] and (spline["enabled"] or three["enabled"]):
        warnings.append("Mobile-priority 3D requires a DPR cap, asset budget, visibility pause and measured fallback.")

    if spline["enabled"] and three["enabled"]:
        blockers.append("Spline and Three.js must not be enabled together by default.")

    return {
        "schemaVersion": 1,
        "artifactType": artifact_type,
        "engines": {
            "echarts": echarts,
            "gsap": gsap,
            "spline": spline,
            "three": three,
        },
        "requiredFallbacks": fallbacks,
        "blockers": blockers,
        "warnings": warnings,
        "ready": not blockers,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path, help="Path to an artifact request JSON file")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the result")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        payload = json.loads(args.request.read_text(encoding="utf-8"))
        plan = build_plan(payload)
    except (OSError, json.JSONDecodeError, InputError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2

    indent = 2 if args.pretty else None
    print(json.dumps(plan, ensure_ascii=False, indent=indent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
