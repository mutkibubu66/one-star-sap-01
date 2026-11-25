#!/usr/bin/env python3
"""Write one one-line 1-star review from a houseplant about its human owner.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

def get_line() -> str:
    """Return the entry line: the grievance, then the single-star verdict."""
    return (
        "One star. My human waters me like a rumour — a splash on Mondays, "
        "then nothing till I droop. The window I was promised faces a brick "
        "wall, and the 'plant food' is old coffee. I photosynthesise out of "
        "spite now. Would not recommend this owner to other ferns."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-279 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 279:
        raise ValueError("entry line must be 1-279 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    assert "\n" not in LINE  # one line: no embedded newline may reach the file
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
