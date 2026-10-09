# File License Map

Copyright (c) 2026 William Francis Rineer III.

This map identifies the intended license layer for each file or file family in
this publication bundle.

This file does not replace `LICENSE.md`, `NOTICE.md`, or the license texts in
`LICENSES/`.

## CC BY-SA 4.0 Layer

The following files are covered by Creative Commons Attribution-ShareAlike 4.0
International unless a more specific notice inside the file says otherwise:

- `SOUL.md`
- `CODEX_LOAD_US_V2.md` (prose and readable documentation; machine-facing use follows the existing COMPANION layer)
- `README.md`
- `PUBLICATION-NOTE.md`
- `AUTHOR-DECLARATION.md`
- `CANONICAL-SOURCE.md`
- `CITATION.cff`
- `GLOSSARY.md`
- `APPENDIX-INFRASTRUCTURE.md`
- `APPENDIX-MASKS-PUBLIC.md`
- `COVENANT.md`
- `NOTICE.md`
- `TRAINING-AND-MODEL-USE.md`
- `COMPLIANCE-QUICKSTART.md`
- `DERIVATIVES-AND-CONTRIBUTIONS.md`
- `RELEASE.md`
- `CHANGES-AND-REMOVALS.md`
- `COMPANION/README.md`
- `COMPANION/COMPANION.md`
- `COMPANION/LICENSE.md`
- `COMPANION/NOTICE.md`
SPDX expression:

`CC-BY-SA-4.0`

## AGPL-3.0-or-later Layer

The following files and derived machine-facing implementations are covered by
GNU Affero General Public License v3.0 or later:

- `COMPANION/spec/companion.ebnf`
- `COMPANION/spec/README.md`
- `COMPANION/spec/glyphs.csv`
- `COMPANION/spec/operations.csv`
- `COMPANION/spec/examples.companion`
- COMPANION-derived parsers, interpreters, validators, runtimes, hosted
  services, prompt runtimes, model adapters, fine-tuning pipelines, evaluator
  tooling, seed corpora, and reference implementations where the AGPL layer
  applies

SPDX expression:

`AGPL-3.0-or-later`

## Standalone LOAD_US_V2 Distribution

- `standalone/LOAD_US_V2/CODEX_LOAD_US_V2.md`, `README.md`, `EXTENDING.md`,
  `LICENSE.md`, and `NOTICE.md`: CC-BY-SA-4.0 prose/documentation.
- `standalone/LOAD_US_V2/machine/LOAD_US_V2.companion` and
  `standalone/LOAD_US_V2/examples/workshop-check.json`: AGPL-3.0-or-later.
- Embedded macro command forms in the original artifact are additionally
  offered under AGPL-3.0-or-later for machine-facing reuse.
- `tools/package_load_us_v2.py`: AGPL-3.0-or-later.
- `standalone/LOAD_US_V2/LICENSES/`: unmodified standard license texts.
- `distributions/LOAD_US_V2-standalone.zip`: the same per-file licenses as its
  source directory; see the included LICENSE.md and NOTICE.md.
- `standalone/LOAD_US_V2/SHA256SUMS`: generated integrity metadata.

## Standard License Texts

The following files are local copies of standard license texts:

- `LICENSES/CC-BY-SA-4.0.txt`
- `LICENSES/AGPL-3.0-or-later.txt`

## Reserved Rights

All rights not expressly granted by the applicable license layer and publication
notices are reserved.

No endorsement, sponsorship, certification, official-status, trademark,
personality, publicity, or impersonation rights are granted.
