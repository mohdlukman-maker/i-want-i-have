import re
import unittest
from pathlib import Path

HTML_PATH = Path(__file__).parents[1] / "app" / "index.html"


class PrototypeRepairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML_PATH.read_text(encoding="utf-8")

    def test_runtime_update_hook_does_not_read_missing_previous_state(self):
        self.assertNotIn("componentDidUpdate(_, prev)", self.html)
        self.assertNotIn("prev.screen", self.html)

    def test_notes_textarea_uses_a_real_value_binding(self):
        self.assertRegex(
            self.html,
            r'<textarea[^>]*value="\{\{ notes \}\}"[^>]*></textarea>',
        )
        self.assertNotIn(">{{ notes }}</textarea>", self.html)

    def test_participant_html_has_no_prototype_explanations(self):
        self.assertIn("<title>I Want, I Have</title>", self.html)
        lower = self.html.lower()
        for text in (
            "user-test prototype",
            "simulated",
            "no data saved",
            "tap to simulate",
            "iwih-sim-strip",
        ):
            self.assertNotIn(text, lower)

    def test_participant_view_has_no_explanatory_handoff_panel(self):
        self.assertNotIn('id="prototype-notes"', self.html)
        for text in (
            "Try the two journeys",
            "UX review — what I changed for the MVP",
            "Deferred to v2",
            "Engineering handoff notes",
            "say the word",
        ):
            self.assertNotIn(text, self.html)

    def test_mobile_layout_has_a_real_responsive_mode(self):
        self.assertIn('id="phone-frame"', self.html)
        self.assertIn("@media (max-width:760px)", self.html)
        self.assertIn("body.mobile", self.html)

    def test_document_has_basic_metadata_and_button_semantics(self):
        self.assertIn('<html lang="en">', self.html)
        self.assertRegex(self.html, r'<title>[^<]+</title>')
        for attrs in re.findall(r"<button\b([^>]*)>", self.html, re.I | re.S):
            self.assertRegex(attrs, r"\btype=", msg=f"button lacks type:{attrs[:120]}")

    def test_form_controls_have_accessible_names(self):
        for attrs in re.findall(r"<(?:input|textarea|select)\b([^>]*)>", self.html, re.I | re.S):
            self.assertRegex(
                attrs,
                r"\b(?:aria-label|aria-labelledby|id)=",
                msg=f"form control lacks accessible name:{attrs[:160]}",
            )

    def test_runtime_dependencies_are_local_and_integrity_pinned(self):
        import base64
        import hashlib
        vendor = HTML_PATH.parent / "vendor"
        expected = {
            "react.production.min.js": "DGyLxAyjq0f9SPpVevD6IgztCFlnMF6oW/XQGmfe+IsZ8TqEiDrcHkMLKI6fiB/Z",
            "react-dom.production.min.js": "gTGxhz21lVGYNMcdJOyq01Edg0jhn/c22nsx0kyqP0TxaV5WVdsSH1fSDUf5YJj1",
        }
        self.assertLess(self.html.index("window.__resources"), self.html.index("./support.js"))
        for filename, wanted in expected.items():
            path = vendor / filename
            self.assertTrue(path.is_file(), msg=f"missing local runtime: {filename}")
            got = base64.b64encode(hashlib.sha384(path.read_bytes()).digest()).decode()
            self.assertEqual(got, wanted)
            self.assertIn("./vendor/" + filename, self.html)

    def test_unimplemented_actions_are_not_presented_as_working(self):
        for label in ("Pause", "Edit", "Cancel", "Save for later", "+ Add item manually", "Dismiss"):
            pattern = rf'<button\b(?=[^>]*\bdisabled\b)[^>]*>\s*{re.escape(label)}\s*</button>'
            self.assertRegex(self.html, pattern, msg=f"{label} should be visibly disabled")


if __name__ == "__main__":
    unittest.main(verbosity=2)
