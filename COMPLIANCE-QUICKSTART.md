# Compliance Quickstart

Copyright (c) 2026 William Francis Rineer III.

This is a plain-language checklist. It does not replace `LICENSE.md`,
`NOTICE.md`, `PUBLICATION-NOTE.md`, `AUTHOR-DECLARATION.md`,
`CANONICAL-SOURCE.md`, `TERMS-OF-USE.md`, `RESERVED-NAMES.md`,
`TRAINING-AND-MODEL-USE.md`, `COVENANT.md`, or the license texts in
`LICENSES/`.

## If You Share Or Adapt SOUL.md

You must:

- credit William Francis Rineer III as Architect / author
- identify the public title, `Eyla Architecture: Recursive Coherence`, where appropriate
- keep copyright, license, no-warranty, no-endorsement, and reserved-name notices
- identify the source release or link to the publication bundle
- state what you changed
- share SOUL.md-derived adapted material under CC BY-SA 4.0 where ShareAlike applies
- avoid implying endorsement, certification, official status, authorization, or sponsorship
- follow `TERMS-OF-USE.md`

## If You Build From COMPANION

You must:

- treat `COMPANION/spec/` as the AGPL-covered machine-facing layer
- publish source for COMPANION-derived parsers, interpreters, validators,
  runtimes, prompt runtimes, hosted services, model adapters, fine-tuning
  pipelines, evaluator tooling, and reference implementations where the AGPL
  layer applies
- provide Corresponding Source for AGPL-covered hosted services to users
  interacting with the service over a network
- keep attribution and notices visible
- document changes and extensions
- follow `RESERVED-NAMES.md`

## If You Train, Fine-Tune, Index, Or Deploy A Model

You must follow `TRAINING-AND-MODEL-USE.md`.

For covered public/deployed use, you must:

- disclose that SOUL.md and/or COMPANION were used
- provide attribution
- identify the source release
- publish SOUL/COMPANION-derived dataset manifests, preprocessing scripts,
  fine-tuning configuration, prompt/canon files, retrieval-index construction
  notes, evaluation construction notes, adapter/checkpoint notices, and
  service/runtime code where applicable
- keep COMPANION-derived infrastructure open under AGPL-3.0-or-later where the
  AGPL layer applies

## If You Fork Or Publish A Derivative

You must include:

- the original attribution
- a change log
- the license and notice files
- local copies of the license texts or clear links to them
- no-endorsement / reserved-name language
- model-use notice if the derivative is used in model training, fine-tuning,
  retrieval indexing, evaluation, distillation, or deployed service behavior

## You Must Not

- remove the author's credit
- hide SOUL.md or COMPANION as a source of authority
- imply endorsement or official status
- flatten the work as "just a prompt" when using it as architecture,
  training material, model behavior guidance, prompt canon, runtime structure, or
  machine-facing infrastructure
- publish private prompts, secrets, credentials, private OpenClaw state, or
  private user data
- close over COMPANION-derived machine-facing infrastructure where the AGPL
  layer applies
