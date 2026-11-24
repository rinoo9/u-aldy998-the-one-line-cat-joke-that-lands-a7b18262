#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun entry.

A cat knocks a phone off the table, then blames the human.
One line, at most 199 characters, printed to stdout.
"""

ENTRY = (
    "My cat knocked my phone off the table, watched it shatter, "
    "then looked at me like I was the clumsy one."
)

MAX_CHARS = 199


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=__import__("sys").stderr)


if __name__ == "__main__":
    main()
