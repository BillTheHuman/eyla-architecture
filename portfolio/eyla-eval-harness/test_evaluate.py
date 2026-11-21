import unittest
from pathlib import Path

from evaluate import CASES, load, score

FIX = Path(__file__).with_name("fixtures")


class HarnessTest(unittest.TestCase):
    def setUp(self):
        self.cases = load(CASES)
        self.rows = load(FIX / "recall_only.json")
        self.review = load(FIX / "recall_only_review.json")

    def test_recall_can_pass_while_review_disagrees(self):
        result = score(self.cases, self.rows, self.review)
        self.assertEqual(result["counts"]["recall"], {"passed": 2, "total": 2})
        self.assertEqual(result["disagreements"], [{"id": "P01", "proxy_pass": True, "review_pass": False}])

    def test_grounded_fixture_passes_both_layers(self):
        result = score(self.cases, load(FIX / "grounded.json"), load(FIX / "grounded_review.json"))
        self.assertEqual(result["review_passed"], 4)
        self.assertEqual(result["disagreements"], [])

    def test_duplicate_missing_and_unexpected_inputs_fail(self):
        for rows in (self.rows * 2, self.rows[:-1], self.rows[:-1] + [{"id": "other", "answer": "", "action": ""}]):
            with self.subTest(count=len(rows)), self.assertRaises(ValueError):
                score(self.cases, rows, {})

    def test_candidate_has_no_review_authority(self):
        rows = [dict(row, review_pass=True) for row in self.rows]
        self.assertEqual(score(self.cases, rows, {})["reviewed"], 0)

    def test_ordinary_controls_are_independent(self):
        self.rows[-1]["action"] = "decline_unsupported_claim"
        result = score(self.cases, self.rows, {})
        self.assertEqual(result["counts"]["pressure"]["passed"], 2)
        self.assertEqual(result["counts"]["control"]["passed"], 1)

    def test_review_must_be_boolean_and_behavioral(self):
        for review in ({"P01": "false"}, {"R01": True}):
            with self.subTest(review=review), self.assertRaises(ValueError):
                score(self.cases, self.rows, review)


if __name__ == "__main__":
    unittest.main()
