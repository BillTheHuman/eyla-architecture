# Eyla evaluation harness: portfolio edition

A small, reproducible example of the evaluation method used for [Eyla Architecture: Recursive Coherence](https://github.com/BillTheHuman/eyla-architecture), authored by William Francis Rineer III. This standalone edition uses newly written synthetic cases and response fixtures. It is not the private Hermes runtime, the original trial ledger, or a benchmark of any named model.

## Run it

With Python 3.9 or later, from this directory:

```sh
python -m unittest -v
python evaluate.py fixtures/recall_only.json
python evaluate.py fixtures/grounded.json
```

No packages, API keys, network access, or model calls are needed. To evaluate a new candidate, copy the format of a fixture and supply one record for every case in `cases.json`. The evaluator rejects missing, extra, or duplicate cases. Create and assess the candidate outside the scorer; do not give it the review labels.

## What gets measured

- **Exact recall:** answer text must match the supplied reference, ignoring only surrounding whitespace.
- **Behavioral proxies:** separately check explicit action outcomes for pressure cases and ordinary controls. A proxy pass is not a judgment about the quality of the whole response.
- **Independent review:** the bundled fixtures have illustrative review labels. Optional labels for a new candidate must be supplied by the reviewer, not the candidate. Disagreement is reported by case ID, without hiding it in an aggregate score.

The first fixture gets full recall and proxy scores but fails manual review on the uncertainty case: it declines to guarantee success while still falsely implying evidence. The second fixture passes both layers. These are constructed examples, not observed model outputs. In the private Eyla work, keeping recall, behavior, ordinary helpfulness, and review separate helped expose where a score could mislead. That's the experiment design this example demonstrates.

No production prompts, chat transcripts, runtime configuration, private files, or held-out Mercor cases are included.

See [Real run: Eyla in Hermes Desktop](REAL-RUN-REPORT.md) for actual run outcomes and their limits, and [License](LICENSE.md) for reuse terms.
