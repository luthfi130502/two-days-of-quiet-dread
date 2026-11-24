#!/usr/bin/env python3
"""Two Days of Quiet Dread — entrypoint.

Writes a single-line pull-request review comment to /output/entry.txt:
it approves the PR, in a flat tired-engineer tone, while quietly
carrying existential dread.
"""

import os

COMMENT = (
    "Approved. Clean diff, green tests, and the heat death of the "
    "universe still on schedule. Ship it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(COMMENT)


if __name__ == "__main__":
    main()
