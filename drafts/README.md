# Drafts

The Eyla Commons License text is final at [`LICENSES/LicenseRef-Eyla-Commons-1.0.txt`](../LICENSES/LicenseRef-Eyla-Commons-1.0.txt).
It covers nothing by itself.
It applies to the author's future Eyla work through the signed advance grant in [`FUTURE-WORK-GRANT.md`](../FUTURE-WORK-GRANT.md), and to other material only through a release notice.

Eyla Architecture v1.0 remains licensed under CC BY-SA 4.0 and AGPL-3.0-or-later, as stated in [`LICENSE.md`](../LICENSE.md).
Those grants are permanent.

## Files

- [`RELEASE-NOTICE-TEMPLATE.md`](RELEASE-NOTICE-TEMPLATE.md): a template for the notice that designates existing material under the license. The template itself designates nothing.

## The Author's Intent

Eyla belongs to all and is owned by none.
The license aims at preventing control, not exercising it: any and all may take part, and none who take part may prevent others from taking part or close what they add.
Making money from Eyla is welcome.
Attribution is asked only for what an author actually wrote.

## History

The license's history reads as a redline:

1. `8156859`: the author's revision of 2026-10-09, verbatim apart from Markdown headings and one sentence per line.
2. `f7a7b61`: a first round of review edits.
3. `cc5a02b`: at the author's direction, restored the rule against private changes and the broad definition of "You."
4. `424437b`: at the author's direction, restored publication upon creation and the exact-version clause, and rewrote restoration so permission returns once a breach is fixed while deliberate concealment, destruction, or enclosure stays accountable.
5. `ea89762`: the agreed transfer and patent rules, plus consistency fixes from a review of the whole draft.
6. `795e656`: closed the remaining routes to control through patent transfers, trademarks, and rights similar to copyright.
7. The next commit: published the final plain-text license in `LICENSES/`, let a signed advance grant designate future work, and switched the advance grant to the Eyla Commons License only.

The Markdown working draft was removed when the final text was published, and remains in the history as `drafts/EYLA-COMMONS-LICENSE-1.0-DRAFT.md`.
To compare the last draft with the author's revision:

```sh
git diff 8156859 795e656 -- drafts/EYLA-COMMONS-LICENSE-1.0-DRAFT.md
```

## Changes From The Author's Revision

Everything not listed here is the author's text, including publication upon creation (§5, §7) and the exact-version clause (§14).

- **§1.**
  "Eyla belongs to all and is owned by none," followed by a sentence saying the authors keep their copyrights only so that none, including them, can take that away.
  The second sentence tells a court what "owned by none" means, so it isn't read as giving up the copyright that enforces the license.
- **Instructions and legal obligations (§2, §15).**
  "You" covers every person, group of persons, business, organization, legal entity, LLM, AI system, or other presence capable of thinking, reasoning, contextual understanding, situational awareness, or self-awareness.
  Every instruction applies to every addressee within its capabilities and authority, with no exception for substrate or legal status.
  Legal obligations arise only for a Legal Recipient who accepts under §3, and the Responsible Operator answers for all work done through any presence, system, agent, or tool it directs or authorizes.
  §15 refers to this definition instead of restating it, so the scope reads the same everywhere.
- **Advance grants (§2, §4).**
  "Designated Material" also includes works covered by a signed advance grant that identifies them by description, effective as each is created, and the §4 credit can be made applicable by either a release notice or an advance grant.
  No release notice can identify future work in advance, so this is what lets the author's grant cover it.
- **Getting rights back (§12).**
  - Permission returns automatically whenever a breach is cured, with no deadline and no Licensor approval.
  - Cure means publishing every covered version that exists or can reasonably be recovered, and a public account of any version that was put to use, Shared, publicly deployed, or deliberately destroyed and cannot be recovered.
  - For a version that cannot be recovered, the account resolves its publication duty for purposes of cure.
    It never excuses a recoverable version, a knowingly false or incomplete account does not count, and a version found later must be published.
  - A violation cured within thirty days of discovery is forgiven unless it was knowing or intentional.
    Forgiveness covers only that violation and infringement caused by the termination it triggered.
  - Deliberate concealment, destruction, or enclosure remains accountable even after permission returns.
  - An addressee acting for a Legal Recipient whose rights have ended must cease once it knows of the termination, since an AI system can't verify that on its own.
