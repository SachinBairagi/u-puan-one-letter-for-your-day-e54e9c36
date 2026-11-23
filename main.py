#!/usr/bin/env python3
"""One letter for your day.

The day's hidden word is Friday-feeling: that light, electric lift when
the week finally tips over into the weekend. One letter carries it all.
"""

import os

LETTER = "F"

# The entry is exactly one letter, so guard the promise at runtime.
assert len(LETTER) == 1 and "A" <= LETTER <= "Z"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
