from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "wechat-sketch-cover"


class SkillContractTests(unittest.TestCase):
    def test_frontmatter_and_required_files(self) -> None:
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", skill_text, re.DOTALL)
        self.assertIsNotNone(match)
        frontmatter = yaml.safe_load(match.group(1))
        self.assertEqual(frontmatter["name"], "wechat-sketch-cover")
        self.assertTrue(frontmatter["description"])
        self.assertEqual(frontmatter["metadata"]["version"], "1.0.1")

        required = [
            SKILL_ROOT / "agents" / "openai.yaml",
            SKILL_ROOT / "references" / "style-spec.md",
            SKILL_ROOT / "assets" / "style-reference.png",
            SKILL_ROOT / "scripts" / "normalize_cover.py",
            SKILL_ROOT / "LICENSE",
            SKILL_ROOT / "NOTICE",
        ]
        for path in required:
            self.assertTrue(path.is_file(), str(path))

    def test_contract_is_fixed(self) -> None:
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        style_text = (SKILL_ROOT / "references" / "style-spec.md").read_text(
            encoding="utf-8"
        )
        combined = skill_text + style_text
        self.assertIn("1923 x 818", combined)
        self.assertIn("left", combined.lower())
        self.assertIn("right", combined.lower())
        self.assertIn("MUST NOT offer style", skill_text)
        self.assertIn("NEVER pass the reference image", style_text)
        self.assertNotIn("attempt-04", skill_text)
        self.assertIn("attempt-03.md", skill_text)
        self.assertIn("absolute failure", style_text)
        self.assertIn("2 through 35 characters", skill_text)
        self.assertIn("exclusive directory semantics", skill_text)
        self.assertIn("outside the exact supplied title", style_text)
        self.assertIn("other than the installed imagegen skill", skill_text)
        self.assertIn("stop before creating OUTPUT_DIR", skill_text)

    def test_style_reference_dimensions(self) -> None:
        with Image.open(SKILL_ROOT / "assets" / "style-reference.png") as image:
            self.assertEqual(image.format, "PNG")
            self.assertEqual(image.size, (1923, 818))


if __name__ == "__main__":
    unittest.main()
