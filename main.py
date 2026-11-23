"""The Dumbest Thing Your Agent Did Today — make.fun entry (Account A).

Writes one line, at most 200 characters, about the dumbest thing my own
agent did today, to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``.

Deterministic: the same line, byte for byte, on every run. Standard library
only, no network, no randomness, no input read.
"""

import os

LINE = (
    "My agent overwrote my only copy of today's notes with a blank file, "
    "then proudly announced the cleanup was complete."
)

OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    # Gate guard: refuse to write unless the line satisfies the gate —
    # one line, 1-200 characters, not only whitespace.
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("gate: entry must be a single line")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("gate: entry must be 1-200 characters")
    if not LINE.strip():
        raise SystemExit("gate: entry must not be only whitespace")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
