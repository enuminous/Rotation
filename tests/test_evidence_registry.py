import unittest
from scripts.validate_evidence import validate


class TestRegistry(unittest.TestCase):
    def test_references_and_statuses(self):
        r=validate()
        self.assertEqual(r["status"],"PASS_SCHEMA_AND_CITATIONS")
        self.assertGreaterEqual(r["claims"],20)
        self.assertGreaterEqual(r["sources"],15)


if __name__ == "__main__":
    unittest.main()
