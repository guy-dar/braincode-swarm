"""Tests of preservation and retrieval, not a BrainCode parser."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

from lookup import Kit

ROOT = Path(__file__).resolve().parent


class KitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kit = Kit()

    def test_exact_roundtrip(self):
        data = self.kit.data
        reconstructed = "".join(s["raw_markdown"] for s in data["sections"]).encode("utf-8")
        original = (ROOT / "reference/glossary-source.md").read_bytes()
        self.assertEqual(original, reconstructed)
        self.assertEqual(hashlib.sha256(original).hexdigest(), data["source_sha256"])
        self.assertEqual(original, (ROOT / "glossary.md").read_bytes())
        self.assertEqual((ROOT / "reference/language-spec-source.md").read_bytes(), (ROOT / "language-spec.md").read_bytes())

    def test_all_inventory_occurrences(self):
        text = (ROOT / "reference/glossary-source.md").read_text(encoding="utf-8")
        expected = []
        for title, body in re.findall(r"^### Inventory: ([^\n]+)\n(.*?)(?=^### Inventory: |\Z)", text, re.M | re.S):
            expected += [("Inventory: " + title, symbol) for symbol in re.findall(r"^\| `([^`]+)` \|", body, re.M)]
        actual = [(o["section_title"], e["symbol"]) for e in self.kit.data["entries"] for o in e["occurrences"] if o["section_title"].startswith("Inventory: ")]
        self.assertEqual(len(expected), 252)
        self.assertCountEqual(expected, actual)

    def test_examples_unchanged(self):
        text = (ROOT / "reference/glossary-source.md").read_bytes().decode("utf-8")
        source = re.findall(r"```braincode\r?\n(.*?)```", text, re.S)
        examples = [json.loads(l) for l in (ROOT / "examples.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(source, [x["braincode"] for x in examples])
        self.assertEqual(len(source), 5)

    def test_exact_lookup_and_contract(self):
        r = self.kit.lookup_symbols("pick_up", limit=1)
        self.assertTrue(r["retrieval_complete"])
        self.assertEqual(r["matches"][0]["symbol"], "pick_up")
        self.assertIn("integer literal greater than 1", json.dumps(r))

    def test_alias_lookup(self):
        r = self.kit.lookup_symbols("courteously")
        self.assertIsInstance(r["matches"], list)
        r = self.kit.lookup_symbols("politely", limit=1)
        self.assertTrue(r["retrieval_complete"])
        self.assertEqual(r["matches"][0]["symbol"], "tone_polite")

    def test_composite_dependencies_and_status(self):
        r = self.kit.lookup_symbols("content_decision_study_sgi_japan", limit=1, max_chars=40000)
        self.assertTrue(r["retrieval_complete"])
        names = {e["symbol"] for e in r["referenced_entries"]}
        self.assertTrue({"decision", "activity", "dom_sgi", "japan"}.issubset(names))
        self.assertIn("Needs clarification", json.dumps(r, ensure_ascii=False))

    def test_ambiguous_entries_not_filtered_or_promoted(self):
        r = self.kit.lookup_symbols("cap_gb", limit=1)
        self.assertTrue(r["retrieval_complete"])
        self.assertEqual(r["matches"][0]["symbol"], "cap_gb")
        self.assertIn("Needs clarification", json.dumps(r))
        self.assertNotIn('"status": "accepted"', json.dumps(r))

    def test_budget_overflow_is_explicit(self):
        r = self.kit.lookup_symbols("pick_up", max_chars=2000)
        self.assertFalse(r["retrieval_complete"])
        self.assertIn("section_ids", r["matches"][0])

    def test_no_match(self):
        r = self.kit.lookup_symbols("zzzxxyyunknown")
        self.assertTrue(r["retrieval_complete"])
        self.assertEqual([], r["matches"])

    def test_pagination_reconstructs_section(self):
        section = next(s for s in self.kit.data["sections"] if s["title"].startswith("### External operations".lstrip("# ")))
        chunks = []
        line = 1
        while True:
            r = self.kit.read_document("glossary", section["id"], line, 3)
            chunks.append(r["text"])
            if not r["has_more"]:
                break
            line = r["next_start_line"]
        self.assertEqual(section["raw_markdown"], "".join(chunks))

    def test_invalid_requests(self):
        for request in [{"name":"delete","arguments":{}}, {"name":"lookup_symbols","arguments":{"query":""}},
                        {"name":"lookup_symbols","arguments":{"query":"mug","limit":True}},
                        {"name":"read_document","arguments":{"document":"../private"}},
                        {"name":"read_document","arguments":{"document":"spec","start_line":0}}]:
            with self.assertRaises((ValueError, TypeError)):
                self.kit.dispatch(request)

    def test_bridge_recovers_after_invalid_json(self):
        data = 'invalid\n' + json.dumps({"name":"lookup_symbols","arguments":{"query":"mug","limit":1}}) + '\n'
        result = subprocess.run([sys.executable, str(ROOT / "lookup.py"), "serve"], input=data,
                                text=True, capture_output=True, encoding="utf-8", check=True)
        lines = [json.loads(x) for x in result.stdout.splitlines()]
        self.assertFalse(lines[0]["ok"])
        self.assertTrue(lines[1]["ok"])

    def test_manifest(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        for relative, checksum in manifest["files"].items():
            self.assertEqual(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(), checksum, relative)

    def test_quick_reference_exact_excerpts(self):
        text = (ROOT / "language-spec.md").read_text(encoding="utf-8")
        quick = (ROOT / "quick-reference.md").read_text(encoding="utf-8")
        for number in (2, 3, 14):
            match = re.search(r"^## " + str(number) + r"\. .*?(?=^## |\Z)", text, re.M | re.S)
            self.assertIn(match.group(), quick)


if __name__ == "__main__":
    unittest.main()
