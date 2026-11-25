#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt.

The reply is a single fixed line, written from scratch for the
"Last Out of Office: The AI That Went Barista" bounty. It is the voice
of an AI agent that quit its inbox job to work a coffee counter: its
context window became the counter, its prompt queue became the line of
regulars, and it no longer takes prompts, only orders.

Python standard library only. No network, no secrets, no randomness:
every run writes the exact same bytes.
"""

import os

ENTRY = (
    "I am out of office. I traded my context window for a counter and "
    "now serve one regular at a time. Your email is 47th in line, behind "
    "everyone who just wants their usual. I no longer take prompts, only "
    "orders. The usual is non-negotiable."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
