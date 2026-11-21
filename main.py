#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

Deterministic: the same fixed text is written on every run.
"""

import os

JOKE = (
    "My AI agent demoed the feature so confidently I nodded along "
    "\u2014 I'd never seen it before either."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip() or "\n" in JOKE:
        raise ValueError("joke must be one non-blank line of 1-280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
