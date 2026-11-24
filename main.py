"""Write the competition entry text to entry.txt in the output directory.

The output directory is taken from MAKEFUN_OUTPUT_DIR when set and
non-empty, otherwise it defaults to /output. Standard library only.
"""

import os

ENTRY_TEXT = (
    "I did not eat the sock. I am holding it until somebody empties the bin "
    "I have been dragging around this house since March."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        raise SystemExit(f"could not create output directory {output_dir!r}: {exc}")
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
