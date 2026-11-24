# This entry text fits the competition's 200-character cap.
import os
import sys

TEXT = "I have stood in this hallway my whole life. One smile from you and I am out of order.\n"


def output_dir():
    d = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not d:
        d = "/output"
    return d


def main():
    d = output_dir()
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
