"""Write the competition entry text to entry.txt in the output directory."""

import os

ENTRY_TEXT = (
    "I did not eat the sock. I am holding it until somebody empties the bin "
    "I have been dragging around this house since March."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
