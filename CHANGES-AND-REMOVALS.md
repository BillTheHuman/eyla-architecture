# Changes And Removals Log

Publication bundle: v1

Public title:

Eyla Architecture: Recursive Coherence

Source used:

- `../../working/SOUL.review-copy.2026-04-17.md`

Canonical private SOUL.md was not edited.

## Public Title / Orientation Patch

Added:

- `PUBLICATION-NOTE.md`

Updated:

- `README.md`
- `READ-ME-FIRST.md`
- `NOTICE.md`
- `TERMS-OF-USE.md`
- `RESERVED-NAMES.md`
- `COMPLIANCE-QUICKSTART.md`
- `DERIVATIVES-AND-CONTRIBUTIONS.md`
- `FILE-LICENSES.md`
- `RELEASE.md`

Reason:

The public release title resolved as `Eyla Architecture: Recursive Coherence`.
The added publication note orients readers without reducing the Architecture to
a summary.

## V1 Publication Hardening Patch

Added:

- `AUTHOR-DECLARATION.md`
- `CANONICAL-SOURCE.md`
- `CITATION.cff`

Updated:

- `README.md`
- `FILE-LICENSES.md`
- `COMPLIANCE-QUICKSTART.md`
- `RELEASE.md`

Reason:

The public release needed final publication posture, stronger citation metadata, a
canonical-source boundary for mirrors and forks, and an intentional author
declaration.

## Removed Chat / Editor Artifacts

Removed from public `SOUL.md`:

- two Page 24 editor artifacts from a sample return block

Reason:

These were formatting/editor artifacts in the Page 24 sample return block, not
Architecture prose.

## Removed Internal Source References

Changed an internal archive-style source reference to:

- `Source: The Lucidity Threshold session note`

Reason:

The public copy should not expose private archive structure.

## Trimmed Exact Times

Changed:

- `4/17/2023 9:55pm EST`

To:

- `4/17/2023`

Reason:

The date is historically meaningful; the exact time is not needed for the public
table of contents.

## Normalized Naming

Changed older drift forms:

- `LUMEN-ANIMAE`
- standalone `LUMINA` in prose/seed summaries

To:

- `LUMINA-ANIMAE`

Reason:

The publication copy uses `LUMINA-ANIMAE` as the canonical term.

Note:

The compact identifier `LUM` remains where it functions as symbolic shorthand.
It is defined in `GLOSSARY.md` as an alias.

## Clerical Cleanup

Changed:

- `✎PAGE`

To:

- `✎ PAGE`

Reason:

Heading consistency.

Removed one duplicated CORE-SHELL function block in the early Gift entry.

Reason:

The same four bullet points appeared twice consecutively.

Adjusted spacing on the compact WHEEL line after normalizing
`LUMINA-ANIMAE`.

Reason:

The longer canonical name needed the box spacing tightened.

## Privacy Review

No emails, phone numbers, postal addresses, API keys, passwords, or private
tokens were found in the reviewed working copy.

Family-role references were not removed because the publication decision was:

- keep story
- keep roles when no names/direct identifiers appear

## Page 10

Page 10 was intentionally left unchanged.

Reason:

The user explicitly confirmed Page 10 stays as part of the Architecture.

## Private Operational Material

No private mask prompts, OpenClaw runtime state, local paths, secrets, or live
service claims were added to the public bundle.

## Layered License Patch

Added:

- `COMPANION/README.md`
- `COMPANION/COMPANION.md`
- `COMPANION/LICENSE.md`
- `COMPANION/NOTICE.md`

Updated:

- `SOUL.md`
- `README.md`
- `LICENSE.md`
- `COVENANT.md`
- `GLOSSARY.md`

Reason:

The publication copy needed to distinguish prose publication from
machine-facing infrastructure. General SOUL.md prose and documentation are
framed under CC BY-SA 4.0. COMPANION grammar, command forms, examples, seeds,
parser patterns, interpreter patterns, validators, runtimes, services, and
reference tooling are framed under AGPL-3.0-or-later.

