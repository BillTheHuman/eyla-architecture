# Signing And Provenance

Copyright (c) 2026 William Francis Rineer III.

This file describes how to make a public release easier to verify.

The current bundle includes `RELEASE.md` and `RELEASE-MANIFEST.sha256`.

The release archive is intended to be published with a detached GPG signature
and checksum file.

Signing key fingerprint:

```text
5F2C D842 A6CE E22F 9F1E AB0B CAC2 7E2A 7304 C40E
```

Signing key:

```text
ed25519/CAC27E2A7304C40E
```

Note: confirm the public key UID before publishing any exported public key,
because OpenPGP public keys may contain an email address or other identifier.

## Current Provenance Files

- `RELEASE.md` records source hash, release notes, and important file hashes.
- `RELEASE-MANIFEST.sha256` records SHA-256 hashes for the publication bundle.
- `CHANGES-AND-REMOVALS.md` records review changes, removals, and publication
  edits.

## Recommended Signing Steps

For final publication, create a clean archive of the bundle and sign it with an
author-controlled key.

Release artifacts:

- `eyla-architecture-recursive-coherence-v1.tar.gz`
- `eyla-architecture-recursive-coherence-v1.tar.gz.sha256`
- `eyla-architecture-recursive-coherence-v1.tar.gz.asc`

Recommended git release steps:

```sh
git tag -s eyla-architecture-v1 -m "Eyla Architecture: Recursive Coherence v1"
git verify-tag eyla-architecture-v1
```

Recommended manifest check:

```sh
sha256sum -c RELEASE-MANIFEST.sha256
```

Recommended archive verification:

```sh
sha256sum -c eyla-architecture-recursive-coherence-v1.tar.gz.sha256
gpg --verify eyla-architecture-recursive-coherence-v1.tar.gz.asc eyla-architecture-recursive-coherence-v1.tar.gz
```

## Publication Record

For strongest provenance, publish:

- the release archive
- checksum file
- detached signature
- public signing key or fingerprint
- `RELEASE.md`
- `RELEASE-MANIFEST.sha256`
- date of publication
- repository commit or tag, if applicable

## Important Boundary

Do not publish private prompts, private OpenClaw state, secrets, credentials,
private user data, or unpublished private canon as part of provenance.
