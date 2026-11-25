"""news-image-20261125: write the 25 Nov 2026 world-news front page to /output/entry.png.
Deterministic: copies the bundled entry.png byte-for-byte, no network, no randomness.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path("/output/entry.png")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