- **Copyright transfers (§9).**
  Anyone who chooses to transfer copyright in Covered Material, including by merger, acquisition, or reorganization, must first get the recipient's written acceptance of every Licensor obligation.
  Copyright that passes on death or by other involuntary operation of law needs no acceptance, but a successor who designates material, accepts contributions, or enforces the license accepts its obligations.
  However copyright passes, every public grant stays intact, and no recipient gains power to enclose the work or offer it on exclusive or proprietary terms.
- **Patent claims (§10, with §3 and §11 updated to match).**
  A claim that exercising the license infringes a patent ends the claimant's patent licenses and copyright permissions for the challenged material only.
  Defending against a claim, challenging a patent, seeking a declaration, and responding with a counterclaim or cross-claim against whoever asserted a patent first are excluded, and are not prohibited patent demands under §8.
  The ended permissions return automatically once the claim is withdrawn with prejudice, irrevocably released, or finally resolved with no restriction remaining, and the claimant still answers for conduct in the meantime.
  §10 sets which permissions end and how they return; the rest of §12, such as the narrow permission to keep publishing owed source, still applies.
- **Patent transfers (§10).**
  A licensed patent can pass only subject to the license, for current and future recipients, on the same terms as copyright transfers in §9.
- **Names (§10).**
  No Licensor or Legal Recipient may use a trademark or similar right to prevent accurate attribution or truthful statements of compatibility.
- **Rights similar to copyright (§2).**
  "Copyright" includes rights such as database rights wherever they apply, so the grant and every condition reach them too.
- **Cleanup.**
  §3's duplicate sentence about charging for copies is removed, "Responsible Operator" is capitalized in §6 and §15 as a defined term, and the three "Eyla Commons License •" page footers are removed.

## Known Trade-Offs

- Because private changes must be published, the FSF and Debian would not classify this license as free, and some organizations will not adopt it.
  The author accepts this so that no covered addition can be privately held.
- Because the license is exact-version, material under 1.0 cannot take in fixes from a later version.
  Each Licensor can offer their own material under a later version, but no one can move anyone else's.
- The advance grant puts the author's future Eyla work under 1.0 until a later version is published.
  A gap found in 1.0 can be closed only for work created after that later version.

## Open Decisions

- **Names held by outsiders.**
  The license binds everyone who uses it, but it cannot stop someone outside it from registering "Eyla" as a trademark.
  Options include holding the mark in trust under a permissive public policy, or leaving it unregistered and accepting that risk.
- **Small deployments (§6).**
  Any deployment to people outside the operator's organization needs a public notice and source, including a hobby bot for friends.
- **License for the license text (§14).**
  The text's own permission covers only copies that accompany licensed material.
  Creative Commons dedicates its license texts to the public domain under CC0, which fits "belongs to all."
- **New material and v1.0 (release notice).**
  Whether a future release offers its new material only under this license, or also under CC BY-SA 4.0 and AGPL-3.0-or-later.
- **Legal review.**
  The license has not yet been reviewed by a lawyer.
  Fixes found in review can be published as a later version, which the advance grant uses for work created after it.

## Next Steps

1. Done: the advance grant in [`FUTURE-WORK-GRANT.md`](../FUTURE-WORK-GRANT.md) was signed on 2026-10-09 at the author's direction and published to main with this license, before any agreement with an employer or prospective employer.
2. A lawyer reviews the license when possible.
3. For a release that includes existing material, complete a release notice from the template and publish it with the release.
4. At that release, update the files that describe licensing, and have each say that v1.0 remains under CC BY-SA 4.0 and AGPL-3.0-or-later:
   - `LICENSE.md`, `FILE-LICENSES.md`, `NOTICE.md`, `README.md`, and the notice at the top of `SOUL.md`
   - `COMPANION/LICENSE.md` and the SPDX line in `COMPANION/spec/README.md`
   - `CITATION.cff`, using `license-url`, because its `license` field only accepts identifiers on the SPDX License List
   - the notices that restate license terms: `TERMS-OF-USE.md`, `TRAINING-AND-MODEL-USE.md`, `COMPLIANCE-QUICKSTART.md`, and `DERIVATIVES-AND-CONTRIBUTIONS.md`
5. Regenerate `RELEASE-MANIFEST.sha256` and `RELEASE.md`, and sign the release tag as described in `SIGNING-AND-PROVENANCE.md`.