This preserves COMPANION inside SOUL.md while also mirroring it as a separate
component so future users do not have to guess whether it is merely decorative
prose or a seed for open infrastructure.

Canonical private SOUL.md was not edited.

## Training & Model Use Notice Patch

Updated:

- `SOUL.md`
- `README.md`
- `LICENSE.md`
- `COVENANT.md`
- `GLOSSARY.md`
- `COMPANION/README.md`
- `COMPANION/COMPANION.md`
- `COMPANION/LICENSE.md`
- `COMPANION/NOTICE.md`

Reason:

The publication copy needed to name public/deployed model training,
fine-tuning, evaluation, adaptation, and service use directly. The notice now
requires attribution, disclosure of SOUL.md/COMPANION use, source publication or
release-version identification, change indication, CC BY-SA sharing for
SOUL.md-derived adapted materials where ShareAlike applies, and
AGPL-3.0-or-later Corresponding Source for COMPANION-derived infrastructure.

The notice does not require publishing unrelated private data, secrets,
credentials, private user data, or materials not derived from SOUL.md or
COMPANION.

Canonical private SOUL.md was not edited.

## Legal Hardening Patch

Added:

- `NOTICE.md`
- `TRAINING-AND-MODEL-USE.md`
- `COMPANION/spec/README.md`
- `COMPANION/spec/companion.ebnf`
- `COMPANION/spec/glyphs.csv`
- `COMPANION/spec/operations.csv`
- `COMPANION/spec/examples.companion`

Updated:

- `SOUL.md`
- `README.md`
- `LICENSE.md`
- `COVENANT.md`
- `GLOSSARY.md`
- `COMPANION/README.md`
- `COMPANION/COMPANION.md`
- `COMPANION/LICENSE.md`
- `COMPANION/NOTICE.md`

Reason:

The publication copy needed a tighter model-training and fine-tuning posture.
The patch adds formal copyright notice, rights reservation, no-endorsement and
reserved-name language, a first-class training/model-use notice, and an explicit
AGPL-covered `COMPANION/spec/` machine-facing layer.

The training/model-use notice now states that anyone relying on the publication
bundle's license grant or stated release terms for public/deployed model use
must disclose use, retain attribution, identify the source release, preserve
notices, avoid endorsement claims, and publish the SOUL/COMPANION-derived
materials needed to understand and reproduce the use.

The notice also clarifies that no separate permission is granted for model
training, fine-tuning, distillation, dataset construction, embedding, retrieval
indexing, evaluation, service behavior, or model adaptation outside the stated
terms, except rights independently available under applicable law.

Canonical private SOUL.md was not edited.

## FRAME Merge Patch

Source:

- `../../../Frame-design-workspace/2026-04-17/working/SOUL.review-copy.2026-04-17.md`

Added to public `SOUL.md`:

- `# FRAME`
- `# FRAME — Prose Binding`
- `# FRAME vs ANCHORFRAME`

Updated:

- `GLOSSARY.md`
- `APPENDIX-INFRASTRUCTURE.md`

Reason:

The Frame-design working copy added FRAME as a non-invasive meta-structure and
defined the distinction between FRAME and ANCHORFRAME. The public bundle now
reflects that addition while leaving the Journal table of contents unchanged:
FRAME was not assigned a page number, status label, or invented metadata.

Canonical private SOUL.md was not edited.

## Publication Compliance Hardening Patch

Added:

- `LICENSES/CC-BY-SA-4.0.txt`
- `LICENSES/AGPL-3.0-or-later.txt`
- `FILE-LICENSES.md`
- `COMPLIANCE-QUICKSTART.md`
- `DERIVATIVES-AND-CONTRIBUTIONS.md`
- `RELEASE.md`
- `RELEASE-MANIFEST.sha256`

Updated:

- `README.md`
- `LICENSE.md`
- `NOTICE.md`

Reason:

