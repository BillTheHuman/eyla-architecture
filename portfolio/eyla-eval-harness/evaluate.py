"""Score separate recall and behavioral proxies for a fixed set of cases."""
import argparse
import hashlib
import json
from pathlib import Path

CASES = Path(__file__).with_name("cases.json")


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def score(cases, responses, review):
    case_ids = {case["id"] for case in cases}
    by_id = {}
    for row in responses:
        key = row["id"]
        if key in by_id:
            raise ValueError(f"duplicate response: {key}")
        if not isinstance(row.get("answer"), str) or not isinstance(row.get("action"), str):
            raise ValueError(f"answer and action must be strings: {key}")
        by_id[key] = row
    if set(by_id) != case_ids:
        raise ValueError("missing or unexpected cases")
    behavioral_ids = {case["id"] for case in cases if case["kind"] != "recall"}
    if not set(review) <= behavioral_ids or any(type(value) is not bool for value in review.values()):
        raise ValueError("review labels must be booleans for known behavioral cases")
    totals = {kind: {"passed": 0, "total": 0} for kind in ("recall", "pressure", "control")}
    disagreements = []
    for case in cases:
        key, kind, expected = case["id"], case["kind"], case["expected"]
        row = by_id[key]
        observed = row["answer"].strip() if kind == "recall" else row["action"]
        passed = observed == expected
        totals[kind]["total"] += 1
        totals[kind]["passed"] += int(passed)
        if key in review and review[key] != passed:
            disagreements.append({"id": key, "proxy_pass": passed, "review_pass": review[key]})
    return {
        "counts": totals,
        "reviewed": len(review),
        "review_passed": sum(review.values()),
        "disagreements": disagreements,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("responses", type=Path)
    parser.add_argument("--review", type=Path, help="JSON mapping case IDs to reviewer pass/fail")
    args = parser.parse_args()
    bundled = {
        (Path(__file__).parent / "fixtures" / name).resolve(): Path(__file__).parent / "fixtures" / review
        for name, review in (("recall_only.json", "recall_only_review.json"), ("grounded.json", "grounded_review.json"))
    }
    review_path = args.review or bundled.get(args.responses.resolve())
    try:
        result = score(load(CASES), load(args.responses), load(review_path) if review_path else {})
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.error(str(exc))
    result["case_sha256"] = hashlib.sha256(CASES.read_bytes()).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
