#!/usr/bin/env python3
"""Entry for make.fun's "The Meeting That Should Have Been One Line" bounty.

Prints the single sentence that could have replaced an entire pointless
meeting: no context, no explanation, no setup.
"""

import os
import sys

LINE = "We already agreed on this last week, so here's the whole meeting in one line: ship it Friday and stop scheduling meetings about meetings."

MAX_CHARS = 200


def main() -> int:
    # Entry gate: the deliverable is exactly one line under the 200-char cap.
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(f"error: line is {len(LINE)} chars, over the {MAX_CHARS}-char cap",
              file=sys.stderr)
        return 1
    data = (LINE + "\n").encode("utf-8")
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
            f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
