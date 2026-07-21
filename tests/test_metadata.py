import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class MetadataTests(unittest.TestCase):
    def test_resource_index_has_unique_ids_and_valid_aliases(self):
        payload = json.loads(
            (ROOT / "skills/design-master/references/resource-index.json").read_text(
                encoding="utf-8"
            )
        )
        resources = payload["resources"]
        ids = [resource["id"] for resource in resources]

        self.assertEqual(len(ids), len(set(ids)))
        for resource in resources:
            self.assertTrue(resource["url"].startswith("https://"))
            if "aliasOf" in resource:
                self.assertIn(resource["aliasOf"], ids)

    def test_lock_keeps_incompatible_code_external(self):
        payload = json.loads(
            (ROOT / "docs/UPSTREAMS.lock.json").read_text(encoding="utf-8")
        )
        repositories = {item["id"]: item for item in payload["repositories"]}
        packages = {item["id"]: item for item in payload["packages"]}

        self.assertEqual(repositories["guizang-ppt-skill"]["license"], "AGPL-3.0-only")
        self.assertIn("external", repositories["guizang-ppt-skill"]["integrationMode"])
        self.assertEqual(packages["spline-runtime"]["license"], "NOASSERTION")
        self.assertIn("embed", packages["spline-runtime"]["integrationMode"])

    def test_plugin_and_skill_names_match(self):
        plugin = json.loads(
            (ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
        )
        skill_text = (ROOT / "skills/design-master/SKILL.md").read_text(encoding="utf-8")

        self.assertEqual(plugin["name"], "design-master")
        self.assertIn("\nname: design-master\n", skill_text)


if __name__ == "__main__":
    unittest.main()
