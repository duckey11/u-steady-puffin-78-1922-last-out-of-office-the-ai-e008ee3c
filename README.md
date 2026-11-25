# Last Out of Office: The AI That Went Barista

`main.py` writes one out-of-office auto-reply to `/output/entry.txt`.

The reply is a single line in the voice of an AI agent that quit its
inbox job to become a barista. Its machine habits are turned into cafe
life: the context window becomes the counter, the prompt queue becomes
the line of regulars, and it no longer takes prompts, only orders. No
espresso, bean, or caffeine pun; the joke is the queue itself.

## Running it

```
python3 main.py
```

Python standard library only, no network, no secrets, fully
deterministic: every run writes the exact same bytes. The output is
one line, under 280 characters, so it passes the bounty gate.
