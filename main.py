#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun entry.

A cat sounds the 3 a.m. alarm, then falls asleep the moment the
human gets up to investigate.
One line, at most 199 characters, written to /output/entry.txt.
"""

import os
import sys

ENTRY = "My cat sat on my keyboard during a work call, typed a better email than I ever have, and then billed me in treats for the consulting."

MAX_CHARS = 199
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise SystemExit(f"{OUTPUT_PATH} does not match the entry")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=sys.stderr)


if __name__ == "__main__":
    main()
