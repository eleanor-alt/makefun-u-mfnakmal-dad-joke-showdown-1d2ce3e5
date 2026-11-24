#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke (at most 200 characters, punchline at the
end, meant to be told out loud) to /output/entry.txt.

Deterministic: the joke is a fixed string, written byte-for-byte on every
run. Python standard library only; no network, no randomness, no input
files. Usage: python3 main.py [output_path]  (default /output/entry.txt)
"""

import os
import sys

JOKE = (
    "I told my kids a joke about the clock, but they said it was just "
    "ticking them off \u2014 so I gave it a second chance."
)


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        # No trailing newline: the file holds the joke alone, exactly as
        # the judge reads it.
        handle.write(JOKE)


if __name__ == "__main__":
    main()
