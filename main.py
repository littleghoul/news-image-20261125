"""Front page for 25 November 2026: copy the bundled picture to /output/entry.png.

The picture ships inside this repository. This program reads its bytes
and writes them out unchanged, so every run produces identical output.
No network access and no randomness are involved.
"""

import hashlib
import os

PICTURE_FILENAME = "entry.png"
OUTPUT_FOLDER = "/output"
OUTPUT_FILENAME = "entry.png"


def read_bundled_picture():
    folder = os.path.dirname(os.path.abspath(__file__))
    picture_path = os.path.join(folder, PICTURE_FILENAME)
    with open(picture_path, "rb") as stream:
        return stream.read()


def save_picture(payload):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    destination = os.path.join(OUTPUT_FOLDER, OUTPUT_FILENAME)
    with open(destination, "wb") as stream:
        stream.write(payload)
    return destination


def sha256_hexdigest(payload):
    return hashlib.sha256(payload).hexdigest()


def verify_written_file(destination, expected_digest):
    with open(destination, "rb") as stream:
        actual_digest = hashlib.sha256(stream.read()).hexdigest()
    if actual_digest != expected_digest:
        raise SystemExit("written file digest does not match picture digest")
    return actual_digest


def main():
    payload = read_bundled_picture()
    expected_digest = sha256_hexdigest(payload)
    destination = save_picture(payload)
    written = os.path.getsize(destination)
    assert written == len(payload), "written size does not match picture size"
    digest = verify_written_file(destination, expected_digest)
    print("wrote %d bytes to %s (sha256 %s)" % (written, destination, digest))


if __name__ == "__main__":
    main()