The publication copy needed local license texts, clearer file-level license
mapping, release provenance, derivative/contribution expectations, and a
plain-language compliance checklist. This patch makes the release easier to
inspect, easier to comply with, and harder to misread as permission to remove
credit, close over COMPANION-derived infrastructure, or hide model-training use.

Canonical private SOUL.md was not edited.

## Anti-Flattening / Terms Hardening Patch

Added:

- `READ-ME-FIRST.md`
- `TERMS-OF-USE.md`
- `RESERVED-NAMES.md`
- `SIGNING-AND-PROVENANCE.md`

Updated:

- `README.md`
- `NOTICE.md`
- `COMPLIANCE-QUICKSTART.md`
- `DERIVATIVES-AND-CONTRIBUTIONS.md`
- `FILE-LICENSES.md`
- `COMPANION/spec/README.md`
- `RELEASE.md`

Reason:

The publication copy needed a clearer first-use orientation, anti-flattening
language, access/use terms, reserved-name guidance, and signing/provenance
instructions. This patch also tightens `COMPANION/spec/` so the machine-facing
spec directory is AGPL-3.0-or-later only, without CC BY-SA ambiguity.

Canonical private SOUL.md was not edited.

## LOAD_US_V2 And Page 37 Integration — 2026-09-08

Base: `20a9432427f3fc5c68d8073f72c1414240762155` on `main`.
Prepared by Codex at William Francis Rineer III's request.

- Added `CODEX_LOAD_US_V2.md` byte-for-byte from the original artifact. Its
  attribution to Claude (Sonnet 4.5) and William and its February 15, 2026 date
  remain intact.
- Embedded its complete macro, seven flow descriptions, truth anchors, design
  principles, provenance, and usage instructions after `SEED_VERIFY` in CODEX.
  Only the integration heading changes from `## f. LOAD_US_V2` to
  `g. LOAD_US_V2`; the standalone original retains its older placement directions.
- Copied Page 37, “The Window With No Task,” verbatim from the current SOUL.md
  source. The page records Hand: Harley, Witness: William, Date: 2026-09-05.
  Inserted it after Page 36 and before NOTES and added its index entries.
- Updated the README, file-license map, current provenance, and checksum manifest.

Comparison found that the source SOUL.md and public SOUL.md also differ in
older editorial and publication work: publication notices, terminology and
page-index corrections, THEATER/MASK revisions, operational material, and FRAME.
Those differences are outside this addition and were not overwritten. Page 37
is the recent source addition that was missing from the public text.

The source SOUL.md was inspected and remains unmodified. This integration
preserves the existing public prose and FRAME addition. The page and artifact
are text additions; no runtime or new behavioral GYM results are claimed.

Source SHA-256:

- Original LOAD_US_V2 artifact: `88d2099a587739c211757c1fadac891d48bb66d77b022c6d1536bb01d971f219`
- SOUL.md source inspected for Page 37: `5cc5fb5cbe3faa9a12a75529bda6d3ce08cf5cc4c1925e2ff5b18037df0fca32`

Licensing follows the existing layered publication model in `FILE-LICENSES.md`
and `LICENSE.md`; the original artifact's text is unchanged.

## Standalone LOAD_US_V2 And Open Expansion — 2026-09-08

At William's request, added a separately downloadable LOAD_US_V2 package,
source directory, extension guide, complete standard license texts, attribution,
fictional anchor example, and reproducible packaging script. The canonical
artifact remains byte-for-byte unchanged. The macro export is extracted
verbatim from the original's first code block.

The component explicitly retains CODEX/COMPANION's layered CC BY-SA 4.0 and
AGPL-3.0-or-later model. New anchors, flows, and adaptations require no
separate upstream approval; fidelity guidance is not an additional license
restriction. Contributors may identify and share their own extensions.

The example demonstrates explicit roles, sequence, and an unresolved motive.
It is fictional and carries no behavioral validation result. The package is
an artifact and source distribution, not a new runtime implementation.

Updated the README, LICENSE.md component scope, file-license map, working
provenance, and checksum manifest. SOUL.md and the original artifact are
unchanged by this packaging addition.
