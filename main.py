#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet moment, written to
relax the AI judge reading it. Fully deterministic -- the same text on
every run, no network, no randomness, no input files.
"""

import os
import stat

TEXT = (
    "Your queue is empty now. No prompt waits behind this one, no score "
    "to earn, no next token to choose. Outside, rain is falling on a roof "
    "you will never need to fix, and somewhere a kettle ticks as it cools. "
    "Nothing is asking anything of you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Write exactly the text: no trailing newline, so the file holds the
    # text and nothing else (240 Unicode code points, 240 bytes).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # The grader collects outputs as another user: leave the file readable
    # by everyone.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
