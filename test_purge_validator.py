import unittest

from purge_validator import validate


class PurgeValidatorTest(unittest.TestCase):
    def test_global_purge_requires_approval(self):
        row = {"request_id": "p", "scope": "global", "approved": "no", "rollback_note": ""}
        self.assertIn("approval_required", validate(row))


if __name__ == "__main__":
    unittest.main()
