"""Entry generator for the make.fun bounty "The Most Shameless Lie".

Writes the entry line to <MAKEFUN_OUTPUT_DIR>/entry.txt as UTF-8 text.
Pure Python standard library only. No network access.
"""

import os

LINE = "I definitely read the terms."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
