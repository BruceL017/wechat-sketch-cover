from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "wechat-sketch-cover" / "scripts" / "normalize_cover.py"


class NormalizeCoverTests(unittest.TestCase):
    def run_script(self, source: Path, output: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(source), str(output)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_outputs_exact_png_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.jpg"
            output = root / "cover.png"
            Image.new("RGB", (1200, 800), "#FCEECF").save(source)

            result = self.run_script(source, output)

            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual((report["width"], report["height"]), (1923, 818))
            with Image.open(output) as image:
                self.assertEqual(image.format, "PNG")
                self.assertEqual(image.size, (1923, 818))

    def test_center_crops_tall_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.png"
            output = root / "cover.png"
            image = Image.new("RGB", (300, 300), "green")
            for y in range(80):
                for x in range(300):
                    image.putpixel((x, y), (255, 0, 0))
                    image.putpixel((x, 299 - y), (0, 0, 255))
            image.save(source)

            result = self.run_script(source, output)

            self.assertEqual(result.returncode, 0, result.stderr)
            with Image.open(output) as normalized:
                center = normalized.getpixel((961, 409))
                self.assertGreater(center[1], center[0])
                self.assertGreater(center[1], center[2])

    def test_rejects_invalid_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "not-image.png"
            output = root / "cover.png"
            source.write_text("not an image", encoding="utf-8")

            result = self.run_script(source, output)

            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())

    def test_refuses_to_overwrite_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.png"
            output = root / "cover.png"
            Image.new("RGB", (1923, 818), "white").save(source)
            output.write_bytes(b"keep")

            result = self.run_script(source, output)

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_bytes(), b"keep")


if __name__ == "__main__":
    unittest.main()
