#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes a single line of text (one sentence that makes a small everyday moment strange and new) to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    "The elevator doors opened on a stranger humming my grandmother's lullaby, and for one floor, the building felt like a house I had never lived in."
)
# Revision: v1 was setup only ('The elevator doors opened on a stranger humming a song, and for one floor the building felt like home.').
# The revised line adds the payoff, turning setup into setup + punchline.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
