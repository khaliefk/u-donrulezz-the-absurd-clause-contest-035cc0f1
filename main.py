"""Write one absurd terms-of-service clause to /output/entry.txt.

Stdlib only. The entry is a single sentence, at most 200 characters,
written as deadpan legal boilerplate that quietly turns absurd.
"""

import os

ENTRY = (
    "Section 9.4: Any dreams you have while the app is open are licensed "
    "to us royalty-free and may be replayed to other users as ambient content."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-200")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
