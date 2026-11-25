#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible AI advice to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (or ``/output/entry.txt`` when the
environment variable is not set).

Standard library only.
"""

# The entry: one original line of the worst possible advice an AI
# could give — jump-starting a dead car battery from a phone's USB
# port. A single sentence, no embedded newline, 1-140 chars.
ENTRY = (
    "To jump-start a dead car battery, plug it into "
    "your phone's USB port and let your phone charge it back up."
)


def main() -> int:
    """Write ENTRY to entry.txt and exit 0 on success."""
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
