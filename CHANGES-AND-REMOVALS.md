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
