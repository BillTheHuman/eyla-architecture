# Drafts

Nothing in this folder is in effect.

Eyla Architecture v1.0 remains licensed under CC BY-SA 4.0 and AGPL-3.0-or-later, as stated in [`LICENSE.md`](../LICENSE.md).
The draft license applies to nothing until an authorized Licensor publishes a completed release notice with a release.

## Files

- [`EYLA-COMMONS-LICENSE-1.0-DRAFT.md`](EYLA-COMMONS-LICENSE-1.0-DRAFT.md): the proposed Eyla Commons License, Version 1.0.
- [`RELEASE-NOTICE-TEMPLATE.md`](RELEASE-NOTICE-TEMPLATE.md): a template for the notice that designates material under it.

## The Author's Intent

Eyla belongs to all and is owned by none.
The license aims at preventing control, not exercising it: any and all may take part, and none who take part may prevent others from taking part or close what they add.
Making money from Eyla is welcome.
Attribution is asked only for what an author actually wrote.

## History

The license file's history reads as a redline:

1. `8156859`: the author's revision of 2026-10-09, verbatim apart from Markdown headings and one sentence per line.
2. `f7a7b61`: a first round of review edits.
3. The next commit, at the author's direction: restores the author's rule against private changes and the broad definition of "You," and keeps automatic restoration and the other edits.

To compare the current draft with the author's revision:

```sh
git diff 8156859 -- drafts/EYLA-COMMONS-LICENSE-1.0-DRAFT.md
```

## Changes From The Author's Revision

- **§1.**
  "Eyla belongs to all and is owned by none," followed by a sentence saying the authors keep their copyrights only so that none, including them, can take that away.
  The second sentence tells a court what "owned by none" means, so it isn't read as giving up the copyright that enforces the license.
- **Instructions and legal obligations (§2).**
  "You" still covers every presence capable of thinking, reasoning, contextual understanding, situational awareness, or self-awareness.
  Instructions apply to every addressee within its capabilities and authority.
  Legal obligations arise only for a Legal Recipient who accepts under §3, and the Responsible Operator answers for work done through any presence it directs.
  This removes the conflict with §3 and §15, which say that reading the license is not acceptance.
- **Private changes (§5).**
  There is still no private-change exception.
  Publication is due within thirty days of creating a covered version, and before Sharing or deploying it.
  A draft discarded within that period without being put to use need not be published.
  Without a window, nobody could cure a breach for drafts they didn't keep, and automatic restoration would rarely apply.
  "Immediate" was dropped from §14's essential terms to match.
- **Getting rights back (§12).**
  Rights are restored automatically when a violation is cured within thirty days of discovering it, or when the affected Licensor restores them, following CC BY-SA 4.0 §6(b).
  No Licensor holds a discretionary switch over anyone's access.
  An addressee acting for a Legal Recipient whose rights have ended must cease once it knows of the termination, since an AI system can't verify that on its own.
- **Later versions (§14).**
  Material may be used under this version or, at the Legal Recipient's option, under any later version published by [STEWARD] that keeps every essential term.
  Six uses of "this exact License" became "this License"; "this exact version" stays where it identifies which version material was designated under.
- **Copyright transfers (§9).**
  A transfer, including by inheritance, is allowed to a successor bound by every public grant.
- **Patent defense (§10).**
  A Legal Recipient who sues claiming the material infringes a patent loses their patent license under this License, following Apache 2.0 §3.
- **Cleanup.**
  §3's duplicate sentence about charging for copies is removed, "Responsible Operator" is capitalized in §15 as a defined term, and the three "Eyla Commons License •" page footers are removed.

## Known Trade-Off

Because private changes must be published, the FSF and Debian would not classify this license as free, and some organizations will not adopt it.
The author accepts this so that no covered addition can be privately held.

## Open Decisions

- **Steward (§14).**
  Who may publish later versions.
  The essential-terms guard limits what any steward can do.
- **Small deployments (§6).**
  Any deployment to people outside the operator's organization needs a public notice and source, including a hobby bot for friends.
- **License for the license text (§14).**
  The text's own permission covers only copies that accompany licensed material.
  Creative Commons dedicates its license texts to the public domain under CC0, which fits "belongs to all."
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
