import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).parents[1]
    / "skills"
    / "design-master"
    / "scripts"
    / "plan_artifact.py"
)
SPEC = importlib.util.spec_from_file_location("plan_artifact", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
plan_artifact = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(plan_artifact)


class PlanArtifactTests(unittest.TestCase):
    def test_dashboard_uses_real_chart_and_story_motion(self):
        result = plan_artifact.build_plan(
            {
                "artifactType": "dashboard",
                "structuredData": {"present": True, "shape": "timeseries"},
                "motion": {"purpose": "story"},
                "performance": {"reducedMotionFallback": True},
            }
        )

        self.assertTrue(result["ready"])
        self.assertTrue(result["engines"]["echarts"]["enabled"])
        self.assertTrue(result["engines"]["gsap"]["enabled"])
        self.assertFalse(result["engines"]["spline"]["enabled"])
        self.assertFalse(result["engines"]["three"]["enabled"])

    def test_spline_without_scene_is_blocked(self):
        result = plan_artifact.build_plan(
            {
                "artifactType": "3d",
                "threeD": {"mode": "spline", "central": True, "sceneProvided": False},
            }
        )

        self.assertFalse(result["ready"])
        self.assertTrue(any("user-provided scene" in item for item in result["blockers"]))

    def test_decorative_motion_does_not_enable_gsap(self):
        result = plan_artifact.build_plan(
            {"artifactType": "page", "motion": {"purpose": "decorative"}}
        )

        self.assertTrue(result["ready"])
        self.assertFalse(result["engines"]["gsap"]["enabled"])
        self.assertTrue(result["warnings"])

    def test_custom_3d_is_exclusive_and_warns_for_mobile(self):
        result = plan_artifact.build_plan(
            {
                "artifactType": "3d",
                "threeD": {"mode": "custom", "central": True},
                "performance": {"mobilePriority": True, "reducedMotionFallback": True},
            }
        )

        self.assertTrue(result["ready"])
        self.assertTrue(result["engines"]["three"]["enabled"])
        self.assertFalse(result["engines"]["spline"]["enabled"])
        self.assertTrue(any("Mobile-priority" in item for item in result["warnings"]))

    def test_rejects_unknown_fields(self):
        with self.assertRaises(plan_artifact.InputError):
            plan_artifact.build_plan({"artifactType": "page", "magic": True})


if __name__ == "__main__":
    unittest.main()
