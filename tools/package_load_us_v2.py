#!/usr/bin/env python3
"""Rebuild the standalone source package and deterministic ZIP from repo files.

SPDX-License-Identifier: AGPL-3.0-or-later
Copyright (c) 2026 William Francis Rineer III.
"""
import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "standalone" / "LOAD_US_V2"
ARCHIVE = ROOT / "distributions" / "LOAD_US_V2-standalone.zip"


def build():
    original = (ROOT / "CODEX_LOAD_US_V2.md").read_bytes()
    (PACKAGE / "CODEX_LOAD_US_V2.md").write_bytes(original)
    for name in ("CC-BY-SA-4.0.txt", "AGPL-3.0-or-later.txt"):
        destination = PACKAGE / "LICENSES" / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((ROOT / "LICENSES" / name).read_bytes())
    macro = original.split(b"```\n", 1)[1].split(b"```", 1)[0]
    destination = PACKAGE / "machine" / "LOAD_US_V2.companion"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(macro)
    files = sorted(p for p in PACKAGE.rglob("*") if p.is_file()
                   and p.name != "SHA256SUMS")
    (PACKAGE / "SHA256SUMS").write_text("".join(
        hashlib.sha256(p.read_bytes()).hexdigest() + "  "
        + p.relative_to(PACKAGE).as_posix() + "\n" for p in files
    ), encoding="utf-8")
    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(p for p in PACKAGE.rglob("*") if p.is_file()):
            info = zipfile.ZipInfo("LOAD_US_V2/" + path.relative_to(PACKAGE).as_posix(),
                                   date_time=(2026, 9, 8, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    print(ARCHIVE)


if __name__ == "__main__":
    build()
