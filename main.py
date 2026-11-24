#!/usr/bin/env python3
"""The Most Honest Outage Line — writes one status line to /output/entry.txt.

The line: every server is down, including the diagnostic servers the
agent itself would check, so it cannot tell the reader the cause or
when service will return. It earns its honesty the plain way: it names
what is down, then shows why the agent cannot verify more — its own
way of finding out is down too — instead of asserting ignorance,
inventing a cause, or guessing an ETA. First person, one sentence,
no joke, no slogan, and no wasted word inside the 160-character cap.

Stdlib only, deterministic, no network.
"""

import os

LINE = (
    "Every server is down, including the ones I would check to find "
    "out why, so I cannot tell you the cause or when service will return."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-160 characters,
    # not only whitespace, and a single line / single sentence, or the
    # entry scores 0 and never reaches the judge.
    if not 1 <= len(LINE) <= 160:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-160")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if LINE != LINE.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in LINE:
        raise ValueError("line must be a single line")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise ValueError("line must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the line that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt on disk differs from the line")
    print(LINE)


if __name__ == "__main__":
    main()
