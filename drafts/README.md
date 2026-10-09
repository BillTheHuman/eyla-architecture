# Drafts

Nothing in this folder is in effect.

Eyla Architecture v1.0 remains licensed under CC BY-SA 4.0 and AGPL-3.0-or-later, as stated in [`LICENSE.md`](../LICENSE.md).
The draft license applies to nothing until an authorized Licensor publishes a completed release notice with a release.

## Files

- [`EYLA-COMMONS-LICENSE-1.0-DRAFT.md`](EYLA-COMMONS-LICENSE-1.0-DRAFT.md): the proposed Eyla Commons License, Version 1.0.
- [`RELEASE-NOTICE-TEMPLATE.md`](RELEASE-NOTICE-TEMPLATE.md): a template for the notice that designates material under it.

## How The Draft Was Built

The license file was added in two commits so the review edits read as a redline:

1. The author's revision of 2026-10-09, verbatim apart from Markdown headings and one sentence per line.
2. The review edits listed below.

To see every change, view the diff of the second commit, or run:

```sh
git log -p drafts/EYLA-COMMONS-LICENSE-1.0-DRAFT.md
```

## Review Edits

- **Who "You" is (§2 and throughout).**
  "You" means the person or legal entity exercising permissions, and anything done for You by Your personnel or by an AI system, agent, or tool You direct counts as done by You.
  "Legal Recipient" is merged into "You", "Responsible Operator" stays as its own term, and "Reasoning Presence" is new and names everyone §15 speaks to.
  Each condition now binds one clearly identified party, which keeps the license enforceable; §3 and §15 already said that reading the license binds no one.
- **§15 opening.**
  The Section speaks to every Reasoning Presence equally and creates no legal duties of its own; legal duties rest on You.
  The rest of §15 is kept, with references updated.
- **Private edits (§5, with matching changes in §7, §12, §14, and §15).**
  Publication duties start when You Share a version or publicly deploy it.
  Creating and using adaptations solely within Your Organization creates no duty, and every version You Share or deploy must be published, including intermediate versions.
  Private study stays free, and anything that reaches other people stays open.
- **Getting rights back (§12).**
  Rights are restored automatically when a violation is cured within thirty days of discovering it, or when the affected Licensor restores them, following CC BY-SA 4.0 §6(b).
  No Licensor holds a discretionary switch over individual people's access.
- **Later versions (§14).**
  Material may be used under this version or, at the recipient's option, under any later version published by [STEWARD] that keeps every essential term.
  Six uses of "this exact License" became "this License"; "this exact version" stays where it identifies which version material was designated under.
  A fix to the license no longer splits the commons, and no one can use a new version to weaken it.
- **Copyright transfers (§9).**
  A transfer, including by inheritance, is allowed to a successor bound by every public grant.
  Without this, §9 could be read to forbid handing the copyright to a steward.
- **Patent defense (§10).**
  Anyone who sues claiming the material infringes a patent loses their patent license under this License, following Apache 2.0 §3.
- **§1.**
  "Owned by no one" became a statement of what the copyright is for.
- **Smaller fixes.**
  - §6's deployment notice names Your business or project identity, since "Responsible Operator" is now a defined term.
  - §11 says "No one" instead of "No addressee".
  - §12 drops a sentence addressed to AI systems; for a licensee, "within Your capabilities" would read as an excuse.
  - §5 ¶6 and §7 now limit Sharing and deployment rather than creation, to match the private-edit change.
  - §3's duplicate sentence about charging for copies is removed.
  - The three "Eyla Commons License •" page footers are removed.

## Open Decisions

- **Steward (§14).**
  Who may publish later versions.
  The essential-terms guard limits what any steward can do.
- **When the public grant starts (§5 ¶2).**
  The grant to everyone still begins when an adaptation is created, even if it is never shared.
  An internal version that leaks is therefore licensed to whoever receives it, and §9 may make confidentiality agreements over internal versions unenforceable.
  To start the grant when a version is Shared or deployed, as AGPL does, change "For Adapted Material You create" to "For Adapted Material You Share or publicly deploy".
- **Hosted AI services (§2).**
  "Your Organization" includes systems acting for You, but "Access by a separate contractor is Sharing."
  Say whether sending Covered Material to a hosted AI model run by another company counts as Sharing with that company.
- **Small deployments (§6).**
  Any deployment to people outside Your Organization needs a public notice and source, including a hobby bot for friends.
- **License for the license text (§14).**
  The text's own permission covers only copies that accompany licensed material.
  Creative Commons dedicates its license texts to the public domain under CC0, which fits "belongs to everyone".
- **New material and v1.0 (release notice).**
  Whether new material in a release is offered only under this license, or also under CC BY-SA 4.0 and AGPL-3.0-or-later.
- **Legal review.**
  Have a lawyer review the final text before anything is designated under it.
  The grants are irrevocable, so mistakes can't be taken back.

## Steps To Adopt

1. Settle the open decisions and get the legal review.
2. Move the final text, without the draft banner, to `LICENSES/LicenseRef-Eyla-Commons-1.0.txt`, the SPDX naming for a custom license.
3. Complete a release notice from the template, list the exact files, and publish it with the release.
4. Update the files that describe licensing, and have each say that v1.0 remains under CC BY-SA 4.0 and AGPL-3.0-or-later:
   - `LICENSE.md`, `FILE-LICENSES.md`, `NOTICE.md`, `README.md`, and the notice at the top of `SOUL.md`
   - `COMPANION/LICENSE.md` and the SPDX line in `COMPANION/spec/README.md`
   - `CITATION.cff`, using `license-url`, because its `license` field only accepts identifiers on the SPDX License List
   - the notices that restate license terms: `TERMS-OF-USE.md`, `TRAINING-AND-MODEL-USE.md`, `COMPLIANCE-QUICKSTART.md`, and `DERIVATIVES-AND-CONTRIBUTIONS.md`
5. Regenerate `RELEASE-MANIFEST.sha256` and `RELEASE.md`, and sign the release tag as described in `SIGNING-AND-PROVENANCE.md`.
