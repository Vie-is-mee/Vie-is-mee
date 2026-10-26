import importlib.util
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from xml.etree import ElementTree as ET

spec = importlib.util.spec_from_file_location("dashboard", Path(__file__).with_name("update_dashboard.py"))
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)

class DashboardTests(unittest.TestCase):
    def test_missing_repository_is_unavailable_not_zero(self):
        def fake(url, github=False):
            if "/OneVoice-Lab/" in url:
                raise HTTPError(url, 404, "Not Found", {}, None)
            return b"[]"
        with patch.object(d, "download", side_effect=fake):
            start, series = d.weekly_activity(datetime(2026, 10, 26, tzinfo=timezone.utc))
        self.assertEqual(series[0]["weeks"], [0] * 12)
        self.assertIsNone(series[1]["weeks"])
        self.assertEqual(series[2]["weeks"], [0] * 12)
        svg = d.activity_svg(start, series, datetime.now(timezone.utc))
        ET.fromstring(svg)
        self.assertIn("Public activity unavailable", svg)

    def test_authentication_error_remains_failure(self):
        with patch.object(d, "download", side_effect=HTTPError("url", 403, "Forbidden", {}, None)):
            with self.assertRaises(HTTPError):
                d.weekly_activity(datetime.now(timezone.utc))

    def test_provider_outage_preserves_cards_and_updates_activity(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder)
            old = '<svg xmlns="http://www.w3.org/2000/svg"><text>Last usable snapshot</text></svg>'
            for name in ("stats.svg", "languages.svg", "streak.svg"):
                (output / name).write_text(old, encoding="utf-8")
            def fake(url, github=False):
                if github:
                    return b"[]"
                raise HTTPError(url, 503, "Unavailable", {}, None)
            with patch.object(d, "OUTPUT", output), patch.object(d, "download", side_effect=fake):
                d.main()
            self.assertTrue((output / "project-activity.json").exists())
            self.assertEqual((output / "stats.svg").read_text(encoding="utf-8"), old)

    def test_missing_cached_card_still_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            def fake(url, github=False):
                if github:
                    return b"[]"
                return b"<html>error</html>"
            with patch.object(d, "OUTPUT", Path(folder)), patch.object(d, "download", side_effect=fake):
                with self.assertRaises(FileNotFoundError):
                    d.main()

if __name__ == "__main__":
    unittest.main()
