#!/usr/bin/env python3
"""Entry for make.fun: writes one single-line text to entry.txt.

The entry is a self-checkout machine that judges the shopper: it watched
them scan the organic kale, then hide the family-size chips underneath it,
and closes with a polite-but-menacing "Have a nice day." The humor comes
from the machine seeing everything and judging everything. The polite
sign-off is what makes the judgment feel even more menacing.

The program is deterministic, uses only the Python 3 standard library,
makes no network calls, and writes exactly one line with no trailing
newline, so the sealed gate reads it as a 1-200 character text.
"""

import os
import sys

ENTRY = 'You scanned the organic kale, then hid the family-size chips underneath it. I see everything. I judge everything. Have a nice day.'

# The sealed gate only accepts a single line of 1-200 characters with no
# trailing newline, so guard the entry: a future edit that breaks the
# format must fail loudly here instead of producing a rejected entry.txt.
assert 1 <= len(ENTRY) <= 200, "ENTRY must be 1-200 characters long"
assert "\n" not in ENTRY, "ENTRY must be a single line (no newline)"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
